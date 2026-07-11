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

## GROUP: _overhaul2/lake/cases/Commonwealth v. Herlth.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Commonwealth v. Herlth"
type: case
citation: "2026 Pa. Super. 114 (2026)"
parallel_cite: ""
neutral_cite: 2026 Pa. Super. 114
court: Pennsylvania Superior Court
court_level: state
circuit: ""
year: 2026
date_decided: 2026-06-05
docket: 183 MDA 2024
authority_weight: "Persuasive — state, illustrative"
treatment:
  field_i_validity: good_law
  as_of_content: 2026-06-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Commonwealth v. Herlth
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10870804/com-v-herlth-j/"
  cluster_id: 10870804
  opinion_id: 11338267
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Progeny / Refinement"
related: ["[[Horton v. California]]", "[[Arizona v. Hicks]]", "[[Coolidge v. New Hampshire]]", "[[Caniglia v. Strom]]"]
aliases: ["Com. v. Herlth", "Commonwealth v. Herlth (Pa. Super. 2026)"]
tags: ["case", "fourth-amendment", "plain-view", "immediately-apparent", "closed-container", "pennsylvania", "state-appellate"]
holding: "A closed, opaque shoebox with a one-inch manufacturer's hole, inside a residence, retains a reasonable expectation of privacy; a trooper…"
lake:
  record_id: Commonwealth v. Herlth
  status: verified
  projected_at: 2026-07-09
---

# Commonwealth v. Herlth

*2026 PA Super 114 (Pa. Super. Ct. June 5, 2026)* · Pennsylvania Superior Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A state trooper entered Herlth's residence in a community-caretaking capacity while EMS treated Herlth for a drug overdose. Inside, the trooper saw a closed, opaque shoebox bearing a one-inch manufacturer's hole and shined a flashlight through the hole to view the contents — "scramble pills" — which became the basis for charges. Herlth moved to suppress; the trial court denied the motion and Herlth appealed.

## Issue
Whether the [[Plain View Doctrine|plain-view doctrine]] permitted the trooper to illuminate and view the interior of a closed, opaque container through a small hole, where the container's contents were not visible from a lawful vantage point.

## Rule
No. The [[Reading and Citing Cases#en-banc|en banc]] court restated the three-part plain-view test: "The plain view doctrine authorizes a warrantless seizure of evidence when (1) the police must observe the object from a lawful vantage point; (2) the incriminating character of the object must be immediately apparent; and (3) the police must have a lawful right of access to the object." — 2026 PA Super 114 (slip op., at 26) (quoting *Commonwealth v. Graham*, citing *Horton v. California*). ^pin-26

Applying it: "Trooper Adams failed to satisfy the second prong of the plain view test, because the object of the search, the closed shoebox, was not immediately incriminating in appearance. To the contrary, this container, a mere shoebox, appeared completely innocuous, so there was no reason to search inside it. In other words, Trooper Adams lacked probable cause to search the shoebox." — *Id.* (slip op., at [29](https://www.courtlistener.com/opinion/10870804/com-v-herlth-j/#:~:text=Trooper%20Adams%20failed%20to%20satisfy)). ^pin-29

The court rejected the "tiniest crack" theory: the Commonwealth's argument "would allow police officers to search the interior of any object from a lawful vantage point, so long as the object had even the tiniest crack or perforation. Precedent does not allow for such an unlawful intrusion." — *Id.* (slip op., at [31](https://www.courtlistener.com/opinion/10870804/com-v-herlth-j/#:~:text=tiniest%20crack)). ^pin-31

## Application
The trooper was lawfully in the living room, but the closed opaque shoebox was innocuous on its face; its incriminating character was not immediately apparent without the additional act of shining a flashlight through the manufacturer's hole. Because that additional step was itself a search the [[Plain View Doctrine|plain-view doctrine]] could not justify, and the trooper had neither a warrant nor probable cause to open the box, the search of the shoebox was unlawful on these facts.

## Conclusion
The flashlight-aided search of the closed shoebox exceeded the plain-view exception; the Superior Court held the trial court erred in denying suppression and reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Persuasive — state, illustrative** (Pennsylvania Superior Court, [[Reading and Citing Cases#en-banc|en banc]]). A recent state decision applying the immediately-apparent and lawful-access prongs of [[Horton v. California]] / [[Arizona v. Hicks]] to a closed container.

## Appears on
- [[Plain View Doctrine]] — *Key — Progeny / Refinement*

## Sources
- *Commonwealth v. Herlth*, 2026 PA Super 114 (Pa. Super. Ct. June 5, 2026) (en banc) — https://www.courtlistener.com/opinion/10870804/com-v-herlth-j/ — pinpoints: slip op., at 26, 29, 31 (CL carries the slip opinion, paginated as the Superior Court slip; cluster 10870804 → lead opinion 11338267).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "098bb984e6562c6e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Commonwealth v. Herlth"}, "payload": {"all": [{"cite": "2026 Pa. Super. 114", "page": "114", "reporter": "Pa. Super.", "selected_official": false, "source": "cluster.citations[]", "type": 8, "volume": "2026"}], "display": "2026 Pa. Super. 114", "official": {"cite": "2026 Pa. Super. 114", "page": "114", "reporter": "Pa. Super.", "selected_official": true, "source": "cluster.citations[]", "type": 8, "volume": "2026"}, "official_selection_present": true, "record_id": "Commonwealth v. Herlth"}}
{"assertion_id": "03ebe5b4231422c5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-26", "record_id": "Commonwealth v. Herlth"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-26", "pinpoint_status": "slip-only", "quote": "— which became the basis for charges. Herlth moved to suppress; the trial court denied the motion and Herlth appealed. ## Issue Whether the plain-view doctrine permitted the trooper to illuminate and view the interior of a closed, opaque container through a small hole, where the container's contents were not visible from a lawful vantage point. ## Rule No. The en banc court restated the three-part plain-view test:", "quote_fidelity": "mismatch", "record_id": "Commonwealth v. Herlth", "star_marker": null}}
{"assertion_id": "6ec9274bff8198df", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-29", "record_id": "Commonwealth v. Herlth"}, "payload": {"fragment": "#:~:text=Trooper%20Adams%20failed%20to%20satisfy", "page": null, "pin_id": "pin-29", "pinpoint_status": "slip-only", "quote": "Trooper Adams failed to satisfy the second prong of the plain view test, because the object of the search, the closed shoebox, was not immediately incriminating in appearance. To the contrary, this container, a mere shoebox, appeared completely innocuous, so there was no reason to search inside it. In other words, Trooper Adams lacked probable cause to search the shoebox.", "quote_fidelity": "matched", "record_id": "Commonwealth v. Herlth", "star_marker": null}}
{"assertion_id": "ace93a5b86b3964a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-31", "record_id": "Commonwealth v. Herlth"}, "payload": {"fragment": "#:~:text=tiniest%20crack", "page": null, "pin_id": "pin-31", "pinpoint_status": "slip-only", "quote": "tiniest crack", "quote_fidelity": "matched", "record_id": "Commonwealth v. Herlth", "star_marker": null}}
{"assertion_id": "d2252320a280cf94", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Commonwealth v. Herlth"}, "payload": {"as_of_content": "2026-06-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Commonwealth v. Herlth", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Commonwealth v. Herlth

```json
{
  "schema_version": "s2.v1",
  "record_id": "Commonwealth v. Herlth",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Com. v. Herlth, J.",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "Commonwealth v. Herlth",
    "court": "Pennsylvania Superior Court",
    "court_id": "pasuperct",
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "2026-06-05",
    "year": 2026,
    "docket": "183 MDA 2024",
    "cluster_id": 10870804,
    "lead_opinion_id": 11338267,
    "sibling_ids": [
      11338267,
      11338268
    ],
    "absolute_url": "/opinion/10870804/com-v-herlth-j/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "2026 Pa. Super. 114",
      "volume": "2026",
      "reporter": "Pa. Super.",
      "page": "114",
      "type": 8,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2026 Pa. Super. 114",
        "volume": "2026",
        "reporter": "Pa. Super.",
        "page": "114",
        "type": 8,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "2026 Pa. Super. 114",
        "volume": "2026",
        "reporter": "Pa. Super.",
        "page": "114",
        "type": 8,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "2026 Pa. Super. 114",
    "official_selection": {
      "court_class": "state",
      "selected": "2026 Pa. Super. 114",
      "reason": "selected_rank_3"
    }
  },
  "pinpoints": [
    {
      "id": "pin-26",
      "page": null,
      "quote": "\u2014 which became the basis for charges. Herlth moved to suppress; the trial court denied the motion and Herlth appealed. ## Issue Whether the plain-view doctrine permitted the trooper to illuminate and view the interior of a closed, opaque container through a small hole, where the container's contents were not visible from a lawful vantage point. ## Rule No. The en banc court restated the three-part plain-view test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-29",
      "page": null,
      "quote": "Trooper Adams failed to satisfy the second prong of the plain view test, because the object of the search, the closed shoebox, was not immediately incriminating in appearance. To the contrary, this container, a mere shoebox, appeared completely innocuous, so there was no reason to search inside it. In other words, Trooper Adams lacked probable cause to search the shoebox.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 49513,
      "fragment": "#:~:text=Trooper%20Adams%20failed%20to%20satisfy",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-31",
      "page": null,
      "quote": "tiniest crack",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 52854,
      "fragment": "#:~:text=tiniest%20crack",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2026-06-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Commonwealth v. Herlth",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11338267 OR 11338268) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR pa OR pasuperct OR pacommwct)",
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
        "query": "cites:(11338267 OR 11338268)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11338267 OR 11338268)",
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
    "complete_query": "cites:(11338267 OR 11338268)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11338267,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 11338268,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/commonwealth-v-herlth.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11338268,
        "cited_id": 148417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 1508320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 2104711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9429131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9432041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9534347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9692042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9759249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9854442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338268,
        "cited_id": 9888627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 148417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1169275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1183387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1206533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1354211,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1460504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1494964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1508320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1521287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 1993436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 2107943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 2149587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 2367721,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 2981297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 4710946,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 4968781,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 4969273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 5128806,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 5132906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 8410300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9429131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9429812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9430502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9430862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9430865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9432041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9432823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9460223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9534347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9554002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9629612,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9634816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9635383,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9702263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9759249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9805406,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9854442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9887288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 9888754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 10746023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 10794952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11338267,
        "cited_id": 10802947,
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
    "date_created": "2026-07-05T01:42:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:42:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:42:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:42:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:42:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Commonwealth v. Herlth

```
J-E03003-25

                               2026 PA Super 114

 COMMONWEALTH OF PENNSYLVANIA            :   IN THE SUPERIOR COURT OF
                                         :        PENNSYLVANIA
                                         :
              v.                         :
                                         :
                                         :
 JAMES LEE HERLTH                        :
                                         :
                   Appellant             :   No. 183 MDA 2024

     Appeal from the Judgment of Sentence Entered December 7, 2023
               In the Court of Common Pleas of York County
             Criminal Division at No: CP-67-CR-0005812-2022

BEFORE: BOWES, J., OLSON, J., STABILE, J., DUBOW, J., KUNSELMAN, J.,
        NICHOLS, J., MURRAY, J., McLAUGHLIN, J., and BECK, J.

OPINION BY STABILE, J.:                              FILED: JUNE 5, 2026

     Appellant, James Lee Herlth, appeals from his judgment of sentence of

7-14 years’ imprisonment for possession of controlled substances with intent

to deliver (“PWID”). Appellant contends that the trial court erred by denying

his motion to suppress evidence that a state trooper found during a

warrantless search of a shoebox in Appellant’s residence. We conclude that

(1) Appellant had a reasonable expectation of privacy in the contents of the

shoebox; (2) the trooper conducted a search by shining a flashlight into a

small hole in the shoebox, and (3) the search was improper under the

community caretaking and plain view exceptions to the Fourth Amendment.

We reverse the order denying suppression, vacate Appellant’s judgment of

sentence and remand for further proceedings.

     On August 31, 2020, the Pennsylvania State Police filed a criminal

complaint against Appellant charging him with PWID under 35 P.S. § 780-
J-E03003-25



113(a)(30).     On March 16, 2023, the court presided over a suppression

hearing in which the sole witness was Trooper Dylan Adams.

       Trooper Adams testified that he had been a trooper with the

Pennsylvania State Police for about six years. N.T., 3/16/23, at 4. On August

31, 2020, the trooper was on duty conducting a patrol to respond to calls in

the area. Id. At around 5:00 a.m., he responded to a report of an overdose

at 138 East Broadway in Red Lion, Pennsylvania.1 Id. This address was a

duplex, a “single building with two doors.” Id. at 5. The trooper entered one

of the doors into a living room. Three EMS paramedics were already there

providing emergency care to Appellant for an overdose. Id. at 11. The living

room was small, so the trooper could only stand in one spot and spin around

in a circle. Id. at 6.

       Trooper Adams testified that he was present to provide security to EMS

personnel because some overdose patients become violent when they are

revived with Narcan. Id. at 10. When asked whether he was assisting in any

medical capacity, Trooper Adams responded, “No, I was not. I’m not medically

trained like EMS are. We allow them to do this job.” Id. He also testified,

“We go there to see what [the patient] overdosed on to possibly make an

investigation further, anything that’s in plain view that we can see.” Id.

____________________________________________


1 The trial court did not make any findingof fact whether this address was
Appellant’s residence. Id. at 26-27 (announcement of court’s decision). The
Commonwealth acknowledges, however, that this was Appellant’s residence,
Commonwealth’s Brief at 8, 12, 22, so we will accept this as true for purposes
of this opinion.

                                           -2-
J-E03003-25



       While standing at Appellant’s feet, Trooper Adams saw a shoebox with

a closed lid.2 Id. at 6. The shoebox was “maybe not even a foot away from

me. It was sitting right next to my left leg.” Id.

       The closed shoebox had a one-inch3 manufacturer’s hole. Trooper

Adams shined his flashlight into the hole and recognized “scramble” capsules,

a narcotic consisting normally of “a mixture of different drugs but mostly

fentanyl.” Id. at 5. The scramble was directly under the hole through which

he shined his flashlight. Id. at 7. The Commonwealth does not claim that

Trooper Adams could have seen the scramble without a flashlight.         See

Commonwealth’s Brief at 19 (“all Trooper Adams needed to do in order to see

the scramble pills in the shoebox was look down and shine a flashlight through

the manufacturers’ hole”) (emphasis added). Nor does the record indicate

that the living room was dark or that a flashlight was necessary to see inside

the living room.

       It “made sense” to Trooper Adams that Appellant overdosed on

scramble. N.T., 3/16/23, at 7. He “opened the [shoe]box and seized [its

contents],” id., 117 scramble capsules in a plastic bag. Id. at 9.

____________________________________________


2 The trial court did not make any finding of fact as to whether the shoebox

belonged to Appellant. N.T., 3/16/23, at 26-27.             The Commonwealth
acknowledges, however, that the shoebox belonged to Appellant and that the
box was located where Appellant chose to place it. Commonwealth’s Brief at
13 (Appellant “placed the box. . . in the middle of his living room”).

3 Although Trooper Adams did not testify that the hole was one inch, the court

stated that the hole was one inch. Id. at 27. Furthermore, both parties assert
in their briefs that the hole was one inch.

                                           -3-
J-E03003-25



      At the conclusion of the suppression hearing, the Commonwealth argued

that Trooper Adams conducted a valid search under the plain view doctrine.

Id. at 24-26.    The trial court denied Appellant’s motion to suppress the

evidence seized from the shoebox. Id. at 26-27. The court did not find or

address whether the trooper shined his flashlight into the shoebox to help EMS

personnel provide medical assistance to Appellant.      The court simply ruled

that the trooper performed a valid search under the plain view doctrine. Id.

      A jury found Appellant guilty of PWID, and on December 7, 2023, the

court entered sentence.    On Monday, December 18, 2023, Appellant filed

timely post-sentence motions. On January 5, 2024, the court denied these

motions. On February 1, 2024, Appellant filed a timely notice of appeal. Both

Appellant and the trial court complied with Pa.R.A.P. 1925.

      Appellant raises a single issue in this appeal:

      The trial court erred when it denied Appellant’s motion to suppress
      evidence because the drugs and cash found in a closed shoebox
      in Appellant’s home were not in plain view. The officer’s use of a
      flashlight to illuminate the inside of the closed shoebox through a
      manufacturer’s hole in the box to identify the contraband was a
      search without probable cause and no exception to the warrant
      requirement applied. The search violated Appellant’s rights under
      the 4th Amendment to the U.S. Constitution and Article I, Section
      8 of the Pennsylvania Constitution.

Appellant’s Brief at 4.

      In reviewing the denial of a suppression motion,

      we are limited to determining whether the suppression court’s
      factual findings are supported by the record and whether the legal
      conclusions drawn from those facts are correct. Thus, [the]
      review of questions of law is de novo. [The] scope of review is to

                                     -4-
J-E03003-25


     consider only the evidence of the Commonwealth and so much of
     the evidence for the defense as remains uncontradicted when read
     in the context of the suppression record as a whole.

Commonwealth v. Shaffer, 653 Pa. 258, 209 A.3d 957, 968–69 (Pa. 2019).

     The Fourth Amendment provides, “The right of the people to be secure

in their persons, houses, papers, and effects, against unreasonable searches

and seizures, shall not be violated. . .”    U.S. Const., amend. IV.     “The

touchstone of Fourth Amendment analysis is whether a person has a

‘constitutionally protected reasonable expectation of privacy.’” California v.

Ciraolo, 476 U.S. 207, 211, 106 S.Ct. 1809, 90 L.Ed.2d 210 (1986) (quoting

Katz v. United States, 389 U.S. 347, 360, 88 S.Ct. 507, 19 L.Ed.2d 576

(1967) (Harlan, J., concurring)). “Protection of reasonable expectations of

privacy is the primary purpose of the prohibition against unreasonable

searches and seizures.” Commonwealth v. Saunders, 326 A.3d 888, 896

(Pa. 2024) (cleaned up). A search or seizure conducted without a warrant is

presumptively unreasonable, subject to a few specifically established, well-

delineated exceptions. Id.

     We begin by examining whether Appellant had a reasonable expectation

of privacy in the shoebox, an issue disputed by the parties to this appeal. A

person who challenges a search or seizure on Fourth Amendment grounds

must demonstrate (1) that he had a subjective expectation of privacy, and (2)

that his subjective expectation of privacy is one that society is prepared to

recognize as reasonable and legitimate. Commonwealth v. Perel, 107 A.3d

185, 188 (Pa. Super. 2014). The Fourth Amendment


                                    -5-
J-E03003-25


     protects the individual’s privacy in a variety of settings. In none
     is the zone of privacy more clearly defined than when bounded by
     the unambiguous physical dimensions of an individual’s home—a
     zone that finds its roots in clear and specific constitutional terms:
     ‘The right of the people to be secure in their . . . houses . . . shall
     not be violated.’

Payton v. New York, 445 U.S. 573, 589, 100 S.Ct. 1371, 63 L.Ed.2d 639

(1980); see also Florida v. Jardines, 569 U.S. 1, 6, 133 S.Ct. 1409, 185

L.Ed.2d 495 (2013) (“when it comes to the Fourth Amendment, the home is

first among equals”). In addition, “what a person knowingly exposes to the

public, even in his own home or office, is not a subject of Fourth Amendment

protection.” Katz, 389 U.S. at 351 (majority opinion).

     It also is well settled that “[t]he Fourth Amendment provides protection

to the owner of every container that conceals its contents from plain view.”

New Jersey v. T.L.O., 469 U.S. 325, 337 (1985). “An understanding that

personal, private effects are commonly stored in purses, backpacks, luggage,

and duffel bags can be gleaned from a casual stroll down any sidewalk. The

contents of persons’ closed containers are obscured from public view and

generally are recognized as private.” Perel, 107 A.3d at 190.

     Based on Appellant’s right to be secure in his residence, Payton,

Jardines, and the protection provided to him as an owner of the closed

shoebox, T.L.O., Perel, Appellant had a reasonable expectation of privacy in

the shoebox found in his residence.         The Commonwealth contends that

Appellant lacked a reasonable expectation of privacy because he placed the

closed shoebox in the middle of his living room, where guests were most likely

                                      -6-
J-E03003-25


to see it, instead of his bedroom. Commonwealth’s Brief at 13, 15, 65. The

plain language of the Fourth Amendment, however, guarantees an individual’s

right to be secure in his “house”. This right extends to his entire house, not

merely his bedroom, Payton, Jardines, and to the curtilage of the house as

well. Commonwealth v. Bowmaster, 101 A.3d 789, 792 (Pa. Super. 2014).

The fact that Appellant placed the closed container in his living room does not

mean that he exposed its contents to the public.

      The Commonwealth also argues that the one-inch manufacturer’s hole

“render[ed] the shoebox, even when the lid [was] shut, more analogous to an

open or clear container than a closed container,” Commonwealth’s Brief at 8,

making its contents visible to any “casual observer” and leaving Appellant

without any reasonable expectation of privacy.         Id. at 12, 16 (citing

Commonwealth v. Heidelberg, 267 A.3d 492, 504 (Pa. Super. 2021) (no

reasonable expectation of privacy in clear plastic baggies left in plain view in

automobile). We do not consider Trooper Adams’ inspection of the shoebox

“casual observation.” The contents of the shoebox were not visible to the

naked eye; Trooper Adams had to use a flashlight to peer inside the shoebox

and discern its contents.    The fact that the lid was closed indicates that

Appellant intended to “conceal its contents from plain view.” T.L.O., Perel,

supra. We therefore conclude that Appellant in fact possessed a reasonable

expectation of privacy in the shoebox whose contents were not open or visible

to any “casual observer”.


                                     -7-
J-E03003-25


      Having determined that Appellant had an expectation of privacy in the

contents of the shoe box, we next examine whether Trooper Adams performed

a search of the shoebox. The Commonwealth argues that he did not:

      Trooper Adams, from a lawful vantage point in [Appellant’s]
      residence pursuant to the emergency aid exception, merely shined
      his flashlight into the manufacturer’s hole of a shoebox laying
      beside [Appellant]. He did not manipulate or disturb the shoebox
      in any way prior to illuminating it with his flashlight. He didn’t
      even need to bend over or maneuver his body in any way to
      recognize the illuminated contraband through the manufacturer’s
      hole in the shoebox … [T]rooper Adams’ mere use of a flashlight
      was not a search.

Commonwealth’s Brief at 22.

      We disagree. Trooper Adams’ act of shining a flashlight into the hole of

the closed shoebox was a search. “A search takes place when police intrude

upon a constitutionally protected area without the individual’s explicit or

implicit permission.” Commonwealth v. Prater, 256 A.3d 1274, 1286 (Pa.

Super. 2021) (citing Jardines, 569 U.S. at 6). “[I]f contraband is left in open

view and is observed by a police officer from a lawful vantage point, there has

been no invasion of a legitimate expectation of privacy and thus no ‘search’

within the meaning of the Fourth Amendment—or at least no search

independent of the initial intrusion that gave the officers their vantage point.”

Minnesota v. Dickerson, 508 U.S. 366, 375, 113 S.Ct. 2130, 124 L.Ed.2d

334 (1993).

      Trooper Adams was inside Appellant’s residence for a proper reason,

namely, to provide security to EMS personnel while they provided medical


                                      -8-
J-E03003-25


treatment to Appellant. Thus, the trooper viewed the shoebox from a lawful

vantage point inside Appellant’s living room.     At that point, however, he

performed a search by shining a flashlight into a small hole of a closed

container found inside the living room, a “constitutionally protected area” in

which Appellant had a reasonable expectation of privacy. Prater, 256 A.3d

at 1286.

      We are not aware of any Pennsylvania decision that addresses whether

a law enforcement officer conducts a search by shining a flashlight inside a

residence into a small hole of a closed container. Although the parties refer

us to two Pennsylvania cases in which police officers used technological aids

outside of residences to inspect residential interiors, the facts in those cases

bear little resemblance to the present case.        See Commonwealth v.

Lemanski, 529      A.2d 1085     (Pa. Super. 1987); Commonwealth v.

Gindlesperger, 560 Pa. 222, 743 A.2d 898 (1998).

      In Lemanski, police observed marijuana growing in a secluded

greenhouse approximately 200 feet from the road by finding an opening in

the brush and shrubbery along the property line of the house and using

binoculars and a zoom lens through the opening. We held that the search

violated the Fourth Amendment, because the police infringed upon the

homeowner’s reasonable expectation of privacy by peering through a hole in

the shrubbery with sophisticated technology from a distance of 200 feet. Id.,

529 A.2d at 1092-93. Subsequently, in Gindlesperger, the police received


                                     -9-
J-E03003-25


tips from a confidential informant that the defendant was growing marijuana

in his basement with artificial lighting. The police used an infrared imaging

device called a “WASP” to detect the presence of unexplained heat emanating

from the basement.4 They then obtained a search warrant that resulted in

seizure of marijuana from the basement. Our Supreme Court held that use of

the WASP ran afoul of the Fourth Amendment by violating the defendant’s

reasonable expectation of privacy “in the heat-generating activities occurring

within his home.” Id., 743 A.2d at 903. We do not consider these decisions

on point, because the vantage point for the searches in these cases was

outside the residence instead of inside, and the technology used in these cases

was far more sophisticated than the flashlight herein.5

       In our view, the most persuasive decisions on the issue before us are

from other jurisdictions: State v. Tarantino, 322 N.C. 386, 368 S.E.2d 588

(1988), and People v. Hagestedt, 2025 IL 130286, 270 N.E.3d 334 (2025).6

____________________________________________


4 The opinion in Gindlesperger does not explicitly state that the police were

outside the defendant’s residence at the time they used the WASP, but it is
reasonable to infer this from the circumstances of the case. Had they been
inside the residence, they could have viewed the plants with their own eyes
and would not have needed to use the WASP.

5 The Commonwealth cites many other cases for the proposition that Trooper

Adams did not perform a search. We discuss these cases, infra.

6 “When confronted with a question heretofore unaddressed by the courts of

this Commonwealth, we may turn to the courts of other jurisdictions.
Although we are not bound by those decisions, we may use decisions from
other jurisdictions for guidance to the degree we find them useful and not
(Footnote Continued Next Page)


                                          - 10 -
J-E03003-25


       In Tarantino, a police detective (Detective Baker) received a tip that

marijuana plants were growing inside a building. The front door of the building

was padlocked, the back doors were nailed shut, and the windows were

boarded up. There were, however, quarter-inch cracks in a wall left uncovered

by wooden boarding. Detective Baker shined a flashlight through the cracks

and saw marijuana plants.          He obtained a search warrant and seized the

marijuana.

       The trial court granted Tarantino’s motion to suppress on the ground

that Detective Baker conducted a search with his flashlight that violated his

Fourth Amendment rights. The North Carolina Supreme Court affirmed. The

court distinguished Tarantino’s case from United States v. Dunn, 480 U.S.

294, 107 S.Ct. 1134, 94 L.Ed.2d 326 (1987), in which DEA agents shined

flashlights into an “essentially open front” of the defendant’s barn7 and saw a

drug laboratory. Id. at 305. The Dunn court held that the DEA agents did

not violate the Fourth Amendment because the barn’s interior was exposed to

the public from an unprotected vantage point. Id. at 304-05. The officers

were not required to “shield their eyes” from that which was exposed to public

view. Id. at 304. In contrast,


____________________________________________


incompatible with Pennsylvania law.” Commonwealth v. Choice, 345 A.3d
719, 733 n.18 (Pa. Super. 2025).

7 There was a locked waist-high gate barring entry into the barn proper, but

the interior of the barn was visible because there only was netting material
between the top of the gate and the ceiling. Id., 480 U.S. at 297.

                                          - 11 -
J-E03003-25


     [Tarantino] had a reasonable expectation of privacy in the building
     which Detective Baker inspected. The building’s padlocked front
     door, nailed back doors, and boarded windows indicate that
     [Tarantino] had a subjective expectation of privacy in his
     building’s interior. This expectation was not unreasonable even
     though there were small cracks between the boards in the
     building’s back wall. The presence of tiny cracks near the floor on
     the interior wall of a second-floor porch is not the kind of exposure
     which serves to eliminate a reasonable expectation of privacy. To
     hold otherwise would result in an unfairly exacting standard. It
     would require owners of non-residential buildings who want to
     enjoy their Fourth Amendment rights to maintain their structures
     almost as airtight containers. The Supreme Court has never
     imposed such a standard, and we decline to do so in this case.

     Nothing in the Supreme Court’s Dunn decision suggests that an
     expectation of privacy is eliminated by quarter-inch cracks in the
     back wall of an otherwise sealed building. The inquiry in Dunn
     centered on the Fourth Amendment’s requirements when law
     enforcement officials are faced with an open barn front obstructed
     only with see-through netting. The barn’s interior was fully
     exposed to anyone standing next to the netting…

     By contrast, in the instant case, Detective Baker confronted a
     nearly solid wall when he entered [Tarantino]’s porch. Boarded
     windows and nailed doors prohibited observation of the inside
     from all but the most rigorous scrutiny. To make his observations,
     Detective Baker had to bend and peer with a flashlight through
     quarter-inch cracks near the floor. Nothing indicates, as in Dunn,
     that had Detective Baker conducted his investigation during the
     day he could have viewed the building’s interior without making
     the same searching inquiry. These facts distinguish this case from
     Dunn in a constitutionally significant way. Far from demanding
     Detective Baker to avert his eyes to avoid viewing the building’s
     interior, the cracks near the porch floor required him to make a
     probing examination in order to see inside. Under these
     circumstances [Tarantino]’s reasonable expectation of privacy
     remained intact.

Id., 368 S.E.2d at 591-92.

     The Tarantino court further observed:




                                    - 12 -
J-E03003-25


      Our decision is consistent with those of other jurisdictions. In
      United States v. Bradshaw, the Fourth Circuit held that the
      defendant’s reasonable expectation of privacy in his truck’s
      interior was not eliminated by the presence of a crack where the
      back doors did not fit snugly. 490 F.2d 1097, 1101 (4th Cir.)…
      The court concluded that police officers violated the Fourth
      Amendment when they looked through the crack without a
      warrant, saw moonshine whiskey jugs, and seized them. The
      court acknowledged that the officers had a right to approach and
      stand next to the truck, but it concluded they went beyond lawful
      investigation when peering through the small space. Id. In State
      v. Kaaheena, the Hawaii Supreme Court concluded the
      defendant’s Fourth Amendment rights were violated when the
      police stood on a crate and looked through a one-inch hole in the
      drapes and blinds of a building which housed a “commercial
      establishment and some rental apartments.” 59 Haw. 23, 575
      P.2d 462, 466 (1978).          Although the police made their
      observations from a public vantage point, the court held that the
      search was impermissible because the defendant maintained his
      reasonable expectation of privacy in the building’s interior. Id.,
      575 P.2d at 467; see also Kroehler v. Scott, 391 F.Supp. 1114
      (E.D.Pa.1975) (violation of Fourth Amendment for officers to peer
      through small ceiling vents); Lorenzana v. Superior Court of
      Los Angeles County, 9 Cal.3d 626, 108 Cal.Rptr. 585, 511 P.2d
      33 (1973) (officers violated Fourth Amendment by peering
      through drawn curtains); People v. Triggs, 8 Cal.3d 884, 106
      Cal.Rptr. 408, 506 P.2d 232 (1973) (illegal search where officers
      in maintenance access area peered through vents); People v.
      Lovelace, 116 Cal.App.3d 541, 172 Cal.Rptr. 65 (1981)
      (reasonable expectation of privacy not eliminated by knotholes
      and cracks in six foot high wooden fence); State v. Biggar, 716
      P.2d 493 (1986) (reasonable expectation of privacy not eliminated
      by crack one half to one inch wide where toilet stall door did not
      close properly).

Id. at 592-93 (cleaned up).

      The critical point in Tarantino was that a small hole in an otherwise

closed building does not defeat the defendant’s reasonable expectation of

privacy in the building’s interior.    Police intrusion into such an area via

flashlight constitutes a search under the Fourth Amendment. Analogously, a

                                      - 13 -
J-E03003-25


small hole in a closed container inside an individual’s residence does not defeat

his reasonable expectation of privacy in the container.          Thus, shining a

flashlight into the hole, as Trooper Adams did here, constitutes a search.

      Hagestedt is equally as persuasive as Tarantino. Police officers in

Hagestedt entered the defendant’s residence without a warrant to assist the

fire department in investigating a reported gas leak.         One of the officers

examined the stove and saw no damage. He observed a cabinet across from

the stove that was secured shut with a chain and padlock. The cabinet was

ajar about one inch. The officer shined his flashlight through the gap and saw

marijuana in a container inside the cabinet. Id., 270 N.E.3d at 338. A second

officer pulled on the cabinet door handles, and the doors opened another inch

or two. Id. at 339. The second officer looked inside and saw marijuana inside

a container. Id. The trial court denied the defendant’s motion to suppress.

The court held that the first officer’s act of shining a flashlight was valid under

the plain view doctrine. Id. The court ruled that the second officer’s act of

pulling the cabinet open further constituted an illegal search in violation of the

Fourth Amendment, but the error was harmless because the first officer had

spotted marijuana during the flashlight search.         Id.   Subsequently, the

defendant was convicted of possession of a controlled substance.

      The Illinois Supreme Court held that the defendant had a reasonable

expectation of privacy in the cabinet. Id. at 343 (“[b]y chaining and locking

a cabinet in his kitchen, defendant took actions to protect his privacy and had


                                      - 14 -
J-E03003-25


shown that he sought to preserve the contents of the cabinet as

private…Society recognizes as reasonable a defendant’s expectation of privacy

in items concealed from plain view in closed containers, especially in a

defendant’s own home”). The court cited Tarantino for the principle that “a

defendant’s reasonable expectation of privacy is not eliminated by small

openings in otherwise closed areas.” Id. at 347.

      The court also held that the officers performed a search of the cabinet.

The court found instructive the United States Supreme Court’s analysis in

Arizona v. Hicks, 480 U.S. 321, 107 S.Ct. 1149, 94 L.Ed.2d 347 (1987). In

Hicks, police officers responded to the defendant’s apartment after a bullet

was fired through the floor of his apartment, striking and injuring a man in

the apartment below. Police officers entered the apartment, searching for the

shooter, other victims, and weapons. While in the apartment, one of police

officers noticed expensive stereo components that seemed out of place. The

officer moved some of the components and read and recorded their serial

numbers. One item was seized immediately as stolen, while the remaining

components were seized later pursuant to a warrant. The defendant filed a

motion to suppress all seized evidence.        The trial court suppressed the

evidence, and a state appellate court affirmed, finding that the officer’s act of

obtaining the serial numbers was an additional search unrelated to the exigent

circumstance of the shooting. The United States Supreme Court affirmed.

The Court reasoned that merely inspecting the parts of the stereo components


                                     - 15 -
J-E03003-25


that were visible, while lawfully in the apartment, would not be an independent

search because “it would have produced no additional invasion of defendant’s

privacy interest.” Id. at 325. When the officer moved one of the components

to view a concealed serial number, however, he conducted a search. Id. at

324-25 (“taking action, unrelated to the objectives of the authorized intrusion,

which exposed to view concealed portions of the apartment or its contents,

did produce a new invasion of defendant’s privacy unjustified by the exigent

circumstance that validated the entry”).

      The Illinois court emphasized that although Hicks concerned stereo

equipment that was moved to expose the serial number, its holding was not

limited to whether the components were moved. Instead, said the Illinois

court, Hicks found that there was a new invasion of the defendant’s privacy

when the officer took action that was “unrelated to the objectives of the

authorized intrusion.” Hagestedt, 270 N.E.3d at 345-46 (citing Hicks, 480

U.S. at 325).

      The Hagestedt court held that the officer who shined a flashlight into

the kitchen cabinet, like the officer in Hicks, took action that was unrelated

to the original objective for entering the defendant’s house.      The original

reason for entering the house, investigation of a reported gas leak, was a

proper community caretaking or public safety exception to the Fourth

Amendment. Id. at 344. By shining a flashlight into the cabinet, however,

the officer “took deliberate action that was unrelated to his authorized


                                     - 16 -
J-E03003-25


intrusion[,] [and this] constituted an independent search.” Id. at 347. The

court elaborated:

      While the cabinet itself was in plain view, its contents were not.
      The cabinet was secured with a chain and a padlock, and the chain
      was wrapped tightly around the cabinet handles. Neither [officer]
      observed the contents of the cabinet prior to taking any action.
      [The second officer’s] action was to open the doors further, which
      the trial court correctly determined was a search. [The first
      officer’s] action was to use his flashlight and an angled view
      through a small gap in an otherwise closed and locked cabinet.
      There was also no evidence that the gas leak was potentially
      coming from the locked cabinet…Thus, [the first officer] was not
      looking for a gas leak in the cabinet, nor was the cabinet
      proximate to the stove so that the use of a flashlight to illuminate
      behind the stove would have illuminated the interior of the
      cabinet. There was no testimony that the flashlight in this case
      was necessary to investigate the gas leak…Rather, the officer saw
      an admittedly suspicious cabinet, locked with a chain, and used
      his flashlight to try to see in through a small gap.

Id. at 347-48.

      Trooper Adams’ conduct was similar to the conduct of the officer in

Hagestedt who shined a flashlight into the kitchen cabinet. The officer in

Hagestedt properly entered the defendant’s residence due to an emergency

(the gas leak), but his act of shining a flashlight into the kitchen cabinet was

“unrelated to his authorized intrusion” and thus constituted an independent

search. Hagestedt, 270 N.E.3d at 347. Similarly, Trooper Adams properly

entered Appellant’s residence due to an emergency (Appellant’s overdose),

but his act of shining his flashlight into a hole in the shoebox was unrelated to

“the objectives of [his] authorized intrusion.” Id. Shining his flashlight thus




                                     - 17 -
J-E03003-25


constituted “an independent search,” id., into an area where Appellant

enjoyed a reasonable expectation of privacy. Id. at 343.

      The decisions cited by the Commonwealth for the proposition that

Trooper Adams did not perform a search, see Commonwealth’s Brief at 21-

32, are distinguishable, because the police in those cases intruded into areas

in which the defendant did not enjoy a reasonable expectation of privacy, such

as plainly visible automobile interiors or other locations visible from lawful

vantage points.

      For example, in Commonwealth v. Milyak, 508 Pa. 2, 493 A.2d 1346

(1985), our Supreme Court held that officers properly seized stolen items that

they observed in a vehicle with the aid of a flashlight. Milyak held that “no

search triggering the protection of the Fourth Amendment is conducted where

an officer observes the plainly viewable interior of a vehicle,” because

      there is no reason [a police officer] should be precluded from
      observing as an officer what would be entirely visible to him as a
      private citizen. There is no legitimate expectation of privacy ...
      shielding that portion of the interior of an automobile which may
      be viewed from outside the vehicle by either inquisitive passersby
      or diligent police officers.

Id., 493 A.2d at 1348.       Under the Fourth Amendment, however, “the

expectation of privacy with respect to one’s automobile is significantly less

than that relating to one’s home…”    Commonwealth v. Gary, 625 Pa. 183,




                                     - 18 -
J-E03003-25


91 A.3d 102, 111 (2014).8 Thus, Milyak does not apply to the search herein

of a closed container inside Appellant’s residence. Multiple other decisions

cited by the Commonwealth are inapplicable for the same reason. See Texas

v. Brown, 460 U.S. 730, 733, 103 S.Ct. 1535, 75 L.Ed.20 502 (1983)

(plurality opinion) (officer shined flashlight into car and observed balloon

containing drugs); Commonwealth v. Merkt, 600 A.2d 1297, 1299 (Pa.

Super. 1992) (citing Milyak) (officer shined flashlight into vehicle and saw

gun); see also United States v. Poller, 129 F.4th 169, 175 (2nd Cir. 2025)

(officer shined flashlight into car); United States v. Harper, 488 Fed. Appx.

63, 66-67 (6th Cir. 2012) (same); United States v. McCoy, 824 F. Supp.

467, 475 (D. Del. 1993) (same); People v. Dickinson, 928 P.2d 1309, 1312

(Colo. 1996) (same); Commonwealth v. Sergienko, 503 N.E.2d 1282,

1285-86 (Mass. 1987) (same).

       Other decisions cited by the Commonwealth are distinguishable because

the police officers shined lights from a public place or lawful vantage point into

an area or on an object in which the defendant did not have a reasonable

expectation of privacy. See United States v. Lee, 274 U.S. 559, 563, 47

S.Ct. 746, 71 L.Ed.2d 1202 (1927) (Coast Guard vessel shined searchlight



____________________________________________


8 Our Supreme Court has held that individuals enjoy a greater expectation of

privacy in their automobiles under Article I, Section 8 of the Pennsylvania
Constitution than under the Fourth Amendment.            Commonwealth v.
Alexander, 664 Pa. 145, 243 A.3d 177, 202-03 (2020). The present
discussion, however, does not concern Article I, Section 8.

                                          - 19 -
J-E03003-25


onto deck of motorboat 24 miles off Massachusetts coast, illuminating cans of

alcohol; “there was [no] exploration below decks or under hatches”);

Commonwealth v. Jones, 978 A.2d 1000, 1005 (Pa. Super. 2009) (shining

spotlight at night onto front porch of residence ten feet away did not violate

Fourth Amendment; spotlight was shined from lawful vantage point on public

street, and illuminated area would have been in plain view in daytime);

United States v. De Jesus Cruz-Mendez, 467 F.3d 1260, 1263, 1266 (10th

Cir. 2006) (officer lawfully inside residence observed cell phone in plain view

and shined flashlight on its dark screen); United States v. Law, 384 Fed.

Appx. 121, 123-24 (3rd Cir. 2010) (police officer lawfully inside apartment to

investigate domestic argument shined flashlight into open bag partially inside

open closet); State v. Johnson, 171 N.J. 192, 793 A.2d 619, 630 (2002)

(police officers investigating report of drug-dealing at night shined flashlight

and searchlight from public street; officer holding flashlight observed

defendant place object in support post of porch; without losing sight of post,

officer walked onto porch, shined flashlight into post, and found container with

drugs inside); State v. Rose, 128 Wash.2d 388, 909 P.2d 280, 283-85 (1996)

(officer who was lawfully on front porch of residence shined flashlight through

unobstructed window and saw drugs inside; no reasonable expectation of




                                     - 20 -
J-E03003-25


privacy under these circumstances, and use of flashlight did not transform

observations into a search).9

       For these reasons, the decisions advanced by the Commonwealth fail to

convince us that Trooper Adams did not perform a search.

       The dissent maintains that Trooper Adams did not perform a search.

The dissent observes that the officers in Hagestedt and Tarantino had to

“strain themselves and move their bodies, in addition to using a flashlight, in

order to see items secreted behind solidly closed objects.”       Dissent at 9.

Trooper Adams, the dissent continues, “simply illuminated his flashlight.” Id.

at 11. “The use of a flashlight to brighten an object,” the dissent concludes,

“is not, by itself, a ‘search’ as that term is used for constitutional purposes.”

Id. at 9. We disagree for two reasons.

       First, we believe the dissent misinterprets Hagestedt and Tarantino

by asserting that that the items in these cases were “secreted behind solidly

closed objects.” Dissent at 9. The objects were not solidly closed. There

were small holes through which the officers in these cases shined flashlights,

just as there was a small hole through which Trooper Adams shined his

flashlight.



____________________________________________


9 This Court reached a result similar to Rose in Commonwealth v. Shannon,

467 A.2d 850 (Pa. Super. 1983), a decision not cited by the Commonwealth.
Id. at 852 (where officers were lawfully in driveway and observed fight
through kitchen window, “the occupants’ failure to close [the] window largely
negates their expectation of privacy”).

                                          - 21 -
J-E03003-25


      Furthermore, and perhaps even more importantly, the dissent concedes

that Appellant had a reasonable expectation of privacy in the contents inside

the shoebox. Id. at 3. The shoebox was closed, reflecting an attempt to

conceal its contents from view.      There is no evidence that Trooper Adams

could see the contents inside the shoebox with his naked eye. He had to use

his flashlight to look through a small hole in the shoebox to see its contents.

To borrow the dissent’s euphemisms, even if he did not “strain himself” or

“move his body,” his use of an artificial aid to “brighten” the shoebox interior

still constituted an unlawful search into an area in which Appellant enjoyed a

reasonable expectation of privacy. See Prater, 256 A.3d at 1286 (search

occurs when “police intrude upon a constitutionally protected area without the

individual’s explicit or implicit permission”).

      The Commonwealth next argues that Trooper Adams’ presence in the

Appellant’s residence under the community caretaking doctrine to render

emergency aid gave him a lawful right of access to the shoe box. We agree

that Trooper Adams was authorized to enter Appellant’s residence without a

warrant under the community caretaking doctrine, a narrow exception to the

Fourth Amendment. We conclude, however, that Trooper Adams’ search of

the shoebox exceeded his authority under the community caretaking doctrine.

      This Court has defined the community caretaking doctrine as follows:

      Under the Fourth Amendment, searches and seizures without a
      warrant are presumptively unreasonable, subject only to
      specifically established exceptions. Certain of these exceptions
      arise in the context of law enforcement and are related to the

                                      - 22 -
J-E03003-25


     detection, investigation and prevention of criminal activity, such
     as the exigent circumstances exception, the plain view exception,
     searches incident to arrest, consent searches, automobile
     searches, and the imminent criminal activity exception.

     In addition to these crime-related exceptions, law enforcement
     officers legitimately perform community caretaking activities that
     also necessitate exception to the warrant requirement. The
     community caretaking doctrine has been characterized as
     encompassing three specific exceptions to the warrant
     requirement: the emergency aid exception, the public servant
     exception, and the automobile impoundment/inventory exception.
     Each of these exceptions contemplates that police officers engage
     in a wide variety of activities relating to the health and safety of
     citizens unrelated to the detection, investigation and prevention
     of criminal activity. Nevertheless, community caretaking activities
     must be performed in strict accordance with the Fourth
     Amendment.

     [T]he emergency aid exception . . . permits police officers to make
     warrantless entries and searches when they reasonably believe
     that a person is in need of immediate aid. As with all of the
     community caretaking exceptions, actions by police pursuant to
     the emergency aid exception must be independent from the
     detection, investigation, and acquisition of criminal evidence.

Commonwealth v. Davenport, 266 A.3d 707, 709-10 (Pa. Super. 2021)

(citations and quotations omitted).

     A warrantless intrusion under the emergency aid exception must be

commensurate with, and limited to, the perceived need to provide immediate

assistance. Commonwealth v. Wilmer, 648 Pa. 577, 194 A.3d 564, 571

(2018). In other words,

     the right of entry into the private dwelling by law enforcement
     officers terminates when either the necessary emergency
     assistance has been provided or it has been confirmed that no one
     inside needs emergency assistance. At that point, law
     enforcement officers must leave the residence unless some



                                      - 23 -
J-E03003-25


      other exception to the warrant requirement permits their
      continued presence.

Id. at 572 (emphasis in original).

      Under the community caretaking doctrine, Trooper Adams properly

entered Appellant’s residence without a warrant to help if Appellant became

violent while receiving emergency treatment from EMS paramedics for his

overdose.   The community caretaking doctrine, however, did not entitle

Trooper Adams to shine his flashlight into the shoebox.          Hagestedt is

persuasive on this point. One of the officers in Hagestedt shined his flashlight

into a small opening in a kitchen cabinet that was unrelated to the gas leak,

a “deliberate action that was unrelated to his authorized intrusion.” Id., 270

N.E.3d at 347. Similarly, Trooper Adams shined his flashlight into a hole in

the shoebox, an act unrelated to his reason for entering the residence under

the community caretaking doctrine, which was to provide help if Appellant

became violent.

      The Commonwealth insists that Trooper Adams’ purpose in shining his

flashlight into the shoebox was to assist EMS personnel, thus validating this

act under the community caretaking doctrine. See Commonwealth’s Brief at

51 (“Trooper Adams immediately recognized scramble pills; at that moment,

the contents of the shoebox became important intelligence for EMS as to what

[Appellant] overdosed on, and potentially how he overdosed on it. Opening

the shoebox potentially reveals more clues that could help EMS treat

[Appellant]”) & at 52 (“Opening the shoebox to reveal its contents served an

                                     - 24 -
J-E03003-25


essential function in that emergency aid – attempting to discern what

[Appellant] used, and how he may have used it, to better help EMS render

emergency services”). No evidence supports this thesis. Trooper Adams, the

sole witness during the suppression hearing, admitted that he did not enter

the residence to provide medical assistance, because he was not trained as

an EMT, and because three EMS workers were already providing medical

treatment to Appellant.     Trooper Adams did not testify that EMS personnel

needed to know what substance caused the overdose or asked him to find or

identify this substance.   Nor did Trooper Adams testify that he told EMS

personnel what he found in the shoebox—testimony he naturally would have

given had his role been to assist in medical treatment.

      The sole reason that Trooper Adams gave for shining his flashlight into

the box—“we go there to see what [the patient] overdosed on to possibly

make an investigation further, anything that’s in plain view that we can

see,” N.T., 3/16/23, at 10 (emphasis added)—was for the purpose of criminal

investigation, not medical assistance. This was how the prosecutor and the

trial court interpreted the trooper’s testimony. The prosecutor argued that

the trooper’s conduct was proper under the plain view doctrine. Id. at 24-26.

The prosecutor did not contend that the trooper shined his flashlight to provide

medical assistance. Similarly, the trial court stated, “The issue in this case is

limited to whether the shoebox with the round hole would be a situation where

the plain view doctrine would grant an exception to the need for a search


                                     - 25 -
J-E03003-25


warrant.” Id. at 27. Thus, by searching the interior of the shoebox with his

flashlight, Trooper Adams exceeded his authority under the community

caretaking exception.

       Finally, we consider whether the search of the shoebox was permissible

under the “plain view” exception to the Fourth Amendment. We conclude that

it was not.

       The plain view doctrine authorizes a warrantless seizure of evidence

when (1) the police must observe the object from a lawful vantage point; (2)

the incriminating character of the object must be immediately apparent10; and

(3) the police must have a lawful right of access to the object.

Commonwealth v. Graham, 721 A.2d 1075, 1079 (Pa. 1998) (citing Horton

v. California, 496 U.S. 128, 136-37 (1990)). Since any evidence seized by

police will be in plain view at the moment of seizure, the “question of whether

property in plain view of the police may be seized therefore must turn on the

legality of the intrusion that enables them to perceive and physically seize the

property in question.” Graham, 721 A.2d at 1079 (citing Texas v. Brown,

460 U.S. 730, 737 (1983)). “Plain view” provides grounds for seizure of an

item


____________________________________________


10 In other words, “the observing officer must have probable cause to believe

the evidence in question is contraband or incriminating evidence”).
Saunders, 326 A.3d at 897 (citations omitted). Probable cause exists “where
the facts and circumstances within the officer's knowledge are sufficient to
warrant a person of reasonable caution in the belief that an offense has been
or is being committed.” Id. (citations omitted).

                                          - 26 -
J-E03003-25


      when an officer’s access to an object has some prior justification
      under the Fourth Amendment. “Plain view” is perhaps better
      understood, therefore, not as an independent “exception” to the
      warrant clause, but simply as an extension of whatever the prior
      justification for an officer’s “access to an object” may be.

Graham, 721 A.2d at 1079 (citing Brown, 460 U.S. at 738-39). Graham

observed that the plain view doctrine “establishes an exception to the

requirement of a warrant not to search for an item, but to seize it.” Id. at

1080. This distinction “highlights the principle that the plain view doctrine

permits police officers to seize contraband that is in their purview if an

independent justification gives the officer a lawful right of access to the item,

but cannot, on its own, justify an officer extending his or her search for that

item.” Id.

      Trooper Adams satisfied the first prong of the plain view test,

observation from a lawful vantage point, because he was lawfully in the living

room inside Appellant’s home for a “community caretaking” function.

      Graham and our Supreme Court’s decision in Commonwealth v.

Norris, 498 Pa. 308, 446 A.2d 246 (1982), help resolve the second and third

plain view prongs. In Norris, two police officers heard loud music emanating

from the defendant’s apartment. The officers knocked on the door for several

minutes and identified themselves before breaking down the door and

conducting a limited search of the apartment. One officer seized a knife seen

on a nightstand.    The officers then thoroughly searched the bedroom and

found a gun under a mattress.         Our Supreme Court held that exigent


                                     - 27 -
J-E03003-25


circumstances justified the forcible entry into and limited search of the

apartment. Moreover, the plain view doctrine authorized the seizure of the

knife on the nightstand, because the exigencies of the situation had already

justified the intrusion into the bedroom where the knife was discovered. Id.,

446 A.2d at 250. The Court found, however, that the plain view doctrine did

not authorize the search under the mattress and the seizure of the gun,

because “[t]he gun could not have been seen without a thorough search of

the bedroom. That search occurred after defendant was securely held and

after it was apparent there was no one else in the apartment to endanger the

officers.” Id.

      In Graham, a police officer realized that an arrest warrant was issued

for one of three men he observed on a porch. He approached the group and

directed the man who was the subject of the warrant to lie down. He then

patted down one of the other men, the defendant, for weapons. After finding

no weapons, the officer shined a flashlight down into the defendant’s pocket

and found a Lifesavers Holes container. The container later was determined

to contain crack cocaine. Our Supreme Court held that the pat-down of the

defendant was a valid search to protect the officer’s safety, relying on Terry

v. Ohio, 392 U.S. 1 (1968).        The Court further held, however, that no

justification existed for shining a flashlight into the defendant’s pocket:

      [The officer] completed the search for weapons authorized under
      Terry before using his flashlight. The subsequent act of shining
      the flashlight was part and parcel of the search that put the
      contraband into plain view. Thus, the Commonwealth seeks to

                                     - 28 -
J-E03003-25


      use the plain view doctrine, not to validate seizing an already
      exposed object, but to justify an extended search and subsequent
      seizure of contraband discovered in the course of a Terry stop.
      Since the plain view doctrine cannot justify extending a
      warrantless search, we find that it cannot legitimize [the officer’s]
      flashlight-aided search of [the defendant’s] backpocket.

Graham, 721 A.2d at 1080. The Court found these facts distinguishable from

Commonwealth v. Burton, 436 A.2d 1010 (Pa. Super. 1981), in which a

police officer shined a flashlight into the backseat of a car during a nighttime

search:

      The [Commonwealth cites Burton] for the proposition that an
      officer lawfully in a position to make an observation may enhance
      his ability to see by the use of a flashlight. Burton involved a
      police officer searching a car incident to a lawful arrest for
      possession of a handgun without a permit. There, the officer
      shined his flashlight into the backseat, revealing contraband.
      The Superior Court found that seizure of the contraband was
      justified by the plain view exception even though the officer
      needed a flashlight to illuminate the contraband. However, the
      reasoning behind Burton, that a flashlight may properly
      illuminate items that would be in plain view during
      daylight hours, does not apply here, as the Lifesavers
      Holes container was not an exposed object.

Graham, 721 A.2d at 1080 (emphasis added).

      In the present case, Trooper Adams failed to satisfy the second prong of

the plain view test, because the object of the search, the closed shoebox, was

not immediately incriminating in appearance. To the contrary, this container,

a mere shoebox, appeared completely innocuous, so there was no reason to

search inside it.   In other words, Trooper Adams lacked probable cause to

search the shoebox. Saunders, 326 A.3d at 897 (equating second prong of

plain view test with probable cause). Nor did Trooper Adams satisfy the third

                                     - 29 -
J-E03003-25


prong because he lacked a lawful right of access to the scramble pills inside the

container. The trooper was only present to provide help if Appellant became

unruly during emergency treatment for a drug overdose.             Under these

circumstances, the trooper had no reason to shine his flashlight into the

manufacturer’s hole of the container, and there was no way for him to see the

scramble pills inside the container without taking this unjustified step. Nor did

the trooper possess a warrant to search the box or demonstrate probable cause

under exigent circumstances that justified a warrantless search of the shoebox.

      Norris and Graham support our decision. In both cases, police officers

conducted an initial search that was proper under the Fourth Amendment.

The items subsequently seized and suppressed were not in plain view despite

the officers having a lawful right to be in the place searched. The present

case is slightly different, because Trooper Adams did not enter the home to

conduct a valid search but instead entered under the community caretaking

doctrine. The initial search herein was Trooper Adams’ flashlight search of the

shoebox, which plainly was improper under the second and third prongs of the

plain view doctrine. As in Norris and Graham, the proper remedy for this

illegal search is suppression of the evidence seized during the search.

      The Commonwealth cites multiple cases which held that the plain view

doctrine was satisfied where a police officer shined a flashlight at night to

illuminate objects that would have been plainly visible during daytime. See,

e.g., Jones, 978 A.2d at 1005; Merkt, 600 A.2d at 1299. We acknowledge,


                                    - 30 -
J-E03003-25


as did Graham, that a police officer can shine his flashlight at nighttime to

illuminate items that would be plainly visible during the daytime.       This

principle, however, does not apply here, because the scramble pills were in a

closed container and would not have been plainly visible with or without the

use of a flashlight had the room been dark and then illuminated at the time

the shoebox was searched.

      The    Commonwealth     argues    that   Norris   and    Graham     are

distinguishable from the present case because the officers in these cases

moved or manipulated objects to reveal incriminating evidence that were not

previously visible, while Trooper Adams did not move anything. We disagree.

Although the officers in Norris and Graham moved or manipulated some

object in order to find incriminating evidence, we know of no requirement that

an officer must move or manipulate an object in order to invalidate a search

under plain view principles. Furthermore, taken to its logical extreme, the

Commonwealth’s argument would allow police officers to search the interior

of any object from a lawful vantage point, so long as the object had even the

tiniest crack or perforation. Precedent does not allow for such an unlawful

intrusion.

      For these reasons, we hold that the trial court erred by denying

Appellant’s motion to suppress. We reverse the order denying suppression,

vacate Appellant’s judgment of sentence and remand to the trial court for

further proceedings.


                                    - 31 -
J-E03003-25


      Order denying suppression reversed. Judgment of sentence vacated.

Case remanded for further proceedings. Jurisdiction relinquished.

      Judge Olson, Judge Dubow, Judge Kunselman, Judge Murray, and Judge

Beck join the opinion.

      Judge Bowes files a dissenting opinion, which Judge Nichols and Judge

McLaughlin join.




Judgment Entered.




Benjamin D. Kohler, Esq.
Prothonotary



Date: 06/05/2026




                                   - 32 -

```

---

## GROUP: _overhaul2/lake/cases/Cone v. Bell.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Cone v. Bell"
type: case
citation: "556 U.S. 449 (2009)"
parallel_cite: "129 S. Ct. 1769; 173 L. Ed. 2d 701"
neutral_cite: 2009 U.S. LEXIS 3298
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-04-28
docket: 07-1114
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-04-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Cone v. Bell
  varies_by_point: false
  scope_note: "Good law. Confirms Brady's disclosure duty reaches evidence material to punishment, not just guilt, and that a state court's mistaken 'previously determined' ruling does not procedurally bar federal habeas review of the Brady claim."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145883/cone-v-bell/"
  cluster_id: 145883
  opinion_id: 145883
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[United States v. Bagley]]", "[[Kyles v. Whitley]]", "[[Strickler v. Greene]]", "[[Banks v. Dretke]]", "[[Giglio v. United States]]"]
aliases: []
tags: ["case", "brady", "giglio", "materiality", "sentencing", "procedural-default", "due-process", "capital"]
holding: "Brady's disclosure obligation extends to evidence material to punishment as well as guilt; a state court's mistaken belief that a claim was 'previously determined' does not bar federal habeas review. Although the suppressed drug-impairment evidence was not material to guilt, the lower courts failed to assess its materiality to the death sentence, requiring remand."
lake:
  record_id: Cone v. Bell
  status: verified
  projected_at: 2026-07-06
---

# Cone v. Bell

*556 U.S. 449 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gary Cone was convicted of the 1980 murders of an elderly Memphis couple and sentenced to death. His defense was that chronic amphetamine addiction — which he traced to combat service in Vietnam — left him impaired or insane. Years later, after gaining access to the prosecutor's file, Cone discovered witness statements and documents the State had suppressed that corroborated his drug impairment around the time of the crimes. The Tennessee courts treated his *[[Brady v. Maryland|Brady]]* claim as "previously determined," and the federal courts found it defaulted and, in any event, not material to guilt.

## Issue
Whether Cone's *[[Brady v. Maryland|Brady]]* claim was procedurally barred from federal [[Common Legal Terms#habeas-corpus|habeas]] review, and whether the suppressed evidence — even if not material to guilt — had to be assessed for materiality to his death sentence.

## Rule
*[[Brady v. Maryland|Brady]]* reaches evidence material to punishment. "[W]hen the State withholds from a criminal defendant evidence that is material to his guilt or punishment, it violates his right to due process of law in violation of the Fourteenth Amendment." — 556 U.S. at 469. ^pin-469

Materiality follows the unified *[[United States v. Bagley|Bagley]]* test: "evidence is 'material' within the meaning of *Brady* when there is a reasonable probability that, had the evidence been disclosed, the result of the proceeding would have been different." — 556 U.S. at 470. ^pin-470

The Court added that disclosure obligations may run broader than the constitutional floor: "the obligation to disclose evidence favorable to the defense may arise more broadly under a prosecutor's ethical or statutory obligations." — 556 U.S. at 470 n.15. ^pin-470b

A mistaken state procedural ruling does not bar review. Because Cone "properly preserved and exhausted his *Brady* claim in the state court," it was "not defaulted," and the state courts' erroneous belief that the claim had been "previously determined" created no obstacle to federal merits review. — 556 U.S. at 469.

## Application
The Court held the *[[Brady v. Maryland|Brady]]* claim was not procedurally defaulted: Cone raised it in state court, and the state courts' "previously determined" disposition rested on a mistaken premise, so it did not bar federal review. On the merits, the suppressed witnesses' statements and documents all "strengthen[ed] the inference that Cone was impaired by his use of drugs." While that evidence was not material to whether Cone committed murder with the requisite mental state, the District Court and Court of Appeals never separately assessed whether the same evidence was material to his *sentence* — i.e., whether it might have led at least one juror to choose life over death. Because the suppressed evidence "may well have been material to the jury's assessment of the proper punishment," a full review was required.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]. The *[[Brady v. Maryland|Brady]]* claim was not defaulted, and the lower courts had to determine in the first instance whether there was a reasonable probability the withheld evidence would have altered at least one juror's sentencing decision — *[[Brady v. Maryland|Brady]]* materiality is assessed as to punishment, not only guilt.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Stevens, J.; Roberts, C.J., concurring in part; Thomas, J., joined in part by Alito, J., dissenting).
- *Cone* applies the [[Brady v. Maryland]] rule and the unified materiality standard of [[United States v. Bagley]] / [[Kyles v. Whitley]] / [[Strickler v. Greene]] to the sentencing phase, and cites [[Banks v. Dretke]] for the "put the whole case in such a different light" formulation. No negative treatment.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Cone v. Bell*, 556 U.S. 449 (2009) — https://www.courtlistener.com/opinion/145883/cone-v-bell/ — pinpoints: 469, 470 (& n.15). (CourtListener carries the slip opinion, paginated "556 U.S. ___"; U.S. Reports pages supplied from the official reporter.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3dcf3131d4291eca", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Cone v. Bell"}, "payload": {"all": [{"cite": "556 U.S. 449", "page": "449", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "556"}, {"cite": "129 S. Ct. 1769", "page": "1769", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "129"}, {"cite": "173 L. Ed. 2d 701", "page": "701", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "173"}, {"cite": "2009 U.S. LEXIS 3298", "page": "3298", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2009"}], "display": "556 U.S. 449", "official": {"cite": "556 U.S. 449", "page": "449", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "556"}, "official_selection_present": true, "record_id": "Cone v. Bell"}}
{"assertion_id": "7cdd9d82332e2ddb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-469", "record_id": "Cone v. Bell"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-469", "pinpoint_status": "slip-only", "quote": "and the federal courts found it defaulted and, in any event, not material to guilt. ## Issue Whether Cone's *Brady* claim was procedurally barred from federal habeas review, and whether the suppressed evidence — even if not material to guilt — had to be assessed for materiality to his death sentence. ## Rule *Brady* reaches evidence material to punishment.", "quote_fidelity": "mismatch", "record_id": "Cone v. Bell", "star_marker": null}}
{"assertion_id": "afdd25e3634e254e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-470b", "record_id": "Cone v. Bell"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-470b", "pinpoint_status": "slip-only", "quote": "the obligation to disclose evidence favorable to the defense may arise more broadly under a prosecutor's ethical or statutory obligations.", "quote_fidelity": "mismatch", "record_id": "Cone v. Bell", "star_marker": null}}
{"assertion_id": "eaea118567a41b4c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-470", "record_id": "Cone v. Bell"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-470", "pinpoint_status": "slip-only", "quote": "evidence is 'material' within the meaning of *Brady* when there is a reasonable probability that, had the evidence been disclosed, the result of the proceeding would have been different.", "quote_fidelity": "mismatch", "record_id": "Cone v. Bell", "star_marker": null}}
{"assertion_id": "1bb73638b9bb1f13", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Cone v. Bell"}, "payload": {"as_of_content": "2009-04-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Cone v. Bell", "scope_note": "Good law. Confirms Brady's disclosure duty reaches evidence material to punishment, not just guilt, and that a state court's mistaken 'previously determined' ruling does not procedurally bar federal habeas review of the Brady claim.", "varies_by_point": false}}
```

### lake record — Cone v. Bell

```json
{
  "schema_version": "s2.v1",
  "record_id": "Cone v. Bell",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Cone v. Bell",
    "case_name_short": "Cone",
    "case_name_full": "Cone v. Bell, Warden",
    "input_case_name": "Cone v. Bell",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-04-28",
    "year": 2009,
    "docket": "07-1114",
    "cluster_id": 145883,
    "lead_opinion_id": 145883,
    "sibling_ids": [
      145883,
      9435356,
      9435357,
      9435358
    ],
    "absolute_url": "/opinion/145883/cone-v-bell/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "556 U.S. 449",
      "volume": "556",
      "reporter": "U.S.",
      "page": "449",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 1769",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 701",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "701",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 3298",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3298",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "556 U.S. 449",
        "volume": "556",
        "reporter": "U.S.",
        "page": "449",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 1769",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 701",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "701",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 3298",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3298",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "556 U.S. 449",
    "official_selection": {
      "court_class": "scotus",
      "selected": "556 U.S. 449",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-469",
      "page": null,
      "quote": "and the federal courts found it defaulted and, in any event, not material to guilt. ## Issue Whether Cone's *Brady* claim was procedurally barred from federal habeas review, and whether the suppressed evidence \u2014 even if not material to guilt \u2014 had to be assessed for materiality to his death sentence. ## Rule *Brady* reaches evidence material to punishment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-470",
      "page": null,
      "quote": "evidence is 'material' within the meaning of *Brady* when there is a reasonable probability that, had the evidence been disclosed, the result of the proceeding would have been different.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-470b",
      "page": null,
      "quote": "the obligation to disclose evidence favorable to the defense may arise more broadly under a prosecutor's ethical or statutory obligations.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-04-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Cone v. Bell",
    "varies_by_point": false,
    "scope_note": "Good law. Confirms Brady's disclosure duty reaches evidence material to punishment, not just guilt, and that a state court's mistaken 'previously determined' ruling does not procedurally bar federal habeas review of the Brady claim.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Scott Panetti v. Lorie Davis, Director",
          "cluster_id": 4408050,
          "cite": [
            "863 F.3d 366",
            "2017 WL 2953154",
            "2017 U.S. App. LEXIS 12390"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "JAMES J. DORSEY v. UNITED STATES",
          "cluster_id": 4370480,
          "cite": [
            "154 A.3d 106",
            "2017 WL 728705",
            "2017 D.C. App. LEXIS 14"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Taylor v. Connelly",
          "cluster_id": 7306337,
          "cite": [
            "18 F. Supp. 3d 242",
            "2014 WL 1814153",
            "2014 U.S. Dist. LEXIS 63236"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lebere v. Abbott",
          "cluster_id": 1085878,
          "cite": [
            "732 F.3d 1224",
            "2013 U.S. App. LEXIS 21131",
            "2013 WL 5663866"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Cain",
          "cluster_id": 620666,
          "cite": [
            "181 L. Ed. 2d 571",
            "132 S. Ct. 627",
            "565 U.S. 73",
            "2012 U.S. LEXIS 576"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffrey Wogenstahl v. Betty Mitchell",
          "cluster_id": 621975,
          "cite": [
            "668 F.3d 307",
            "2012 WL 310819",
            "2012 U.S. App. LEXIS 1905"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Secretary, Pennsylvania Department of Corrections",
          "cluster_id": 4250271,
          "cite": [
            "834 F.3d 263",
            "2016 U.S. App. LEXIS 15434",
            "2016 WL 4440925"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Verdugo",
          "cluster_id": 1801961,
          "cite": [
            "50 Cal. 4th 263",
            "236 P.3d 1035",
            "113 Cal. Rptr. 3d 803",
            "2010 Cal. LEXIS 7524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Conway",
          "cluster_id": 2718013,
          "cite": [
            "763 F.3d 115",
            "2014 WL 3953234",
            "2014 U.S. App. LEXIS 15589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grant v. Royal",
          "cluster_id": 4482788,
          "cite": [
            "886 F.3d 874"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turner v. United States",
          "cluster_id": 4403802,
          "cite": [
            "582 U.S. 313",
            "2017 U.S. LEXIS 4041",
            "137 S. Ct. 1885",
            "198 L. Ed. 2d 443",
            "26 Fla. L. Weekly Fed. S 700",
            "85 U.S.L.W. 4488",
            "2017 WL 2674152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Moore",
          "cluster_id": 222130,
          "cite": [
            "651 F.3d 30",
            "397 U.S. App. D.C. 148",
            "2011 U.S. App. LEXIS 15666",
            "2011 WL 3211511"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jalowiec v. Bradshaw",
          "cluster_id": 613237,
          "cite": [
            "657 F.3d 293",
            "2011 U.S. App. LEXIS 18570",
            "2011 WL 3903439"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Verdugo",
          "cluster_id": 2389003,
          "cite": [
            "50 Cal. 4th 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Runningeagle v. Schriro",
          "cluster_id": 804607,
          "cite": [
            "686 F.3d 758",
            "2012 WL 2913810",
            "2012 U.S. App. LEXIS 14682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marcos Poventud v. City of New York",
          "cluster_id": 2649520,
          "cite": [
            "750 F.3d 121",
            "2014 WL 182313",
            "2014 U.S. App. LEXIS 864"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brooks v. Tennessee",
          "cluster_id": 179722,
          "cite": [
            "626 F.3d 878",
            "2010 U.S. App. LEXIS 24025",
            "2010 WL 4721099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Belnap v. Iasis Healthcare",
          "cluster_id": 4336218,
          "cite": [
            "844 F.3d 1272",
            "2017 WL 56277",
            "2017 U.S. App. LEXIS 180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Downs v. Lape",
          "cluster_id": 613588,
          "cite": [
            "657 F.3d 97",
            "2011 U.S. App. LEXIS 18921",
            "2011 WL 4057173"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Caro",
          "cluster_id": 261,
          "cite": [
            "597 F.3d 608",
            "2010 U.S. App. LEXIS 5511",
            "2010 WL 963201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florencio Dominguez v. Scott Kernan",
          "cluster_id": 4546317,
          "cite": [
            "906 F.3d 1127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mason v. Allen",
          "cluster_id": 146270,
          "cite": [
            "605 F.3d 1114",
            "2010 U.S. App. LEXIS 9646",
            "2010 WL 1856165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henness v. Bagley",
          "cluster_id": 220347,
          "cite": [
            "644 F.3d 308",
            "2011 U.S. App. LEXIS 13656",
            "2011 WL 2621896"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ulbricht",
          "cluster_id": 4395694,
          "cite": [
            "858 F.3d 71",
            "2017 WL 2346566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Harris v. Sheryl Thompson",
          "cluster_id": 810477,
          "cite": [
            "698 F.3d 609",
            "2012 WL 4944325",
            "2012 U.S. App. LEXIS 21727"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Danberg",
          "cluster_id": 1380327,
          "cite": [
            "594 F.3d 210",
            "2010 U.S. App. LEXIS 2100",
            "2010 WL 337319"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shun Warren v. Michael Baenen",
          "cluster_id": 857090,
          "cite": [
            "712 F.3d 1090",
            "2013 WL 1316905",
            "2013 U.S. App. LEXIS 6674"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. WARRIOR",
          "cluster_id": 2330570,
          "cite": [
            "277 P.3d 1111",
            "294 Kan. 484",
            "2012 WL 1648899",
            "2012 Kan. LEXIS 255"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cone v. Bell:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145883 OR 9435356 OR 9435357 OR 9435358) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzU1MDk3NjAwMDAwJnM9MTA0NTQ5NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145883+OR+9435356+OR+9435357+OR+9435358%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(145883 OR 9435356 OR 9435357 OR 9435358)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MCZzPTYxODQ2OSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145883+OR+9435356+OR+9435357+OR+9435358%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145883 OR 9435356 OR 9435357 OR 9435358)",
        "reviewed": 38,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 38,
        "triage_read": 0,
        "triage_snippet_classified": 38
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145883 OR 9435356 OR 9435357 OR 9435358)",
    "indexed_citing_opinions": 354,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145883,
        "count": 278,
        "count_source": "search"
      },
      {
        "opinion_id": 9435356,
        "count": 82,
        "count_source": "search"
      },
      {
        "opinion_id": 9435357,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435358,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1062,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/cone-v-bell.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NzQ4OTcmcz05NDk3MjcxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28145883+OR+9435356+OR+9435357+OR+9435358%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145883,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 107015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 111822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 112640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 112642,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 112665,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 112773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 118509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 130159,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 131165,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 134723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 137745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 145648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 145691,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 145719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 417963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 552438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 571286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 589636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 683594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 747610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 759546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 763114,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 772305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 772513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 783551,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 789238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 793149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 797540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 799980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1060393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1082314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1446767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1460405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1505581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1524614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 1687210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 2438728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145883,
        "cited_id": 2468521,
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
    "date_created": "2026-07-05T00:47:54Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:48:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:48:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:52:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:48:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Cone v. Bell

```
(Slip Opinion)              OCTOBER TERM, 2008                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                       CONE v. BELL, WARDEN

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE SIXTH CIRCUIT

   No. 07–1114. Argued December 9, 2008—Decided April 28, 2009
After the State discredited petitioner Cone’s defense that he killed two
  people while suffering from acute psychosis caused by drug addiction,
  he was convicted and sentenced to death. The Tennessee Supreme
  Court affirmed on direct appeal and the state courts denied postcon
  viction relief. Later, in a second petition for state postconviction re
  lief, Cone raised the claim that the State had violated Brady v. Mary
  land, 373 U. S. 83, by suppressing witness statements and police
  reports that would have corroborated his insanity defense and bol
  stered his case in mitigation of the death penalty. The postconviction
  court denied him a hearing on the ground that the Brady claim had
  been previously determined, either on direct appeal or in earlier col
  lateral proceedings. The State Court of Criminal Appeals affirmed.
  Cone then filed a petition for a writ of habeas corpus in Federal Dis
  trict Court. That Court denied relief, holding the Brady claim proce
  durally barred because the state courts’ disposition rested on ade
  quate and independent state grounds: Cone had waived it by failing
  to present his claim in state court. Even if he had not defaulted the
  claim, ruled the court, it would fail on its merits because none of the
  withheld evidence would have cast doubt on his guilt. The Sixth Cir
  cuit agreed with the latter conclusion, but considered itself barred
  from reaching the claim’s merits because the state courts had ruled
  the claim previously determined or waived under state law.
Held:
    1. The state courts’ rejection of Cone’s Brady claim does not rest on
 a ground that bars federal review. Neither of the State’s asserted
 justifications for such a bar—that the claim was decided by the State
 Supreme Court on direct review or that Cone had waived it by never
 properly raising it in state court—provides an independent and ade
2                             CONE v. BELL

                                  Syllabus

    quate state ground for denying review of Cone’s federal claim. The
    state postconviction court’s denial of the Brady claim on the ground it
    had been previously determined in state court rested on a false prem
    ise: Cone had not presented the claim in earlier proceedings and, con
    sequently, the state courts had not passed on it. The Sixth Circuit’s
    rejection of the claim as procedurally defaulted because it had been
    twice presented to the Tennessee courts was thus erroneous. Also
    unpersuasive is the State’s alternative argument that federal review
    is barred because the Brady claim was properly dismissed by the
    state postconviction courts as waived. Those courts held only that
    the claim had been previously determined, and this Court will not
    second-guess their judgment. Because the claim was properly pre
    served and exhausted in state court, it is not defaulted. Pp. 15–19.
       2. The lower federal courts failed to adequately consider whether
    the withheld documents were material to Cone’s sentence. Both the
    quantity and quality of the suppressed evidence lend support to
    Cone’s trial position that he habitually used excessive amounts of
    drugs, that his addiction affected his behavior during the murders,
    and that the State’s contrary arguments were false and misleading.
    Nevertheless, even when viewed in the light most favorable to Cone,
    the evidence does not sustain his insanity defense: His behavior be
    fore, during, and after the crimes was inconsistent with the conten
    tion that he lacked substantial capacity either to appreciate the
    wrongfulness of his conduct or to conform it to the requirements of
    law. Because the likelihood that the suppressed evidence would have
    affected the jury’s verdict on the insanity issue is remote, the Sixth
    Circuit did not err by denying habeas relief on the ground that such
    evidence was immaterial to the jury’s guilt finding. The same cannot
    be said of that court’s summary treatment of Cone’s claim that the
    suppressed evidence would have influenced the jury’s sentencing rec
    ommendation. Because the suppressed evidence might have been
    material to the jury’s assessment of the proper punishment, a full re
    view of that evidence and its effect on the sentencing verdict is war
    ranted. Pp. 20–26.
492 F. 3d 743, vacated and remanded.

  STEVENS, J., delivered the opinion of the Court, in which KENNEDY,
SOUTER, GINSBURG, and BREYER, JJ., joined. ROBERTS, C. J., filed an
opinion concurring in the judgment. ALITO, J., filed an opinion concur
ring in part and dissenting in part. THOMAS, J., filed a dissenting opin
ion, in which SCALIA, J., joined.
                        Cite as: 556 U. S. ____ (2009)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 07–1114
                                   _________________


   GARY BRADFORD CONE, PETITIONER v. RICKY 

               BELL, WARDEN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                                 [April 28, 2009] 


  JUSTICE STEVENS delivered the opinion of the Court.
  The right to a fair trial, guaranteed to state criminal
defendants by the Due Process Clause of the Fourteenth
Amendment, imposes on States certain duties consistent
with their sovereign obligation to ensure “that ‘justice
shall be done’ ” in all criminal prosecutions. United States
v. Agurs, 427 U. S. 97, 111 (1976) (quoting Berger v.
United States, 295 U. S. 78, 88 (1935)). In Brady v. Mary
land, 373 U. S. 83 (1963), we held that when a State sup
presses evidence favorable to an accused that is material
to guilt or to punishment, the State violates the defen
dant’s right to due process, “irrespective of the good faith
or bad faith of the prosecution.” Id., at 87.
  In this case, Gary Cone, a Vietnam veteran sentenced to
death, contends that the State of Tennessee violated his
right to due process by suppressing witness statements
and police reports that would have corroborated his trial
defense and bolstered his case in mitigation of the death
penalty. At his trial in 1982, Cone asserted an insanity
defense, contending that he had killed two people while
suffering from acute amphetamine psychosis, a disorder
2                      CONE v. BELL

                     Opinion of the Court

caused by drug addiction. The State of Tennessee discred
ited that defense, alleging that Cone’s drug addiction was
“baloney.” Ten years later, Cone learned that the State
had suppressed evidence supporting his claim of drug
addiction.
   Cone presented his new evidence to the state courts in a
petition for postconviction relief, but the Tennessee courts
denied him a hearing on the ground that his Brady claim
had been “previously determined,” either on direct appeal
from his conviction or in earlier collateral proceedings. On
application for a writ of habeas corpus pursuant to 28
U. S. C. §2254, the Federal District Court concluded that
the state courts’ disposition rested on an adequate and
independent state ground that barred further review in
federal court, and the Court of Appeals for the Sixth Cir
cuit agreed. Doubt concerning the correctness of that
holding, coupled with conflicting decisions from other
Courts of Appeals, prompted our grant of certiorari.
   After a complete review of the trial and postconviction
proceedings, we conclude that the Tennessee courts’ rejec
tion of petitioner’s Brady claim does not rest on a ground
that bars federal review. Furthermore, although the
District Court and the Court of Appeals passed briefly on
the merits of Cone’s claim, neither court distinguished the
materiality of the suppressed evidence with respect to
Cone’s guilt from the materiality of the evidence with
respect to his punishment. While we agree that the with
held documents were not material to the question whether
Cone committed murder with the requisite mental state,
the lower courts failed to adequately consider whether
that same evidence was material to Cone’s sentence.
Therefore, we vacate the decision of the Court of Appeals
and remand the case to the District Court to determine in
the first instance whether there is a reasonable probability
that the withheld evidence would have altered at least one
juror’s assessment of the appropriate penalty for Cone’s
                    Cite as: 556 U. S. ____ (2009)                   3

                         Opinion of the Court

crimes.
                             I
  On the afternoon of Saturday, August 10, 1980, Cone
robbed a jewelry store in downtown Memphis, Tennessee.
Fleeing the scene by car, he led police on a high-speed
chase into a residential neighborhood. Once there, he
abandoned his vehicle and shot a police officer.1 When a
bystander tried to impede his escape, Cone shot him, too,
before escaping on foot.
  A short time later, Cone tried to hijack a nearby car.
When that attempt failed (because the driver refused to
surrender his keys), Cone tried to shoot the driver and a
hovering police helicopter before realizing he had run out
of ammunition. He then fled the scene. Although police
conducted a thorough search, Cone was nowhere to be
found.
  Early the next morning, Cone reappeared in the same
neighborhood at the door of an elderly woman. He asked
to use her telephone, and when she refused, he drew a
gun. Before he was able to gain entry, the woman
slammed the door and called the police. By the time offi
cers arrived, however, Cone had once again disappeared.
  That afternoon, Cone gained entry to the home of 93
year-old Shipley Todd and his wife, 79-year-old Cleopatra
Todd. Cone beat the couple to death with a blunt instru
ment and ransacked the first floor of their home. Later,
he shaved his beard and escaped to the airport without
being caught. Cone then traveled to Florida, where he
was arrested several days later after robbing a drugstore
in Pompano Beach.
  A Tennessee grand jury charged Cone with two counts
——————
  1 From  the abandoned vehicle, police recovered stolen jewelry, large
quantities of illegal and prescription drugs, and approximately $2,400
in cash. Much of the cash was later connected to a grocery store rob
bery that had occurred on the previous day.
4                      CONE v. BELL

                     Opinion of the Court

of first-degree murder, two counts of murder in the perpe
tration of a burglary, three counts of assault with intent to
murder, and one count of robbery by use of deadly force.
At his jury trial in 1982, Cone did not challenge the over
whelming physical and testimonial evidence supporting
the charges against him. His sole defense was that he was
not guilty by reason of insanity.
  Cone’s counsel portrayed his client as suffering from
severe drug addiction attributable to trauma Cone had
experienced in Vietnam. Counsel argued that Cone had
committed his crimes while suffering from chronic am
phetamine psychosis, a disorder brought about by his drug
abuse. That defense was supported by the testimony of
three witnesses. First was Cone’s mother, who described
her son as an honorably discharged Vietnam veteran who
had changed following his return from service. She re
called Cone describing “how terrible” it had been to handle
the bodies of dead soldiers, and she explained that Cone
slept restlessly and sometimes “holler[ed]” in his sleep.
Tr. 1643–1645 (Apr. 20, 1982). She also described one
occasion, following Cone’s return from service, when a
package was shipped to him that contained marijuana.
Before the war, she asserted, Cone had not used drugs of
any kind.
  Two expert witnesses testified on Cone’s behalf. Mat
thew Jaremko, a clinical psychologist, testified that Cone
suffered from substance abuse and posttraumatic stress
disorders related to his military service in Vietnam. Ja
remko testified that Cone had expressed remorse for the
murders, and he opined that Cone’s mental disorder ren
dered him substantially incapable of conforming his con
duct to the law. Jonathan Lipman, a neuropharmacolo
gist, recounted at length Cone’s history of illicit drug use,
which began after Cone joined the Army and escalated to
the point where Cone was consuming “rather horrific”
quantities of drugs daily. App. 100. According to Lipman,
                    Cite as: 556 U. S. ____ (2009)                  5

                        Opinion of the Court

Cone’s drug abuse had led to chronic amphetamine psy
chosis, a disorder manifested through hallucinations and
ongoing paranoia that prevented Cone from obeying the
law and appreciating the wrongfulness of his actions.
   In rebutting Cone’s insanity defense the State’s strategy
throughout trial was to present Cone as a calculating,
intelligent criminal who was fully in control of his deci
sions and actions at the time of the crimes. A key compo
nent of that strategy involved discrediting Cone’s claims of
drug use.2 Through cross-examination, the State estab
lished that both defense experts’ opinions were based
solely on Cone’s representations to them about his drug
use rather than on any independently corroborated
sources, such as medical records or interviews with family
or friends. The prosecution also adduced expert and lay
testimony to establish that Cone was not addicted to drugs
and had acted rationally and intentionally before, during,
and after the Todd murders.
   Particularly damaging to Cone’s defense was the testi
mony of rebuttal witness Ilene Blankman, who had spent
time with Cone several months before the murders and at
whose home Cone had stayed in the days leading up to his
arrest in Florida. Blankman admitted to being a former
heroin addict but testified that she no longer used drugs
and tried to stay away from people who did. She testified
that she had never seen Cone use drugs, had never ob
served track marks on his body, and had never seen him
exhibit signs of paranoia.
   Emphasizing the State’s position with respect to Cone’s
——————
  2 The State also cast doubt on Cone’s defense by eliciting testimony

that Cone had enrolled in college following his return from Vietnam
and had graduated with high honors. Later, after serving time in
prison for an armed robbery, Cone gained admission to the University
of Arkansas Law School. The State suggested that Cone’s academic
success provided further proof that he was not impaired following his
return from war.
6                           CONE v. BELL

                         Opinion of the Court

alleged addiction, the prosecutor told the jury during
closing argument, “[Y]ou’re not dealing with a crazy per
son, an insane man. A man . . . out of his mind. You’re
dealing, I submit to you, with a premeditated, cool, delib
erate—and even cowardly, really—murderer.” Tr. 2084
(Apr. 22, 1982). Pointing to the quantity of drugs found in
Cone’s car, the prosecutor suggested that far from being a
drug addict, Cone was actually a drug dealer. The prose
cutor argued, “I’m not trying to be absurd, but he says he’s
a drug addict. I say baloney. He’s a drug seller. Doesn’t
the proof show that?” Id., at 107.3
   The jury rejected Cone’s insanity defense and found him
guilty on all counts. At the penalty hearing, the prosecu
tion asked the jury to find that Cone’s crime met the crite
ria for four different statutory aggravating factors, any
one of which would render him eligible for a capital sen
tence.4 Cone’s counsel called no witnesses but instead
rested on the evidence adduced during the guilt phase
proceedings. Acknowledging that the prosecution’s ex
perts had disputed the existence of Cone’s alleged mental
disorder, counsel nevertheless urged the jury to consider
Cone’s drug addiction when weighing the aggravating and
——————
  3 In his closing rebuttal argument, the prosecutor continued to press

the point, asserting: “There aren’t any charges for drug sales, but that
doesn’t mean that you can’t look and question in deciding whether or
not this man was, in fact, a drug user, or why he had those drugs. Did
he just have those drugs, or did he have those drugs and thousands of
dollars in that car? Among those drugs are there only the drugs he
used? How do we know if he used drugs? The only thing that we ever
had that he used drugs, period, is the fact that those drugs were in the
car and what he told people. What he told people. But according to
even what he told people, there are drugs in there he didn’t even use.”
Tr. 2068 (Apr. 22, 1982).
  4 The jury could impose a capital sentence only if it unanimously

determined that one or more statutory aggravating circumstances had
been proved by the State beyond a reasonable doubt, and that the
mitigating circumstances of the case did not outweigh any statutory
aggravating factors. Tenn. Code Ann. §39–2–203(g) (1982).
                     Cite as: 556 U. S. ____ (2009)                    7

                          Opinion of the Court

mitigating factors in the case.5 The jury found all four
aggravating factors and unanimously returned a sentence
of death.6
                            II
  On direct appeal Cone raised numerous challenges to
his conviction and sentence. Among those was a claim
that the prosecution violated state law by failing to dis
close a tape-recorded statement and police reports relating
to several trial witnesses. See App. 114–117. The Ten
nessee Supreme Court rejected each of Cone’s claims, and
affirmed his conviction and sentence. State v. Cone, 665
S. W. 2d 87 (1984).7 Cone then filed a petition for postcon
——————
   5 As defense counsel emphasized to the jury, one of the statutory miti

gating factors it was required to consider was whether “[t]he capacity of
the defendant to appreciate the wrongfulness of his conduct or to
conform his conduct to the requirements of the law was substantially
impaired as a result of mental disease or defect or intoxication which
was insufficient to establish a defense to the crime but which substan
tially affected his judgment.” §39–2404(j)(8).
   6 Specifically, the jury found Cone had committed one or more prior

felonies involving the use or threat of violence, see §39–2404(i)(2); the
murders had been committed for the purpose of avoiding, interfering
with, or preventing Cone’s lawful arrest or prosecution, see §39–
2404(i)(6); the murders were especially heinous, atrocious, or cruel in
that they involved torture and depravity of mind, see §39–2404(i)(5);
and Cone had knowingly created a risk of death to two or more persons,
other than the victim murdered, during his act of murder, see §39–
2404(i)(3). The Tennessee Supreme Court later observed that by
finding Cone guilty of murder in the first degree during the perpetra
tion of a burglary, the jury implicitly found the existence of an addi
tional statutory aggravating factor: that the murders occurred while
Cone was committing a burglary, §39–2404(i)(7). State v. Cone, 665
S. W. 2d 87, 94 (1984).
   7 In summarizing the trial proceedings the Tennessee Supreme Court

observed: “The only defense interposed on [Cone’s] behalf was that of
insanity, or lack of mental capacity, due to drug abuse and to stress
arising out of his previous service in the Vietnamese war, some eleven
years prior to the events involved in this case. This proved to be a
tenuous defense, at best, since neither of the expert witnesses who
8                            CONE v. BELL

                          Opinion of the Court

viction relief, primarily raising claims that his trial coun
sel had been ineffective; the Tennessee Court of Criminal
Appeals affirmed the denial of that petition in 1987. Cone
v. State, 747 S. W. 2d 353.
   In 1989, Cone, acting pro se, filed a second petition for
postconviction relief, raising myriad claims of error.
Among these was a claim that the State had failed to
disclose evidence in violation of his rights under the
United States Constitution. At the State’s behest, the
postconviction court summarily denied the petition, con
cluding that all the claims raised in it had either been
“previously determined” or “waived.” Order Dismissing
Petition for Post-Conviction Relief in Cone v. State, No. P–
06874 (Crim. Ct. Shelby Cty., Tenn., Jan. 2, 1990).8 At
that time, the court did not specify which claims fell into
which category.
   Cone appealed the denial of his petition to the Tennes
see Court of Criminal Appeals, asserting that the postcon
viction court had erred by dismissing 13 claims—his
——————
testified on his behalf had ever seen or heard of him until a few weeks
prior to the trial. Neither was a medical doctor or psychiatrist, and
neither had purported to treat him as a patient. Their testimony that
he lacked mental capacity was based purely upon his personal recita
tion to them of his history of military service and drug abuse.” Id., at
90.
   8 Under Tennessee law in effect at the time a criminal defendant was

entitled to collateral relief if his conviction or sentence violated “any
right guaranteed by the constitution of [Tennessee] or the Constitution
of the United States.” Tenn. Code Ann. §40–30–105 (1982); see also
§40–30–102. Any hearing on a petition for postconviction relief was
limited, however, to claims that had not been “waived or previously
determined.” See §40–30–111. A ground for relief was “previously
determined” if “a court of competent jurisdiction ha[d] ruled on the
merits [of the claim] after a full and fair hearing.” §40–30–112(a). The
claim was waived “if the petitioner knowingly and understandingly
failed to present it for determination in any proceeding before a court of
competent jurisdiction in which the ground could have been presented.”
§40–30–112(b)(1).
                    Cite as: 556 U. S. ____ (2009)                   9

                         Opinion of the Court

Brady claim among them—as previously determined
when, in fact, they had not been “previously addressed or
determined by any court.” Brief for Petitioner-Appellant
Gary Bradford Cone in No. P–06874, pp. 23–24, and n. 11.
In addition Cone urged the court to remand the case to
allow him, with the assistance of counsel, to rebut the
presumption that he had waived any of his claims by not
raising them at an earlier stage in the litigation. Id., at
24.9 The court agreed and remanded the case for further
proceedings.
  On remand counsel was appointed and an amended
petition was filed. The State once again urged the post
conviction court to dismiss Cone’s petition. Apparently
conflating the state-law disclosure claim Cone had raised
on direct appeal with his newly filed Brady claim, the
State represented that the Tennessee Supreme Court had
already decided the Brady issue and that Cone was there
fore barred from relitigating it. See App. 15–16.
  While that petition remained pending before the post
conviction court, the Tennessee Court of Appeals held for
the first time that the State’s Public Records Act allowed a
criminal defendant to review the prosecutor’s file in his
case. See Capital Case Resource Center of Tenn., Inc. v.
Woodall, No. 01–A–01–9104–CH–00150, 1992 WL 12217
(Jan. 29, 1992). Based on that holding, Cone obtained
access to the prosecutor’s files, in which he found proof
that evidence had indeed been withheld from him at trial.
Among the undisclosed documents Cone discovered were
statements from witnesses who had seen him several days
before and several days after the murders. The witnesses
described Cone’s appearance as “wild eyed,” App. 50, and
——————
  9 See Swanson v. State, 749 S. W. 2d 731, 734 (Tenn. 1988) (courts

should not dismiss postconviction petitions on technical grounds unless
the petitioner has first had “reasonable opportunity, with aid of coun
sel, to file amendments” and rebut presumption of waiver (internal
quotation marks omitted)).
10                          CONE v. BELL

                          Opinion of the Court

his behavior as “real weird,” id., at 49. One witness af
firmed that Cone had appeared “to be drunk or high.”
Ibid. The file also contained a police report describing
Cone’s arrest in Florida following the murders. In that
report, a police officer described Cone looking around “in a
frenzied manner,” and “walking in [an] agitated manner”
prior to his apprehension. Id., at 53. Multiple police
bulletins describing Cone as a “drug user” and a “heavy
drug user” were also among the undisclosed evidence. See
id., at 55–59.
   With the newly discovered evidence in hand, Cone
amended his postconviction petition once again in October
1993, expanding his Brady claim to allege more specifi
cally that the State had withheld exculpatory evidence
demonstrating that he “did in fact suffer drug problems
and/or drug withdrawal or psychosis both at the time of
the offense and in the past.” App. at 20. Cone pointed to
specific examples of evidence that had been withheld,
alleging the evidence was “exculpatory to both the jury’s
determination of petitioner’s guilt and its consideration of
the proper sentence,” and that there was “a reasonable
probability that, had the evidence not been withheld, the
jurors would not have convicted [him] and would not have
sentenced him to death.” Id., at 20–21.10 In a lengthy
affidavit submitted with his amended petition, Cone ex
plained that he had not raised his Brady claim in earlier
proceedings because the facts underlying it “ha[d] been
revealed through disclosure of the State’s files, which
occurred after the first post-conviction proceeding.” App.
18.
   After denying Cone’s request for an evidentiary hearing,
——————
  10 As examples of evidence that had been withheld, Cone pointed to

“statements of Charles and Debbie Slaughter, statements of Sue Cone,
statements of Lucille Tuech, statements of Herschel Dalton, and
patrolman Collins” and “statements contained in official police reports.”
App. 20.
                  Cite as: 556 U. S. ____ (2009)            11

                      Opinion of the Court

the postconviction court denied relief on each claim pre
sented in the amended petition. Many of the claims were
dismissed on the ground that they had been waived by
Cone’s failure to raise them in earlier proceedings; how
ever, consistent with the position urged by the State, the
court dismissed many others, including the Brady claim,
as mere “re-statements of previous grounds heretofore
determined and denied by the Tennessee Supreme Court
upon Direct Appeal or the Court of Criminal Appeals upon
the First Petition.” App. 22.
  Noting that “the findings of the trial court in post
conviction hearings are conclusive on appeal unless the
evidence preponderates against the judgment,” the Ten
nessee Court of Criminal Appeals affirmed. Cone v. State,
927 S. W. 2d 579, 581–582 (1995). The court concluded
that Cone had “failed to rebut the presumption of waiver
as to all claims raised in his second petition for post
conviction relief which had not been previously deter
mined.” Id., at 582 (emphasis added). Cone unsuccess
fully petitioned for review in the Tennessee Supreme
Court, and we denied certiorari. Cone v. Tennessee, 519
U. S. 934 (1996).
                               III
    In 1997, Cone filed a petition for a federal writ of habeas
corpus. Without disclosing to the District Court the con
trary position it had taken in the state-court proceedings,
the State acknowledged that Cone’s Brady claim had not
been raised prior to the filing of his second postconviction
petition. However, wrenching out of context the state
appellate court’s holding that Cone had “waived ‘all claims
. . . which had not been previously determined,’ ” the State
now asserted the Brady claim had been waived. App. 39
(quoting Cone, 927 S. W. 2d, at 581–582).
    In May 1998, the District Court denied Cone’s request
for an evidentiary hearing on his Brady claim. Lamenting
12                      CONE v. BELL

                      Opinion of the Court

that its consideration of Cone’s claims had been “made
more difficult” by the parties’ failure to articulate the state
procedural rules under which each of Cone’s claims had
allegedly been defaulted, App. to Pet. for Cert. 98a, the
District Court nevertheless held that the Brady claim was
procedurally barred. After parsing the claim into 11
separate subclaims based on 11 pieces of withheld evi
dence identified in the habeas petition, the District Court
concluded that Cone had waived each subclaim by failing
to present or adequately develop it in state court. App. to
Pet. for Cert. 112a–113a. Moreover, the court concluded
that even if Cone had not defaulted his Brady claim, it
would fail on its merits because none of the withheld
evidence would have cast doubt on Cone’s guilt. App. to
Pet. for Cert. 116a–119a. Throughout its opinion the
District Court repeatedly referenced factual allegations
contained in early versions of Cone’s second petition for
postconviction relief rather than the amended version of
the petition upon which the state court’s decision had
rested. See, e.g., id., at 112a.
   After the District Court dismissed the remainder of
Cone’s federal claims, the Court of Appeals for the Sixth
Circuit granted him permission to appeal several issues,
including the alleged suppression of Brady material.
Before the Court of Appeals, the State shifted its proce
dural default argument once more, this time contending
that Cone had “simply never raised” his Brady claim in
the state court because he failed to make adequate factual
allegations to support that claim in his second petition for
postconviction relief. App. 41. Repeating the District
Court’s error, the State directed the Court of Appeals’
attention to Cone’s pro se petition and to the petition
Cone’s counsel filed before he gained access to the prosecu
tion’s case file. Id., at 41–42, and n. 7. In other words,
instead of citing the October 1993 amended petition on
which the state court’s decision had been based and to
                 Cite as: 556 U. S. ____ (2009)          13

                     Opinion of the Court

which its order explicitly referred, the State pointed the
court to earlier, less developed versions of the same claim.
   The Court of Appeals concluded that Cone had proce
durally defaulted his Brady claim and had failed to show
cause and prejudice to overcome the default. Cone v. Bell,
243 F. 3d 961, 968 (2001). The court acknowledged that
Cone had raised his Brady claim. 243 F. 3d, at 969. Nev
ertheless, the court considered itself barred from reaching
the merits of the claim because the Tennessee courts had
concluded the claim was “previously determined or waived
under Tenn. Code Ann. §40–30–112.” Ibid.
   Briefly mentioning several isolated pieces of suppressed
evidence, the court summarily concluded that even if
Cone’s Brady claim had not been defaulted, the sup
pressed evidence would not undermine confidence in the
verdict (and hence was not Brady material) “because of
the overwhelming evidence of Cone’s guilt.” 243 F. 3d, at
968. The court did not discuss whether any of the undis
closed evidence was material with respect to Cone’s sen
tencing proceedings.
   Although the Court of Appeals rejected Cone’s Brady
claim, it held that he was entitled to have his death sen
tence vacated because of his counsel’s ineffective assis
tance at sentencing. See 243 F. 3d, at 975. In 2002, this
Court reversed that holding after concluding that the
Tennessee courts’ rejection of Cone’s ineffective
assistance-of-counsel claim was not “objectively unreason
able” within the meaning of the Antiterrorism and Effec
tive Death Penalty Act of 1996 (AEDPA). See Bell v. Cone,
535 U. S. 685, 699.
   In 2004, following our remand, the Court of Appeals
again entered judgment ordering a new sentencing hear
ing, this time based on the purported invalidity of an
aggravating circumstance found by the jury. Cone v. Bell,
359 F. 3d 785. Again we granted certiorari and reversed,
relying in part on the deferential standard that governs
14                          CONE v. BELL

                         Opinion of the Court

our review of state-court decisions under AEDPA. See
Bell v. Cone, 543 U. S. 447, 452–458 (2005) (per curiam).
  Following our second remand, the Court of Appeals
revisited Cone’s Brady claim. This time, the court divided
the claim into four separate subclaims: “(1) evidence re
garding [Cone’s] drug use; (2) evidence that might have
been useful to impeach the testimony and credibility of
prosecution witness Sergeant Ralph Roby; (3) FBI re
ports;[11] and (4) evidence showing that prosecution wit
ness Ilene Blankman was untruthful and biased.” 492 F.
3d 743, 753 (2007). Noting that it had previously found all
four subclaims to be procedurally defaulted, the court
declined to reconsider its earlier decision. See ibid. (citing
Cone, 243 F. 3d, at 968–970). At the same time, the court
reiterated that the withheld evidence “would not have
overcome the overwhelming evidence of Cone’s guilt in
committing a brutal double murder and the persuasive
testimony that Cone was not under the influence of
drugs.” 492 F. 3d, at 756. Summarily discounting Cone’s
contention that the withheld evidence was material with
respect to his sentence, the court concluded that the intro
duction of the suppressed evidence would not have altered
the jurors’ finding that Cone’s alleged drug use did not
“vitiate his specific intent to murder his victims and did
not mitigate his culpability sufficient to avoid the death
sentence.” Id., at 757.
  Judge Merritt dissented. He castigated the State not
only for withholding documents relevant to Cone’s sole
defense and plea for mitigation, but also for its “falsifica
——————
  11 In the course of federal habeas proceedings, Cone had obtained

access to files from the Federal Bureau of Investigation where he found
additional previously undisclosed evidence not contained in the state
prosecutor’s case file. The suppressed FBI documents make repeated
reference to Cone’s drug use and corroborate his expert’s representation
that he had used drugs during his prior incarceration for armed rob
bery. See id., at 26–28.
                 Cite as: 556 U. S. ____ (2009)           15

                     Opinion of the Court

tion of the procedural record . . . concerning the State’s
procedural default defense to the Brady claim.” Id., at
760. Over the dissent of seven judges, Cone’s petition for
rehearing en banc was denied. 505 F. 3d 610 (2007).
   We granted certiorari, 554 U. S. ___ (2008), to answer
the question whether a federal habeas claim is “proce
durally defaulted” when it is twice presented to the state
courts.
                              IV
   During the state and federal proceedings below, the
State of Tennessee offered two different justifications for
denying review of the merits of Cone’s Brady claim. First,
in connection with Cone’s amended petition for state
postconviction relief, the State argued that the Brady
claim was barred because it had been decided on direct
appeal. See App. 15–16. Then, in connection with Cone’s
federal habeas petition, the State argued that Cone’s claim
was waived because it had never been properly raised
before the state courts. See id., at 39. The District Court
and the Court of Appeals agreed that Cone’s claim was
procedurally barred, but for different reasons. The Dis
trict Court held that the claim had been waived, App. to
Pet. for Cert. 102a, while the Court of Appeals held that
the claim had been either waived or previously deter
mined, Cone, 243 F. 3d, at 969. We now conclude that
neither prior determination nor waiver provides an inde
pendent and adequate state ground for denying Cone
review of his federal claim.
   It is well established that federal courts will not review
questions of federal law presented in a habeas petition
when the state court’s decision rests upon a state-law
ground that “is independent of the federal question and
adequate to support the judgment.” Coleman v. Thomp
son, 501 U. S. 722, 729 (1991); Lee v. Kemna, 534 U. S.
362, 375 (2002). In the context of federal habeas proceed
16                      CONE v. BELL

                      Opinion of the Court

ings, the independent and adequate state ground doctrine
is designed to “ensur[e] that the States’ interest in correct
ing their own mistakes is respected in all federal habeas
cases.” Coleman, 501 U. S., at 732. When a petitioner
fails to properly raise his federal claims in state court, he
deprives the State of “an opportunity to address those
claims in the first instance” and frustrates the State’s
ability to honor his constitutional rights. Id., at 732, 748.
Therefore, consistent with the longstanding requirement
that habeas petitioners must exhaust available state
remedies before seeking relief in federal court, we have
held that when a petitioner fails to raise his federal claims
in compliance with relevant state procedural rules, the
state court’s refusal to adjudicate the claim ordinarily
qualifies as an independent and adequate state ground for
denying federal review. See id., at 731.
   That does not mean, however, that federal habeas re
view is barred every time a state court invokes a proce
dural rule to limit its review of a state prisoner’s claims.
We have recognized that “ ‘the adequacy of state proce
dural bars to the assertion of federal questions’ . . . is not
within the State’s prerogative finally to decide; rather,
adequacy ‘is itself a federal question.’ ” Lee, 534 U. S., at
375 (quoting Douglas v. Alabama, 380 U. S. 415, 422
(1965)); see also Coleman, 501 U. S., at 736 (“[F]ederal
habeas courts must ascertain for themselves if the peti
tioner is in custody pursuant to a state court judgment
that rests on independent and adequate state grounds”).
The question before us now is whether federal review of
Cone’s Brady claim is procedurally barred either because
the claim was twice presented to the state courts or be
cause it was waived, and thus not presented at all.
   First, we address the contention that the repeated pres
entation of a claim in state court bars later federal review.
The Tennessee postconviction court denied Cone’s Brady
claim after concluding it had been previously determined
                    Cite as: 556 U. S. ____ (2009)                 17

                        Opinion of the Court

following a full and fair hearing in state court. See Tenn.
Code Ann. §40–30–112(a) (1982). That conclusion rested
on a false premise: Contrary to the state courts’ finding,
Cone had not presented his Brady claim in earlier pro
ceedings and, consequently, the state courts had not
passed on it. The Sixth Circuit recognized that Cone’s
Brady claim had not been decided on direct appeal, see
Cone, 243 F. 3d, at 969, but felt constrained by the state
courts’ refusal to reach the merits of that claim on post
conviction review. The Court of Appeals concluded that
because the state postconviction courts had applied a state
procedural law to avoid reaching the merits of Cone’s
Brady claim, “an ‘independent and adequate’ state
ground” barred federal habeas review. 243 F. 3d, at 969.
In this Court the State does not defend that aspect of the
Court of Appeals’ holding, and rightly so.
   When a state court declines to review the merits of a
petitioner’s claim on the ground that it has done so al
ready, it creates no bar to federal habeas review. In Ylst
v. Nunnemaker, 501 U. S. 797, 804, n. 3 (1991), we ob
served in passing that when a state court declines to
revisit a claim it has already adjudicated, the effect of the
later decision upon the availability of federal habeas is
“nil” because “a later state decision based upon ineligibil
ity for further state review neither rests upon procedural
default nor lifts a pre-existing procedural default.”12
When a state court refuses to readjudicate a claim on the
ground that it has been previously determined, the court’s
——————
  12 With the exception of the Sixth Circuit, all Courts of Appeals to
have directly confronted the question both before and after Ylst, 501
U. S. 797, have agreed that a state court’s successive rejection of a
federal claim does not bar federal habeas review. See, e.g., Page v.
Frank, 343 F. 3d 901, 907 (CA7 2003); Brecheen v. Reynolds, 41 F. 3d
1343, 1358 (CA10 1994); Bennett v. Whitley, 41 F. 3d 1581, 1582 (CA5
1994); Silverstein v. Henderson, 706 F. 2d 361, 368 (CA2 1983). See
also Lambright v. Stewart, 241 F. 3d 1201, 1206 (CA9 2001).
18                          CONE v. BELL

                          Opinion of the Court

decision does not indicate that the claim has been proce
durally defaulted. To the contrary, it provides strong
evidence that the claim has already been given full consid
eration by the state courts and thus is ripe for federal
adjudication. See 28 U. S. C. §2254(b)(1)(A) (permitting
issuance of a writ of habeas corpus only after “the appli
cant has exhausted the remedies available in the courts of
the State”).
  A claim is procedurally barred when it has not been
fairly presented to the state courts for their initial consid
eration—not when the claim has been presented more
than once. Accordingly, insofar as the Court of Appeals
rejected Cone’s Brady claim as procedurally defaulted
because the claim had been twice presented to the Ten
nessee courts, its decision was erroneous.
  As an alternative (and contradictory) ground for barring
review of Cone’s Brady claim, the State has argued that
Cone’s claim was properly dismissed by the state postcon
viction court on the ground it had been waived. We are
not persuaded. The state appellate court affirmed the
denial of Cone’s Brady claim on the same mistaken ground
offered by the lower court—that the claim had been previ
ously determined.13 Contrary to the State’s assertion, the
——————
  13 As recounted earlier, Cone’s state postconviction petition contained
numerous claims of error. The state postconviction court dismissed
some of those claims as waived and others, including the Brady claim,
as having been previously determined. In affirming the denial of
Cone’s petition the Tennessee Court of Criminal Appeals summarily
stated that Cone had “failed to rebut the presumption of waiver as to
all claims raised in his second petition for post-conviction relief which
had not been previously determined.” Cone v. State, 927 S. W. 2d 579,
582 (1995). Pointing to that language, the State asserts that the
Tennessee Court of Criminal Appeals denied Cone’s Brady claim not
because it had been previously determined, but because it was waived
in the postconviction court proceedings. Not so. Without questioning
the trial court’s finding that Cone’s Brady claim had been previously
determined, the Court of Criminal Appeals affirmed the denial of
                     Cite as: 556 U. S. ____ (2009)                    19

                          Opinion of the Court

Tennessee appellate court did not hold that Cone’s Brady
claim was waived.
  When a state court declines to find that a claim has
been waived by a petitioner’s alleged failure to comply
with state procedural rules, our respect for the state-court
judgment counsels us to do the same. Although we have
an independent duty to scrutinize the application of state
rules that bar our review of federal claims, Lee, 534 U. S.,
at 375, we have no concomitant duty to apply state proce
dural bars where state courts have themselves declined to
do so. The Tennessee courts did not hold that Cone
waived his Brady claim, and we will not second-guess
their judgment.14
——————
Cone’s postconviction petition in its entirety. Nothing in that decision
suggests the appellate court believed the Brady claim had been waived
in the court below.
  Similarly, while JUSTICE ALITO’s parsing of the record persuades him
that Cone failed to adequately raise his Brady claim to the Tennessee
Court of Criminal Appeals, he does not argue that the court expressly
held that Cone waived the claim. A review of Cone’s opening brief
reveals that he made a broad challenge to the postconviction court’s
dismissal of his petition and plainly asserted that the court erred by
dismissing claims as previously determined on direct appeal or in his
initial postconviction petition. See Brief for Petitioner-Appellant in No.
02–C–01–9403–CR–00052 (Tenn. Crim. App.), pp. 7, 14. The state
appellate court did not state or suggest that Cone had waived his Brady
claim. Rather, after commending the postconviction court for its
“exemplary and meticulous treatment of the appellant’s petition,” Cone,
927 S. W. 2d, at 581, the appellate court simply adopted without
modification the lower court’s findings with respect to the application of
Tenn. Code Ann. §40–30–112 to the facts of this case. The best reading
of the Tennessee Court of Criminal Appeals’ decision is that it was
based on an approval of the postconviction court’s reasoning rather
than on an unmentioned failure by Cone to adequately challenge the
dismissal of his Brady claim on appeal.
  14 Setting aside the state courts’ mistaken belief that Cone’s Brady

claim had been previously determined, there are many reasons the
state courts might have rejected the State’s waiver argument. The
record establishes that the suppressed documents which form the basis
for Cone’s claim were not available to him until the Tennessee Court of
20                          CONE v. BELL

                          Opinion of the Court

  The State’s procedural objections to federal review of the
merits of Cone’s claim have resulted in a significant delay
in bringing this unusually protracted case to a conclusion.
Ultimately, however, they provide no obstacle to judicial
review. Cone properly preserved and exhausted his Brady
claim in the state court; therefore, it is not defaulted. We
turn now to the merits of that claim.
                             V
  Although the State is obliged to “prosecute with ear
nestness and vigor,” it “is as much [its] duty to refrain
from improper methods calculated to produce a wrongful
conviction as it is to use every legitimate means to bring
about a just one.” Berger, 295 U. S., at 88. Accordingly,
we have held that when the State withholds from a crimi
nal defendant evidence that is material to his guilt or
punishment, it violates his right to due process of law in
violation of the Fourteenth Amendment. See Brady, 373
U. S., at 87. In United States v. Bagley, 473 U. S. 667, 682
(1985) (opinion of Blackmun, J.), we explained that evi
dence is “material” within the meaning of Brady when
there is a reasonable probability that, had the evidence
been disclosed, the result of the proceeding would have
been different. In other words, favorable evidence is sub
ject to constitutionally mandated disclosure when it “could
reasonably be taken to put the whole case in such a differ
——————
Appeals’ 1992 decision interpreting the State’s Public Records Act as
authorizing the disclosure of prosecutorial records. Soon after obtain
ing access to the prosecutor’s file and discovering within it documents
that had not been disclosed prior to trial, Cone amended his petition for
postconviction relief, adding detailed allegations regarding the sup
pressed evidence recovered from the file, along with an affidavit ex
plaining the reason why his claim had not been filed sooner. See App.
13, 18. The State did not oppose the amendment of Cone’s petition on
the ground that it was untimely, and it appears undisputed that there
would have been no basis under state law for doing so. See Brief for
Petitioner 7, n. 1.
                     Cite as: 556 U. S. ____ (2009)                   21

                          Opinion of the Court

ent light as to undermine confidence in the verdict.” Kyles
v. Whitley, 514 U. S. 419, 435 (1995); accord, Banks v.
Dretke, 540 U. S. 668, 698–699 (2004); Strickler v. Greene,
527 U. S. 263, 290 (1999).15
  The documents suppressed by the State vary in kind,
but they share a common feature: Each strengthens the
inference that Cone was impaired by his use of drugs
around the time his crimes were committed. The sup
pressed evidence includes statements by witnesses ac
knowledging that Cone appeared to be “drunk or high,”
App. 49, “acted real weird,” ibid., and “looked wild eyed,”
id., at 50, in the two days preceding the murders.16 It also
includes documents that could have been used to impeach
——————
  15 Although the Due Process Clause of the Fourteenth Amendment, as

interpreted by Brady, only mandates the disclosure of material evi
dence, the obligation to disclose evidence favorable to the defense may
arise more broadly under a prosecutor’s ethical or statutory obligations.
See Kyles, 514 U. S., at 437 (“[T]he rule in Bagley (and, hence, in
Brady) requires less of the prosecution than the ABA Standards for
Criminal Justice Prosecution Function and Defense Function 3–3.11(a)
(3d ed. 1993)”). See also ABA Model Rule of Professional Conduct
3.8(d) (2008) (“The prosecutor in a criminal case shall” “make timely
disclosure to the defense of all evidence or information known to the
prosecutor that tends to negate the guilt of the accused or mitigates the
offense, and, in connection with sentencing, disclose to the defense and
to the tribunal all unprivileged mitigating information known to the
prosecutor, except when the prosecutor is relieved of this responsibility
by a protective order of the tribunal”). As we have often observed, the
prudent prosecutor will err on the side of transparency, resolving
doubtful questions in favor of disclosure. See Kyles, 514 U. S., at 439;
United States v. Bagley, 473 U. S. 667, 711, n. 4 (1985) (STEVENS, J.,
dissenting); United States v. Agurs, 427 U. S. 97, 108 (1976).
  16 The State contends that the statements were made by witnesses

who observed Cone during and immediately after he committed robber
ies; therefore, it is not surprising that Cone appeared less than “se
rene.” See Brief for Respondent 46. Although a jury would have been
free to infer that Cone’s behavior was attributable to his criminal
activity, the evidence is also consistent with Cone’s assertion that he
was suffering from chronic amphetamine psychosis at the time of the
crimes.
22                          CONE v. BELL

                         Opinion of the Court

witnesses whose trial testimony cast doubt on Cone’s drug
addiction. For example, Memphis police officer Ralph
Roby testified at trial that Cone had no needle marks on
his body when he was arrested—an observation that
bolstered the State’s argument that Cone was not a drug
user. The suppressed evidence reveals, however, that
Roby authorized multiple teletypes to law enforcement
agencies in the days following the murders in which he
described Cone as a “drug user” and a “heavy drug user.”
See id., at 55–58.17 A suppressed statement made by the
chief of police of Cone’s hometown also describes Cone as a
serious drug user. See Cone, 243 F. 3d, at 968. And un
disclosed notes of a police interview with Ilene Blankman
conducted several days after the murders reveal discrep
ancies between her initial statement and her trial testi
mony relevant to Cone’s alleged drug use. App. 72–73. In
sum, both the quantity and the quality of the suppressed
evidence lends support to Cone’s position at trial that he
habitually used excessive amounts of drugs, that his ad
diction affected his behavior during his crime spree, and
that the State’s arguments to the contrary were false and
misleading.
  Thus, the federal question that must be decided is
whether the suppression of that probative evidence de
prived Cone of his right to a fair trial. See Agurs, 427
——————
   17 As the dissent points out, Roby did not testify directly that Cone

was not a drug user and FBI Agent Eugene Flynn testified that, at the
time of Cone’s arrest in Pompano Beach, Cone reported that he had
used cocaine, Dilaudid, and Demerol and was suffering from “slight
withdrawal symptoms.” See post, at 7, 11. See also Tr. 1916, 1920
(Apr. 22, 1982). It is important to note, however, that neither Flynn
nor Roby corroborated Cone’s account of alleged drug use. Taken in
context, Roby’s statement that he had not observed any needle marks
on Cone’s body invited the jury to infer that Cone’s self-reported drug
use was either minimal or contrived. See id., at 1939. Therefore,
although the suppressed evidence does not directly contradict Roby’s
trial testimony, it does place it in a different light.
                    Cite as: 556 U. S. ____ (2009)                  23

                         Opinion of the Court

U. S., at 108. Because the Tennessee courts did not reach
the merits of Cone’s Brady claim, federal habeas review is
not subject to the deferential standard that applies under
AEDPA to “any claim that was adjudicated on the merits
in State court proceedings.” 28 U. S. C. §2254(d). Instead,
the claim is reviewed de novo. See, e.g., Rompilla v.
Beard, 545 U. S. 374, 390 (2005) (de novo review where
state courts did not reach prejudice prong under Strick
land v. Washington, 466 U. S. 668 (1984)); Wiggins v.
Smith, 539 U. S. 510, 534 (2003) (same).
   Contending that the Federal District Court and Court of
Appeals adequately and correctly resolved the merits of
that claim, the State urges us to affirm the Sixth Circuit’s
denial of habeas relief. In assessing the materiality of the
evidence suppressed by the State, the Court of Appeals
suggested that two facts outweighed the potential force of
the suppressed evidence. First, the evidence of Cone’s
guilt was overwhelming. Second, the evidence of Cone’s
drug use was cumulative because the jury had heard
evidence of Cone’s alleged addiction from witnesses and
from officers who interviewed Cone and recovered drugs
from his vehicle.18 The Court of Appeals did not thor
oughly review the suppressed evidence or consider what
its cumulative effect on the jury would have been. More
over, in concluding that the suppressed evidence was not
material within the meaning of Brady, the court did not
distinguish between the materiality of the evidence with
respect to guilt and the materiality of the evidence with
respect to punishment—an omission we find significant.
   Evidence that is material to guilt will often be material
——————
  18 In pointing to the trial evidence of Cone’s drug use, the Court of

Appeals made no mention of the fact that the State had discredited the
testimony of Cone’s experts on the ground that no independent evi
dence corroborated Cone’s alleged addiction and that the State had
argued that the drugs in Cone’s car were intended for resale, rather
than personal use.
24                     CONE v. BELL

                     Opinion of the Court

for sentencing purposes as well; the converse is not always
true, however, as Brady itself demonstrates. In our semi
nal case on the disclosure of prosecutorial evidence, defen
dant John Brady was indicted for robbery and capital
murder. At trial, Brady took the stand and confessed to
robbing the victim and being present at the murder but
testified that his accomplice had actually strangled the
victim. Brady v. State, 226 Md. 422, 425, 174 A. 2d 167,
168 (1961). After Brady was convicted and sentenced to
death he discovered that the State had suppressed the
confession of his accomplice, which included incriminating
statements consistent with Brady’s version of events. Id.,
at 426, 174 A. 2d, at 169. The Maryland Court of Appeals
concluded that Brady’s due process rights were violated by
the suppression of the accomplice’s confession but declined
to order a new trial on guilt. Observing that nothing in
the accomplice’s confession “could have reduced . . .
Brady’s offense below murder in the first degree,” the
state court ordered a new trial on the question of punish
ment only. Id., at 430, 174 A. 2d, at 171. We granted
certiorari and affirmed, rejecting Brady’s contention that
the state court’s limited remand violated his constitutional
rights. 373 U. S., at 88.
   As in Brady, the distinction between the materiality of
the suppressed evidence with respect to guilt and punish
ment is significant in this case. During the guilt phase of
Cone’s trial, the only dispute was whether Cone was “sane
under the law,” Tr. 2040 (Apr. 22, 1982), as his counsel
described the issue, or “criminally responsible” for his
conduct, App. 110, as the prosecutor argued. Under Ten
nessee law, Cone could not be held criminally responsible
for the murders if, “at the time of [his] conduct as a result
of mental disease or defect he lack[ed] substantial capacity
either to appreciate the wrongfulness of his conduct or to
conform his conduct to the requirements of law.” Graham
v. State, 547 S. W. 2d 531, 543 (Tenn. 1977). Although we
                 Cite as: 556 U. S. ____ (2009)          25

                     Opinion of the Court

take exception to the Court of Appeals’ failure to assess
the effect of the suppressed evidence “collectively” rather
than “item by item,” see Kyles, 514 U. S., at 436, we never
theless agree that even when viewed in the light most
favorable to Cone, the evidence falls short of being suffi
cient to sustain his insanity defense.
   Cone’s experts testified that his drug addiction and
posttraumatic stress disorder originated during his service
in Vietnam, more than 13 years before the Todds were
murdered. During those years, despite Cone’s drug use
and mental disorder, he managed to successfully complete
his education, travel, and (when not incarcerated) function
in civil society. The suppressed evidence may have
strengthened the inference that Cone was on drugs or
suffering from withdrawal at the time of the murders, but
his behavior before, during, and after the crimes was
inconsistent with the contention that he lacked substan
tial capacity either to appreciate the wrongfulness of his
conduct or to conform his conduct to the requirements of
law. See Graham, 547 S. W. 2d, at 543. The likelihood
that the suppressed evidence would have affected the
jury’s verdict on the issue of insanity is therefore remote.
Accordingly, we conclude that the Sixth Circuit did not err
by denying habeas relief on the ground that the sup
pressed evidence was immaterial to the jury’s finding of
guilt.
   The same cannot be said of the Court of Appeals’ sum
mary treatment of Cone’s claim that the suppressed evi
dence influenced the jury’s sentencing recommendation.
There is a critical difference between the high standard
Cone was required to satisfy to establish insanity as a
matter of Tennessee law and the far lesser standard that a
defendant must satisfy to qualify evidence as mitigating in
a penalty hearing in a capital case. See Bell, 535 U. S., at
712 (STEVENS, J., dissenting) (“[T]here is a vast difference
between insanity—which the defense utterly failed to
26                         CONE v. BELL

                         Opinion of the Court

prove—and the possible mitigating effect of drug addiction
incurred as a result of honorable service in the military”).
As defense counsel emphasized in his brief opening state
ment during penalty phase proceedings, the jury was
statutorily required to consider whether Cone’s “capacity
. . . to appreciate the wrongfulness of his conduct or to
conform his conduct to the requirements of the law was
substantially impaired as a result of mental disease or
defect or intoxication which was insufficient to establish a
defense to the crime but which substantially affected his
judgment.” Tenn. Code Ann. §39–2–203(j)(8) (1982). It is
possible that the suppressed evidence, viewed cumula
tively, may have persuaded the jury that Cone had a far
more serious drug problem than the prosecution was
prepared to acknowledge, and that Cone’s drug use played
a mitigating, though not exculpating, role in the crimes he
committed.19 The evidence might also have rebutted the
State’s suggestion that Cone had manipulated his expert
witnesses into falsely believing he was a drug addict when
in fact he did not struggle with substance abuse.
    Neither the Court of Appeals nor the District Court fully
considered whether the suppressed evidence might have
persuaded one or more jurors that Cone’s drug addiction—
especially if attributable to honorable service of his coun
try in Vietnam—was sufficiently serious to justify a deci
sion to imprison him for life rather than sentence him to
death. Because the evidence suppressed at Cone’s trial

——————
  19 We agree with the dissent that the standard to be applied by the

District Court in evaluating the merits of Cone’s Brady claim on re
mand is whether there is a reasonable probability that, had the sup
pressed evidence been disclosed, the result of the proceeding would
have been different. See post, at 5. Because neither the District Court
nor the Court of Appeals considered the merits of Cone’s claim with
respect to the effect of the withheld evidence on his sentence, it is
appropriate for the District Court, rather than this Court, to do so in
the first instance.
                 Cite as: 556 U. S. ____ (2009)           27

                     Opinion of the Court

may well have been material to the jury’s assessment of
the proper punishment in this case, we conclude that a
full review of the suppressed evidence and its effect is
warranted.
                             VI
  In the 27 years since Gary Cone was convicted of mur
der and sentenced to death, no Tennessee court has
reached the merits of his claim that state prosecutors
withheld evidence that would have bolstered his defense
and rebutted the State’s attempts to cast doubt on his
alleged drug addiction. Today we hold that the Tennessee
courts’ procedural rejection of Cone’s Brady claim does not
bar federal habeas review of the merits of that claim.
Although we conclude that the suppressed evidence was
not material to Cone’s conviction for first-degree murder,
the lower courts erred in failing to assess the cumulative
effect of the suppressed evidence with respect to Cone’s
capital sentence. Accordingly, the judgment of the Court
of Appeals is vacated, and the case is remanded to the
District Court with instructions to give full consideration
to the merits of Cone’s Brady claim.
                                            It is so ordered.
                  Cite as: 556 U. S. ____ (2009)            1

              ROBERTS, C. J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
                           _________________

                          No. 07–1114
                           _________________


   GARY BRADFORD CONE, PETITIONER v. RICKY 

               BELL, WARDEN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                         [April 28, 2009] 


  CHIEF JUSTICE ROBERTS, concurring in the judgment.
  The Court’s decision is grounded in unusual facts that
necessarily limit its reach. When issues under Brady v.
Maryland, 373 U. S. 83 (1963), are presented on federal
habeas, they usually have been previously addressed in
state proceedings. Federal review is accordingly sharply
limited by established principles of deference: If the claim
has been waived under state rules, that waiver typically
precludes federal review. If the claim has been decided in
the state system, federal review is restricted in light of the
state court’s legal and factual conclusions. The unique
procedural posture of this case presents a Brady claim
neither barred under state rules for failure to raise it nor
decided in the state system.
  When it comes to that claim, the Court specifies that the
appropriate legal standard is the one we set forth in Kyles
v. Whitley, 514 U. S. 419, 435 (1995) (whether “the favor
able evidence could reasonably be taken to put the whole
case in such a different light as to undermine confidence
in the verdict”). See ante, at 20–21, 26, n. 19. I do not
understand the majority to depart from that standard, and
the majority certainly does not purport to do so.
  That leaves only application of the accepted legal stan
dard to the particular facts. It is highly unusual for this
Court to engage in such an enterprise, see Kyles, supra, at
2                        CONE v. BELL

              ROBERTS, C. J., concurring in judgment

458 (SCALIA, J., dissenting), and the Court’s asserted basis
for doing so in this case is dubious, see post, at 1, 4–5
(THOMAS, J., dissenting).
  In any event, the Court’s review of the facts does not
lead it to conclude that Cone is entitled to relief—only that
the courts below did not adequately consider his claim
with respect to sentencing. See ante, at 26 (“Neither the
Court of Appeals nor the District Court fully considered
whether the suppressed evidence” undermines confidence
in Cone’s sentence). The Court simply reviews the facts in
the light most favorable to Cone, concludes that the evi
dence does not undermine confidence in the jury’s deter
mination that Cone is guilty, but sends the case back for
“full consideration” of whether the same is true as to the
jury’s sentence of death. Ante, at 25–27.
  So this is what we are left with: a fact-specific determi
nation, under the established legal standard, viewing the
unique facts in favor of the defendant, that the Brady
claim fails with respect to guilt, but might have merit as
to sentencing. In light of all this, I see no reason to quar
rel with the Court’s ruling on the Brady claim.
  In considering on remand whether the facts establish a
Brady violation, it is clear that the lower courts should
analyze the issue under the constitutional standards we
have set forth, not under whatever standards the Ameri
can Bar Association may have established. The ABA
standards are wholly irrelevant to the disposition of this
case, and the majority’s passing citation of them should
not be taken to suggest otherwise. See ante, at 21, n. 15.
                    Cite as: 556 U. S. ____ (2009)                  1

                         Opinion of ALITO, J.

SUPREME COURT OF THE UNITED STATES
                             _________________

                            No. 07–1114
                             _________________


   GARY BRADFORD CONE, PETITIONER v. RICKY 

               BELL, WARDEN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                           [April 28, 2009] 


   JUSTICE ALITO, concurring in part and dissenting in
part.
   We granted certiorari in this case to answer two ques­
tions:
     “1. Is a federal habeas claim ‘procedurally defaulted’
     because it has been presented twice to the state
     courts?
     “2. Is a federal habeas court powerless to recognize
     that a state court erred in holding that state law pre­
     cludes reviewing a claim?” Pet. for Cert. i.
   Both of these questions are based on a factually incor­
rect premise, namely, that the Tennessee Court of Crimi­
nal Appeals, the highest state court to entertain peti­
tioner’s appeal from the denial of his second petition for
state postconviction relief,1 rejected petitioner’s Brady2
claim on the ground that the claim had been previously

——————
  1 Because  the Tennessee Supreme Court denied discretionary review
of the decision of the Tennessee Court of Criminal Appeals decision
affirming the denial of petitioner’s second amended petition for post­
conviction relief, we must look to the decision of the latter court to
determine if the decision below was based on an adequate and inde­
pendent state ground. See Baldwin v. Reese, 541 U. S. 27, 30–32
(2004); O’Sullivan v. Boerckel, 526 U. S. 838, 842–843 (1999).
  2 Brady v. Maryland, 373 U. S. 83 (1963).
2                      CONE v. BELL

                      Opinion of ALITO, J.

decided by the Tennessee Supreme Court in petitioner’s
direct appeal. Petitioner’s argument is that the State
Supreme Court did not decide any Brady issue on direct
appeal, that the Tennessee Court of Criminal Appeals
erred in holding otherwise, and that the Sixth Circuit
erred in concluding that the Brady claim had been proce­
durally defaulted on this ground. Petitioner is quite cor­
rect that his Brady claim was not decided on direct appeal,
and the Court in the present case is clearly correct in
holding that a second attempt to litigate a claim in state
court does not necessarily bar subsequent federal habeas
review. See ante, at 8–9.
  But all of this is beside the point because the Tennessee
Court of Criminal Appeals did not reject petitioner’s Brady
claim on the ground that the claim had been previously
determined on direct appeal. Rather, petitioner’s Brady
claim was simply never raised before the Tennessee Court
of Criminal Appeals, and that court did not rule on the
claim at all.
  Because the Sixth Circuit’s decision on the issue of
procedural default rests on the same mistaken premise
that the Tennessee Court of Criminal Appeals rejected
petitioner’s Brady claim on the ground that it had been
previously determined, I entirely agree with the majority
that the Sixth Circuit’s decision on that issue cannot be
sustained and that a remand is required. I cannot join the
Court’s opinion, however, for two chief reasons.
  First, the Court states without explanation that “Cone
properly preserved and exhausted his Brady claim in the
state court” and that therefore the claim has not been
defaulted. Ante, at 20. Because Cone never fairly raised
this claim in the Tennessee Court of Criminal Appeals, the
claim is either not exhausted (if Cone could now raise the
claim in state court) or is procedurally defaulted (if state
law now provides no avenue for further review). I would
leave these questions for resolution in the first instance on
                 Cite as: 556 U. S. ____ (2009)            3

                      Opinion of ALITO, J.

remand.
  Second, the Court, again without explanation, remands
this case to the District Court, not the Court of Appeals. I
see no justification for this step.
                              I
  In order to understand the tangled procedural default
issue presented in this case, it is necessary to review the
far-from-exemplary manner in which the attorneys for
petitioner and respondent litigated the Brady claim in the
state courts.
  On direct appeal, petitioner did not raise any Brady
claim. As the Court notes, petitioner did claim that the
State had violated a state discovery rule by failing to
provide prior statements given by certain witnesses and
that therefore the testimony of these witnesses should
have been stricken. App. 114–117; State v. Cone, 665
S. W. 2d 87, 94 (Tenn. 1984). Although this claim con­
cerned the State’s failure to turn over information, it is
clear that this was not a Brady claim.
  The first appearance of anything resembling the claim
now at issue occurred in 1993 when petitioner’s experi­
enced attorneys filed an amendment to his second petition
for postconviction relief in the Shelby County Criminal
Court. This petition included a long litany of tangled
claims. Paragraph 35 of this amended petition claimed,
among other things, that the State had wrongfully with­
held information demonstrating that one particular prose­
cution witness had testified falsely concerning “petitioner
and his drug use.” App. 13–14. This nondisclosure, the
petition stated, violated not only the Fifth and Fourteenth
Amendments to the Constitution of the United States
(which protect the due process right on which Brady is
based) but also the Fourth, Sixth, and Eighth Amend­
ments to the United States Constitution and four provi­
sions of the Tennessee Constitution.
4                          CONE v. BELL

                         Opinion of ALITO, J.

   Two months later, counsel for petitioner filed an
amendment adding 12 more claims, including one (¶41)
alleging that the State had abridged petitioner’s rights by
failing to disclose evidence that petitioner suffered from
drug problems. Id., at 20. According to this new submis­
sion, the nondisclosure violated, in addition to the previ­
ously cited provisions of the federal and state constitu­
tions, five more provisions of the state constitution,
including provisions regarding double jeopardy, see Tenn.
Const., Art. I, §10, ex post facto laws, §11, indictment, §14,
and open courts, §17.
   The Shelby County Criminal Court was faced with the
task of wading through the morass presented in the
amended petition. Under Tenn. Code Ann. §40–30–112
(1990) (repealed 1995),3 a claim could not be raised in a
postconviction proceeding if the claim had been “previ­
ously determined” or waived. Citing the State Supreme
Court’s rejection on direct appeal of petitioner’s claim that
the prosecution had violated a state discovery rule by
failing to turn over witness statements, the State incor­
rectly informed the court that the failure-to-disclose­
exculpatory-evidence claim set out in ¶41 had been “previ­
ously determined” on direct appeal. App. 15–16. The
Shelby County Criminal Court rejected the claim on this
ground, and held that all of petitioner’s claims had either
been previously determined or waived. Id., at 22.
   Given the importance now assigned to petitioner’s
Brady claim, one might think that petitioner’s attorneys
would have (a) stressed that claim in the opening brief
that they filed in the Tennessee Court of Criminal Ap­
——————
   3 Tennessee law has since changed. Currently, the Tennessee Post-

Conviction Procedure Act bars any second postconviction petition, see
Tenn. Code Ann. §40–30–102 (2006), and permits the reopening of a
petition only under limited circumstances, §40–30–117. These restric­
tions apply to any petition filed after the enactment of the Post-
Conviction Procedure Act, even if the conviction occurred long before.
                     Cite as: 556 U. S. ____ (2009)                     5

                          Opinion of ALITO, J.

peals, (b) pointed out the lower court’s clear error in con­
cluding that this claim had been decided in the direct
appeal, and (c) explained that information supporting the
claim had only recently come to light due to the production
of documents under the State’s public records act. But
counsel did none of these things. In fact, the Brady claim
was not mentioned at all.
  Nor was Brady cited in the reply brief filed by the same
attorneys. The reply brief did contain a passing reference
to “the withholding of exculpatory evidence,” but the brief
did not elaborate on this claim and again failed to mention
that this claim had never been previously decided and was
supported by newly discovered evidence.4
  The Tennessee Court of Criminal Appeals affirmed the
decision of the lower state court, but the appellate court
made no mention of the Brady claim, and I see no basis for
concluding that the court regarded the issue as having
been raised on appeal.
  Appellate courts generally do not reach out to decide
issues not raised by the appellant. Snell v. Tunnell, 920
F. 2d 673, 676 (CA10 1990); see Powers v. Hamilton Cty.
Public Defender Comm’n, 501 F. 3d 592, 609–610 (CA6
2007); see also Galvan v. Alaska Dept. of Corrections, 397
F. 3d 1198, 1204 (CA9 2005) (“Courts generally do not
decide issues not raised by the parties. If they granted
relief to petitioners on grounds not urged by petitioners,

——————
   4 After referring to a long list of claims (not including any claim for

the failure to disclose exculpatory evidence), the reply brief states:
“[I]t is clear that meritorious claims have been presented for adjudica­
tion. These claims have not been waived and a remand for a hearing is
essential in order to enable Mr. Cone to present evidence and prove the
factual allegations, including those relating to his claims of ineffective
assistance of counsel, Petition ¶¶15, 16, 44, R–67, 71 and 141 and of the
withholding of exculpatory evidence. Petition ¶41, R–139.” Reply Brief
of Petitioner-Appellant in No. 02–C–01–9403–CR–0052, p. 5 (emphasis
added) (hereinafter Reply Brief).
6                          CONE v. BELL

                          Opinion of ALITO, J.

respondents would be deprived of a fair opportunity to
respond, and the courts would be deprived of the benefit of
briefing” (footnote omitted)). Nor do they generally con­
sider issues first mentioned in a reply brief. Physicians
Comm. For Responsible Medicine v. Johnson, 436 F. 3d
326, 331, n. 6 (CA2 2006); Doe v. Beaumont Independent
School Dist., 173 F. 3d 274, 299, n. 13 (CA5 1999) (Garza,
J., dissenting); Doolin Security Sav. Bank, F. S. B. v.
Office of Thrift Supervision, 156 F. 3d 190, 191 (CADC
1998); Boone v. Carlsbad Bancorporation, Inc., 972 F. 2d
1545, 1554, n. 6 (CA10 1992). And it is common to prac­
tice for appellate courts to refuse to consider issues that
are mentioned only in passing. Reynolds v. Wagner, 128
F. 3d 166, 178 (CA3 1997) (citing authorities).
   The Tennessee Court of Criminal Appeals follows these
standard practices. Rule 10(b) of that court states quite
specifically: “Issues which are not supported by argument,
citation to authorities, or appropriate references to the
record will be treated as waived in this court.” The court
has applied this rule in capital cases, State v. Dellinger, 79
S. W. 3d 458, 495, 497, 503 (Tenn. 2002) (appendix to
majority opinion); Brimmer v. State, 29 S. W. 3d 497, 530
(1998), and in others. See, e.g., State v. Faulkner, 2001
WL 378540 (Tenn. Crim. App., Sept. 10, 2001) (73-year
sentence for first-degree murder). And in both capital and
noncapital cases, the court has refused to entertain
arguments raised for the first time in a reply brief. See
State v. Gerhardt, 2009 WL 160930 (Tenn. Crim. App.,
Jan. 23, 2009) (capital case); Carruthers v. State, 814 S. W.
2d 64, 68 (Tenn. Crim. App. 1991) (capital case); Cammon
v. State, 2007 WL 2409568, *6 (Tenn. Crim. App., Aug. 23,
2007) (noncapital case).5 Thus, unless the Tennessee
——————
  5 In a footnote in his reply brief, petitioner stated that he was not

waiving any claim presented in the court below and asked the appellate
court to consider all those claims. See Reply Brief 3, n. 1. But the
                    Cite as: 556 U. S. ____ (2009)                  7

                         Opinion of ALITO, J.

Court of Criminal Appeals departed substantially from its
general practice, that court did not regard petitioner’s
Brady claim as having been raised on appeal.
   In the decision now under review, the Sixth Circuit held
that “[t]he Tennessee courts found that Cone’s Brady
claims were ‘previously determined’ and, therefore, not
cognizable in [his] state post-conviction action.” 492 F. 3d
743, 756 (2007). In my judgment, however, there is no
basis for concluding that the Tennessee Court of Criminal
Appeals thought that any Brady issue was before it. A
contrary interpretation would mean that the Tennessee
Court of Criminal Appeals, disregarding its own rules and
standard practice, entertained an issue that was not men­
tioned at all in the appellant’s main brief and was men­
tioned only in passing and without any development in the
reply brief. It would mean that the Tennessee Court of
Criminal Appeals, having chosen to delve into the Brady
issue on its own, ruled on the issue without even mention­
ing it in its opinion and without bothering to check the
record to determine whether in fact the Brady issue had
been decided on direct appeal. Such an interpretation is
utterly implausible, and it is telling that the majority
in this case cites no support for such an interpretation in
the opinion of the Tennessee Court of Criminal Appeals’
opinion.
   The Sixth Circuit’s decision on the question of proce­
dural default rests on an erroneous premise and must
therefore be vacated.
                           II
  I also agree with the Court that we should not affirm
the decision below on the ground that the Brady claim
lacks substantive merit. After its erroneous discussion of
——————
Tennessee Court of Criminal Appeals has specifically held that claims
may not be raised on appeal in this manner. See Leonard v. State, 2007
WL 1946662, *21–*22 (Tenn. Crim. App., July 5, 2007).
8                          CONE v. BELL

                          Opinion of ALITO, J.

procedural default, the Sixth Circuit went on to discuss
the merits of petitioner’s Brady claim. In its 2001 opinion,
the Court of Appeals recognized that the prosecution’s
Brady obligation extends not only to evidence that is
material to guilt but also to evidence that is material to
punishment. See Cone v. Bell, 243 F. 3d 961, 968 (2001)
(citing Pennsylvania v. Ritchie, 480 U. S. 39, 57 (1987)).
But neither in that opinion nor in its 2006 opinion did the
court address the materiality of the information in ques­
tion here in relation to petitioner’s punishment. See 492
F. 3d, at 756 (“A review of the allegedly withheld docu­
ments shows that this evidence would not have overcome
the overwhelming evidence of Cone’s guilt in committing a
brutal double murder and the persuasive testimony that
Cone was not under the influence of drugs” (emphasis
added)). Therefore, despite the strength of the arguments
in JUSTICE THOMAS’ dissent, I would leave that question to
be decided by the Sixth Circuit on remand.
                             III
   The Court, however, does not simply vacate and remand
to the Sixth Circuit but goes further.
   First, the Court states without elaboration that peti­
tioner “preserved and exhausted his Brady claim in the
state court.” Ante, at 20. As I have explained, petitioner
did not fairly present his Brady claim in his prior appeal
to the Tennessee Court of Criminal Appeals, and therefore
that claim is either unexhausted or procedurally barred.
If the State is not now foreclosed from relying on the
failure to exhaust, see 28 U. S. C. §2254(b)(3), or on proce­
dural default,6 those questions may be decided on remand.
——————
  6 Unlike exhaustion, procedural default may be waived if it is not

raised as a defense. Banks v. Dretke, 540 U. S. 668, 705 (2004) (allow­
ing for waiver of “procedural default” “based on the State’s litigation
conduct” (citing Gray v. Netherland, 518 U. S. 152, 166 (1996))). Here,
it appears that the State has consistently argued that petitioner’s
                   Cite as: 556 U. S. ____ (2009)                 9

                        Opinion of ALITO, J.

   Second, the Court remands the case to the District
Court rather than the Court of Appeals. A remand to the
District Court would of course be necessary if petitioner
were entitled to an evidentiary hearing, but the Court
does not hold that an evidentiary hearing is either re­
quired or permitted. In my view, unless there is to be an
evidentiary hearing, there is no reason to remand this
case to the District Court. If the only purpose of remand is
to require an evaluation of petitioner’s Brady claim in
light of the present record, the District Court is not in a
superior position to conduct such a review. And even if
such a review is conducted in the first instance by the
District Court, that court’s decision would be subject to de
novo review in the Court of Appeals. 492 F. 3d, at 750;
Cone v. Bell, 243 F. 3d, at 966–967 (CA6 2001); see United
States v. Graham, 484 F. 3d 413 (CA6 2007); United States
v. Miller, 161 F. 3d 977, 987 (CA6 1998); United States v.
Phillip, 948 F. 2d 241, 250 (CA6 1991). Accordingly, I see
no good reason for remanding to the District Court rather
than the Court of Appeals. And if the majority has such a
reason, it is one that it has chosen to keep to itself.
                       *   *     *
  For these reasons, I would vacate the decision of the
Court of Appeals and remand to that court.




——————
Brady claim was procedurally defaulted, but the State’s supporting
arguments have shifted. Whether the question of procedural default
described in this opinion should be entertained under the particular
circumstances here is an intensely fact-bound matter that should be
left for the Sixth Circuit on remand.
                 Cite as: 556 U. S. ____ (2009)            1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 07–1114
                         _________________


   GARY BRADFORD CONE, PETITIONER v. RICKY 

               BELL, WARDEN

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                        [April 28, 2009] 


   JUSTICE THOMAS, with whom JUSTICE SCALIA joins,
dissenting.
   The Court affirms Gary Cone’s conviction for beating an
elderly couple to death with a blunt object. In so doing,
the majority correctly rejects Cone’s argument that his
guilty verdict was secured in violation of his rights under
Brady v. Maryland, 373 U. S. 83 (1963). The majority
declines, however, to decide whether the same evidence
that was insufficient under Brady to overturn his convic
tion provides a basis for overturning his death sentence.
The majority instead remands this question to the District
Court for further consideration because it finds that the
Court of Appeals engaged in a “summary treatment” of
Cone’s Brady sentencing claim. See ante, at 25–27.
   I respectfully dissent. The Court of Appeals’ allegedly
“summary treatment” of Cone’s sentencing claim does not
justify a remand to the District Court. Cone has failed to
establish “ ‘a reasonable probability that, had the evidence
been disclosed to the defense, the result of the [sentencing]
proceeding would have been different,’ ” Kyles v. Whitley,
514 U. S. 419, 435 (1995) (quoting United States v. Bagley,
473 U. S. 667, 682 (1985) (opinion of Blackmun, J.)). As a
result, I would affirm the judgment of the Court of Ap
2                           CONE v. BELL

                         THOMAS, J., dissenting

peals. 1
                                I
   This case arises from a crime spree 28 years ago that
began with Cone’s robbery of a jewelry store in Memphis,
Tennessee, and concluded with his robbery of a drugstore
in Pompano Beach, Florida. Along the way, Cone shot a
police officer and a bystander while trying to escape the
first robbery, attempted to shoot another man in a failed
carjacking attempt, unsuccessfully tried to force his way
into a woman’s apartment at gunpoint, and murdered 93
year-old Shipley Todd and his 79-year-old wife, Cleopatra.
When he was tried on two counts of first-degree murder in
1982, Cone’s sole defense was that he did not have the
requisite intent to commit first-degree murder because
he was in the grip of a chronic amphetamine psychosis.
The jury rejected the defense and convicted Cone of both
murders.
   At sentencing, the Tennessee jury found beyond a rea
sonable doubt that four statutory aggravating factors
applied to Cone’s offense: (1) Cone had been convicted of
one or more previous felonies involving the use or threat of
violence; (2) he had knowingly created a great risk of
death to two or more persons other than the victim during
his act of murder; (3) the murder was especially heinous,
atrocious or cruel in that it involved torture or depravity of
mind; and (4) the murder was committed for the purpose
of avoiding a lawful arrest. Tr. 2151–2152 (Apr. 23, 1982);
see also State v. Cone, 665 S. W. 2d 87, 94–96 (Tenn.


——————
   1 Because I would affirm on the basis of the Court of Appeals’ alterna

tive holding below, I do not reach the issues of procedural default
resolved by the majority. See United States v. Atlantic Research Corp.,
551 U. S. 128, 141, n. 8 (2007); Ayotte v. Planned Parenthood of North
ern New Eng., 546 U. S. 320, 332 (2006); Ardestani v. INS, 502 U. S.
129, 139 (1991).
                    Cite as: 556 U. S. ____ (2009)                   3

                        THOMAS, J., dissenting

1984). Tenn. Code Ann. §39–2-203(i) (1982).2 Cone ar
gued to the jury at sentencing that his “capacity . . . to
appreciate the wrongfulness of his conduct or to conform
his conduct to the requirements of the law was substan
tially impaired as a result of mental disease or defect or
intoxication which was insufficient to establish a defense
to the crime but which substantially affected his judg
ment.” See §39–2-203(j)(8). But the jury found that nei
ther this, nor any other mitigating factor, outweighed the
aggravating factors. The jury, as required by Tennessee
law, unanimously sentenced Cone to death. See §39–2
203(g).
   For almost three decades, Cone’s case has traveled
through the Tennessee and federal courts. This Court has
twice reversed decisions from the Court of Appeals that
invalidated Cone’s conviction and sentence. See Bell v.
Cone, 535 U. S. 685 (2002); Bell v. Cone, 543 U. S. 447
(2005) (per curiam). On remand from this Court’s latest
decision, the Court of Appeals directly considered whether
a handful of police reports, law enforcement bulletins, and
notes that were allegedly withheld from Cone’s trial attor
neys could have changed the result of Cone’s trial or sen
tencing. And, for the second time, the Court of Appeals
held that there was not a “ ‘reasonable probability’ ” that
the evidence would have altered the jury’s conclusion “that
Cone’s prior drug use did not vitiate his specific intent to
murder his victims and did not mitigate his culpability
sufficient to avoid the death sentence.” 492 F. 3d 743, 757
(CA6 2007). The Court of Appeals, therefore, held that
neither Cone’s conviction nor his sentence was invalid.
——————
  2 The Tennessee Supreme Court later concluded that the record in

Cone’s case was doubtful as to evidence supporting the second circum
stance given the lapse in time between the initial events of the escape
and the Todd murders. Cone, 665 S. W. 2d, at 95. The court, however,
determined that the existence of the other three factors rendered any
possible error in this factor harmless beyond a reasonable doubt. Ibid.
4                       CONE v. BELL

                     THOMAS, J., dissenting

See ibid.; Cone v. Bell, 243 F. 3d 961, 968 (CA6 2001). We
should affirm the Court of Appeals and put an end to this
litigation.
                               II
    According to the majority, the Court of Appeals’ decision
affirming Cone’s death sentence is too “summary,” ante, at
25, and the facts are such that, on further examination,
Cone “might” be able to demonstrate that it is “possible”
that the contested evidence would have persuaded the jury
to spare his life, ante, at 25–26. On this reasoning, the
majority remands the case directly to the District Court
for “full consideration [of] the merits of Cone’s [sentencing]
claim.” Ante, at 27. I disagree on all counts. Remanding
the sentencing issue to the District Court is an “unusual
step” for this Court to take. House v. Bell, 547 U. S. 518,
557 (2006) (ROBERTS, C. J., concurring in judgment in part
and dissenting in part). Furthermore, in this case, it is a
step that is legally and factually unjustified. There is not
“ ‘a reasonable probability that, had the evidence been
disclosed to the defense, the result of the proceeding would
have been different.’ ” Kyles, 514 U. S., at 433–434 (quot
ing Bagley, 473 U. S., at 682 (opinion of Blackmun, J.)).
                            A
  The majority’s criticism of the Court of Appeals’ alleg
edly “summary treatment” of the sentencing question is
misplaced. Before the Court of Appeals, Cone dedicated
eight pages of his opening brief to arguing that the impli
cated evidence was material to his guilt or innocence, but
spent only one paragraph arguing its materiality to his
death sentence. See Brief for Appellant in No. 99–5279
(CA6), pp. 40–48. The Court of Appeals’ focus on the guilt
phase, rather than the sentencing phase, simply followed
Cone’s lead. See 492 F. 3d, at 755 (“In his most recent
brief, claiming that his receiving the withheld evidence
                     Cite as: 556 U. S. ____ (2009)                     5

                         THOMAS, J., dissenting

would have resulted in a different sentence, Cone has
made only conclusory arguments”).3        There is nothing
defective about a judicial decision that summarily rejects
an abbreviated legal argument, especially where, as here,
the burden of proving the materiality of the contested
evidence was on Cone.4
                             B
  In remanding this matter to the District Court, the
majority makes two critical errors—one legal and one
factual—that leave the false impression that Cone’s Brady
claim has a chance of success. First, the majority states
that “[i]t is possible that the suppressed evidence” may
have convinced the jury that Cone’s substance abuse
played a mitigating role in his crime and “[t]he evidence
might also have rebutted the State’s suggestion” that
Cone’s experts were inaccurately depicting the depth of his
drug-induced impairment. Ante, at 26 (emphasis added);
see also ante, at 26–27 (remanding “[b]ecause the evidence
suppressed at Cone’s trial may well have been material to
the jury’s assessment of the proper punishment in this
case” (emphasis added)). But, as the majority implicitly
——————
  3 The assertion by the majority, ante, at 26, n. 19, and JUSTICE ALITO,

ante, at 8 (opinion concurring in part and dissenting in part), that the
Court of Appeals did not address the merits of the sentencing issue at
all is flatly wrong. See 492 F. 3d, at 757 (rejecting Cone’s Brady claim
because the proffered evidence would not have altered the jury’s con
clusion “that Cone’s prior drug use did not vitiate his specific intent to
murder his victims and did not mitigate his culpability sufficient to
avoid the death sentence” (emphasis added)).
  4 The majority does not attempt to justify its remand by contending

that it is necessary because the record is insufficient to decide the
claim. Nor could it persuasively contend a remand is necessary so that
the District Court can hold an evidentiary hearing. Such a hearing
would shed no additional light on the trial proceedings or the relative
impeachment value of the withheld documents. Cone himself agrees
that “this Court should resolve the merits of [his] Brady claim.” Reply
Brief for Petitioner 24; see also Brief for Respondent 26–27.
6                       CONE v. BELL

                     THOMAS, J., dissenting

acknowledges, see ante, at 26, n. 19, this is not the correct
legal test for evaluating a Brady claim: “The mere possibil
ity that an item of undisclosed information might have
helped the defense, or might have affected the outcome of
the trial, does not establish ‘materiality’ in the constitu
tional sense.” United States v. Agurs, 427 U. S. 97, 109–
110 (1976) (emphasis added).
   Rather, this Court has made clear that the legal stan
dard for adjudicating such a claim is whether there is a
“reasonable probability” that the jury would have been
persuaded by the allegedly withheld evidence. Kyles,
supra, at 435; Bagley, supra, at 682 (opinion of Blackmun,
J.). It simply is not sufficient, therefore, to claim that
“there is a reasonable possibility that . . . testimony might
have produced a different result . . . . [P]etitioner’s burden
is to establish a reasonable probability of a different re
sult.” Strickler v. Greene, 527 U. S. 263, 291 (1999) (em
phasis in original). To satisfy the “reasonable probability”
standard, Cone must show that “the favorable evidence
could reasonably be taken to put the whole case in such a
different light as to undermine confidence” in the jury’s
sentencing determination. Kyles, supra, at 435. The
Court must view the record “as a whole,” Sawyer v.
Whitley, 505 U. S. 333, 374 (1992) (STEVENS, J., concur
ring in judgment), and determine whether the absence of
the disclosure prevented Cone from receiving “ ‘a trial
resulting in a [sentence] worthy of confidence.’ ” Strickler,
supra, at 290 (quoting Kyles, 514 U. S., at 434).
   In the context of this case, for Cone to establish “ ‘a
reasonable probability that, had the evidence been dis
closed to the defense, the result of the [sentencing] pro
ceeding would have been different,’ ” id., at 435, he must
not only demonstrate that the withheld evidence would
have established that he was substantially impaired as a
result of drug abuse or withdrawal; Cone also must estab
lish that the addition of the allegedly withheld evidence
                      Cite as: 556 U. S. ____ (2009)                     7

                         THOMAS, J., dissenting

ultimately would have led the jury to conclude that any
mitigating factors (including substantial impairment)
outweighed all of the established aggravating factors. See
Tenn. Code Ann. §39–2-203(g).5
   Second, the majority incorrectly claims that to prevail
on his Brady claim, Cone must demonstrate simply that
the withheld evidence supported the inference that he
“was impaired by his use of drugs around the time his
crimes were committed.” See ante, at 21. This is factually
inaccurate because there was already significant evidence
of Cone’s drug use at trial. To establish that the allegedly
withheld evidence would reasonably have had any impact
on his case, Cone must instead show that the evidence
would have supported his claim of substantial mental
impairment from drug use.
   There was extensive evidence at trial that supported the
inference that Cone was not only a longstanding drug
user, but that he was in fact using drugs at the time of his
crimes. The State itself presented significant evidence on
this point. For example, it presented proof that officers
found marijuana cigarette butts, empty drug vials, and
loose syringes in the car that Cone abandoned immedi
ately after the jewelry store robbery. Tr. 1505–1509 (Apr.
19, 1982). The State also did not challenge testimony from
Cone’s mother that Cone used drugs. Id., at 1647, 1648–
1653 (Apr. 20, 1982). And, most tellingly, the State intro
duced evidence that Cone was abusing three drugs—
——————
  5 The majority asserts that the standard under Tennessee law for

demonstrating mental defect or intoxication as a mitigating factor at
sentencing is “far lesser” than the standard for demonstrating insanity
in the guilt phase of a criminal trial. Ante, at 25. But the mitigating
factor still requires a showing that Cone’s mental capacity was “sub
stantially impaired” as a result of mental defect. Tenn. Code Ann. §39–
2-203(j)(8). In any event, the only authority cited by the majority for its
assertion that the standard is “far” lesser than that for insanity is
JUSTICE STEVENS’ lone dissent in a prior appeal in this case. Ante, at
25.
8                           CONE v. BELL

                         THOMAS, J., dissenting

cocaine, Dilaudid, and Demerol—at the time of his arrest
and was suffering “slight withdrawal symptoms” from
them. Id., at 1915–1916, 1920 (Apr. 22, 1982). As the
Court of Appeals explained, “[i]t would not have been news
to the jurors, that Cone was a ‘drug user.’ ” 492 F. 3d, at
757.6
   In contrast, what was contested by the State during
trial was Cone’s defense that his drug use was so signifi
cant that it caused him to suffer from extreme ampheta
mine psychosis at the time of the murders. One of Cone’s
expert witnesses, a neuropharmacologist, testified that by
the summer of 1980, when the crimes occurred, Cone was
ingesting “ferociously large doses” of drugs and that his
increasing tolerance and use of amphetamines caused a
chronic amphetamine psychosis. Tr. 1736–1737, 1744–
1747, 1758–1759 (Apr. 21, 1982). The expert further
testified that if a person with chronic amphetamine psy
chosis were to go into withdrawal, he could suffer extreme
mood swings, “a crashing depression,” and a state of weak
ness so severe that “he could barely lift himself.” Id., at
1857–1859. In this expert’s view, these symptoms could
cause a person to “lose his mind.” Id., at 1859.
   The State contradicted that testimony with significant
——————
    6 Althoughthere were two occasions during closing arguments where
prosecutors intimated that Cone was not a drug user, see Tr. 2014–
2015, 2068 (Apr. 22, 1982), the State’s argument otherwise consistently
focused on the real issue in the case: that Cone was not so significantly
affected by his drug use around the time of his crimes that he was “out
of his mind” or “drug crazy” during the critical days of August 1980.
See id., at 2023–2024, 2071–2084. The majority’s focus on two brief
excerpts from the State’s closing argument fails to faithfully view the
record “as a whole” for purposes of a Brady analysis. See Sawyer v.
Whitley, 505 U. S. 333, 374 (1992) (STEVENS, J., concurring in judg
ment); see also Strickler v. Greene, 527 U. S. 263, 290–291 (1999)
(finding no reasonable probability of a different result even when
prosecutor’s closing argument relied on testimony that could have been
impeached by withheld material).
                 Cite as: 556 U. S. ____ (2009)            9

                    THOMAS, J., dissenting

evidence that Cone did not act like someone who was “out
of his mind” during the commission of his crimes. Rather,
the State argued, Cone behaved rationally during his
initial Tennessee robbery, his subsequent escape, his
flight from Tennessee to Florida after the Todd murders,
his Florida robbery, and his subsequent arrest. See, e.g.,
id., at 2074–2084 (Apr. 22, 1982). To substantiate this
argument, the State called FBI Special Agent Eugene
Flynn to the stand. Agent Flynn testified that, when
captured, Cone coherently detailed his travel from Ten
nessee to Florida, explained his efforts to evade detection
by shaving his beard and buying new clothes, and initi
ated negotiations for a plea bargain. Id., at 1918–1921.
The State also presented testimony from a friend of
Cone’s, Ilene Blankman, that she saw no indication that
Cone was under the influence of drugs or severe with
drawal in the days immediately following the murder of
the Todds. Id., at 1875–1876, 1882–1883 (Apr. 21, 1982).
   Viewing the record as a whole, then, it is apparent that
the contested issue at trial and sentencing was not
whether Cone used drugs, but rather the quantity of
Cone’s drug use and its effect on his mental state. Only if
the evidence allegedly withheld from Cone was relevant to
this question whether Cone suffered from extreme am
phetamine psychosis or other substantial impairment
would the evidence have been exculpatory for purposes of
Brady. See Order Denying Motion for Evidentiary Hear
ing and Order of Partial Dismissal, Cone v. Bell, No. 97–
2312–M1/A (WD Tenn., May 15, 1998), App. to Pet. for
Cert. 119a, n. 9 (explaining that “the issue at trial was not
whether Cone had ever abused any drugs (he clearly had),
but whether he was out of his mind on amphetamines at
the time of the murders”); Tr. 2115–2116 (Apr. 23, 1982).
                          III
  With the legal and factual issues correctly framed, it
10                     CONE v. BELL

                    THOMAS, J., dissenting

becomes clear that Cone cannot establish a reasonable
probability that admission of the evidence—viewed either
individually or cumulatively—would have caused the jury
to alter his sentence.
                             A
                             1
  Cone first argues that he was improperly denied police
reports that included witness statements regarding Cone’s
behavior around the time of his crime spree. The first
statement was given by a convenience store employee,
Robert McKinney, who saw Cone the day before he robbed
the Tennessee jewelry store. When asked whether Cone
appeared “to be drunk or high on anything,” McKinney
answered, “[w]ell he did, he acted real weird . . . he just
wandered around the store.” App. 49. But McKinney
subsequently clarified that Cone “didn’t sound drunk” and
that the reason Cone attracted his attention was because
he “wasn’t acting like a regular customer”; he was “just
kinda wandering” around the store. Motion to Expand the
Record in No. 97–2312–M1 (WD Tenn.), Exh. 2, pp. 3, 4.
Contrary to the majority’s assertion, this interview is not
convincing evidence “that Cone appeared to be ‘drunk or
high’ ” when McKinney saw him. Ante, at 21. McKinney’s
clarification that he had characterized Cone’s behavior as
“weird” because Cone appeared to be killing time rather
than acting like a normal shopper undermines the impli
cation of McKinney’s earlier statement that Cone looked
“weird” because he might have been drunk or on drugs.
Thus, there is little chance that McKinney’s statement
would have provided any significant additional evidence
that Cone was using drugs, let alone provide sentence
changing evidence that he was substantially impaired due
to amphetamine psychosis.
  The second statement was given by Charles and Debbie
Slaughter, who both witnessed Cone fleeing from police
                  Cite as: 556 U. S. ____ (2009)           11

                     THOMAS, J., dissenting

after the jewelry store robbery and reportedly told police
that he looked “wild eyed.” App. 50. Cone had just robbed
a jewelry store, shot a police officer and a bystander, and
was still fleeing from police when seen by the Slaughters.
It is thus unlikely that their observation of a “wild eyed”
man would have been interpreted by the jury to mean that
Cone “was suffering from chronic amphetamine psychosis
at the time of the crimes,” ante, at 21, n. 16, rather than to
mean that Cone looked like a man on the run.
   The third statement is contained in a police report
authored by an officer who helped apprehend Cone after
the Florida drugstore robbery. He reported that he saw a
suspect “at the rear of Sambos restaurant. Subject was
observed to be looking about in a frenzied manner and also
appeared to be looking for a place to run.” App. 53. Noth
ing in this police report either connects Cone to drug use
or appears otherwise capable of altering the jury’s under
standing of Cone’s mental state at the time of the crimes.
It certainly makes perfect sense that Cone was “looking
about in a frenzied manner,” ibid.; he had just robbed a
drugstore and was about to engage in a gun battle with
police in order to evade arrest. The police officer’s descrip
tion of Cone’s appearance under these circumstances thus
does not “undermine confidence” in Cone’s sentence.
Kyles, 514 U. S., at 435.
                             2
  The next category of documents that Cone relies upon to
establish his Brady claim are police bulletins. Some of the
bulletins were sent by Memphis Police Sergeant Roby to
neighboring jurisdictions on the day of the Todd murders
and the day after. The bulletins sought Cone’s apprehen
sion and alternatively described him as a “drug user” or a
“heavy drug user.” App. 55–58. Cone asserts that he
could have used these bulletins to impeach Sergeant
Roby’s trial testimony that the sergeant did not see any
12                         CONE v. BELL

                        THOMAS, J., dissenting

track marks when visiting Cone in jail a week later. Tr.
1939 (Apr. 22, 1982). Cone’s reasoning is faulty for two
key reasons. First, Sergeant Roby never testified that
Cone was not a drug user. His only trial testimony on this
point was simply that he observed no “needle marks” on
Cone’s arm when taking hair samples from him a few days
after Cone’s apprehension. Ibid. Second, the bulletins
establish only “that the police were initially cautious
regarding the characteristics of a person who had commit
ted several heinous crimes.” App. to Pet. for Cert. 119a, n.
9. The bulletins would not have tended to prove that the
fugitive Cone was, in fact, a heavy drug user—let alone
“out of his mind” or otherwise substantially impaired due
to amphetamine psychosis—at the time of his crimes.7
                              3
  Cone also argues that material was withheld that could
have been used to impeach Ilene Blankman’s testimony
that Cone did not appear to be high or in withdrawal when
she helped him obtain a Florida driver’s license during his
efforts to evade arrest in Florida. Tr. 1875–1882 (Apr. 21,
1982). But he again fails to meet the standard for excul
patory evidence set by Brady.
  Cone first points to police notes of a pre-trial interview
with Blankman, which did not reflect the statement she
gave at trial that she saw no track marks on Cone’s arm.
App. 72–73. But Blankman was questioned at trial about
——————
   7 Alert bulletins sent by the FBI similarly identified Cone as a “be

lieved heavy drug user” or a “drug user.” App. 62–70. Cone argues
that these bulletins could have been used to impeach FBI Agent Flynn’s
testimony about Cone’s arrest in Florida. The bulletins would not have
constituted material impeachment evidence, however, for the second
reason identified above. In addition, the bulletins would not have
contradicted any of FBI Agent Flynn’s testimony; he in fact stated at
trial that Cone reported using three drugs and was undergoing mild
drug withdrawal when he was captured in Florida. Tr. 1915–1916
(Apr. 22, 1982).
                  Cite as: 556 U. S. ____ (2009)            13

                     THOMAS, J., dissenting

her failure to initially disclose this fact to police, Tr. 1903
(Apr. 21, 1982), so the jury was fully aware of the omis
sion. Disclosure of the original copy of the police notes
thus could not have had any material effect on the jury’s
deliberations. Moreover, the missing notes also recorded a
damning statement by Blankman that Cone “never used
drugs around” her and she “never saw Cone with drug
paraphernalia.” App. 73. Thus, it is difficult to accept
Cone’s argument that he would have benefited from the
introduction of notes from Blackman’s pretrial interview.
If anything, these police notes would have undermined his
mitigation argument.
   Cone next relies on a report that describes a woman’s
confrontation with the prosecution team and Blankman at
a restaurant during trial. During the encounter, the
woman accused Blankman of lying on the stand in order to
frame Cone for the murders. Id., at 74–75. The report
indicates that the prosecutors politely declined the
woman’s numerous attempts to discuss the merits of the
case and that Blankman said nothing. Id., at 75. Nothing
about this encounter raises doubts about Blankman’s
credibility.
   Last, Cone points to “correspondence in the district
attorney’s files suggest[ing] that the prosecution had been
unusually solicitous of [Blankman’s] testimony.” Brief for
Petitioner 45. But the correspondence was completely
innocuous. One of the notes, sent in response to Blank
man’s request for a copy of her prior statement, expressed
to Blankman that her “cooperation in this particular
matter is appreciated.” App. 76. The prosecutor then sent
a letter to confirm that Blankman would testify at trial.
Id., at 77. And finally, after trial, the prosecutor sent a
note to inform Blankman of the verdict and indicate that
they “certainly appreciate[d] [her] cooperation with [them]
in the trial of Gary Bradford Cone.” Id., at 78. There is
nothing about these notes that “tend[s] to prove any fact
14                     CONE v. BELL

                    THOMAS, J., dissenting

that is both favorable to Cone and material to his guilt or
punishment.” App. to Pet. for Cert. 116a.
                               B
   Viewing the record as a whole, Cone has not come close
to demonstrating that there is a “reasonable probability”
that the withheld evidence, analyzed individually or cu
mulatively, would have changed the result of his sentenc
ing. Much of the impeachment evidence identified by
Cone is of no probative value whatsoever. The police
bulletins do not contradict any of the trial testimony; the
restaurant encounter was innocuous; and the correspon
dence sent by prosecutors to Blankman does not under
mine her testimony or call Cone’s mental state into doubt.
If the remaining evidence has any value to Cone, it is
marginal at best. There was testimony that Blankman
did not initially tell police that Cone lacked track marks.
See Tr. 1903 (Apr. 21, 1982). McKinney clarified in his
statement that Cone’s activity in the store was consistent
with a person killing time, not the use of drugs or alcohol.
And the behavior described by the Slaughters and the
Florida police officer is more naturally attributable to the
circumstances of Cone’s flight from the police than to any
inference that Cone was “out of his mind” or otherwise
substantially impaired due to amphetamine psychosis.
   Countering the trivial value of the alleged Brady mate
rial is the clear and overwhelming evidence that during
Cone’s crime spree, he was neither sufficiently insane to
avoid a conviction of murder nor substantially impaired by
his drug use or withdrawal-related psychosis. There was
substantial evidence that Cone carefully planned the
jewelry store robbery and was calm in carrying it out, Tr.
at 974–976, 1014 (Apr. 16, 1982), 1350–1352 (Apr. 17,
1982), 1501 (Apr. 19, 1982), 2075 (Apr. 22, 1982); that he
successfully eluded police after engaging them in a shoot
out, id., at 1053–1064 (Apr. 16, 1982); that, after hiding
                 Cite as: 556 U. S. ____ (2009)           15

                    THOMAS, J., dissenting

overnight, he concocted a ruse to try to gain illegal entry
to a residence, id., at 1205–1208 (Apr. 17, 1982); that he
murdered the Todds after they declined to cooperate with
his efforts to further elude police, id., at 1681 (Apr. 20,
1982); that he took steps to change his appearance at the
Todd residence and then successfully fled to Florida, id., at
1918–1919 (Apr. 22, 1982); that he arrived in Florida
exhibiting no signs of drug use or severe withdrawal, id.,
at 1875–1882 (Apr. 21, 1982); that he obtained false iden
tification in a further effort to avoid apprehension, id., at
1881–1882, and that he denied any memory lapses and
described undergoing only minor drug withdrawal when
police arrested him, id., at 1919–1920 (Apr. 22, 1982).
Given this wealth of evidence, there is no “reasonable
probability” that the jury would have found that Cone was
entitled to the substantial impairment mitigator had the
evidence he seeks been made available to him.
   And even if Cone could have presented this evidence to
the jury at sentencing and established an entitlement to
this mitigator, he still has not demonstrated a reasonable
probability that it would have outweighed all of the aggra
vating factors supporting the jury’s death sentence. See
id., at 2151–2154 (Apr. 23, 1982). In its decision on direct
appeal, the Tennessee Supreme Court was well aware of
the evidence regarding the “degree and extent of [Cone’s]
drug abuse.” Cone, 665 S. W. 2d, at 90. As part of its
required independent review of whether the mitigation
evidence was sufficiently substantial to outweigh the
aggravating factors, see Tenn. Code Ann. §39–2-205, the
Tennessee court nevertheless concluded that the sentence
was “not in any way disproportionate under all of the
circumstances, including the brutal murders of two elderly
defenseless persons by an escaping armed robber who had
terrorized a residential neighborhood for twenty-four
hours.” 665 S. W. 2d, at 95–96. None of Cone’s proffered
evidence places that conclusion, made by both the jury and
16                     CONE v. BELL

                    THOMAS, J., dissenting

the Tennessee Supreme Court, “in such a different light as
to undermine confidence” in Cone’s sentence. Kyles, 514
U. S., at 435; see also Strickler, 527 U. S., at 296.
                            IV
  This Court should not vacate and remand lower court
decisions based on nothing more than the vague suspicion
that error might be present, or because the court below
could have been more clear. This is especially so where, as
here, the record before the Court is adequate to evaluate
Cone’s Brady claims with respect to both the guilt and
sentencing phases of his trial. The Court’s willingness to
return the sentencing issue to the District Court without
any firm conviction that an error was committed by the
Court of Appeals is inconsistent with our established
practice and disrespectful to the lower courts that have
considered this case. Worse still, the inevitable result will
be years of additional delay in the execution of a death
sentence lawfully imposed by a Tennessee jury. Because I
would affirm the judgment below, I respectfully dissent.

```

---

## GROUP: _overhaul2/lake/cases/Connally v. Georgia.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Connally v. Georgia"
type: case
citation: "429 U.S. 245 (1977)"
parallel_cite: "97 S. Ct. 546; 50 L. Ed. 2d 444"
neutral_cite: 1977 U.S. LEXIS 27
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-01-10
docket: 76-461
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-01-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Connally v. Georgia
  varies_by_point: false
  scope_note: "Controlling: a magistrate with a direct pecuniary interest in issuing warrants is not neutral and detached, so such warrants are void."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109572/connally-v-georgia/"
  cluster_id: 109572
  opinion_id: 109572
  identity_checked: true
homes:
  - page: "[[The Neutral and Detached Magistrate]]"
    role: "Progeny"
related: ["[[Coolidge v. New Hampshire]]", "[[Lo-Ji Sales, Inc. v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant-requirement", "neutral-magistrate"]
holding: "A search warrant issued by a magistrate who is paid a fee for issuing a warrant but nothing for denying one is invalid: such a magistrate has a direct, personal, pecuniary interest in issuance and is not neutral and detached as the Fourth Amendment requires."
lake:
  record_id: Connally v. Georgia
  status: verified
  projected_at: 2026-07-06
---

# Connally v. Georgia

*429 U.S. 245 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Georgia justice of the peace issued a search warrant for Connally's premises. Under Georgia's fee system, the justice received a $5 fee when he issued a warrant and nothing when he declined to issue one. The justice testified that the fee did enter his mind when deciding whether to issue a warrant. Connally challenged the warrant on the ground that it was issued by a magistrate who was not neutral and detached.

## Issue
Is a search warrant valid under the Fourth Amendment when issued by a magistrate who is compensated for issuing the warrant but receives nothing for denying it?

## Rule
No. Applying the principle of *Tumey* and *Ward*, the justice's "financial welfare . . . is enhanced by positive action and is not enhanced by negative action" — a system offering "'a possible temptation to the average man as a judge . . . [that] might lead him not to hold the balance nice, clear and true between the State and the accused.'" — 429 U.S. at 250. ^pin-250

The defendant is thus "subjected to what surely is judicial action by an officer of a court who has 'a direct, personal, substantial, pecuniary interest' in his conclusion to issue or to deny the warrant." — *Id.* ^pin-250b

The Court therefore "h[e]ld that the issuance of the search warrant by the justice of the peace in Connally's case effected a violation of the protections afforded him by the Fourth and Fourteenth Amendments." — *Id.* at 251. ^pin-251

## Application
The Georgia justice of the peace earned $5 only when he issued a warrant and nothing when he denied one, so his compensation rose with issuance — the precise pecuniary temptation the neutral-magistrate requirement forbids, and one he candidly admitted entered his mind. The fee was not *[[Common Legal Terms#de-minimis|de minimis]]*. Because the issuing official had a personal financial stake in granting the warrant, he was not the neutral and detached magistrate the Fourth Amendment demands, and the warrant was invalid.

## Conclusion
The warrant violated the Fourth and Fourteenth Amendments; the judgment of the Georgia Supreme Court was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Connally* remains controlling on the neutral-and-detached-magistrate requirement, applying the disqualifying-financial-interest principle to warrant issuance. It is taught alongside [[Coolidge v. New Hampshire]] (warrant issued by the prosecuting attorney general) and [[Lo-Ji Sales, Inc. v. New York]] (magistrate who joined the search). No negative treatment.

## Appears on
- [[The Neutral and Detached Magistrate]] — *Progeny*

## Sources
- *Connally v. Georgia*, 429 U.S. 245 (1977) (per curiam) — https://www.courtlistener.com/opinion/109572/connally-v-georgia/ — pinpoints: 250, 251.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ca4d4d32e8ae1351", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Connally v. Georgia"}, "payload": {"all": [{"cite": "429 U.S. 245", "page": "245", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "429"}, {"cite": "97 S. Ct. 546", "page": "546", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "50 L. Ed. 2d 444", "page": "444", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "50"}, {"cite": "1977 U.S. LEXIS 27", "page": "27", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "429 U.S. 245", "official": {"cite": "429 U.S. 245", "page": "245", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "429"}, "official_selection_present": true, "record_id": "Connally v. Georgia"}}
{"assertion_id": "28518b2fa00b62f0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-251", "record_id": "Connally v. Georgia"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-251", "pinpoint_status": "slip-only", "quote": "h[e]ld that the issuance of the search warrant by the justice of the peace in Connally's case effected a violation of the protections afforded him by the Fourth and Fourteenth Amendments.", "quote_fidelity": "mismatch", "record_id": "Connally v. Georgia", "star_marker": null}}
{"assertion_id": "a3de19a9537a5d47", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-250b", "record_id": "Connally v. Georgia"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-250b", "pinpoint_status": "slip-only", "quote": "subjected to what surely is judicial action by an officer of a court who has 'a direct, personal, substantial, pecuniary interest' in his conclusion to issue or to deny the warrant.", "quote_fidelity": "mismatch", "record_id": "Connally v. Georgia", "star_marker": null}}
{"assertion_id": "e5671eb2e324286e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-250", "record_id": "Connally v. Georgia"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-250", "pinpoint_status": "slip-only", "quote": "--- # Connally v. Georgia *429 U.S. 245 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Georgia justice of the peace issued a search warrant for Connally's premises. Under Georgia's fee system, the justice received a $5 fee when he issued a warrant and nothing when he declined to issue one. The justice testified that the fee did enter his mind when deciding whether to issue a warrant. Connally challenged the warrant on the ground that it was issued by a magistrate who was not neutral and detached. ## Issue Is a search warrant valid under the Fourth Amendment when issued by a magistrate who is compensated for issuing the warrant but receives nothing for denying it? ## Rule No. Applying the principle of *Tumey* and *Ward*, the justice's", "quote_fidelity": "mismatch", "record_id": "Connally v. Georgia", "star_marker": null}}
{"assertion_id": "28d3835b9eb63650", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Connally v. Georgia"}, "payload": {"as_of_content": "1977-01-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Connally v. Georgia", "scope_note": "Controlling: a magistrate with a direct pecuniary interest in issuing warrants is not neutral and detached, so such warrants are void.", "varies_by_point": false}}
```

### lake record — Connally v. Georgia

```json
{
  "schema_version": "s2.v1",
  "record_id": "Connally v. Georgia",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Connally v. Georgia",
    "case_name_short": "Connally",
    "case_name_full": "Connally v. Georgia",
    "input_case_name": "Connally v. Georgia",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-01-10",
    "year": 1977,
    "docket": "76-461",
    "cluster_id": 109572,
    "lead_opinion_id": 109572,
    "sibling_ids": [
      109572
    ],
    "absolute_url": "/opinion/109572/connally-v-georgia/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 245",
      "volume": "429",
      "reporter": "U.S.",
      "page": "245",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 546",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "546",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 444",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "444",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 27",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "27",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 245",
        "volume": "429",
        "reporter": "U.S.",
        "page": "245",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 546",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "546",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 444",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "444",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 27",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "27",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 245",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 245",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-250",
      "page": null,
      "quote": "--- # Connally v. Georgia *429 U.S. 245 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Georgia justice of the peace issued a search warrant for Connally's premises. Under Georgia's fee system, the justice received a $5 fee when he issued a warrant and nothing when he declined to issue one. The justice testified that the fee did enter his mind when deciding whether to issue a warrant. Connally challenged the warrant on the ground that it was issued by a magistrate who was not neutral and detached. ## Issue Is a search warrant valid under the Fourth Amendment when issued by a magistrate who is compensated for issuing the warrant but receives nothing for denying it? ## Rule No. Applying the principle of *Tumey* and *Ward*, the justice's",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-250b",
      "page": null,
      "quote": "subjected to what surely is judicial action by an officer of a court who has 'a direct, personal, substantial, pecuniary interest' in his conclusion to issue or to deny the warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-251",
      "page": null,
      "quote": "h[e]ld that the issuance of the search warrant by the justice of the peace in Connally's case effected a violation of the protections afforded him by the Fourth and Fourteenth Amendments.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-01-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Connally v. Georgia",
    "varies_by_point": false,
    "scope_note": "Controlling: a magistrate with a direct pecuniary interest in issuing warrants is not neutral and detached, so such warrants are void.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Tennessee v. Rosemary L. Decosimo",
          "cluster_id": 4529649,
          "cite": [
            "555 S.W.3d 494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane1_negative"
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
        "journal_ref": "Connally v. Georgia:lane1_negative"
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
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
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
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Jerrico, Inc.",
          "cluster_id": 110251,
          "cite": [
            "64 L. Ed. 2d 182",
            "100 S. Ct. 1610",
            "446 U.S. 238",
            "1980 U.S. LEXIS 126",
            "24 Wage & Hour Cas. (BNA) 681"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dalia v. United States",
          "cluster_id": 110061,
          "cite": [
            "60 L. Ed. 2d 177",
            "99 S. Ct. 1682",
            "441 U.S. 238",
            "1979 U.S. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ira Silverman (90-3205) Morris G. Woodard (90-5816) and Gary Caton (90-5733/91-6506)",
          "cluster_id": 592207,
          "cite": [
            "976 F.2d 1502",
            "1992 U.S. App. LEXIS 22892"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Felker v. State",
          "cluster_id": 1257587,
          "cite": [
            "314 S.E.2d 621",
            "252 Ga. 351",
            "1984 Ga. LEXIS 691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
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
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mettler Walloon, LLC v. Melrose Township",
          "cluster_id": 1991212,
          "cite": [
            "761 N.W.2d 293",
            "281 Mich. App. 184"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
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
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hyde",
          "cluster_id": 1119531,
          "cite": [
            "921 P.2d 655",
            "186 Ariz. 252",
            "220 Ariz. Adv. Rep. 19",
            "1996 Ariz. LEXIS 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Railey v. Webb",
          "cluster_id": 1268291,
          "cite": [
            "540 F.3d 393",
            "2008 U.S. App. LEXIS 18230",
            "2008 WL 3905492"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lackey v. State",
          "cluster_id": 1308629,
          "cite": [
            "271 S.E.2d 478",
            "246 Ga. 331",
            "1980 Ga. LEXIS 1130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haas v. County of San Bernardino",
          "cluster_id": 2638590,
          "cite": [
            "45 P.3d 280",
            "119 Cal. Rptr. 2d 341",
            "27 Cal. 4th 1017",
            "2002 Cal. Daily Op. Serv. 3888",
            "2002 Daily Journal DAR 4893",
            "2002 Cal. LEXIS 2609"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grigsby v. Mabry",
          "cluster_id": 1518699,
          "cite": [
            "569 F. Supp. 1273",
            "1983 U.S. Dist. LEXIS 14839"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Los Angeles Memorial Coliseum Commission v. National Football League",
          "cluster_id": 8812474,
          "cite": [
            "89 F.R.D. 497",
            "1981 U.S. Dist. LEXIS 13126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harris",
          "cluster_id": 65395,
          "cite": [
            "566 F.3d 422",
            "2009 WL 1065970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Santiago Ramirez",
          "cluster_id": 702391,
          "cite": [
            "63 F.3d 937",
            "42 Fed. R. Serv. 1270",
            "1995 U.S. App. LEXIS 21416",
            "1995 WL 465806"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Slaughter",
          "cluster_id": 1408323,
          "cite": [
            "315 S.E.2d 865",
            "252 Ga. 435",
            "1984 Ga. LEXIS 731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William (Bob) Brown v. Wiley C. Edwards and All Other Constables in the State of Mississippi",
          "cluster_id": 427621,
          "cite": [
            "721 F.2d 1442",
            "1984 U.S. App. LEXIS 26739"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ryan",
          "cluster_id": 2001201,
          "cite": [
            "601 N.W.2d 473",
            "257 Neb. 635",
            "1999 Neb. LEXIS 158"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ismene M. Kalaris, Administrative Appeals Judge v. Raymond J. Donovan, Secretary of Labor, Julius Miller, Administrative Appeals Judge v. Raymond J. Donovan, Secretary of Labor, Ismene M. Kalaris, Administrative Appeals Judge v. Raymond J. Donovan, Secretary of Labor Julius Miller, Administrative Appeals Judge v. Raymond J. Donovan, Secretary of Labor",
          "cluster_id": 413120,
          "cite": [
            "697 F.2d 376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John P. Davern",
          "cluster_id": 587642,
          "cite": [
            "970 F.2d 1490",
            "1992 WL 167526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharon Pollard",
          "cluster_id": 461623,
          "cite": [
            "778 F.2d 1177",
            "19 Fed. R. Serv. 593",
            "1985 U.S. App. LEXIS 24958"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Margaret T. Whitacre v. James F. Davey",
          "cluster_id": 532956,
          "cite": [
            "890 F.2d 1168",
            "281 U.S. App. D.C. 363",
            "1989 U.S. App. LEXIS 17393",
            "52 Empl. Prac. Dec. (CCH) 39,478",
            "51 Fair Empl. Prac. Cas. (BNA) 538",
            "1989 WL 140507"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waterman Steamship Corp. v. Avondale Shipyards, Inc.",
          "cluster_id": 2369360,
          "cite": [
            "527 F. Supp. 256",
            "1981 U.S. Dist. LEXIS 16059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connally v. Georgia:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109572) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 93,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 93,
        "triage_read": 2,
        "triage_snippet_classified": 91
      },
      "lane2_top_cited": {
        "query": "cites:(109572)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMiZzPTEyNDQxODImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109572%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109572)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109572)",
    "indexed_citing_opinions": 111,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109572,
        "count": 111,
        "count_source": "search"
      }
    ],
    "citation_count": 175,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/connally-v-georgia.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjIxMjc2NTMmcz0yOTc2OTU2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109572%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109572,
        "cited_id": 101031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 101283,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 102105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 108629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 1090898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109572,
        "cited_id": 1296142,
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
    "date_created": "2026-07-05T00:52:15Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:52:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:52:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:56:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:52:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Connally v. Georgia

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b395-9">
  Per Curiam.
 </author>
<p id="b395-10">
  Appellant John Connally was indicted, tried, and convicted in the Superior Court of Walker County, Ga., for possession of marihuana in violation of the Georgia Controlled Substances Act, Ga. Code Ann. § 79A-801
  <em>
   et seq.
  </em>
  (1973). On his appeal to the Supreme Court of Georgia, he asserted trial error in four respects: the constitutional impropriety of the fee system governing the issuance of search warrants by justices of the peace in Georgia; the deprivation of his right of confrontation when revelation of an informer’s identity was refused; the failure to give a requested instruction on joint occupancy of premises; and the failure to enter a judgment of acquittal because of an alleged absence of proof of the type of cannabis involved. The Supreme Court of Georgia affirmed, with two justices dissenting (one on the first issue) and one justice concurring as to the second, third, and fourth issues and in the judgment. <span class="citation" data-id="9854792"><a href="/opinion/1296142/connally-v-state/" aria-description="Citation for case: Connally v. State">237 Ga. 203</a></span>, <span class="citation" data-id="9854792"><a href="/opinion/1296142/connally-v-state/" aria-description="Citation for case: Connally v. State">227 S. E. 2d 352</a></span> (1976). The appellant, on direct appeal here,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  raises
  <span citation-index="1" class="star-pagination" label="246"> 
   *246
   </span>
  the first two questions. We deem the challenge to the warrant procedure worthy of consideration.
 </p>
<p id="b396-5">
  Pursuant to a search warrant issued by a justice of the peace, appellant's house was raided and marihuana found there was seized. Connally was arrested.. At his trial he moved to suppress the evidence so seized on the ground that the justice who had issued the warrant was not “a neutral and detached magistrate”
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  because he had a pecuniary interest in issuing the warrant. The trial court denied that motion, and the Supreme Court of Georgia, in affirming, rejected the constitutional challenge.
 </p>
<p id="b396-6">
  Under <span class="citation no-link">Ga. Code Ann. § 24-1601</span> (1971), the fee for the issuance of a search warrant by a Georgia justice of the peace “shall be” $5, “and it shall be lawful for said [justice] of the peace to charge and collect the same.” If the requested warrant is refused, the justice of the peace collects no fee for reviewing and denying the application. The fee so charged apparently goes into county funds and from there to the issuing justice as compensation.
 </p>
<p id="b396-7">
  At a pretrial hearing in Connally's case, the issuing justice testified on cross-examination that he was a justice primarily because he was “interested in a livelihood,” Record 502; that he received no salary,
  <em>
   ibid.;
  </em>
  that his compensation was “directly dependent on how many warrants” he issued,
  <em>
   ibid.;
  </em>
  that since January 1, 1973, he had issued “some 10,000” warrants for arrests or searches,
  <em>
   ibid.;
  </em>
  and that he had no legal background other than attendance at seminars and reading law,
  <span class="citation no-link"><em>
   id.,
  </em>
  at 506-508, 512-515</span>.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b397-4">
<span citation-index="1" class="star-pagination" label="247"> 
   *247
   </span>
  Fifty years ago, in
  <em>
   Tumey
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">273 U. S. 510</a></span> (1927), the Court considered state statutes that permitted a charge of violating the State’s prohibition laws to be tried without
  <span citation-index="1" class="star-pagination" label="248"> 
   *248
   </span>
  a jury before a village mayor. Any fine imposed was divided between the State and the village. The latter’s share was used to hire attorneys and detectives to arrest offenders and
  <span citation-index="1" class="star-pagination" label="249"> 
   *249
   </span>
  prosecute them before the mayor. When the mayor convicted, he received fees and costs, and these were in addition to his salary. The Court, in an opinion by Mr. Chief Justice Taft, unanimously held that subjecting a defendant to trial before a judge having “a direct, personal, pecuniary interest in convicting the defendant,” that is, in the $12 of fees and costs imposed,
  <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/#523" aria-description="Citation for case: Tumey v. Ohio"><em>
   id.,
  </em>
  at 523, 531</a></span>, effected a denial of due process in violation of the Fourteenth Amendment.
 </p>
<p id="b399-6">
  This approach was reiterated in
  <em>
   Ward
  </em>
  v.
  <em>
   Village of Monroeville,
  </em>
  <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/" aria-description="Citation for case: Ward v. Village of Monroeville">409 U. S. 57</a></span> (1972). There, an Ohio statute authorized mayors to sit as judges of ordinance violations and certain traffic offenses. The petitioner was so convicted and fined by the mayor of Monroeville. Although the mayor had no direct personal financial stake in the outcome of cases before him, a major portion of the village’s income was derived from the fines, fees, and costs imposed in the mayor’s court. This Court,
  <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/#59" aria-description="Citation for case: Ward v. Village of Monroeville"><em>
   id.,
  </em>
  at 59-60</a></span>, cited
  <em>
   <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">Tumey</a></span>
  </em>
  and repeated the test formulated in that case, namely, “whether the may- or’s situation is one ‘which would offer a possible temptation to the average man as a judge to forget the burden of proof required to convict the defendant, or which might lead him not to hold the balance nice, clear and true between the State and the accused ....’” <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/#60" aria-description="Citation for case: Ward v. Village of Monroeville">409 U. S., at 60</a></span>.
  <em>
   Dugan
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="101283"><a href="/opinion/101283/dugan-v-ohio/" aria-description="Citation for case: Dugan v. Ohio">277 U. S. 61</a></span> (1928), where a mayor had judicial, functions but only “very limited executive authority,” and the executive power rested in a city manager and a commission, was distinguished as a situation where “the Mayor’s relationship to the finances and financial policy of the city was too remote to warrant a presumption of bias toward conviction in prosecutions before him as [a] judge,” <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/#60" aria-description="Citation for case: Ward v. Village of Monroeville">409 U. S., at 60-61</a></span>,
  <span citation-index="1" class="star-pagination" label="250"> 
   *250
   </span>
  and the possibility of a later
  <em>
   de novo
  </em>
  trial in another court was held to be of no constitutional relevance because the defendant was “entitled to a neutral and detached judge in the first instance.”
  <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/#61" aria-description="Citation for case: Ward v. Village of Monroeville"><em>
   Id.,
  </em>
  at 61-62</a></span>.
 </p>
<p id="b400-5">
  The present case, of course, is not precisely the same as
  <em>
   <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">Tumey</a></span>
  </em>
  or as
  <em>
   <span class="citation" data-id="9425043"><a href="/opinion/108629/ward-v-village-of-monroeville/" aria-description="Citation for case: Ward v. Village of Monroeville">Ward</a></span>,
  </em>
  but the principle of those cases, we conclude, is applicable to the Georgia system for the issuance of search warrants by justices of the peace. The justice is not salaried. He is paid, so far as search warrants are concerned, by receipt of the fee prescribed by statute for his
  <em>
   issuance
  </em>
  of the warrant, and he receives nothing for his
  <em>
   denial
  </em>
  of the warrant. His financial welfare, therefore, is enhanced by positive action and is not enhanced by negative action. The situation, again, is one which offers “a possible temptation to the average man as a judge ... or which might lead him not to hold the balance nice, clear and true between the State and the accused.” It is, in other words, another situation where the defendant is subjected to what surely is judicial action by an officer of a court who has “a direct, personal, substantial, pecuniary interest” in his conclusion to issue or to deny the warrant. See
  <em>
   Bennett
  </em>
  v.
  <em>
   Cottingham,
  </em>
  <span class="citation" data-id="2147032"><a href="/opinion/2147032/bennett-v-cottingham/#762" aria-description="Citation for case: Bennett v. Cottingham">290 F. Supp. 759, 762-763</a></span> (ND Ala. 1968), aff’d, <span class="citation multiple-matches"><a href="/c/U.%20S./393/317/">393 U. S. 317</a></span> (1969).
 </p>
<p id="b400-6">
<em>
   Shadwick
  </em>
  v.
  <em>
   City of Tampa,
  </em>
  <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345</a></span> (1972), does not weigh to the contrary. The issue there centered in the qualification of municipal court clerks to issue arrest warrants for breaches of ordinances. The Court held that the clerks, although laymen, worked within the judicial branch under the supervision of judges and were qualified to determine the existence of probable cause. They were, therefore, “neutral and detached magistrates for purposes of the Fourth Amendment.”
  <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#346" aria-description="Citation for case: Shadwick v. City of Tampa"><em>
   Id.,
  </em>
  at 346</a></span>. There was no element of personal financial gain in the clerks’ issuance or nonissuance of arrest warrants. Cf.
  <em>
   Coolidge
  </em>
  v.
  <em>
   New Hampshire,
  </em>
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 449-453</a></span> (1971).
 </p>
<p id="b401-4">
<span citation-index="1" class="star-pagination" label="251"> 
   *251
   </span>
  We disagree with the Supreme Court of Georgia’s rulings, <span class="citation" data-id="9854792"><a href="/opinion/1296142/connally-v-state/#205" aria-description="Citation for case: Connally v. State">237 Ga., at 205-206</a></span>, <span class="citation" data-id="9854792"><a href="/opinion/1296142/connally-v-state/#354" aria-description="Citation for case: Connally v. State">227 S. E. 2d, at 354-355</a></span>, that the amount of the search warrant fee is
  <em>
   de minimis
  </em>
  in the present context, that the unilateral character of the justice’s adjudication of probable cause distinguishes the present case from
  <em>
   Turney,
  </em>
  and that, instead, this case equates with
  <em>
   Bevan
  </em>
  v.
  <em>
   Krieger,
  </em>
  <span class="citation" data-id="102105"><a href="/opinion/102105/bevan-v-krieger/#465" aria-description="Citation for case: Bevan v. Krieger">289 U. S. 459, 465-466</a></span> (1933), where a notary public’s fee for taking a deposition was measured by the folios of testimony taken.
 </p>
<p id="b401-5">
  We therefore hold that the issuance of the search warrant by the justice of the peace in Connally’s case effected a violation of the protections afforded him by the Fourth and Fourteenth Amendments of the United States Constitution. The judgment of the Supreme Court of Georgia is vacated, and the case is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b401-6">
<em>
   So ordered.
  </em>
</p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b395-11">
   Cf.
   <em>
    Stone
   </em>
   v.
   <em>
    Powell,
   </em>
   <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b396-8">
   See
   <em>
    Johnson
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948);
   <em>
    Coolidge
   </em>
   v.
   <em>
    New Hampshire,
   </em>
   <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#453" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 453</a></span> (1971);
   <em>
    Shadwick
   </em>
   v.
   <em>
    City of Tampa,
   </em>
   <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#350" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345, 350</a></span> (1972).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b396-9">
   “Q In the case of a search warrant, I believe you receive compensation ultimately in the amount of $5.00, if you issue the warrant, do you not?
  </p>
<p id="b396-10">
   “A That’s true.
  </p>
<p id="b397-5">
<span citation-index="1" class="star-pagination" label="247"> 
    *247
    </span>
   “Q If you choose not to issue the warrant, what compensation do you receive?
  </p>
<p id="b397-6">
   “A I don’t know.
  </p>
<p id="b397-7">
   “Q You receive no compensation?
  </p>
<p id="b397-8">
   “A Well, I never have, I’ll put it that way.
  </p>
<p id="b397-9">
   “Q Now with respect to issuing the search warrant, Mr. Murphy, does the $5.00, since that’s the only way you get paid, does that enter your mind when you’re sitting there contemplating whether or not to issue a search warrant?
  </p>
<p id="b397-10">
   “A It has.
  </p>
<p id="b397-11">
   “Q As a matter of fact, I believe you quite honestly and candidly told me on the day we had that preliminary hearing up here, I believe that was on, the best I can recall, it was on the 18th of May, that you would be a liar if you said it didn’t enter your mind?
  </p>
<p id="b397-12">
   “A That’s what I said.
  </p>
<p id="b397-13">
   “Q Is that true now, you would be [a] liar if you said it didn’t enter your mind?
  </p>
<p id="b397-14">
   “A It’s only human nature to me.
  </p>
<p id="b397-15">
   “Q Okay. Now, I believe you said you had been a J. P. since January 1st of 1973, is that correct?
  </p>
<p id="b397-16">
<em>
    “A
   </em>
   Yes, sir.
  </p>
<p id="b397-17">
   “Q All right. Now, since January — you have to run for that office, or is it an appointed office?
  </p>
<p id="b397-18">
   “A Yes sir, it’s an elected office.
  </p>
<p id="b397-19">
   “Q Well, you ran for the office for the purpose of having employment and earning a living, is that correct?
  </p>
<p id="b397-20">
   “A That’s part of it.
  </p>
<p id="b397-21">
   “Q Of course, you like in other people’s motivations, primarily you were interested in a livelihood?
  </p>
<p id="b397-22">
   “A True.
  </p>
<p id="b397-23">
   “Q Now do you support yourself with the salary or with the fees that you receive in a J. P. system down here, or as J. P.?
  </p>
<p id="b397-24">
<em>
    “A
   </em>
   Uh huh, yes sir.
  </p>
<p id="b397-25">
   “Q And you receive no salary at all, so that your compensation is directly dependent on how many warrants you issue, is that correct?
  </p>
<p id="b398-5">
<span citation-index="1" class="star-pagination" label="248"> 
    *248
    </span>
<em>
    “A
   </em>
   That’s right.
  </p>
<p id="b398-6">
   “Q Now, since January 1st, 1973, I
   <em>
    believe you
   </em>
   told me the
   <em>
    other
   </em>
   day, and let me ask you again, you have issued some 10,000 warrants of the arrest — either arrest or search warrants, is that correct?
  </p>
<p id="b398-7">
   “A That’s pretty close, total warrants.
  </p>
<p id="b398-8">
   “Q Okay. Total warrants?
  </p>
<p id="b398-9">
   “A Criminal warrants.
  </p>
<p id="b398-10">
   “Q That would be right about 10,000 of them?
  </p>
<p id="b398-11">
<em>
    “A
   </em>
   Uh huh.
  </p>
<p id="b398-12">
   “Q Now with respect to the qualifications that you have for your office, of course, the people of Walker County elected you and under the law that would qualify you, but I believe the law prescribes some qualifications that you must have prior to the time you are elected, what are those qualifications?
  </p>
<p id="b398-13">
   “A You have to be a resident of the militia district in which you’re running for that office, registered voter, it might sound stupid but that’s all I remember.
  </p>
<p id="b398-14">
   “Q Okay. Now of course, the people have selected you as the J. P. for this militia district, and you have the qualifications that you mentioned that you are a resident and of age and so on and so forth, other than those, do you have any background, legal background or other background with respect to the instruments and issuance of warrants?
  </p>
<p id="b398-15">
<em>
    “A
   </em>
   No, sir.
  </p>
<p id="b398-16">
   “Q So, the qualifications that you have mentioned are your sole qualifications for holding your job, is that correct?
  </p>
<p id="b398-17">
   “A That’s right.
  </p>
<p id="b398-18">
   “Q Okay.
  </p>
<p id="b398-19">
   “A Up to the time I was elected.
  </p>
<p id="b398-20">
   "MR. DANIEL: Okay, sir, that’s all I have.
  </p>
<p id="b398-21">
   “THE COURT: Have you done anything since you were elected to improve any qualifications that might be necessary?
  </p>
<p id="b398-22">
   “THE WITNESS: Yes, sir.
  </p>
<p id="b398-23">
   “THE COURT: What have you done?
  </p>
<p id="b398-24">
   “THE WITNESS: I have attended several training seminars sponsored by our J. P. State Association, as a matter of fact, I’m leaving
   <span citation-index="1" class="star-pagination" label="249"> 
    *249
    </span>
   this afternoon if I can get out of here to go to a 2-day training seminar in Warner Robbins, Georgia, sponsored by the same State Association.
  </p>
<p id="b399-8">
   “I’ve bought one manual, study course from Judson-Pace at my own expense and attempted to learn a little bit more about the duties.” Record 499-500, 501-502, 506-508.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Connecticut v. Barrett.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Connecticut v. Barrett"
type: case
citation: "479 U.S. 523 (1987)"
parallel_cite: "107 S. Ct. 828; 93 L. Ed. 2d 920; 55 U.S.L.W. 4151"
neutral_cite: 1987 U.S. LEXIS 419
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-01-27
docket: 85-899
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-01-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Connecticut v. Barrett
  varies_by_point: false
  scope_note: Good law.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111796/connecticut-v-barrett/"
  cluster_id: 111796
  opinion_id: 111796
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Edwards v. Arizona]]", "[[Smith v. Illinois]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "invocation", "right-to-counsel"]
holding: "A suspect may make a limited invocation of counsel; where he refuses to give a written statement without a lawyer but affirmatively agrees to talk orally, that limited request does not bar oral interrogation — courts honor the scope of the invocation as the suspect framed it."
lake:
  record_id: Connecticut v. Barrett
  status: verified
  projected_at: 2026-07-06
---

# Connecticut v. Barrett

*479 U.S. 523 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After [[Miranda and Custodial Interrogation|Miranda warnings]], Barrett told police he would not give a *written* statement without a lawyer present, but that he was willing to talk about the incident *orally*. The police took his oral statements without counsel. The Connecticut Supreme Court treated his refusal to give a written statement as an invocation of counsel barring all interrogation and suppressed the oral statements.

## Issue
Whether a suspect who refuses to make a written statement without counsel, but agrees to speak orally, has invoked his right to counsel so as to bar all further interrogation under *[[Edwards v. Arizona]]*.

## Rule
No. The right to counsel may be invoked in a limited way, and authorities may honor the limits the suspect himself sets. "Nothing in our decisions, however, or in the rationale of *Miranda*, requires authorities to ignore the tenor or sense of a defendant's response to these warnings." — 479 U.S. at 528. ^pin-528

Barrett's "limited requests for counsel ... were accompanied by affirmative announcements of his willingness to speak with the authorities," so taking his oral confession "is quite consistent with the Fifth Amendment. *Miranda* gives the defendant a right to choose between speech and silence, and Barrett chose to speak." — *Id.* at 529. ^pin-529

## Application
Barrett drew his own line: counsel for a written statement, but a willingness to talk orally. That was not a blanket invocation triggering *[[Edwards v. Arizona|Edwards]]*'s bar on all questioning. Because his decision to speak orally was a voluntary waiver and he was not "threatened, tricked, or cajoled," the police permissibly took his oral statements. The Connecticut court erred by construing his limited request as an all-purpose invocation.

## Conclusion
A limited invocation is honored as made; Barrett's oral statements were admissible. The Connecticut Supreme Court's suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Barrett* complements [[Edwards v. Arizona]] and [[Smith v. Illinois]]: an invocation must be respected, but its **scope** is set by the suspect's own words; a partial invocation does not automatically bar all questioning.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Connecticut v. Barrett*, 479 U.S. 523 (1987) — https://www.courtlistener.com/opinion/111796/connecticut-v-barrett/ — pinpoints: 528, 529.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "378656600947b445", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Connecticut v. Barrett"}, "payload": {"all": [{"cite": "479 U.S. 523", "page": "523", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "479"}, {"cite": "107 S. Ct. 828", "page": "828", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "93 L. Ed. 2d 920", "page": "920", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "1987 U.S. LEXIS 419", "page": "419", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "55 U.S.L.W. 4151", "page": "4151", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "479 U.S. 523", "official": {"cite": "479 U.S. 523", "page": "523", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "479"}, "official_selection_present": true, "record_id": "Connecticut v. Barrett"}}
{"assertion_id": "34cd0c34f91d7ec4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-529", "record_id": "Connecticut v. Barrett"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-529", "pinpoint_status": "slip-only", "quote": "limited requests for counsel ... were accompanied by affirmative announcements of his willingness to speak with the authorities,", "quote_fidelity": "mismatch", "record_id": "Connecticut v. Barrett", "star_marker": null}}
{"assertion_id": "bf626c61a5209b3c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-528", "record_id": "Connecticut v. Barrett"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-528", "pinpoint_status": "slip-only", "quote": "--- # Connecticut v. Barrett *479 U.S. 523 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Miranda warnings, Barrett told police he would not give a *written* statement without a lawyer present, but that he was willing to talk about the incident *orally*. The police took his oral statements without counsel. The Connecticut Supreme Court treated his refusal to give a written statement as an invocation of counsel barring all interrogation and suppressed the oral statements. ## Issue Whether a suspect who refuses to make a written statement without counsel, but agrees to speak orally, has invoked his right to counsel so as to bar all further interrogation under *Edwards v. Arizona*. ## Rule No. The right to counsel may be invoked in a limited way, and authorities may honor the limits the suspect himself sets.", "quote_fidelity": "mismatch", "record_id": "Connecticut v. Barrett", "star_marker": null}}
{"assertion_id": "730c7cc6972f0792", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Connecticut v. Barrett"}, "payload": {"as_of_content": "1987-01-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Connecticut v. Barrett", "scope_note": "Good law.", "varies_by_point": false}}
```

### lake record — Connecticut v. Barrett

```json
{
  "schema_version": "s2.v1",
  "record_id": "Connecticut v. Barrett",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Connecticut v. Barrett",
    "case_name_short": "Barrett",
    "case_name_full": "Connecticut v. Barrett",
    "input_case_name": "Connecticut v. Barrett",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-01-27",
    "year": 1987,
    "docket": "85-899",
    "cluster_id": 111796,
    "lead_opinion_id": 111796,
    "sibling_ids": [
      111796,
      9430786,
      9430787,
      9430788
    ],
    "absolute_url": "/opinion/111796/connecticut-v-barrett/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "479 U.S. 523",
      "volume": "479",
      "reporter": "U.S.",
      "page": "523",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 828",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 920",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "920",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4151",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4151",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 419",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "419",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "479 U.S. 523",
        "volume": "479",
        "reporter": "U.S.",
        "page": "523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 828",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 920",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "920",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 419",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "419",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4151",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4151",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "479 U.S. 523",
    "official_selection": {
      "court_class": "scotus",
      "selected": "479 U.S. 523",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-528",
      "page": null,
      "quote": "--- # Connecticut v. Barrett *479 U.S. 523 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Miranda warnings, Barrett told police he would not give a *written* statement without a lawyer present, but that he was willing to talk about the incident *orally*. The police took his oral statements without counsel. The Connecticut Supreme Court treated his refusal to give a written statement as an invocation of counsel barring all interrogation and suppressed the oral statements. ## Issue Whether a suspect who refuses to make a written statement without counsel, but agrees to speak orally, has invoked his right to counsel so as to bar all further interrogation under *Edwards v. Arizona*. ## Rule No. The right to counsel may be invoked in a limited way, and authorities may honor the limits the suspect himself sets.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-529",
      "page": null,
      "quote": "limited requests for counsel ... were accompanied by affirmative announcements of his willingness to speak with the authorities,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-01-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Connecticut v. Barrett",
    "varies_by_point": false,
    "scope_note": "Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tellez-Suarez",
          "cluster_id": 10134379,
          "cite": [
            "312 Or. App. 531",
            "493 P.3d 28"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
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
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
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
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robin Lynn Anderson v. State",
          "cluster_id": 2850439,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Larry Winsett v. Odie Washington, Warden of Dixon Correctional Center",
          "cluster_id": 748614,
          "cite": [
            "130 F.3d 269",
            "1997 U.S. App. LEXIS 32286",
            "1997 WL 716044"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cothren v. State",
          "cluster_id": 1913446,
          "cite": [
            "705 So. 2d 849",
            "1997 WL 15337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Hendricks",
          "cluster_id": 6130812,
          "cite": [
            "222 A.D.2d 74",
            "646 N.Y.S.2d 845",
            "1996 N.Y. App. Div. LEXIS 8596"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cooper v. Dupnik",
          "cluster_id": 9008075,
          "cite": [
            "963 F.2d 1220",
            "1992 WL 88704"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane1_negative"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. District Court in & for First Judicial District, Jefferson County",
          "cluster_id": 1138536,
          "cite": [
            "785 P.2d 141",
            "14 Brief Times Rptr. 75",
            "1990 Colo. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Withrow v. Williams",
          "cluster_id": 112847,
          "cite": [
            "123 L. Ed. 2d 407",
            "113 S. Ct. 1745",
            "507 U.S. 680",
            "1993 U.S. LEXIS 2980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1801669,
          "cite": [
            "49 Cal. 4th 405",
            "2010 D.A.R. 10",
            "111 Cal. Rptr. 3d 589",
            "233 P.3d 1000",
            "2010 Cal. LEXIS 5970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Mauro",
          "cluster_id": 111878,
          "cite": [
            "95 L. Ed. 2d 458",
            "107 S. Ct. 1931",
            "481 U.S. 520",
            "1987 U.S. LEXIS 1933"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1784340,
          "cite": [
            "587 So. 2d 848",
            "1991 WL 178413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Martinez",
          "cluster_id": 2637824,
          "cite": [
            "47 Cal. 4th 911",
            "10 Cal. Daily Op. Serv. 583",
            "224 P.3d 877",
            "105 Cal. Rptr. 3d 131",
            "2010 Cal. LEXIS 111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Sully",
          "cluster_id": 1386747,
          "cite": [
            "812 P.2d 163",
            "53 Cal. 3d 1195",
            "283 Cal. Rptr. 144",
            "91 Cal. Daily Op. Serv. 5489",
            "1991 Cal. LEXIS 2977"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
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
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 1654613,
          "cite": [
            "760 N.W.2d 35",
            "277 Neb. 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ian Gordon, United States of America v. Ian Gordon",
          "cluster_id": 536184,
          "cite": [
            "895 F.2d 932"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gerald",
          "cluster_id": 2260422,
          "cite": [
            "549 A.2d 792",
            "113 N.J. 40",
            "83 A.L.R. 4th 331",
            "1988 N.J. LEXIS 107"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alvarado v. State",
          "cluster_id": 2450595,
          "cite": [
            "853 S.W.2d 17",
            "1993 Tex. Crim. App. LEXIS 70",
            "1993 WL 89307"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis Rosa Collazo v. Wayne Estelle, Warden, California Mens Colony",
          "cluster_id": 565270,
          "cite": [
            "940 F.2d 411",
            "91 Daily Journal DAR 8681",
            "91 Cal. Daily Op. Serv. 5640",
            "1991 U.S. App. LEXIS 15265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hunter",
          "cluster_id": 1659158,
          "cite": [
            "840 S.W.2d 850",
            "1992 WL 308879"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Thomas",
          "cluster_id": 844168,
          "cite": [
            "54 Cal. 4th 908",
            "281 P.3d 361",
            "144 Cal. Rptr. 3d 366",
            "2012 WL 3043901",
            "2012 Cal. LEXIS 7089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hooks v. State",
          "cluster_id": 1765577,
          "cite": [
            "534 So. 2d 329"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. State",
          "cluster_id": 1775207,
          "cite": [
            "779 S.W.2d 417",
            "1989 Tex. Crim. App. LEXIS 185",
            "1989 WL 122612"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Montez",
          "cluster_id": 1345733,
          "cite": [
            "789 P.2d 1352",
            "309 Or. 564",
            "1990 Ore. LEXIS 68"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Murray",
          "cluster_id": 1824177,
          "cite": [
            "827 So. 2d 488",
            "2002 WL 1980814"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connecticut v. Barrett:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111796 OR 9430786 OR 9430787 OR 9430788) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDUwMjQwMDAwMDAmcz01ODM0NDcmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111796+OR+9430786+OR+9430787+OR+9430788%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111796 OR 9430786 OR 9430787 OR 9430788)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTAmcz03NDg2MTQmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111796+OR+9430786+OR+9430787+OR+9430788%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111796 OR 9430786 OR 9430787 OR 9430788)",
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
    "complete_query": "cites:(111796 OR 9430786 OR 9430787 OR 9430788)",
    "indexed_citing_opinions": 362,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111796,
        "count": 325,
        "count_source": "search"
      },
      {
        "opinion_id": 9430786,
        "count": 48,
        "count_source": "search"
      },
      {
        "opinion_id": 9430787,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430788,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 572,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/connecticut-v-barrett.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MDcyMiZzPTQ2OTM0NDgmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111796+OR+9430786+OR+9430787+OR+9430788%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111796,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111796,
        "cited_id": 444143,
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
    "date_created": "2026-07-05T00:56:06Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:56:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:56:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:01:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:56:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Connecticut v. Barrett

```
<div>
<center><b><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">479 U.S. 523</a></span> (1987)</b></center>
<center><h1>CONNECTICUT<br>
v.<br>
BARRETT</h1></center>
<center>No. 85-899.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 9, 1986</center>
<center>Decided January 27, 1987</center>
CERTIORARI TO THE SUPREME COURT OF CONNECTICUT
<p><span class="star-pagination">*524</span> <i>Julia DiCocco Dewey,</i> Assistant State's Attorney of Connecticut, argued the cause and filed a brief for petitioner.</p>
<p><i>Charles A. Rothfeld</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Fried, Assistant Attorney General Trott,</i> and <i>Deputy Solicitor General Bryson.</i></p>
<p><i>Robert L. Genuario</i> argued the cause for respondent. With him on the brief was <i>John F. Kavanewsky, Jr.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*525</span> CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Respondent William Barrett was convicted after a jury trial of sexual assault, unlawful restraint, and possession of a controlled substance. The Connecticut Supreme Court reversed the convictions. It held that incriminating statements made by Barrett should have been suppressed under our decision in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), because Barrett, though stating his willingness to speak to police, had indicated that he would not make a written statement outside the presence of counsel. <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/" aria-description="Citation for case: State v. Barrett">197 Conn. 50</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/" aria-description="Citation for case: State v. Barrett">495 A. 2d 1044</a></span> (1985). We granted certiorari to consider the federal constitutional issues presented by this holding. <span class="citation multiple-matches"><a href="/c/U.%20S./476/1114/">476 U. S. 1114</a></span> (1986). We reverse.</p>
<p>In the early morning of October 24, 1980, Barrett was transported from New Haven, Connecticut, to Wallingford, where he was a suspect in a sexual assault that had occurred the previous evening. Upon arrival at the Wallingford police station, Officer Peter Cameron advised Barrett of his rights, and Barrett signed and dated an acknowledgment that he had received the warnings required by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Barrett stated that "he would not give the police any written statements but he had no problem in talking about the incident." App. 12A.</p>
<p>Approximately 30 minutes later, Barrett was questioned by Officer Cameron and Officer John Genovese. Before this questioning, he was again advised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights and signed a card acknowledging that he had been read the rights. Respondent stated that he understood his rights, and told the officers that he would not give a written statement unless his attorney was present but had "no problem" talking about the incident. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 21A. Barrett then gave an oral statement admitting his involvement in the sexual assault.</p>
<p>After discovering that a tape recorder used to preserve the statement had malfunctioned, the police conducted a second <span class="star-pagination">*526</span> interview. For the third time, Barrett was advised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights by the Wallingford police, and once again stated that "he was willing to talk about [the incident] verbally but he did not want to put anything in writing until his attorney came." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 44A. He then repeated to the police his confession regarding the previous evening's events.</p>
<p>When the officers discovered that their tape recorder had again failed to record the statement, Officer Cameron reduced to writing his recollection of respondent's statement.</p>
<p>The trial court, after a suppression hearing, held that the confession was admissible. It found that respondent not only indicated that he understood the warnings, but also "offered the statements that he did not need anything explained to him because he understood. So it was not merely a passive acquiescence . . . ." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 70A. Barrett's decision to make no written statement without his attorney "indicate[d] to the Court that he certainly understood from having his rights read to him that . . . he was under no obligation to give any statement." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> The court held that Barrett had voluntarily waived his right to counsel and thus allowed testimony at trial as to the content of Barrett's statement. Barrett took the stand in his own defense and testified that he had understood his rights as they were read to him. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 130A. He was convicted and sentenced to a prison term of 9 to 18 years.</p>
<p>The Connecticut Supreme Court reversed the conviction, holding that respondent had invoked his right to counsel by refusing to make written statements without the presence of his attorney. In the court's view, Barrett's expressed desire for counsel before making a written statement served as an invocation of the right for all purposes:</p>
<blockquote>"The fact that the defendant attached his request for counsel to the making of a written statement does not affect the outcome of . . . our inquiry. No particular form of words has ever been required to trigger an individual's fifth amendment protections; nor have requests for <span class="star-pagination">*527</span> counsel been narrowly construed. The defendant's refusal to give a written statement without his attorney present was a clear request for the assistance of counsel to protect his rights in his dealings with the police. Such a request continues to be constitutionally effective despite the defendant's willingness to make oral statements. We conclude, therefore, that the defendant did invoke his right to counsel under the fifth and fourteenth amendments." <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#57" aria-description="Citation for case: State v. Barrett">197 Conn., at 57</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1049" aria-description="Citation for case: State v. Barrett">495 A. 2d, at 1049</a></span> (citations omitted).</blockquote>
<p>This invocation, the court believed, brought the case within what it called the "bright-line rule for establishing a waiver of this right." <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#58" aria-description="Citation for case: State v. Barrett"><i>Id.,</i> at 58</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1049" aria-description="Citation for case: State v. Barrett">495 A. 2d, at 1049</a></span>. That rule requires a finding that the suspect "(a) initiated further discussions with the police, and (b) knowingly and intelligently waived the right he had invoked." <i>Smith</i> v. <i>Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#95" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 95</a></span> (1984) <i>(per curiam)</i><i>.</i> See also <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona"><i>Edwards, supra,</i> at 485, 486, n. 9</a></span>. Because Barrett had not initiated further discussions with police, the court found his statement improperly admitted.</p>
<p>We think that the Connecticut Supreme Court erred in holding that the United States Constitution required suppression of Barrett's statement. Barrett made clear to police his willingness to talk about the crime for which he was a suspect. The trial court found that this decision was a voluntary waiver of his rights, and there is no evidence that Barrett was "threatened, tricked, or cajoled" into this waiver. <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span>. The Connecticut Supreme Court nevertheless held as a matter of law<sup>[1]</sup> that respondent's <span class="star-pagination">*528</span> limited invocation of his right to counsel prohibited all interrogation absent initiation of further discussion by Barrett. Nothing in our decisions, however, or in the rationale of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> requires authorities to ignore the tenor or sense of a defendant's response to these warnings.</p>
<p>The fundamental purpose of the Court's decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was "to assure that <i>the individual's right to choose</i> between speech and silence remains unfettered throughout the interrogation process." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#469" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 469</a></span> (emphasis added). See also <i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#426" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 426</a></span> (1986) ("<i>Miranda</i> attempted to reconcile [competing] concerns by giving the <i>defendant</i> the power to exert some control over the course of the interrogation") (emphasis in original); <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#308" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 308</a></span> (1985) ("Once warned, the suspect is free to exercise <i>his own volition</i> in deciding whether or not to make a statement to the authorities") (emphasis added). To this end, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> Court adopted prophylactic rules designed to insulate the exercise of Fifth Amendment rights from the government "compulsion, subtle or otherwise," that "operates on the individual to overcome free choice in producing a statement after the privilege has been once invoked." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 474</a></span>. See also <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#98" aria-description="Citation for case: Smith v. Illinois"><i>Smith, supra,</i> at 98</a></span>; <i>Oregon</i> v. <i>Bradshaw,</i> <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983). One such rule requires that, once the accused "states that he wants an attorney, the interrogation must cease until an attorney is present." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 474</a></span>. See also <i>Edwards,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484</a></span>. It remains clear, however, that this prohibition on further questioning  like other aspects of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>  is not itself required by the Fifth Amendment's prohibition on coerced confessions, but is instead justified only by reference to its prophylactic purpose. See <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 654</a></span> (1984). By prohibiting further interrogation after the invocation of these rights, we erect an auxiliary barrier against police coercion.</p>
<p><span class="star-pagination">*529</span> But we know of no constitutional objective that would be served by suppression in this case. It is undisputed that Barrett desired the presence of counsel before making a written statement. Had the police obtained such a statement without meeting the waiver standards of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> it would clearly be inadmissible.<sup>[2]</sup> Barrett's limited requests for counsel, however, were accompanied by affirmative announcements of his willingness to speak with the authorities. The fact that officials took the opportunity provided by Barrett to obtain an oral confession is quite consistent with the Fifth Amendment. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> gives the defendant a right to choose between speech and silence, and Barrett chose to speak.</p>
<p>The Connecticut Supreme Court's decision to the contrary rested on the view that requests for counsel are not to be narrowly construed. <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#57" aria-description="Citation for case: State v. Barrett">197 Conn., at 57</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1049" aria-description="Citation for case: State v. Barrett">495 A. 2d, at 1049</a></span>. In support of this premise, respondent observes that our prior decisions have given broad effect to requests for counsel that were less than all-inclusive. See <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1041" aria-description="Citation for case: Oregon v. Bradshaw"><i>Bradshaw, supra,</i> at 1041-1042</a></span> ("I do want an attorney before it goes very much further"); <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#479" aria-description="Citation for case: Edwards v. Arizona"><i>Edwards, supra,</i> at 479</a></span> ("I want an attorney before making a deal"). We do not denigrate the "settled approach to questions of waiver [that] requires us to give a broad, rather than a narrow, interpretation to a defendant's request for counsel," <i>Michigan</i> v. <i>Jackson,</i> <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#633" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 633</a></span> (1986), when we observe that this approach does little to aid respondent's cause. Interpretation is only required where the defendant's words, understood as ordinary people would understand them, are ambiguous. Here, however, Barrett made clear his intentions, and they were honored by police.<sup>[3]</sup> To conclude that respondent invoked his right to <span class="star-pagination">*530</span> counsel for all purposes requires not a broad interpretation of an ambiguous statement, but a disregard of the ordinary meaning of respondent's statement.</p>
<p>We also reject the contention that the distinction drawn by Barrett between oral and written statements indicates an understanding of the consequences so incomplete that we should deem his limited invocation of the right to counsel effective for all purposes. This suggestion ignores Barrett's testimony  and the finding of the trial court not questioned by the Connecticut Supreme Court  that respondent fully understood the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. These warnings, of course, made clear to Barrett that "[i]f you talk to any police officers, anything you say can and will be used against you in court." App. at 48A. The fact that some might find Barrett's decision illogical<sup>[4]</sup> is irrelevant, for we have never "embraced the theory that a defendant's ignorance of the full consequences of his decisions vitiates their voluntariness." <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 316</a></span>; <i>Colorado</i> v. <i>Spring, post,</i> p. 564.</p>
<p>For the reasons stated, the judgment of the Connecticut Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BRENNAN, concurring in the judgment.</p>
<p>I concur in the judgment that the Constitution does not require the suppression of Barrett's statements to the police, but for reasons different from those set forth in the opinion of the Court. Barrett's contemporaneous waiver of his right to silence and limited invocation of his right to counsel (for the <span class="star-pagination">*531</span> purpose of making a written statement) suggested that he did not understand that anything he <i>said</i> could be used against him. However, the State eliminated this apparent ambiguity when it demonstrated that Barrett's waiver of his right to silence was voluntary, knowing, and intelligent. Barrett testified at trial that he understood his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, <i>i. e.,</i> he knew that he need not talk to the police without a lawyer present and that anything he said could be used against him. Under these circumstances, the waiver of the right to silence and the limited invocation of the right to counsel were valid.</p>
<p></p>
<h2>I</h2>
<p>In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the Court held that custodial interrogation is inherently coercive and that a defendant must receive detailed warnings that he or she has the rights to remain silent and to receive assistance of counsel before and during questioning. A statement obtained from a defendant during custodial interrogation is admissible only if the State carries its "heavy burden" of establishing that a defendant has executed a valid waiver of the privilege against self-incrimination and the right to counsel. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 475</a></span>. To do so, the State must demonstrate "an intentional relinquishment or abandonment of a known right or privilege." <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span> (1938); see <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 475-479</a></span>. In making this determination, courts must examine "the particular facts and circumstances surrounding that case, including the background, experience, and conduct of the accused." <i>Johnson</i> v. <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst"><i>Zerbst, supra,</i> at 464</a></span>.</p>
<p>The language and tenor of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion suggested that the Court would require that a waiver of the rights at stake be "specifically made." See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#470" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 470</a></span>. While the Court retreated from that position in <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 373</a></span> (1979), I continue to believe that the Court should require the police to obtain an " `affirmative waiver' " of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights before proceeding with interrogation. <span class="star-pagination">*532</span> See <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">id.,</a></span></i> at 377 (quoting <i>Carnley</i> v. <i>Cochran,</i> <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#516" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506, 516</a></span> (1962)).</p>
<p>In this case, Barrett affirmatively waived his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Unlike the defendant in <i><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span>,</i> Barrett orally expressed his willingness to talk with the police <i>and</i> willingly signed a form indicating that he understood his rights. The police obtained an explicit oral waiver of the right to silence. Furthermore, the officer who administered the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to Barrett testified that the latter understood his rights "[c]ompletely": "I asked [Barrett] several times during my administration of those rights, if, in fact, he understood them; if there were points he wanted me to clarify, and he indicated to me, no, he understood everything fairly well." Tr. 452. At trial, one issue was whether Barrett voluntarily, knowingly, and intelligently waived his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and Barrett himself testified that he understood his rights as they were read to him. <i>Id.,</i> at 879-880.<sup>[1]</sup></p>
<p>Had the State been without Barrett's testimony at trial, where he was represented by counsel, I could not reach this conclusion. Barrett's statement to police  that he would talk to them, but allow nothing in writing without counsel  created doubt about whether he actually understood that anything he <i>said</i> could be used against him. In other words, the statement is not, on its face, a knowing and intelligent waiver of the right to silence.<sup>[2]</sup> As a general matter, I believe <span class="star-pagination">*533</span> that this odd juxtaposition (a willingness to talk and an unwillingness to have anything preserved) militates against finding a knowing or intelligent waiver of the right to silence. See <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#378" aria-description="Citation for case: North Carolina v. Butler"><i>Butler, supra,</i> at 378</a></span> ("[T]here is no reason to believe that [the defendant's] oral statements, which followed a refusal to sign a written waiver form, were intended to signify relinquishment of his rights").<sup>[3]</sup> But Barrett's testimony revealed that he understood that he had rights to remain silent and to have an attorney present, and that anything he said could be used against him; nevertheless he chose to speak.</p>
<p>In sum, the State has carried its "heavy burden" of demonstrating waiver. It has shown that Barrett received the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, that he had the capacity to understand them<sup>[4]</sup> and <i>in fact</i> understood them, and that he expressly <span class="star-pagination">*534</span> waived his right to silence, saying that he "had no problem in talking about the incident." Tr. 452; see also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 461-462, 490-491, 674</a></span>. In my view, each of these findings was essential to the conclusion that a voluntary, knowing, and intelligent waiver of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights occurred.</p>
<p></p>
<h2>II</h2>
<p>Barrett argues that his refusal to make a written statement without an attorney present constituted an invocation of the right to counsel for all purposes and that any further interrogation after this mention of his desire for an attorney was impermissible under <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). It is settled that any plain reference, however glancing, to a need or a desire for representation must result in the cessation of questioning. See <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444-445</a></span> (questioning must cease when the accused "indicates in any manner and at any stage of the process that he wishes to consult with an attorney before speaking"); <i>Smith</i> v. <i>Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91</a></span> (1984) <i>(per curiam)</i><i>.</i></p>
<p>I believe that a partial invocation of the right to counsel, without more, invariably will be ambiguous. It gives rise to doubts about the defendant's precise wishes regarding representation and about his or her understanding of the nature and scope of the right to counsel. Thus, the police may not infer from a partial invocation of the right to counsel <i>alone</i> that the defendant has waived any of his or her rights not specifically invoked.</p>
<p>However, circumstances may clarify an otherwise ambiguous situation. If the partial invocation is accompanied by an explicit waiver of the right to silence that is voluntary, knowing, and intelligent, it may lose its ambiguity.<sup>[5]</sup> It may become <span class="star-pagination">*535</span> clear that the portion of the right to counsel that was not invoked was in fact waived, when, for example, a knowing and intelligent waiver of the right to silence necessarily includes a waiver of the right to have counsel present at questioning. This is such a case.<sup>[6]</sup> Here Barrett's limited invocation was not ambiguous: It was accompanied by an express waiver of his right to silence, the validity of which was plainly established by his subsequent trial testimony. The accompaniment of Barrett's reference to his limited desire for counsel with an explicit waiver of his right to silence rendered permissible the authorities' use of his statements.<sup>[7]</sup></p>
<p>For these reasons, I concur in the judgment of the Court.</p>
<p><span class="star-pagination">*536</span> JUSTICE STEVENS, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>The Court's disposition of this case raises two troublesome questions.</p>
<p>First, why did the Court decide to exercise its discretion to grant review in this case? The facts of the case are surely unique. They do not give rise to any issue of general or recurring significance. There is no conflict among the state or federal courts on how the narrow question presented should be resolved. It is merely a case in which one State Supreme Court arguably granted more protection to a citizen accused of crime than the Federal Constitution requires.<sup>[1]</sup> The State "asks us to rule that the state court interpreted federal rights too broadly and `overprotected' the citizen." <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1068" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1068</a></span> (1983) (STEVENS, J., dissenting). If this is a sufficient reason for adding a case to our already overcrowded docket, we will need, not one, but several newly fashioned "intercircuit tribunals" to keep abreast of our work.</p>
<p>Second, why was respondent's request for the assistance of counsel any less ambiguous than the request in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981)? In that case, the defendant said that he wanted an attorney " `before making a deal.' " <span class="star-pagination">*537</span> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#479" aria-description="Citation for case: Edwards v. Arizona"><i>Id.,</i> at 479</a></span>. He also said he would talk to the police " `but I don't want it on tape.' " <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span></i> The police interrogation complied with the everyday meaning of both of those conditions; it occurred before Edwards made any "deal"  indeed, he never made a deal  and no tape recording of the session was made. The Court nevertheless found the interrogation objectionable. In this case, respondent requested an attorney before signing a written statement. Why the police's compliance with the literal terms of that request makes the request  as opposed to the subsequent waiver<sup>[2]</sup>  any less of a request for the assistance of counsel than Edwards' is not adequately explained in the Court's opinion. In all events, the Court does not purport to change the governing rule of law that judges must "give a broad, rather than a narrow, interpretation to a defendant's request for counsel." <i>Michigan</i> v. <i>Jackson,</i> <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#633" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 633</a></span> (1986).</p>
<p>I would dismiss the writ of certiorari as improvidently granted.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the State of Alaska et al. by <i>David Crump</i> and by the Attorneys General for their respective States as follows: <i>Harold M. Brown</i> of Alaska, <i>Robert K. Corbin</i> of Arizona, <i>John Steven Clark</i> of Arkansas, <i>John K. Van de Kamp</i> of California, <i>Duane Woodard</i> of Colorado, <i>James T. Jones</i> of Idaho, <i>Linley E. Pearson</i> of Indiana, <i>David L. Armstrong</i> of Kentucky, <i>William J. Guste, Jr.,</i> of Louisiana, <i>Frank J. Kelley</i> of Michigan, <i>Hubert H. Humphrey III</i> of Minnesota, <i>Edwin L. Pittman</i> of Mississippi, <i>William L. Webster</i> of Missouri, <i>Lacy H. Thornburg</i> of North Carolina, <i>LeRoy S. Zimmerman</i> of Pennsylvania, <i>T. Travis Medlock</i> of South Carolina, <i>Mark V. Meierhenry</i> of South Dakota, <i>Mary Sue Terry</i> of Virginia, <i>Kenneth O. Eikenberry</i> of Washington, and <i>Bronson C. La Follette</i> of Wisconsin; and for the National District Attorneys Association by <i>Robert S. Marsel, Jack E. Yelverton,</i> and <i>James P. Manak.</i></p>
<p>[1]  The Connecticut Supreme Court noted in its opinion that the trial court "impliedly found that the defendant had requested counsel." <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#56" aria-description="Citation for case: State v. Barrett">197 Conn. 50, 56</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1048" aria-description="Citation for case: State v. Barrett">495 A. 2d 1044, 1048</a></span> (1985). This statement does not suggest, however, that the request for counsel was in fact all-inclusive, and the Supreme Court expressly noted the trial court's finding that defendant had refused to give a written statement without his attorney present. <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#56" aria-description="Citation for case: State v. Barrett"><i>Id.,</i> at 56, n. 6</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1048" aria-description="Citation for case: State v. Barrett">495 A. 2d, at 1048, n. 6</a></span>. The holding that Barrett had invoked his right to counsel, then, rests on a legal conclusion about the effect of his limited invocation rather than on a factual finding.</p>
<p>[2]  Because the attempts to record Barrett's statements were unsuccessful, we have no occasion to consider whether the result would be different if police had taped the statements and used the recording against Barrett.</p>
<p>[3]  Since we reject the claim that Barrett's statements represent an ambiguous or equivocal response to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, there is no need for us to address the question left open in <i>Smith</i> v. <i>Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#96" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 96, n. 3</a></span> (1984) <i>(per curiam)</i><i>.</i></p>
<p>[4]  We do not suggest that the distinction drawn by Barrett is in fact illogical, for there may be several strategic reasons why a defendant willing to speak to the police would still refuse to write out his answers to questions, or to sign a transcript of his answers prepared by the police, a statement that may be used against him.</p>
<p>[1]  The trial judge denied Barrett's motion to suppress the statements made following administration of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, holding:
</p>
<p>"[T]he Court concludes from the evidence it heard that [Barrett] indicated he understood perfectly what was being read to him. Not only did he indicate that he understood, he offered the statements that he did not need anything explained to him because he understood. So it was not merely a passive acquiescence and his agreement that he understood, he did go on to explain that he did not need anything explained to him because he perfectly understood." App. 70A.</p>
<p>[2]  The Court states that " `a defendant's ignorance of the full consequences of his decisions' " would not " `vitiat[e] their voluntariness.' " <i>Ante,</i> at 530 (quoting <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 316</a></span> (1985)). I do not accept that a defendant could voluntarily, knowingly, or intelligently waive a right that he or she does not understand to exist. Cf. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#277" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 277</a></span> (1973) (BRENNAN, J., dissenting) ("The Court holds today that an individual can effectively waive this right [to be secure against an unreasonable search] even though he is totally ignorant of the fact that, in the absence of his consent, such invasions of privacy would be constitutionally prohibited. It wholly escapes me how our citizens can meaningfully be said to have waived something as precious as a constitutional guarantee without ever being aware of its existence"); <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">ibid.</a></span></i> (MARSHALL, J., dissenting) ("I would have thought that the capacity to choose necessarily depends upon knowledge that there is a choice to be made. But today the Court reaches the curious result that one can choose to relinquish a constitutional right  the right to be free of unreasonable searches  without knowing that he has the alternative of refusing to accede to a police request to search").</p>
<p>[3]  See also 1 W. LaFave &amp; J. Israel, Criminal Procedure § 6.9(f), pp. 534-535 (1984 ed.) ("[T]he <i><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span></i> facts certainly suggest that the defendant misperceived the effect of a waiver which was oral rather than written. Under such circumstances, there is much to be said for the view that the police are under an obligation to clear up misunderstandings of this nature which are apparent to any reasonable observer. Short of this, it certainly makes sense to conclude that the defendant's conduct should significantly increase the prosecution's burden to overcome the presumption against waiver of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights").</p>
<p>[4]  It is undisputed that the defendant here, unlike the defendant in <i><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span>,</i> had the capacity to understand his rights: the police ascertained that Barrett had a 12th-grade education, Tr. 458, while in <i><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span></i> there was a dispute over whether the defendant could read. <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#378" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 378</a></span> (1979).</p>
<p>[5]  In order for a valid waiver and partial invocation of the right to counsel to occur, the accused must effect them contemporaneously. In <i>Smith</i> v. <i>Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91</a></span> (1984) <i>(per curiam)</i><i>,</i> the Court considered a defendant's plain request for counsel that had been closely followed by statements rendering equivocal or ambiguous his first request. The State Supreme Court determined that the defendant's statements, considered as a totality, were ambiguous and therefore did not invoke his right to counsel. We held that "an accused's <i>postrequest</i> responses to further interrogation may not be used to cast retrospective doubt on the clarity of the initial request itself." <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#100" aria-description="Citation for case: Smith v. Illinois"><i>Id.,</i> at 100</a></span>. Thus, if the initial request for counsel is clear, as it was here, the police may not create ambiguity in a defendant's desire by continuing to question him or her about it.</p>
<p>[6]  See also <i>United States</i> v. <i>Jardina,</i> <span class="citation" data-id="444143"><a href="/opinion/444143/united-states-v-charles-c-jardina/#949" aria-description="Citation for case: United States v. Charles C. Jardina">747 F. 2d 945, 949</a></span> (CA5 1984) (The defendant stated "without the slightest ambiguity that he would then and there answer some questions but not others" and "clearly indicated that he wished his attorney to work out a cooperative deal with the government in the future." The Court of Appeals found that these combined statements "did not invoke any <i>present</i> right to counsel").</p>
<p>[7]  It is undisputed that "[h]ad the police obtained [a written] statement without meeting the waiver standards of <i>Edwards</i> [v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981)], it would clearly be inadmissible." <i>Ante,</i> at 529. Barrett's invocation of his rights demonstrates that he opposed any immediate preservation of statements made without counsel. If the attempt to tape Barrett's statements had succeeded, the recording would have been inadmissible.
</p>
<p>In addition, the police attempted to persuade Barrett to waive the right he had asserted not to make a written statement without the assistance of counsel, not once, but twice, absent any indication from Barrett that he had changed his mind on this point. Tr. 689 ("Sergeant Genovese at the first [questioning] and Lieutenant Howard at the second inquired whether or not he had changed his mind [about reducing his statements to writing]"); see also <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#521" aria-description="Citation for case: Edwards v. Arizona"><i>id.,</i> at 521</a></span>. In <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span>, we held that once an accused invokes the right to counsel, he or she is not subject to further custodial interrogation "until counsel has been made available to him [or her], unless the accused . . . initiates further communication, exchanges, or conversations with the police." Here the police failed to respect Barrett's limited assertion of his right to counsel. Had a written statement been obtained as a result of these persistent efforts to change Barrett's mind, it would have been inadmissible.</p>
<p>[1]  "The central contention of the Petitioner in this action is that the Connecticut Supreme Court unduly expanded the protections accorded criminal defendants under the Fifth Amendment to the United States [C]onstitution when it determined that this defendant involuntarily waived his right to assistance of counsel at his interrogation. This result was possible only through use of a prophylactic rule which ignored the circumstances of this case." Pet. for Cert. 5.</p>
<p>[2]  In this case, the Connecticut Supreme Court interpreted the trial court's ruling as embodying a factual finding that respondent had requested the assistance of counsel but <i>thereafter</i> waived his right to counsel. It agreed with that factual determination but held that the subsequent waiver was ineffective as a matter of law. <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#60" aria-description="Citation for case: State v. Barrett">197 Conn. 50, 60</a></span>, <span class="citation" data-id="7839349"><a href="/opinion/7892198/state-v-barrett/#1050" aria-description="Citation for case: State v. Barrett">495 A. 2d 1044, 1050</a></span> (1985).</p>

</div>
```

---
