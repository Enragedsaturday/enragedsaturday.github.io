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

## GROUP: content/cases/Caniglia v. Strom.md  (`case`, 5 assertions)

### content_page

```
---
title: "Caniglia v. Strom"
type: case
citation: "593 U.S. 194 (2021)"
parallel_cite: "209 L. Ed. 2d 604; 141 S. Ct. 1596"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2021
date_decided: 2021-05-17
docket: 20-157
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2021-05-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Caniglia v. Strom
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4883694/caniglia-v-strom/"
  cluster_id: 4883694
  opinion_id: 4687473
  identity_checked: true
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Progeny / Refinement"
related: ["[[Cady v. Dombrowski]]", "[[Brigham City v. Stuart]]", "[[Kentucky v. King]]"]
aliases: []
tags: ["case", "fourth-amendment", "community-caretaking", "home", "warrantless-entry"]
holding: "There is NO freestanding 'community caretaking' exception authorizing warrantless entry into the HOME. Cady's caretaking rationale was…"
lake:
  record_id: Caniglia v. Strom
  status: verified
  projected_at: 2026-07-06
---

# Caniglia v. Strom

*593 U.S. 194 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a marital argument in which Caniglia melodramatically suggested his wife shoot him, she spent the night elsewhere and, unable to reach him the next day, asked police for a welfare check. Officers, concerned he was suicidal, persuaded him to go for a psychiatric evaluation and then — without a warrant or his consent — entered his home and seized his firearms. The First Circuit upheld the entry under a freestanding "community caretaking" exception drawn from *[[Cady v. Dombrowski]]*.

## Issue
Whether the community-caretaking rationale of *[[Cady v. Dombrowski]]* creates a standalone exception authorizing warrantless entry into and seizures within the home.

## Rule
There is no such freestanding exception: "The First Circuit's 'community caretaking' rule, however, goes beyond anything this Court has recognized." — *Caniglia v. Strom*, 593 U.S. 194 (2021) (slip op., at 3). ^pin-op3

*[[Cady v. Dombrowski|Cady]]* does not support extending caretaking to the home: "Neither the holding nor logic of *Cady* justified that approach. True, *Cady* also involved a warrantless search for a firearm. But the location of that search was an impounded vehicle — not a home — 'a constitutional difference' that the opinion repeatedly stressed." — *Id.* (slip op., at 4). ^pin-op4

## Application
The officers entered Caniglia's home and seized his firearms with no warrant, no consent, and — as the case came up — no recognized [[Exigent Circumstances and Hot Pursuit|exigency]], relying solely on a freestanding caretaking theory. Because *[[Cady v. Dombrowski|Cady]]* concerned an impounded vehicle rather than a home, its caretaking rationale did not authorize this warrantless entry into Caniglia's house.

## Conclusion
There is no standalone community-caretaking exception for the home; the judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Caniglia* **cabins** [[Cady v. Dombrowski]] to the vehicle context and leaves intact the home-entry exceptions of [[Emergency Aid|emergency aid]] and [[Exigent Circumstances and Hot Pursuit|exigency]] ([[Brigham City v. Stuart]]; [[Kentucky v. King]]).

## Appears on
- [[Emergency Aid]] — *Key — Progeny / Refinement*

## Sources
- *Caniglia v. Strom*, 593 U.S. 194 (2021) — https://www.courtlistener.com/opinion/4883694/caniglia-v-strom/ — pinpoints: slip op., at 3, 4 (CL carries the slip opinion; cluster 4883694 → opinion 4687473).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d3b041c2ee6c7ad7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "593 U.S. 194 (2021)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "209 L. Ed. 2d 604; 141 S. Ct. 1596", "title": "Caniglia v. Strom", "year": "2021"}}
{"assertion_id": "c541ee415f725f8f", "dimension": "support", "kind": "home_role", "locator": {"home": "Emergency Aid"}, "payload": {"home": "Emergency Aid", "role": "Key — Progeny / Refinement", "title": "Caniglia v. Strom"}}
{"assertion_id": "cb7097aae69714e3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "There is NO freestanding 'community caretaking' exception authorizing warrantless entry into the HOME. Cady's caretaking rationale was…", "title": "Caniglia v. Strom"}}
{"assertion_id": "7963b8fb79d0c612", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2021-05-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Caniglia v. Strom", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Caniglia v. Strom", "varies_by_point": "false"}}
{"assertion_id": "d314c575416f21d5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Caniglia v. Strom"}}
```

### lake record — Caniglia v. Strom

```json
{
  "schema_version": "s2.v1",
  "record_id": "Caniglia v. Strom",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Caniglia v. Strom",
    "case_name_short": "Caniglia",
    "case_name_full": "",
    "input_case_name": "Caniglia v. Strom",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2021-05-17",
    "year": 2021,
    "docket": "20-157",
    "cluster_id": 4883694,
    "lead_opinion_id": 4687473,
    "sibling_ids": [
      4687473
    ],
    "absolute_url": "/opinion/4883694/caniglia-v-strom/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "593 U.S. 194",
      "volume": "593",
      "reporter": "U.S.",
      "page": "194",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "209 L. Ed. 2d 604",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 1596",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "1596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "593 U.S. 194",
        "volume": "593",
        "reporter": "U.S.",
        "page": "194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 604",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 1596",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "1596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "593 U.S. 194",
    "official_selection": {
      "court_class": "scotus",
      "selected": "593 U.S. 194",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op3",
      "page": null,
      "quote": "exception drawn from *Cady v. Dombrowski*. ## Issue Whether the community-caretaking rationale of *Cady v. Dombrowski* creates a standalone exception authorizing warrantless entry into and seizures within the home. ## Rule There is no such freestanding exception:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op4",
      "page": null,
      "quote": "Neither the holding nor logic of *Cady* justified that approach. True, *Cady* also involved a warrantless search for a firearm. But the location of that search was an impounded vehicle \u2014 not a home \u2014 'a constitutional difference' that the opinion repeatedly stressed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-05-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Caniglia v. Strom",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Torcivia v. Suffolk County, New York",
          "cluster_id": 5295971,
          "cite": [
            "17 F.4th 342"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Williams v. Brian Maurer",
          "cluster_id": 4958226,
          "cite": [
            "9 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teresa Graham v. Shannon Barnette",
          "cluster_id": 4900401,
          "cite": [
            "5 F.4th 872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Aljohani",
          "cluster_id": 6478244,
          "cite": [
            "463 Ill. Dec. 764",
            "211 N.E.3d 325",
            "2022 IL 127037"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
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
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Rogers",
          "cluster_id": 9492473,
          "cite": [
            "97 F.4th 1038"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Bruce Akers",
          "cluster_id": 5093384,
          "cite": [
            "259 A.3d 127",
            "2021 ME 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Russell Taylor",
          "cluster_id": 9386597,
          "cite": [
            "63 F.4th 637"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Sanders",
          "cluster_id": 4900399,
          "cite": [
            "4 F.4th 672"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hagestedt",
          "cluster_id": 10328364,
          "cite": [
            "2025 IL 130286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guerrero",
          "cluster_id": 5303613,
          "cite": [
            "19 F.4th 547"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jaron Howard Morgan",
          "cluster_id": 9409483,
          "cite": [
            "71 F.4th 540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Clemons v. John Couch",
          "cluster_id": 4898166,
          "cite": [
            "3 F.4th 897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bakutis v. Dean",
          "cluster_id": 10339329,
          "cite": [
            "129 F.4th 299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. W. Case",
          "cluster_id": 10032858,
          "cite": [
            "553 P.3d 985",
            "417 Mont. 354",
            "2024 MT 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Edgin, M.",
          "cluster_id": 10316123,
          "cite": [
            "273 A.3d 573",
            "2022 Pa. Super. 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Giambro",
          "cluster_id": 10314463,
          "cite": [
            "126 F.4th 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Grassrope",
          "cluster_id": 9508066,
          "cite": [
            "970 N.W.2d 558",
            "2022 S.D. 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tidwell v. State",
          "cluster_id": 10367697,
          "cite": [
            "863 S.E.2d 127",
            "312 Ga. 459"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tran",
          "cluster_id": 9479664,
          "cite": [
            "545 P.3d 248",
            "2024 UT 7"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Antoine Maxwell",
          "cluster_id": 9455466,
          "cite": [
            "89 F.4th 671"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alexander Treisman",
          "cluster_id": 9409277,
          "cite": [
            "71 F.4th 225"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Delaware v. McKenzie S. Beasley",
          "cluster_id": 10876355,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4687473) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
      },
      "lane2_top_cited": {
        "query": "cites:(4687473)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9MTAwODg2MzYmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284687473%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4687473)",
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
    "complete_query": "cites:(4687473)",
    "indexed_citing_opinions": 62,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4687473,
        "count": 62,
        "count_source": "search"
      }
    ],
    "citation_count": 154,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/caniglia-v-strom.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNjU3NSZzPTk0MTUwODUmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%284687473%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4687473,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 110067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 858288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 2801435,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 4516423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9413217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9422640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9423434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9424643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9425411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9426490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9427218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9427279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9429413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9431979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9432531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9441559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9842006,
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
    "date_created": "2026-07-04T23:28:44Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:29:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:29:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:32:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:29:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Caniglia v. Strom

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

                      CANIGLIA v. STROM ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE FIRST CIRCUIT

      No. 20–157.      Argued March 24, 2021—Decided May 17, 2021
During an argument with his wife, petitioner Edward Caniglia placed a
 handgun on the dining room table and asked his wife to “shoot [him]
 and get it over with.” His wife instead left the home and spent the
 night at a hotel. The next morning, she was unable to reach her hus-
 band by phone, so she called the police to request a welfare check. The
 responding officers accompanied Caniglia’s wife to the home, where
 they encountered Caniglia on the porch. The officers called an ambu-
 lance based on the belief that Caniglia posed a risk to himself or others.
 Caniglia agreed to go to the hospital for a psychiatric evaluation on the
 condition that the officers not confiscate his firearms. But once
 Caniglia left, the officers located and seized his weapons. Caniglia
 sued, claiming that the officers had entered his home and seized him
 and his firearms without a warrant in violation of the Fourth Amend-
 ment. The District Court granted summary judgment to the officers.
 The First Circuit affirmed, extrapolating from the Court’s decision in
 Cady v. Dombrowski, 413 U. S. 433, a theory that the officers’ removal
 of Caniglia and his firearms from his home was justified by a “commu-
 nity caretaking exception” to the warrant requirement.
Held: Neither the holding nor logic of Cady justifies such warrantless
 searches and seizures in the home. Cady held that a warrantless
 search of an impounded vehicle for an unsecured firearm did not vio-
 late the Fourth Amendment. In reaching this conclusion, the Court
 noted that the officers who patrol the “public highways” are often
 called to discharge noncriminal “community caretaking functions,”
 such as responding to disabled vehicles or investigating accidents. 413
 U. S., at 441. But searches of vehicles and homes are constitutionally
 different, as the Cady opinion repeatedly stressed. Id., at 439, 440–
 442. The very core of the Fourth Amendment’s guarantee is the right
2                          CANIGLIA v. STROM

                                  Syllabus

    of a person to retreat into his or her home and “there be free from un-
    reasonable governmental intrusion.” Florida v. Jardines, 569 U. S. 1,
    6. A recognition of the existence of “community caretaking” tasks, like
    rendering aid to motorists in disabled vehicles, is not an open-ended
    license to perform them anywhere. Pp. 3–4.
953 F. 3d 112, vacated and remanded.

  THOMAS, J., delivered the opinion for a unanimous Court. ROBERTS,
C. J., filed a concurring opinion, in which BREYER, J., joined. ALITO, J.,
and KAVANAUGH, J., filed concurring opinions.
                        Cite as: 593 U. S. ____ (2021)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 20–157
                                    _________________


          EDWARD A. CANIGLIA, PETITIONER v.
              ROBERT F. STROM, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
             APPEALS FOR THE FIRST CIRCUIT
                                  [May 17, 2021]

  JUSTICE THOMAS delivered the opinion of the Court.
  Decades ago, this Court held that a warrantless search of
an impounded vehicle for an unsecured firearm did not vio-
late the Fourth Amendment. Cady v. Dombrowski, 413
U. S. 433 (1973). In reaching this conclusion, the Court ob-
served that police officers who patrol the “public highways”
are often called to discharge noncriminal “community care-
taking functions,” such as responding to disabled vehicles
or investigating accidents. Id., at 441. The question today
is whether Cady’s acknowledgment of these “caretaking”
duties creates a standalone doctrine that justifies warrant-
less searches and seizures in the home. It does not.
                               I
  During an argument with his wife at their Rhode Island
home, Edward Caniglia (petitioner) retrieved a handgun
from the bedroom, put it on the dining room table, and
asked his wife to “shoot [him] now and get it over with.” She
declined, and instead left to spend the night at a hotel. The
next morning, when petitioner’s wife discovered that she
could not reach him by telephone, she called the police (re-
spondents) to request a welfare check.
2                    CANIGLIA v. STROM

                      Opinion of the Court

   Respondents accompanied petitioner’s wife to the home,
where they encountered petitioner on the porch. Petitioner
spoke with respondents and confirmed his wife’s account of
the argument, but denied that he was suicidal. Respond-
ents, however, thought that petitioner posed a risk to him-
self or others. They called an ambulance, and petitioner
agreed to go to the hospital for a psychiatric evaluation—
but only after respondents allegedly promised not to confis-
cate his firearms. Once the ambulance had taken petitioner
away, however, respondents seized the weapons. Guided
by petitioner’s wife—whom they allegedly misinformed
about his wishes—respondents entered the home and took
two handguns.
   Petitioner sued, claiming that respondents violated the
Fourth Amendment when they entered his home and seized
him and his firearms without a warrant. The District Court
granted summary judgment to respondents, and the First
Circuit affirmed solely on the ground that the decision to
remove petitioner and his firearms from the premises fell
within a “community caretaking exception” to the warrant
requirement. 953 F. 3d 112, 121–123, 131 and nn. 5, 9
(2020). Citing this Court’s statement in Cady that police
officers often have noncriminal reasons to interact with mo-
torists on “public highways,” 413 U. S., at 441, the First Cir-
cuit extrapolated a freestanding community-caretaking ex-
ception that applies to both cars and homes. 953 F. 3d, at
124 (“Threats to individual and community safety are not
confined to the highways”). Accordingly, the First Circuit
saw no need to consider whether anyone had consented to
respondents’ actions; whether these actions were justified
by “exigent circumstances”; or whether any state law per-
mitted this kind of mental-health intervention. Id., at 122–
123. All that mattered was that respondents’ efforts to pro-
tect petitioner and those around him were “distinct from
‘the normal work of criminal investigation,’ ” fell “within the
realm of reason,” and generally tracked what the court
                   Cite as: 593 U. S. ____ (2021)               3

                       Opinion of the Court

viewed to be “sound police procedure.” Id., at 123–128, 132–
133. We granted certiorari. 592 U. S. ___ (2020).
                                 II
    The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures.” The “ ‘very
core’ ” of this guarantee is “ ‘the right of a man to retreat into
his own home and there be free from unreasonable govern-
mental intrusion.’ ” Florida v. Jardines, 569 U. S. 1, 6
(2013).
    To be sure, the Fourth Amendment does not prohibit all
unwelcome intrusions “on private property,” ibid.—only
“unreasonable” ones. We have thus recognized a few per-
missible invasions of the home and its curtilage. Perhaps
most familiar, for example, are searches and seizures pur-
suant to a valid warrant. See Collins v. Virginia, 584 U. S.
___, ___–___ (2018) (slip op., at 5–6). We have also held that
law enforcement officers may enter private property with-
out a warrant when certain exigent circumstances exist, in-
cluding the need to “ ‘render emergency assistance to an in-
jured occupant or to protect an occupant from imminent
injury.’ ” Kentucky v. King, 563 U. S. 452, 460, 470 (2011);
see also Brigham City v. Stuart, 547 U. S. 398, 403–404
(2006) (listing other examples of exigent circumstances).
And, of course, officers may generally take actions that
“ ‘any private citizen might do’ ” without fear of liability.
E.g., Jardines, 569 U. S., at 8 (approaching a home and
knocking on the front door).
    The First Circuit’s “community caretaking” rule, how-
ever, goes beyond anything this Court has recognized. The
decision below assumed that respondents lacked a warrant
or consent, and it expressly disclaimed the possibility that
they were reacting to a crime. The court also declined to
consider whether any recognized exigent circumstances
were present because respondents had forfeited the point.
4                    CANIGLIA v. STROM

                      Opinion of the Court

Nor did it find that respondents’ actions were akin to what
a private citizen might have had authority to do if peti-
tioner’s wife had approached a neighbor for assistance in-
stead of the police.
   Neither the holding nor logic of Cady justified that ap-
proach. True, Cady also involved a warrantless search for
a firearm. But the location of that search was an im-
pounded vehicle—not a home—“ ‘a constitutional differ-
ence’ ” that the opinion repeatedly stressed. 413 U. S., at
439; see also id., at 440–442. In fact, Cady expressly con-
trasted its treatment of a vehicle already under police con-
trol with a search of a car “parked adjacent to the dwelling
place of the owner.” Id., at 446–448 (citing Coolidge v. New
Hampshire, 403 U. S. 443 (1971)).
   Cady’s unmistakable distinction between vehicles and
homes also places into proper context its reference to “com-
munity caretaking.” This quote comes from a portion of the
opinion explaining that the “frequency with which . . . vehi-
cle[s] can become disabled or involved in . . . accident[s] on
public highways” often requires police to perform noncrim-
inal “community caretaking functions,” such as providing
aid to motorists. 413 U. S., at 441. But, this recognition
that police officers perform many civic tasks in modern so-
ciety was just that—a recognition that these tasks exist,
and not an open-ended license to perform them anywhere.
                         *    *     *
    What is reasonable for vehicles is different from what is
reasonable for homes. Cady acknowledged as much, and
this Court has repeatedly “declined to expand the scope of
. . . exceptions to the warrant requirement to permit war-
rantless entry into the home.” Collins, 584 U. S., at ___ (slip
op., at 8). We thus vacate the judgment below and remand
for further proceedings consistent with this opinion.

                                              It is so ordered.
                 Cite as: 593 U. S. ____ (2021)            1

                   ROBERTS, C. J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 20–157
                         _________________


        EDWARD A. CANIGLIA, PETITIONER v.
            ROBERT F. STROM, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
             APPEALS FOR THE FIRST CIRCUIT
                        [May 17, 2021]

   CHIEF JUSTICE ROBERTS, with whom JUSTICE BREYER
joins, concurring.
   Fifteen years ago, this Court unanimously recognized
that “[t]he role of a peace officer includes preventing vio-
lence and restoring order, not simply rendering first aid to
casualties.” Brigham City v. Stuart, 547 U. S. 398, 406
(2006). A warrant to enter a home is not required, we ex-
plained, when there is a “need to assist persons who are se-
riously injured or threatened with such injury.” Id., at 403;
see also Michigan v. Fisher, 558 U. S. 45, 49 (2009) (per cu-
riam) (warrantless entry justified where “there was an ob-
jectively reasonable basis for believing that medical assis-
tance was needed, or persons were in danger” (internal
quotation marks omitted)). Nothing in today’s opinion is to
the contrary, and I join it on that basis.
                  Cite as: 593 U. S. ____ (2021)            1

                      ALITO, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 20–157
                          _________________


        EDWARD A. CANIGLIA, PETITIONER v.
            ROBERT F. STROM, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
             APPEALS FOR THE FIRST CIRCUIT
                         [May 17, 2021]

   JUSTICE ALITO, concurring.
   I join the opinion of the Court but write separately to ex-
plain my understanding of the Court’s holding and to high-
light some important questions that the Court does not de-
cide.
   1. The Court holds—and I entirely agree—that there is
no special Fourth Amendment rule for a broad category of
cases involving “community caretaking.” As I understand
the term, it describes the many police tasks that go beyond
criminal law enforcement. These tasks vary widely, and
there is no clear limit on how far they might extend in the
future. The category potentially includes any non-law-en-
forcement work that a community chooses to assign, and
because of the breadth of activities that may be described
as community caretaking, we should not assume that the
Fourth Amendment’s command of reasonableness applies
in the same way to everything that might be viewed as fall-
ing into this broad category.
   The Court’s decision in Cady v. Dombrowski, 413 U. S.
433 (1973), did not recognize any such “freestanding”
Fourth Amendment category. See ante, at 2, 4. The opinion
merely used the phrase “community caretaking” in passing.
413 U. S., at 441.
   2. While there is no overarching “community caretaking”
doctrine, it does not follow that all searches and seizures
2                        CANIGLIA v. STROM

                          ALITO, J., concurring

conducted for non-law-enforcement purposes must be ana-
lyzed under precisely the same Fourth Amendment rules
developed in criminal cases. Those rules may or may not be
appropriate for use in various non-criminal-law-enforce-
ment contexts. We do not decide that issue today.
   3. This case falls within one important category of cases
that could be viewed as involving community caretaking:
conducting a search or seizure for the purpose of preventing
a person from committing suicide. Assuming that peti-
tioner did not voluntarily consent to go with the officers for
a psychological assessment,1 he was seized and thus sub-
jected to a serious deprivation of liberty. But was this war-
rantless seizure “reasonable”? We have addressed the
standards required by due process for involuntary commit-
ment to a mental treatment facility, see Addington v. Texas,
441 U. S. 418, 427 (1979); see also O’Connor v. Donaldson,
422 U. S. 563, 574–576 (1975); Foucha v. Louisiana, 504
U. S. 71, 75–77, 83 (1992), but we have not addressed
Fourth Amendment restrictions on seizures like the one
that we must assume occurred here, i.e., a short-term sei-
zure conducted for the purpose of ascertaining whether a
person presents an imminent risk of suicide. Every State
has laws allowing emergency seizures for psychiatric treat-
ment, observation, or stabilization, but these laws vary in
many respects, including the categories of persons who may
request the emergency action, the reasons that can justify
the action, the necessity of a judicial proceeding, and the
nature of the proceeding.2 Mentioning these laws only in
passing, petitioner asked us to render a decision that could
——————
   1 The Court of Appeals assumed petitioner’s consent was not voluntary

because the police allegedly promised that they would not seize his guns
if he went for a psychological evaluation. 953 F. 3d 112, 121 (CA1 2020).
The Court does not decide whether this assumption was justified.
   2 See Brief for Petitioner 38–39, n. 4 (gathering state authorities); L.

Hedman et al., State Laws on Emergency Holds for Mental Health Sta-
bilization, 67 Psychiatric Servs. 579 (2016).
                  Cite as: 593 U. S. ____ (2021)            3

                      ALITO, J., concurring

call features of these laws into question. The Court appro-
priately refrains from doing so.
   4. This case also implicates another body of law that pe-
titioner glossed over: the so-called “red flag” laws that some
States are now enacting. These laws enable the police to
seize guns pursuant to a court order to prevent their use for
suicide or the infliction of harm on innocent persons. See,
e.g., Cal. Penal Code Ann. §§18125–18148 (West Cum.
Supp. 2021); Fla. Stat. §790.401(4) (Cum. Supp. 2021);
Mass. Gen. Laws Ann., ch. 140, §131T (2021). They typi-
cally specify the standard that must be met and the proce-
dures that must be followed before firearms may be seized.
Provisions of red flag laws may be challenged under the
Fourth Amendment, and those cases may come before us.
Our decision today does not address those issues.
   5. One additional category of cases should be noted: those
involving warrantless, nonconsensual searches of a home
for the purpose of ascertaining whether a resident is in ur-
gent need of medical attention and cannot summon help.
At oral argument, THE CHIEF JUSTICE posed a question
that highlighted this problem. He imagined a situation in
which neighbors of an elderly woman call the police and ex-
press concern because the woman had agreed to come over
for dinner at 6 p.m., but by 8 p.m., had not appeared or
called even though she was never late for anything. The
woman had not been seen leaving her home, and she was
not answering the phone. Nor could the neighbors reach
her relatives by phone. If the police entered the home with-
out a warrant to see if she needed help, would that violate
the Fourth Amendment? Tr. of Oral Arg. 6–8.
   Petitioner’s answer was that it would. Indeed, he argued,
even if 24 hours went by, the police still could not lawfully
enter without a warrant. If the situation remained un-
changed for several days, he suggested, the police might be
able to enter after obtaining “a warrant for a missing per-
son.” Id., at 9.
4                        CANIGLIA v. STROM

                          ALITO, J., concurring

  THE CHIEF JUSTICE’s question concerns an important
real-world problem. Today, more than ever, many people,
including many elderly persons, live alone.3 Many elderly
men and women fall in their homes,4 or become incapaci-
tated for other reasons, and unfortunately, there are many
cases in which such persons cannot call for assistance. In
those cases, the chances for a good recovery may fade with
each passing hour.5 So in THE CHIEF JUSTICE’s imaginary
case, if the elderly woman was seriously hurt or sick and
the police heeded petitioner’s suggestion about what the
Fourth Amendment demands, there is a fair chance she
would not be found alive. This imaginary woman may have
regarded her house as her castle, but it is doubtful that she
would have wanted it to be the place where she died alone
and in agony.
  Our current precedents do not address situations like
this. We have held that the police may enter a home with-
out a warrant when there are “exigent circumstances.”
Payton v. New York, 445 U. S. 573, 590 (1980). But circum-
stances are exigent only when there is not enough time to
get a warrant, see Missouri v. McNeely, 569 U. S. 141, 149
(2013); Michigan v. Tyler, 436 U. S. 499, 509 (1978), and
warrants are not typically granted for the purpose of check-
ing on a person’s medical condition. Perhaps States should
institute procedures for the issuance of such warrants, but
——————
   3 Dept. of Commerce, Bureau of Census, The Rise of Living Alone,

Fig. HH–4 (2020), https://www.census.gov/content/dam/Census/
library /visualizations/time-series/demo/families-and-households/hh-4.pdf;
Ortiz-Ospina, The Rise of Living Alone (Dec. 10, 2019), https://our-
worldindata.org/living-alone; Smith, Cities With the Most Adults Living
Alone (May 4, 2020), https://www.self.inc/blog/adults-living-alone.
   4 See B. Moreland, R. Kakara, & A. Henry, Trends in Nonfatal Falls

and Fall-Related Injuries Among Adults Aged ≥65 Years—United States,
2012–2018, 69 Morbidity and Mortality Weekly Rep. 875 (2020).
   5 See, e.g., J. Gurley, N. Lum, M. Sande, B. Lo, & M. Katz, Persons

Found in Their Homes Helpless or Dead, 334 New Eng. J. Med. 1710
(1996).
                Cite as: 593 U. S. ____ (2021)          5

                    ALITO, J., concurring

in the meantime, courts may be required to grapple with
the basic Fourth Amendment question of reasonableness.
   6. The three categories of cases discussed above are
simply illustrative. Searches and seizures conducted for
other non-law-enforcement purposes may arise and may
present their own Fourth Amendment issues. Today’s de-
cision does not settle those questions.
                         *    *       *
  In sum, the Court properly rejects the broad “community
caretaking” theory on which the decision below was based.
The Court’s decision goes no further, and on that under-
standing, I join the opinion in full.
                  Cite as: 593 U. S. ____ (2021)             1

                   KAVANAUGH, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 20–157
                          _________________


        EDWARD A. CANIGLIA, PETITIONER v.
            ROBERT F. STROM, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
             APPEALS FOR THE FIRST CIRCUIT
                         [May 17, 2021]

   JUSTICE KAVANAUGH, concurring.
   I join the Court’s opinion in full. I write separately to
underscore and elaborate on THE CHIEF JUSTICE’s point
that the Court’s decision does not prevent police officers
from taking reasonable steps to assist those who are inside
a home and in need of aid. See ante, at 1 (ROBERTS, C. J.,
concurring). For example, as I will explain, police officers
may enter a home without a warrant in circumstances
where they are reasonably trying to prevent a potential su-
icide or to help an elderly person who has been out of con-
tact and may have fallen and suffered a serious injury.
   Ratified in 1791 and made applicable to the States in
1868, the Fourth Amendment protects the “right of the peo-
ple to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures.” As the con-
stitutional text establishes, the “ultimate touchstone of the
Fourth Amendment is reasonableness.” Riley v. California,
573 U. S. 373, 381 (2014) (internal quotation marks omit-
ted). The Court has said that a warrant supported by prob-
able cause is ordinarily required for law enforcement offic-
ers to enter a home. See U. S. Const., Amdt. 4. But drawing
on common-law analogies and a commonsense appraisal of
what is “reasonable,” the Court has recognized various sit-
uations where a warrant is not required. For example, the
exigent circumstances doctrine allows officers to enter a
2                    CANIGLIA v. STROM

                   KAVANAUGH, J., concurring

home without a warrant in certain situations, including: to
fight a fire and investigate its cause; to prevent the immi-
nent destruction of evidence; to engage in hot pursuit of a
fleeing felon or prevent a suspect’s escape; to address a
threat to the safety of law enforcement officers or the gen-
eral public; to render emergency assistance to an injured
occupant; or to protect an occupant who is threatened with
serious injury. See Mitchell v. Wisconsin, 588 U. S. ___, ___
(2019) (plurality opinion) (slip op., at 6); City and County of
San Francisco v. Sheehan, 575 U. S. 600, 612 (2015); Ken-
tucky v. King, 563 U. S. 452, 460, 462 (2011); Michigan v.
Fisher, 558 U. S. 45, 47 (2009) (per curiam); Brigham City
v. Stuart, 547 U. S. 398, 403 (2006); Minnesota v. Olson, 495
U. S. 91, 100 (1990); Michigan v. Clifford, 464 U. S. 287,
293, and n. 4 (1984) (plurality opinion); Mincey v. Arizona,
437 U. S. 385, 392–394 (1978); Michigan v. Tyler, 436 U. S.
499, 509–510 (1978); United States v. Santana, 427 U. S.
38, 42–43 (1976); Warden, Md. Penitentiary v. Hayden, 387
U. S. 294, 298–299 (1967); Ker v. California, 374 U. S. 23,
40–41 (1963) (plurality opinion).
   Over the years, many courts, like the First Circuit in this
case, have relied on what they have labeled a “community
caretaking” doctrine to allow warrantless entries into the
home for a non-investigatory purpose, such as to prevent a
suicide or to conduct a welfare check on an older individual
who has been out of contact. But as the Court today ex-
plains, any such standalone community caretaking doctrine
was primarily devised for searches of cars, not homes. Ante,
at 3–4; see Cady v. Dombrowski, 413 U. S. 433, 447–448
(1973).
   That said, this Fourth Amendment issue is more labeling
than substance. The Court’s Fourth Amendment case law
already recognizes the exigent circumstances doctrine,
which allows an officer to enter a home without a warrant
if the “exigencies of the situation make the needs of law en-
                  Cite as: 593 U. S. ____ (2021)             3

                   KAVANAUGH, J., concurring

forcement so compelling that the warrantless search is ob-
jectively reasonable under the Fourth Amendment.”
Brigham City, 547 U. S., at 403 (internal quotation marks
omitted); see also ante, at 3. As relevant here, one such rec-
ognized “exigency” is the “need to assist persons who are
seriously injured or threatened with such injury.” Brigham
City, 547 U. S., at 403; see also ante, at 1 (ROBERTS, C. J.,
concurring). The Fourth Amendment allows officers to en-
ter a home if they have “an objectively reasonable basis for
believing” that such help is needed, and if the officers’ ac-
tions inside the home are reasonable under the circum-
stances. Brigham City, 547 U. S., at 406; see also Michigan
v. Fisher, 558 U. S., at 47–48.
   This case does not require us to explore all the contours
of the exigent circumstances doctrine as applied to emer-
gency-aid situations because the officers here disclaimed re-
liance on that doctrine. But to avoid any confusion going
forward, I think it important to briefly describe how the doc-
trine applies to some heartland emergency-aid situations.
   As Chief Judge Livingston has cogently explained, alt-
hough this doctrinal area does not draw much attention
from courts or scholars, “municipal police spend a good deal
of time responding to calls about missing persons, sick
neighbors, and premises left open at night.” Livingston, Po-
lice, Community Caretaking, and the Fourth Amendment,
1998 U. Chi. Leg. Forum 261, 263 (1998). And as she aptly
noted, “the responsibility of police officers to search for
missing persons, to mediate disputes, and to aid the ill or
injured has never been the subject of serious debate; nor
has” the “responsibility of police to provide services in an
emergency.” Id., at 302.
   Consistent with that reality, the Court’s exigency prece-
dents, as I read them, permit warrantless entries when po-
lice officers have an objectively reasonable basis to believe
that there is a current, ongoing crisis for which it is reason-
4                       CANIGLIA v. STROM

                      KAVANAUGH, J., concurring

able to act now. See, e.g., Sheehan, 575 U. S., at 612; Mich-
igan v. Fisher, 558 U. S., at 48–49; Brigham City, 547 U. S.,
at 406–407. The officers do not need to show that the harm
has already occurred or is mere moments away, because
knowing that will often be difficult if not impossible in cases
involving, for example, a person who is currently suicidal or
an elderly person who has been out of contact and may have
fallen. If someone is at risk of serious harm and it is rea-
sonable for officers to intervene now, that is enough for the
officers to enter.
   A few (non-exhaustive) examples illustrate the point.
   Suppose that a woman calls a healthcare hotline or 911
and says that she is contemplating suicide, that she has
firearms in her home, and that she might as well die. The
operator alerts the police, and two officers respond by driv-
ing to the woman’s home. They knock on the door but do
not receive a response. May the officers enter the home? Of
course.
   The exigent circumstances doctrine applies because the
officers have an “objectively reasonable basis” for believing
that an occupant is “seriously injured or threatened with
such injury.” Id., at 400, 403; cf. Sheehan, 575 U. S., at 612
(officers could enter the room of a mentally ill person who
had locked herself inside with a knife). After all, a suicidal
individual in such a scenario could kill herself at any mo-
ment. The Fourth Amendment does not require officers to
stand idly outside as the suicide takes place.1
   Consider another example. Suppose that an elderly man
is uncharacteristically absent from Sunday church services
——————
   1 In 2019 in the United States, 47,511 people committed suicide. That

number is more than double the number of annual homicides. See Dept.
of Health and Human Servs., Centers for Disease Control and Preven-
tion, D. Stone, C. Jones, & K. Mack, Changes in Suicide Rates––United
States, 2018–2019, 70 Morbidity and Mortality Weekly Rep. 261, 263
(2021) (MMWR); Dept. of Justice, Federal Bureau of Investigation, Uni-
form Crime Report, Crime in the United States, 2019, p. 2 (2020).
                      Cite as: 593 U. S. ____ (2021)                     5

                       KAVANAUGH, J., concurring

and repeatedly fails to answer his phone throughout the
day and night. A concerned relative calls the police and
asks the officers to perform a wellness check. Two officers
drive to the man’s home. They knock but receive no re-
sponse. May the officers enter the home? Of course.
   Again, the officers have an “objectively reasonable basis”
for believing that an occupant is “seriously injured or
threatened with such injury.” Brigham City, 547 U. S., at
400, 403. Among other possibilities, the elderly man may
have fallen and hurt himself, a common cause of death or
serious injury for older individuals. The Fourth Amend-
ment does not prevent the officers from entering the home
and checking on the man’s well-being.2
   To be sure, courts, police departments, and police officers
alike must take care that officers’ actions in those kinds of
cases are reasonable under the circumstances. But both of
those examples and others as well, such as cases involving
unattended young children inside a home, illustrate the
kinds of warrantless entries that are perfectly constitu-
tional under the exigent circumstances doctrine, in my
view.
   With those observations, I join the Court’s opinion in full.




——————
  2 In 2018 in the United States, approximately 32,000 older adults died

from falls. Falls are also the leading cause of injury for older adults. B.
Moreland, R. Kakara, & A. Henry, Trends in Nonfatal Falls and Fall-
Related Injuries Among Adults Aged ≥ 65 Years––United States, 2012–
2018, 69 MMWR 875 (2020).

```

---

## GROUP: content/cases/Cardwell v. Lewis.md  (`case`, 6 assertions)

### content_page

```
---
title: "Cardwell v. Lewis"
type: case
citation: "417 U.S. 583 (1974)"
parallel_cite: "94 S. Ct. 2464; 41 L. Ed. 2d 325; 69 Ohio Op. 2d 69"
neutral_cite: 1974 U.S. LEXIS 75
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-06-17
docket: 72-1603
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Cardwell v. Lewis
  varies_by_point: false
  scope_note: "Plurality opinion (Blackmun, J., joined by Burger, White, Rehnquist; Powell, J., concurring in the result). The reduced-expectation-of-privacy-in-a-vehicle's-exterior rationale is settled and routinely cited (e.g., quoted in United States v. Chadwick)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109069/cardwell-v-lewis/"
  cluster_id: 109069
  opinion_id: 109069
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[Chambers v. Maroney]]", "[[Cooper v. California]]", "[[Coolidge v. New Hampshire]]", "[[New York v. Class]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "reduced-expectation-of-privacy", "vehicle-exterior", "no-search"]
holding: "Examining a car's exterior (paint scrapings, tire tread) on probable cause in a public lot invades no privacy interest the warrant requirement protects; one has a reduced expectation of privacy in a vehicle, especially its exterior."
lake:
  record_id: Cardwell v. Lewis
  status: verified
  projected_at: 2026-07-09
---

# Cardwell v. Lewis

*417 U.S. 583 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police investigating a murder had probable cause to believe the respondent's car had been used in the crime. After the respondent came to the station and was arrested, police impounded his car from a public commercial lot, towed it to an impound area, and there took paint scrapings from the exterior and made a cast of a tire tread. That exterior evidence was introduced at his murder trial.

## Issue
Whether the warrantless examination of an automobile's exterior — paint scrapings and tire tread — on probable cause, after the car was impounded from a public lot, is a search that violates the Fourth Amendment.

## Rule
No. A vehicle, and especially its exterior, carries a reduced expectation of privacy: "One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one's residence or as the repository of personal effects. A car has little capacity for escaping public scrutiny. It travels public thoroughfares where both its occupants and its contents are in plain view." — 417 U.S. at 590 (plurality opinion). ^pin-590

Because only the exterior was examined, no protected privacy was invaded: "With the 'search' limited to the examination of the tire on the wheel and the taking of paint scrapings from the exterior of the vehicle left in the public parking lot, we fail to comprehend what expectation of privacy was infringed." — *Id.* at 591. ^pin-591

The bottom line: "where probable cause exists, a warrantless examination of the exterior of a car is not unreasonable under the Fourth and Fourteenth Amendments." — [*Id.* at 592](https://www.courtlistener.com/opinion/109069/cardwell-v-lewis/#:~:text=where%20probable%20cause%20exists%2C%20a). ^pin-592

## Application
Nothing from the interior of the car and no personal effects were searched or seized; the evidence was limited to paint scrapings from the exterior and an observation of the tire tread on an operative wheel, taken from a car left in a public lot. With probable cause established, that exterior examination invaded no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]], and the prior impoundment did not change the result, since police could have made the same examination on the spot.

## Conclusion
The exterior examination was reasonable; the seizure and examination did not violate the Fourth Amendment, and the grant of [[Common Legal Terms#habeas-corpus|habeas]] relief was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Powell, J., concurred in the result on a different ground).
- No negative treatment of the exterior-examination / reduced-vehicle-privacy rationale, which the Court has continued to invoke (e.g., quoted in [[United States v. Chadwick]] and reflected in the no-REP-in-a-public-VIN holding of [[New York v. Class]]).

## Appears on
- [[Automobile Exception]] — *Related (cross-doctrine)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *Cardwell v. Lewis*, 417 U.S. 583 (1974) — https://www.courtlistener.com/opinion/109069/cardwell-v-lewis/ — pinpoints: 590, 591, 592.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6525c972a315386b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "417 U.S. 583 (1974)", "court": "U.S. Supreme Court", "neutral_cite": "1974 U.S. LEXIS 75", "official_citation_present": true, "parallel_cite": "94 S. Ct. 2464; 41 L. Ed. 2d 325; 69 Ohio Op. 2d 69", "title": "Cardwell v. Lewis", "year": "1974"}}
{"assertion_id": "2c4bda24c0a24f7b", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Related (cross-doctrine)", "title": "Cardwell v. Lewis"}}
{"assertion_id": "54e5dd4985013d06", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "Cardwell v. Lewis"}}
{"assertion_id": "9f4b28ff21567824", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Examining a car's exterior (paint scrapings, tire tread) on probable cause in a public lot invades no privacy interest the warrant requirement protects; one has a reduced expectation of privacy in a vehicle, especially its exterior.", "title": "Cardwell v. Lewis"}}
{"assertion_id": "dfd409f7f1aae2b6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1974-06-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Cardwell v. Lewis", "field_i_validity": "good_law", "scope_note": "Plurality opinion (Blackmun, J., joined by Burger, White, Rehnquist; Powell, J., concurring in the result). The reduced-expectation-of-privacy-in-a-vehicle's-exterior rationale is settled and routinely cited (e.g., quoted in United States v. Chadwick).", "title": "Cardwell v. Lewis", "varies_by_point": "false"}}
{"assertion_id": "fa8ad73b1fef5714", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Cardwell v. Lewis"}}
```

### lake record — Cardwell v. Lewis

```json
{
  "schema_version": "s2.v1",
  "record_id": "Cardwell v. Lewis",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Cardwell v. Lewis",
    "case_name_short": "Cardwell",
    "case_name_full": "Cardwell, Warden v. Lewis",
    "input_case_name": "Cardwell v. Lewis",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-06-17",
    "year": 1974,
    "docket": "72-1603",
    "cluster_id": 109069,
    "lead_opinion_id": 109069,
    "sibling_ids": [
      109069,
      9425767,
      9425768,
      9425769
    ],
    "absolute_url": "/opinion/109069/cardwell-v-lewis/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8997104,
        "score": 20,
        "case_name": "Cardwell v. Lewis"
      },
      {
        "cluster_id": 8996372,
        "score": 20,
        "case_name": "Cardwell v. Lewis"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "417 U.S. 583",
      "volume": "417",
      "reporter": "U.S.",
      "page": "583",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 2464",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "2464",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "41 L. Ed. 2d 325",
        "volume": "41",
        "reporter": "L. Ed. 2d",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 Ohio Op. 2d 69",
        "volume": "69",
        "reporter": "Ohio Op. 2d",
        "page": "69",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 75",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "75",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "417 U.S. 583",
        "volume": "417",
        "reporter": "U.S.",
        "page": "583",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 2464",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "2464",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "41 L. Ed. 2d 325",
        "volume": "41",
        "reporter": "L. Ed. 2d",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 75",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "75",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 Ohio Op. 2d 69",
        "volume": "69",
        "reporter": "Ohio Op. 2d",
        "page": "69",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "417 U.S. 583",
    "official_selection": {
      "court_class": "scotus",
      "selected": "417 U.S. 583",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-590",
      "page": null,
      "quote": "--- # Cardwell v. Lewis *417 U.S. 583 (1974)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police investigating a murder had probable cause to believe the respondent's car had been used in the crime. After the respondent came to the station and was arrested, police impounded his car from a public commercial lot, towed it to an impound area, and there took paint scrapings from the exterior and made a cast of a tire tread. That exterior evidence was introduced at his murder trial. ## Issue Whether the warrantless examination of an automobile's exterior \u2014 paint scrapings and tire tread \u2014 on probable cause, after the car was impounded from a public lot, is a search that violates the Fourth Amendment. ## Rule No. A vehicle, and especially its exterior, carries a reduced expectation of privacy:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-591",
      "page": null,
      "quote": "With the 'search' limited to the examination of the tire on the wheel and the taking of paint scrapings from the exterior of the vehicle left in the public parking lot, we fail to comprehend what expectation of privacy was infringed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-592",
      "page": null,
      "quote": "where probable cause exists, a warrantless examination of the exterior of a car is not unreasonable under the Fourth and Fourteenth Amendments.",
      "star_marker": "592",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 16006,
      "fragment": "#:~:text=where%20probable%20cause%20exists%2C%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Cardwell v. Lewis",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (Blackmun, J., joined by Burger, White, Rehnquist; Powell, J., concurring in the result). The reduced-expectation-of-privacy-in-a-vehicle's-exterior rationale is settled and routinely cited (e.g., quoted in United States v. Chadwick).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4786330,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Vasquez-Algarin",
          "cluster_id": 3199633,
          "cite": [
            "821 F.3d 467",
            "2016 U.S. App. LEXIS 7889",
            "2016 WL 1730540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morgan v. State",
          "cluster_id": 1713874,
          "cite": [
            "906 S.W.2d 620",
            "1995 WL 515837"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Savva",
          "cluster_id": 2277827,
          "cite": [
            "616 A.2d 774",
            "159 Vt. 75",
            "1992 Vt. LEXIS 116"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cyrus Jonathan George",
          "cluster_id": 588130,
          "cite": [
            "971 F.2d 1113"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sanchez",
          "cluster_id": 2383586,
          "cite": [
            "800 S.W.2d 292",
            "1990 WL 178626"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Francisco Paulino",
          "cluster_id": 508162,
          "cite": [
            "850 F.2d 93",
            "1988 U.S. App. LEXIS 8724",
            "1988 WL 64524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rakas v. Illinois",
          "cluster_id": 109953,
          "cite": [
            "58 L. Ed. 2d 387",
            "99 S. Ct. 421",
            "439 U.S. 128",
            "1978 U.S. LEXIS 2452"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Fuerte",
          "cluster_id": 109541,
          "cite": [
            "49 L. Ed. 2d 1116",
            "96 S. Ct. 3074",
            "428 U.S. 543",
            "1976 U.S. LEXIS 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Indianapolis v. Edmond",
          "cluster_id": 118391,
          "cite": [
            "148 L. Ed. 2d 333",
            "121 S. Ct. 447",
            "531 U.S. 32",
            "2000 U.S. LEXIS 8084",
            "69 U.S.L.W. 4009",
            "14 Fla. L. Weekly Fed. S 9",
            "2000 Colo. J. C.A.R. 6401",
            "2000 Cal. Daily Op. Serv. 9549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyoming v. Houghton",
          "cluster_id": 118277,
          "cite": [
            "143 L. Ed. 2d 408",
            "119 S. Ct. 1297",
            "526 U.S. 295",
            "1999 U.S. LEXIS 2347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knotts",
          "cluster_id": 110882,
          "cite": [
            "75 L. Ed. 2d 55",
            "103 S. Ct. 1081",
            "460 U.S. 276",
            "1983 U.S. LEXIS 135",
            "51 U.S.L.W. 4232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Class",
          "cluster_id": 111600,
          "cite": [
            "89 L. Ed. 2d 81",
            "106 S. Ct. 960",
            "475 U.S. 106",
            "1986 U.S. LEXIS 5",
            "54 U.S.L.W. 4178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1196592,
          "cite": [
            "867 P.2d 593",
            "123 Wash. 2d 173",
            "1994 Wash. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Belton",
          "cluster_id": 5685394,
          "cite": [
            "55 N.Y.2d 49",
            "432 N.E.2d 745",
            "447 N.Y.S.2d 873",
            "1982 N.Y. LEXIS 3067"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 1142777,
          "cite": [
            "666 P.2d 802",
            "295 Or. 227",
            "1983 Ore. LEXIS 1342"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Alston",
          "cluster_id": 2283490,
          "cite": [
            "440 A.2d 1311",
            "88 N.J. 211",
            "1981 N.J. LEXIS 1677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carlo Scott Bagley",
          "cluster_id": 457913,
          "cite": [
            "772 F.2d 482",
            "19 Fed. R. Serv. 222",
            "1985 U.S. App. LEXIS 23309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109069 OR 9425767 OR 9425768 OR 9425769) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NTgzMTY4MDAwMDAmcz0xNjM4MjczJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109069+OR+9425767+OR+9425768+OR+9425769%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(109069 OR 9425767 OR 9425768 OR 9425769)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzcmcz0yMDY2MDk3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109069+OR+9425767+OR+9425768+OR+9425769%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109069 OR 9425767 OR 9425768 OR 9425769)",
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
    "complete_query": "cites:(109069 OR 9425767 OR 9425768 OR 9425769)",
    "indexed_citing_opinions": 662,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109069,
        "count": 589,
        "count_source": "search"
      },
      {
        "opinion_id": 9425767,
        "count": 102,
        "count_source": "search"
      },
      {
        "opinion_id": 9425768,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425769,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1012,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/cardwell-v-lewis.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3MDU0NTEmcz00NzM5MTkzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109069+OR+9425767+OR+9425768+OR+9425769%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109069,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 109032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 310138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 1380337,
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
    "date_created": "2026-07-04T23:32:02Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:32:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:32:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:36:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:32:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Cardwell v. Lewis

```
<div>
<center><b><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">417 U.S. 583</a></span> (1974)</b></center>
<center><h1>CARDWELL, WARDEN<br>
v.<br>
LEWIS.</h1></center>
<center>No. 72-1603.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 18, 1974.</center>
<center>Decided June 17, 1974.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT.
<p><span class="star-pagination">*584</span> <i>Leo J. Conway,</i> Assistant Attorney General of Ohio, argued the cause for petitioner. With him on the brief were <i>William J. Brown,</i> Attorney General, and <i>Nicholas R. Curci,</i> Assistant Attorney General.</p>
<p><i>Bruce A. Campbell,</i> by appointment of the Court, 414 <span class="star-pagination">*585</span> U. S. 1140, argued the cause and filed a brief for respondent.</p>
<p><i>Andrew L. Frey</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. On the brief were <i>Solicitor General Bork, Assistant Attorney General Petersen,</i> and <i>Edward R. Korman.</i></p>
<p>MR. JUSTICE BLACKMUN announced the judgment of the Court and an opinion in which the CHIEF JUSTICE, MR. JUSTICE WHITE, and MR. JUSTICE REHNQUIST join.</p>
<p>This case presents the issue of the legality, under the Fourth and Fourteenth Amendments, of a warrantless seizure of an automobile and the examination of its exterior at a police impoundment area after the car had been removed from a public parking lot.</p>
<p>Evidence obtained upon this examination was introduced at the respondent's state court trial for first-degree murder. He was convicted. The Federal District Court, on a habeas corpus application, ruled that the examination was a search violative of the Fourth and Fourteenth Amendments. <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp. 26</a></span> (SD Ohio 1972). The United States Court of Appeals for the Sixth Circuit affirmed. <span class="citation" data-id="310138"><a href="/opinion/310138/arthur-ben-lewis-jr-v-harold-j-cardwell-warden/" aria-description="Citation for case: Arthur Ben Lewis, Jr. v. Harold J. Cardwell, Warden">476 F. 2d 467</a></span> (1973). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1062/">414 U. S. 1062</a></span> (1973), and now conclude that, under the circumstances of this case, there was no violation of the protection afforded by the Amendments.</p>
<p></p>
<h2>I</h2>
<p>In 1968 respondent Arthur Ben Lewis, Jr., was tried and convicted by a jury in an Ohio state court for the first-degree murder of Paul Radcliffe. On appeal, the Supreme Court of Ohio affirmed the judgment of conviction. <i>State</i> v. <i>Lewis,</i> <span class="citation" data-id="6754444"><a href="/opinion/6864632/state-v-lewis/" aria-description="Citation for case: State v. Lewis">22 Ohio St. 2d 125</a></span>, <span class="citation" data-id="6754444"><a href="/opinion/6864632/state-v-lewis/" aria-description="Citation for case: State v. Lewis">258 N. E. 2d 445</a></span> (1970). This Court denied review. <i>Lewis</i> v. <i>Ohio,</i> <span class="citation" data-id="8973497"><a href="/opinion/8981620/lewis-v-ohio/" aria-description="Citation for case: Lewis v. Ohio">400 U. S. 959</a></span> (1970).</p>
<p><span class="star-pagination">*586</span> On respondent's federal habeas application, the District Court, from the record and after an evidentiary hearing, adduced the following facts:</p>
<p>On the afternoon of July 19, 1967, Radcliffe's body was found near his car on the banks of the Olentangy River in Delaware County, Ohio. The car had gone over the embankment and had come to rest in brush. Radcliffe had died from shotgun wounds. Casts were made of tire tracks at the scene, and foreign paint scrapings were removed from the right rear fender of Radcliffe's automobile.</p>
<p>Within five days of Radcliffe's death, the investigation began to focus upon respondent Lewis. It was learned that Lewis knew Radcliffe. Lewis had been negotiating the sale of a business and had executed a contract of sale. The purchaser, Jack Smith, employed Radcliffe, an accountant, to examine Lewis' books. Police went to Lewis' place of business to question him and there observed the model and color of his car in the thought that it might have been used to push the Radcliffe vehicle over the embankment. Not until several months later, however, in late September, was Lewis again questioned. On October 9, he was asked to appear the next morning at the Office of the Division of Criminal Activities in Columbus for further interrogation.</p>
<p>On October 10, at 8 a. m., a warrant for respondent's arrest was obtained.<sup>[1]</sup> The District Court found that at <span class="star-pagination">*587</span> this time, in addition to probable cause for the arrest, the police also had probable cause to believe that Lewis' car was used in the commission of the crime. An automobile similar to his had been observed leaving the scene; the color of his vehicle was similar to the color of the paint scrapings from the victim's car; in a telephone call to Mrs. Smith, made by a person who said he was Radcliffe, but proved not to be,<sup>[2]</sup> the caller made statements that, if true, would benefit only Lewis; he had had body repair work done on the grille, hood, right front fender, and other parts of his car on the day following the crime; and the victim's desk calendar for the day of his death showed the notation, "Call Ben Lewis."<sup>[3]</sup></p>
<p>Respondent Lewis complied with the request to appear. He drove his car to the Activities Office, placed it in a public commercial parking lot a half block away, and arrived shortly after 10 a. m. Although the police were in possession of the arrest warrant for the entire period that Lewis was present, he was not served with that warrant or arrested until late that afternoon, at approximately 5 p. m. Two hours earlier, Lewis had been permitted to call his lawyer, and two attorneys were present on his behalf in the office at the time of the formal arrest. Upon the arrest, Lewis' car keys and the parking lot claim check were released to the police. A tow truck <span class="star-pagination">*588</span> was dispatched to remove the car from the parking lot to the police impoundment lot.</p>
<p>The impounded car was examined the next day by a technician from the Ohio Bureau of Criminal Investigation. The tread of its right rear tire was found to match the cast of a tire impression made at the scene of the crime.<sup>[4]</sup> The technician testified that, in his opinion, the foreign paint on the fender of Radcliffe's car was not different from the paint samples taken from respondent's vehicle, that is, there was no difference in color, texture, or order of layering of the paint.</p>
<p>The District Court concluded that the seizure and examination of Lewis' car were violative of the Fourth and Fourteenth Amendments, and that the evidence obtained therefrom should have been excluded at the state court trial. The court, accordingly, issued a writ of habeas corpus requiring the State to "initiate action for a new trial of" respondent within 90 days or, in the alternative, to release him. <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/#44" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp., at 44</a></span>. The Court of Appeals, in affirming, held that the scraping of paint from the exterior of Lewis' car was in fact a search, within the meaning of the Fourth Amendment; that there was no consent to that search; that it was not incident to Lewis' arrest; and that the seizure of the car could not be justified on the ground that the vehicle was an instrumentality of the crime in plain view.</p>
<p></p>
<h2>II</h2>
<p>This case is factually different from prior car search cases decided by this Court. The evidence with which we are concerned is not the product of a "search" that implicates <span class="star-pagination">*589</span> traditional considerations of the owner's privacy interest. It consisted of paint scrapings from the <i>exterior</i> and an observation of the tread of a tire on an operative wheel. The issue, therefore, is whether the examination of an automobile's exterior upon probable cause invades a right to privacy which the interposition of a warrant requirement is meant to protect. This is an issue this Court has not previously addressed.</p>
<p>The common-law notion that a warrant to search and seize is dependent upon the assertion of a superior government interest in property, see, <i>e. g., </i><i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 1066 (1765), and the proposition that a warrant is valid "only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it," <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 309</a></span> (1921), were explicitly rejected as controlling Fourth Amendment considerations in <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#302" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 302-306</a></span> (1967). Rather than property rights, the primary object of the Fourth Amendment was determined to be the protection of privacy. <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#305" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden"><i>Id.,</i> at 305-306</a></span>. And it had been said earlier: "The decisions of this Court have time and again underscored the essential purpose of the Fourth Amendment to shield the citizen from unwarranted intrusions into his privacy." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#498" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 498</a></span> (1958). See also <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#769" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 769-770</a></span> (1966); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 350</a></span> (1967); <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#14" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 14-15</a></span> (1973).</p>
<p>At least since <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), the Court has recognized a distinction between the warrantless search and seizure of automobiles or other movable vehicles, on the one hand, and the search of a home or office, on the other. Generally, less stringent <span class="star-pagination">*590</span> warrant requirements have been applied to vehicles. In <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#49" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 49</a></span> (1970), the Court chronicled the development of car searches and seizures.<sup>[5]</sup> An underlying factor in the <i>Carroll-Chambers</i> line of decisions has been the exigent circumstances that exist in connection with movable vehicles. "[T]he circumstances that furnish probable cause to search a particular auto for particular articles are most often unforeseeable; moreover, the opportunity to search is fleeting since a car is readily movable." <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#50" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 50-51</a></span>. This is strikingly true where the automobile's owner is alerted to police intentions and, as a consequence, the motivation to remove evidence from official grasp is heightened.</p>
<p>There is still another distinguishing factor. "The search of an automobile is far less intrusive on the rights protected by the Fourth Amendment than the search of one's person or of a building." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#279" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 279</a></span> (1973) (POWELL, J., concurring). One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one's residence or as the repository of personal effects. A car has little capacity for escaping public scrutiny. It travels public thoroughfares where both its occupants and its contents are in plain view. See <i>People</i> v. <i>Case,</i> <span class="citation" data-id="7951958"><a href="/opinion/7998117/people-v-case/#388" aria-description="Citation for case: People v. Case">220 Mich. 379, 388-389</a></span>, <span class="star-pagination">*591</span> <span class="citation" data-id="7951958"><a href="/opinion/7998117/people-v-case/#292" aria-description="Citation for case: People v. Case">190 N. W. 289, 292</a></span> (1922). "What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351</a></span>; <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#14" aria-description="Citation for case: United States v. Dionisio">410 U. S., at 14</a></span>. This is not to say that no part of the interior of an automobile has Fourth Amendment protection; the exercise of a desire to be mobile does not, of course, waive one's right to be free of unreasonable government intrusion. But insofar as Fourth Amendment protection extends to a motor vehicle, it is the right to privacy that is the touchstone of our inquiry.</p>
<p>In the present case, nothing from the interior of the car and no personal effects, which the Fourth Amendment traditionally has been deemed to protect, were searched or seized and introduced in evidence.<sup>[6]</sup> With the "search" limited to the examination of the tire on the wheel and the taking of paint scrapings from the exterior of the vehicle left in the public parking lot, we fail to comprehend what expectation of privacy was infringed.<sup>[7]</sup> Stated <span class="star-pagination">*592</span> simply, the invasion of privacy, "if it can be said to exist, is abstract and theoretical." <i>Air Pollution Variance Board</i> v. <i>Western Alfalfa Corp.,</i> <span class="citation" data-id="109032"><a href="/opinion/109032/air-pollution-variance-bd-of-colo-v-western-alfalfa-corp/#865" aria-description="Citation for case: Air Pollution Variance Bd. of Colo. v. Western Alfalfa Corp.">416 U. S. 861, 865</a></span> (1974). Under circumstances such as these, where probable cause exists, a warrantless examination of the exterior of a car is not unreasonable under the Fourth and Fourteenth Amendments.<sup>[8]</sup></p>
<p>Here, it has been established and is conceded that the police had probable cause to search Lewis' car. An automobile similar in color and model to his car had been seen leaving the scene of the crime. This similarity was corroborated by comparison of the paint scrapings taken from the victim's car with the color and paint of Lewis' automobile. Lewis had had repair work done on his car immediately following the death of the victim. And he had a nexus with Radcliffe on the day of death. All this provided reason to believe that the car was used in the commission of the crime for which Lewis was arrested. <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61</a></span> (1967).</p>
<p></p>
<h2>III</h2>
<p>Concluding, as we have, that the examination of the exterior of the vehicle upon probable cause was reasonable, <span class="star-pagination">*593</span> we have yet to determine whether the prior impoundment of the automobile rendered that examination a violation of the Fourth and Fourteenth Amendments. We do not think that, because the police impounded the car prior to the examination, which they could have made on the spot, there is a constitutional barrier to the use of the evidence obtained thereby. Under the circumstances of this case, the seizure itself was not unreasonable.</p>
<p>Respondent asserts that this case is indistinguishable from <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971). We do not agree. The present case differs from <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> both in the scope of the search<sup>[9]</sup> and in the circumstances of the seizure. Since the Coolidge car was parked on the defendant's driveway, the seizure of that automobile required an entry upon private property. Here, as in <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), the automobile was seized from a public place where access was not meaningfully restricted. This is, in fact, the ground upon which the <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> plurality opinion distinguished <i>Chambers,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 463</a></span> n. 20. See also <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#446" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 446-447</a></span> (1973).</p>
<p>In considering whether the lack of a warrant to seize a vehicle invalidates the otherwise legal examination of the car, <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> is highly pertinent. In <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> four men in an automobile were arrested shortly after an armed robbery. The Court concluded that there was probable cause to arrest and probable cause to search the vehicle. The car was taken from the highway to <span class="star-pagination">*594</span> the police station where, some time later, a search producing incriminating evidence, was conducted. We stated:</p>
<blockquote>"For constitutional purposes, we see no difference between on the one hand seizing and holding a car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant. Given probable cause to search, either course is reasonable under the Fourth Amendment.</blockquote>
<blockquote>". . . The probable-cause factor still obtained at the station house and so did the mobility of the car unless the Fourth Amendment permits a warrantless seizure of the car and the denial of its use to anyone until a warrant is secured. In that event there is little to choose in terms of practical consequences between an immediate search without a warrant and the car's immobilization until a warrant is obtained." <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 52</a></span>.</blockquote>
<p>The fact that the car in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> was seized after being stopped on a highway, whereas Lewis' car was seized from a public parking lot, has little, if any, legal significance.<sup>[10]</sup> The same arguments and considerations of exigency, immobilization on the spot, and posting a <span class="star-pagination">*595</span> guard obtain. In fact, because the interrogation session ended with awareness that Lewis had been arrested and that his car constituted incriminating evidence, the incentive and potential for the car's removal substantially increased. There was testimony at the federal hearing that Lewis asked one of his attorneys to see that his wife and family got the car, and that the attorney relinquished the keys to the police in order to avoid a physical confrontation. <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/#33" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp., at 33</a></span>. In <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> all occupants of the car were in custody and there were no means of relating this fact or the location of the car (if it had not been impounded) to a friend or confederate. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> also stated that a search of the car on the spot was impractical because it was dark and the search could not be carefully executed. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 52</a></span> n. 10. Here too, the seizure facilitated the type of close examination necessary.<sup>[11]</sup></p>
<p>Respondent contends that here, unlike <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> probable cause to search the car existed for some time prior to arrest and that, therefore, there were no exigent circumstances. Assuming that probable cause previously existed, we know of no case or principle that suggests that the right to search on probable cause and the reasonableness of seizing a car under exigent circumstances are foreclosed if a warrant was not obtained at the first practicable moment. Exigent circumstances with regard to vehicles are not limited to situations where probable cause is unforeseeable and arises only at the time of arrest. Cf. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#50" aria-description="Citation for case: Chambers v. Maroney"><i>Chambers, id.,</i> at 50-51</a></span>. The exigency may arise at any time, and the fact that the police might have obtained <span class="star-pagination">*596</span> a warrant earlier does not negate the possibility of a current situation's necessitating prompt police action.<sup>[12]</sup></p>
<p>The judgment of the Court of Appeals is reversed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE POWELL, concurring in the result.</p>
<p>I would reverse the judgment of the Court of Appeals for the reasons set forth in my concurring opinion in <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#250" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 250</a></span> (1973). As stated therein, I would hold that "federal collateral review of a state prisoner's Fourth Amendment claims claims which rarely bear on innocenceshould be confined solely to the question of whether the petitioner [for habeas corpus] was provided a fair opportunity to raise and have adjudicated the question in state courts." <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Ibid.</a></span></i> In this case there is no contention that respondent was denied a full and fair opportunity to litigate his claim in the state courts.</p>
<p>MR. JUSTICE STEWART, with whom MR. JUSTICE DOUGLAS, MR. JUSTICE BRENNAN, and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>The most fundamental rule in this area of constitutional law is that "searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendment subject only to a few specifically established and well-delineated exceptions." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>; <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span>. See also <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span>. Since there was no warrant authorizing <span class="star-pagination">*597</span> the search and seizure in this case, and since none of the "specifically established and well-delineated exceptions" to the warrant requirement here existed, I am convinced the judgment of the Court of Appeals must be affirmed.<sup>[1]</sup></p>
<p>In casting about for some way to avoid the impact of our previous decisions, the plurality opinion first suggests, <i>ante,</i> at 588-589, that no "search" really took place in this case, since all that the police did was to scrape paint from the respondent's car and make observations of its tires. Whatever merit this argument might possess in the abstract, it is irrelevant in the circumstances disclosed by this record. The argument is irrelevant for the simple reason that the police, before taking the paint scrapings and looking at the tires, first took possession of the car itself. The Fourth and Fourteenth Amendments protect against "unreasonable searches and <i>seizures,</i>" and there most assuredly was a seizure here.</p>
<p>The plurality opinion next seems to suggest that the basic constitutional rule can be overlooked in this case because the subject of the seizure was an automobile. It is true, of course, that a line of decisions, beginning with <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, have recognized a so-called "automobile exception" to the constitutional requirement of a warrant. But "[t]he word `automobile' is not a talisman in whose presence the Fourth Amendment fades away and disappears." <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#461" aria-description="Citation for case: Coolidge v. New Hampshire"><i>Coolidge, supra,</i> at 461-462</a></span>. Rather, the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine simply recognizes the obviousthat a <i>moving</i> automobile on the open road presents a situation "where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the <span class="star-pagination">*598</span> warrant must be sought." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States"><i>Carroll, supra,</i> at 153</a></span>. See also <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#269" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 269</a></span>. Where there is no reasonable likelihood that the automobile would or could be moved, the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine is simply inapplicable. See, <i>e. g., <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge, supra;</a></span> </i><i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>.</p>
<p>The facts of this case make clear beyond peradventure that the "automobile exception" is not available to uphold the warrantless seizure of the respondent's car. Well before the time that the automobile was seized, the respondentand the keys to his carwere securely within police custody. There was thus absolutely no likelihood that the respondent could have either moved the car or meddled with it during the time necessary to obtain a search warrant. And there was no realistic possibility that anyone else was in a position to do so either. I am at a loss, therefore, to understand the plurality opinion's conclusion, <i>ante,</i> at 595, that there was a "potential for the car's removal" during the period immediately preceding the car's seizure. The facts of record can only support a diametrically opposite conclusion.</p>
<p>Finally, the plurality opinion suggests that other "exigent circumstances" might have excused the failure of the police to procure a warrant. The opinion nowhere states what these mystical exigencies might have been, and counsel for the petitioner has not been so inventive as to suggest any.<sup>[2]</sup> Since the authorities had taken care to procure an arrest warrant even before the respondent <span class="star-pagination">*599</span> arrived for questioning, it can scarcely be said that probable cause was not discovered until so late a point in time as to prevent the obtaining of a warrant for seizure of the automobile. And, with the automobile effectively immobilized during the period of the respondent's interrogation, the fear that evidence might be destroyed was hardly an exigency, particularly when it is remembered that no such fear prompted a seizure during all the preceding months while the respondent, though under investigation, had been in full control of the car.<sup>[3]</sup> This is, quite simply, a case where no exigent circumstances existed.<sup>[4]</sup></p>
<p>Until today it has been clear that "[n]either <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> . . . nor other cases in this Court require or suggest that in every conceivable circumstance the search of an auto even with probable cause may be made without the extra protection for privacy that a warrant affords." <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#50" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 50</a></span>. I would follow the settled constitutional law established in our decisions and affirm the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[1]  The arrest warrant was obtained in Delaware County, where the crime was committed. The Activities Office is in adjacent Franklin County. In Ohio, an arrest warrant may be served in any county of the State. <span class="citation no-link">Ohio Rev. Code Ann. § 2941.36</span> (1953). In contrast, a search warrant in Ohio may be issued by a judge or magistrate only "within his jurisdiction." <span class="citation no-link">Ohio Rev. Code Ann. § 2933.21</span> (Supp. 1972). Thus, a search warrant obtained in Delaware County is not valid in Franklin County.</p>
<p>[2]  The call was made at about 9:30 a. m. on July 19 by a man who identified himself to Mrs. Smith as Radcliffe and who stated that the books were in "A-1 condition." Mrs. Smith, who knew the victim, did not identify the caller as Radcliffe. Gunshots were heard between 8 a. m. and 8:30 a. m. that day by two women who lived near the site of the crime. It thus became clear that someone had impersonated Radcliffe in making the telephone call.</p>
<p>[3]  The calendar's page for July 19 was missing. Investigation disclosed a writing indentation, on the next and underlying page for July 20, which indicated what had been written on the page for July 19.</p>
<p>[4]  Apparently, the car's trunk was also opened and a tire in the trunk was observed. <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/#33" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp. 26, 33</a></span>; <span class="citation" data-id="310138"><a href="/opinion/310138/arthur-ben-lewis-jr-v-harold-j-cardwell-warden/#468" aria-description="Citation for case: Arthur Ben Lewis, Jr. v. Harold J. Cardwell, Warden">476 F. 2d 467, 468</a></span>. No evidence obtained from any part of the interior of the vehicle, however, was introduced.</p>
<p>[5]  The Court there discussed the following post-<i>Carroll</i> cases: <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931); <i>Scher</i> v. <i>United States,</i> <span class="citation" data-id="103100"><a href="/opinion/103100/scher-v-united-states/" aria-description="Citation for case: Scher v. United States">305 U. S. 251</a></span> (1938); <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949); <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964); <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967); <i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span> (1968). Cases decided since <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> and that now might be added to the list include <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973). See also <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968); Note, Warrantless Searches and Seizures of Automobiles, <span class="citation no-link">87 Harv. L. Rev. 835</span> (1974).</p>
<p>[6]  Petitioner contends that Lewis' car keys and the parking lot claim check were seized in plain view as an incident to his arrest, and that this seizure served to transfer constructive possession of the vehicle which could then be searched and seized as an instrumentality of the crime. We feel that the District Court and the Court of Appeals were correct in rejecting this argument. Irrespective of the plain-view or instrumentality analyses, the concept of constructive possession has not been found to justify the search or seizure of an item not in actual possession.</p>
<p>[7]  As has been noted, the arrest was made at the Office of the Division of Criminal Activities; but the examination of the vehicle took place some time later at the police impoundment lot. This difference in time and place eliminates any search-incident-to-an-arrest contention.
</p>
<p>"The rule allowing contemporaneous searches is justified, for example, by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crimethings which might easily happen where the weapon or evidence is on the accused's person or under his immediate control. But these justifications are absent where a search is remote in time or place from the arrest. Once an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest." <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964).</p>
<p>See also <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#47" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 47</a></span> (1970).</p>
<p>[8]  Again, we are not confronted with any issue as to the propriety of a search of a car's interior. "Neither <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span></i> nor other cases in this Court require or suggest that in every conceivable circumstance the search of an auto even with probable cause may be made without the extra protection for privacy that a warrant affords." <i>Id.,</i> at 50.</p>
<p>[9]  <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> concerned a thorough and extensive search of the entire automobile including the interior from which, by vacuum sweepings, incriminating evidence was obtained. A search of that kind raises different and additional considerations not present in the examination of a tire on an operative wheel and in the taking of exterior paint samples from the vehicle in the present case for which there was no reasonable expectation of privacy.</p>
<p>[10]  Before the District Court, the State argued that Lewis had consented to the seizure of his car by requesting that the police impound it for safekeeping. The District Court stated:
</p>
<p>"Viewing the evidence in the light most favorable to the State, petitioner [Lewis] did not clearly and unequivocally consent to the seizure and search of the automobile. The testimony . . . established, at most, that petitioner consented to their taking custody of the car for safekeeping. There is no evidence that petitioner consented, expressly or impliedly, to a seizure of the automobile for purposes of a search. . . ." <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/#37" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp., at 37-38</a></span>.</p>
<p>Inasmuch as we hold the seizure to be justified under <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> we do not reach the issue of Lewis' consent.</p>
<p>[11]  To make a comparison with a paint scraping required that a section of the painted exterior that had not been recently repaired be sampled. This conceivably could necessitate several scrapings if the first sample was not conclusive after laboratory analysis. Similarly, to make a cast of the tire tread on the operative wheel would require laboratory equipment.</p>
<p>[12]  We do not address the question found to be determinative in MR. JUSTICE POWELL's opinion concurring in the result. This question was not raised or briefed by the parties.</p>
<p>[1]  This dissent is directed toward the search-and-seizure analysis in MR. JUSTICE BLACKMUN's plurality opinion. Like the plurality, I do not consider the issue raised by MR. JUSTICE POWELL's concurrence, it having been neither briefed nor argued by the parties.</p>
<p>[2]  Even the Solicitor General, who appeared as <i>amicus curiae</i> urging a reversal of the Court of Appeals' judgment in this case, has candidly admitted in his brief that "no satisfactory reason appears for the failure of the law enforcement officers to have obtained a warrant there appears on the facts of this case to have been no real likelihood that respondent would have destroyed or concealed the evidence sought during the time required to seek and procure a warrant." Brief for United States as <i>Amicus Curiae</i> 4-5.</p>
<p>[3]  It can hardly be argued that the questioning of the respondent by the police for the first time alerted him to their intentions, thus suddenly providing him a motivation to remove the car from "official grasp." <i>Ante,</i> at 590, 595. Even putting to one side the question of how the respondent could have acted to destroy any evidence while he was in police custody, the fact is that he was fully aware of official suspicion during several months preceding the interrogation. He had been questioned on several occasions prior to his arrest, and he had been alerted on the day before the interrogation that the police wished to see him. Nonetheless, he voluntarily drove his car to Columbus to keep his appointment with the investigators.</p>
<p>[4]  The plurality opinion correctly rejects, <i>ante,</i> at 591-592, n. 7, the petitioner's contention that the seizure here was incident to the arrest of the respondent. "Once an accused is under arrest and in custody, then a search made at another place, without a warrant; is simply not incident to the arrest." <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span>.</p>

</div>
```

---

## GROUP: content/cases/Carpenter v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Carpenter v. United States"
type: case
citation: "585 U.S. 296 (2018)"
parallel_cite: "138 S. Ct. 2206; 201 L. Ed. 2d 507"
neutral_cite: 2018 U.S. LEXIS 3844
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-06-22
docket: 16-402
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2018-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Carpenter v. United States
  varies_by_point: false
  scope_note: "Carpenter itself narrows the third-party doctrine for digital-age location data; it is good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4510032/carpenter-v-united-states/"
  cluster_id: 4510032
  opinion_id: 4287285
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Key — CSLI dividing line (co-home, A6)"
related: ["[[United States v. Jones]]", "[[Katz v. United States]]", "[[Smith v. Maryland]]", "[[Riley v. California]]", "[[Chatrie v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "digital-privacy", "cell-site", "third-party-doctrine"]
holding: "Acquiring extended historical cell-site location information is a search — a reasonable expectation of privacy in 'the whole of [one's] physical movements'; narrows the third-party doctrine for digital-age data."
lake:
  record_id: Carpenter v. United States
  status: verified
  projected_at: 2026-07-06
---

# Carpenter v. United States

*585 U.S. 296 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a series of armed robberies, the FBI obtained 127 days of Carpenter's historical cell-site location information (CSLI) from his wireless carriers under the Stored Communications Act, which required only "specific and articulable facts" — a showing short of probable cause — rather than a warrant. The records (nearly 12,900 location points) placed his phone near the robbery sites. He moved to suppress the CSLI as the product of a warrantless search.

## Issue
Whether the Government's acquisition of historical cell-site records that chronicle a person's past movements is a search under the Fourth Amendment.

## Rule
Yes. "Whether the Government employs its own surveillance technology as in *Jones* or leverages the technology of a wireless carrier, we hold that an individual maintains a legitimate expectation of privacy in the record of his physical movements as captured through CSLI." — *Carpenter v. United States*, 585 U.S. 296 (2018) (slip op., at 11). ^pin-op11

Because that acquisition is a search, the Government must generally obtain a warrant supported by probable cause before acquiring such records. The Court declined to extend the third-party doctrine of *[[Smith v. Maryland]]* and *[[United States v. Miller]]* to the "qualitatively different category of cell-site records."

## Application
The Government accessed 127 days of Carpenter's CSLI without a warrant, relying instead on a court order issued on less than probable cause. Because that data provided an all-encompassing, retrospective record of his whereabouts — "an intimate window into a person's life" — its acquisition invaded a legitimate expectation of privacy and was a search; on these facts the warrantless acquisition could not be justified by the third-party doctrine.

## Conclusion
Acquiring Carpenter's historical CSLI was a Fourth Amendment search; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. The Court's holding was expressly narrow, declining to disturb conventional surveillance techniques or other business records.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Carpenter* itself **narrows** the third-party doctrine ([[Smith v. Maryland]]) for digital-age location data and builds on the mosaic concern voiced in the [[United States v. Jones]] [[Common Legal Terms#concurring-opinion|concurrences]].
- **Extended (2026):** *[[Chatrie v. United States]]*, 609 U.S. ___ (2026), **applies and extends *Carpenter*** to bulk **geofence / Google Location History** data — holding its acquisition is a Fourth Amendment search even for a short (~2-hour) window and even though held by a third party (rejecting the opt-in/third-party rationale) — and leaves geofence-warrant probable cause/[[Particularity|particularity]] for remand. *Carpenter* remains good law and anchors that ruling.

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key — Progeny / Refinement*
- [[Third-Party Doctrine & CSLI]] — *Key — CSLI dividing line (co-home)*

## Sources
- *Carpenter v. United States*, 585 U.S. 296 (2018) — https://www.courtlistener.com/opinion/4510032/carpenter-v-united-states/ — pinpoint: slip op., at 11 (CL carries the slip opinion; cluster 4510032 → opinion 4287285).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2b84b01e040ee716", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "585 U.S. 296 (2018)", "court": "U.S. Supreme Court", "neutral_cite": "2018 U.S. LEXIS 3844", "official_citation_present": true, "parallel_cite": "138 S. Ct. 2206; 201 L. Ed. 2d 507", "title": "Carpenter v. United States", "year": "2018"}}
{"assertion_id": "35962f218af7ae7b", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Key — CSLI dividing line (co-home, A6)", "title": "Carpenter v. United States"}}
{"assertion_id": "83b328bcf623018f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Acquiring extended historical cell-site location information is a search — a reasonable expectation of privacy in 'the whole of [one's] physical movements'; narrows the third-party doctrine for digital-age data.", "title": "Carpenter v. United States"}}
{"assertion_id": "e477112e00353fa2", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Key — Progeny / Refinement", "title": "Carpenter v. United States"}}
{"assertion_id": "2417aaf56bf96977", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Carpenter v. United States"}}
{"assertion_id": "80af5b78319ed83a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2018-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Carpenter v. United States", "field_i_validity": "good_law", "scope_note": "Carpenter itself narrows the third-party doctrine for digital-age location data; it is good law.", "title": "Carpenter v. United States", "varies_by_point": "false"}}
```

### lake record — Carpenter v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Carpenter v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Carpenter v. United States",
    "case_name_short": "Carpenter",
    "case_name_full": "",
    "input_case_name": "Carpenter v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-06-22",
    "year": 2018,
    "docket": "16-402",
    "cluster_id": 4510032,
    "lead_opinion_id": 4287285,
    "sibling_ids": [
      4287285
    ],
    "absolute_url": "/opinion/4510032/carpenter-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4512666,
        "score": 20,
        "case_name": "Carpenter v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "585 U.S. 296",
      "volume": "585",
      "reporter": "U.S.",
      "page": "296",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 2206",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "2206",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 507",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "507",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 3844",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3844",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "585 U.S. 296",
        "volume": "585",
        "reporter": "U.S.",
        "page": "296",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 2206",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "2206",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 507",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "507",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 3844",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3844",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "585 U.S. 296",
    "official_selection": {
      "court_class": "scotus",
      "selected": "585 U.S. 296",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op11",
      "page": null,
      "quote": "\u2014 a showing short of probable cause \u2014 rather than a warrant. The records (nearly 12,900 location points) placed his phone near the robbery sites. He moved to suppress the CSLI as the product of a warrantless search. ## Issue Whether the Government's acquisition of historical cell-site records that chronicle a person's past movements is a search under the Fourth Amendment. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Carpenter v. United States",
    "varies_by_point": false,
    "scope_note": "Carpenter itself narrows the third-party doctrine for digital-age location data; it is good law.",
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
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Von Harris",
          "cluster_id": 10324088,
          "cite": [
            "2025 Ohio 279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Devin J. Johnson",
          "cluster_id": 10132115,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas v. State",
          "cluster_id": 10680321,
          "cite": [
            "902 S.E.2d 566",
            "319 Ga. 123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Singleton",
          "cluster_id": 9506618,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Janvier",
          "cluster_id": 9494606,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jamin Kidron Stocker v. the State of Texas",
          "cluster_id": 9329108,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hoffman",
          "cluster_id": 10135310,
          "cite": [
            "321 Or. App. 330",
            "515 P.3d 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
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
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "v. Thompson",
          "cluster_id": 4858089,
          "cite": [
            "2021 CO 15"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Perrin Davis v. Facebook, Inc.",
          "cluster_id": 4743751,
          "cite": [
            "956 F.3d 589"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caro",
          "cluster_id": 4629272,
          "cite": [
            "248 Cal. Rptr. 3d 96",
            "7 Cal. 5th 463",
            "442 P.3d 316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matthew Jones",
          "cluster_id": 4757714,
          "cite": [
            "960 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North American Butterfly Association v. Chad F. Wolf",
          "cluster_id": 4795622,
          "cite": [
            "977 F.3d 1244"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eaglin",
          "cluster_id": 8443840,
          "cite": [
            "913 F.3d 88"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martinez",
          "cluster_id": 6243814,
          "cite": [
            "570 S.W.3d 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Kurtz, J.",
          "cluster_id": 10317095,
          "cite": [
            "294 A.3d 509",
            "2023 Pa. Super. 72"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
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
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leaders of Beautiful Struggle v. Baltimore Police Department",
          "cluster_id": 4894627,
          "cite": [
            "2 F.4th 330"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Troester v. Starbucks Corporation",
          "cluster_id": 4520879,
          "cite": [
            "235 Cal. Rptr. 3d 820",
            "5 Cal. 5th 829",
            "421 P.3d 1114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In the Matter of the Application of Jason Leopold to Unseal Certain Electronic Surveillance Applications and Orders",
          "cluster_id": 4766181,
          "cite": [
            "964 F.3d 1121"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Miller",
          "cluster_id": 4835528,
          "cite": [
            "982 F.3d 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kaufhold",
          "cluster_id": 4770908,
          "cite": [
            "2020 Ohio 3835"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trump v. Mazars USA, LLP",
          "cluster_id": 4766665,
          "cite": [
            "140 S. Ct. 2019",
            "207 L. Ed. 2d 951"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charlie L. Green",
          "cluster_id": 4833880,
          "cite": [
            "981 F.3d 945"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. State",
          "cluster_id": 10367330,
          "cite": [
            "850 S.E.2d 110",
            "310 Ga. 180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kelsey Rose Juliana v. United States",
          "cluster_id": 4707560,
          "cite": [
            "947 F.3d 1159"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Dunkins, A.",
          "cluster_id": 10315445,
          "cite": [
            "229 A.3d 622",
            "2020 Pa. Super. 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne Sheckles",
          "cluster_id": 4879211,
          "cite": [
            "996 F.3d 330"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kunz",
          "cluster_id": 9400913,
          "cite": [
            "68 F.4th 748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcus Walker",
          "cluster_id": 4861532,
          "cite": [
            "990 F.3d 316"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rex Hammond",
          "cluster_id": 4877368,
          "cite": [
            "996 F.3d 374"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George Young, Jr. v. State of Hawaii",
          "cluster_id": 4867182,
          "cite": [
            "992 F.3d 765"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eric K. Brooks v. D Miller",
          "cluster_id": 9421763,
          "cite": [
            "78 F.4th 1267"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4287285) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjQzNjczNjAwMDAwJnM9NjI0NzMxNCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%284287285%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(4287285)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMiZzPTEwMzgyNzc1JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%284287285%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4287285)",
        "reviewed": 178,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 178,
        "triage_read": 6,
        "triage_snippet_classified": 172
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4287285)",
    "indexed_citing_opinions": 525,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4287285,
        "count": 525,
        "count_source": "search"
      }
    ],
    "citation_count": 1207,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/carpenter-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNDgxMDUmcz0xMDU4MTk5OSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%284287285%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4287285,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 99422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 100047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 103990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 104239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 104758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 108713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 118148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 137006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 145633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 145777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 148797,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 149703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 158478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 181032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 612140,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 746807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 779290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 1087666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 1215380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 1440458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2443377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2513954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2680439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2789928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2812209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 3235330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 4181058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 4274911,
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
    "date_created": "2026-07-04T23:36:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:36:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:36:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:40:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:36:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Carpenter v. United States (truncated)

```
(Slip Opinion)              OCTOBER TERM, 2017                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                 CARPENTER v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE SIXTH CIRCUIT

   No. 16–402.      Argued November 29, 2017—Decided June 22, 2018
Cell phones perform their wide and growing variety of functions by con-
  tinuously connecting to a set of radio antennas called “cell sites.”
  Each time a phone connects to a cell site, it generates a time-stamped
  record known as cell-site location information (CSLI). Wireless carri-
  ers collect and store this information for their own business purposes.
  Here, after the FBI identified the cell phone numbers of several rob-
  bery suspects, prosecutors were granted court orders to obtain the
  suspects’ cell phone records under the Stored Communications Act.
  Wireless carriers produced CSLI for petitioner Timothy Carpenter’s
  phone, and the Government was able to obtain 12,898 location points
  cataloging Carpenter’s movements over 127 days—an average of 101
  data points per day. Carpenter moved to suppress the data, arguing
  that the Government’s seizure of the records without obtaining a
  warrant supported by probable cause violated the Fourth Amend-
  ment. The District Court denied the motion, and prosecutors used
  the records at trial to show that Carpenter’s phone was near four of
  the robbery locations at the time those robberies occurred. Carpen-
  ter was convicted. The Sixth Circuit affirmed, holding that Carpen-
  ter lacked a reasonable expectation of privacy in the location infor-
  mation collected by the FBI because he had shared that information
  with his wireless carriers.
Held:
    1. The Government’s acquisition of Carpenter’s cell-site records
 was a Fourth Amendment search. Pp. 4–18.
       (a) The Fourth Amendment protects not only property interests
 but certain expectations of privacy as well. Katz v. United States, 389
 U. S. 347, 351. Thus, when an individual “seeks to preserve some-
 thing as private,” and his expectation of privacy is “one that society is
2                   CARPENTER v. UNITED STATES

                                  Syllabus

    prepared to recognize as reasonable,” official intrusion into that
    sphere generally qualifies as a search and requires a warrant sup-
    ported by probable cause. Smith v. Maryland, 442 U. S. 735, 740 (in-
    ternal quotation marks and alterations omitted). The analysis re-
    garding which expectations of privacy are entitled to protection is
    informed by historical understandings “of what was deemed an un-
    reasonable search and seizure when [the Fourth Amendment] was
    adopted.” Carroll v. United States, 267 U. S. 132, 149. These Found-
    ing-era understandings continue to inform this Court when applying
    the Fourth Amendment to innovations in surveillance tools. See, e.g.,
    Kyllo v. United States, 533 U. S. 27. Pp. 4–7.
         (b) The digital data at issue—personal location information
    maintained by a third party—does not fit neatly under existing prec-
    edents but lies at the intersection of two lines of cases. One set ad-
    dresses a person’s expectation of privacy in his physical location and
    movements. See, e.g., United States v. Jones, 565 U. S. 400 (five Jus-
    tices concluding that privacy concerns would be raised by GPS track-
    ing). The other addresses a person’s expectation of privacy in infor-
    mation voluntarily turned over to third parties. See United States v.
    Miller, 425 U. S. 435 (no expectation of privacy in financial records
    held by a bank), and Smith, 442 U. S. 735 (no expectation of privacy
    in records of dialed telephone numbers conveyed to telephone compa-
    ny). Pp. 7–10.
         (c) Tracking a person’s past movements through CSLI partakes
    of many of the qualities of GPS monitoring considered in Jones—it is
    detailed, encyclopedic, and effortlessly compiled. At the same time,
    however, the fact that the individual continuously reveals his loca-
    tion to his wireless carrier implicates the third-party principle of
    Smith and Miller. Given the unique nature of cell-site records, this
    Court declines to extend Smith and Miller to cover them. Pp. 10–18.
            (1) A majority of the Court has already recognized that indi-
    viduals have a reasonable expectation of privacy in the whole of their
    physical movements. Allowing government access to cell-site rec-
    ords—which “hold for many Americans the ‘privacies of life,’ ” Riley v.
    California, 573 U. S. ___, ___—contravenes that expectation. In fact,
    historical cell-site records present even greater privacy concerns than
    the GPS monitoring considered in Jones: They give the Government
    near perfect surveillance and allow it to travel back in time to retrace
    a person’s whereabouts, subject only to the five-year retention poli-
    cies of most wireless carriers. The Government contends that CSLI
    data is less precise than GPS information, but it thought the data ac-
    curate enough here to highlight it during closing argument in Car-
    penter’s trial. At any rate, the rule the Court adopts “must take ac-
    count of more sophisticated systems that are already in use or in
                   Cite as: 585 U. S. ____ (2018)                    3

                              Syllabus

development,” Kyllo, 533 U. S., at 36, and the accuracy of CSLI is
rapidly approaching GPS-level precision. Pp. 12–15.
       (2) The Government contends that the third-party doctrine
governs this case, because cell-site records, like the records in Smith
and Miller, are “business records,” created and maintained by wire-
less carriers. But there is a world of difference between the limited
types of personal information addressed in Smith and Miller and the
exhaustive chronicle of location information casually collected by
wireless carriers.
   The third-party doctrine partly stems from the notion that an indi-
vidual has a reduced expectation of privacy in information knowingly
shared with another. Smith and Miller, however, did not rely solely
on the act of sharing. They also considered “the nature of the partic-
ular documents sought” and limitations on any “legitimate ‘expecta-
tion of privacy’ concerning their contents.” Miller, 425 U. S., at 442.
In mechanically applying the third-party doctrine to this case the
Government fails to appreciate the lack of comparable limitations on
the revealing nature of CSLI.
   Nor does the second rationale for the third-party doctrine—
voluntary exposure—hold up when it comes to CSLI. Cell phone lo-
cation information is not truly “shared” as the term is normally un-
derstood. First, cell phones and the services they provide are “such a
pervasive and insistent part of daily life” that carrying one is indis-
pensable to participation in modern society. Riley, 573 U. S., at ___.
Second, a cell phone logs a cell-site record by dint of its operation,
without any affirmative act on the user’s part beyond powering up.
Pp. 15–17.
     (d) This decision is narrow. It does not express a view on matters
not before the Court; does not disturb the application of Smith and
Miller or call into question conventional surveillance techniques and
tools, such as security cameras; does not address other business rec-
ords that might incidentally reveal location information; and does not
consider other collection techniques involving foreign affairs or na-
tional security. Pp. 17–18.
   2. The Government did not obtain a warrant supported by proba-
ble cause before acquiring Carpenter’s cell-site records. It acquired
those records pursuant to a court order under the Stored Communi-
cations Act, which required the Government to show “reasonable
grounds” for believing that the records were “relevant and material to
an ongoing investigation.” 18 U. S. C. §2703(d). That showing falls
well short of the probable cause required for a warrant. Consequent-
ly, an order issued under §2703(d) is not a permissible mechanism for
accessing historical cell-site records. Not all orders compelling the
production of documents will require a showing of probable cause. A
4                  CARPENTER v. UNITED STATES

                                 Syllabus

    warrant is required only in the rare case where the suspect has a le-
    gitimate privacy interest in records held by a third party. And even
    though the Government will generally need a warrant to access
    CSLI, case-specific exceptions—e.g., exigent circumstances—may
    support a warrantless search. Pp. 18–22.
819 F. 3d 880, reversed and remanded.

   ROBERTS, C. J., delivered the opinion of the Court, in which GINS-
BURG,  BREYER, SOTOMAYOR, and KAGAN, JJ., joined. KENNEDY, J., filed a
dissenting opinion, in which THOMAS and ALITO, JJ., joined. THOMAS, J.,
filed a dissenting opinion. ALITO, J., filed a dissenting opinion, in which
THOMAS, J., joined. GORSUCH, J., filed a dissenting opinion.
                        Cite as: 585 U. S. ____ (2018)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 16–402
                                   _________________


    TIMOTHY IVORY CARPENTER, PETITIONER v.

               UNITED STATES

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                                 [June 22, 2018] 


  CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
  This case presents the question whether the Govern-
ment conducts a search under the Fourth Amendment
when it accesses historical cell phone records that provide
a comprehensive chronicle of the user’s past movements.
                               I

                               A

   There are 396 million cell phone service accounts in the
United States—for a Nation of 326 million people. Cell
phones perform their wide and growing variety of func-
tions by connecting to a set of radio antennas called “cell
sites.” Although cell sites are usually mounted on a tower,
they can also be found on light posts, flagpoles, church
steeples, or the sides of buildings. Cell sites typically have
several directional antennas that divide the covered area
into sectors.
   Cell phones continuously scan their environment look-
ing for the best signal, which generally comes from the
closest cell site.       Most modern devices, such as
smartphones, tap into the wireless network several times
2              CARPENTER v. UNITED STATES

                      Opinion of the Court

a minute whenever their signal is on, even if the owner is
not using one of the phone’s features. Each time the
phone connects to a cell site, it generates a time-stamped
record known as cell-site location information (CSLI). The
precision of this information depends on the size of the
geographic area covered by the cell site. The greater the
concentration of cell sites, the smaller the coverage area.
As data usage from cell phones has increased, wireless
carriers have installed more cell sites to handle the traffic.
That has led to increasingly compact coverage areas,
especially in urban areas.
  Wireless carriers collect and store CSLI for their own
business purposes, including finding weak spots in their
network and applying “roaming” charges when another
carrier routes data through their cell sites. In addition,
wireless carriers often sell aggregated location records to
data brokers, without individual identifying information of
the sort at issue here. While carriers have long retained
CSLI for the start and end of incoming calls, in recent
years phone companies have also collected location infor-
mation from the transmission of text messages and rou-
tine data connections. Accordingly, modern cell phones
generate increasingly vast amounts of increasingly precise
CSLI.
                              B
   In 2011, police officers arrested four men suspected of
robbing a series of Radio Shack and (ironically enough) T-
Mobile stores in Detroit. One of the men confessed that,
over the previous four months, the group (along with a
rotating cast of getaway drivers and lookouts) had robbed
nine different stores in Michigan and Ohio. The suspect
identified 15 accomplices who had participated in the
heists and gave the FBI some of their cell phone numbers;
the FBI then reviewed his call records to identify addi-
tional numbers that he had called around the time of the
                 Cite as: 585 U. S. ____ (2018)            3

                     Opinion of the Court

robberies.
   Based on that information, the prosecutors applied for
court orders under the Stored Communications Act to
obtain cell phone records for petitioner Timothy Carpenter
and several other suspects. That statute, as amended in
1994, permits the Government to compel the disclosure of
certain telecommunications records when it “offers specific
and articulable facts showing that there are reasonable
grounds to believe” that the records sought “are relevant
and material to an ongoing criminal investigation.” 18
U. S. C. §2703(d). Federal Magistrate Judges issued two
orders directing Carpenter’s wireless carriers—MetroPCS
and Sprint—to disclose “cell/site sector [information] for
[Carpenter’s] telephone[ ] at call origination and at call
termination for incoming and outgoing calls” during the
four-month period when the string of robberies occurred.
App. to Pet. for Cert. 60a, 72a. The first order sought 152
days of cell-site records from MetroPCS, which produced
records spanning 127 days. The second order requested
seven days of CSLI from Sprint, which produced two days
of records covering the period when Carpenter’s phone was
“roaming” in northeastern Ohio. Altogether the Govern-
ment obtained 12,898 location points cataloging Carpen-
ter’s movements—an average of 101 data points per day.
   Carpenter was charged with six counts of robbery and
an additional six counts of carrying a firearm during a
federal crime of violence. See 18 U. S. C. §§924(c), 1951(a).
Prior to trial, Carpenter moved to suppress the cell-site
data provided by the wireless carriers. He argued that the
Government’s seizure of the records violated the Fourth
Amendment because they had been obtained without a
warrant supported by probable cause. The District Court
denied the motion. App. to Pet. for Cert. 38a–39a.
   At trial, seven of Carpenter’s confederates pegged him
as the leader of the operation. In addition, FBI agent
Christopher Hess offered expert testimony about the cell-
4              CARPENTER v. UNITED STATES

                      Opinion of the Court

site data. Hess explained that each time a cell phone taps
into the wireless network, the carrier logs a time-stamped
record of the cell site and particular sector that were used.
With this information, Hess produced maps that placed
Carpenter’s phone near four of the charged robberies. In
the Government’s view, the location records clinched the
case: They confirmed that Carpenter was “right where the
. . . robbery was at the exact time of the robbery.” App.
131 (closing argument). Carpenter was convicted on all
but one of the firearm counts and sentenced to more than
100 years in prison.
    The Court of Appeals for the Sixth Circuit affirmed. 819
F. 3d 880 (2016). The court held that Carpenter lacked a
reasonable expectation of privacy in the location infor-
mation collected by the FBI because he had shared that
information with his wireless carriers. Given that cell
phone users voluntarily convey cell-site data to their
carriers as “a means of establishing communication,” the
court concluded that the resulting business records are not
entitled to Fourth Amendment protection. Id., at 888
(quoting Smith v. Maryland, 442 U. S. 735, 741 (1979)).
    We granted certiorari. 582 U. S. ___ (2017).
                             II

                             A

  The Fourth Amendment protects “[t]he right of the
people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.” The
“basic purpose of this Amendment,” our cases have recog-
nized, “is to safeguard the privacy and security of individ-
uals against arbitrary invasions by governmental offi-
cials.” Camara v. Municipal Court of City and County of
San Francisco, 387 U. S. 523, 528 (1967). The Founding
generation crafted the Fourth Amendment as a “response
to the reviled ‘general warrants’ and ‘writs of assistance’ of
the colonial era, which allowed British officers to rum-
                    Cite as: 585 U. S. ____ (2018)                  5

                        Opinion of the Court

mage through homes in an unrestrained search for evi-
dence of criminal activity.” Riley v. California, 573 U. S.
___, ___ (2014) (slip op., at 27). In fact, as John Adams
recalled, the patriot James Otis’s 1761 speech condemning
writs of assistance was “the first act of opposition to the
arbitrary claims of Great Britain” and helped spark the
Revolution itself. Id., at ___–___ (slip op., at 27–28) (quot-
ing 10 Works of John Adams 248 (C. Adams ed. 1856)).
   For much of our history, Fourth Amendment search
doctrine was “tied to common-law trespass” and focused on
whether the Government “obtains information by physi-
cally intruding on a constitutionally protected area.”
United States v. Jones, 565 U. S. 400, 405, 406, n. 3 (2012).
More recently, the Court has recognized that “property
rights are not the sole measure of Fourth Amendment
violations.” Soldal v. Cook County, 506 U. S. 56, 64
(1992). In Katz v. United States, 389 U. S. 347, 351 (1967),
we established that “the Fourth Amendment protects
people, not places,” and expanded our conception of the
Amendment to protect certain expectations of privacy as
well. When an individual “seeks to preserve something as
private,” and his expectation of privacy is “one that society
is prepared to recognize as reasonable,” we have held that
official intrusion into that private sphere generally quali-
fies as a search and requires a warrant supported by
probable cause. Smith, 442 U. S., at 740 (internal quota-
tion marks and alterations omitted).
   Although no single rubric definitively resolves which
expectations of privacy are entitled to protection,1 the
——————
  1 JUSTICE KENNEDY believes that there is such a rubric—the “proper-

ty-based concepts” that Katz purported to move beyond. Post, at 3
(dissenting opinion). But while property rights are often informative,
our cases by no means suggest that such an interest is “fundamental”
or “dispositive” in determining which expectations of privacy are
legitimate. Post, at 8–9. JUSTICE THOMAS (and to a large extent
JUSTICE GORSUCH) would have us abandon Katz and return to an
6                 CARPENTER v. UNITED STATES

                          Opinion of the Court

analysis is informed by historical understandings “of what
was deemed an unreasonable search and seizure when
[the Fourth Amendment] was adopted.” Carroll v. United
States, 267 U. S. 132, 149 (1925). On this score, our cases
have recognized some basic guideposts. First, that the
Amendment seeks to secure “the privacies of life” against
“arbitrary power.” Boyd v. United States, 116 U. S. 616,
630 (1886). Second, and relatedly, that a central aim of
the Framers was “to place obstacles in the way of a too
permeating police surveillance.” United States v. Di Re,
332 U. S. 581, 595 (1948).
  We have kept this attention to Founding-era under-
standings in mind when applying the Fourth Amendment
to innovations in surveillance tools. As technology has
enhanced the Government’s capacity to encroach upon
areas normally guarded from inquisitive eyes, this Court
has sought to “assure[ ] preservation of that degree of
privacy against government that existed when the Fourth
Amendment was adopted.” Kyllo v. United States, 533
U. S. 27, 34 (2001). For that reason, we rejected in Kyllo a
“mechanical interpretation” of the Fourth Amendment and
held that use of a thermal imager to detect heat radiating
from the side of the defendant’s home was a search. Id., at
35. Because any other conclusion would leave homeown-
ers “at the mercy of advancing technology,” we determined
that the Government—absent a warrant—could not capi-
talize on such new sense-enhancing technology to explore
——————
exclusively property-based approach. Post, at 1–2, 17–21 (THOMAS J.,
dissenting); post, at 6–9 (GORSUCH, J., dissenting). Katz of course
“discredited” the “premise that property interests control,” 389 U. S., at
353, and we have repeatedly emphasized that privacy interests do not
rise or fall with property rights, see, e.g., United States v. Jones, 565
U. S. 400, 411 (2012) (refusing to “make trespass the exclusive test”);
Kyllo v. United States, 533 U. S. 27, 32 (2001) (“We have since decou-
pled violation of a person’s Fourth Amendment rights from trespassory
violation of his property.”). Neither party has asked the Court to
reconsider Katz in this case.
                  Cite as: 585 U. S. ____ (2018)              7

                      Opinion of the Court

what was happening within the home. Ibid.
  Likewise in Riley, the Court recognized the “immense
storage capacity” of modern cell phones in holding that
police officers must generally obtain a warrant before
searching the contents of a phone. 573 U. S., at ___ (slip
op., at 17). We explained that while the general rule
allowing warrantless searches incident to arrest “strikes
the appropriate balance in the context of physical objects,
neither of its rationales has much force with respect to”
the vast store of sensitive information on a cell phone. Id.,
at ___ (slip op., at 9).
                                B
   The case before us involves the Government’s acquisi-
tion of wireless carrier cell-site records revealing the
location of Carpenter’s cell phone whenever it made or
received calls. This sort of digital data—personal location
information maintained by a third party—does not fit
neatly under existing precedents. Instead, requests for
cell-site records lie at the intersection of two lines of cases,
both of which inform our understanding of the privacy
interests at stake.
   The first set of cases addresses a person’s expectation of
privacy in his physical location and movements. In United
States v. Knotts, 460 U. S. 276 (1983), we considered the
Government’s use of a “beeper” to aid in tracking a vehicle
through traffic. Police officers in that case planted a
beeper in a container of chloroform before it was pur-
chased by one of Knotts’s co-conspirators. The officers
(with intermittent aerial assistance) then followed the
automobile carrying the container from Minneapolis to
Knotts’s cabin in Wisconsin, relying on the beeper’s signal
to help keep the vehicle in view. The Court concluded that
the “augment[ed]” visual surveillance did not constitute a
search because “[a] person traveling in an automobile on
public thoroughfares has no reasonable expectation of
8              CARPENTER v. UNITED STATES

                     Opinion of the Court

privacy in his movements from one place to another.” Id.,
at 281, 282. Since the movements of the vehicle and its
final destination had been “voluntarily conveyed to anyone
who wanted to look,” Knotts could not assert a privacy
interest in the information obtained. Id., at 281.
   This Court in Knotts, however, was careful to distin-
guish between the rudimentary tracking facilitated by the
beeper and more sweeping modes of surveillance. The
Court emphasized the “limited use which the government
made of the signals from this particular beeper” during a
discrete “automotive journey.” Id., at 284, 285. Signifi-
cantly, the Court reserved the question whether “different
constitutional principles may be applicable” if “twenty-four
hour surveillance of any citizen of this country [were]
possible.” Id., at 283–284.
   Three decades later, the Court considered more sophis-
ticated surveillance of the sort envisioned in Knotts and
found that different principles did indeed apply. In United
States v. Jones, FBI agents installed a GPS tracking de-
vice on Jones’s vehicle and remotely monitored the vehi-
cle’s movements for 28 days. The Court decided the case
based on the Government’s physical trespass of the vehi-
cle. 565 U. S., at 404–405. At the same time, five Justices
agreed that related privacy concerns would be raised by,
for example, “surreptitiously activating a stolen vehicle
detection system” in Jones’s car to track Jones himself, or
conducting GPS tracking of his cell phone. Id., at 426, 428
(ALITO, J., concurring in judgment); id., at 415
(SOTOMAYOR, J., concurring). Since GPS monitoring of a
vehicle tracks “every movement” a person makes in that
vehicle, the concurring Justices concluded that “longer
term GPS monitoring in investigations of most offenses
impinges on expectations of privacy”—regardless whether
those movements were disclosed to the public at large.
Id., at 430 (opinion of ALITO, J.); id., at 415 (opinion of
                      Cite as: 585 U. S. ____ (2018)                      9

                           Opinion of the Court

SOTOMAYOR, J.).2
  In a second set of decisions, the Court has drawn a line
between what a person keeps to himself and what he
shares with others. We have previously held that “a per-
son has no legitimate expectation of privacy in information
he voluntarily turns over to third parties.” Smith, 442
U. S., at 743–744. That remains true “even if the infor-
mation is revealed on the assumption that it will be used
only for a limited purpose.” United States v. Miller, 425
U. S. 435, 443 (1976). As a result, the Government is
typically free to obtain such information from the recipient
without triggering Fourth Amendment protections.
  This third-party doctrine largely traces its roots to
Miller. While investigating Miller for tax evasion, the
Government subpoenaed his banks, seeking several
months of canceled checks, deposit slips, and monthly
statements. The Court rejected a Fourth Amendment
challenge to the records collection. For one, Miller could
“assert neither ownership nor possession” of the docu-
ments; they were “business records of the banks.” Id., at
440. For another, the nature of those records confirmed
Miller’s limited expectation of privacy, because the checks
were “not confidential communications but negotiable
instruments to be used in commercial transactions,” and
the bank statements contained information “exposed to
——————
  2 JUSTICE KENNEDY argues that this case is in a different category

from Jones and the dragnet-type practices posited in Knotts because the
disclosure of the cell-site records was subject to “judicial authorization.”
Post, at 14–16. That line of argument conflates the threshold question
whether a “search” has occurred with the separate matter of whether
the search was reasonable. The subpoena process set forth in the
Stored Communications Act does not determine a target’s expectation
of privacy. And in any event, neither Jones nor Knotts purported to
resolve the question of what authorization may be required to conduct
such electronic surveillance techniques. But see Jones, 565 U. S., at
430 (ALITO, J., concurring in judgment) (indicating that longer term
GPS tracking may require a warrant).
10             CARPENTER v. UNITED STATES

                     Opinion of the Court

[bank] employees in the ordinary course of business.” Id.,
at 442. The Court thus concluded that Miller had “take[n]
the risk, in revealing his affairs to another, that the in-
formation [would] be conveyed by that person to the Gov-
ernment.” Id., at 443.
  Three years later, Smith applied the same principles in
the context of information conveyed to a telephone com-
pany. The Court ruled that the Government’s use of a pen
register—a device that recorded the outgoing phone num-
bers dialed on a landline telephone—was not a search.
Noting the pen register’s “limited capabilities,” the Court
“doubt[ed] that people in general entertain any actual
expectation of privacy in the numbers they dial.” 442
U. S., at 742. Telephone subscribers know, after all, that
the numbers are used by the telephone company “for a
variety of legitimate business purposes,” including routing
calls. Id., at 743. And at any rate, the Court explained,
such an expectation “is not one that society is prepared to
recognize as reasonable.” Ibid. (internal quotation marks
omitted). When Smith placed a call, he “voluntarily con-
veyed” the dialed numbers to the phone company by “ex-
pos[ing] that information to its equipment in the ordinary
course of business.” Id., at 744 (internal quotation marks
omitted). Once again, we held that the defendant “as-
sumed the risk” that the company’s records “would be
divulged to police.” Id., at 745.
                            III
  The question we confront today is how to apply the
Fourth Amendment to a new phenomenon: the ability to
chronicle a person’s past movements through the record of
his cell phone signals. Such tracking partakes of many of
the qualities of the GPS monitoring we considered in
Jones. Much like GPS tracking of a vehicle, cell phone
location information is detailed, encyclopedic, and effort-
lessly compiled.
                     Cite as: 585 U. S. ____ (2018)                    11

                          Opinion of the Court

   At the same time, the fact that the individual continu-
ously reveals his location to his wireless carrier implicates
the third-party principle of Smith and Miller. But while
the third-party doctrine applies to telephone numbers and
bank records, it is not clear whether its logic extends to
the qualitatively different category of cell-site records.
After all, when Smith was decided in 1979, few could have
imagined a society in which a phone goes wherever its
owner goes, conveying to the wireless carrier not just
dialed digits, but a detailed and comprehensive record of
the person’s movements.
   We decline to extend Smith and Miller to cover these
novel circumstances. Given the unique nature of cell
phone location records, the fact that the information is
held by a third party does not by itself overcome the user’s
claim to Fourth Amendment protection. Whether the
Government employs its own surveillance technology as in
Jones or leverages the technology of a wireless carrier, we
hold that an individual maintains a legitimate expectation
of privacy in the record of his physical movements as
captured through CSLI. The location information ob-
tained from Carpenter’s wireless carriers was the product
of a search.3

——————
  3 The parties suggest as an alternative to their primary submissions

that the acquisition of CSLI becomes a search only if it extends beyond
a limited period. See Reply Brief 12 (proposing a 24-hour cutoff); Brief
for United States 55–56 (suggesting a seven-day cutoff). As part of its
argument, the Government treats the seven days of CSLI requested
from Sprint as the pertinent period, even though Sprint produced only
two days of records. Brief for United States 56. Contrary to JUSTICE
KENNEDY’s assertion, post, at 19, we need not decide whether there is a
limited period for which the Government may obtain an individual’s
historical CSLI free from Fourth Amendment scrutiny, and if so, how
long that period might be. It is sufficient for our purposes today to hold
that accessing seven days of CSLI constitutes a Fourth Amendment
search.
12             CARPENTER v. UNITED STATES

                     Opinion of the Court

                              A
   A person does not surrender all Fourth Amendment
protection by venturing into the public sphere. To the
contrary, “what [one] seeks to preserve as private, even in
an area accessible to the public, may be constitutionally
protected.” Katz, 389 U. S., at 351–352. A majority of this
Court has already recognized that individuals have a
reasonable expectation of privacy in the whole of their
physical movements. Jones, 565 U. S., at 430 (ALITO, J.,
concurring in judgment); id., at 415 (SOTOMAYOR, J.,
concurring). Prior to the digital age, law enforcement
might have pursued a suspect for a brief stretch, but doing
so “for any extended period of time was difficult and costly
and therefore rarely undertaken.” Id., at 429 (opinion of
ALITO, J.). For that reason, “society’s expectation has
been that law enforcement agents and others would not—
and indeed, in the main, simply could not—secretly moni-
tor and catalogue every single movement of an individual’s
car for a very long period.” Id., at 430.
   Allowing government access to cell-site records contra-
venes that expectation. Although such records are gener-
ated for commercial purposes, that distinction does not
negate Carpenter’s anticipation of privacy in his physical
location. Mapping a cell phone’s location over the course
of 127 days provides an all-encompassing record of the
holder’s whereabouts. As with GPS information, the time-
stamped data provides an intimate window into a person’s
life, revealing not only his particular movements, but
through them his “familial, political, professional, reli-
gious, and sexual associations.” Id., at 415 (opinion of
SOTOMAYOR, J.). These location records “hold for many
Americans the ‘privacies of life.’ ” Riley, 573 U. S., at ___
(slip op., at 28) (quoting Boyd, 116 U. S., at 630). And like
GPS monitoring, cell phone tracking is remarkably easy,
cheap, and efficient compared to traditional investigative
tools. With just the click of a button, the Government can
                  Cite as: 585 U. S. ____ (2018)            13

                      Opinion of the Court

access each carrier’s deep repository of historical location
information at practically no expense.
   In fact, historical cell-site records present even greater
privacy concerns than the GPS monitoring of a vehicle we
considered in Jones. Unlike the bugged container in
Knotts or the car in Jones, a cell phone—almost a “feature
of human anatomy,” Riley, 573 U. S., at ___ (slip op., at
9)—tracks nearly exactly the movements of its owner.
While individuals regularly leave their vehicles, they
compulsively carry cell phones with them all the time. A
cell phone faithfully follows its owner beyond public thor-
oughfares and into private residences, doctor’s offices,
political headquarters, and other potentially revealing
locales. See id., at ___ (slip op., at 19) (noting that “nearly
three-quarters of smart phone users report being within
five feet of their phones most of the time, with 12% admit-
ting that they even use their phones in the shower”);
contrast Cardwell v. Lewis, 417 U. S. 583, 590 (1974)
(plurality opinion) (“A car has little capacity for escaping
public scrutiny.”). Accordingly, when the Government
tracks the location of a cell phone it achieves near perfect
surveillance, as if it had attached an ankle monitor to the
phone’s user.
   Moreover, the retrospective quality of the data here
gives police access to a category of information otherwise
unknowable. In the past, attempts to reconstruct a per-
son’s movements were limited by a dearth of records and
the frailties of recollection. With access to CSLI, the
Government can now travel back in time to retrace a
person’s whereabouts, subject only to the retention polices
of the wireless carriers, which currently maintain records
for up to five years. Critically, because location infor-
mation is continually logged for all of the 400 million
devices in the United States—not just those belonging to
persons who might happen to come under investigation—
this newfound tracking capacity runs against everyone.
14             CARPENTER v. UNITED STATES

                     Opinion of the Court

Unlike with the GPS device in Jones, police need not even
know in advance whether they want to follow a particular
individual, or when.
   Whoever the suspect turns out to be, he has effectively
been tailed every moment of every day for five years, and
the police may—in the Government’s view—call upon the
results of that surveillance without regard to the con-
straints of the Fourth Amendment. Only the few with-
out cell phones could escape this tireless and absolute
surveillance.
   The Government and JUSTICE KENNEDY contend, how-
ever, that the collection of CSLI should be permitted
because the data is less precise than GPS information.
Not to worry, they maintain, because the location records
did “not on their own suffice to place [Carpenter] at the
crime scene”; they placed him within a wedge-shaped
sector ranging from one-eighth to four square miles. Brief
for United States 24; see post, at 18–19. Yet the Court has
already rejected the proposition that “inference insulates a
search.” Kyllo, 533 U. S., at 36. From the 127 days of
location data it received, the Government could, in combi-
nation with other information, deduce a detailed log of
Carpenter’s movements, including when he was at the site
of the robberies. And the Government thought the CSLI
accurate enough to highlight it during the closing argu-
ment of his trial. App. 131.
   At any rate, the rule the Court adopts “must take ac-
count of more sophisticated systems that are already in
use or in development.” Kyllo, 533 U. S., at 36. While the
records in this case reflect the state of technology at the
start of the decade, the accuracy of CSLI is rapidly ap-
proaching GPS-level precision. As the number of cell sites
has proliferated, the geographic area covered by each cell
sector has shrunk, particularly in urban areas. In addi-
tion, with new technology measuring the time and angle of
signals hitting their towers, wireless carriers already have
                 Cite as: 585 U. S. ____ (2018)           15

                     Opinion of the Court

the capability to pinpoint a phone’s location within 50
meters. Brief for Electronic Frontier Foundation et al. as
Amici Curiae 12 (describing triangulation methods that
estimate a device’s location inside a given cell sector).
  Accordingly, when the Government accessed CSLI from
the wireless carriers, it invaded Carpenter’s reason-
able expectation of privacy in the whole of his physical
movements.
                              B
  The Government’s primary contention to the contrary is
that the third-party doctrine governs this case. In its
view, cell-site records are fair game because they are
“business records” created and maintained by the wireless
carriers. The Government (along with JUSTICE KENNEDY)
recognizes that this case features new technology, but
asserts that the legal question nonetheless turns on a
garden-variety request for information from a third-party
witness. Brief for United States 32–34; post, at 12–14.
  The Government’s position fails to contend with the
seismic shifts in digital technology that made possible the
tracking of not only Carpenter’s location but also everyone
else’s, not for a short period but for years and years.
Sprint Corporation and its competitors are not your typi-
cal witnesses. Unlike the nosy neighbor who keeps an eye
on comings and goings, they are ever alert, and their
memory is nearly infallible. There is a world of difference
between the limited types of personal information ad-
dressed in Smith and Miller and the exhaustive chronicle
of location information casually collected by wireless
carriers today. The Government thus is not asking for a
straightforward application of the third-party doctrine,
but instead a significant extension of it to a distinct cate-
gory of information.
  The third-party doctrine partly stems from the notion
that an individual has a reduced expectation of privacy in
16             CARPENTER v. UNITED STATES

                      Opinion of the Court

information knowingly shared with another. But the fact
of “diminished privacy interests does not mean that the
Fourth Amendment falls out of the picture entirely.”
Riley, 573 U. S., at ___ (slip op., at 16). Smith and Miller,
after all, did not rely solely on the act of sharing. Instead,
they considered “the nature of the particular documents
sought” to determine whether “there is a legitimate ‘expec-
tation of privacy’ concerning their contents.” Miller, 425
U. S., at 442. Smith pointed out the limited capabilities of
a pen register; as explained in Riley, telephone call logs
reveal little in the way of “identifying information.”
Smith, 442 U. S., at 742; Riley, 573 U. S., at ___ (slip op.,
at 24). Miller likewise noted that checks were “not confi-
dential communications but negotiable instruments to be
used in commercial transactions.” 425 U. S., at 442. In
mechanically applying the third-party doctrine to this
case, the Government fails to appreciate that there are no
comparable limitations on the revealing nature of CSLI.
  The Court has in fact already shown special solicitude
for location information in the third-party context. In
Knotts, the Court relied on Smith to hold that an individ-
ual has no reasonable expectation of privacy in public
movements that he “voluntarily conveyed to anyone who
wanted to look.” Knotts, 460 U. S., at 281; see id., at 283
(discussing Smith). But when confronted with more per-
vasive tracking, five Justices agreed that longer term GPS
monitoring of even a vehicle traveling on public streets
constitutes a search. Jones, 565 U. S., at 430 (ALITO, J.,
concurring in judgment); id., at 415 (SOTOMAYOR, J.,
concurring). JUSTICE GORSUCH wonders why “someone’s
location when using a phone” is sensitive, post, at 3, and
JUSTICE KENNEDY assumes that a person’s discrete
movements “are not particularly private,” post, at 17. Yet
this case is not about “using a phone” or a person’s move-
ment at a particular time. It is about a detailed chronicle
of a person’s physical presence compiled every day, every
                 Cite as: 585 U. S. ____ (2018)           17

                     Opinion of the Court

moment, over several years. Such a chronicle implicates
privacy concerns far beyond those considered in Smith and
Miller.
  Neither does the second rationale underlying the third-
party doctrine—voluntary exposure—hold up when it
comes to CSLI. Cell phone location information is not
truly “shared” as one normally understands the term. In
the first place, cell phones and the services they provide
are “such a pervasive and insistent part of daily life” that
carrying one is indispensable to participation in modern
society. Riley, 573 U. S., at ___ (slip op., at 9). Second, a
cell phone logs a cell-site record by dint of its operation,
without any affirmative act on the part of the user beyond
powering up. Virtually any activity on the phone gener-
ates CSLI, including incoming calls, texts, or e-mails and
countless other data connections that a phone automati-
cally makes when checking for news, weather, or social
media updates. Apart from disconnecting the phone from
the network, there is no way to avoid leaving behind a
trail of location data. As a result, in no meaningful sense
does the user voluntarily “assume[ ] the risk” of turning
over a comprehensive dossier of his physical movements.
Smith, 442 U. S., at 745.
  We therefore decline to extend Smith and Miller to the
collection of CSLI. Given the unique nature of cell phone
location information, the fact that the Government ob-
tained the information from a third party does not over-
come Carpenter’s claim to Fourth Amendment protection.
The Government’s acquisition of the cell-site records was a
search within the meaning of the Fourth Amendment.
                       *     *    *
  Our decision today is a narrow one. We do not express a
view on matters not before us: real-time CSLI or “tower
dumps” (a download of information on all the devices that
connected to a particular cell site during a particular
18                CARPENTER v. UNITED STATES

                         Opinion of the Court

interval). We do not disturb the application of Smith and
Miller or call into question conventional surveillance
techniques and tools, such as security cameras. Nor do we
address other business records that might incidentally
reveal location information. Further, our opinion does not
consider other collection techniques involving foreign
affairs or national security. As Justice Frankfurter noted
when considering new innovations in airplanes and radios,
the Court must tread carefully in such cases, to ensure
that we do not “embarrass the future.” Northwest Air-
lines, Inc. v. Minnesota, 322 U. S. 292, 300 (1944).4
                               IV
   Having found that the acquisition of Carpenter’s CSLI
was a search, we also conclude that the Government must
generally obtain a warrant supported by probable cause
before acquiring such records. Although the “ultimate
measure of the constitutionality of a governmental search
is ‘reasonableness,’ ” our cases establish that warrantless
searches are typically unreasonable where “a search is
undertaken by law enforcement officials to discover evi-
dence of criminal wrongdoing.” Vernonia School Dist. 47J
v. Acton, 515 U. S. 646, 652–653 (1995). Thus, “[i]n the
absence of a warrant, a search is reasonable only if it falls
within a specific exception to the warrant requirement.”
Riley, 573 U. S., at ___ (slip op., at 5).
   The Government acquired the cell-site records pursuant
to a court order issued under the Stored Communications
Act, which required the Government to show “reasonable
grounds” for believing that the records were “relevant and
——————
  4 JUSTICE GORSUCH faults us for not promulgating a complete code

addressing the manifold situations that may be presented by this new
technology—under a constitutional provision turning on what is “rea-
sonable,” no less. Post, at 10–12. Like JUSTICE GORSUCH, we “do not
begin to claim all the answers today,” post, at 13, and therefore decide
no more than the case before us.
                 Cite as: 585 U. S. ____ (2018)          19

                     Opinion of the Court

material to an ongoing investigation.”          18 U. S. C.
§2703(d). That showing falls well short of the probable
cause required for a warrant. The Court usually requires
“some quantum of individualized suspicion” before
a search or seizure may take place. United States v.
Martinez-Fuerte, 428 U. S. 543, 560–561 (1976). Under the
standard in the Stored Communications Act, however, law
enforcement need only show that the cell-site evidence
might be pertinent to an ongoing investigation—a “gigan-
tic” departure from the probable cause rule, as the Gov-
ernment explained below. App. 34. Consequently, an
order issued under Section 2703(d) of the Act is not a
permissible mechanism for accessing historical cell-site
records. Before compelling a wireless carrier to turn over
a subscriber’s CSLI, the Government’s obligation is a
familiar one—get a warrant.
   JUSTICE ALITO contends that the warrant requirement
simply does not apply when the Government acquires
records using compulsory process. Unlike an actual
search, he says, subpoenas for documents do not involve
the direct taking of evidence; they are at most a “construc-
tive search” conducted by the target of the subpoena. Post,
at 12. Given this lesser intrusion on personal privacy,
JUSTICE ALITO argues that the compulsory production of
records is not held to the same probable cause standard.
In his view, this Court’s precedents set forth a categorical
rule—separate and distinct from the third-party doc-
trine—subjecting subpoenas to lenient scrutiny without
regard to the suspect’s expectation of privacy in the rec-
ords. Post, at 8–19.
   But this Court has never held that the Government may
subpoena third parties for records in which the suspect
has a reasonable expectation of privacy. Almost all of the
examples JUSTICE ALITO cites, see post, at 14–15, contem-
plated requests for evidence implicating diminished pri-
20                CARPENTER v. UNITED STATES

                          Opinion of the Court

vacy interests or for a corporation’s own books.5 The lone
exception, of course, is Miller, where the Court’s analysis
of the third-party subpoena merged with the application of
the third-party doctrine. 425 U. S., at 444 (concluding
that Miller lacked the necessary privacy interest to contest
the issuance of a subpoena to his bank).
   JUSTICE ALITO overlooks the critical issue. At some
point, the dissent should recognize that CSLI is an entirely
different species of business record—something that
implicates basic Fourth Amendment concerns about arbi-
trary government power much more directly than corpo-
rate tax or payroll ledgers. When confronting new con-
cerns wrought by digital technology, this Court has been
careful not to uncritically extend existing precedents. See
Riley, 573 U. S., at ___ (slip op., at 10) (“A search of
the information on a cell phone bears little resemblance
to the type of brief physical search considered [in prior
precedents].”).
   If the choice to proceed by subpoena provided a categori-
cal limitation on Fourth Amendment protection, no type of
record would ever be protected by the warrant require-
ment. Under JUSTICE ALITO’s view, private letters, digital
contents of a cell phone—any personal information re-
duced to document form, in fact—may be collected by
——————
  5 See United States v. Dionisio, 410 U. S. 1, 14 (1973) (“No person can

have a reasonable expectation that others will not know the sound of
his voice”); Donovan v. Lone Steer, Inc., 464 U. S. 408, 411, 415 (1984)
(payroll and sales records); California Bankers Assn. v. Shultz, 416
U. S. 21, 67 (1974) (Bank Secrecy Act reporting requirements); See v.
Seattle, 387 U. S. 541, 544 (1967) (financial books and records); United
States v. Powell, 379 U. S. 48, 49, 57 (1964) (corporate tax records);
McPhaul v. United States, 364 U. S. 372, 374, 382 (1960) (books and
records of an organization); United States v. Morton Salt Co., 338 U. S.
632, 634, 651–653 (1950) (Federal Trade Commission reporting re-
quirement); Oklahoma Press Publishing Co. v. Walling, 327 U. S. 186,
189, 204–208 (1946) (payroll records); Hale v. Henkel, 201 U. S. 43, 45,
75 (1906) (corporate books and papers).
                  Cite as: 585 U. S. ____ (2018)            21

                      Opinion of the Court

subpoena for no reason other than “official curiosity.”
United States v. Morton Salt Co., 338 U. S. 632, 652
(1950). JUSTICE KENNEDY declines to adopt the radical
implications of this theory, leaving open the question
whether the warrant requirement applies “when the Gov-
ernment obtains the modern-day equivalents of an indi-
vidual’s own ‘papers’ or ‘effects,’ even when those papers
or effects are held by a third party. ” Post, at 13 (citing
United States v. Warshak, 631 F. 3d 266, 283–288 (CA6
2010)). That would be a sensible exception, because it
would prevent the subpoena doctrine from overcoming any
reasonable expectation of privacy. If the third-party doc-
trine does not apply to the “modern-day equivalents of an
individual’s own ‘papers’ or ‘effects,’ ” then the clear impli-
cation is that the documents should receive full Fourth
Amendment protection. We simply think that such pro-
tection should extend as well to a detailed log of a person’s
movements over several years.
   This is certainly not to say that all orders compelling the
production of documents will require a showing of proba-
ble cause. The Government will be able to use subpoenas
to acquire records in the overwhelming majority of inves-
tigations. We hold only that a warrant is required in the
rare case where the suspect has a legitimate privacy in-
terest in records held by a third party.
   Further, even though the Government will generally
need a warrant to access CSLI, case-specific exceptions
may support a warrantless search of an individual’s cell-
site records under certain circumstances. “One well-
recognized exception applies when ‘ “the exigencies of the
situation” make the needs of law enforcement so compel-
ling that [a] warrantless search is objectively reasonable
under the Fourth Amendment.’ ” Kentucky v. King, 563
U. S. 452, 460 (2011) (quoting Mincey v. Arizona, 437 U. S.
385, 394 (1978)). Such exigencies include the need to
pursue a fleeing suspect, protect individuals who are
22             CARPENTER v. UNITED STATES

                     Opinion of the Court

threatened with imminent harm, or prevent the imminent
destruction of evidence. 563 U. S., at 460, and n. 3.
  As a result, if law enforcement is confronted with an
urgent situation, such fact-specific threats will likely
justify the warrantless collection of CSLI. Lower courts,
for instance, have approved warrantless searches related
to bomb threats, active shootings, and child abductions.
Our decision today does not call into doubt warrantless
access to CSLI in such circumstances. While police must
get a warrant when collecting CSLI to assist in the mine-
run criminal investigation, the rule we set forth does not
limit their ability to respond to an ongoing emergency.
                        *      *   *
   As Justice Brandeis explained in his famous dissent, the
Court is obligated—as “[s]ubtler and more far-reaching
means of invading privacy have become available to the
Government”—to ensure that the “progress of science”
does not erode Fourth Amendment protections. Olmstead
v. United States, 277 U. S. 438, 473–474 (1928). Here the
progress of science has afforded law enforcement a power-
ful new tool to carry out its important responsibilities. At
the same time, this tool risks Government encroachment
of the sort the Framers, “after consulting the lessons of
history,” drafted the Fourth Amendment to prevent. Di
Re, 332 U. S., at 595.
   We decline to grant the state unrestricted access to a
wireless carrier’s database of physical location infor-
mation. In light of the deeply revealing nature of CSLI,
its depth, breadth, and comprehensive reach, and the
inescapable and automatic nature of its collection, the fact
that such information is gathered by a third party does not
make it any less deserving of Fourth Amendment protec-
tion. The Government’s acquisition of the cell-site records
here was a search under that Amendment.
   The judgment of the Court of Appeals is reversed, and
                Cite as: 585 U. S. ____ (2018)         23

                    Opinion of the Court

the case is remanded for further proceedings consistent
with this opinion.
                                        It is so ordered.
                 Cite as: 585 U. S. ____ (2018)          1

                   KENNEDY, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 16–402
                         _________________


   TIMOTHY IVORY CARPENTER, PETITIONER v.

              UNITED STATES

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                        [June 22, 2018] 


  JUSTICE KENNEDY, with whom JUSTICE THOMAS and
JUSTICE ALITO join, dissenting.
  This case involves new technology, but the Court’s stark
departure from relevant Fourth Amendment precedents
and principles is, in my submission, unnecessary and
incorrect, requiring this respectful dissent.
  The new rule the Court seems to formulate puts needed,
reasonable, accepted, lawful, and congressionally author-
ized criminal investigations at serious risk in serious
cases, often when law enforcement seeks to prevent the
threat of violent crimes. And it places undue restrictions
on the lawful and necessary enforcement powers exercised
not only by the Federal Government, but also by law
enforcement in every State and locality throughout the
Nation. Adherence to this Court’s longstanding prece-
dents and analytic framework would have been the proper
and prudent way to resolve this case.
  The Court has twice held that individuals have no
Fourth Amendment interests in business records which
are possessed, owned, and controlled by a third party.
United States v. Miller, 425 U. S. 435 (1976); Smith v.
Maryland, 442 U. S. 735 (1979). This is true even when
the records contain personal and sensitive information. So
when the Government uses a subpoena to obtain, for
example, bank records, telephone records, and credit card
2              CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

statements from the businesses that create and keep these
records, the Government does not engage in a search of
the business’s customers within the meaning of the Fourth
Amendment.
   In this case petitioner challenges the Government’s
right to use compulsory process to obtain a now-common
kind of business record: cell-site records held by cell phone
service providers. The Government acquired the records
through an investigative process enacted by Congress.
Upon approval by a neutral magistrate, and based on the
Government’s duty to show reasonable necessity, it au-
thorizes the disclosure of records and information that are
under the control and ownership of the cell phone service
provider, not its customer. Petitioner acknowledges that
the Government may obtain a wide variety of business
records using compulsory process, and he does not ask the
Court to revisit its precedents. Yet he argues that, under
those same precedents, the Government searched his
records when it used court-approved compulsory process to
obtain the cell-site information at issue here.
   Cell-site records, however, are no different from the
many other kinds of business records the Government has
a lawful right to obtain by compulsory process. Customers
like petitioner do not own, possess, control, or use the
records, and for that reason have no reasonable expecta-
tion that they cannot be disclosed pursuant to lawful
compulsory process.
   The Court today disagrees. It holds for the first time
that by using compulsory process to obtain records of a
business entity, the Government has not just engaged in
an impermissible action, but has conducted a search of the
business’s customer. The Court further concludes that the
search in this case was unreasonable and the Government
needed to get a warrant to obtain more than six days of
cell-site records.
   In concluding that the Government engaged in a search,
                 Cite as: 585 U. S. ____ (2018)            3

                    KENNEDY, J., dissenting

the Court unhinges Fourth Amendment doctrine from the
property-based concepts that have long grounded the
analytic framework that pertains in these cases. In doing
so it draws an unprincipled and unworkable line between
cell-site records on the one hand and financial and tele-
phonic records on the other. According to today’s majority
opinion, the Government can acquire a record of every
credit card purchase and phone call a person makes over
months or years without upsetting a legitimate expecta-
tion of privacy. But, in the Court’s view, the Government
crosses a constitutional line when it obtains a court’s
approval to issue a subpoena for more than six days of
cell-site records in order to determine whether a person
was within several hundred city blocks of a crime scene.
That distinction is illogical and will frustrate principled
application of the Fourth Amendment in many routine yet
vital law enforcement operations.
   It is true that the Cyber Age has vast potential both to
expand and restrict individual freedoms in dimensions not
contemplated in earlier times. See Packingham v. North
Carolina, 582 U. S. ___, ___–___ (2017) (slip op., at 46).
For the reasons that follow, however, there is simply no
basis here for concluding that the Government interfered
with information that the cell phone customer, either from
a legal or commonsense standpoint, should have thought
the law would deem owned or controlled by him.
                              I
  Before evaluating the question presented it is helpful to
understand the nature of cell-site records, how they are
commonly used by cell phone service providers, and their
proper use by law enforcement.
  When a cell phone user makes a call, sends a text mes-
sage or e-mail, or gains access to the Internet, the cell
phone establishes a radio connection to an antenna at a
nearby cell site. The typical cell site covers a more-or-less
4               CARPENTER v. UNITED STATES

                     KENNEDY, J., dissenting

circular geographic area around the site. It has three (or
sometimes six) separate antennas pointing in different
directions. Each provides cell service for a different 120-
degree (or 60-degree) sector of the cell site’s circular cover-
age area. So a cell phone activated on the north side of a
cell site will connect to a different antenna than a cell
phone on the south side.
   Cell phone service providers create records each time a
cell phone connects to an antenna at a cell site. For a
phone call, for example, the provider records the date,
time, and duration of the call; the phone numbers making
and receiving the call; and, most relevant here, the cell
site used to make the call, as well as the specific antenna
that made the connection. The cell-site and antenna data
points, together with the date and time of connection, are
known as cell-site location information, or cell-site records.
By linking an individual’s cell phone to a particular 120-
or 60-degree sector of a cell site’s coverage area at a par-
ticular time, cell-site records reveal the general location of
the cell phone user.
   The location information revealed by cell-site records is
imprecise, because an individual cell-site sector usually
covers a large geographic area. The FBI agent who offered
expert testimony about the cell-site records at issue here
testified that a cell site in a city reaches between a half
mile and two miles in all directions. That means a 60-
degree sector covers between approximately one-eighth
and two square miles (and a 120-degree sector twice that
area). To put that in perspective, in urban areas cell-site
records often would reveal the location of a cell phone user
within an area covering between around a dozen and
several hundred city blocks. In rural areas cell-site rec-
ords can be up to 40 times more imprecise. By contrast, a
Global Positioning System (GPS) can reveal an individ-
ual’s location within around 15 feet.
   Major cell phone service providers keep cell-site records
                 Cite as: 585 U. S. ____ (2018)            5

                    KENNEDY, J., dissenting

for long periods of time. There is no law requiring them to
do so. Instead, providers contract with their customers to
collect and keep these records because they are valuable to
the providers. Among other things, providers aggregate
the records and sell them to third parties along with other
information gleaned from cell phone usage. This data can
be used, for example, to help a department store deter-
mine which of various prospective store locations is likely
to get more foot traffic from middle-aged women who live
in affluent zip codes. The market for cell phone data is
now estimated to be in the billions of dollars. See Brief for
Technology Experts as Amici Curiae 23.
   Cell-site records also can serve an important investiga-
tive function, as the facts of this case demonstrate. Peti-
tioner, Timothy Carpenter, along with a rotating group of
accomplices, robbed at least six RadioShack and T-Mobile
stores at gunpoint over a 2-year period. Five of those
robberies occurred in the Detroit area, each crime at least
four miles from the last. The sixth took place in Warren,
Ohio, over 200 miles from Detroit.
   The Government, of course, did not know all of these
details in 2011 when it began investigating Carpenter. In
April of that year police arrested four of Carpenter’s co-
conspirators. One of them confessed to committing nine
robberies in Michigan and Ohio between December 2010
and March 2011. He identified 15 accomplices who had
participated in at least one of those robberies; named
Carpenter as one of the accomplices; and provided Carpen-
ter’s cell phone number to the authorities. The suspect
also warned that the other members of the conspiracy
planned to commit more armed robberies in the immediate
future.
   The Government at this point faced a daunting task.
Even if it could identify and apprehend the suspects, still
it had to link each suspect in this changing criminal gang
to specific robberies in order to bring charges and convict.
6               CARPENTER v. UNITED STATES

                     KENNEDY, J., dissenting

And, of course, it was urgent that the Government take all
necessary steps to stop the ongoing and dangerous crime
spree.
   Cell-site records were uniquely suited to this task. The
geographic dispersion of the robberies meant that, if Car-
penter’s cell phone were within even a dozen to several
hundred city blocks of one or more of the stores when the
different robberies occurred, there would be powerful
circumstantial evidence of his participation; and this
would be especially so if his cell phone usually was not
located in the sectors near the stores except during the
robbery times.
   To obtain these records, the Government applied to
federal magistrate judges for disclosure orders pursuant to
§2703(d) of the Stored Communications Act. That Act
authorizes a magistrate judge to issue an order requiring
disclosure of cell-site records if the Government demon-
strates “specific and articulable facts showing that there
are reasonable grounds to believe” the records “are rele-
vant and material to an ongoing criminal investigation.”
18 U. S. C. §§2703(d), 2711(3). The full statutory provi-
sion is set out in the Appendix, infra.
   From Carpenter’s primary service provider, MetroPCS,
the Government obtained records from between December
2010 and April 2011, based on its understanding that nine
robberies had occurred in that timeframe. The Govern-
ment also requested seven days of cell-site records from
Sprint, spanning the time around the robbery in Warren,
Ohio. It obtained two days of records.
   These records confirmed that Carpenter’s cell phone was
in the general vicinity of four of the nine robberies, includ-
ing the one in Ohio, at the times those robberies occurred.
                               II
  The first Clause of the Fourth Amendment provides that
“the right of the people to be secure in their persons, houses,
                 Cite as: 585 U. S. ____ (2018)           7

                   KENNEDY, J., dissenting

papers, and effects, against unreasonable searches and
seizures, shall not be violated.” The customary beginning
point in any Fourth Amendment search case is whether
the Government’s actions constitute a “search” of the
defendant’s person, house, papers, or effects, within the
meaning of the constitutional provision. If so, the next
question is whether that search was reasonable.
   Here the only question necessary to decide is whether
the Government searched anything of Carpenter’s when it
used compulsory process to obtain cell-site records from
Carpenter’s cell phone service providers. This Court’s
decisions in Miller and Smith dictate that the answer is
no, as every Court of Appeals to have considered the ques-
tion has recognized. See United States v. Thompson, 866
F. 3d 1149 (CA10 2017); United States v. Graham, 824
F. 3d 421 (CA4 2016) (en banc); Carpenter v. United
States, 819 F. 3d 880 (CA6 2016); United States v. Davis,
785 F. 3d 498 (CA11 2015) (en banc); In re Application
of U. S. for Historical Cell Site Data, 724 F. 3d 600
(CA5 2013).
                             A
  Miller and Smith hold that individuals lack any protected
Fourth Amendment interests in records that are pos-
sessed, owned, and controlled only by a third party. In
Miller federal law enforcement officers obtained four
months of the defendant’s banking records. 425 U. S., at
437438. And in Smith state police obtained records of
the phone numbers dialed from the defendant’s home
phone. 442 U. S., at 737. The Court held in both cases
that the officers did not search anything belonging to the
defendants within the meaning of the Fourth Amendment.
The defendants could “assert neither ownership nor pos-
session” of the records because the records were created,
owned, and controlled by the companies. Miller, supra, at
440; see Smith, supra, at 741. And the defendants had no
8               CARPENTER v. UNITED STATES

                     KENNEDY, J., dissenting

reasonable expectation of privacy in information they
“voluntarily conveyed to the [companies] and exposed to
their employees in the ordinary course of business.” Mil-
ler, supra, at 442; see Smith, 442 U. S., at 744. Rather,
the defendants “assumed the risk that the information
would be divulged to police.” Id., at 745.
   Miller and Smith have been criticized as being based on
too narrow a view of reasonable expectations of privacy.
See, e.g., Ashdown, The Fourth Amendment and the “Le-
gitimate Expectation of Privacy,” 34 Vand. L. Rev. 1289,
13131316 (1981). Those criticisms, however, are unwar-
ranted. The principle established in Miller and Smith is
correct for two reasons, the first relating to a defendant’s
attenuated interest in property owned by another, and the
second relating to the safeguards inherent in the use of
compulsory process.
   First, Miller and Smith placed necessary limits on the
ability of individuals to assert Fourth Amendment inter-
ests in property to which they lack a “requisite connec-
tion.” Minnesota v. Carter, 525 U. S. 83, 99 (1998)
(KENNEDY, J., concurring). Fourth Amendment rights,
after all, are personal. The Amendment protects “[t]he
right of the people to be secure in their . . . persons, houses,
papers, and effects”—not the persons, houses, papers, and
effects of others. (Emphasis added.)
   The concept of reasonable expectations of privacy, first
announced in Katz v. United States, 389 U. S. 347 (1967),
sought to look beyond the “arcane distinctions developed
in property and tort law” in evaluating whether a person
has a sufficient connection to the thing or place searched
to assert Fourth Amendment interests in it. Rakas v.
Illinois, 439 U. S. 128, 143 (1978). Yet “property concepts”
are, nonetheless, fundamental “in determining the pres-
ence or absence of the privacy interests protected by that
Amendment.” Id., at 143144, n. 12. This is so for at least
two reasons. First, as a matter of settled expectations
                 Cite as: 585 U. S. ____ (2018)           9

                    KENNEDY, J., dissenting

from the law of property, individuals often have greater
expectations of privacy in things and places that belong to
them, not to others. And second, the Fourth Amendment’s
protections must remain tethered to the text of that
Amendment, which, again, protects only a person’s own
“persons, houses, papers, and effects.”
   Katz did not abandon reliance on property-based con-
cepts. The Court in Katz analogized the phone booth used
in that case to a friend’s apartment, a taxicab, and a hotel
room. 389 U. S., at 352, 359. So when the defendant
“shu[t] the door behind him” and “pa[id] the toll,” id., at
352, he had a temporary interest in the space and a legit-
imate expectation that others would not intrude, much
like the interest a hotel guest has in a hotel room, Stoner
v. California, 376 U. S. 483 (1964), or an overnight guest
has in a host’s home, Minnesota v. Olson, 495 U. S. 91
(1990). The Government intruded on that space when it
attached a listening device to the phone booth. Katz, 389
U. S., at 348. (And even so, the Court made it clear that
the Government’s search could have been reasonable had
there been judicial approval on a case-specific basis,
which, of course, did occur here. Id., at 357359.)
   Miller and Smith set forth an important and necessary
limitation on the Katz framework. They rest upon the
commonsense principle that the absence of property law
analogues can be dispositive of privacy expectations. The
defendants in those cases could expect that the third-party
businesses could use the records the companies collected,
stored, and classified as their own for any number of
business and commercial purposes. The businesses were
not bailees or custodians of the records, with a duty to
hold the records for the defendants’ use. The defendants
could make no argument that the records were their own
papers or effects. See Miller, supra, at 440 (“the docu-
ments subpoenaed here are not respondent’s ‘private
papers’ ”); Smith, supra, at 741 (“petitioner obviously
10             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

cannot claim that his ‘property’ was invaded”). The rec-
ords were the business entities’ records, plain and simple.
The defendants had no reason to believe the records were
owned or controlled by them and so could not assert a
reasonable expectation of privacy in the records.
    The second principle supporting Miller and Smith is the
longstanding rule that the Government may use compul-
sory process to compel persons to disclose documents and
other evidence within their possession and control. See
United States v. Nixon, 418 U. S. 683, 709 (1974) (it is an
“ancient proposition of law” that “the public has a right to
every man’s evidence” (internal quotation marks and
alterations omitted)). A subpoena is different from a
warrant in its force and intrusive power. While a warrant
allows the Government to enter and seize and make the
examination itself, a subpoena simply requires the person
to whom it is directed to make the disclosure. A subpoena,
moreover, provides the recipient the “opportunity to pre-
sent objections” before complying, which further mitigates
the intrusion. Oklahoma Press Publishing Co. v. Walling,
327 U. S. 186, 195 (1946).
    For those reasons this Court has held that a subpoena
for records, although a “constructive” search subject to
Fourth Amendment constraints, need not comply with the
procedures applicable to warrants—even when challenged
by the person to whom the records belong. Id., at 202,
208.      Rather, a subpoena complies with the Fourth
Amendment’s reasonableness requirement so long as it is
“ ‘sufficiently limited in scope, relevant in purpose, and
specific in directive so that compliance will not be unrea-
sonably burdensome.’ ” Donovan v. Lone Steer, Inc., 464
U. S. 408, 415 (1984). Persons with no meaningful inter-
ests in the records sought by a subpoena, like the defend-
ants in Miller and Smith, have no rights to object to the
records’ disclosure—much less to assert that the Govern-
ment must obtain a warrant to compel disclosure of the
                 Cite as: 585 U. S. ____ (2018)          11

                   KENNEDY, J., dissenting

records. See Miller, 425 U. S., at 444446; SEC v. Jerry T.
O’Brien, Inc., 467 U. S. 735, 742743 (1984).
  Based on Miller and Smith and the principles underly-
ing those cases, it is well established that subpoenas may
be used to obtain a wide variety of records held by busi-
nesses, even when the records contain private information.
See 2 W. LaFave, Search and Seizure §4.13 (5th ed. 2012).
Credit cards are a prime example. State and federal law
enforcement, for instance, often subpoena credit card
statements to develop probable cause to prosecute crimes
ranging from drug trafficking and distribution to
healthcare fraud to tax evasion. See United States v.
Phibbs, 999 F. 2d 1053 (CA6 1993) (drug distribution);
McCune v. DOJ, 592 Fed. Appx. 287 (CA5 2014)
(healthcare fraud); United States v. Green, 305 F. 3d 422
(CA6 2002) (drug trafficking and tax evasion); see also 12
U. S. C. §§3402(4), 3407 (allowing the Government to
subpoena financial records if “there is reason to believe
that the records sought are relevant to a legitimate law
enforcement inquiry”). Subpoenas also may be used to
obtain vehicle registration records, hotel records, employ-
ment records, and records of utility usage, to name just a
few other examples. See 1 LaFave, supra, §2.7(c).
  And law enforcement officers are not alone in their
reliance on subpoenas to obtain business records for legit-
imate investigations. Subpoenas also are used for investi-
gatory purposes by state and federal grand juries, see
United States v. Dionisio, 410 U. S. 1 (1973), state and
federal administrative agencies, see Oklahoma Press,
supra, and state and federal legislative bodies, see
McPhaul v. United States, 364 U. S. 372 (1960).
                             B
   Carpenter does not question these traditional investiga-
tive practices. And he does not ask the Court to reconsider
Miller and Smith. Carpenter argues only that, under
12             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

Miller and Smith, the Government may not use compulsory
process to acquire cell-site records from cell phone service
providers.
   There is no merit in this argument. Cell-site records,
like all the examples just discussed, are created, kept,
classified, owned, and controlled by cell phone service
providers, which aggregate and sell this information to
third parties. As in Miller, Carpenter can “assert neither
ownership nor possession” of the records and has no con-
trol over them. 425 U. S., at 440.
   Carpenter argues that he has Fourth Amendment inter-
ests in the cell-site records because they are in essence his
personal papers by operation of 47 U. S. C. §222. That
statute imposes certain restrictions on how providers may
use “customer proprietary network information”—a term
that encompasses cell-site records. §§222(c), (h)(1)(A).
The statute in general prohibits providers from disclosing
personally identifiable cell-site records to private third
parties. §222(c)(1). And it allows customers to request
cell-site records from the provider. §222(c)(2).
   Carpenter’s argument is unpersuasive, however, for
§222 does not grant cell phone customers any meaningful
interest in cell-site records. The statute’s confidentiality
protections may be overridden by the interests of the
providers or the Government. The providers may disclose
the records “to protect the[ir] rights or property” or to
“initiate, render, bill, and collect for telecommunications
services.” §§222(d)(1), (2). They also may disclose the
records “as required by law”—which, of course, is how they
were disclosed in this case. §222(c)(1). Nor does the stat-
ute provide customers any practical control over the rec-
ords. Customers do not create the records; they have no
say in whether or for how long the records are stored; and
they cannot require the records to be modified or de-
stroyed. Even their right to request access to the records
is limited, for the statute “does not preclude a carrier from
                  Cite as: 585 U. S. ____ (2018)           13

                    KENNEDY, J., dissenting

being reimbursed by the customers . . . for the costs asso-
ciated with making such disclosures.” H. R. Rep. No. 104–
204, pt. 1, p. 90 (1995). So in every legal and practical
sense the “network information” regulated by §222 is,
under that statute, “proprietary” to the service providers,
not Carpenter. The Court does not argue otherwise.
  Because Carpenter lacks a requisite connection to the
cell-site records, he also may not claim a reasonable expec-
tation of privacy in them. He could expect that a third
party—the cell phone service provider—could use the
information it collected, stored, and classified as its own
for a variety of business and commercial purposes.
  All this is not to say that Miller and Smith are without
limits. Miller and Smith may not apply when the Gov-
ernment obtains the modern-day equivalents of an indi-
vidual’s own “papers” or “effects,” even when those papers
or effects are held by a third party. See Ex parte Jackson,
96 U. S. 727, 733 (1878) (letters held by mail carrier);
United States v. Warshak, 631 F. 3d 266, 283288 (CA6
2010) (e-mails held by Internet service provider). As
already discussed, however, this case does not involve
property or a bailment of that sort. Here the Govern-
ment’s acquisition of cell-site records falls within the
heartland of Miller and Smith.
  In fact, Carpenter’s Fourth Amendment objection is
even weaker than those of the defendants in Miller and
Smith. Here the Government did not use a mere sub-
poena to obtain the cell-site records. It acquired the records
only after it proved to a Magistrate Judge reasonable
grounds to believe that the records were relevant and
material to an ongoing criminal investigation. See 18
U. S. C. §2703(d). So even if §222 gave Carpenter some
attenuated interest in the records, the Government’s
conduct here would be reasonable under the standards
governing subpoenas. See Donovan, 464 U. S., at 415.
  Under Miller and Smith, then, a search of the sort that
14             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

requires a warrant simply did not occur when the Gov-
ernment used court-approved compulsory process, based
on a finding of reasonable necessity, to compel a cell phone
service provider, as owner, to disclose cell-site records.
                             III
  The Court rejects a straightforward application of Miller
and Smith. It concludes instead that applying those cases
to cell-site records would work a “significant extension” of
the principles underlying them, ante, at 15, and holds that
the acquisition of more than six days of cell-site records
constitutes a search, ante, at 11, n. 3.
  In my respectful view the majority opinion misreads this
Court’s precedents, old and recent, and transforms Miller
and Smith into an unprincipled and unworkable doctrine.
The Court’s newly conceived constitutional standard will
cause confusion; will undermine traditional and important
law enforcement practices; and will allow the cell phone to
become a protected medium that dangerous persons will
use to commit serious crimes.
                             A
  The Court errs at the outset by attempting to sidestep
Miller and Smith. The Court frames this case as following
instead from United States v. Knotts, 460 U. S. 276 (1983),
and United States v. Jones, 565 U. S. 400 (2012). Those
cases, the Court suggests, establish that “individuals have
a reasonable expectation of privacy in the whole of their
physical movements.” Ante, at 79, 12.
  Knotts held just the opposite: “A person traveling in an
automobile on public thoroughfares has no reasonable
expectation of privacy in his movements from one place to
another.” 460 U. S., at 281. True, the Court in Knotts also
suggested that “different constitutional principles may be
applicable” to “dragnet-type law enforcement practices.”
Id., at 284. But by dragnet practices the Court was refer-
                  Cite as: 585 U. S. ____ (2018)           15

                    KENNEDY, J., dissenting

ring to “ ‘twenty-four hour surveillance of any citizen of
this country . . . without judicial knowledge or supervi-
sion.’ ” Id., at 283.
   Those “different constitutional principles” mentioned in
Knotts, whatever they may be, do not apply in this case.
Here the Stored Communications Act requires a neutral
judicial officer to confirm in each case that the Govern-
ment has “reasonable grounds to believe” the cell-site
records “are relevant and material to an ongoing criminal
investigation.” 18 U. S. C. §2703(d). This judicial check
mitigates the Court’s concerns about “ ‘a too permeating
police surveillance.’ ” Ante, at 6 (quoting United States v.
Di Re, 332 U. S. 581, 595 (1948)). Here, even more so
than in Knotts, “reality hardly suggests abuse.” 460 U. S.,
at 284.
   The Court’s reliance on Jones fares no better. In Jones
the Government installed a GPS tracking device on the
defendant’s automobile. The Court held the Government
searched the automobile because it “physically occupied
private property [of the defendant] for the purpose of
obtaining information.” 565 U. S., at 404. So in Jones it
was “not necessary to inquire about the target’s expecta-
tion of privacy in his vehicle’s movements.” Grady v.
North Carolina, 575 U. S. ___, ___ (2015) (per curiam) (slip
op., at 3).
   Despite that clear delineation of the Court’s holding in
Jones, the Court today declares that Jones applied the
“ ‘different constitutional principles’ ” alluded to in Knotts
to establish that an individual has an expectation of pri-
vacy in the sum of his whereabouts. Ante, at 8, 12. For that
proposition the majority relies on the two concurring
opinions in Jones, one of which stated that “longer term
GPS monitoring in investigations of most offenses impinges
on expectations of privacy.” 565 U. S., at 430 (ALITO, J.,
concurring). But Jones involved direct governmental
surveillance of a defendant’s automobile without judicial
16             CARPENTER v. UNITED STATES

                   KENNEDY, J., dissenting

authorization—specifically, GPS surveillance accurate
within 50 to 100 feet. Id., at 402403. Even assuming
that the different constitutional principles mentioned in
Knotts would apply in a case like Jones—a proposition the
Court was careful not to announce in Jones, supra, at
412413—those principles are inapplicable here. Cases
like this one, where the Government uses court-approved
compulsory process to obtain records owned and controlled
by a third party, are governed by the two majority opin-
ions in Miller and Smith.
                              B
   The Court continues its analysis by misinterpreting
Miller and Smith, and then it reaches the wrong outcome
on these facts even under its flawed standard.
   The Court appears, in my respectful view, to read Miller
and Smith to establish a balancing test. For each “quali-
tatively different category” of information, the Court
suggests, the privacy interests at stake must be weighed
against the fact that the information has been disclosed to
a third party. See ante, at 11, 1517. When the privacy
interests are weighty enough to “overcome” the third-party
disclosure, the Fourth Amendment’s protections apply.
See ante, at 17.
   That is an untenable reading of Miller and Smith. As
already discussed, the fact that information was relin-
quished to a third party was the entire basis for conclud-
ing that the defendants in those cases lacked a reasonable
expectation of privacy. Miller and Smith do not establish
the kind of category-by-category balancing the Court today
prescribes.
   But suppose the Court were correct to say that Miller
and Smith rest on so imprecise a foundation. Still the
Court errs, in my submission, when it concludes that cell-
site records implicate greater privacy interests—and thus
deserve greater Fourth Amendment protection—than
                  Cite as: 585 U. S. ____ (2018)             17

                     KENNEDY, J., dissenting

financial records and telephone records.
    Indeed, the opposite is true. A person’s movements are
not particularly private. As the Court recognized in
Knotts, when the defendant there “traveled over the public
streets he voluntarily conveyed to anyone who wanted to
look the fact that he was traveling over particular roads in
a particular direction, the fact of whatever stops he made,
and the fact of his final destination.” 460 U. S., at
281282. Today expectations of privacy in one’s location
are, if anything, even less reasonable than when the Court
decided Knotts over 30 years ago. Millions of Americans
choose to share their location on a daily basis, whether by
using a variety of location-based services on their phones,
or by sharing their location with friends and the public at
large via social media.
    And cell-site records, as already discussed, disclose a
person’s location only in a general area. The records at
issue here, for example, revealed Carpenter’s location
within an area covering between around a dozen and
several hundred city blocks. “Areas of this scale might
encompass bridal stores and Bass Pro Shops, gay bars and
straight ones, a Methodist church and the local mosque.”
819 F. 3d 880, 889 (CA6 2016). These records could not
reveal where Carpenter lives and works, much less his
“ ‘familial, political, professional, religious, and sexual
associations.’ ” Ante, at 12 (quoting Jones, supra, at 415
(SOTOMAYOR, J., concurring)).
    By contrast, financial records and telephone records do
“ ‘revea[l] . . . personal affairs, opinions, habits and associ-
ations.’ ” Miller, 425 U. S., at 451 (Brennan, J., dissent-
ing); see Smith, 442 U. S., at 751 (Marshall, J., dissent-
ing). What persons purchase and to whom they talk might
disclose how much money they make; the political and
religious organizations to which they donate; whether they
have visited a psychiatrist, plastic surgeon, abortion clinic,
or AIDS treatment center; whether they go to gay bars or
18             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

straight ones; and who are their closest friends and family
members. The troves of intimate information the Gov-
ernment can and does obtain using financial records and
telephone records dwarfs what can be gathered from cell-
site records.
   Still, the Court maintains, cell-site records are “unique”
because they are “comprehensive” in their reach; allow for
retrospective collection; are “easy, cheap, and efficient
compared to traditional investigative tools”; and are not
exposed to cell phone service providers in a meaningfully
voluntary manner. Ante, at 1113, 17, 22. But many
other kinds of business records can be so described. Fi-
nancial records are of vast scope. Banks and credit card
companies keep a comprehensive account of almost every
transaction an individual makes on a daily basis. “With
just the click of a button, the Government can access each
[company’s] deep repository of historical [financial] infor-
mation at practically no expense.” Ante, at 1213. And
the decision whether to transact with banks and credit
card companies is no more or less voluntary than the
decision whether to use a cell phone. Today, just as when
Miller was decided, “ ‘it is impossible to participate in the
economic life of contemporary society without maintaining
a bank account.’ ” 425 U. S., at 451 (Brennan, J., dissent-
ing). But this Court, nevertheless, has held that individ-
uals do not have a reasonable expectation of privacy in
financial records.
   Perhaps recognizing the difficulty of drawing the consti-
tutional line between cell-site records and financial and
telephonic records, the Court posits that the accuracy of
cell-site records “is rapidly approaching GPS-level preci-
sion.” Ante, at 14. That is certainly plausible in the era of
cyber technology, yet the privacy interests associated with
location information, which is often disclosed to the public
at large, still would not outweigh the privacy interests
implicated by financial and telephonic records.
                 Cite as: 585 U. S. ____ (2018)          19

                    KENNEDY, J., dissenting

   Perhaps more important, those future developments are
no basis upon which to resolve this case. In general, the
Court “risks error by elaborating too fully on the Fourth
Amendment implications of emerging technology before its
role in society has become clear.” Ontario v. Quon, 560
U. S. 746, 759 (2010). That judicial caution, prudent in
most cases, is imperative in this one.
   Technological changes involving cell phones have com-
plex effects on crime and law enforcement. Cell phones
make crimes easier to coordinate and conceal, while also
providing the Government with new investigative tools
that may have the potential to upset traditional privacy
expectations.     See Kerr, An Equilibrium-Adjustment
Theory of the Fourth Amendment, 125 Harv. L. Rev 476,
512517 (2011). How those competing effects balance
against each other, and how property norms and expecta-
tions of privacy form around new technology, often will be
difficult to determine during periods of rapid technological
change. In those instances, and where the governing legal
standard is one of reasonableness, it is wise to defer to
legislative judgments like the one embodied in §2703(d) of
the Stored Communications Act. See Jones, 565 U. S., at
430 (ALITO, J., concurring). In §2703(d) Congress weighed
the privacy interests at stake and imposed a judicial check
to prevent executive overreach. The Court should be wary
of upsetting that legislative balance and erecting constitu-
tional barriers that foreclose further legislative instruc-
tions. See Quon, supra, at 759. The last thing the Court
should do is incorporate an arbitrary and outside limit—in
this case six days’ worth of cell-site records—and use it as
the foundation for a new constitutional framework. The
Court’s decision runs roughshod over the mechanism
Congress put in place to govern the acquisition of cell-site
records and closes off further legislative debate on these
issues.
20             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

                               C
   The Court says its decision is a “narrow one.” Ante, at
17. But its reinterpretation of Miller and Smith will have
dramatic consequences for law enforcement, courts, and
society as a whole.
   Most immediately, the Court’s holding that the Gov-
ernment must get a warrant to obtain more than six days
of cell-site records limits the effectiveness of an important
investigative tool for solving serious crimes. As this case
demonstrates, cell-site records are uniquely suited to help
the Government develop probable cause to apprehend
some of the Nation’s most dangerous criminals: serial
killers, rapists, arsonists, robbers, and so forth. See also,
e.g., Davis, 785 F. 3d, at 500501 (armed robbers); Brief
for Alabama et al. as Amici Curiae 2122 (serial killer).
These records often are indispensable at the initial stages
of investigations when the Government lacks the evidence
necessary to obtain a warrant. See United States v. Pem-
brook, 876 F. 3d 812, 816819 (CA6 2017). And the long-
term nature of many serious crimes, including serial
crimes and terrorism offenses, can necessitate the use of
significantly more than six days of cell-site records. The
Court’s arbitrary 6-day cutoff has the perverse effect
of nullifying Congress’ reasonable framework for obtain-
ing cell-site records in some of the most serious criminal
investigations.
   The Court’s decision also will have ramifications that
extend beyond cell-site records to other kinds of infor-
mation held by third parties, yet the Court fails “to pro-
vide clear guidance to law enforcement” and courts on key
issues raised by its reinterpretation of Miller and Smith.
Riley v. California, 573 U. S. ___, ___ (2014) (slip op.,
at 22).
   First, the Court’s holding is premised on cell-site records
being a “distinct category of information” from other busi-
                 Cite as: 585 U. S. ____ (2018)          21

                    KENNEDY, J., dissenting

ness records. Ante, at 15. But the Court does not explain
what makes something a distinct category of information.
Whether credit card records are distinct from bank rec-
ords; whether payment records from digital wallet applica-
tions are distinct from either; whether the electronic bank
records available today are distinct from the paper and
microfilm records at issue in Miller; or whether cell-phone
call records are distinct from the home-phone call records
at issue in Smith, are just a few of the difficult questions
that require answers under the Court’s novel conception of
Miller and Smith.
   Second, the majority opinion gives courts and law en-
forcement officers no indication how to determine whether
any particular category of information falls on the finan-
cial-records side or the cell-site-records side of its newly
conceived constitutional line. The Court’s multifactor
analysis—considering intimacy, comprehensiveness, ex-
pense, retrospectivity, and voluntariness—puts the law on
a new and unstable foundation.
   Third, even if a distinct category of information is
deemed to be more like cell-site records than financial
records, courts and law enforcement officers will have to
guess how much of that information can be requested
before a warrant is required. The Court suggests that less
than seven days of location information may not require a
warrant. See ante, at 11, n. 3; see also ante, at 1718
(expressing no opinion on “real-time CSLI,” tower dumps,
and security-camera footage). But the Court does not
explain why that is so, and nothing in its opinion even
alludes to the considerations that should determine
whether greater or lesser thresholds should apply to in-
formation like IP addresses or website browsing history.
   Fourth, by invalidating the Government’s use of court-
approved compulsory process in this case, the Court calls
into question the subpoena practices of federal and state
grand juries, legislatures, and other investigative bodies,
22             CARPENTER v. UNITED STATES

                   KENNEDY, J., dissenting

as JUSTICE ALITO’s opinion explains. See post, at 219
(dissenting opinion). Yet the Court fails even to mention
the serious consequences this will have for the proper
administration of justice.
  In short, the Court’s new and uncharted course will
inhibit law enforcement and “keep defendants and judges
guessing for years to come.” Riley, 573 U. S., at ___ (slip
op., at 25) (internal quotation marks omitted).
                        *     *     *
   This case should be resolved by interpreting accepted
property principles as the baseline for reasonable expecta-
tions of privacy. Here the Government did not search
anything over which Carpenter could assert ownership or
control. Instead, it issued a court-authorized subpoena to
a third party to disclose information it alone owned and
controlled. That should suffice to resolve this case.
   Having concluded, however, that the Government
searched Carpenter when it obtained cell-site records from
his cell phone service providers, the proper resolution of
this case should have been to remand for the Court of
Appeals to determine in the first instance whether the
search was reasonable. Most courts of appeals, believing
themselves bound by Miller and Smith, have not grappled
with this question. And the Court’s reflexive imposition of
the warrant requirement obscures important and difficult
issues, such as the scope of Congress’ power to authorize
the Government to collect new forms of information using
processes that deviate from traditional warrant proce-
dures, and how the Fourth Amendment’s reasonableness
requirement should apply when the Government uses
compulsory process instead of engaging in an actual,
physical search.
   These reasons all lead to this respectful dissent.
                 Cite as: 585 U. S. ____ (2018)          23

                   KENNEDY
               Appendix      , J., dissenting
                        to opinion  of KENNEDY, J.

                         APPENDIX

“§2703. Required disclosure of customer communi-
cations or records

   “(d) REQUIREMENTS FOR COURT ORDER.—A court order
for disclosure under subsection (b) or (c) may be issued by
any court that is a court of competent jurisdiction and
shall issue only if the governmental entity offers specific
and articulable facts showing that there are reasonable
grounds to believe that the contents of a wire or electronic
communication, or the records or other information
sought, are relevant and material to an ongoing criminal
investigation. In the case of a State governmental author-
ity, such a court order shall not issue if prohibited by the
law of such State. A court issuing an order pursuant to
this section, on a motion made promptly by the service
provider, may quash or modify such order, if the infor-
mation or records requested are unusually voluminous in
nature or compliance with such order otherwise would
cause an undue burden on such provider.”
                 Cite as: 585 U. S. ____ (2018)            1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 16–402
                         _________________


    TIMOTHY IVORY CARPENTER, PETITIONER v.

               UNITED STATES

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                        [June 22, 2018] 


  JUSTICE THOMAS, dissenting.
  This case should not turn on “whether” a search oc­
curred. Ante, at 1. It should turn, instead, on whose
property was searched. The Fourth Amendment guaran­
tees individuals the right to be secure from unreasonable
searches of “their persons, houses, papers, and effects.”
(Emphasis added.) In other words, “each person has the
right to be secure against unreasonable searches . . . in his
own person, house, papers, and effects.” Minnesota v.
Carter, 525 U. S. 83, 92 (1998) (Scalia, J., concurring). By
obtaining the cell-site records of MetroPCS and Sprint, the
Government did not search Carpenter’s property. He did
not create the records, he does not maintain them, he
cannot control them, and he cannot destroy them. Neither
the terms of his contracts nor any provision of law makes
the records his. The records belong to MetroPCS and
Sprint.
  The Court concludes that, although the records are not
Carpenter’s, the Government must get a warrant because
Carpenter had a reasonable “expectation of privacy” in the
location information that they reveal. Ante, at 11. I agree
with JUSTICE KENNEDY, JUSTICE ALITO, JUSTICE
GORSUCH, and every Court of Appeals to consider the
question that this is not the best reading of our
precedents.
2                 CARPENTER v. UNITED STATES

                         THOMAS, J., dissenting

  The more fundamental problem with the Court’s opin­
ion, however, is its use of the “reasonable expectation of
privacy” test, which was first articulated by Justice Har­
lan in Katz v. United States, 389 U. S. 347, 360–361 (1967)
(concurring opinion). The Katz test has no basis in the
text or history of the Fourth Amendment. And, it invites
courts to make judgments about policy, not law. Until we
confront the problems with this test, Katz will continue to
distort Fourth Amendment jurisprudence. I respectfully
dissent.
                             I
  Katz was the culmination of a series of decisions apply­
ing the Fourth Amendment to electronic eavesdropping.
The first such decision was Olmstead v. United States, 277
U. S. 438 (1928), where federal officers had intercepted the
defendants’ conversations by tapping telephone lines near
their homes. Id., at 456–457. In an opinion by Chief
Justice Taft, the Court concluded that this wiretap did not
violate the Fourth Amendment. No “search” occurred,
according to the Court, because the officers did not physi­
cally enter the defendants’ homes. Id., at 464–466. And
neither the telephone lines nor the defendants’ intangible
conversations qualified as “persons, houses, papers, [or]
effects” within the meaning of the Fourth Amendment.
Ibid.1 In the ensuing decades, this Court adhered to

——————
   1 Justice Brandeis authored the principal dissent in Olmstead. He

consulted the “underlying purpose,” rather than “the words of the
[Fourth] Amendment,” to conclude that the wiretap was a search. 277
U. S., at 476. In Justice Brandeis’ view, the Framers “recognized the
significance of man’s spiritual nature, of his feelings and of his intel­
lect” and “sought to protect Americans in their beliefs, their thoughts,
their emotions and their sensations.” Id., at 478. Thus, “every unjusti­
fiable intrusion by the Government upon the privacy of the individual,
whatever the means employed,” should constitute an unreasonable
search under the Fourth Amendment. Ibid.
                 Cite as: 585 U. S. ____ (2018)           3

                    THOMAS, J., dissenting

Olmstead and rejected Fourth Amendment challenges to
various methods of electronic surveillance. See On Lee v.
United States, 343 U. S. 747, 749–753 (1952) (use of mi­
crophone to overhear conversations with confidential
informant); Goldman v. United States, 316 U. S. 129, 131–
132, 135–136 (1942) (use of detectaphone to hear conver­
sations in office next door).
  In the 1960’s, however, the Court began to retreat from
Olmstead. In Silverman v. United States, 365 U. S. 505
(1961), for example, federal officers had eavesdropped on
the defendants by driving a “spike mike” several inches
into the house they were occupying. Id., at 506–507. This
was a “search,” the Court held, because the “unauthorized
physical penetration into the premises” was an “actual
intrusion into a constitutionally protected area.” Id., at
509, 512. The Court did not mention Olmstead’s other
holding that intangible conversations are not “persons,
houses, papers, [or] effects.” That omission was signifi­
cant. The Court confirmed two years later that “[i]t fol­
lows from [Silverman] that the Fourth Amendment may
protect against the overhearing of verbal statements as
well as against the more traditional seizure of ‘papers and
effects.’ ” Wong Sun v. United States, 371 U. S. 471, 485
(1963); accord, Berger v. New York, 388 U. S. 41, 51 (1967).
  In Katz, the Court rejected Olmstead’s remaining hold-
ing—that eavesdropping is not a search absent a physical
intrusion into a constitutionally protected area. The
federal officers in Katz had intercepted the defendant’s
conversations by attaching an electronic device to the
outside of a public telephone booth. 389 U. S., at 348. The
Court concluded that this was a “search” because the
officers “violated the privacy upon which [the defendant]
justifiably relied while using the telephone booth.” Id., at
353. Although the device did not physically penetrate the
booth, the Court overruled Olmstead and held that “the
reach of [the Fourth] Amendment cannot turn upon the
4              CARPENTER v. UNITED STATES

                    THOMAS, J., dissenting

presence or absence of a physical intrusion.” 389 U. S., at
353. The Court did not explain what should replace
Olmstead’s physical-intrusion requirement.         It simply
asserted that “the Fourth Amendment protects people, not
places” and “what [a person] seeks to preserve as private
. . . may be constitutionally protected.” 389 U. S., at 351.
    Justice Harlan’s concurrence in Katz attempted to artic­
ulate the standard that was missing from the majority
opinion. While Justice Harlan agreed that “ ‘the Fourth
Amendment protects people, not places,’ ” he stressed that
“[t]he question . . . is what protection it affords to those
people,” and “the answer . . . requires reference to a
‘place.’ ” Id., at 361. Justice Harlan identified a “twofold
requirement” to determine when the protections of the
Fourth Amendment apply: “first that a person have exhib­
ited an actual (subjective) expectation of privacy and,
second, that the expectation be one that society is pre­
pared to recognize as ‘reasonable.’ ” Ibid.
    Justice Harlan did not cite anything for this “expecta­
tion of privacy” test, and the parties did not discuss it in
their briefs. The test appears to have been presented for
the first time at oral argument by one of the defendant’s
lawyers. See Winn, Katz and the Origins of the “Reason-
able Expectation of Privacy” Test, 40 McGeorge L. Rev. 1,
9–10 (2009). The lawyer, a recent law-school graduate,
apparently had an “[e]piphany” while preparing for oral
argument. Schneider, Katz v. United States: The Untold
Story, 40 McGeorge L. Rev. 13, 18 (2009). He conjectured
that, like the “reasonable person” test from his Torts class,
the Fourth Amendment should turn on “whether a rea­
sonable person . . . could have expected his communication
to be private.” Id., at 19. The lawyer presented his new
theory to the Court at oral argument. See, e.g., Tr. of Oral
Arg. in Katz v. United States, O. T. 1967, No. 35, p. 5
(proposing a test of “whether or not, objectively speaking,
the communication was intended to be private”); id., at 11
                 Cite as: 585 U. S. ____ (2018)            5

                    THOMAS, J., dissenting

(“We propose a test using a way that’s not too dissimilar
from the tort ‘reasonable man’ test”). After some question­
ing from the Justices, the lawyer conceded that his test
should also require individuals to subjectively expect
privacy. See id., at 12. With that modification, Justice
Harlan seemed to accept the lawyer’s test almost verbatim
in his concurrence.
  Although the majority opinion in Katz had little practi­
cal significance after Congress enacted the Omnibus
Crime Control and Safe Streets Act of 1968, Justice Har­
lan’s concurrence profoundly changed our Fourth Amend­
ment jurisprudence. It took only one year for the full
Court to adopt his two-pronged test. See Terry v. Ohio,
392 U. S. 1, 10 (1968). And by 1979, the Court was de­
scribing Justice Harlan’s test as the “lodestar” for deter­
mining whether a “search” had occurred. Smith v. Mary-
land, 442 U. S. 735, 739 (1979). Over time, the Court
minimized the subjective prong of Justice Harlan’s test.
See Kerr, Katz Has Only One Step: The Irrelevance of
Subjective Expectations, 82 U. Chi. L. Rev. 113 (2015).
That left the objective prong—the “reasonable expectation
of privacy” test that the Court still applies today. See
ante, at 5; United States v. Jones, 565 U. S. 400, 406
(2012).
                               II
   Under the Katz test, a “search” occurs whenever “gov­
ernment officers violate a person’s ‘reasonable expectation
of privacy.’ ” Jones, supra, at 406. The most glaring prob­
lem with this test is that it has “no plausible foundation in
the text of the Fourth Amendment.” Carter, 525 U. S., at
97 (opinion of Scalia, J.). The Fourth Amendment, as
relevant here, protects “[t]he right of the people to be
secure in their persons, houses, papers, and effects,
against unreasonable searches.” By defining “search” to
mean “any violation of a reasonable expectation of pri-
6              CARPENTER v. UNITED STATES

                     THOMAS, J., dissenting

vacy,” the Katz test misconstrues virtually every one of
these words.
                               A
   The Katz test distorts the original meaning of
“searc[h]”—the word in the Fourth Amendment that it
purports to define, see ante, at 5; Smith, supra. Under the
Katz test, the government conducts a search anytime it
violates someone’s “reasonable expectation of privacy.”
That is not a normal definition of the word “search.”
   At the founding, “search” did not mean a violation of
someone’s reasonable expectation of privacy. The word
was probably not a term of art, as it does not appear in
legal dictionaries from the era. And its ordinary meaning
was the same as it is today: “ ‘[t]o look over or through for
the purpose of finding something; to explore; to examine
by inspection; as, to search the house for a book; to search
the wood for a thief.’ ” Kyllo v. United States, 533 U. S. 27,
32, n. 1 (2001) (quoting N. Webster, An American Diction­
ary of the English Language 66 (1828) (reprint 6th ed.
1989)); accord, 2 S. Johnson, A Dictionary of the English
Language (5th ed. 1773) (“Inquiry by looking into every
suspected place”); N. Bailey, An Universal Etymological
English Dictionary (22d ed. 1770) (“a seeking after, a
looking for, &c.”); 2 J. Ash, The New and Complete Dic­
tionary of the English Language (2d ed. 1795) (“An en­
quiry, an examination, the act of seeking, an enquiry by
looking into every suspected place; a quest; a pursuit”); T.
Sheridan, A Complete Dictionary of the English Language
(6th ed. 1796) (similar). The word “search” was not asso­
ciated with “reasonable expectation of privacy” until Jus­
tice Harlan coined that phrase in 1967. The phrase “ex­
pectation(s) of privacy” does not appear in the pre-Katz
federal or state case reporters, the papers of prominent
                    Cite as: 585 U. S. ____ (2018)                   7

                        THOMAS, J., dissenting

Founders,2 early congressional documents and debates,3
collections of early American English texts,4 or early
American newspapers.5
                               B
   The Katz test strays even further from the text by focus­
ing on the concept of “privacy.” The word “privacy” does
not appear in the Fourth Amendment (or anywhere else in
the Constitution for that matter). Instead, the Fourth
Amendment references “[t]he right of the people to be
secure.” It then qualifies that right by limiting it to “per­
sons” and three specific types of property: “houses, papers,
and effects.” By connecting the right to be secure to these
four specific objects, “[t]he text of the Fourth Amendment
reflects its close connection to property.” Jones, supra, at
405. “[P]rivacy,” by contrast, “was not part of the political
vocabulary of the [founding]. Instead, liberty and privacy
rights were understood largely in terms of property
rights.” Cloud, Property Is Privacy: Locke and Brandeis in
the Twenty-First Century, 55 Am. Crim. L. Rev. 37, 42
(2018).
   Those who ratified the Fourth Amendment were quite
familiar with the notion of security in property. Security
in property was a prominent concept in English law. See,
e.g., 3 W. Blackstone, Commentaries on the Laws of Eng-

——————
  2 National Archives, Library of Congress, Founders Online, https://
founders.archives.gov (all Internet materials as last visited June
18, 2018).
  3 A Century of Lawmaking For A New Nation, U. S. Congressional

Documents and Debates, 1774–1875 (May 1, 2003), https://memory.loc
.gov/ammem/amlaw/lawhome.html.
  4 Corpus of Historical American English, https://corpus.byu.edu/coha;

Google Books (American), https://googlebooks.byu.edu/x.asp; Corpus of
Founding Era American English, https://lawncl.byu.edu/cofea.
  5 Readex,   America’s Historical Newspapers (2018), https://
www.readex.com/content/americas-historical-newspapers.
8                CARPENTER v. UNITED STATES

                       THOMAS, J., dissenting

land 288 (1768) (“[E]very man’s house is looked upon by
the law to be his castle”); 3 E. Coke, Institutes of Laws of
England 162 (6th ed. 1680) (“[F]or a man[’]s house is his
Castle, & domus sua cuique est tutissimum refugium
[each man’s home is his safest refuge]”). The political
philosophy of John Locke, moreover, “permeated the 18th­
century political scene in America.” Obergefell v. Hodges,
576 U. S. ___, ___ (2015) (THOMAS, J., dissenting) (slip op.,
at 8). For Locke, every individual had a property right “in
his own person” and in anything he “removed from the
common state [of] Nature” and “mixed his labour with.”
Second Treatise of Civil Government §27 (1690). Because
property is “very unsecure” in the state of nature, §123,
individuals form governments to obtain “a secure enjoy­
ment of their properties.” §95. Once a government is
formed, however, it cannot be given “a power to destroy
that which every one designs to secure”; it cannot legiti­
mately “endeavour to take away, and destroy the property
of the people,” or exercise “an absolute power over [their]
lives, liberties, and estates.” §222.
   The concept of security in property recognized by Locke
and the English legal tradition appeared throughout the
materials that inspired the Fourth Amendment. In Entick
v. Carrington, 19 How. St. Tr. 1029 (C. P. 1765)—a her­
alded decision that the founding generation considered
“the true and ultimate expression of constitutional law,”
Boyd v. United States, 116 U. S. 616, 626 (1886)—Lord
Camden explained that “[t]he great end, for which men
entered into society, was to secure their property.” 19
How. St. Tr., at 1066. The American colonists echoed this
reasoning in their “widespread hostility” to the Crown’s
writs of assistance6—a practice that inspired the Revolu­

——————
   6 Writs of assistance were “general warrants” that gave “customs

officials blanket authority to search where they pleased for goods
                     Cite as: 585 U. S. ____ (2018)                      9

                         THOMAS, J., dissenting

tion and became “[t]he driving force behind the adoption of
the [Fourth] Amendment.” United States v. Verdugo-
Urquidez, 494 U. S. 259, 266 (1990). Prominent colonists
decried the writs as destroying “ ‘domestic security’ ” by
permitting broad searches of homes. M. Smith, The Writs
of Assistance Case 475 (1978) (quoting a 1772 Boston town
meeting); see also id., at 562 (complaining that “ ‘every
householder in this province, will necessarily become less
secure than he was before this writ’ ” (quoting a 1762
article in the Boston Gazette)); id., at 493 (complaining
that the writs were “ ‘expressly contrary to the common
law, which ever regarded a man’s house as his castle, or a
place of perfect security’ ” (quoting a 1768 letter from John
Dickinson)). John Otis, who argued the famous Writs of
Assistance case, contended that the writs violated “ ‘the
fundamental Principl[e] of Law’ ” that “ ‘[a] Man who is
quiet, is as secure in his House, as a Prince in his Castle.’ ”
Id., at 339 (quoting John Adam’s notes). John Adams
attended Otis’ argument and later drafted Article XIV of
the Massachusetts Constitution,7 which served as a model
for the Fourth Amendment. See Clancy, The Framers’
Intent: John Adams, His Era, and the Fourth Amendment,
86 Ind. L. J. 979, 982 (2011); Donahue, The Original
Fourth Amendment, 83 U. Chi. L. Rev. 1181, 1269 (2016)

—————— 

imported in violation of the British tax laws.” Stanford v. Texas, 379

U. S. 476, 481 (1965).
   7 “Every subject has a right to be secure from all unreasonable

searches and seizures of his person, his house, his papers, and all his
possessions. All warrants, therefore, are contrary to right, if the cause
or foundation of them be not previously supported by oath or affirma­
tion, and if the order in the warrant to a civil officer, to make search in
suspected places, or to arrest one or more suspected persons, or to seize
their property, be not accompanied with a special designation of the
person or objects of search, arrest, or seizure; and no warrant ought to
be issued but in cases, and with the formalities prescribed by the laws.”
Mass. Const., pt. I, Art. XIV (1780).
10              CARPENTER v. UNITED STATES

                      THOMAS, J., dissenting

(Donahue). Adams agreed that “[p]roperty must be se­
cure

[...TRUNCATED 124974 of 244974 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Carroll v. Carman.md  (`case`, 5 assertions)

### content_page

```
---
title: Carroll v. Carman
type: case
citation: "574 U.S. 13 (2014)"
parallel_cite: ""
neutral_cite: ""
court: U.S.
court_level: scotus
circuit: ""
year: 2014
date_decided: 2014-11-10
docket: 14-212
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
  opinion_url: "https://www.courtlistener.com/opinion/2750102/carroll-v-carman/"
  cluster_id: 2750102
  opinion_id: null
  identity_checked: false
lake:
  record_id: Carroll v. Carman
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Knock and Talk]]"
    role: Key
related:
  - "[[Knock and Talk]]"
  - "[[Florida v. Jardines]]"
tags:
  - case
  - fourth-amendment
  - knock-and-talk
  - curtilage
  - qualified-immunity
  - per-curiam
holding: "It is not clearly established that the 'knock and talk' exception requires officers to approach only the front door; an officer who went to a side sliding-glass door that visitors could use was therefore entitled to qualified immunity, and the Supreme Court left open whether such an approach is constitutional."
aliases:
  - Carman v. Carroll
---

# Carroll v. Carman

*574 U.S. 13 (2014)* (No. 14-212) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): per curiam; identity cluster 2750102 → 574 U.S. 13, 135 S. Ct. 348, decided 2014-11-10; Rule quote string-matched to the CL opinion text 2026-07-07. The CL text carries S. Ct. star pagination, so the pin is to 135 S. Ct. 352. S9 promotes. -->

## Background
Officer Jeremy Carroll went to the Carmans' home to investigate a report about a stolen car and a possibly armed suspect. Rather than the front door, he walked into the backyard and onto a deck, entering through a sliding glass door area, where an encounter ensued. The Carmans sued under § 1983; a jury found for Carroll, but the Third Circuit reversed, holding as a matter of law that the "knock and talk" exception requires officers to begin at the front door and denying Carroll [[Qualified Immunity|qualified immunity]].

## Issue
Whether it was clearly established that the "knock and talk" exception to the warrant requirement forbids officers from approaching a home by any route other than the front door.

## Rule
The Supreme Court, [[Common Legal Terms#per-curiam|per curiam]], reversed. It held that no such rule was clearly established: the Third Circuit's sole authority did not require officers to knock at the front door before going to other visitor-accessible parts of the property, and other courts had upheld approaches to side and back entrances. The Court expressly reserved the merits: "We do not decide today whether those cases were correctly decided or whether a police officer may conduct a 'knock and talk' at any entrance that is open to visitors rather than only the front door." — 135 S. Ct. at 352. Because the contrary rule was not "beyond debate," "[t]he Third Circuit therefore erred when it held that Carroll was not entitled to qualified immunity."

## Application
[[Qualified Immunity|Qualified immunity]] protects officers unless they violate a right so settled that every reasonable officer would know it — a standard the front-door rule did not meet in 2009. Whatever the correct Fourth Amendment answer, an officer could reasonably have believed he was permitted to approach a door open to ordinary visitors, so Carroll could not be held personally liable.

## Conclusion
[[Reading and Citing Cases#certiorari-cert|Certiorari]] granted; the judgment of the Third Circuit was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]] — Officer Carroll was entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Carroll v. Carman* is a qualified-immunity decision that deliberately left the front-door question open: it neither adopted nor rejected the view that a lawful "knock and talk" (cf. *[[Florida v. Jardines]]*'s implied-license analysis) is confined to the front door, holding only that the contrary rule was not clearly established.

## Appears on
- [[Knock and Talk]] — *Key*

## Sources
- [*Carroll v. Carman*, 574 U.S. 13 (2014) (per curiam)](https://www.courtlistener.com/opinion/2750102/carroll-v-carman/) — pinpoint: 135 S. Ct. 348, 352 (the parallel reporter the CL text star-paginates; = 574 U.S. at 18–19); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "16cb8c568329845c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "574 U.S. 13 (2014)", "court": "U.S.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Carroll v. Carman", "year": "2014"}}
{"assertion_id": "32444f098ef8c7cc", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Key", "title": "Carroll v. Carman"}}
{"assertion_id": "9e0090a8436e6f2d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "It is not clearly established that the 'knock and talk' exception requires officers to approach only the front door; an officer who went to a side sliding-glass door that visitors could use was therefore entitled to qualified immunity, and the Supreme Court left open whether such an approach is constitutional.", "title": "Carroll v. Carman"}}
{"assertion_id": "81814e5ab4161672", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Carroll v. Carman", "varies_by_point": "false"}}
{"assertion_id": "b573001531d0d1f2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Carroll v. Carman"}}
```

### lake record — Carroll v. Carman

```json
{
  "schema_version": "s2.v1",
  "record_id": "Carroll v. Carman",
  "status": "under_review",
  "identity": {
    "case_name": "Carroll v. Carman",
    "case_name_short": "Carroll",
    "case_name_full": "Jeremy CARROLL v. Andrew CARMAN, Et Ux.",
    "input_case_name": "Carroll v. Carman",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2014-11-10",
    "year": 2014,
    "docket": "14-212",
    "cluster_id": 2750102,
    "lead_opinion_id": 2750102,
    "sibling_ids": [],
    "absolute_url": "/opinion/2750102/carroll-v-carman/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "574 U.S. 13",
      "volume": "574",
      "reporter": "U.S.",
      "page": "13",
      "type": 1,
      "selected_official": true,
      "source": "web-dual-leg"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "574 U.S. 13",
        "volume": "574",
        "reporter": "U.S.",
        "page": "13",
        "type": 1,
        "selected_official": true,
        "source": "web-dual-leg"
      }
    ],
    "display": "574 U.S. 13",
    "official_selection": {
      "court_class": "scotus",
      "selected": "574 U.S. 13",
      "reason": "web-dual-leg"
    },
    "web_legs": [
      {
        "source": "Google Scholar",
        "url": "https://scholar.google.com/scholar_case?case=3474605511210172307",
        "cite": "574 U.S. 13",
        "checked_date": "2026-07-07"
      },
      {
        "source": "Oyez",
        "url": "https://www.oyez.org/cases/2014/14-212",
        "cite": "574 U.S. 13",
        "checked_date": "2026-07-07"
      }
    ]
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
    "date_created": "2026-07-07T01:36:17Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:37:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:37:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "carroll-v-carman--2750102",
      "to_record_id": "Carroll v. Carman",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Carroll v. Carman

```
                 Cite as: 574 U. S. ____ (2014)            1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
   JEREMY CARROLL v. ANDREW CARMAN, ET UX.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE THIRD CIRCUIT

            No. 14–212.   Decided November 10, 2014


   PER CURIAM.
   On July 3, 2009, the Pennsylvania State Police Depart-
ment received a report that a man named Michael Zita
had stolen a car and two loaded handguns. The report
also said that Zita might have fled to the home of Andrew
and Karen Carman. The department sent Officers Jeremy
Carroll and Brian Roberts to the Carmans’ home to inves-
tigate. Neither officer had been to the home before. 749
F. 3d 192, 195 (CA3 2014).
   The officers arrived in separate patrol cars around 2:30
p.m. The Carmans’ house sat on a corner lot—the front of
the house faced a main street while the left (as viewed
from the front) faced a side street. The officers initially
drove to the front of the house, but after discovering that
parking was not available there, turned right onto the side
street. As they did so, they saw several cars parked side-
by-side in a gravel parking area on the left side of the
Carmans’ property. The officers parked in the “first avail-
able spot,” at “the far rear of the property.” Ibid. (quoting
Tr. 70 (Apr. 8, 2013)).
   The officers exited their patrol cars. As they looked
toward the house, the officers saw a small structure (ei-
ther a carport or a shed) with its door open and a light on.
Id., at 71. Thinking someone might be inside, Officer
Carroll walked over, “poked [his] head” in, and said
“Pennsylvania State Police.” 749 F. 3d, at 195 (quoting Tr.
71 (Apr. 8, 2013); alteration in original). No one was
there, however, so the officers continued walking toward
the house. As they approached, they saw a sliding glass
2                   CARROLL v. CARMAN

                         Per Curiam

door that opened onto a ground-level deck. Carroll
thought the sliding glass door “looked like a customary
entryway,” so he and Officer Roberts decided to knock on
it. 749 F. 3d, at 195 (quoting Tr. 83 (Apr. 8, 2013)).
   As the officers stepped onto the deck, a man came out
of the house and “belligerent[ly] and aggressively ap-
proached” them. 749 F. 3d, at 195. The officers identified
themselves, explained they were looking for Michael Zita,
and asked the man for his name. The man refused to
answer. Instead, he turned away from the officers and
appeared to reach for his waist. Id., at 195–196. Carroll
grabbed the man’s right arm to make sure he was not
reaching for a weapon. The man twisted away from Car-
roll, lost his balance, and fell into the yard. Id., at 196.
   At that point, a woman came out of the house and asked
what was happening. The officers again explained that
they were looking for Zita. The woman then identified
herself as Karen Carman, identified the man as her hus-
band, Andrew Carman, and told the officers that Zita was
not there. In response, the officers asked for permission to
search the house for Zita. Karen Carman consented, and
everyone went inside. Ibid.
   The officers searched the house, but did not find Zita.
They then left. The Carmans were not charged with any
crimes. Ibid.
   The Carmans later sued Officer Carroll in Federal
District Court under 42 U. S. C. §1983. Among other
things, they alleged that Carroll unlawfully entered their
property in violation of the Fourth Amendment when he
went into their backyard and onto their deck without a
warrant. 749 F. 3d, at 196.
   At trial, Carroll argued that his entry was lawful under
the “knock and talk” exception to the warrant require-
ment. That exception, he contended, allows officers to
knock on someone’s door, so long as they stay “on those
portions of [the] property that the general public is al-
                  Cite as: 574 U. S. ____ (2014)            3

                           Per Curiam

lowed to go on.” Tr. 7 (Apr. 8, 2013). The Carmans re-
sponded that a normal visitor would have gone to their
front door, rather than into their backyard or onto their
deck. Thus, they argued, the “knock and talk” exception
did not apply.
  At the close of Carroll’s case in chief, the parties each
moved for judgment as a matter of law. The District Court
denied both motions, and sent the case to a jury. As rele-
vant here, the District Court instructed the jury that the
“knock and talk” exception “allows officers without a
warrant to knock on a resident’s door or otherwise ap-
proach the residence seeking to speak to the inhabitants,
just as any private citizen might.” Id., at 24 (Apr. 10,
2013). The District Court further explained that “officers
should restrict their movements to walkways, driveways,
porches and places where visitors could be expected to go.”
Ibid. The jury then returned a verdict for Carroll.
  The Carmans appealed, and the Court of Appeals for the
Third Circuit reversed in relevant part. The court held
that Officer Carroll violated the Fourth Amendment as a
matter of law because the “knock and talk” exception
“requires that police officers begin their encounter at the
front door, where they have an implied invitation to go.”
749 F. 3d, at 199. The court also held that Carroll was not
entitled to qualified immunity because his actions violated
clearly established law. Ibid. The court therefore re-
versed the District Court and held that the Carmans were
entitled to judgment as a matter of law.
  Carroll petitioned for certiorari. We grant the petition
and reverse the Third Circuit’s determination that Carroll
was not entitled to qualified immunity.
  A government official sued under §1983 is entitled to
qualified immunity unless the official violated a statutory
or constitutional right that was clearly established at the
time of the challenged conduct. See Ashcroft v. al-Kidd,
563 U. S. ___, ___ (2011) (slip op., at 3). A right is clearly
4                    CARROLL v. CARMAN

                          Per Curiam

established only if its contours are sufficiently clear that
“a reasonable official would understand that what he is
doing violates that right.” Anderson v. Creighton, 483
U. S. 635, 640 (1987). In other words, “existing precedent
must have placed the statutory or constitutional question
beyond debate.” al-Kidd, 563 U. S., at ___ (slip op., at 9).
This doctrine “gives government officials breathing room
to make reasonable but mistaken judgments,” and “pro-
tects ‘all but the plainly incompetent or those who know-
ingly violate the law.’ ” Id., at ___ (slip op., at 12) (quoting
Malley v. Briggs, 475 U. S. 335, 341 (1986)).
   Here the Third Circuit cited only a single case to sup-
port its decision that Carroll was not entitled to qualified
immunity—Estate of Smith v. Marasco, 318 F. 3d 497
(CA3 2003). Assuming for the sake of argument that a
controlling circuit precedent could constitute clearly estab-
lished federal law in these circumstances, see Reichle v.
Howards, 566 U. S. ___, ___ (2012) (slip op., at 7), Marasco
does not clearly establish that Carroll violated the Car-
mans’ Fourth Amendment rights.
   In Marasco, two police officers went to Robert Smith’s
house and knocked on the front door. When Smith did not
respond, the officers went into the backyard, and at least
one entered the garage. 318 F. 3d, at 519. The court
acknowledged that the officers’ “entry into the curtilage
after not receiving an answer at the front door might be
reasonable.” Id., at 520. It held, however, that the Dis-
trict Court had not made the factual findings needed to
decide that issue. Id., at 521. For example, the Third
Circuit noted that the record “did not discuss the layout of
the property or the position of the officers on that prop-
erty,” and that “there [was] no indication of whether the
officers followed a path or other apparently open route
that would be suggestive of reasonableness.” Ibid. The
court therefore remanded the case for further proceedings.
   In concluding that Officer Carroll violated clearly estab-
                 Cite as: 574 U. S. ____ (2014)            5

                          Per Curiam

lished law in this case, the Third Circuit relied exclusively
on Marasco’s statement that “entry into the curtilage after
not receiving an answer at the front door might be reason-
able.” Id., at 520; see 749 F. 3d, at 199 (quoting Marasco,
supra, at 520). In the court’s view, that statement clearly
established that a “knock and talk” must begin at the
front door. But that conclusion does not follow. Marasco
held that an unsuccessful “knock and talk” at the front
door does not automatically allow officers to go onto other
parts of the property. It did not hold, however, that
knocking on the front door is required before officers go
onto other parts of the property that are open to visitors.
Thus, Marasco simply did not answer the question whether
a “knock and talk” must begin at the front door when
visitors may also go to the back door. Indeed, the house at
issue seems not to have even had a back door, let alone
one that visitors could use. 318 F. 3d, at 521.
   Moreover, Marasco expressly stated that “there [was] no
indication of whether the officers followed a path or other
apparently open route that would be suggestive of reason-
ableness.” Ibid. That makes Marasco wholly different
from this case, where the jury necessarily decided that
Carroll “restrict[ed] [his] movements to walkways, drive-
ways, porches and places where visitors could be expected
to go.” Tr. 24 (Apr. 10, 2013).
   To the extent that Marasco says anything about this
case, it arguably supports Carroll’s view. In Marasco, the
Third Circuit noted that “[o]fficers are allowed to knock on
a residence’s door or otherwise approach the residence
seeking to speak to the inhabitants just as any private
citizen may.” 318 F. 3d, at 519. The court also said that,
“ ‘when the police come on to private property . . . and
restrict their movements to places visitors could be ex-
pected to go (e.g., walkways, driveways, porches), observa-
tions made from such vantage points are not covered by
the Fourth Amendment.’ ” Ibid. (quoting 1 W. LaFave,
6                       CARROLL v. CARMAN

                              Per Curiam

Search and Seizure §2.3(f ) (3d ed. 1996 and Supp. 2003)
(footnotes omitted)). Had Carroll read those statements
before going to the Carmans’ house, he may have concluded—
quite reasonably—that he was allowed to knock on any
door that was open to visitors.*
   The Third Circuit’s decision is even more perplexing in
comparison to the decisions of other federal and state
courts, which have rejected the rule the Third Circuit
adopted here. For example, in United States v. Titemore,
437 F. 3d 251 (CA2 2006), a police officer approached a
house that had two doors. The first was a traditional door
that opened onto a driveway; the second was a sliding
glass door that opened onto a small porch. The officer
chose to knock on the latter. Id., at 253–254. On appeal,
the defendant argued that the officer had unlawfully
entered his property without a warrant in violation of the
Fourth Amendment. Id., at 255–256. But the Second
Circuit rejected that argument. As the court explained,
the sliding glass door was “a primary entrance visible to
and used by the public.” Id., at 259. Thus, “[b]ecause [the
officer] approached a principal entrance to the home using
a route that other visitors could be expected to take,” the
court held that he did not violate the Fourth Amendment.
Id., at 252.
   The Seventh Circuit’s decision in United States v.
James, 40 F. 3d 850 (1994), vacated on other grounds, 516
U. S. 1022 (1995), provides another example. There, police
——————
  * In a footnote, the Court of Appeals “recognize[d] that there may be
some instances in which the front door is not the entrance used by
visitors,” but noted that “this is not one such instance.” 749 F. 3d 192,
198, n. 6 (2014) (emphasis added). This footnote still reflects the Third
Circuit’s view that the “knock and talk” exception is available for only
one entrance to a dwelling, “which in most circumstances is the front
door.” Id., at 198. Cf. United States v. Perea-Rey, 680 F. 3d 1179, 1188
(CA9 2012) (“Officers conducting a knock and talk . . . need not ap-
proach only a specific door if there are multiple doors accessible to the
public.”).
                 Cite as: 574 U. S. ____ (2014)           7

                          Per Curiam

officers approached a duplex with multiple entrances.
Bypassing the front door, the officers “used a paved walk-
way along the side of the duplex leading to the rear side
door.” 40 F. 3d, at 862. On appeal, the defendant argued
that the officers violated his Fourth Amendment rights
when they went to the rear side door. The Seventh Circuit
rejected that argument, explaining that the rear side door
was “accessible to the general public” and “was commonly
used for entering the duplex from the nearby alley.” Ibid.
In situations “where the back door of a residence is readily
accessible to the general public,” the court held, “the
Fourth Amendment is not implicated when police officers
approach that door in the reasonable belief that it is a
principal means of access to the dwelling.” Ibid. See also,
e.g., United States v. Garcia, 997 F. 2d 1273, 1279–1280
(CA9 1993) (“If the front and back of a residence are read-
ily accessible from a public place, like the driveway and
parking area here, the Fourth Amendment is not implicated
when officers go to the back door reasonably believing it
is used as a principal entrance to the dwelling”); State v.
Domicz, 188 N. J. 285, 302, 907 A. 2d 395, 405 (2006)
(“when a law enforcement officer walks to a front or back
door for the purpose of making contact with a resident and
reasonably believes that the door is used by visitors, he is
not unconstitutionally trespassing on to the property”).
   We do not decide today whether those cases were cor-
rectly decided or whether a police officer may conduct a
“knock and talk” at any entrance that is open to visitors
rather than only the front door. “But whether or not the
constitutional rule applied by the court below was correct,
it was not ‘beyond debate.’ ” Stanton v. Sims, 571 U. S.
___, ___ (2013) (per curiam) (slip op., at 8) (quoting al-
Kidd, 563 U. S., at ___ (slip op., at 9)). The Third Circuit
therefore erred when it held that Carroll was not entitled
to qualified immunity.
   The petition for certiorari is granted. The judgment of
8                   CARROLL v. CARMAN

                         Per Curiam

the United States Court of Appeals for the Third Circuit is
reversed, and the case is remanded for further proceedings
consistent with this opinion.
                                           It is so ordered.

```

---
