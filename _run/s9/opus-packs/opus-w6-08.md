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

## GROUP: _overhaul2/lake/cases/Lange v. California.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "34524a60334f5fcc", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Lange v. California"}, "payload": {"all": [{"cite": "594 U.S. 295", "page": "295", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "594"}], "display": "594 U.S. 295", "official": {"cite": "594 U.S. 295", "page": "295", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "594"}, "official_selection_present": true, "record_id": "Lange v. California"}}
{"assertion_id": "8b8f8add2fc00062", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op1a", "record_id": "Lange v. California"}, "payload": {"fragment": "#:~:text=A%20great%20many%20misdemeanor%20pursuits", "page": null, "pin_id": "pin-op1a", "pinpoint_status": "slip-only", "quote": "A great many misdemeanor pursuits involve exigencies allowing warrantless entry. But whether a given one does so turns on the particular facts of the case.", "quote_fidelity": "matched", "record_id": "Lange v. California", "star_marker": null}}
{"assertion_id": "90ff27a56ba35271", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op1", "record_id": "Lange v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op1", "pinpoint_status": "slip-only", "quote": "--- # Lange v. California *594 U.S. 295 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A California highway patrol officer began following Lange, who was playing loud music and honking, and turned on his overhead lights to signal a stop when Lange was about a hundred feet from home. Rather than stopping, Lange drove into his attached garage. The officer followed him in, questioned him, observed signs of intoxication, and a later blood test showed Lange was over the legal limit. He was charged with the misdemeanor of driving under the influence. ## Issue Whether the pursuit of a fleeing misdemeanor suspect categorically (always) qualifies as an exigent circumstance justifying a warrantless entry into the home. ## Rule No — there is no categorical rule; exigency is judged case by case.", "quote_fidelity": "mismatch", "record_id": "Lange v. California", "star_marker": null}}
{"assertion_id": "cc555689b096a5fc", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Lange v. California"}, "payload": {"as_of_content": "2021-06-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Lange v. California", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Lefkowitz v. Turley.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Lefkowitz v. Turley"
type: case
citation: "414 U.S. 70 (1973)"
parallel_cite: "94 S. Ct. 316; 38 L. Ed. 2d 274"
neutral_cite: 1973 U.S. LEXIS 132
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-11-19
docket: 72-331
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-11-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Lefkowitz v. Turley
  varies_by_point: false
  scope_note: "Good law; extends the Garrity/Gardner principle to independent contractors and fixes the rule that the State must grant immunity rather than demand a waiver."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108882/lefkowitz-v-turley/"
  cluster_id: 108882
  opinion_id: 108882
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Key — Progeny / Refinement"
related: ["[[Garrity v. New Jersey]]", "[[Gardner v. Broderick]]", "[[Kalkines v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "public-employee", "garrity", "immunity", "contractors"]
holding: "A State may not compel a person (employee or contractor) to choose between waiving Fifth Amendment immunity and losing state employment or contracts; it may compel testimony about official functions only by granting use-and-derivative-use immunity, never by insisting on a waiver."
lake:
  record_id: Lefkowitz v. Turley
  status: verified
  projected_at: 2026-07-06
---

# Lefkowitz v. Turley

*414 U.S. 70 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New York statutes provided that any person doing business with the State who, when called before a grand jury, refused to waive immunity or to answer questions about his state contracts would have his existing contracts cancelled and be disqualified from public contracting for five years. Two architects who performed state work were subpoenaed before a grand jury, refused to waive immunity, and sued to enjoin the statutes as violating the Fifth Amendment. A three-judge district court held the statutes unconstitutional, and the New York Attorney General appealed.

## Issue
Whether a State may, consistent with the Fifth Amendment, require a contractor (or public employee) either to waive his privilege against self-incrimination and testify or to forfeit his existing state contracts and be disqualified from future state work.

## Rule
The State may compel duty-related answers, but only under immunity: "[G]iven adequate immunity, the State may plainly insist that employees either answer questions under oath about the performance of their job or suffer the loss of employment." — 414 U.S. at 84. ^pin-84

What it may not do is demand a waiver: "[T]he State may not insist that appellees waive their Fifth Amendment privilege against self-incrimination and consent to the use of the fruits of the interrogation in any later proceedings brought against them. Rather, the State must recognize what our cases hold: that answers elicited upon the threat of the loss of employment are compelled and inadmissible in evidence. Hence, if answers are to be required in such circumstances States must offer to the witness whatever immunity is required to supplant the privilege and may not insist that the employee or contractor waive such immunity." — *Id.* at 84–85. ^pin-84a

## Application
The New York statutes confronted the architects with the very choice the Fifth Amendment forbids: waive immunity (exposing their testimony and its fruits to criminal use) or lose their contracts and be barred from state work for five years. The State could have compelled their testimony about their state contracts by granting use-and-derivative-use immunity, but instead it demanded a waiver of the privilege as the price of keeping their livelihood. Because answers extracted under that threat are compelled and inadmissible, conditioning contracts on a waiver violated the Fifth Amendment.

## Conclusion
The statutes were unconstitutional, and the judgment was affirmed. *Lefkowitz* confirms that a government may compel testimony about official functions only by supplying immunity, and may never penalize a person for refusing to surrender the privilege itself.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Lefkowitz* is good law; it extends [[Garrity v. New Jersey]] and [[Gardner v. Broderick]] beyond employees to independent contractors and states the controlling immunity-not-waiver rule that the federal [[Kalkines v. United States]] warning implements.

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Key — Progeny / Refinement*

## Sources
- *Lefkowitz v. Turley*, 414 U.S. 70 (1973) — https://www.courtlistener.com/opinion/108882/lefkowitz-v-turley/ — pinpoints: 84–85.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a489f3ff174941a7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Lefkowitz v. Turley"}, "payload": {"all": [{"cite": "414 U.S. 70", "page": "70", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "414"}, {"cite": "94 S. Ct. 316", "page": "316", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "38 L. Ed. 2d 274", "page": "274", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "38"}, {"cite": "1973 U.S. LEXIS 132", "page": "132", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1973"}], "display": "414 U.S. 70", "official": {"cite": "414 U.S. 70", "page": "70", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "414"}, "official_selection_present": true, "record_id": "Lefkowitz v. Turley"}}
{"assertion_id": "4b5353171ffde692", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-84", "record_id": "Lefkowitz v. Turley"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-84", "pinpoint_status": "slip-only", "quote": "--- # Lefkowitz v. Turley *414 U.S. 70 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New York statutes provided that any person doing business with the State who, when called before a grand jury, refused to waive immunity or to answer questions about his state contracts would have his existing contracts cancelled and be disqualified from public contracting for five years. Two architects who performed state work were subpoenaed before a grand jury, refused to waive immunity, and sued to enjoin the statutes as violating the Fifth Amendment. A three-judge district court held the statutes unconstitutional, and the New York Attorney General appealed. ## Issue Whether a State may, consistent with the Fifth Amendment, require a contractor (or public employee) either to waive his privilege against self-incrimination and testify or to forfeit his existing state contracts and be disqualified from future state work. ## Rule The State may compel duty-related answers, but only under immunity:", "quote_fidelity": "mismatch", "record_id": "Lefkowitz v. Turley", "star_marker": null}}
{"assertion_id": "d65dc23e0494e262", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-84a", "record_id": "Lefkowitz v. Turley"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-84a", "pinpoint_status": "slip-only", "quote": "[T]he State may not insist that appellees waive their Fifth Amendment privilege against self-incrimination and consent to the use of the fruits of the interrogation in any later proceedings brought against them. Rather, the State must recognize what our cases hold: that answers elicited upon the threat of the loss of employment are compelled and inadmissible in evidence. Hence, if answers are to be required in such circumstances States must offer to the witness whatever immunity is required to supplant the privilege and may not insist that the employee or contractor waive such immunity.", "quote_fidelity": "mismatch", "record_id": "Lefkowitz v. Turley", "star_marker": null}}
{"assertion_id": "5b0cd7b13667a7ab", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Lefkowitz v. Turley"}, "payload": {"as_of_content": "1973-11-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Lefkowitz v. Turley", "scope_note": "Good law; extends the Garrity/Gardner principle to independent contractors and fixes the rule that the State must grant immunity rather than demand a waiver.", "varies_by_point": false}}
```

### lake record — Lefkowitz v. Turley

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lefkowitz v. Turley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lefkowitz v. Turley",
    "case_name_short": "Lefkowitz",
    "case_name_full": "LEFKOWITZ, ATTORNEY GENERAL OF NEW YORK, Et Al. v. TURLEY Et Al.",
    "input_case_name": "Lefkowitz v. Turley",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-11-19",
    "year": 1973,
    "docket": "72-331",
    "cluster_id": 108882,
    "lead_opinion_id": 108882,
    "sibling_ids": [
      108882
    ],
    "absolute_url": "/opinion/108882/lefkowitz-v-turley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8991929,
        "score": 20,
        "case_name": "Lefkowitz v. Turley"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "414 U.S. 70",
      "volume": "414",
      "reporter": "U.S.",
      "page": "70",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 316",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "316",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 274",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "274",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 132",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "414 U.S. 70",
        "volume": "414",
        "reporter": "U.S.",
        "page": "70",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 316",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "316",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 274",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "274",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 132",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "414 U.S. 70",
    "official_selection": {
      "court_class": "scotus",
      "selected": "414 U.S. 70",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-84",
      "page": null,
      "quote": "--- # Lefkowitz v. Turley *414 U.S. 70 (1973)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New York statutes provided that any person doing business with the State who, when called before a grand jury, refused to waive immunity or to answer questions about his state contracts would have his existing contracts cancelled and be disqualified from public contracting for five years. Two architects who performed state work were subpoenaed before a grand jury, refused to waive immunity, and sued to enjoin the statutes as violating the Fifth Amendment. A three-judge district court held the statutes unconstitutional, and the New York Attorney General appealed. ## Issue Whether a State may, consistent with the Fifth Amendment, require a contractor (or public employee) either to waive his privilege against self-incrimination and testify or to forfeit his existing state contracts and be disqualified from future state work. ## Rule The State may compel duty-related answers, but only under immunity:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-84a",
      "page": null,
      "quote": "[T]he State may not insist that appellees waive their Fifth Amendment privilege against self-incrimination and consent to the use of the fruits of the interrogation in any later proceedings brought against them. Rather, the State must recognize what our cases hold: that answers elicited upon the threat of the loss of employment are compelled and inadmissible in evidence. Hence, if answers are to be required in such circumstances States must offer to the witness whatever immunity is required to supplant the privilege and may not insist that the employee or contractor waive such immunity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-11-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Lefkowitz v. Turley",
    "varies_by_point": false,
    "scope_note": "Good law; extends the Garrity/Gardner principle to independent contractors and fixes the rule that the State must grant immunity rather than demand a waiver.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Gideon",
          "cluster_id": 4632199,
          "cite": [
            "2019 Ohio 2482",
            "130 N.E.3d 357"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Heffington v. Moser",
          "cluster_id": 4531554,
          "cite": [
            "192 A.3d 900",
            "238 Md. App. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gregory Wayne Powell",
          "cluster_id": 4348676,
          "cite": [
            "161 Idaho 774",
            "391 P.3d 659",
            "2017 WL 587254",
            "2017 Ida. App. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People in re L.K",
          "cluster_id": 4247631,
          "cite": [
            "2016 COA 112",
            "410 P.3d 664"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Von Behren",
          "cluster_id": 3202148,
          "cite": [
            "822 F.3d 1139",
            "2016 U.S. App. LEXIS 8567",
            "2016 WL 2641270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jesus J. Pena v. State",
          "cluster_id": 3199326,
          "cite": [
            "508 S.W.3d 599",
            "2016 WL 1702219",
            "2016 Tex. App. LEXIS 4360"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turner",
          "cluster_id": 2723970,
          "cite": [
            "300 Kan. 662",
            "333 P.3d 155",
            "2014 Kan. LEXIS 499"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Brent Vreeland",
          "cluster_id": 803377,
          "cite": [
            "684 F.3d 653",
            "2012 WL 2477578",
            "2012 U.S. App. LEXIS 13307"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex Parte Dangelo",
          "cluster_id": 2537141,
          "cite": [
            "339 S.W.3d 143",
            "2010 WL 5118650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Spielbauer v. County of Santa Clara",
          "cluster_id": 5608087,
          "cite": [
            "45 Cal. 4th 704",
            "199 P.3d 1125",
            "88 Cal. Rptr. 3d 590",
            "28 I.E.R. Cas. (BNA) 1254",
            "2009 Cal. LEXIS 1010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Aguilera v. Baca",
          "cluster_id": 1390016,
          "cite": [
            "510 F.3d 1161",
            "27 I.E.R. Cas. (BNA) 31",
            "2007 U.S. App. LEXIS 29804",
            "2007 WL 4531990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cleveland Board of Education v. Loudermill",
          "cluster_id": 111372,
          "cite": [
            "84 L. Ed. 2d 494",
            "105 S. Ct. 1487",
            "470 U.S. 532",
            "1985 U.S. LEXIS 68",
            "1 I.E.R. Cas. (BNA) 424",
            "53 U.S.L.W. 4306",
            "118 L.R.R.M. (BNA) 3041"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Elstad",
          "cluster_id": 111364,
          "cite": [
            "84 L. Ed. 2d 222",
            "105 S. Ct. 1285",
            "470 U.S. 298",
            "1985 U.S. LEXIS 60",
            "53 U.S.L.W. 4244"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Palmigiano",
          "cluster_id": 109429,
          "cite": [
            "47 L. Ed. 2d 810",
            "96 S. Ct. 1551",
            "425 U.S. 308",
            "1976 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arnett v. Kennedy",
          "cluster_id": 109008,
          "cite": [
            "40 L. Ed. 2d 15",
            "94 S. Ct. 1633",
            "416 U.S. 134",
            "1974 U.S. LEXIS 125"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
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
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKune v. Lile",
          "cluster_id": 121146,
          "cite": [
            "153 L. Ed. 2d 47",
            "122 S. Ct. 2017",
            "536 U.S. 24",
            "2002 U.S. LEXIS 4206"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
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
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maness v. Meyers",
          "cluster_id": 109130,
          "cite": [
            "42 L. Ed. 2d 574",
            "95 S. Ct. 584",
            "419 U.S. 449",
            "1975 U.S. LEXIS 20"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Comm'rs, Wabaunsee Cty. v. Umbehr",
          "cluster_id": 118059,
          "cite": [
            "135 L. Ed. 2d 843",
            "116 S. Ct. 2342",
            "518 U.S. 668",
            "1996 U.S. LEXIS 4262",
            "10 Fla. L. Weekly Fed. S 124",
            "64 U.S.L.W. 4682",
            "96 Cal. Daily Op. Serv. 4821",
            "11 I.E.R. Cas. (BNA) 1393",
            "96 Daily Journal DAR 7732"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilkie v. Robbins",
          "cluster_id": 145705,
          "cite": [
            "168 L. Ed. 2d 389",
            "127 S. Ct. 2588",
            "551 U.S. 537",
            "2007 U.S. LEXIS 8513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefkowitz v. Cunningham",
          "cluster_id": 109683,
          "cite": [
            "53 L. Ed. 2d 1",
            "97 S. Ct. 2132",
            "431 U.S. 801",
            "1977 U.S. LEXIS 19"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen v. Illinois",
          "cluster_id": 111745,
          "cite": [
            "92 L. Ed. 2d 296",
            "106 S. Ct. 2988",
            "478 U.S. 364",
            "1986 U.S. LEXIS 130",
            "54 U.S.L.W. 4966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garner v. United States",
          "cluster_id": 109400,
          "cite": [
            "47 L. Ed. 2d 370",
            "96 S. Ct. 1178",
            "424 U.S. 648",
            "1976 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mandujano",
          "cluster_id": 109442,
          "cite": [
            "48 L. Ed. 2d 212",
            "96 S. Ct. 1768",
            "425 U.S. 564",
            "1976 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Selective Service System v. Minnesota Public Interest Research Group",
          "cluster_id": 111260,
          "cite": [
            "82 L. Ed. 2d 632",
            "104 S. Ct. 3348",
            "468 U.S. 841",
            "1984 U.S. LEXIS 151",
            "52 U.S.L.W. 5140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Hare Truck Service, Inc. v. City of Northlake",
          "cluster_id": 118060,
          "cite": [
            "135 L. Ed. 2d 874",
            "116 S. Ct. 2353",
            "518 U.S. 712",
            "1996 U.S. LEXIS 4263",
            "64 U.S.L.W. 4694",
            "10 Fla. L. Weekly Fed. S 115",
            "11 I.E.R. Cas. (BNA) 1377",
            "96 Cal. Daily Op. Serv. 4812",
            "96 Daily Journal DAR 7746"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Asplin v. Mueller",
          "cluster_id": 1389666,
          "cite": [
            "687 P.2d 1329",
            "1984 Colo. App. LEXIS 1157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heller v. District of Columbia",
          "cluster_id": 614652,
          "cite": [
            "670 F.3d 1244",
            "399 U.S. App. D.C. 314",
            "2011 U.S. App. LEXIS 20130",
            "2011 WL 4551558"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sonya Evette Singleton, National Association of Criminal Defense Lawyers, Amicus Curiae",
          "cluster_id": 760928,
          "cite": [
            "165 F.3d 1297",
            "1999 Colo. J. C.A.R. 590",
            "1999 U.S. App. LEXIS 222",
            "1999 WL 6469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas v. Texas",
          "cluster_id": 903977,
          "cite": [
            "186 L. Ed. 2d 376",
            "133 S. Ct. 2174",
            "2013 U.S. LEXIS 4697",
            "570 U.S. 178",
            "81 U.S.L.W. 4467",
            "24 Fla. L. Weekly Fed. S 294",
            "2013 WL 2922119"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip Fantone v. Fred Latini",
          "cluster_id": 2779958,
          "cite": [
            "780 F.3d 184",
            "2015 U.S. App. LEXIS 2470",
            "2015 WL 669290"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Avant v. Clifford",
          "cluster_id": 1549504,
          "cite": [
            "341 A.2d 629",
            "67 N.J. 496",
            "1975 N.J. LEXIS 205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karl P. Zinn",
          "cluster_id": 76088,
          "cite": [
            "321 F.3d 1084",
            "2003 WL 328925"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard Aichele",
          "cluster_id": 566407,
          "cite": [
            "941 F.2d 761",
            "91 Cal. Daily Op. Serv. 6180",
            "91 Daily Journal DAR 9211",
            "1991 U.S. App. LEXIS 16620",
            "1991 WL 138118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108882) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDUzOTkzNjAwMDAwJnM9MTI3ODkxJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108882%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108882)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzUmcz03MzIyMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108882%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108882)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 0,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108882)",
    "indexed_citing_opinions": 663,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108882,
        "count": 663,
        "count_source": "search"
      }
    ],
    "citation_count": 1103,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lefkowitz-v-turley.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwNTQxMjMmcz05MzY3NTAyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108882%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108882,
        "cited_id": 85566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 105095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 106075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 107248,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 107336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 107738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 107739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 108238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 2339910,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 2499246,
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
    "date_created": "2026-07-05T10:47:20Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:47:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:47:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:51:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:47:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Lefkowitz v. Turley

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b223-13">
  Mr. Justice White
 </author>
<p id="Aos">
  delivered the opinion of the Court.
 </p>
<p id="b223-14">
  New York General Municipal Law §§ 103-a and 103-b and New York Public Authorities Law §§ 2601 and 2602 require public contracts to provide that if a contractor refuses to waive immunity or to answer questions when called to testify concerning his contracts with the State or any of its subdivisions, his existing contracts may be canceled and he shall be disqualified from further transactions with the State for five years.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  In addition to
  <span citation-index="1" class="star-pagination" label="72"> 
   *72
   </span>
  specifying these contract terms, the statutes require disqualification from contracting with public authorities upon failure of any person to waive immunity or to
  <span citation-index="1" class="star-pagination" label="73"> 
   *73
   </span>
  answer questions with respect to his transactions with the State or its subdivisions. The issue in this case is whether these sections are consistent with the Four
  <span citation-index="1" class="star-pagination" label="74"> 
   *74
   </span>
  teenth Amendment insofar as it makes applicable to the States the Fifth Amendment privilege against compelled self-incrimination.
 </p>
<p id="b227-4">
<span citation-index="1" class="star-pagination" label="75"> 
   *75
   </span>
  I
 </p>
<p id="b227-5">
  Appellees are two architects licensed by the State of New York. They were summoned to testify before a grand jury investigating various charges of conspiracy,
  <span citation-index="1" class="star-pagination" label="76"> 
   *76
   </span>
  bribery, and larceny. They were asked, but refused, to sign waivers of immunity, the effect of which would have been to waive their right not to be compelled in a criminal case to be a witness against themselves. They were then excused and the District Attorney, as directed by law, notified various contracting authorities of appellees’ conduct and called attention to the applicable disqualification statutes. Appellees thereupon brought this action alleging that their existing contracts and future contracting privileges were threatened and asserted that the pertinent statutory provisions were violative of the constitutional privilege against compelled self-incrimination. A three-judge District Court was convened and declared the four statutory provision's at issue unconstitutional under the Fourteenth and Fifth Amendments, <span class="citation" data-id="2339910"><a href="/opinion/2339910/turley-v-lefkowitz/" aria-description="Citation for case: Turley v. Lefkowitz">342 F. Supp. 544</a></span> (WDNY 1972). We noted probable jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./410/924/">410 U. S. 924</a></span> (1973). The State appealed pursuant to <span class="citation no-link">28 U. S. C. § 1253</span>. We affirm the judgment of the District Court.
 </p>
<p id="b229-8">
<span citation-index="1" class="star-pagination" label="77"> 
   *77
   </span>
  ) — i
 </p>
<p id="b229-3">
  The Fifth Amendment provides that no person shall be compelled in any criminal case to be a witness against himself.” The Amendment not only protects the individual against being involuntarily called as a witness against himself in a criminal prosecution but also privileges him not to answer official questions put to him in any other proceeding, civil or criminal, formal or informal, where the answers might incriminate him in future criminal proceedings.
  <em>
   McCarthy
  </em>
  v.
  <em>
   Arndstein,
  </em>
  <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#40" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34, 40</a></span> (1924), squarely held that
 </p>
<blockquote id="b229-4">
  “[t]he privilege is not ordinarily dependent upon the nature of the proceeding in which the testimony is sought or is to be used. It applies alike to civil and criminal proceedings, wherever the answer might tend to subject to criminal responsibility him who gives it. The privilege protects a mere witness as fully as it does one who is also a party defendant.”
 </blockquote>
<p id="b229-5">
  In this respect,
  <em>
   McCarthy
  </em>
  v.
  <em>
   <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/" aria-description="Citation for case: McCarthy v. Arndstein">Arndstein</a></span>
  </em>
  reflected the settled view in this Court. The object of the Amendment “was to insure that a person should not be compelled, when acting as a witness in any investigation, to give testimony which might tend to show that he himself had committed a crime.”
  <em>
   Counselman
  </em>
  v.
  <em>
   Hitchcock,
  </em>
  <span class="citation no-link">142 U. S. 647</span>, 562 (1892). See also
  <em>
   Bram
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94789"><a href="/opinion/94789/hall-v-united-states/#542" aria-description="Citation for case: Hall v. United States">168 U. S. 632, 542-543</a></span> (1897);
  <em>
   Brown
  </em>
  v.
  <em>
   Walker,
  </em>
  <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">161 U. S. 591</a></span> (1896);
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 634, 637-638</a></span> (1886);
  <em>
   United States
  </em>
  v.
  <em>
   Saline Bank,
  </em>
  <span class="citation" data-id="85566"><a href="/opinion/85566/the-united-states-v-the-saline-bank-of-virginia-john-webster-and-others/" aria-description="Citation for case: The United States v. The Saline Bank of Virginia, John...">1 Pet. 100</a></span> (1828). This is the rule that is now applicable to the States.
  <em>
   Malloy
  </em>
  v.
  <em>
   Hogan,
  </em>
  <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964). “It must be considered irrelevant that the petitioner was a witness in a statutory inquiry and not a defendant in a criminal prosecution, for it has long been settled that the privilege protects witnesses in similar federal inquiries.”
  <span citation-index="1" class="star-pagination" label="78"> 
   *78
   </span>
<span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#11" aria-description="Citation for case: Malloy v. Hogan"><em>
   Id.,
  </em>
  at 11</a></span>. In any of these contexts, therefore, a witness protected by the privilege may rightfully refuse to answer unless and until he is protected at least against the use of his compelled answers and evidence derived therefrom in any subsequent criminal case in which he is a defendant.
  <em>
   Kastigar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441</a></span> (1972). Absent such protection, if he is nevertheless compelled to answer, his answers are inadmissible against him in a later criminal prosecution.
  <em>
   Bram
  </em>
  v.
  <em>
   United States, supra; Boyd
  </em>
  v.
  <em>
   United States, supra.
  </em>
</p>
<p id="b230-5">
  Against this background, there is no room for urging that the Fifth Amendment privilege is inapplicable simply because the issue arises, as it does here, in the context of official inquiries into the job performance of a public contractor. Surely, the ordinary rule is that the privilege is available to witnesses called before grand juries as these appellee architects were.
  <em>
   Hale
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#66" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 66</a></span> (1906).
 </p>
<p id="b230-6">
  It is- true that the State has a strong, legitimate interest in maintaining the integrity of its civil service and of its transactions with independent contractors furnishing a wide range of goods and services; and New York would have it that this interest is sufficiently strong to override the privilege. The suggestion is that the State should be able to interrogate employees and contractors about their job performance without regard to the Fifth Amendment, to discharge those who refuse to answer or to waive the privilege by waiving the immunity to which they would otherwise be entitled, and to use any incriminating answers obtained in subsequent criminal prosecutions. But claims of overriding interests are not unusual in Fifth Amendment litigation and they have not fared well.
 </p>
<p id="b230-7">
  In
  <em>
   McCarthy
  </em>
  v.
  <em>
   <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/" aria-description="Citation for case: McCarthy v. Arndstein">Arndstein, supra,</a></span>
  </em>
  the United States insisted that because of the strong public interest in marshaling and distributing assets of bankrupts, the
  <span citation-index="1" class="star-pagination" label="79"> 
   *79
   </span>
  Fifth Amendment should not protect a bankrupt during the official examinations mandated by the Bankruptcy Act. That position did not prevail. The bankrupt’s testimony could be had, but only if he were afforded sufficient immunity to supplant the privilege. And long before
  <em>
   McCarthy
  </em>
  v.
  <em>
   <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/" aria-description="Citation for case: McCarthy v. Arndstein">Arndstein</a></span>,
  </em>
  the Court recognized that without the compelled testimony of knowledgeable and perhaps implicated witnesses, the enforcement of the transportation laws “would become impossible,” but nevertheless proceeded on a basis that witnesses must be granted adequate immunity if their evidence was to be compelled.
  <em>
   Brown
  </em>
  v.
  <em>
   Walker,
  </em>
  <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#610" aria-description="Citation for case: Brown v. Walker">161 U. S., at 610</a></span>. Similarly, the enforcement of the antitrust laws against private corporations was at stake in
  <em>
   Hale
  </em>
  v.
  <em>
   <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">Henkel, supra,</a></span>
  </em>
  but immunity was essential to command the testimony of individual witnesses. Also, it would be difficult to overestimate the importance of the interest of the States in the enforcement of their ordinary criminal laws; but the price for incriminating answers from third-party witnesses is sufficient immunity to satisfy the imperatives of the Fifth Amendment privilege against compelled self-incrimination. Finally, in almost the very context here involved, this Court has only recently held that employees of the State do not forfeit their constitutional privilege and that they may be compelled to respond to questions about the performance of their duties but only if their answers cannot be used against them in subsequent criminal prosecutions.
  <em>
   Garrity
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U. S. 493</a></span> (1967);
  <em>
   Gardner
  </em>
  v.
  <em>
   Broderick,
  </em>
  <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">392 U. S. 273</a></span> (1968);
  <em>
   Sanitation Men
  </em>
  v.
  <em>
   Sanitation Comm’r,
  </em>
  <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280</a></span> (1968).
 </p>
<p id="b231-5">
  Ill
 </p>
<p id="b231-6">
  In
  <em>
   Garrity
  </em>
  v.
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">New Jersey</a></span>,
  </em>
  certain police officers were summoned to an inquiry being conducted by the Attorney General concerning the fixing of traffic tickets.
  <span citation-index="1" class="star-pagination" label="80"> 
   *80
   </span>
  They were asked questions following warnings that if they did not answer they would be removed from office and that anything they said might be used against them in any criminal proceeding. No immunity of any kind was offered or available under state law. The questions were answered and the answers later used over their objections, in their prosecutions for conspiracy. The Court held that “the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic.” <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/#500" aria-description="Citation for case: Garrity v. New Jersey">385 U. S., at 500</a></span>. The Court also held that in the context of threats of removal from office the act of responding to interrogation was not voluntary and was not an effective waiver of the privilege against self-incrimination, the Court conceding, however, that there might be other situations “where one who is anxious to make a clean breast of the whole affair volunteers the information.”
  <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/#499" aria-description="Citation for case: Garrity v. New Jersey"><em>
   Id.,
  </em>
  at 499</a></span>.
 </p>
<p id="b232-5">
  The issue in
  <em>
   Gardner
  </em>
  v.
  <em>
   <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Broderick, supra,</a></span>
  </em>
  was whether the State might discharge a police officer who, after he was summoned before a grand jury to testify about the performance of his official duties and was advised of his right against compulsory self-incrimination, then refused to waive that right as requested by the State. Conceding that appellant could be discharged for refusing to answer questions about the performance of his official duties, if not required to waive immunity, the Court held that the officer could not be terminated, as he was, for refusing to waive his constitutional privilege. Although under
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
  </em>
  any waiver executed may have been invalid and any answers elicited inadmissible in evidence, the State did not purport to recognize as much and instead
  <span citation-index="1" class="star-pagination" label="81"> 
   *81
   </span>
  attempted to coerce a waiver on the penalty of loss of employment. The “testimony was demanded before the grand jury in part so that it might be used to prosecute him, and not solely for the purpose of securing an accounting of his performance of his public trust.” 392 U. S., at 279. Hence, the State’s statutory provision requiring his dismissal for his refusal to waive immunity could not stand.
 </p>
<p id="b233-4">
  The companion case,
  <em>
   Sanitation Men
  </em>
  v.
  <em>
   Sanitation Comm’r, supra,
  </em>
  was to the same effect. Here again, public employees were officially interrogated and advised that refusal to answer and sign waivers of immunity would lead to dismissal. Here again, the Court held that the State presented the employees with “a choice between surrendering their constitutional rights or their jobs,” 392 U. S., at 284, although clearly they would “subject themselves to dismissal if they refuse to account for their performance of their public trust, after proper proceedings, which do not involve an attempt to coerce them to relinquish their constitutional rights.”
  <em>
   Id.,
  </em>
  at 285.
 </p>
<p id="b233-5">
  These cases, and their predecessors, ultimately rest on a reconciliation of the well-recognized policies behind the privilege of self-incrimination,
  <em>
   Murphy
  </em>
  v.
  <em>
   Waterfront Comm’n,
  </em>
  <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964), and the need of the State, as well as the Federal Government, to obtain information “to assure the effective functioning of government,”
  <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#93" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor"><em>
   id.,
  </em>
  at 93</a></span> (White, J., concurring). Immunity is required if there is to be “rational accommodation between the imperatives of the privilege and the legitimate demands of government to compel citizens to testify.”
  <em>
   Kastigar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#446" aria-description="Citation for case: Kastigar v. United States">406 U. S., at 446</a></span>. It is in this sense that immunity
  <span citation-index="1" class="star-pagination" label="82"> 
   *82
   </span>
  statutes have “become part of our constitutional fabric.”
  <em>
   Ullmann
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#438" aria-description="Citation for case: Ullmann v. United States">350 U. S. 422, 438</a></span> (1956).
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b234-5">
  We agree with the District Court that
  <em>
   Garrity, Gardner,
  </em>
  and
  <em>
   <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">Sanitation Men</a></span>
  </em>
  control the issue now before us. The State sought to interrogate appellees about their transactions with the State and to require them to furnish possibly incriminating testimony by demanding that they waive their immunity and by disqualifying them as public contractors when they refused. It seems to us that the State intended to accomplish what
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
  </em>
  specifically prohibited — to compel testimony that had not been immunized. The waiver sought by the State, under threat of loss of contracts, would have been no less compelled than a direct request for the testimony without resort to the waiver device. A waiver secured under threat of substantial economic sanction cannot be
  <span citation-index="1" class="star-pagination" label="83"> 
   *83
   </span>
  termed voluntary. As already noted,
  <em>
   Oarrity
  </em>
  specifically rejected the claim of an effective waiver when the policemen in that case, in the face of possible discharge, proceeded to answer the questions put to them. <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/#498" aria-description="Citation for case: Garrity v. New Jersey">385 U. S., at 498</a></span>. The same holding is implicit in both
  <em>
   <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Gardner</a></span>
  </em>
  and
  <em>
   <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">Sanitation Men</a></span>.
  </em>
</p>
<p id="b235-5">
  The State nevertheless asserts that whatever may be true of state employees, a different rule is applicable to public contractors such as architects. Because independent contractors may not depend entirely on transactions with the State for their livelihood, it is suggested that disqualification from contracting with official agencies for a period of five years is neither compulsion within the meaning of the Fifth Amendment nor a forbidden penalty for refusing to answer questions put to them about their job performance. But we agree with the District Court that “the plaintiffs’ disqualification from public contracting for five years as a penalty for asserting a constitutional privilege is violative of their Fifth Amendment rights.” <span class="citation" data-id="2339910"><a href="/opinion/2339910/turley-v-lefkowitz/#549" aria-description="Citation for case: Turley v. Lefkowitz">342 F. Supp., at 549</a></span>. We fail to see a difference of constitutional magnitude between the threat of job loss to an employee of the State, and a threat of loss of contracts to a contractor.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b235-6">
  If the argument is that the cost to a contractor is small in comparison to the cost to an employee of losing his job, the premise must be that it is harder for a state employee to find employment in the private sector, than it is for an architect. An architect lives off his contracting fees as surely as a state employee lives off his salary, and fees and salaries may be equally hard to come by in the private sector after sanctions have been taken by
  <span citation-index="1" class="star-pagination" label="84"> 
   *84
   </span>
  the State. In some sense the plight of the architect may be worse, for under the New York statutes it may be that any firm that employs him thereafter will also be subject to contract cancellation and disqualification.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  A significant infringement of constitutional rights cannot be justified by the speculative ability of those affected to cover the damage.
 </p>
<p id="b236-5">
  IV
 </p>
<p id="b236-6">
  We should make clear, however, what we have said before. Although due regard for the Fifth Amendment forbids the State to compel incriminating answers from its employees and contractors that may be used against them in criminal proceedings, the Constitution permits that very testimony to be compelled if neither it nor its fruits are available for such use.
  <em>
   Kastigar
  </em>
  v.
  <em>
   United States, supra.
  </em>
  Furthermore, the accommodation between the interest of the State and the Fifth Amendment requires that the State have means at its disposal to secure testimony if immunity is supplied and testimony is still refused. This is recognized by the power of the courts to. compel testimony, after a grant of immunity, by use of civil contempt and coerced imprisonment.
  <em>
   Shillitani
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="107248"><a href="/opinion/107248/shillitani-v-united-states/" aria-description="Citation for case: Shillitani v. United States">384 U. S. 364</a></span> (1966). Also, given adequate immunity, the State may plainly insist that employees either answer questions under oath about the performance of their job or suffer the loss of employment. By like token, the State may insist that the architects involved in this case either respond to relevant inquiries about the performance of their contracts or suffer cancellation of current relationships and disqualification from contracting with public agencies for an appropriate time in the future. But the State may not insist that appellees
  <span citation-index="1" class="star-pagination" label="85"> 
   *85
   </span>
  waive their Fifth Amendment privilege against self-incrimination and consent to the use of the fruits of the interrogation in any later proceedings brought against them. Rather, the State must recognize what our cases hold: that answers elicited upon the threat of the loss of employment are compelled and inadmissible in evidence. Hence, if answers are to be required in such circumstances States must offer to the witness whatever immunity is required to supplant the privilege and may not insist that the employee or contractor waive such immunity.
 </p>
<p id="b237-6">
  ~ ,
  <em>
   Affirmed.
  </em>
</p>
<author id="b237-7">
  Mr. Justice Brennan,
 </author>
<p id="Amjp">
  with whom Mr. Justice Douglas and Mr. Justice Marshall join.
 </p>
<p id="b237-8">
  I join the Court’s opinion in all respects but one. It is my view that immunity which permits testimony to be compelled “if neither it nor its fruits are available for . . . use” in criminal proceedings does not satisfy the privilege against self-incrimination. “I believe that the Fifth Amendment’s privilege against self-incrimination requires that any jurisdiction that compels a man to incriminate himself grant him absolute immunity under its laws from prosecution for any transaction revealed in that testimony.”
  <em>
   Piccirillo
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9424403"><a href="/opinion/108238/piccirillo-v-new-york/#562" aria-description="Citation for case: Piccirillo v. New York">400 U. S. 548, 562</a></span> (1971) (Brennan, J., dissenting.)
 </p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b223-15">
   N. Y. Gen. Munic. Law §§ 103-a and 103-b (Supp. 1973-1974) provide:
  </p>
<blockquote id="b223-16">
   Section 103-a. Ground for cancellation of contract by municipal corporations and fire districts:
  </blockquote>
<blockquote id="b223-17">
<em>
    “A
   </em>
   clause shall be inserted in all specifications or contracts made or awarded by a municipal corporation or any public department, agency or official thereof on or after the first day of July, nineteen
   <span citation-index="1" class="star-pagination" label="72"> 
    *72
    </span>
   hundred fifty-nine or by a fire district or any agency or official thereof on or after the first day of September, nineteen hundred sixty, for work or services performed or to be performed, or goods sold or to be sold, to provide that upon the refusal of a person, when called before a grand jury, head of a state department, temporary state commission or other state agency, . . . head of a city department, or other city agency, which is empowered to compel the attendance of witnesses and examine them under oath, to testify in an investigation concerning any transaction or contract had with the state, any political subdivision thereof, a public authority or with any public department, agency or official of the state or of any political subdivision thereof or of a public authority, to sign a waiver of immunity against subsequent criminal prosecution or to answer any relevant question concerning such transaction or contract,
  </blockquote>
<blockquote id="b224-6">
   “(a) such person, and any firm, partnership or corporation of which he is a member, partner, director or officer shall be disqualified from thereafter selling to or submitting bids to or receiving awards from or entering into any contracts with any municipal corporation, or firé district, or any public department, agency or official thereof, for goods, work or services, for a period of five years after such refusal, and to provide also that
  </blockquote>
<blockquote id="b224-7">
   “(b) any and all contracts made with any municipal corporation or any public department, agency or official thereof on or after the first day of July, nineteen hundred fifty-nine or with any fire district or any agency or official thereof on or after the first day of September, nineteen hundred sixty, by such person, and by any firm, partnership, or corporation of which he is a member, partner, director or officer may be cancelled or terminated by the municipal corporation or fire district without incurring any penalty or damages on account of such cancellation or termination, but any monies owing by the municipal corporation or fire district for goods delivered or work done prior to the cancellation or termination shall be paid.
  </blockquote>
<blockquote id="b224-8">
   “The provisions of this section as in force and effect prior to the first day of September, nineteen hundred sixty, shall apply to specifications or contracts made or awarded by a municipal corpora
   <span citation-index="1" class="star-pagination" label="73"> 
    *73
    </span>
   tion on or after .the first day of July, nineteen hundred fifty-nine, but prior to the first day of September, nineteen hundred sixty.”
  </blockquote>
<p id="b225-6">
   Section 103-b. Disqualification to contract with municipal corporations and fire districts:
  </p>
<blockquote id="b225-7">
   “Any person, who, when called before a grand jury, head of a state department, temporary state commission or other state agency, . . . head of a city department or other city agency, which is empowered to compel the attendance of witnesses and examine them under oath, to testify in an investigation concerning any transaction or contract had with the state, any political subdivision thereof, a public authority, or with a public department, agency or official of the state or of any political subdivision thereof or of a public authority, refuses to sign a waiver of immunity against subsequent criminal prosecution or to answer any relevant question concerning such transaction or contract, and any firm, partnership or corporation of which he is a member, partner, director or officer shall be disqualified from thereafter selling to or submitting bids to or receiving awards from or entering into any contracts with any municipal corporation or fire district, or with any public department, agency or official thereof, for goods, work or services, for a period of five years after such refusal or until a disqualification shall be removed pursuant to the provisions of section one hundred three-c of this article.
  </blockquote>
<blockquote id="b225-8">
   “It shall be the duty of the officer conducting the investigation before the grand jury, the head of a state department, the chairman of the temporary state commission or other state agency,... . the head of a city department or other city agency before which the refusal occurs to send notice of such refusal, together with the names of any firm, partnership, or corporation of which the person so refusing is known to be a member, partner, officer or director, to the commissioner of transportation of the state of New York and the appropriate departments, agencies and officials of the state, political subdivisions thereof or public authorities with whom the person so refusing and any firm, partnership or corporation of which he is a member, partner, director or officer, is known to have a contract. However, when such refusal occurs before a body other than a grand jury, notice of refusal shall not be sent for a period of ten days after such refusal occurs. Prior to the expiration of
   <span citation-index="1" class="star-pagination" label="74"> 
    *74
    </span>
   this ten day period, any person, firm, partnership or corporation which has become liable to the cancellation or termination of a contract or disqualification to contract on account of such refusal may commence a special proceeding at a special term of the supreme court, held within the judicial district in which the refusal occurred, for an order determining whether the questions in response to which the refusal occurred were relevant and material to the inquiry. Upon the commencement of such proceeding, the sending of such notice of refusal to answer shall be subject to order of the court in which the proceeding was brought in a manner and on such terms as the court may deem just. If a proceeding is not brought within ten days, notice of refusal shall thereupon be sent as provided herein.”
  </blockquote>
<p id="b226-6">
   N. Y. Pub. Auth. Law §§2601 and 2602 (Supp. 1973-1974) provide:
  </p>
<p id="b226-7">
   Section 2601. Ground for cancellation of contract by public authority:
  </p>
<blockquote id="b226-8">
   “A clause shall be inserted in all specifications or contracts hereafter made or awarded by any public authority or by any official of any public authority created by the state or any political subdivision, for work or services performed or to be performed or goods sold or to be sold, to provide that upon the refusal by a person, when called before a grand jury, head of a state department, temporary state commission or other state agency,... head of a city department, or other city agency, which is empowered to compel the attendance of witnesses and examine them under oath, to testify in an investigation concerning any transaction or contract had with the state, any political subdivision thereof, a public authority or with any. public department, agency or official of the state or of any political subdivision thereof or of a public authority, to sign a waiver of immunity against subsequent criminal prosecution or to answer any relevant question concerning such transaction or contract,
  </blockquote>
<blockquote id="b226-9">
   “(a) such person, and any firm, partnership or corporation of which he is a member, partner, director or officer shall be disqualified from thereafter selling to or submitting bids to or receiving awards from or entering into any contracts with any public authority or official thereof, for goods, work or services, for a period of five years after such refusal, and to provide also that
  </blockquote>
<blockquote id="b226-10">
   “(b) any and all contracts made with any public authority or
   <span citation-index="1" class="star-pagination" label="75"> 
    *75
    </span>
   official thereof, since the effective date of this law, by such person and by any firm, partnership or corporation of which he is a member, partner, director or officer may be cancelled or terminated by the public authority without incurring any penalty or damages on account of such cancellation or termination, but any monies owing by the public authority for goods delivered or work done prior to the cancellation or termination shall be paid.”
  </blockquote>
<p id="b227-7">
   Section 2602. Disqualification to contract with public authority:
  </p>
<blockquote id="b227-8">
   “Any person, who, when called before a grand jury, head of a state department, temporary state commission or other state agency, . . . head of a city department, or other city agency, which is empowered to compel the attendance of witnesses and examine them under oath, to testify in an investigation concerning any transaction or contract had with the state, any political subdivision thereof, a public authority or with a public department, agency or official of the state or of any political subdivision thereof or of a public authority, refuses to sign a waiver of immunity against subsequent criminal prosecution or to answer any relevant questions concerning such transaction or contract, and any firm, partnership or corporation, of which he is a member, partner, director, or officer shall be disqualified from thereafter selling to or submitting bids to or receiving awards from or entering into any contracts with any public authority or any official of any public authority created by the state or any political subdivision, for goods, work or services, for a period of five years after such refusal or until a disqualification shall be removed pursuant to the provisions of section twenty-six hundred three of this title.
  </blockquote>
<blockquote id="b227-9">
   “It shall be the duty of the officer conducting the investigation before the grand jury, the head of a state department, the chairman of the temporary state commission or other state agency,... the head of a city department or other city agency before which the refusal occurs to send notice of such refusal, together with the names of any firm, partnership or corporation of which the person so refusing is known to be a member, partner, officer or director, to the commissioner of transportation of the state of New York, or the commissioner of general services as the case may be, and the appropriate
   <span citation-index="1" class="star-pagination" label="76"> 
    *76
    </span>
   departments, agencies and officials of the state, political subdivisions thereof or public authorities with whom the persons [sic] so refusing and any firm, partnership or corporation of which he is a member, partner, director or officer, is known to have a contract. However, when such refusal occurs before a body other than a grand jury, notice of refusal shall not be sent for a period of ten days after such refusal occurs. Prior to the expiration of this ten day period, any person, firm, partnership or corporation which has become liable to the. cancellation or termination of a contract or disqualification to contract on account of such refusal may commence a special proceeding at a special term of the supreme court, held within the judicial district in which the refusal occurred, for an order determining whether the questions in response to which the refusal occurred were relevant and material to the inquiry. Upon the commencement of such proceeding, the sending of such notice of refusal to answer shall be subject to order of the court in which the proceeding was brought in a manner and on such terms as the court may deem just. If a proceeding is not brought within ten days, notice of refusal shall thereupon be sent as provided herein.”
  </blockquote>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b234-6">
   In
   <em>
    Orloff
   </em>
   v.
   <em>
    Willoughby,
   </em>
   <span class="citation" data-id="9420889"><a href="/opinion/105095/orloff-v-willoughby/" aria-description="Citation for case: Orloff v. Willoughby">345 U. S. 83</a></span> (1953), a doctor inducted into the Army was denied a commission as an officer after refusing to divulge whether he was a Communist, as required by a loyalty certificate prescribed for commissioned officers. Instead he asserted his “Federal constitutional privilege” when called upon to answer the question. In holding that the Government was justified in refusing the commission because of the failure to answer, the Court had no occasion to consider whether Orloff would have been exposed to criminal prosecution if he had stated that he was a member of the Communist Party. The case differs significantly from the one before us since the State here asks the architects to affirmatively expose themselves to criminal prosecution by waiving their privilege against self-in crimination, or from
   <em>
    <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>,
   </em>
   where the threat of criminal prosecution was apparent both from the nature of the proceeding, and the absence of applicable state immunity statutes.
  </p>
<p id="b234-7">
<em>
    Kimm
   </em>
   v.
   <em>
    Rosenberg,
   </em>
   <span class="citation" data-id="9422018"><a href="/opinion/106075/kimm-v-rosenberg/" aria-description="Citation for case: Kimm v. Rosenberg">363 U. S. 405</a></span> (1960), is also inapposite. The Court there held that an alien whose deportation had been ordered was ineligible for a discretionary order permitting his voluntary departure, because he had failed to establish that he was not affiliated with the Communist Party. .Petitioner’s imminent departure from the country, whether it was voluntary or compelled, obviously made the threat of criminal prosecution on the basis of his answer remote.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b235-7">
   As
   <em>
    <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
   </em>
   succinctly put it: “The option to lose their means of livelihood or to pay the penalty of self-incrimination is the antithesis of free choice to speak out or to remain silent.” <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/#497" aria-description="Citation for case: Garrity v. New Jersey">385 U. S. 493, 497</a></span> (1967).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b236-7">
   The contract disqualifications apply not only to the person who refuses to waive immunity but also to “any firm, partnership or corporation of which he is a member, partner, director or officer . . . .”
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Lego v. Twomey.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Lego v. Twomey"
type: case
citation: "404 U.S. 477 (1972)"
parallel_cite: "92 S. Ct. 619; 30 L. Ed. 2d 618"
neutral_cite: 1972 U.S. LEXIS 100
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-01-12
docket: 70-5037
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1972-01-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Lego v. Twomey
  varies_by_point: false
  scope_note: "Good law; the federal constitutional floor for proving confession voluntariness is a preponderance of the evidence. Reaffirmed and extended to Miranda-waiver proof in Colorado v. Connelly."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108429/lego-v-twomey/"
  cluster_id: 108429
  opinion_id: 108429
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Colorado v. Connelly]]", "[[Rogers v. Richmond]]", "[[Brown v. Mississippi]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "confessions", "voluntariness", "due-process", "burden-of-proof"]
holding: "The prosecution need prove the voluntariness of a confession only by a preponderance of the evidence, not beyond a reasonable doubt; and a defendant whose voluntariness claim the judge has decided is not entitled to have the jury redetermine voluntariness. States may adopt a higher standard."
lake:
  record_id: Lego v. Twomey
  status: verified
  projected_at: 2026-07-06
---

# Lego v. Twomey

*404 U.S. 477 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Lego was convicted of armed robbery on evidence that included his confession, which he claimed the police had beaten out of him. At a pretrial [[Common Legal Terms#suppression-hearing|suppression hearing]] the trial judge — applying the then-prevailing practice — found the confession voluntary by a [[Common Legal Terms#preponderance-of-the-evidence|preponderance of the evidence]] and admitted it. Lego argued that the Constitution required the prosecution to prove voluntariness [[Common Legal Terms#beyond-a-reasonable-doubt|beyond a reasonable doubt]], and that he was entitled to have the jury decide voluntariness anew. He sought federal [[Common Legal Terms#habeas-corpus|habeas corpus]] (Twomey was the prison warden).

## Issue
Whether the prosecution must prove a confession's voluntariness [[Common Legal Terms#beyond-a-reasonable-doubt|beyond a reasonable doubt]], and whether a defendant is entitled to have the jury redetermine voluntariness after the judge has ruled it admissible.

## Rule
A [[Common Legal Terms#preponderance-of-the-evidence|preponderance of the evidence]] is the constitutional floor. "[W]hen a confession challenged as involuntary is sought to be used against a criminal defendant at his trial, he is entitled to a reliable and clear-cut determination that the confession was in fact voluntarily rendered. Thus, the prosecution must prove at least by a preponderance of the evidence that the confession was voluntary. Of course, the States are free, pursuant to their own law, to adopt a higher standard." — 404 U.S. at 489. ^pin-489

The Court also held that, the judge having reliably determined voluntariness, the defendant has no constitutional right to have the jury pass on the claim a second time.

## Application
The trial judge had found Lego's confession voluntary under the preponderance standard, and that determination was constitutionally sufficient. *In re Winship*'s beyond-a-reasonable-doubt requirement governs proof of guilt, not the preliminary admissibility question of voluntariness, so the higher standard was not required. And because a judge's reliable voluntariness ruling adequately protects the defendant's rights, Lego was not entitled to relitigate voluntariness before the jury. His [[Common Legal Terms#habeas-corpus|habeas]] petition therefore failed.

## Conclusion
The prosecution need prove voluntariness only by a [[Common Legal Terms#preponderance-of-the-evidence|preponderance of the evidence]], and the defendant has no right to a second, jury determination of voluntariness; the judgment denying [[Common Legal Terms#habeas-corpus|habeas]] relief was affirmed. States remain free to impose a higher burden.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Lego* sets the burden of proof for the voluntariness inquiry developed in the due-process line ([[Brown v. Mississippi]], [[Rogers v. Richmond]]) and for the *Jackson v. Denno* requirement of a separate judicial voluntariness determination. The Court extended the same preponderance standard to proof of a [[Miranda v. Arizona]] waiver and to voluntariness generally in [[Colorado v. Connelly]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Lego v. Twomey*, 404 U.S. 477 (1972) — https://www.courtlistener.com/opinion/108429/lego-v-twomey/ — pinpoint: 489.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9072b0bbdf93d084", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Lego v. Twomey"}, "payload": {"all": [{"cite": "404 U.S. 477", "page": "477", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "404"}, {"cite": "92 S. Ct. 619", "page": "619", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}, {"cite": "30 L. Ed. 2d 618", "page": "618", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "30"}, {"cite": "1972 U.S. LEXIS 100", "page": "100", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1972"}], "display": "404 U.S. 477", "official": {"cite": "404 U.S. 477", "page": "477", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "404"}, "official_selection_present": true, "record_id": "Lego v. Twomey"}}
{"assertion_id": "b8c8a4b6307a7674", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-489", "record_id": "Lego v. Twomey"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-489", "pinpoint_status": "slip-only", "quote": "--- # Lego v. Twomey *404 U.S. 477 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Lego was convicted of armed robbery on evidence that included his confession, which he claimed the police had beaten out of him. At a pretrial suppression hearing the trial judge — applying the then-prevailing practice — found the confession voluntary by a preponderance of the evidence and admitted it. Lego argued that the Constitution required the prosecution to prove voluntariness beyond a reasonable doubt, and that he was entitled to have the jury decide voluntariness anew. He sought federal habeas corpus (Twomey was the prison warden). ## Issue Whether the prosecution must prove a confession's voluntariness beyond a reasonable doubt, and whether a defendant is entitled to have the jury redetermine voluntariness after the judge has ruled it admissible. ## Rule A preponderance of the evidence is the constitutional floor.", "quote_fidelity": "mismatch", "record_id": "Lego v. Twomey", "star_marker": null}}
{"assertion_id": "862ed073a7ac96f3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Lego v. Twomey"}, "payload": {"as_of_content": "1972-01-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Lego v. Twomey", "scope_note": "Good law; the federal constitutional floor for proving confession voluntariness is a preponderance of the evidence. Reaffirmed and extended to Miranda-waiver proof in Colorado v. Connelly.", "varies_by_point": false}}
```

### lake record — Lego v. Twomey

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lego v. Twomey",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lego v. Twomey",
    "case_name_short": "Lego",
    "case_name_full": "Lego v. Twomey, Warden",
    "input_case_name": "Lego v. Twomey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-01-12",
    "year": 1972,
    "docket": "70-5037",
    "cluster_id": 108429,
    "lead_opinion_id": 108429,
    "sibling_ids": [
      108429,
      9424726,
      9424727
    ],
    "absolute_url": "/opinion/108429/lego-v-twomey/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8991183,
        "score": 20,
        "case_name": "Lego v. Twomey"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "404 U.S. 477",
      "volume": "404",
      "reporter": "U.S.",
      "page": "477",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "92 S. Ct. 619",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "30 L. Ed. 2d 618",
        "volume": "30",
        "reporter": "L. Ed. 2d",
        "page": "618",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 100",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "404 U.S. 477",
        "volume": "404",
        "reporter": "U.S.",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 619",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "30 L. Ed. 2d 618",
        "volume": "30",
        "reporter": "L. Ed. 2d",
        "page": "618",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 100",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "404 U.S. 477",
    "official_selection": {
      "court_class": "scotus",
      "selected": "404 U.S. 477",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-489",
      "page": null,
      "quote": "--- # Lego v. Twomey *404 U.S. 477 (1972)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Lego was convicted of armed robbery on evidence that included his confession, which he claimed the police had beaten out of him. At a pretrial suppression hearing the trial judge \u2014 applying the then-prevailing practice \u2014 found the confession voluntary by a preponderance of the evidence and admitted it. Lego argued that the Constitution required the prosecution to prove voluntariness beyond a reasonable doubt, and that he was entitled to have the jury decide voluntariness anew. He sought federal habeas corpus (Twomey was the prison warden). ## Issue Whether the prosecution must prove a confession's voluntariness beyond a reasonable doubt, and whether a defendant is entitled to have the jury redetermine voluntariness after the judge has ruled it admissible. ## Rule A preponderance of the evidence is the constitutional floor.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1972-01-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Lego v. Twomey",
    "varies_by_point": false,
    "scope_note": "Good law; the federal constitutional floor for proving confession voluntariness is a preponderance of the evidence. Reaffirmed and extended to Miranda-waiver proof in Colorado v. Connelly.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Capote v. State",
          "cluster_id": 10680228,
          "cite": [
            "908 S.E.2d 540",
            "320 Ga. 191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kasey A. Smith",
          "cluster_id": 4442984,
          "cite": [
            "162 Idaho 878",
            "406 P.3d 890"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Thomas S. Sharrow",
          "cluster_id": 4489413,
          "cite": [
            "175 A.3d 1236",
            "2017 VT 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jalonte Little v. United States",
          "cluster_id": 3153940,
          "cite": [
            "125 A.3d 1119",
            "2015 D.C. App. LEXIS 526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Feliz",
          "cluster_id": 2817827,
          "cite": [
            "794 F.3d 123",
            "2015 U.S. App. LEXIS 12303",
            "2015 WL 4322298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "CHARLES S. TURNER,CHRISTOPHER D. TURNER,RUSSELL L. OVERTON, LEVY ROUSE, CLIFTON E. YARBOROUGH, KELVIN D. SMITH, & TIMOTHY CATLETT",
          "cluster_id": 2807493,
          "cite": [
            "116 A.3d 894",
            "2015 D.C. App. LEXIS 262"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Greineder",
          "cluster_id": 6580608,
          "cite": [
            "464 Mass. 580",
            "984 N.E.2d 804",
            "2013 WL 951135",
            "2013 Mass. LEXIS 46"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen Murdock",
          "cluster_id": 622650,
          "cite": [
            "399 U.S. App. D.C. 153",
            "667 F.3d 1302",
            "2012 WL 414459",
            "2012 U.S. App. LEXIS 2599"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jelks, 17-08-18 (11-10-2008)",
          "cluster_id": 4009442,
          "cite": [
            "2008 Ohio 5828"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burnette",
          "cluster_id": 2519721,
          "cite": [
            "535 F. Supp. 2d 772",
            "2007 WL 4911523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Banford, L-05-1334 (7-27-2007)",
          "cluster_id": 3978076,
          "cite": [
            "2007 Ohio 3821"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Wayne Simpson v. State",
          "cluster_id": 2933337,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Miller",
          "cluster_id": 6588574,
          "cite": [
            "68 Mass. App. Ct. 835",
            "865 N.E.2d 825",
            "2007 Mass. App. LEXIS 495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rojas Tapia",
          "cluster_id": 202140,
          "cite": [
            "446 F.3d 1",
            "2006 U.S. App. LEXIS 8803",
            "2006 WL 923990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tashiri Wayne Williams",
          "cluster_id": 793121,
          "cite": [
            "435 F.3d 1148",
            "2006 U.S. App. LEXIS 2235",
            "2006 WL 213852"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullaney v. Wilbur",
          "cluster_id": 109265,
          "cite": [
            "44 L. Ed. 2d 508",
            "95 S. Ct. 1881",
            "421 U.S. 684",
            "1975 U.S. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. New York",
          "cluster_id": 109698,
          "cite": [
            "53 L. Ed. 2d 281",
            "97 S. Ct. 2319",
            "432 U.S. 197",
            "1977 U.S. LEXIS 120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Mathiason",
          "cluster_id": 109587,
          "cite": [
            "50 L. Ed. 2d 714",
            "97 S. Ct. 711",
            "429 U.S. 492",
            "1977 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crane v. Kentucky",
          "cluster_id": 111687,
          "cite": [
            "90 L. Ed. 2d 636",
            "106 S. Ct. 2142",
            "476 U.S. 683",
            "1986 U.S. LEXIS 89",
            "54 U.S.L.W. 4598"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bourjaily v. United States",
          "cluster_id": 111938,
          "cite": [
            "97 L. Ed. 2d 144",
            "107 S. Ct. 2775",
            "483 U.S. 171",
            "1987 U.S. LEXIS 2874",
            "22 Fed. R. Serv. 1105",
            "55 U.S.L.W. 4962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneble v. Florida",
          "cluster_id": 108488,
          "cite": [
            "31 L. Ed. 2d 340",
            "92 S. Ct. 1056",
            "405 U.S. 427",
            "1972 U.S. LEXIS 77"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Orange Jell Beechum",
          "cluster_id": 358983,
          "cite": [
            "582 F.2d 898",
            "1978 U.S. App. LEXIS 8198",
            "3 Fed. R. Serv. 1185"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Medina v. California",
          "cluster_id": 112775,
          "cite": [
            "120 L. Ed. 2d 353",
            "112 S. Ct. 2572",
            "505 U.S. 437",
            "1992 U.S. LEXIS 3696"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alvarado v. State",
          "cluster_id": 1676536,
          "cite": [
            "912 S.W.2d 199",
            "1995 Tex. Crim. App. LEXIS 116",
            "1995 WL 675552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guidry v. State",
          "cluster_id": 2342370,
          "cite": [
            "9 S.W.3d 133",
            "1999 Tex. Crim. App. LEXIS 145",
            "1999 WL 1144826"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Montoya",
          "cluster_id": 1202376,
          "cite": [
            "753 P.2d 729",
            "12 Brief Times Rptr. 482",
            "1988 Colo. LEXIS 39",
            "1988 WL 25119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Prim",
          "cluster_id": 2050056,
          "cite": [
            "289 N.E.2d 601",
            "53 Ill. 2d 62",
            "1972 Ill. LEXIS 262"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Guerra",
          "cluster_id": 2633286,
          "cite": [
            "129 P.3d 321",
            "40 Cal. Rptr. 3d 118",
            "37 Cal. 4th 1067",
            "2006 Cal. Daily Op. Serv. 1802",
            "2006 Daily Journal DAR 2547",
            "2006 Cal. LEXIS 2872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald James and David Anthony Butler, United States of America v. Henry Smith and Kenneth Wayne Whitmore",
          "cluster_id": 362801,
          "cite": [
            "590 F.2d 575",
            "1979 U.S. App. LEXIS 17005",
            "3 Fed. R. Serv. 785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108429 OR 9424726 OR 9424727) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTE3NzU2ODAwMDAwJnM9MzEzNTIyOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108429+OR+9424726+OR+9424727%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 15,
        "triage_snippet_classified": 185
      },
      "lane2_top_cited": {
        "query": "cites:(108429 OR 9424726 OR 9424727)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMTkmcz0xMjQ0NzY5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108429+OR+9424726+OR+9424727%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108429 OR 9424726 OR 9424727)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 1,
        "triage_snippet_classified": 17
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108429 OR 9424726 OR 9424727)",
    "indexed_citing_opinions": 1278,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108429,
        "count": 1139,
        "count_source": "search"
      },
      {
        "opinion_id": 9424726,
        "count": 170,
        "count_source": "search"
      },
      {
        "opinion_id": 9424727,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1930,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lego-v-twomey.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4MjM2MDYmcz02NjIxMzYxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108429+OR+9424726+OR+9424727%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108429,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 108111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 108231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 269702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 286166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1207372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1402028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1409161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1419387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1515039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1534970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1568872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1586369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1645241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1795610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1798836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1940977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1992878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2000298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2047659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2128885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2199240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2225068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2374676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2499246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2619842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 3420642,
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
    "date_created": "2026-07-05T10:51:42Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:53:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:53:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:56:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:53:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Lego v. Twomey

```
<div>
<center><b><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">404 U.S. 477</a></span> (1972)</b></center>
<center><h1>LEGO<br>
v.<br>
TWOMEY, WARDEN.</h1></center>
<center>No. 70-5037.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 11, 1971</center>
<center>Decided January 12, 1972</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT.
<p><span class="star-pagination">*478</span> <i>Nathan Lewin,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./402/928/">402 U. S. 928</a></span>, argued the cause and filed a brief for petitioner.</p>
<p><i>James B. Zagel,</i> Assistant Attorney General of Illinois, argued the cause for respondent. With him on the brief were <i>William J. Scott,</i> Attorney General, <i>Joel M. Flaum,</i> First Assistant Attorney General, and <i>Warren K. Smoot,</i> Assistant Attorney General.</p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>In 1964 this Court held that a criminal defendant who challenges the voluntariness of a confession made to officials and sought to be used against him at his trial has a due process right to a reliable determination that the confession was in fact voluntarily given and not the outcome of coercion which the Constitution forbids. <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span>. While our decision made plain that only voluntary confessions may be admitted at the trial of guilt or innocence, we did not then announce, or even suggest, that the factfinder at a coercion hearing need judge voluntariness with reference to an especially severe standard of proof. Nevertheless, <span class="star-pagination">*479</span> since <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>,</i> state and federal courts have addressed themselves to the issue with a considerable variety of opinions.<sup>[1]</sup> We granted certiorari in this case to resolve the question. <span class="citation multiple-matches"><a href="/c/U.%20S./401/992/">401 U. S. 992</a></span> (1971).</p>
<p><span class="star-pagination">*480</span> Petitioner Lego was convicted of armed robbery in 1961 after a jury trial in Superior Court, Cook County, Illinois. The court sentenced him to prison for 25 to 50 years. The evidence introduced against Lego at trial included a confession he had made to police after arrest and while in custody at the station house. Prior to trial Lego sought to have the confession suppressed. He did not deny making it but did challenge that he had done so voluntarily. The trial judge conducted a hearing, out of the presence of the jury, at which Lego testified that police had beaten him about the head and neck with a gun butt. His explanation of this treatment was that the local police chief, a neighbor and former classmate of the robbery victim, had sought revenge upon him. Lego introduced into evidence a photograph that had been taken of him at the county jail on the day after his arrest. The photograph showed that petitioner's face had been swollen and had traces of blood on it. Lego admitted that his face had been scratched in a scuffle with the robbery victim but maintained that the encounter did not explain the condition shown in the photograph. The police chief and four officers also testified. They denied either beating or threatening petitioner and disclaimed knowledge that any other officer had done so. The trial judge resolved this credibility problem in favor of the police and ruled the confession admissible.<sup>[2]</sup> At trial, Lego testified in his own behalf. Although he did not dispute the truth of the confession directly, he did tell his version of the events that had transpired at the <span class="star-pagination">*481</span> police station. The trial judge instructed the jury as to the prosecution's burden of proving guilt. He did not instruct that the jury was required to find the confession voluntary before it could be used in judging guilt or innocence.<sup>[3]</sup> On direct appeal the Illinois Supreme Court affirmed the conviction. <i>People</i> v. <i>Lego,</i> <span class="citation" data-id="2199240"><a href="/opinion/2199240/the-people-v-lego/" aria-description="Citation for case: The PEOPLE v. Lego">32 Ill. 2d 76</a></span>, <span class="citation" data-id="2199240"><a href="/opinion/2199240/the-people-v-lego/" aria-description="Citation for case: The PEOPLE v. Lego">203 N. E. 2d 875</a></span> (1965).</p>
<p>Four years later petitioner challenged his conviction by seeking a writ of habeas corpus in the United States District Court for the Northern District of Illinois. He maintained that the trial judge should have found the confession voluntary beyond a reasonable doubt before admitting it into evidence. Although the judge had made no mention of the standard he used, Illinois law provided that a confession challenged as involuntary could be admitted into evidence if, at a hearing outside the presence of the jury, the judge found it voluntary by a preponderance of the evidence.<sup>[4]</sup> In the alternative petitioner argued that the voluntariness question should also have been submitted to the jury for its separate consideration. <span class="star-pagination">*482</span> After first denying the writ for failure to exhaust state remedies, the District Court granted a rehearing motion, concluded that Lego had no state remedy then available to him and denied relief on the merits. <i>United States ex rel. Lego</i> v. <i>Pate,</i> <span class="citation" data-id="1568872"><a href="/opinion/1568872/united-states-ex-rel-lego-v-pate/" aria-description="Citation for case: United States Ex Rel. Lego v. Pate">308 F. Supp. 38</a></span> (1970).<sup>[5]</sup> The Court of Appeals for the Seventh Circuit affirmed.<sup>[6]</sup></p>
<p></p>
<h2>I</h2>
<p>Petitioner challenges the judgment of the Court of Appeals on three grounds. The first is that he was not proved guilty beyond a reasonable doubt as required by <i>In re Winship,</i> <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970), because the confession used against him at his trial had been proved voluntary only by a preponderance of the evidence. Implicit in the claim is an assumption that a voluntariness hearing is designed to enhance the reliability of jury verdicts. To judge whether that is so we must return to <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span> (1964).</p>
<p>In New York prior to <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>,</i> juries most often determined the voluntariness of confessions and hence whether confessions could be used in deciding guilt or innocence. Trial judges were required to make an initial determination and could exclude a confession, but only if it could not under any circumstances be deemed voluntary.<sup>[7]</sup> When voluntariness was fairly debatable, either because a dispute of fact existed or because reasonable men could have drawn differing inferences from undisputed facts, the question whether the confession violated due process was for the jury. This meant the confession <span class="star-pagination">*483</span> was introduced at the trial itself. If evidence challenging its voluntariness were adduced, the jury was instructed first to pass upon voluntariness and, if it found the confession involuntary, ignore it in determining guilt. If, on the other hand, the confession were found to be voluntary, the jury was then free to consider its truth or falsity and give the confession an appropriate weight in judging guilt or innocence.</p>
<p>We concluded that the New York procedure was constitutionally defective because at no point along the way did a criminal defendant receive a clear-cut determination that the confession used against him was in fact voluntary. The trial judge was not entitled to exclude a confession merely because he himself would have found it involuntary, and, while we recognized that the jury was empowered to perform that function, we doubted it could do so reliably. Precisely because confessions of guilt, whether coerced or freely given, may be truthful and potent evidence, we did not believe a jury could be called upon to ignore the probative value of a truthful but coerced confession; it was also likely, we thought, that in judging voluntariness itself the jury would be influenced by the reliability of a confession it considered an accurate account of the facts. "It is now axiomatic," we said,</p>
<blockquote>"that a defendant in a criminal case is deprived of due process of law if his conviction is founded, in whole or in part, upon an involuntary confession, without regard for the truth or falsity of the confession, <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span>, and even though there is ample evidence aside from the confession to support the conviction. <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>; <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">343 U. S. 181</a></span>; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>. Equally clear is the defendant's constitutional right at some stage in the proceedings to object to the use of the confession <span class="star-pagination">*484</span> and to have a fair hearing and a reliable determination on the issue of voluntariness, a determination uninfluenced by the truth or falsity of the confession. <i>Rogers</i> v. <i><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">Richmond, supra</a></span></i><i>.</i>"<sup>[8]</sup></blockquote>
<p>We did not think it necessary, or even appropriate, in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> to announce that prosecutors would be required to meet a particular burden of proof in a <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> hearing held before the trial judge.<sup>[9]</sup> Indeed, the then-established duty to determine voluntariness had not been framed in terms of a burden of proof,<sup>[10]</sup> nor has it been since <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> was decided.<sup>[11]</sup> We could fairly assume then, as we can now, that a judge would admit into evidence only those confessions that he reliably found, at least by a preponderance of the evidence, had been made voluntarily.</p>
<p>We noted in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> that there may be a relationship between the involuntariness of a confession and its unreliability.<sup>[12]</sup> But our decision was not based in the <span class="star-pagination">*485</span> slightest on the fear that juries might misjudge the accuracy of confessions and arrive at erroneous determinations of guilt or innocence. That case was not aimed at reducing the possibility of convicting innocent men.</p>
<p>Quite the contrary, we feared that the reliability and truthfulness of even coerced confessions could impermissibly influence a jury's judgment as to voluntariness. The use of coerced confessions, whether true or false, is forbidden because the method used to extract them offends constitutional principles. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 540-541</a></span> (1961).<sup>[13]</sup> The procedure we established in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> was designed to safeguard the right of an individual, entirely apart from his guilt or innocence, not to be compelled to condemn himself by his own utterances. Nothing in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> questioned the province or capacity of juries to assess the truthfulness of confessions. Nothing in that opinion took from the jury any evidence relating to the accuracy or weight of confessions admitted into evidence. A defendant has <span class="star-pagination">*486</span> been as free since <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> as he was before to familiarize a jury with circumstances that attend the taking of his confession, including facts bearing upon its weight and voluntariness.<sup>[14]</sup> In like measure, of course, juries have been at liberty to disregard confessions that are insufficiently corroborated or otherwise deemed unworthy of belief.</p>
<p>Since the purpose that a voluntariness hearing is designed to serve has nothing whatever to do with improving the reliability of jury verdicts, we cannot accept the charge that judging the admissibility of a confession by a preponderance of the evidence undermines the mandate of <i>In re Winship,</i> <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970). Our decision in <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> was not concerned with standards for determining the admissibility of evidence or with the prosecution's burden of proof at a suppression hearing when evidence is challenged on constitutional grounds. <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> went no further than to confirm the fundamental right that protects "the accused against conviction except upon proof beyond a reasonable doubt of every fact necessary to constitute the crime with which he is charged." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#364" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 364</a></span>. A high standard of proof is <span class="star-pagination">*487</span> necessary, we said, to ensure against unjust convictions by giving substance to the presumption of innocence. <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#363" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 363</a></span>. A guilty verdict is not rendered less reliable or less consonant with <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> simply because the admissibility of a confession is determined by a less stringent standard. Petitioner does not maintain that either his confession or its voluntariness is an element of the crime with which he was charged. He does not challenge the constitutionality of the standard by which the jury was instructed to decide his guilt or innocence; nor does he question the sufficiency of the evidence that reached the jury to satisfy the proper standard of proof. Petitioner's rights under <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> have not been violated.<sup>[15]</sup></p>
<p></p>
<h2>II</h2>
<p>Even conceding that <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> is inapplicable because the purpose of a voluntariness hearing is not to implement the presumption of innocence, petitioner presses for reversal on the alternative ground that evidence offered against a defendant at a criminal trial and challenged on constitutional grounds must be determined admissible beyond a reasonable doubt in order to give adequate protection to those values that exclusionary rules are designed to serve. <i>Jackson</i> v. <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Denno, supra</a></span></i><i>,</i> an offspring of <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), requires judicial rulings on voluntariness prior to admitting confessions. <i>Miranda</i> v. <i>Arizona,</i> 384 <span class="star-pagination">*488</span> U. S. 436 (1966), excludes confessions flowing from custodial interrogations unless adequate warnings were administered and a waiver was obtained. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), and <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), make impermissible the introduction of evidence obtained in violation of a defendant's Fourth Amendment rights. In each instance, and without regard to its probative value, evidence is kept from the trier of guilt or innocence for reasons wholly apart from enhancing the reliability of verdicts. These independent values, it is urged, themselves require a stricter standard of proof in judging admissibility.</p>
<p>The argument is straightforward and has appeal. But we are unconvinced that merely emphasizing the importance of the values served by exclusionary rules is itself sufficient demonstration that the Constitution also requires admissibility to be proved beyond reasonable doubt.<sup>[16]</sup> Evidence obtained in violation of the Fourth Amendment has been excluded from federal criminal trials for many years. <i>Weeks</i> v. <i>United States, supra</i><i>.</i> The same is true of coerced confessions offered in either federal or state trials. <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U. S. 532</a></span> (1897); <i>Brown</i> v. <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Mississippi, supra</a></span></i><i>.</i> But, from our experience over this period of time no substantial evidence has accumulated that federal rights have suffered from determining admissibility by a preponderance of the evidence. Petitioner offers nothing to suggest that admissibility rulings have been unreliable or otherwise wanting in quality because not based on some higher standard. Without good cause, we are unwilling to expand currently applicable exclusionary rules by erecting additional barriers to placing truthful and probative evidence <span class="star-pagination">*489</span> before state juries and by revising the standards applicable in collateral proceedings. Sound reason for moving further in this direction has not been offered here nor do we discern any at the present time. This is particularly true since the exclusionary rules are very much aimed at deterring lawless conduct by police and prosecution and it is very doubtful that escalating the prosecution's burden of proof in Fourth and Fifth Amendment suppression hearings would be sufficiently productive in this respect to outweigh the public interest in placing probative evidence before juries for the purpose of arriving at truthful decisions about guilt or innocence.</p>
<p>To reiterate what we said in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>:</i> when a confession challenged as involuntary is sought to be used against a criminal defendant at his trial, he is entitled to a reliable and clear-cut determination that the confession was in fact voluntarily rendered. Thus, the prosecution must prove at least by a preponderance of the evidence that the confession was voluntary. Of course, the States are free, pursuant to their own law, to adopt a higher standard. They may indeed differ as to the appropriate resolution of the values they find at stake.<sup>[17]</sup></p>
<p></p>
<h2>III</h2>
<p>We also reject petitioner's final contention that, even though the trial judge ruled on his coercion claim, he was entitled to have the jury decide the claim anew. To the extent this argument asserts that the judge's determination was insufficiently reliable, it is no more persuasive than petitioner's other contentions. To the extent the position assumes that a jury is better suited than a judge to determine voluntariness, it questions the basic assumptions of <i>Jackson</i> v. <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Denno</a></span></i><i>;</i> it also ignores <span class="star-pagination">*490</span> that <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> neither raised any question about the constitutional validity of the so-called orthodox rule for judging the admissibility of confessions nor even suggested that the Constitution requires submission of voluntariness claims to a jury as well as a judge. Finally, <i>Duncan</i> v. <i>Louisiana,</i> <span class="citation" data-id="9423691"><a href="/opinion/107685/duncan-v-louisiana/" aria-description="Citation for case: Duncan v. Louisiana">391 U. S. 145</a></span> (1968), which made the Sixth Amendment right to trial by jury applicable to the States, did not purport to change the normal rule that the admissibility of evidence is a question for the court rather than the jury. Nor did that decision require that both judge and jury pass upon the admissibility of evidence when constitutional grounds are asserted for excluding it. We are not disposed to impose as a constitutional requirement a procedure we have found wanting merely to afford petitioner a second forum for litigating his claim.</p>
<p>The decision of the Court of Appeals is</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE POWELL and MR. JUSTICE REHNQUIST took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>When the prosecution, state or federal, seeks to put in evidence an allegedly involuntary confession, its admissibility is determined by the command of the Fifth Amendment that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself." <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#740" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 740</a></span> (1966); <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 7-8</a></span> (1964); <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542-543</a></span> (1897). This right against compulsory self-incrimination is the "essential mainstay" of our system of criminal prosecution, <i>Malloy</i> v. <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan"><i>Hogan, supra,</i> at 7</a></span>, "a system in which the State must establish guilt by evidence independently <span class="star-pagination">*491</span> and freely secured and may not by coercion prove its charge against an accused out of his own mouth," <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#541" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 541</a></span> (1961). What is thereby protected from governmental invasion is, quite simply, "the right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will." <i>Malloy</i> v. <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan"><i>Hogan, supra,</i> at 8</a></span>. Hence, a confession is involuntary and inadmissible unless it is "the product of a rational intellect and a free will." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#208" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 208</a></span> (1960); see <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#440" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 440</a></span> (1961).</p>
<p>Ideally, of course, a defendant's compelled utterance would never be admitted into evidence against him. As we said in <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#376" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368, 376</a></span> (1964), it is "axiomatic" that a criminal conviction cannot stand if it "is founded, in whole or in part, upon an involuntary confession . . . even though there is ample evidence aside from the confession to support the conviction." Yet I doubt that informed observers of the criminal process would deny that at least some compelled utterances slip through, even assuming scrupulous adherence to constitutional standards and the most rigorous procedural protections. <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> was an attempt to move that reality somewhat closer to the ideal. We there rejected the New York rule because it "did not afford a reliable determination of the voluntariness of the confession offered in evidence at the trial" and consequently "did not adequately protect [a defendant's] right to be free of a conviction based upon a coerced confession." <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#377" aria-description="Citation for case: Jackson v. Denno"><i>Id.,</i> at 377</a></span>. As the Court today points out, "[t]he procedure we established in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> was designed to safeguard the right of an individual, entirely apart from his guilt or innocence, not to be compelled to condemn himself by his own utterances." <i>Ante,</i> at 485.</p>
<p>There is no need to dwell upon the importance our American concept of justice attaches to preserving the <span class="star-pagination">*492</span> integrity of the constitutional privilege. Both the rule that automatically reverses a conviction when an involuntary confession was admitted at trial and the procedure established in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> for determining whether a confession was voluntary are means to further the end that no utterance of a defendant not the product of his own free choice will be used against him. The Court today reaffirms what we held in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>:</i> "[W]hen a confession challenged as involuntary is sought to be used against a criminal defendant at his trial, he is entitled to a reliable and clear-cut determination that the confession was in fact voluntarily rendered." <i>Ante,</i> at 489. But the Court goes on to hold that it follows from <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> that "the prosecution must prove at least by a preponderance of the evidence that the confession was voluntary." <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Ibid.</a></span></i> I disagree. In my view, the rationale of <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> requires the conclusion that the preponderance standard does not provide sufficient protection against the danger that involuntary confessions will be employed in criminal trials.</p>
<p>A <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> hearing normally presents the factfinder with conflicting testimony from the defendant and law enforcement officers about what occurred during the officers' interrogation of the defendant. The factfinder's resolution of this conflict is often, as a practical matter, the final resolution of the voluntariness issue. <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#390" aria-description="Citation for case: Jackson v. Denno"><i>Jackson, supra,</i> at 390-391</a></span>. This case is a typical example. Petitioner testified that he confessed because the police had beaten him; the police testified that there was no beating. As the Court notes, "[t]he trial judge resolved this credibility problem in favor of the police and ruled the confession admissible." <i>Ante,</i> at 480. When the question before the factfinder is whether to believe one or the other of two self-serving accounts of what has happened, it is apparent that the standard of persuasion will in many instances be of controlling significance. <span class="star-pagination">*493</span> See <i>Speiser</i> v. <i>Randall,</i> <span class="citation" data-id="9421696"><a href="/opinion/105751/speiser-v-randall/#525" aria-description="Citation for case: Speiser v. Randall">357 U. S. 513, 525-526</a></span> (1958). Although the Court suggests "that federal rights have [not] suffered from determining admissibility by a preponderance of the evidence" and that there has been no showing "that admissibility rulings have been unreliable. . . because not based on some higher standard," <i>ante,</i> at 488, I do not think it can be denied, given the factual nature of the ordinary voluntariness determination, that permitting a lower standard of proof will necessarily result in the admission of more involuntary confessions than would be admitted were the prosecution required to meet a higher standard. The converse, of course, is also true. Requiring the higher standard means that some voluntary confessions will be excluded as involuntary even though they would have been found voluntary under the lower standard.</p>
<p>The standard of proof required for a criminal conviction presents a similar situation, yet we have held that guilt must be established by proof beyond a reasonable doubt. <i>In re Winship,</i> <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#361" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358, 361-364</a></span> (1970); see <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#370" aria-description="Citation for case: In Re WINSHIP"><i>id.,</i> at 370-372</a></span> (Harlan, J., concurring.) Permitting proof by a preponderance of the evidence would necessarily result in the conviction of more defendants who are in fact innocent. Conversely, imposing the burden of proof beyond a reasonable doubt means that more defendants who are in fact guilty are found innocent. It seems to me that the same considerations that demand the reasonable-doubt standard when guilt or innocence is at stake also demand that standard when the question is the admissibility of an allegedly involuntary confession.</p>
<p>We permit proof by a preponderance of the evidence in civil litigation because "we view it as no more serious in general for there to be an erroneous verdict in the defendant's favor than for there to be an erroneous verdict in the plaintiff's favor." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#371" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 371</a></span> (Harlan, J., concurring). We do not take that view in criminal cases. <span class="star-pagination">*494</span> We said in <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> that the reasonable-doubt standard "is a prime instrument for reducing the risk of convictions resting on factual error. The standard provides concrete substance for the presumption of innocence . . . ." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#363" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 363</a></span>. As Mr. Justice Harlan put it in his concurring opinion, the requirement of proof beyond a reasonable doubt is "bottomed on a fundamental value determination of our society that it is far worse to convict an innocent man than to let a guilty man go free." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#372" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 372</a></span>.</p>
<p>If we permit the prosecution to prove by a preponderance of the evidence that a confession was voluntary, then, to paraphrase Mr. Justice Harlan, we must be prepared to justify the view that it is no more serious in general to admit involuntary confessions than it is to exclude voluntary confessions. I am not prepared to justify that view. Compelled self-incrimination is so alien to the American sense of justice that I see no way that such a view could ever be justified. If we are to provide "concrete substance" for the command of the Fifth Amendment that no person shall be compelled to condemn himself, we must insist, as we do at the trial of guilt or innocence, that the prosecution prove that the defendant's confession was voluntary beyond a reasonable doubt.<sup>[*]</sup> In my judgment, to paraphrase Mr. Justice <span class="star-pagination">*495</span> Harlan again, the command of the Fifth Amendment reflects the determination of our society that it is worse to permit involuntary self-condemnation than it is to deprive a jury of probative evidence. Just as we do not convict when there is a reasonable doubt of guilt, we should not permit the prosecution to introduce into evidence a defendant's confession when there is a reasonable doubt that it was the product of his free and rational choice.</p>
<p>I add only that the absolute bar against the admission of a defendant's compelled utterance at his criminal trial is fundamentally an expression of the American commitment to the moral worth of the individual. What we said in <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> bears repeating here. "[U]se of the reasonable-doubt standard is indispensable to command the respect and confidence of the community in applications of the criminal law. It is critical that the moral force of the criminal law not be diluted by a standard of proof that leaves people in doubt whether innocent men are being condemned." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#364" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 364</a></span>. I believe that it is just as critical to our system of criminal justice that when a person's words are used against him, no reasonable doubt remains that he spoke of his own free will.</p>
<h2>NOTES</h2>
<p>[1]  State courts that have considered the question since <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> have adopted a variety of standards, most of them founded upon state law. Many have sanctioned a standard of proof less strict than beyond a reasonable doubt, including proof of voluntariness by a preponderance of the evidence or to the satisfaction of the court or proof of voluntariness in fact. <i>E. g., </i><i>Duncan</i> v. <i>State,</i> <span class="citation" data-id="9656485"><a href="/opinion/1586369/duncan-v-state/" aria-description="Citation for case: Duncan v. State">278 Ala. 145</a></span>, <span class="citation" data-id="9656485"><a href="/opinion/1586369/duncan-v-state/" aria-description="Citation for case: Duncan v. State">176 So. 2d 840</a></span> (1965); <i>State</i> v. <i>Dillon,</i> <span class="citation" data-id="1402028"><a href="/opinion/1402028/state-v-dillon/" aria-description="Citation for case: State v. Dillon">93 Idaho 698</a></span>, <span class="citation" data-id="1402028"><a href="/opinion/1402028/state-v-dillon/" aria-description="Citation for case: State v. Dillon">471 P. 2d 553</a></span> (1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/942/">401 U. S. 942</a></span> (1971); <i>People</i> v. <i>Harper,</i> <span class="citation" data-id="9884438"><a href="/opinion/2047659/the-people-v-harper/" aria-description="Citation for case: The PEOPLE v. Harper">36 Ill. 2d 398</a></span>, <span class="citation" data-id="9884438"><a href="/opinion/2047659/the-people-v-harper/" aria-description="Citation for case: The PEOPLE v. Harper">223 N. E. 2d 841</a></span> (1967); <i>State</i> v. <i>Milow,</i> <span class="citation" data-id="1409161"><a href="/opinion/1409161/state-v-milow/" aria-description="Citation for case: State v. Milow">199 Kan. 576</a></span>, <span class="citation" data-id="1409161"><a href="/opinion/1409161/state-v-milow/" aria-description="Citation for case: State v. Milow">433 P. 2d 538</a></span> (1967); <i>Barnhart</i> v. <i>State,</i> <span class="citation" data-id="1515039"><a href="/opinion/1515039/barnhart-v-state/" aria-description="Citation for case: Barnhart v. State">5 Md. App. 222</a></span>, <span class="citation" data-id="1515039"><a href="/opinion/1515039/barnhart-v-state/" aria-description="Citation for case: Barnhart v. State">246 A. 2d 280</a></span> (1968); <i>Commonwealth</i> v. <i>White,</i> <span class="citation" data-id="2225068"><a href="/opinion/2225068/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">353 Mass. 409</a></span>, <span class="citation" data-id="2225068"><a href="/opinion/2225068/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">232 N. E. 2d 335</a></span> (1967); <i>State</i> v. <i>Nolan,</i> <span class="citation" data-id="1795610"><a href="/opinion/1795610/state-v-nolan/" aria-description="Citation for case: State v. Nolan">423 S. W. 2d 815</a></span> (Mo. 1968); <i>State</i> v. <i>White,</i> <span class="citation" data-id="8025470"><a href="/opinion/8067290/state-v-white/" aria-description="Citation for case: State v. White">146 Mont. 226</a></span>, <span class="citation" data-id="8025470"><a href="/opinion/8067290/state-v-white/" aria-description="Citation for case: State v. White">405 P. 2d 761</a></span> (1965), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1023/">384 U. S. 1023</a></span> (1966); <i>State</i> v. <i>Brewton,</i> <span class="citation" data-id="9794916"><a href="/opinion/2619842/state-v-brewton/" aria-description="Citation for case: State v. Brewton">238 Ore. 590</a></span>, <span class="citation" data-id="9794916"><a href="/opinion/2619842/state-v-brewton/" aria-description="Citation for case: State v. Brewton">395 P. 2d 874</a></span> (1964); <i>Commonwealth ex rel. Butler</i> v. <i>Rundle,</i> <span class="citation" data-id="1992878"><a href="/opinion/1992878/commonwealth-ex-rel-butler-v-rundle/" aria-description="Citation for case: Commonwealth Ex Rel. Butler v. Rundle">429 Pa. 141</a></span>, <span class="citation" data-id="1992878"><a href="/opinion/1992878/commonwealth-ex-rel-butler-v-rundle/" aria-description="Citation for case: Commonwealth Ex Rel. Butler v. Rundle">239 A. 2d 426</a></span> (1968); <i>Monts</i> v. <i>State,</i> <span class="citation" data-id="2374676"><a href="/opinion/2374676/monts-v-state/" aria-description="Citation for case: Monts v. State">218 Tenn. 31</a></span>, <span class="citation" data-id="2374676"><a href="/opinion/2374676/monts-v-state/" aria-description="Citation for case: Monts v. State">400 S. W. 2d 722</a></span> (1966); <i>State</i> v. <i>Davis,</i> <span class="citation" data-id="9562176"><a href="/opinion/1207372/state-v-davis/" aria-description="Citation for case: State v. Davis">73 Wash. 2d 271</a></span>, <span class="citation" data-id="9562176"><a href="/opinion/1207372/state-v-davis/" aria-description="Citation for case: State v. Davis">438 P. 2d 185</a></span> (1968).
</p>
<p>Other States, using state law or not specifying a basis, require proof beyond a reasonable doubt. <i>E. g., </i><i>State</i> v. <i>Ragsdale,</i> <span class="citation" data-id="1940977"><a href="/opinion/1940977/state-v-ragsdale/" aria-description="Citation for case: State v. Ragsdale">249 La. 420</a></span>, <span class="citation" data-id="1940977"><a href="/opinion/1940977/state-v-ragsdale/" aria-description="Citation for case: State v. Ragsdale">187 So. 2d 427</a></span> (1966), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./385/1029/">385 U. S. 1029</a></span> (1967); <i>State</i> v. <i>Keiser,</i> <span class="citation" data-id="1645241"><a href="/opinion/1645241/state-v-keiser/" aria-description="Citation for case: State v. Keiser">274 Minn. 265</a></span>, <span class="citation" data-id="1645241"><a href="/opinion/1645241/state-v-keiser/" aria-description="Citation for case: State v. Keiser">143 N. W. 2d 75</a></span> (1966); <i>State</i> v. <i>Yough,</i> 49 N. J. 587, <span class="citation" data-id="1534970"><a href="/opinion/1534970/state-v-yough/" aria-description="Citation for case: State v. Yough">231 A. 2d 598</a></span> (1967); <i>People</i> v. <i>Huntley,</i> 15 N. Y. 2d 72, <span class="citation" data-id="5521571"><a href="/opinion/5674048/people-v-huntley/" aria-description="Citation for case: People v. Huntley">204 N. E. 2d 179</a></span> (1965); <i>State</i> v. <i>Thundershield,</i> 83 S. D. 414, <span class="citation" data-id="9722826"><a href="/opinion/2128885/state-v-thundershield/" aria-description="Citation for case: State v. Thundershield">160 N. W. 2d 408</a></span> (1968); <i>State ex rel. Goodchild</i> v. <i>Burke,</i> <span class="citation" data-id="1798836"><a href="/opinion/1798836/state-ex-rel-goodchild-v-burke/" aria-description="Citation for case: State Ex Rel. Goodchild v. Burke">27 Wis. 2d 244</a></span>, <span class="citation" data-id="1798836"><a href="/opinion/1798836/state-ex-rel-goodchild-v-burke/" aria-description="Citation for case: State Ex Rel. Goodchild v. Burke">133 N. W. 2d 753</a></span> (1965), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1017/">384 U. S. 1017</a></span> (1966).</p>
<p>Two federal courts have held as an exercise of supervisory power that voluntariness must be proved beyond a reasonable doubt. <i>Ralph</i> v. <i>Warden,</i> <span class="citation" data-id="9456545"><a href="/opinion/294988/william-ralph-v-warden-maryland-penitentiary/#793" aria-description="Citation for case: William Ralph v. Warden, Maryland Penitentiary">438 F. 2d 786, 793</a></span> (CA4 1970), clarifying <i>United States</i> v. <i>Inman,</i> <span class="citation" data-id="269702"><a href="/opinion/269702/united-states-v-richard-floyd-inman/" aria-description="Citation for case: United States v. Richard Floyd Inman">352 F. 2d 954</a></span> (CA4 1965); <i>Pea</i> v. <i>United States,</i> 130 U. S. App. D. C. 66, <span class="citation" data-id="9453787"><a href="/opinion/280914/emanuel-pea-jr-v-united-states/" aria-description="Citation for case: Emanuel Pea, Jr. v. United States">397 F. 2d 627</a></span> (1967); cf. <i>United States</i> v. <i>Schipani,</i> <span class="citation" data-id="1419387"><a href="/opinion/1419387/united-states-v-schipani/" aria-description="Citation for case: United States v. Schipani">289 F. Supp. 43</a></span> (EDNY 1968), aff'd, <span class="citation" data-id="286166"><a href="/opinion/286166/united-states-v-joseph-f-schipani/" aria-description="Citation for case: United States v. Joseph F. Schipani">414 F. 2d 1262</a></span> (CA2 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./397/922/">397 U. S. 922</a></span> (1970), requiring the Government to prove beyond a reasonable doubt that certain evidence was not tainted by violation of the Fourth Amendment.</p>
<p>[2]  In ruling the confession admissible, the judge stated:
</p>
<p>"The petitioner has admitted under oath he had a struggle with the complaining witness over the gun; he was wounded, obtained a facial wound. The Officers testified he was bloody at the time he was arrested.</p>
<p>"I don't believe the defendant's testimony at all that he was beaten up by the Police. The condition he is in is well explained by the defendant himself."</p>
<p>[3]  Illinois followed what we described in <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span> (1964), as "the orthodox rule, under which the judge himself solely and finally determines the voluntariness of the confession . . . ." <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#378" aria-description="Citation for case: Jackson v. Denno"><i>Id.,</i> at 378</a></span>. While the procedures of all the States could not be neatly classified, we noted that some followed the Massachusetts procedure whereby the judge himself first resolves evidentiary conflicts and determines whether a confession is in fact voluntary. If he is unable so to conclude, the confession may not be admitted into evidence. If judged voluntary and therefore admissible, the jury must also determine the coercion issue and is instructed to ignore a confession it finds involuntary. <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Id.,</a></span></i> at 378 n. 8. Other States had adopted the New York procedure at issue in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>.</i> Our decision in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> cast no doubt upon the orthodox and Massachusetts procedures but did call into question the practice of every State that did not clearly follow one of these procedures. A thorough tabulation of what States did in the wake of <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> appears in 3 J. Wigmore, Evidence 585-593 (J. Chadbourn rev. 1970).</p>
<p>[4]  <i>People</i> v. <i>Wagoner,</i> <span class="citation" data-id="2000298"><a href="/opinion/2000298/the-people-v-wagoner/" aria-description="Citation for case: The PEOPLE v. Wagoner">8 Ill. 2d 188</a></span>, <span class="citation" data-id="2000298"><a href="/opinion/2000298/the-people-v-wagoner/" aria-description="Citation for case: The PEOPLE v. Wagoner">133 N. E. 2d 24</a></span> (1956); <i>People</i> v. <i>Thomlison,</i> <span class="citation" data-id="3420642"><a href="/opinion/3423792/the-people-v-thomlison/" aria-description="Citation for case: The People v. Thomlison">400 Ill. 555</a></span>, <span class="citation" data-id="3420642"><a href="/opinion/3423792/the-people-v-thomlison/" aria-description="Citation for case: The People v. Thomlison">81 N. E. 2d 434</a></span> (1948).</p>
<p>[5]  Respondent makes no contention here that petitioner either waived the right to adjudicate his federal claims or deliberately bypassed state procedures for testing those claims. Cf. <i>Fay</i> v. <i>Noia,</i> <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#439" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 439</a></span> (1963).</p>
<p>[6]  The Seventh Circuit's affirmance is unreported. <i>United States ex rel. Lego</i> v. <i>Pate,</i> No. 18313 (CA7 Oct. 8, 1970).</p>
<p>[7]  A more thorough description of the New York procedure is found in <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#377" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 377-391</a></span>.</p>
<p>[8]  <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#376" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 376-377</a></span>.</p>
<p>[9]  "Judge" is used here and throughout the opinion to mean a factfinder, whether trial judge or jury, at a voluntariness hearing. The proscription against permitting the jury that passes upon guilt or innocence to judge voluntariness in the same proceeding does not preclude the States from impaneling a separate jury to determine voluntariness. <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 391</a></span> n. 19.</p>
<p>[10]  See, <i>e. g., </i><i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span> (1963); <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span> (1959); <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (1958).</p>
<p>[11]  See, <i>e. g., </i><i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span> (1969); <i>Boulden</i> v. <i>Holman,</i> <span class="citation" data-id="9423981"><a href="/opinion/107893/boulden-v-holman/" aria-description="Citation for case: Boulden v. Holman">394 U. S. 478</a></span> (1969); <i>Harrison</i> v. <i>United States,</i> <span class="citation" data-id="9423779"><a href="/opinion/107736/harrison-v-united-states/" aria-description="Citation for case: Harrison v. United States">392 U. S. 219</a></span> (1968); <i>Greenwald</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9423651"><a href="/opinion/107650/greenwald-v-wisconsin/" aria-description="Citation for case: Greenwald v. Wisconsin">390 U. S. 519</a></span> (1968); <i>Clewis</i> v. <i>Texas,</i> <span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707</a></span> (1967); <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span> (1966); cf. <i>Procunier</i> v. <i>Atchley,</i> <span class="citation" data-id="108231"><a href="/opinion/108231/procunier-v-atchley/" aria-description="Citation for case: Procunier v. Atchley">400 U. S. 446</a></span> (1971).</p>
<p>[12]  We noted that coerced confessions are forbidden in part because of their "probable unreliability." <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#385" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 385-386</a></span>. However, it had been settled when this Court decided <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> that the exclusion of unreliable confessions is not the purpose that a voluntariness hearing is designed to serve. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span> (1961). The sole issue in such a hearing is whether a confession was coerced. Whether it be true or false is irrelevant; indeed, such an inquiry is forbidden. The judge may not take into consideration evidence that would indicate that the confession, though compelled, is reliable, even highly so. <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#545" aria-description="Citation for case: Rogers v. Richmond"><i>Id.,</i> at 545</a></span>. As difficult as such tasks may be to accomplish, the judge is also duty-bound to ignore implications of reliability in facts relevant to coercion and to shut from his mind any internal evidence of authenticity that a confession itself may bear.</p>
<p>[13]  In <i>Jackson,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#377" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 377-391</a></span>, we traced the genesis of the view that due process forbids the use of coerced confessions, whether or not reliable. The Court had departed from that view in <i>Stein</i> v. <i>New York,</i> <span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">346 U. S. 156</a></span> (1953), whose premise was that a confession is excludable because of its inherent untrustworthiness. The <i><span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">Stein</a></span></i> premise was repudiated in <i>Rogers</i> v. <i><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">Richmond</a></span></i> and <i><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">Rogers</a></span></i> was reaffirmed in <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#739" aria-description="Citation for case: Davis v. North Carolina">384 U. S., at 739</a></span>, and <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span>, 729 n. 9 (1966). That case continues to serve as the basis for evaluating coercion claims. See cases cited in n. 11, <i>supra.</i></p>
<p>[14]  This is the course that petitioner pursued. Cf. <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 386</a></span> n. 13. Although <span class="citation no-link">18 U. S. C. § 3501</span> (a) is inapplicable here, it is relevant to note the provisions of that section:
</p>
<p>"(a) In any criminal prosecution brought by the United States or by the District of Columbia, a confession, as defined in subsection (e) hereof, shall be admissible in evidence if it is voluntarily given. Before such confession is received in evidence, the trial judge shall, out of the presence of the jury, determine any issue as to voluntariness. If the trial judge determines that the confession was voluntarily made it shall be admitted in evidence and the trial judge shall permit the jury to hear relevant evidence on the issue of voluntariness and shall instruct the jury to give such weight to the confession as the jury feels it deserves under all the circumstances."</p>
<p>[15]  Nothing is to be gained from restating the constitutional rule as requiring proof of guilt beyond a reasonable doubt on the basis of constitutionally obtained evidence and then arguing that rights under <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> are diluted unless admissibility is governed by a high standard. Transparently, this assumes the question at issue, which is whether a confession is admissible if found voluntary by a preponderance of the evidence. <i>United States</i> v. <i>Schipani, supra,</i> n. 1, followed this unsatisfactory course in a Fourth Amendment case but stopped short of basing the decision on the Constitution.</p>
<p>[16]  It is no more persuasive to impose the stricter standard of proof as an exercise of supervisory power than as a constitutional rule. Cf. <i>Ralph</i> v. <span class="citation" data-id="9456545"><a href="/opinion/294988/william-ralph-v-warden-maryland-penitentiary/#1" aria-description="Citation for case: William Ralph v. Warden, Maryland Penitentiary"><i>Warden, supra,</i> n. 1</a></span>, clarifying <i>United States</i> v. <span class="citation" data-id="269702"><a href="/opinion/269702/united-states-v-richard-floyd-inman/#1" aria-description="Citation for case: United States v. Richard Floyd Inman"><i>Inman, supra,</i> n. 1</a></span>; <i>Pea</i> v. <i>United States, supra,</i> n. 1.</p>
<p>[17]  See cases cited in n. 1, <i>supra.</i></p>
<p>[*]  My view that the reasonable-doubt standard must be imposed upon the prosecution does not depend upon whether that standard would be more effective than some lower standard in deterring police misconduct. When a defendant challenges his confession as involuntary, "the constitutional inquiry is not whether the conduct of state officers in obtaining the confession was shocking, but whether the confession was `free and voluntary . . . .' " <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 7</a></span> (1964). It is true that the defendant will frequently allege police misconduct, as petitioner did here. Nevertheless, as we said in <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#308" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293, 308</a></span> (1963), "[a]ny questioning by police officers which <i>in fact</i> produces a confession which is not the product of a free intellect renders that confession inadmissible." (Emphasis in original.)</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Lewis v. United States (1966).json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Lewis v. United States (1966)"
type: case
citation: "385 U.S. 206 (1966)"
parallel_cite: "87 S. Ct. 424; 17 L. Ed. 2d 312"
neutral_cite: 1966 U.S. LEXIS 3
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-12-12
docket: 36
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1966-12-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Lewis v. United States (1966)"
  varies_by_point: false
  scope_note: "Good law; part of the settled misplaced-trust / false-friend line (Hoffa, Lopez, On Lee, later United States v. White) holding that undercover dealing with a willing party is no Fourth Amendment search."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107312/lewis-v-united-states/"
  cluster_id: 107312
  opinion_id: 9423294
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (undercover entry / misplaced trust)"
  - page: "[[Consent Searches]]"
    role: "Related"
related: ["[[Gouled v. United States]]"]
aliases: ["Lewis v. United States"]
tags: ["case", "fourth-amendment", "search-threshold", "undercover", "misplaced-trust", "consent", "home"]
holding: "When an occupant converts his home into a commercial center and invites an undercover agent in to transact illegal business, the agent's entry and purchase are no Fourth Amendment search; the agent may not, however, exceed the invitation to conduct a general search."
lake:
  record_id: "Lewis v. United States (1966)"
  status: verified
  projected_at: 2026-07-10
---

# Lewis v. United States (1966)

*385 U.S. 206 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

> **Disambiguation:** This is *Lewis v. United States*, 385 U.S. 206 (1966) (undercover entry / misplaced trust). Distinct from later same-named cases (e.g., 445 U.S. 55 (1980), felon-in-possession; 518 U.S. 322 (1996), petty-offense jury right), which are not part of this corpus. A bare `[[Lewis v. United States]]` link resolves here.

## Background
A federal narcotics agent, posing as a willing buyer, telephoned Lewis and was twice invited to Lewis's home to purchase marihuana. At each visit Lewis sold the agent narcotics; on the second sale he threw in an extra bag for a prospective "regular customer." The agent saw, heard, and took nothing beyond what Lewis exposed and handed over as part of the drug sale. Lewis moved to suppress, arguing the agent's deception-procured entry into his home was an unconstitutional search.

## Issue
Whether a government agent's entry into a home by the occupant's invitation, achieved by concealing his identity, to buy contraband as part of the occupant's illegal business constitutes a Fourth Amendment search.

## Rule
No search occurs. "[W]hen … the home is converted into a commercial center to which outsiders are invited for purposes of transacting unlawful business, that business is entitled to no greater sanctity than if it were carried on in a store, a garage, a car, or on the street. A government agent, in the same manner as a private person, may accept an invitation to do business and may enter upon the premises for the very purposes contemplated by the occupant." — 385 U.S. at 211. ^pin-211

The rule has a limit: it "does not mean that, whenever entry is obtained by invitation and the locus is characterized as a place of business, an agent is authorized to conduct a general search for incriminating materials" — the agent may not exceed the scope of the invitation. — [*Id.*](https://www.courtlistener.com/opinion/107312/lewis-v-united-states/#:~:text=does%20not%20mean%20that%2C%20whenever) (citing *Gouled*). ^pin-211b

## Application
"During neither of his visits to petitioner's home did the agent see, hear, or take anything that was not contemplated, and in fact intended, by petitioner as a necessary part of his illegal business." — 385 U.S. at 210. ^pin-210

Lewis chose the location and willingly admitted the agent to make the sale he sought, so there was no governmental intrusion on protected privacy and nothing was taken beyond the marihuana voluntarily transferred. The agent did no more than buy the wares offered, so no Fourth Amendment search occurred.

## Conclusion
The undercover purchase in the home was not a Fourth Amendment search; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Lewis* is a settled member of the misplaced-trust / false-friend line — a person who deals with someone who turns out to be an undercover agent assumes the risk of that misplaced trust — alongside *[[Hoffa v. United States]]*, *Lopez v. United States*, and later affirmed in *United States v. White*. Its limit (no general search beyond the invitation) traces to [[Gouled v. United States]].

## Appears on
- [[Reasonable Expectation of Privacy]] — *Related (undercover entry / misplaced trust)*
- [[Consent Searches]] — *Related*

## Sources
- *Lewis v. United States*, 385 U.S. 206 (1966) — https://www.courtlistener.com/opinion/107312/lewis-v-united-states/ — pinpoints: 210, 211.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "255ad97e50293fbe", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Lewis v. United States (1966)"}, "payload": {"all": [{"cite": "385 U.S. 206", "page": "206", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "385"}, {"cite": "87 S. Ct. 424", "page": "424", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "17 L. Ed. 2d 312", "page": "312", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "17"}, {"cite": "1966 U.S. LEXIS 3", "page": "3", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1966"}], "display": "385 U.S. 206", "official": {"cite": "385 U.S. 206", "page": "206", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "385"}, "official_selection_present": true, "record_id": "Lewis v. United States (1966)"}}
{"assertion_id": "7c09332ec3e19722", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-211b", "record_id": "Lewis v. United States (1966)"}, "payload": {"fragment": "#:~:text=does%20not%20mean%20that%2C%20whenever", "page": null, "pin_id": "pin-211b", "pinpoint_status": "star-verified", "quote": "does not mean that, whenever entry is obtained by invitation and the locus is characterized as a place of business, an agent is authorized to conduct a general search for incriminating materials", "quote_fidelity": "matched", "record_id": "Lewis v. United States (1966)", "star_marker": "211"}}
{"assertion_id": "afe04295d1c6e2b9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-210", "record_id": "Lewis v. United States (1966)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-210", "pinpoint_status": "slip-only", "quote": "During neither of his visits to petitioner's home did the agent see, hear, or take anything that was not contemplated, and in fact intended, by petitioner as a necessary part of his illegal business.", "quote_fidelity": "mismatch", "record_id": "Lewis v. United States (1966)", "star_marker": null}}
{"assertion_id": "b027f1903f12adbf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-211", "record_id": "Lewis v. United States (1966)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-211", "pinpoint_status": "slip-only", "quote": "The agent saw, heard, and took nothing beyond what Lewis exposed and handed over as part of the drug sale. Lewis moved to suppress, arguing the agent's deception-procured entry into his home was an unconstitutional search. ## Issue Whether a government agent's entry into a home by the occupant's invitation, achieved by concealing his identity, to buy contraband as part of the occupant's illegal business constitutes a Fourth Amendment search. ## Rule No search occurs.", "quote_fidelity": "mismatch", "record_id": "Lewis v. United States (1966)", "star_marker": null}}
{"assertion_id": "d8fba46b2e5101ec", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Lewis v. United States (1966)"}, "payload": {"as_of_content": "1966-12-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Lewis v. United States (1966)", "scope_note": "Good law; part of the settled misplaced-trust / false-friend line (Hoffa, Lopez, On Lee, later United States v. White) holding that undercover dealing with a willing party is no Fourth Amendment search.", "varies_by_point": false}}
```

### lake record — Lewis v. United States (1966)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lewis v. United States (1966)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lewis v. United States",
    "case_name_short": "Lewis",
    "case_name_full": "Lewis v. United States",
    "input_case_name": "Lewis v. United States (1966)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-12-12",
    "year": 1966,
    "docket": "36",
    "cluster_id": 107312,
    "lead_opinion_id": 9423294,
    "sibling_ids": [
      107312,
      9423294,
      9423295
    ],
    "absolute_url": "/opinion/107312/lewis-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8965963,
        "score": 20,
        "case_name": "Marine National Exchanges Bank v. Government of the Virgin Islands"
      },
      {
        "cluster_id": 8965961,
        "score": 20,
        "case_name": "McFaddin Express, Inc. v. Adley Corp."
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "385 U.S. 206",
      "volume": "385",
      "reporter": "U.S.",
      "page": "206",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 424",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 312",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "312",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 3",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "3",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "385 U.S. 206",
        "volume": "385",
        "reporter": "U.S.",
        "page": "206",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 424",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 312",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "312",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 3",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "3",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "385 U.S. 206",
    "official_selection": {
      "court_class": "scotus",
      "selected": "385 U.S. 206",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-211",
      "page": null,
      "quote": "The agent saw, heard, and took nothing beyond what Lewis exposed and handed over as part of the drug sale. Lewis moved to suppress, arguing the agent's deception-procured entry into his home was an unconstitutional search. ## Issue Whether a government agent's entry into a home by the occupant's invitation, achieved by concealing his identity, to buy contraband as part of the occupant's illegal business constitutes a Fourth Amendment search. ## Rule No search occurs.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-211b",
      "page": null,
      "quote": "does not mean that, whenever entry is obtained by invitation and the locus is characterized as a place of business, an agent is authorized to conduct a general search for incriminating materials",
      "star_marker": "211",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8982,
      "fragment": "#:~:text=does%20not%20mean%20that%2C%20whenever",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-210",
      "page": null,
      "quote": "During neither of his visits to petitioner's home did the agent see, hear, or take anything that was not contemplated, and in fact intended, by petitioner as a necessary part of his illegal business.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1966-12-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Lewis v. United States (1966)",
    "varies_by_point": false,
    "scope_note": "Good law; part of the settled misplaced-trust / false-friend line (Hoffa, Lopez, On Lee, later United States v. White) holding that undercover dealing with a willing party is no Fourth Amendment search.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Perry G. Blocker",
          "cluster_id": 733272,
          "cite": [
            "104 F.3d 720",
            "1997 U.S. App. LEXIS 712",
            "1997 WL 14762"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tidswell",
          "cluster_id": 8707842,
          "cite": [
            "753 F. Supp. 1001",
            "1990 U.S. Dist. LEXIS 17789",
            "1990 WL 251821"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Berry",
          "cluster_id": 8928076,
          "cite": [
            "722 F.2d 443"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Auletta",
          "cluster_id": 5994618,
          "cite": [
            "88 A.D.2d 867",
            "452 N.Y.S.2d 32",
            "1982 N.Y. App. Div. LEXIS 17187"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Barry Dean Michael, A/K/A Mike Thompson, A/K/A Mike Johnson, Defendant",
          "cluster_id": 389127,
          "cite": [
            "645 F.2d 252",
            "1981 U.S. App. LEXIS 13417"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rovinsky v. State",
          "cluster_id": 1501764,
          "cite": [
            "605 S.W.2d 578",
            "1980 Tex. Crim. App. LEXIS 1335"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pedro Amezquita v. Rafael Hernandez Colon",
          "cluster_id": 328469,
          "cite": [
            "518 F.2d 8",
            "1975 U.S. App. LEXIS 5616"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patterson v. State",
          "cluster_id": 1371382,
          "cite": [
            "212 S.E.2d 858",
            "133 Ga. App. 742",
            "1975 Ga. App. LEXIS 2268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "W. Thomas Holmes v. Waldon v. Burr, Sheriff of Pima County, Arizona",
          "cluster_id": 314071,
          "cite": [
            "486 F.2d 55"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Piazzola v. Watkins",
          "cluster_id": 8898665,
          "cite": [
            "442 F.2d 284"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Grady Monroe Holsen v. United States",
          "cluster_id": 292305,
          "cite": [
            "432 F.2d 47",
            "1970 U.S. App. LEXIS 7135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Garland William Boggus",
          "cluster_id": 284907,
          "cite": [
            "411 F.2d 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
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
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
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
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCray v. Illinois",
          "cluster_id": 107394,
          "cite": [
            "18 L. Ed. 2d 62",
            "87 S. Ct. 1056",
            "386 U.S. 300",
            "1967 U.S. LEXIS 1983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Club Retro, L.L.C. v. Hilton",
          "cluster_id": 1459439,
          "cite": [
            "568 F.3d 181",
            "2009 U.S. App. LEXIS 9864",
            "2006 WL 6245546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Davis",
          "cluster_id": 1235711,
          "cite": [
            "533 P.2d 222",
            "13 Cal. 3d 757",
            "120 Cal. Rptr. 94",
            "1975 Cal. LEXIS 208"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Martino, John Torrioni, Policardo Despaigne, A/K/A \"Paulie,\" Odell Miller, A/K/A \"Pluggy,\" John Radice, and John Perry",
          "cluster_id": 397139,
          "cite": [
            "664 F.2d 860",
            "1981 U.S. App. LEXIS 16278"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Aguilar",
          "cluster_id": 8980450,
          "cite": [
            "883 F.2d 662"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Turner",
          "cluster_id": 8910590,
          "cite": [
            "528 F.2d 143"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Larry Knohl",
          "cluster_id": 276382,
          "cite": [
            "379 F.2d 427",
            "1967 U.S. App. LEXIS 5888"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hardin",
          "cluster_id": 1427400,
          "cite": [
            "539 F.3d 404",
            "2008 U.S. App. LEXIS 18135",
            "2008 WL 3891265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Texeira",
          "cluster_id": 1409339,
          "cite": [
            "433 P.2d 593",
            "50 Haw. 138",
            "1967 Haw. LEXIS 75"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bosley v. State",
          "cluster_id": 2411414,
          "cite": [
            "414 S.W.2d 468",
            "1967 Tex. Crim. App. LEXIS 1072"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "A. A. Dietemann v. Time, Inc., a New York Corporation",
          "cluster_id": 299367,
          "cite": [
            "449 F.2d 245",
            "1 Media L. Rep. (BNA) 2417",
            "1971 U.S. App. LEXIS 8409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David T. Lace, Roger R. Ducharme, Gary D. Butts, Patricia Eckman, and Glenn Pollack",
          "cluster_id": 398901,
          "cite": [
            "669 F.2d 46",
            "1982 U.S. App. LEXIS 22855"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis Roy Choate",
          "cluster_id": 355886,
          "cite": [
            "576 F.2d 165"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Theofel v. Farey-Jones",
          "cluster_id": 8438109,
          "cite": [
            "359 F.3d 1066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wyatt",
          "cluster_id": 1389377,
          "cite": [
            "687 P.2d 544",
            "67 Haw. 293",
            "1984 Haw. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmine G. Desapio",
          "cluster_id": 293630,
          "cite": [
            "435 F.2d 272",
            "1970 U.S. App. LEXIS 6389"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Ross Phillips",
          "cluster_id": 319783,
          "cite": [
            "497 F.2d 1131"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James A. White",
          "cluster_id": 283034,
          "cite": [
            "405 F.2d 838"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arthur Fera",
          "cluster_id": 375495,
          "cite": [
            "616 F.2d 590",
            "1980 U.S. App. LEXIS 20064"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charles B. Bradley, Jr.",
          "cluster_id": 301708,
          "cite": [
            "455 F.2d 1181"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Curtis Keith Glassel",
          "cluster_id": 315375,
          "cite": [
            "488 F.2d 143",
            "1973 U.S. App. LEXIS 6619"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107312 OR 9423294 OR 9423295) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 167,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 12,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 167,
        "triage_read": 15,
        "triage_snippet_classified": 152
      },
      "lane2_top_cited": {
        "query": "cites:(107312 OR 9423294 OR 9423295)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NyZzPTEwOTE0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107312+OR+9423294+OR+9423295%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107312 OR 9423294 OR 9423295)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107312 OR 9423294 OR 9423295)",
    "indexed_citing_opinions": 236,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107312,
        "count": 145,
        "count_source": "search"
      },
      {
        "opinion_id": 9423294,
        "count": 100,
        "count_source": "search"
      },
      {
        "opinion_id": 9423295,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 885,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lewis-v-united-states-1966.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjI0OTIyMTEmcz0yNTI1NzQ5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107312+OR+9423294+OR+9423295%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107312,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 94127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 94440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 101997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 269666,
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
    "date_created": "2026-07-05T12:44:19Z",
    "date_modified": "2026-07-10T00:12:42Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:45:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:45:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:50:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:45:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Lewis v. United States (1966)

```
<opinion type="majority">
<author id="b310-15">Mr. Chief Justice Warren</author>
<p id="A82">delivered the opinion of the Court.</p>
<p id="b310-16">The question for resolution here is whether the Fourth Amendment was violated when a federal narcotics agent, <page-number citation-index="1" label="207">*207</page-number>by misrepresenting his identity and stating his willingness to purchase narcotics, was invited into petitioner’s home where an unlawful narcotics transaction was consummated and the narcotics were thereafter introduced at petitioner’s criminal trial over his objection. We hold that under the facts of this case it was not. Those facts are not disputed and may be briefly stated as follows:</p>
<p id="b311-5">On December 3, 1964, Edward Cass, an undercover federal narcotics agent, telephoned petitioner’s home to inquire about the possibility of purchasing marihuana. Cass, who previously had not met or dealt with petitioner, falsely identified himself as one “Jimmy the Pollack <em>[sic]” </em>and stated that a mutual friend had told him petitioner might be able to supply marihuana. In response, petitioner said, “Yes. I believe, Jimmy, I can take care of you,” and then directed Cass to his home where, it was indicated, a sale of marihuana would occur. Cass drove to petitioner’s home, knocked on the door, identified himself as “Jim,” and was admitted. After discussing the possibility of regular future dealings at a discounted price, petitioner led Cass to a package located on the front porch of his home. Cass gave petitioner $50, took the package, and left the premises. The package contained five bags of marihuana.<footnotemark>1</footnotemark> On December 17, 1964, a similar transaction took place, beginning with a phone conversation in which Cass identified himself as “Jimmy the Pollack” and ending with an invited visit, by Cass to petitioner’s home where a second sale of marihuana occurred. Once again, Cass paid petitioner <page-number citation-index="1" label="208">*208</page-number>$50, but this time he received in return a package containing six bags of marihuana.<footnotemark>2</footnotemark></p>
<p id="b312-6">Petitioner was arrested on April 27, 1965, and charged by a two-count indictment with violations of the narcotics laws relating to transfers of marihuana. <span class="citation no-link">26 U. S. C. § 4742</span> (a). A pretrial motion to suppress as evidence the marihuana and the conversations between petitioner and the agent was denied, and they were introduced at the trial. The District Court, sitting without a jury, convicted petitioner on both counts and imposed concurrent five-year penitentiary sentences. The Court of Appeals for the First Circuit affirmed, <span class="citation" data-id="269666"><a href="/opinion/269666/duke-lee-lewis-aka-lee-d-lewis-v-united-states/" aria-description="Citation for case: Duke Lee Lewis, A/k/a/ Lee D. Lewis v. United States">352 F. 2d 799</a></span>, and we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./382/1024/">382 U. S. 1024</a></span>.</p>
<p id="b312-7">Petitioner does not argue that he was entrapped, as he could not on the facts of this case;<footnotemark>3</footnotemark> nor does he contend that a search of his home was made or that anything other than the purchased narcotics was taken away. His only contentions are that, in the absence of a warrant, any official intrusion upon the privacy of a home constitutes a Fourth Amendment violation and that the fact the suspect invited the intrusion cannot be held a waiver when the invitation was induced by fraud and deception.</p>
<p id="b312-8">Both petitioner and the Government recognize the necessity for some undercover police activity and both concede that the particular circumstances of each case govern the admissibility of evidence obtained by stratagem or deception.<footnotemark>4</footnotemark> Indeed, it has long been acknowl<page-number citation-index="1" label="209">*209</page-number>edged by the decisions of this Court, see <em>Grimm </em>v. <em>United States, </em><span class="citation" data-id="94127"><a href="/opinion/94127/grimm-v-united-states/#610" aria-description="Citation for case: Grimm v. United States">156 U. S. 604, 610</a></span> (1895), and <em>Andrews </em>v. <em>United States, </em><span class="citation" data-id="94440"><a href="/opinion/94440/andrews-v-united-states/#423" aria-description="Citation for case: Andrews v. United States">162 U. S. 420, 423</a></span> (1896),<footnotemark>5</footnotemark> that, in the detection of many types of crime, the Government is entitled to use decoys and to conceal the identity of its agents. The various protections of the Bill of Rights, of course, provide checks upon such official deception for the protection of the individual. See, <em>e. g., Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964); <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948).</p>
<p id="b313-5">Petitioner argues that the Government overstepped the constitutional bounds in this case and places principal reliance on <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span> (1921). But a short statement of that case will demonstrate how misplaced his reliance is. There, a business acquaintance of the petitioner, acting under orders of federal officers, obtained entry into the petitioner’s office by falsely representing that he intended only to pay a social visit. In the petitioner’s absence, however, the <page-number citation-index="1" label="210">*210</page-number>intruder secretly ransacked the office and seized certain private papers of an incriminating nature. This Court had no difficulty concluding that the Fourth Amendment had been violated by the secret and general ransacking, notwithstanding that the initial intrusion was occasioned by a fraudulently obtained invitation rather than by force or stealth.</p>
<p id="b314-4">In the instant case, on the other hand, the petitioner invited the undercover agent to his home for the specific purpose of executing a felonious sale of narcotics. Petitioner’s only concern was whether the agent was a willing purchaser who could pay the agreed price. Indeed, in order to convince the agent that his patronage at petitioner’s home was desired, petitioner told him that, if he became a regular customer there, he would in the future receive an extra bag of marihuana at no additional cost; and in fact petitioner did hand over an extra bag at a second sale which was consummated at the same place and in precisely the same manner. During neither of his visits to petitioner’s home did the agent see, hear, or take anything that was not contemplated, and in fact intended, by petitioner as a necessary part of his illegal business. Were we to hold the deceptions of the agent in this case constitutionally prohibited, we would come near to a rule that the use of undercover agents in any manner is virtually unconstitutional <em>per se. </em>Such a rule would, for example, severely hamper the Government in ferreting out those organized criminal activities that are characterized by covert dealings with victims who either cannot or do not protest.<footnotemark>6</footnotemark> A prime example is provided by the narcotics traffic.</p>
<p id="b315-4"><page-number citation-index="1" label="211">*211</page-number>The fact that the undercover agent entered petitioner’s home does not compel a different conclusion. Without question, the home is accorded the full range of Fourth Amendment protections. See Amos v. <em>United States, </em><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span> (1921); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#151" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 151, n. 15</a></span> (1947). But when, as here, the home is converted into a commercial center to which outsiders are invited for purposes of transacting unlawful business, that business is entitled to no greater sanctity than if it were carried on in a store, a garage, a car, or on the street. A government agent, in the same manner as a private person, may accept an invitation to do business and may enter upon the premises for the very purposes contemplated by the occupant. Of course, this does not mean that, whenever entry is obtained by invitation and the locus is characterized as a place of business, an agent is authorized to conduct a general search for incriminating materials; a citation to the <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>case, <em>supra, </em>is sufficient to dispose of that contention.</p>
<p id="b315-5">Finally, petitioner also relies on <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span> (1960); <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960); <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948); and <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948). But those cases all dealt with the exclusion of evidence that had been forcibly seized against the suspects’ desires and without the authorization conferred by search warrants. A reading of them will readily demonstrate that they are inapposite to the facts of this case; <page-number citation-index="1" label="212">*212</page-number>and, in this area, each case must be judged on its own particular facts. Nor is <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961), in point; for there, the conduct proscribed was that of eavesdroppers, unknown and unwanted intruders who furtively listened to conversations occurring in the privacy of a house. The instant case involves no such problem; it has been well summarized by the Government at the conclusion of its brief as follows:</p>
<blockquote id="b316-4">“In short, this case involves the exercise of no governmental power to intrude upon protected premises; the visitor was invited and willingly admitted by the suspect. It concerns no design on the part of a government agent to observe or hear what was happening in the privacy of a home; the suspect chose the location where the transaction took place. It presents no question of the invasion of the privacy of a dwelling; the only statements repeated were those that were willingly made to the agent and the only things taken were the packets of marihuana voluntarily transferred to him. The pretense resulted in no breach of privacy; it merely encouraged the suspect to say things which he was willing and anxious to say to anyone who would be interested in purchasing marihuana.”</blockquote>
<p id="b316-5">Further elaboration is not necessary. The judgment is</p>
<p id="b316-6">
<em>Affirmed.</em>
</p>
<p id="b316-7">[For opinion of Douglas, J., dissenting, see <em>post, </em>p. 340.]</p>
<footnote label="1">
<p id="b311-6"> In the illegal narcotics trade, an average “bag” of marihuana contains approximately five grams of marihuana. The five bags transferred to the agent by petitioner, however, contained a quantity of marihuana measuring 31.16 grams.</p>
</footnote>
<footnote label="2">
<p id="b312-9"> The six bags transferred in this second transaction contained 40.34 grams of marihuana.</p>
</footnote>
<footnote label="3">
<p id="b312-10"> Compare <em>Sherman </em>v. <em>United States, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">356 U. S. 369</a></span> (1958), and <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span> (1932). See generally Mikell, The Doctrine of Entrapment in the Federal Courts, <span class="citation no-link">90 U. Pa. L. <em>Rev. </em>245</span> (1942).</p>
</footnote>
<footnote label="4">
<p id="b312-11"> In oral argument before this Court, counsel for petitioner conceded that information obtained by the agent in the course of his <page-number citation-index="1" label="209">*209</page-number>general undercover investigation, together with the subject matter of the first telephone conversation between the agent and petitioner, provided probable cause for believing that a narcotics offense would be committed in petitioner’s home and, therefore, would have supported the issuance of a search warrant. According to counsel, the agent’s misrepresentations would not have vitiated a magistrate’s determination of probable cause. Counsel further suggested that, if the agent had arrested petitioner at the latter’s home and then had conducted a search incidental to the arrest, no constitutional problems would be presented.</p>
</footnote>
<footnote label="5">
<p id="b313-10"> Former Chief Justice Hughes commented as follows upon the use of official deception in combating criminal activity:</p>
<blockquote id="b313-11">“Artifice and stratagem may be employed to catch those engaged in criminal enterprises. . . . The appropriate object of this permitted activity, frequently essential to the enforcement of the law, is to reveal the criminal design; to expose the illicit traffic, the prohibited publication, the fraudulent use of the mails, the illegal conspiracy, or other offenses, and thus to disclose the would-be violators of the law.” <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#441" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435, 441-442</a></span> (1932).</blockquote>
</footnote>
<footnote label="6">
<p id="b314-5"> “Particularly, in the enforcement of vice, liquor or narcotics laws, it is all but impossible to obtain evidence for prosecution save by the use of decoys. There are rarely complaining witnesses. The participants in the crime enjoy themselves. Misrepresentation by a police officer or agent concerning the identity of the purchaser of <page-number citation-index="1" label="211">*211</page-number>illegal narcotics is a practical necessity. . . . Therefore, the law must attempt to distinguish between those deceits and persuasions which are permissible and those which are not.” Model Penal Code §2.10, comment, p. 16 (Tent. Draft No. 9, 1959).</p>
<p id="b315-7">See also Donnelly, Judicial Control of Informants, Spies, Stool Pigeons and Agent Provocateurs, 60 Yale L. J. 1091, 1094 (1951); Note, <span class="citation no-link">73 Harv. L. Rev. 1333</span>, 1338-1339 (1960).</p>
</footnote>
</opinion>
```

---
