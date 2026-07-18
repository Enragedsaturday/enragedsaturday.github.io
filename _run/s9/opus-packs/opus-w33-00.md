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

## GROUP: content/cases/French v. Merrill.md  (`case`, 6 assertions)

### content_page

```
---
title: "French v. Merrill"
type: case
citation: "15 F.4th 116 (2021)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, First Circuit"
court_level: coa
circuit: 1st
year: 2021
date_decided: 2021-10-01
docket: ""
authority_weight: "Binding in-circuit — 1st Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2021-10-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: French v. Merrill
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/5273192/french-v-merrill/"
  cluster_id: 5273192
  opinion_id: 5100775
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Curtilage]]"
    role: "Related (cross-doctrine)"
related: ["[[Florida v. Jardines]]", "[[Kentucky v. King]]"]
aliases: ["French v. Merrill (1st Cir. 2021)"]
tags: ["case", "fourth-amendment", "knock-and-talk", "curtilage", "implied-license", "first-circuit", "qualified-immunity"]
holding: "The scope of the 'knock and talk' exception to the warrant requirement is controlled by the implied social license to enter the…"
lake:
  record_id: French v. Merrill
  status: verified
  projected_at: 2026-07-06
---

# French v. Merrill

*15 F.4th 116 (1st Cir. 2021)* · U.S. Court of Appeals, First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Detectives investigating French repeatedly entered the [[Curtilage|curtilage]] of his home to conduct "knock and talks." During a final visit around 5:00 a.m., officers went onto the property, knocked on the front door and then on French's bedroom window, peered through a drawn window covering, and shined a flashlight inside. French sued under § 1983, and the officers asserted [[Qualified Immunity|qualified immunity]], contending their conduct did not violate clearly established Fourth Amendment law.

## Issue
Whether officers who repeatedly entered the [[Curtilage|curtilage]] of a home and engaged in intrusive, pre-dawn conduct in the course of attempted knock and talks exceeded the implied social license — and whether [[Florida v. Jardines]] clearly established the unlawfulness of that conduct.

## Rule
The [[Knock and Talk|knock-and-talk]] exception is bounded by the implied social license, which is limited in both area and purpose. The court explained that the license's scope "is limited not only to a particular area but also to a specific purpose, both of which are defined by what a homeowner might reasonably expect from a private citizen on the homeowner's curtilage." — *French v. Merrill*, 15 F.4th 116 (1st Cir. 2021) (slip op., at 39). ^pin-op39

Officers who exceed that purpose through intrusive, repeated entries fall outside the license: "The officers in this case, like the officers in Jardines, in the absence of any license to do so, 'physically intrud[ed]' on a suspect's property repeatedly and engaged in intrusive conduct that no reasonable visitor could have understood as impliedly authorized by a resident." — *Id.* (slip op., at 39). ^pin-op39a

## Application
The officers came onto French's [[Curtilage|curtilage]] repeatedly and, on the final pre-dawn entry, knocked on his bedroom window, peered through a drawn covering, and shined a light inside — conduct no homeowner would understand a private visitor at 5:00 a.m. to be impliedly licensed to undertake. Because that conduct exceeded the purpose-limited implied license, it was a Fourth Amendment intrusion, and *[[Florida v. Jardines|Jardines]]* had clearly established as much.

## Conclusion
The officers' repeated, intrusive entries exceeded the implied social license and violated French's clearly established Fourth Amendment rights; the officers were not entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 1st Cir.**
- No negative treatment. *French* applies [[Florida v. Jardines]] to the [[Knock and Talk|knock-and-talk]]: the implied license is limited by area and purpose, and repeated or intrusive police conduct on the [[Curtilage|curtilage]] exceeds it even without a drug-sniffing dog.

## Appears on
- [[Knock and Talk]] — *Key — Progeny / Refinement*

## Sources
- *French v. Merrill*, 15 F.4th 116 (1st Cir. 2021) — https://www.courtlistener.com/opinion/5273192/french-v-merrill/ — pinpoints given as slip-opinion pages (slip op., at 39); CourtListener carries the slip opinion, paginated by slip page (cluster 5273192 → opinion 5100775).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "20a0c2be4f405405", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "15 F.4th 116 (2021)", "court": "U.S. Court of Appeals, First Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "French v. Merrill", "year": "2021"}}
{"assertion_id": "68bc8689289b9ce8", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Related (cross-doctrine)", "title": "French v. Merrill"}}
{"assertion_id": "699ac45f934cbecd", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The scope of the 'knock and talk' exception to the warrant requirement is controlled by the implied social license to enter the…", "title": "French v. Merrill"}}
{"assertion_id": "716d41338cce4bd2", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Key — Progeny / Refinement", "title": "French v. Merrill"}}
{"assertion_id": "172fe2aefcf2b6f2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 1st Cir.", "title": "French v. Merrill"}}
{"assertion_id": "19e653e0c9eb86f8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2021-10-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "French v. Merrill", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "French v. Merrill", "varies_by_point": "false"}}
```

### lake record — French v. Merrill

```json
{
  "schema_version": "s2.v1",
  "record_id": "French v. Merrill",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "French v. Merrill",
    "case_name_short": "French",
    "case_name_full": "",
    "input_case_name": "French v. Merrill",
    "court": "U.S. Court of Appeals, First Circuit",
    "court_id": "ca1",
    "court_level": "coa",
    "circuit": "1st",
    "state": null,
    "date_decided": "2021-10-01",
    "year": 2021,
    "docket": null,
    "cluster_id": 5273192,
    "lead_opinion_id": 5100775,
    "sibling_ids": [
      5100775
    ],
    "absolute_url": "/opinion/5273192/french-v-merrill/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "15 F.4th 116",
      "volume": "15",
      "reporter": "F.4th",
      "page": "116",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "15 F.4th 116",
        "volume": "15",
        "reporter": "F.4th",
        "page": "116",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "15 F.4th 116",
    "official_selection": {
      "court_class": "coa",
      "selected": "15 F.4th 116",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op39",
      "page": null,
      "quote": "During a final visit around 5:00 a.m., officers went onto the property, knocked on the front door and then on French's bedroom window, peered through a drawn window covering, and shined a flashlight inside. French sued under \u00a7 1983, and the officers asserted qualified immunity, contending their conduct did not violate clearly established Fourth Amendment law. ## Issue Whether officers who repeatedly entered the curtilage of a home and engaged in intrusive, pre-dawn conduct in the course of attempted knock and talks exceeded the implied social license \u2014 and whether [[Florida v. Jardines]] clearly established the unlawfulness of that conduct. ## Rule The knock-and-talk exception is bounded by the implied social license, which is limited in both area and purpose. The court explained that the license's scope",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op39a",
      "page": null,
      "quote": "The officers in this case, like the officers in Jardines, in the absence of any license to do so, 'physically intrud[ed]' on a suspect's property repeatedly and engaged in intrusive conduct that no reasonable visitor could have understood as impliedly authorized by a resident.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-10-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "French v. Merrill",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Johnson v. City of Biddeford",
          "cluster_id": 9540774,
          "cite": [
            "92 F.4th 367"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harson Chong v. United States",
          "cluster_id": 10040367,
          "cite": [
            "112 F.4th 848"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morgan v. Garland",
          "cluster_id": 10265780,
          "cite": [
            "120 F.4th 913"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malachi I. Yahtues v. Old Colony Correctional Center et al.",
          "cluster_id": 10699377,
          "cite": [
            "2024 DNH 031"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shawn Murphy v. Strafford County et al.",
          "cluster_id": 10699233,
          "cite": [
            "2022 DNH 022"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fernando Sanchez v. Warden, FCI Berlin",
          "cluster_id": 10695006,
          "cite": [
            "2023 DNH 051"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Doe, et al. v. P Commissioner, New Hampshire Department of Health and Human Services",
          "cluster_id": 10694979,
          "cite": [
            "2023 DNH 020"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Patten v. P Metropolitan Property and Casualty Insurance Company",
          "cluster_id": 10694051,
          "cite": [
            "2022 DNH 072"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America v. Jos\u00e9 Luis Guerrero Nu\u00f1ez, et al.",
          "cluster_id": 10699378,
          "cite": [
            "2025 DNH 015"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Melody Costenbader v. Home Depot USA, Inc. and W/S North Hampton Properties BB c/o WS Asset Management, Inc.",
          "cluster_id": 10698848,
          "cite": [
            "2024 DNH 057"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sevelitte v. The Guardian Life Insurance Company of America",
          "cluster_id": 10292452,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The People v. Devon T. Butler",
          "cluster_id": 9453233,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "French v. Merrill:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(5100775) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca1)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      },
      "lane2_top_cited": {
        "query": "cites:(5100775)",
        "reviewed": 19,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 12,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(5100775)",
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
    "complete_query": "cites:(5100775)",
    "indexed_citing_opinions": 19,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 5100775,
        "count": 19,
        "count_source": "search"
      }
    ],
    "citation_count": 57,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/french-v-merrill.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 19,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 5100775,
        "cited_id": 77385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 100047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 137733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 148957,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 195798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 198711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 198991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 199851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 200983,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 201160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 201366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 201394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 201990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 204049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 345713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 536025,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 716599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 729931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 1013984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 1448451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 2773276,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 2844024,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 3155905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 3187625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 3211696,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 4168223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 4198889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 4209917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 4238107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 4269964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 4412394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 4582848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 4766420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 7234664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9420616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9429232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9429563,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9430379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9431119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9432240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9434318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9434540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9434715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9441559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9820073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9822082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5100775,
        "cited_id": 9873344,
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
    "date_created": "2026-07-05T05:01:43Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:01:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:01:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:04:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:01:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — French v. Merrill

```
          United States Court of Appeals
                     For the First Circuit

No. 20-1650

                      CHRISTOPHER FRENCH,

                     Plaintiff, Appellant,

                               v.

 DANIEL MERRILL, individually and in his official capacity as a
  Sergeant in the Police Department of the Town of Orono; JOSH
  EWING, individually and in his official capacity as Chief of
   Police of the Town of Orono; TOWN OF ORONO; TRAVIS MORSE,
  individually and in his official capacity; CHRISTOPHER GRAY,
    individually and in his official capacity; NATHAN DROST,
           individually and in his official capacity,

                     Defendants, Appellees.


          APPEAL FROM THE UNITED STATES DISTRICT COURT
                    FOR THE DISTRICT OF MAINE

         [Hon. John C. Nivison, U.S. Magistrate Judge]


                             Before

                   Lynch, Lipez, and Barron,
                        Circuit Judges.


     Timothy C. Woodcock for appellant.
     Kasia Soon Park, with whom Edward R. Benjamin, Jr.      and
Drummond Woodsum were on brief, for appellees.


                        October 1, 2021
           LIPEZ,   Circuit Judge.          Appellant Christopher French

claims   that   police   officers    in     Orono,   Maine,   violated   his

constitutional rights during two encounters in 2016 -- one in

February and one in September -- both of which resulted in his

warrantless arrests on charges that were later dropped.             French

brought this action for damages under 42 U.S.C. § 1983 against the

Town of Orono, the chief of the Orono Police Department, and four

of the officers with whom he interacted during the two episodes.

The district court       granted summary judgment        in favor of the

defendants on all counts. French appeals only the district court's

entry of summary judgment on Counts I and IX alleging that the

individual officers violated his Fourth Amendment rights during

the February and September incidents respectively.1

           After careful review, we affirm the district court's

entry of summary judgment on Count I, relating to the February

incident. We    reverse on Count IX,          relating to the September

incident, because the unconstitutional conduct of the officers

violated the clearly established law of the Supreme Court as set

forth in Florida v. Jardines, 569 U.S. 1, 6 (2013).




     1 The remaining eleven counts alleged violations of French's
Fifth Amendment, Sixth Amendment, Eighth Amendment, and procedural
Due Process rights, as well as various state law tort claims,
supervisory liability claims against Town of Orono Police Chief
Joshua Ewing, and municipal liability claims against the Town of
Orono. None of those claims are at issue on appeal.


                                    - 2 -
                                         I.

            We   describe    below     each    of    the     challenged   episodes

between French and the law enforcement officers.                    We rely on the

parties' limited stipulated facts2 and recount the remaining facts

as they were presented to the district court on summary judgment

in the light most favorable to French as the non-moving party.

See, e.g., McKenney v. Mangino, 873 F.3d 75, 78 (1st Cir. 2017).

A. The February 2016 Incident

            In February 2016, French was a student at the University

of Maine and was dating a fellow student, Samantha Nardone.                      In

the early morning hours of February 18th, French and Nardone had

an argument at Nardone's residence after a night at the local bars.

A neighbor called the police and reported that the couple had been

fighting loudly.

            Officer    Nathan    Drost,       Sergeant     Daniel    Merrill,   and

another officer from the Orono Police Department3 responded to the

neighbor's call at approximately 1:00 a.m.                     Upon arrival, the

officers    observed    French     and    Drew      White,    one    of   Nardone's

roommates,    standing      on   the   sidewalk      in    front     of   Nardone's



     2 The parties stipulated to the identity of the officers
involved, the timing of the events, the addresses of the relevant
locations, and the authenticity of video recording of the events
from body cameras and police cruisers. They also stipulated to
other minor facts which we will identify where relevant.
     3   The third officer was not named as a defendant in this case.


                                       - 3 -
residence.   A few moments later, Nardone and her other roommate,

Alicia McDonald, came outside.    Drost questioned Nardone, White,

and McDonald, who all confirmed that French and Nardone had been

involved in a domestic dispute.

          Nardone told the officers that she and French had had

similar disputes in the past, but that French had never been

physically violent.    She also said that she did not wish to press

charges, but that she did want to end her relationship with French

and wanted him to leave her alone for the night.     Drost directed

French to go home and cautioned him that returning to Nardone's

residence within 24 hours would result in a criminal trespass

warning that would ban French from the premises for a year.      Drost

also informed French that Nardone wanted her personal property

returned the following day and offered to facilitate an exchange.

          French   complied   with   Drost's   directive   and   left

Nardone's residence.    During his walk to his apartment -- which

was just a short distance away -- French sent Nardone several

offensive text messages.4     Nardone showed the messages to the

officers, who were still present.       At that point, the officers

informed Nardone that they could serve French with a notice to

stop harassing her and, if he continued to harass her, French could

be arrested and charged with a crime.


     4 The parties stipulated to the content and timing of all
messages French sent to Nardone on February 18, 2016.


                                - 4 -
            At Nardone's request, the officers caught up with French

outside of his residence and served him with a Cease Harassment

Notice ("CHN").        The CHN informed French that he was "forbidden

from engaging, without reasonable cause, in any course of conduct

with the intent to harass, torment or threaten . . . Samantha

Nardone."    Less than an hour after receiving the notice, French

sent   Nardone   two    more   messages    via   Snapchat    declaring   their

relationship over, threatening suicide, and inviting her to his

forthcoming funeral.

            Later   that   day,   French    sent   Nardone    a   message   via

Instagram asking if she was "ok" and assuring her that "everything

is fixable."     Having received no response, French sent Nardone

several emails approximately four hours later asking to "talk

please" and explaining that he wanted to return some of her

property.    French maintains that he was trying to comply with

Officer Drost's directive to return Nardone's property that day.

Two and a half hours later, French sent Nardone another email

lamenting that she refused to respond to him and insisting that he

only wanted to talk to her about their argument.                   Forty-five

minutes or so later, French sent Nardone another message inquiring

about whether he could drop off Nardone's property.

            At around 7:30 p.m. that evening, Officer Drost called

Nardone to check in. Nardone reported that French had been calling




                                    - 5 -
her5 and sending her messages via text, email, and various social

media platforms throughout the day.        She also told Drost that some

of her friends had told her that French was looking for her on the

University of Maine campus and that she had seen French during a

trip to a local store with a friend and assumed French was

following her.     Nardone agreed to go to the Orono Police Station

to complete a sworn written statement.

            Nardone's    statement     recounted    her   version    of   the

overnight dispute, described French's attempts to communicate with

her   throughout   the    day,   and    stated     that   French's   conduct

"terrified" her.     While at the police station, Nardone received

additional communications from French, which she showed to the

officers.    She also provided Officer Drost copies of all other

messages she had received from French on February 18, 2016.6               At

10:54 p.m., French emailed Nardone asking where she was, followed

by a second email about forty-five minutes later stating "I will

find u."    Nardone asked the officers whether French was in trouble

and they replied that he was.




      5Several calls were from a "blocked" number. Nardone did
not answer those calls, but she assumed they were from French.
French appears to concede that he made at least some of the blocked
calls.
      6The parties stipulated that the copies Nardone provided to
Officer Drost were authentic.


                                  - 6 -
              Based on the overnight events, their conversations with

Nardone,   and      French's   continued   attempts   to   contact   Nardone,

Officer Drost and Sergeant Merrill decided to arrest French for

harassment.      Nardone agreed to assist in that effort.            The next

time French called Nardone, at 12:30 a.m. on February 19th, she

was   still    at    the   police   station   and   answered   the   call   on

speakerphone, with the officers listening.             Nardone told French

that he was "not supposed" to talk to her, and neither officer

corrected Nardone's apparent misunderstanding of the CHN, which

prohibited harassment but not all communication.           French responded

that he was concerned for Nardone's safety and was simply trying

to discuss their fight with her.

              Nardone agreed to meet French at her residence in the

early morning hours of February 19th.            Drost accompanied Nardone

home and waited inside for French.            Upon French's arrival, Drost

promptly arrested him for harassing Nardone.               The charges were

eventually dropped by the state for insufficient evidence.

B. The September 2016 Incident

              At 3:19 a.m. on September 14, 2016, the Orono Police

Department received a report of a possible break-in at Nardone's

residence.       Orono Police Officers Travis Morse and Christopher




                                     - 7 -
Gray responded and, upon their arrival, obtained sworn statements

from Nardone and her roommate, McDonald.7

           Nardone reported that, at some point after the February

incident, Nardone and French reconciled.     She explained that she

was not dating French, but that they had seen each other at a local

bar earlier that evening.    She told the officers that when she was

driving away from the bar, French ran into the street toward her

vehicle and accused her of drunk driving.       French denies that

allegation.   Nardone recalled that, upon arriving home, she and

her roommate locked the doors, Nardone placed her phone on her

bedside table, and she went to sleep around 12:30 a.m.     When she

awoke at 3:00 a.m., her phone was missing.     Nardone and McDonald

looked around for the phone and discovered that their apartment

door was unlocked.   Nardone told Officers Morse and Gray that she

suspected French had broken in and stolen her cell phone.       She

also explained that French had taken her keys the prior week and

had not yet returned them.    Sometime between 4:00 and 4:30 a.m.,

the officers left Nardone's residence and returned to the police

station.

           Shortly thereafter, at approximately 4:43 a.m., Officers

Morse and Gray responded to a second call from Nardone reporting

that she and her roommate had seen French attempting to enter their


     7 Officer Morse wore a body camera that recorded the events
of the morning. Officer Gray did not wear a body camera.


                                - 8 -
home, but that he had run off when the women screamed.                    As the

officers approached            Nardone's building, they received another

report that French had just been seen running down the street

toward          his   apartment.    They   then   went   directly   to   French's

apartment.             At some point, two additional officers, Detective

Fearon and Officer Orr from the nearby Old Town Police Department,

arrived on the scene.8

                  French's residence had a small front porch with a single

door.       Appellees describe French's residence as "more akin to an

apartment building" -- presumably compared to a single-family home

-- but they fail to further explain that comparison.                 All we can

glean from the record is that the dwelling has a single front

entryway, three young adult males lived in the residence, there is

a single kitchen, and French had a separate bedroom.                Viewed from

the street, a driveway is adjacent to the residence on the right,

and, on the left, a narrow strip of grass -- four or five feet

wide       --    separates   the   property   from   the   neighbor's    adjacent

driveway.             On the left side of French's residence, there is a

cellar window at ground level and a bedroom window that is low

enough for a person of average height to reach the window frame.


       The record does not provide an explanation for why police
       8

officers from both Orono and Old Town responded to Nardone's 911
call. It appears that Nardone's residence was located in Orono
but was close to the Old Town line.      In any event, Detective
Fearon, Officer Orr, and the Old Town Police Department were not
named as defendants in French's complaint.


                                        - 9 -
            Upon their arrival at French's apartment, the officers

sought to speak with French about his suspected criminal activity.

In pursuit of that goal, the officers entered the curtilage of

French's home several times to try to convince him to come outside

and talk.    That is, the officers knocked on the front door and

French's bedroom window frame and repeatedly yelled for French to

come to the front door.        We recount the details of the officers'

misconduct within the curtilage of French's home in Part IV.

            Eventually, French reluctantly came to the door ("When

I went to the door to speak to the police, I felt I had no

choice.").      Officer Morse asked French whether he had been at

Nardone's residence.      According to Morse, French's response was

jumbled and did not make sense. Morse asked French about Nardone's

cell phone and French responded that he did not have it.             The

officers pressed French further and, eventually, he said the phone

was inside and he agreed to retrieve it.        The officers told French

he could not reenter the residence without an officer, so French,

not wanting the officers to enter his home, asked his roommate,

Corey Andrews, to look for the cell phone.          After a few moments,

Andrews returned and reported that his search was unsuccessful.

French   told   Andrews   to   check   the   basement   stairs.   Shortly

thereafter, Andrews returned with Nardone's phone.

            French told the officers that he had visited Nardone's

residence for help with a puppy that he had recently adopted, but


                                  - 10 -
that he had entered only the front entryway.         He claimed that he

found the phone on the ground outside of Nardone's building.         He

insisted that he had picked it up with the intention of returning

it to Nardone the following day.           The officers deemed French's

story not credible and arrested him for burglary at around 5:30

a.m.        The state subsequently dismissed all charges because "the

victim refuse[d] to cooperate and [wa]s out of state."

C. Procedural History

               In May 2018, French filed a complaint against the Orono

officers involved in the February and September 2016 incidents,

seeking damages under 42 U.S.C. § 1983 for violations of his Fourth

Amendment rights.9      Specifically, he claimed that he was arrested

without probable cause in February 2016 and that, in September

2016, the officers engaged in an unlawful and warrantless search

and seizure.10       Following discovery, the district court entered

summary judgment in favor of the defendants on all counts.



       As we have explained, French also sued the Town of Orono
       9

and the police chief and brought a variety of other constitutional
and state tort law claims against the officers, but none of those
claims are at issue in this appeal. See supra note 1.
       French labels his September 2016 Fourth Amendment claim as
       10

an unlawful seizure and explains in his reply brief that he has
maintained throughout these proceedings that the officers seized
him when they "effectively coerc[ed] him to come to the door
against his will." Appellees correctly note, however, that the
thrust of French's argument on appeal is whether the officers
violated his Fourth Amendment rights when they entered his
curtilage without a warrant to conduct several investigatory
"knock and talks." That is an unlawful search claim. Hence, we


                                  - 11 -
            Regarding the February 2016 incident, the district court

concluded that the officers had probable cause to arrest French

for harassment and, even if they did not, the question of probable

cause was so debatable that the officers were entitled to qualified

immunity.   As for the September 2016 incident, the court concluded

that "a fact finder could find that the officers' multiple attempts

to persuade [French] to come to the door at an early morning hour,

including attempts at a location other than the front door (i.e.,

a window of the home), [were] unreasonable and not within the

permissible knock and talk exception to the Fourth Amendment

warrant requirement."     The court went on to conclude, however,

that the officers' conduct was protected by qualified immunity

because there was no clearly established law that rendered their

conduct unlawful.

                                 II.

            We review a district court's grant of summary judgment

de novo, viewing the record in the light most favorable to the

non-moving party.     Santiago-Ramos v. Centennial P.R. Wireless

Corp., 217 F.3d 46, 52 (1st Cir. 2000).           Summary judgment is

appropriate "if the movant shows that there is no genuine dispute

as to any material fact and the movant is entitled to judgment as

a matter of law."   Fed. R. Civ. P. 56(a).     A genuine dispute as to


limit our analysis to whether          the   conduct   of   the   officers
constituted an unlawful search.


                               - 12 -
a material fact exists if a fact that "carries with it the

potential to affect the outcome of the suit" is disputed such that

"a reasonable jury could resolve the point in the favor of the

non-moving party." Santiago-Ramos, 217 F.3d at 52 (quoting Sánchez

v. Alvarado, 101 F.3d 223, 227 (1st Cir. 1996)).

           We begin by considering French's claim that he was

improperly arrested without probable cause in February 2016 and

then turn to his contentions concerning the September events.

                                  III.

           The Fourth Amendment protects an individual's right to

be free from unreasonable seizure.          U.S. Const. amend. IV.          A

warrantless arrest by a law enforcement officer is a reasonable

seizure under the Fourth Amendment "where there is probable cause

to believe that a criminal offense has been or is being committed."

Devenpeck v. Alford, 543 U.S. 146, 152 (2004).              Probable cause

exists   where   "at   the   moment   of   the   arrest,    the   facts   and

circumstances within the [officers'] knowledge and of which they

had reasonably reliable information were adequate to warrant a

prudent person in believing that the object of his suspicions had

perpetrated or was poised to perpetrate an offense."               Roche v.

John Hancock Mut. Life Ins. Co., 81 F.3d 249, 254 (1st Cir. 1996).

In asking whether probable cause existed at the time of the arrest,

we look to the "totality of the circumstances."            United States v.

Rivera, 825 F.3d 59, 63 (1st Cir. 2016).         In doing so, we recognize


                                 - 13 -
that    "probable    cause   is   a   fluid    concept    --   turning   on   the

assessment of probabilities in particular factual contexts -- not

readily, or even usefully, reduced to a neat set of legal rules."

Illinois v. Gates, 462 U.S. 213, 232 (1983).

            Officer Drost and Sergeant Merrill arrested French for

harassment.       Under Maine law, an officer may arrest "[a]ny person

who the officer has probable cause to believe has committed . . .

harassment." Me. Rev. Stat. tit. 17-A, § 15(1)(A)(12). Harassment

is defined in the statute as "engag[ing] in any course of conduct

with the intent to harass, torment or threaten another person,

[a]fter having been notified, in writing or otherwise, not to

engage in such conduct" by a law enforcement officer within one

year or by a court.      Id. § 506-A(1)(A)(1).          The notice requirement

was met when French was served with the CHN, which tracked the

language of § 506-A(1)(A)(1).          French does not contest notice.         He

claims only that the officers lacked probable cause to arrest him.

            The    undisputed     facts   show   that    French   used   several

different communication platforms to call and message Nardone

repeatedly despite receiving no response from her.11               The content

of the messages ranged from pleas to talk and attempts to arrange



        French contends in his brief that "[t]here is no clear
       11

evidence that Nardone ever read [French's] messages."          The
stipulated facts demonstrate, however, that Nardone described the
messages she received from French to Drost and provided Drost with
screenshots of the messages.


                                      - 14 -
an exchange of property to threatening suicide, inviting Nardone

to his funeral, and telling Nardone that he would "find" her.

Nardone provided a sworn statement to the Orono Police explaining

that French's conduct terrified her.     She also reported to the

officers that French had been looking for her on the University of

Maine campus12 and that he had followed her to the parking lot of

a local store.   Those facts, considered in the totality of the

circumstances, were sufficient to support a finding of probable

cause to believe that French was engaging in a course of conduct

with the intent to torment, threaten, or harass Nardone.

          French's arguments to the contrary are unpersuasive.   He

first argues that the officers erroneously misunderstood the CHN

as prohibiting all contact, even lawful contact, with Nardone.

The record supports that claim, but it does not alter the probable

cause analysis, which is based on objective factors and does not


     12 French denies this allegation and contends that the
officers could not rely on the information to establish probable
cause because it was hearsay -- Nardone told the officers that she
learned French was looking for her on campus from a friend. We
have explained, however, that "hearsay may contribute to the
existence of probable cause so long as there is a 'substantial
basis' for crediting the hearsay information." United States v.
Poulack, 556 F.2d 83, 87 (1st Cir. 1997). Here, the officers found
Nardone credible and articulate, and reviewed corroborating
messages about the incident from her phone. Hence, the officers
were permitted to rely on that information to support their finding
of probable cause. See Forest v. Pawtucket Police Dep't, 377 F.3d
52, 57 (1st Cir. 2004) (explaining that officers are entitled to
rely upon a "credible complaint by a victim to support a finding
of probable cause" without corroborating every aspect of the
complaint).


                              - 15 -
account for the "actual motive or thought process of the officer."

Holder v. Town of Sandown, 585 F.3d 500, 504 (1st Cir. 2009)

(quoting Bolton v. Taylor, 367 F.3d 5, 7 (1st Cir. 2004)).                       The

issue is whether French's cumulative communications and behavior

provided a reasonable basis for the officers to conclude that he

engaged in conduct criminalized by the state statute, not whether

the officers also took into account some contact that -- viewed in

isolation -- actually may have been lawful.

           French also contends that the district court's finding

of probable cause cannot stand because the court failed to compare

the facts known to the officers with the elements of the statute

-- including intent -- when assessing probable cause.                       However,

probable cause is a "fluid concept," and a district court need not

engage in an "excessively technical dissection" of the elements

supporting probable cause.          Gates, 462 U.S. at 232, 234.              Such a

technical assessment confuses probable cause with the standard

required to secure a criminal conviction.                Id.

           Here,    Drost    and    Merrill       were   aware      of     reasonably

reliable   facts    that    demonstrated      a    pattern     of    unwanted    and

continued contact that ranged from innocuous to threatening, and

they   reasonably   inferred       criminal   intent      from      that    objective

information.   See Cox v. Hainey, 391 F.3d 25, 34 (1st Cir. 2004)

("[T]he practical restraints on police in the field are great[]

with respect to ascertaining intent and, therefore, the latitude


                                     - 16 -
accorded to officers considering the probable cause issue in the

context of mens rea crimes must be correspondingly great.").

          French's   attempt   to   explain   away   each   of   the   many

messages he sent to Nardone -- by claiming he was seeking to

exchange property or expressing concern for her wellbeing -- is

similarly unpersuasive.    Probable cause is based on the totality

of the facts and circumstances known to the officers at the time

of the arrest.   See United States v. Flores, 888 F.3d 537, 544

(1st Cir. 2018) ("Attempting to analyze each piece of evidence in

a vacuum is inconsistent with Supreme Court case law, which makes

pellucid that each item is to be considered as part of the totality

of the circumstances.").   Whether French had a seemingly innocent

reason for sending a particular message or making a particular

call is thus irrelevant.    The frequency, content, and context of

the messages and calls collectively, in combination with the other

facts and circumstances known to the officers -- Nardone's written

statement, allegations that French was looking for Nardone on

campus, and his following her to a local store -- were adequate to

support a finding of probable cause.

          In sum, the district court did not err in concluding

that the record supported a finding that the officers had probable

cause to arrest French for harassing Nardone.               Even if that

conclusion was debatable -- and for the reasons already explained,

we do not think it is -- qualified immunity would attach and


                                - 17 -
French's claim would still fail.   As the district court explained,

it is well established that "in the case of a warrantless arrest,

if the presence of probable cause is arguable or subject to

legitimate question, qualified immunity will attach."      Cox, 391

F.3d at 31.    The district court thus properly granted summary

judgment in favor of Officer Drost and Sergeant Merrill on French's

Fourth Amendment claim arising out of the February 2016 arrest.

                                IV.

           In the realm protected by the Fourth Amendment, the "home

is first among equals." Jardines, 569 U.S. at 6. To give practical

effect to the protection of the home, its "curtilage" -- the area

"immediately surrounding and associated with the home" -- is

treated as "part of the home itself" and subject to the same

heightened protection.   Id. (quoting Oliver v. United States, 466

U.S. 170, 180 (1984)).    French contends that Officers Morse and

Gray violated his Fourth Amendment rights when, in the early

morning hours of September 14, 2016, they entered the curtilage of

his home, repeatedly knocked on his front door and bedroom window,

shouted his name, and urged him to answer the door, all without a

warrant and in an attempt to investigate whether he had committed

a crime.

           The district court agreed that "a fact finder could find

that the officers' multiple attempts to persuade [French] to come

to the door at an early morning hour, including attempts at a


                               - 18 -
location other than the front door (i.e., a window of the home),"

went beyond a permissible "knock and talk" and thus violated

French's Fourth Amendment rights.                However, the district court

concluded that the unlawfulness of the officers' actions was not

"clearly established" at the time and, thus,                       that    they were

entitled to qualified immunity.

              The officers do not challenge on appeal the district

court's finding on the constitutional violation issue.                      Thus, we

focus our qualified immunity analysis on whether the unlawfulness

of the officers' conduct was "clearly established" at the time of

the events in this case.

              A violation of "clearly established" law means that the

law rendering the officers' conduct unlawful was "sufficiently

clear"   at    the    time    such    that   a   "'reasonable      official    would

understand that what he is doing' is unlawful."                          District of

Columbia v. Wesby, 138 S. Ct. 577, 589 (2018) (quoting Ashcroft v.

al-Kidd,      563    U.S.    731,    741   (2011)).        In   other     words,   the

unconstitutionality of the officer's conduct must be beyond debate

in light of an existing principle of law "dictated by 'controlling

authority'     or      'a    robust    consensus      of   cases    of    persuasive

authority.'"        Id. at 589-90 (quoting al-Kidd, 563 U.S. at 741-42).

              The existing legal principle need not be derived from a

case "directly on point," but precedent must "place[] the statutory

or constitutional question beyond debate."                 White v. Pauly, 137 S.


                                       - 19 -
Ct. 548, 551 (2017) (per curiam) (quoting Mullenix v. Luna, 577

U.S. 7, 12 (2015)); see also Taylor v. Riojas, 141 S. Ct. 52, 53-

54 (2020) (per curiam) (reversing the Fifth Circuit's conclusion

that the officers were not given "fair warning" that "prisoners

could not be housed in cells teeming with human waste for only six

days" because, even though there was no controlling precedent

directly on point, "no reasonable correctional officer could have

concluded that . . . it was constitutionally permissible to house

[the plaintiff] in such deplorably unsanitary conditions for such

an extended period of time").     To that end, general statements of

the law may give "'fair and clear warning' to officers" so long

as, "in the light of the pre-existing law[,] the unlawfulness [of

their conduct is] apparent."       White, 137 S. Ct. at 552 (first

quoting United States v. Lanier, 520 U.S. 259, 271 (1997); then

quoting Anderson v. Creighton, 483 U.S. 635, 640 (1987)); see also

Hope v. Pelzer, 536 U.S. 730, 741 (2002) ("[O]fficials can still

be on notice that their conduct violates established law even in

novel factual circumstances.").     A rule is too general, however,

"if the unlawfulness of the officer's conduct 'does not follow

immediately   from   the   conclusion   that   [the   rule]   was   firmly

established.'"   Wesby, 138 S. Ct. at 590 (quoting Anderson, 483

U.S. at 641).

          Against that backdrop, we conclude that, in light of

Jardines and the nature of the conduct here, taken as whole, no


                                - 20 -
reasonable officer could have thought that what the Orono police

did was consistent with the Fourth Amendment.       To understand why,

we first review Jardines; we then turn to the facts of this case.

A. Florida v. Jardines

             In Jardines, the Miami-Dade Police Department received

a tip that the defendant was growing marijuana in his home.            569

U.S. at 3.     After surveilling the home for a period of time, two

officers entered the curtilage with a drug-sniffing canine ("K-

9").    Id. at 4.     On the defendant's front porch, the dog alerted

to the presence of drugs.      Id.   Based on the dog's signaling, the

officers applied for and secured a search warrant.           Id.     Upon

executing the warrant, the officers discovered several marijuana

plants in the defendant's home and charged the defendant with drug

trafficking.    Id.    At trial, the defendant sought to suppress the

marijuana evidence as the fruit of an unlawful search.          Id. at 4-

5.     The trial court granted the motion and the state appellate

court reversed. Id. at 5.      The Florida Supreme Court then reversed

the appellate court and the United States Supreme Court granted

certiorari.    Id.

             Justice Scalia, writing for the majority, labeled the

case    as   "straightforward."      Id.    The   officers   entered     a

constitutionally protected area -- the curtilage of the home --

without a warrant to investigate the commission of a crime and,

hence, the Fourth Amendment was implicated.       Id. at 6-7.    Whether


                                  - 21 -
the Fourth Amendment was violated, the Court explained, required

an    assessment   of   whether    the     officers'     investigation     in   a

constitutionally    protected      area    "was    accomplished       through   an

unlicensed physical intrusion."           Id. at 7.      In the Court's words,

"an officer's leave to gather information is sharply circumscribed

when he steps off [public] thoroughfares and enters the Fourth

Amendment's protected areas."        Id.    Because it was undisputed that

the officers "had all four of their feet and all four of their

companion's   firmly    planted     on    the   constitutionally       protected

extension of Jardines' home, the only question" for the Court was

"whether [the homeowner] had given his leave (even implicitly) for

[the officers] to do so."         Id. at 8.

            Focusing on implicit consent, the Court recognized that

a license to enter another's property may be implied "from the

habits of the country."       Id. (quoting McKee v. Gratz, 260 U.S.

127, 136 (1922)).       Indeed, "the knocker on the front door is

treated as an invitation or license to attempt an entry, justifying

ingress to the home by solicitors, hawkers and peddlers of all

kinds."    Id. (quoting Breard v. City of Alexandria, 341 U.S. 622,

626    (1951)).     That   implicit       license,      the   Court   explained,

"typically permits the visitor to approach the home by the front

path, knock promptly, wait briefly to be received, and then (absent

invitation to linger longer) leave."              Id.   The Court underscored

the simplicity of that license, explaining that "[c]omplying with


                                    - 22 -
the terms of that traditional invitation does not require fine-

grained legal knowledge; it is generally managed without incident

by the Nation's Girl Scouts and trick-or-treaters."       Id.    For that

reason, "a police officer not armed with a warrant may approach a

home and knock, precisely because that is 'no more than any private

citizen might do.'"     Id. (quoting Kentucky v. King, 563 U.S. 452,

469 (2011)).

             The Court went on to find that the officers exceeded the

scope   of    the   implicit   social   license   there   because     they

"introduc[ed] a trained police dog to explore the area around the

home in hopes of discovering incriminating evidence," and "[t]here

is no customary invitation to do that."           Id. at 9.     The Court

explained that the license implied by societal norms that invites

a visitor to the front door to knock and attempt to speak with the

occupant does not extend "[a]n invitation to engage in canine

forensic investigation" in the curtilage of the home.           Id.    The

Court concluded that, although the officers in Jardines remained

within the physical area covered by the license, their behavior

exceeded that "which . . . anyone would think he had license to

do" while on the property of another.        Hence, they exceeded the

scope of the implicit license authorizing their entry onto the

curtilage.     Id. at 10.

             As Justice Scalia put it:    "To find a visitor knocking

on the door is routine (even if sometimes unwelcome) [but] to spot


                                 - 23 -
that same visitor exploring the front path with a metal detector,

or marching his bloodhound into the garden before saying hello and

asking permission, would inspire most of us to -- well, call the

police."    Id. at 9.     Because the officers "learned what they

learned only by physically intruding on [the] property to gather

evidence" without a warrant and in excess of any implied license

to do so, they violated the Fourth Amendment.     Id.   at 11.   Again

commenting on the simplicity of the rule, the Court observed that

"[o]ne virtue of the Fourth Amendment's property-rights baseline

is that it keeps easy cases easy."       Id.

B.   Applying Jardines

           1. The Unconstitutional Conduct of the Officers

           Officers Morse and Gray arrived at French's home shortly

before 5:00 a.m.   They observed lights on in the home and decided

to conduct a "knock and talk" rather than immediately apply for a

warrant.   The officers entered the property, walked onto the front

porch, knocked on the front door, and announced that they were

police officers seeking to speak with French.    No one answered and

the officers left the property.13   At this point, there was nothing

constitutionally infirm about the officers' conduct, which was

expressly permitted by the "knock and talk" exception to the

warrant requirement.     Morse and Gray initially did no more than a


     13Although Officer Morse was wearing a body camera, it did
not record the initial knock and talk.


                                - 24 -
member   of    the    public    might    be    expected     to     do    --   enter   the

curtilage, knock on the front door seeking to speak with an

occupant, wait to be received and, receiving no response, leave.

See id. at 9-10.            Because this behavior was consistent with the

conduct permitted by the implied social license, the officers'

initial entry onto the curtilage was lawful.                     Thus, we focus our

clearly established law analysis on the conduct of the officers in

the wake of that first lawful entry onto the curtilage, and

consider it in totality.          It is that conduct in the aggregate that

requires      the    conclusion       that    the    officers      violated     clearly

established law.

              After the initial attempted knock and talk, Officers

Morse and Gray left the property.                     Morse went to speak with

Nardone,      and    Gray    stayed    near   French's      home    to    surveil     the

property.       While watching the property, Gray walked onto the

neighbor's adjacent driveway, which provided an unobstructed view

of the narrow strip of grass, the bedroom window, and the cellar

window of French's home.              From there, Gray observed a young man

peering out the basement window.                    Then, still standing on the

neighbor's      driveway,      Gray    shined       his   flashlight      through     the

window, which caused the young man to cover the window and turn

off the basement lights.          Gray then returned to the front porch of

French's building and again knocked on the front door, but no one

answered.      The knocking apparently caused a dog in the home "to


                                        - 25 -
bark frantically."   At that point, Gray's incident report recounts

that "still no one came to the door.       More lights were quickly

being turned off in the residence.     Window coverings which looked

like blankets were drawn over the open windows as well."14

          Morse then returned from Nardone's apartment and, along

with the two Old Town police officers (Detective Fearon and Officer

Orr), joined Gray off the property but near French's building.

Instead of honoring the clear signals that the occupants of the

home did not wish to receive visitors, Morse walked back onto the

property and, peering through a drawn window covering, saw that a

light remained on in the kitchen.      Morse then rejoined the other

officers and told them that he would return to the station to apply

for a search warrant.   Fearon suggested that the officers attempt

another "knock and talk," to which Morse responded that he and

Officer Gray "had already knocked" and that "[he] didn't think

that . . . French would respond."    See Affidavit of Travis Morse,

Dkt. No. 35-22.

          Ignoring Morse's hesitation and      suggestion   that the

officers should apply for a search warrant, the officers persisted



     14 In his incident report, Gray states that Morse was still
at French's residence when Gray noticed the young man peering out
of the basement window and that Morse and Gray proceeded to knock
on the front door a second time together. In his sworn affidavit
submitted to the district court, however, Gray explains that Morse
had already left to speak with Nardone when Gray proceeded to knock
a second time. Morse's affidavit also confirms that fact.


                              - 26 -
in their efforts to get French to come out of his home.15               This

time, Fearon and Morse went to the left side of the house, walked

through the curtilage along the narrow strip of grass and located

what they had reason to believe was French's bedroom window.16

They knocked forcefully on the window frame and yelled for French

to come out and talk.       Fearon also shined his light into the

bedroom.    At the same time, Officer Gray returned to the front

porch, knocked on the front door, and told French to come outside.

            The simultaneous knocking         apparently caused     the dog

inside the home to start barking loudly again.              At some point,

Andrews    finally   answered   the   front   door   and,   after   a   brief

discussion with Gray, agreed to look for French.              According to

French's affidavit, Andrews decided to answer the door because he

was afraid that the police would break the door down, which would

cause his dog to become defensive and could result in the police

shooting the dog.     A short while later, French, feeling as though

he "had no choice," came to the door.

            By the time French came to the door, the officers had

entered his property four times.         The first entry occurred when



     15Officer Orr agreed to canvass the area to see if she could
locate French and did not return to French's residence until after
he was arrested.
     16 The officers believed that window was in French's bedroom
based on a visit to the residence in November 2015 that involved
French.


                                  - 27 -
Morse and Gray initially approached French's residence by the front

path, knocked on the front door, and asked French to come to the

door.    The    second   occurred    when     Gray,    after   he    shined    his

flashlight     through   the   basement      window    from    the       neighbor's

driveway and saw a young man looking out, again approached the

home by the front path, knocked on the front door, and asked French

to come to the door.        This second entry caused the occupants of

the home to quickly turn off lights and cover windows.                    The third

entry involved only Officer Morse when, after returning from

Nardone's residence, he reentered the property, peered through a

drawn window covering, and saw a light on in the kitchen.                    Morse

then rejoined the other officers and recommended applying for a

warrant, but Detective Fearon suggested that they try again.                     On

the fourth entry, Morse and Fearon walked through the curtilage of

French's home, located his bedroom window, knocked on the window

frame, and asked him to come out, while Gray reentered the property

by the front path, knocked on the front door, and asked French to

come to the door.

          2. Violating Clearly Established Law

          While    the     officers'   conduct        does   not    involve    the

gathering of evidence from the curtilage of French's home with the

help of a dog, it does plainly demonstrate that, if we consider

their actions as a whole, they exceeded the scope of the implicit

social   license    that    authorized       their    presence      on     French's


                                    - 28 -
property.    Despite obvious signs that the occupants of the home

were aware of and did not want to receive visitors -- their refusal

to answer the door upon Morse and Gray's initial knock and Gray's

second knock, and their swift covering of windows and turning off

lights in response to that second knock -- the police doubled down

on their efforts to coax French out of the home.             Any reasonable

officer would have understood that their actions on the curtilage

of French's property exceeded the limited scope of the customary

social license to "approach the home by the front path, knock

promptly, wait briefly to be received, and then (absent invitation

to linger longer) leave."        Jardines, 569 U.S. at 8.            Indeed,

Officer Morse revealed such an understanding when he observed that

French was not likely to come to the door upon another attempt and

that the officers should secure a warrant.              Yet, the officers

disregarded Morse's advice and reentered the curtilage without a

warrant.

            Once back in the curtilage, the officers then upped the

ante in their attempts to convince French to come out of his home

by, among other things, continuing to knock on his front door,

locating and knocking on his bedroom window frame, and yelling for

him to come out of his home.       The officers could not reasonably

have   thought   that   an   invitation   to   engage   in    such   conduct

"inhere[s] in the very act of hanging a knocker" on the front door,

id. at 9, or that their actions were "no more than [what] any


                                 - 29 -
private citizen might do," id. at 8 (quoting King, 563 U.S. at

469).     There is no implicit social license to invade the curtilage

repeatedly, forcefully knock on the front door and a bedroom window

frame, and urge the residents to come outside, all in pursuit of

a criminal investigation.      As such, the officers' behavior was

plainly inconsistent with Jardines, which clearly established that

an implicit social license       sets the boundaries of what acts

officers may engage in within the curtilage of the home, absent

exigent circumstances.17    See id. at 8-10; see also King, 563 U.S.

at 469-470 ("When law enforcement officers who are not armed with

a warrant knock on a door . . . the occupant has no obligation to

open the door or to speak. . . . And even if an occupant chooses

to open the door and speak with the officers, the occupant need

not allow the officers to enter the premises and may refuse to

answer any questions at any time."); Hopkins v. Bonvicino, 573

F.3d 752, 765 (9th Cir. 2009) ("The mere fact that [the defendant]

did not answer the door cannot tip the balance in the officers'

favor, since nothing requires an individual to answer the door in

response to a police officer's knocking." (citations omitted)).

             The officers' attempts to undercut the straightforward

application of Jardines to this case are unpersuasive.    They first



     17The officers do not claim that their conduct was justified
by exigent circumstances and, as we shall explain, the dissent's
exigent circumstances argument was not made below or on appeal.


                                 - 30 -
argue   that   Jardines   could     not    have   clearly   established    the

unlawfulness of the officers' conduct because an officer reading

Jardines should anticipate only that, "if he or she brings a

trained drug-sniffing K-9 onto the porch or otherwise into the

curtilage of a residence without a warrant or consent of the

homeowner, then the officer may be liable for an unlawful search."

Their   argument    reflects   the    untenable     position   that    clearly

established law requires cases with practically identical facts.

The majority in Jardines made clear that "[i]t [was] not the dog

that [was] the problem" there.             569 U.S. at 9 n.3.        The drug-

sniffing K-9 was significant in Jardines because the officers used

the dog to "gather[] information in an area belonging to Jardines

and immediately surrounding his house -- in the curtilage of the

house . . . .      And they gathered that information by physically

entering and occupying the area to engage in conduct [a search for

evidence of a crime] not explicitly or implicitly permitted by the

homeowner."    Jardines, 569 U.S. at 5-6. Indeed, the Court added,

"[w]e think a typical person would find it a cause for great alarm

. . . to find a stranger snooping about his front porch with or

without a dog."     Id. at 9 n.3 (internal quotation marks omitted).

           Here, as we have explained, the conduct "not explicitly

or   implicitly    permitted   by    the   homeowner"   was    the   officers'

repeated reentry onto the property and the aggressive actions taken

by the officers.     In Jardines and here, police officers not armed


                                    - 31 -
with   a   warrant   engaged   in   conduct   in   pursuit   of   a   criminal

investigation within the curtilage that was inconsistent with the

implied social license pursuant to which an officer may enter the

curtilage of a home.     See id. at 8-9 ("[A] police officer not armed

with a warrant may approach a home and knock, precisely because

that is 'no more than any private citizen might do.' . . . . [T]he

background social norms that invite a visitor to the front door do

not invite him there to conduct a search." (quoting King, 563 U.S.

at 469)).

            The officers also argue that a rule abstracted from

Jardines is too general and "fails to appreciate the myriad

different circumstances law enforcement officers are confronted

with in the field."      The officers point to conflicting cases in

the wake of Jardines that involve either one or some combination

of the factors present in this case.           For example, the officers

cite disagreement regarding (1) whether a knock and talk conducted

early in the morning is inherently unlawful, see, e.g., United

States v. Lundin, 817 F.3d 1151, 1159 (9th Cir. 2016) (explaining

that the officers knocked "around 4:00 a.m. without evidence that

[the defendant] generally accepted visitors at that hour, and

without a reason for knocking that a resident would ordinarily

accept as sufficiently weighty to justify the disturbance"); Young

v. Borders, 850 F.3d 1274, 1286 (11th Cir. 2017) (Hull, J.,

concurring) (rejecting the dissent's assertion that an officer


                                    - 32 -
"exceeded the scope of the permissible knock and talk exception

because it was 1:30 a.m., he unholstered his weapon, and he knocked

so loudly"); (2) whether officers may survey the curtilage for a

different entry to the home if a knock and talk at the front door

is unsuccessful, see Carroll v. Carman, 574 U.S. 13, 20 (2014)

(per curiam)   (holding that     it was not beyond debate        whether

officers conducting a knock and talk may knock at any entrance

open to visitors rather than just the front door); (3) whether

knocking for more than a few minutes violates the knock and talk

rule, see United States v. Carloss, 818 F.3d 988, 998 (10th Cir.

2016) ("We decline to place a specific time limit on how long a

person can knock before exceeding the scope of th[e] implied

license."); (4) whether more than one knock and talk can be

attempted in a limited time period, see United States v. Walker,

799 F.3d 1361, 1362-64 (11th Cir. 2015) (finding it was reasonable

for officers to make a third attempt to knock and talk at 5:00

a.m. where the first two knocks had elicited no response and were

conducted the prior evening -- at 9:00 p.m. and at 11:00 p.m. --

and the officers observed lights on in the home and in a car parked

outside   before   reentering   the   property);   and   (5) whether   the

number of officers present matters, see United States v. White,

928 F.3d 734, 741 (8th Cir. 2019) ("[W]e fail to see why the number

or type of officers in this case would render the second entry

impermissible.").


                                 - 33 -
            Those cases do not detract from the clarity of Jardines'

application in this case.           We are not concerned only with the

number of officers present or the hour, location, or length of the

attempted knock and talks.          Instead, we are focused on the legal

principle at the core of Jardines -- the scope of the implied

license to enter the curtilage -- and the application of that

principle to the conduct of the officers in totality.                    Here, as

in Jardines, the officers had their feet "firmly planted on the

constitutionally protected extension of [the] home" and their

activity    was    therefore    limited    to   that    which   was   implicitly

authorized (absent explicit consent) by the homeowner.                  Jardines,

569 U.S. at 7.      It does not take "fine-grained legal knowledge" to

understand that the officers' actions in this case exceeded the

implicit authorization to enter the property of another without a

warrant.    See id. at 8.       Far from engaging only in conduct that a

homeowner might reasonably expect from a private citizen on their

property    --    that   is,    again,    approaching     the   door,    knocking

promptly, and leaving if not greeted by an occupant -- the officers

reentered the property four times and took aggressive actions until

French came to the door so that the officers could pursue their

criminal investigation.          By so doing, the officers engaged in

precisely    the    kind   of     warrantless    and     unlicensed      physical

intrusion    on    the   property    of    another     that   Jardines    clearly

established as a Fourth Amendment violation.              Hence, the officers


                                     - 34 -
violated clearly established law and are not entitled to qualified

immunity.

C. The Dissent

              There are two major problems with the dissent.                   It goes

to great lengths to make an exigent circumstances argument that

the appellees never make.           It also fails to address the principle

at the heart of Jardines: the scope of the knock and talk exception

to the warrant requirement is controlled by the implied license to

enter the curtilage.

              1. Exigent Circumstances

              The dissent tries to portray this case as one involving

exigent circumstances requiring the officers to act quickly "to

ensure the safety of a victim or prevent the destruction of

evidence."          The   exigent   circumstances        doctrine     is   a   narrow

exception to the "'basic principle of Fourth Amendment law' that

searches      and    seizures   inside    a     home   without    a   warrant       are

presumptively unreasonable."           Groh v. Ramirez, 540 U.S. 551, 559

(2004) (quoting Payton v. New York, 445 U.S. 573, 586 (1980)).

"[O]fficers may enter a home without a warrant to render emergency

assistance to an injured occupant or to protect an occupant from

imminent injury," Brigham City v. Stuart, 547 U.S. 398, 403 (2006),

or when doing so "is reasonably necessary to head off the imminent

loss of evidence,"         United States v. Almonte-Báez, 857 F.3d 27, 33

(1st   Cir.    2017).       Officers     must    carry    the    heavy     burden    of


                                       - 35 -
identifying an "objectively reasonable basis" for believing that

"there [wa]s such a compelling necessity for immediate action"

that the delay of obtaining a warrant could not be tolerated.                 Id.

at 32-31 (first quoting United States v. Samboy, 433 F.3d 154, 158

(1st Cir. 2005); then quoting Matalon v. Hynnes, 806 F.3d 627, 636

(1st Cir. 2015)).

             The officers do not, however, argue on appeal -- and

they did not argue in their summary judgment motion below -- that

their     actions   were    justified   by    exigent   circumstances.        The

officers do not claim that the safety of Nardone or the risk that

evidence would be destroyed was so acute that delay to seek a

warrant    could    not    be   tolerated.     There    is   a   single   passing

reference to exigent circumstances in the appellees' briefing.                 It

appears in a parenthetical to a case citation and serves as a mere

description of the circumstances of the case cited.18                As we have

said, "[i]t is not enough merely to mention a possible argument in

the most skeletal way, leaving the court to do counsel's work,


     18 In support of their argument that Jardines is ambiguous,
the officers pose a series of questions they contend are unanswered
by Jardines, each of which is followed by case citations allegedly
showing disagreement as to the answer. It is in that context that
the officers make their single ancillary reference to exigent
circumstances: "How loudly may an officer knock? See Kentucky v.
King, 563 U.S. 452, 468–69, 131 S. Ct. 1849, 1861 (2011) ('Police
officers may have a very good reason to announce their presence
loudly and to knock on the door with some force. A forceful knock
may be necessary to alert the occupants that someone is at the
door.') (discussing exigent circumstances exception to warrant
requirement)." Appellee's Br. at 37.


                                     - 36 -
create the ossature for the argument, and put flesh on its bones."

United States v. Zannino, 895 F.2d 1, 17 (1st Cir. 1990).   We see

no reason here to depart from the well settled rule that "issues

adverted to in a perfunctory manner, unaccompanied by some effort

at developed argumentation, are deemed waived."19   Id.

          The dissent also seems to suggest that even if the

circumstances of this case did not amount to a true emergency

justifying application of the exigent circumstances exception to

the warrant requirement, the nature of the exigencies involved

expanded the scope of the license for the officers to enter

French's property to conduct a knock and talk.      That argument

conflates the knock and talk and exigent circumstances exceptions.

Whereas the scope of the exigent circumstances exception is case-

specific and varies based on the nature of the exigency and the

severity of the underlying crime, see Welsh v. Wisconsin, 466 U.S.




     19 To be sure, the officers were justifiably concerned about
Nardone's wellbeing given her credible accounts of French's
conduct that evening and throughout the entirety of his
relationship with her. But the officers plainly do not argue that
there was such an imminent risk that French would harm Nardone or
destroy evidence that they were justified in dispensing with the
warrant requirement on that ground, such that they could exceed
the social license recognized in Jardines. See generally Williams
v. Maurer, 9 F.4th 416, 435-36 (6th Cir. 2021) (holding that a
reasonable jury could find no exigent circumstances where the
officers "respond[ed] to a report of a [possible domestic]
disturbance, [but] when they arrived on the scene, there was no
indication of a tumultuous situation in [the] home and [they] did
not witness any violent behavior inside the apartment").



                             - 37 -
740, 750 (1984), the scope of the knock and talk exception is

limited to the implied social license to enter the property of

another regardless of the nature of the suspected crime of interest

to the officers, see Jardines, 569 U.S. at 8 ("[A] police officer

not armed with a warrant may approach a home and knock, precisely

because that is 'no more than any private citizen might do.'"

(quoting King, 563 U.S. at 469)).      The dissent fails to point to

any case law suggesting otherwise.20

          2. The Scope of the Implied Social License to Conduct a
             Knock and Talk

          The dissent claims that Jardines cannot have clearly

established the unlawfulness of the officers' conduct in this case

because the Court's reasoning in Jardines was dependent upon the

fact that the officers entered the property with a drug-sniffing

dog "to gather information on the curtilage, not to speak with a

resident."   According to the dissent, because the officers in this

case entered the property with an intent to speak to French and



     20 The dissent also suggests that the scope of the implied
license to conduct a knock and talk might vary "when officers are
investigating a crime for which state law authorizes a warrantless
arrest." But that consideration is irrelevant. Probable cause to
arrest a suspect, even if that is all that is required under state
law, cannot overcome the protections that the Fourth Amendment
affords to a person inside his or her home under federal law. See,
e.g., Morse v. Cloutier, 869 F.3d 16, 23 (1st Cir. 2017)
("Arresting a suspect inside his home without a warrant violates
the Fourth Amendment unless some 'well-delineated exception[]'
shields the intrusion." (quoting United States v. Romain, 393 F.3d
63, 68 (1st Cir. 2004) (alteration in original)).



                              - 38 -
not to engage in a search with a drug-sniffing dog, Jardines is

inapposite.   The dissent's attempt to limit Jardines to its facts

ignores the animating principles of Jardines21 -- and the reason

Justice Scalia labeled the case "a straightforward one."    Id. at

5.   It also ignores the Court's insistence that it was not the dog

that was the problem in that case.22    See id. at 9 n.3.

           To reiterate, the constitutional violation in Jardines

was the officers' "physical[] ent[rance] and occup[ation]" on the

curtilage of Jardines' home "to engage in conduct not explicitly

or implicitly permitted by the homeowner."     Id. at 6.    Because

there was no explicit permission by Jardines, the Court reasoned

that the officers' permission to enter the property was authorized



      21The dissent unconvincingly tries to dismiss Jardines'
explanation of the scope of the implied social license as mere
dicta. But the Court's careful consideration of the contours of
the implied license, and whether the officers' conduct on Jardines'
curtilage was authorized by that license, was crucial to its
holding that the officers violated the Fourth Amendment.

       The dissent also tries to disaggregate the conduct of the
      22

officers and argues that, because Detective Fearon is not a
defendant in this case, his actions should not be taken into
account in determining whether Morse and Gray violated French's
Fourth Amendment rights. But that approach ignores the fact that
Fearon, Morse, and Gray acted in concert while pursuing the
investigation of French in the curtilage of the residence. It may
have been Fearon who suggested that the officers attempt another
knock and talk before applying for a warrant and he may have been
the first one to knock on French's window, but Morse and Gray
agreed with his proposal, participated in the final re-entry on
French's property, and Morse joined Fearon in knocking on French's
bedroom window. Hence, carving out Fearon's conduct accomplishes
nothing in terms of Morse and Gray's liability in this case.



                               - 39 -
by an implicit social license -- informed by "the habits of the

country" -- to enter the property of another and seek to speak

with an occupant.   Id. at 8 (quoting McKee v. Gratz, 260 U.S. 127,

136 (1922) (Holmes, J.)).   That license, the Court explained, has

both a physical and a purpose-based limitation.      Id. at 9.     In

other words, its scope "is limited not only to a particular area

but also to a specific purpose," both of which are defined by what

a homeowner might reasonably expect from a private citizen on the

homeowner's curtilage.   Id. at 9.     The Court concluded that the

officers abided by the terms of the physical scope of the license

-- their activities on the property were limited to areas that a

member of the public might be expected to visit.       However, the

officers in Jardines exceeded the limited purpose authorized by

the license through their conduct. They did so by seeking evidence

of drugs with the help of a trained, drug-sniffing dog.

          That the precise manner in which the officers in this

case exceeded the scope of the implied license differs from that

in Jardines is inconsequential.    The officers in this case, like

the officers in Jardines, in the absence of any license to do so,

"physically intrud[ed]" on a suspect's property repeatedly and

engaged in intrusive conduct that no reasonable visitor could have

understood as impliedly authorized by a resident.   Id. at 11.    The

dissent portrays the officers' final, unlicensed entry on French's

property as a mere attempt to conduct a knock and talk.          That


                              - 40 -
portrayal is unsupported by the record, given the contentious and

invasive conduct of the officers described above.

          The dissent's attempt to detract from the clarity of

Jardines by invoking Carroll v. Carman, 574 U.S. 13 (2014) (per

curiam), and United States v. Walker, 799 F.3d 1361, 1364 (11th

Cir. 2015) (per curiam), is unpersuasive.      In Carroll, instead of

knocking at the front door, officers traveled to the back of a

home and knocked at a sliding glass door that opened onto a ground-

level deck.   574 U.S. at 14.    The Supreme Court held that it was

not clearly established that the officers were prohibited from

knocking "at an[] entrance that is open to visitors . . . [other]

than . . . the front door."     Id. at 20.    Here, our case involves

officers knocking on an occupant's bedroom window and not "an[]

entrance" other than the front door "that is open to visitors."

See id.

          Walker    is   similarly   inapposite.      There,   officers

attempted three knock and talks over a span of about eight hours.

799 F.3d at 1362.   The officers first knocked at around 9:00 p.m.

and received no response.   Id. They left and returned around 11:00

p.m. and noticed a car was parked outside of the home that had not

been there during their first attempt.       Id.   The officers knocked

again but saw no indication that anyone was inside of the home.

Id.   The following morning, around 5:00 a.m., the officers drove

by the property and noticed that some lights were on in the home


                                - 41 -
and   inside   of   the    vehicle   parked   outside.     Id.      With   the

recognition that someone was likely now in the home, the officers

approached a third time.       See id.     Before they could knock on the

door, however, the officers noticed a man inside of the vehicle

with his head resting on the steering wheel.             Id.     The officers

knocked on the car window to determine who the man was and whether

he needed medical attention.         Id.   Nowhere in Walker is there any

suggestion that the officers engaged in the kind of aggressive

conduct that we have described here.

           As we have already explained, we are not concerned with

isolated facts like those presented in Carroll and Walker -- i.e.,

the number of officers present or the hour, location, or length of

the attempted knock and talks -- and whether those facts alone

might have supported a finding that the officers violated clearly

established law.          We are concerned only with Jardines' clear

prohibition on the officers' conduct in this case which, as we

have explained, plainly exceeded the scope of the implied license

to enter the curtilage of French's home.23




      23The dissent's notion that a neighbor -- let alone a group
of strangers visiting a home at 5:00 a.m. -- may, under the implied
social license, repeatedly knock on the front door, peer through
a drawn window covering, shine a flashlight through windows in the
home, and knock on a bedroom window frame, all while yelling for
the occupant to come outside, strains credulity and is contrary to
Jardines.


                                     - 42 -
                                      V.

              In sum, we agree with the district court that Officers

Drost   and    Merrill     had   probable    cause   to   arrest    French   for

harassment in February 2016 and, even if they did not, the question

of probable cause was debatable              such that the officers were

entitled to qualified immunity.             We therefore affirm that aspect

of the district court's summary judgment ruling.

              As to the September 2016 incident, we conclude that,

viewing the summary judgment evidence in the light most favorable

to   French,    Officers    Morse   and     Gray   violated   French's   Fourth

Amendment rights by exceeding the lawful bounds of a warrantless

"knock and talk."        We further conclude that the unlawfulness of

the officers' conduct was clearly established at the time by the

principles of law set forth in Florida v. Jardines.                Accordingly,

we reverse the district court's grant of summary judgment as to

Count IX and remand for further proceedings consistent with this

opinion.      Each party is to bear its own costs.            See 1st Cir. R.

39(a)(4).

              So ordered.

                      -Dissenting Opinion Follows-




                                    - 43 -
            LYNCH, Circuit Judge, dissenting in part.                 I join the

majority opinion as to the affirmance of summary judgment arising

from claims about the February arrest of Christopher French.                    I

strongly dissent from the reversal of the grant of qualified

immunity    to    Officers   Gray   and    Morse    as   to   the   September   14

incident.        In my view, the majority is wrong that Florida v.

Jardines, 569 U.S. 1 (2013), which concerned officers' entry onto

private property for the purpose of using a drug-sniffing dog on

the curtilage of the house, clearly established the purported

illegality of the officers' conduct in knocking at French's home

on September 14, 2016.

            The doctrine of qualified immunity has sometimes been

abused, but the majority's denial of qualified immunity here is

flatly contrary to Supreme Court and circuit law and creates a

circuit     split.       Moreover,        this     unfortunate      ruling   will

disincentivize police from taking action after persons of any

gender have credibly alleged that they have been threatened and

are frightened by former romantic partners.

            When they approached French's home, Officers Gray and

Morse were responding to an urgent and potentially dangerous

situation.        French had twice that night broken into Samantha

Nardone's house and had stolen her phone from her bedside table,

Nardone had previously called the police for help in dealing with

French's harassment of her, and Nardone told the officers that she


                                    - 44 -
was scared of what French might do if he accessed the contents of

her phone.    Given these circumstances and the state of the law in

2016, the officers' choice to knock several times at French's door

and window shortly after the second break-in was reasonable.

Nothing in Jardines clearly established otherwise.      The officers

in this case acted sensibly and with restraint, and most certainly

should not be deprived of qualified immunity and sent back to face

damages claims against them, as the majority holds.

                                 I.

            The following key facts of the September 14, 2016,

encounter are those which     would have been understood by any

reasonable officer in the shoes of Officer Morse, the lead officer,

and Officer Gray.   These facts reveal why the majority is wrong in

its reading of Jardines and its conclusion that the law was clearly

established as to the implied license analysis.       The facts also

demonstrate why the two officers are clearly entitled to qualified

immunity.

            The supposed violation of   French's Fourth Amendment

rights occurred sometime around 5:00 or 5:30 AM on September 14,

2016.   This is what the officers knew at the time.

  A. The Officers' First Visit to 60 Park Street.

            The victims, Samantha Nardone and her roommates, called

the police department at or around 3:19 AM on September 14, 2016,

to report that their residence had been broken into.    Nardone also


                               - 45 -
reported that her phone, which she had placed on her nightstand

before she went to sleep around 12:30 AM, was missing.

           Officers Morse and Gray were dispatched immediately to

Nardone's residence at 60 Park Street in Orono, Maine.                 Both

officers were familiar with the history between French and Nardone

and knew that Nardone had several times in the past called the

Orono Police Department because of problems with French.              Morse

was   familiar   with   French   because   he,   accompanied   by   Officer

Barrieau, had arrested French in November 2015 for violating his

conditions of release.     From this prior incident, Morse knew that

French lived at 13 Park Street, a nearby multi-tenant house about

.2 miles from Nardone's house.       He knew French did not live in a

single-family house. He also knew that French's room in that house

was on the first floor to the left of the front door.               He had

spoken with other officers about French multiple times.                Gray

testified at his deposition that he was familiar with French's

name in September 2016 and that it was "highly likely" he had read

French's previous arrest records.24




      24  Nardone wrote in her police statement about the February
incident that she had gotten in an altercation with French and he
would not leave her home when she asked him to. She reported that
he tried to put her in a headlock, and she pushed him away. She
told him he had ten minutes to collect his items from her home
before she called the police. She was concerned for her safety,
so she locked herself and her roommates into one of the bedrooms.
French began jiggling the lock and started using a card to pop it
open. They held the knob so he could not pop it open. Moments


                                  - 46 -
           On the way to Nardone's house, Morse saw that lights

were on at French's house at 13 Park Street.     When the officers

arrived, Nardone told them that she suspected French of breaking

in and taking her phone.   She explained that French had stolen her

keys the previous week and still had them, though she had since

changed the locks.    When she noticed her phone was missing, she

found that all of the doors she had locked before going to bed

were now unlocked.

           Nardone stated that she was afraid French would do

something to her if he gained access to her phone and read what

was on it.    She later added that "if he gets in [the phone], I'm

fucked."     Nardone explained that she had put a passcode on her

cellphone, but that the passcode she had chosen was not secure and

that she thought he would be able to crack it.    She thought that

if French had the phone he was "obviously gonna run" from his

apartment so that he would have time to look through the phone.

She said she was scared he would break in again that night and

wrote in her victim statement that she had reason to believe French

"would do it again (now/tonight)."   Nardone also told the officers

she thought French might be drunk or on drugs because he was

"obviously fired up."



later, Nardone heard a "huge smash downstairs," ran down, and saw
"the TV was shattered face down on the floor."



                               - 47 -
           Nardone told the police numerous good reasons for her

fear, including the events of that very night, of the prior week,

and from before that.   Nardone explained that earlier in the night

on September 13, 2016, Nardone had run into French in a chance

encounter at the Roost, a local lounge.       There, French came up to

her and they exchanged words; the interaction made her feel

uncomfortable in remaining there.      So she left around 10:30 PM.

           Nardone   later   drove   over   with   her   roommate   Alicia

McDonald to see a friend who lived nearby.         After the visit, the

two women attempted to drive home.     French found them and stood in

the middle of the road to force them to stop.       He yelled and swore

at Nardone, asking her where she had been, and accused her of drunk

driving.   As Nardone tried to drive away, French jumped onto her

car.

           As the police report recounts, "[o]nce Nardone made it

home she and McDonald locked all the doors and windows in fear

that French would come to their residence."         Nardone checked her

phone and saw she had nine missed calls from a blocked number --

which she had reason to believe were from French -- and eleven

messages from French. Nardone had blocked French on all her social

media accounts and on her email and phone but was still receiving

messages from French on the "First Class" University of Maine

platform that she had been unable to block him on.            French had

previously harassed her with calls from a blocked number in the


                                - 48 -
hours after being served a Cease Harassment Notice on February 18,

2016. On her roommate's advice, Nardone did not read the messages.

She told Morse she was "so freaking scared" when she went to bed.

Before falling asleep, she placed the phone on her nightstand.

Nardone woke up around 3:00 AM and saw that her phone was missing.

That was when she discovered that all the doors she had locked

before going to bed were now unlocked.

           As to the prior week, Nardone explained to the officers

that she had broken up with French six days before, on September

8, 2016.   That night, French had broken into Nardone's home and

stolen her keys and laptop. The following morning, Nardone noticed

that her laptop was gone, went to French's house to look for it,

and saw that her laptop was open on his bed and that he had been

going through her iMessages on her laptop.        The next day, on

Saturday, September 10, Nardone went out with friends.       Walking

towards a local bar, they saw someone watching them from the

kitchen window of French's house.      When she returned home later,

her car keys and a spare key on her windowsill had disappeared,

and she had not been able to find them since. She told the officers

she suspected French had taken her keys a second time, so she had

changed the locks.

           Nardone also told the officers that on a different,

previous occasion, French had taken Nardone's keys and she had

been afraid he would break in.   The hardware store was closed so


                              - 49 -
she could not change her locks that night, so French's roommates

put sensors on French's doors and windows so that they would be

alerted if French left and they could warn Nardone.           Nardone was

scared enough that night that she piled up furniture in front of

her bedroom door to make sure French could not get in.         She changed

her locks the following day.

           While   the   officers    were   at   Nardone's   apartment   on

September 14, her roommate Jennifer Prince found that an upstairs

bathroom window had been opened and the items in the windowsill

knocked to the floor, indications that the window was the entry

point.   Officer Morse took photographs of the window.          Morse also

asked dispatch to arrange a "ping" on Nardone's phone with the

cellphone carrier to see if they could find out whether the phone

was at 13 Park, French's residence.

           The   officers   left    Nardone's    home   at   approximately

4:26 AM.   Shortly before leaving, they asked Nardone if she would

feel safe staying at the apartment.         She repeated that she would

not feel safe if French got into her phone.         They returned to the

police station to try to "ping" Nardone's phone to find its

location and figure out if it was at French's apartment.           Nardone

had told them that she had tried to use iCloud to locate her phone,

but the phone had been turned off and so she could not locate it.




                                   - 50 -
  B. French's Second Break-In to Nardone's House

          The fears which Nardone reported about French again

trying to break in that same night came true.   At 4:43 AM, Nardone

called the police a second time and reported that French had come

back to her apartment.   He entered through the front doorway, but

only got to the mudroom when the screams of Nardone's roommates

stopped his entry and caused him to flee.

          Gray and Morse were dispatched again.     While on their

way, dispatch told them that French had been seen running down the

road towards his home at 13 Park.   They stopped at 13 Park on the

way and saw that there were lights on in the house.   They knocked

on French's door.    Nobody responded, so the officers left the

porch.   The officers decided that Gray should stay on the road

near 13 Park while Morse went back to Nardone's residence at 60

Park to gather the account of its residents first-hand.       Gray

walked down the driveway to the left of 13 Park and saw a man

peering out of the basement window of the building.   Gray knocked

a second time on French's door.

          Officers James Fearon and Melissa Orr from the Old Town

Maine Police Department were sent to join Morse at 60 Park.

Nardone and her roommates explained that French had broken in again

and that he was yelling that he needed help with his puppy. Nardone

stated that French was probably waiting for the police to leave

and her roommate said French would probably return "the second


                              - 51 -
[the police] leave."   Morse asked if there was somewhere else that

they could go and encouraged them to go elsewhere for the rest of

the night.

           That is what the officers knew of French's criminal

activities that night when they decided to return to 13 Park.

Among other things, they had every reason to believe (1) French

was a threat to Nardone and her roommates; (2) he had expressed

his anger in many ways toward them; (3) they had to move quickly,

particularly as he might read the email and messages on Nardone's

phone; (4) they had to move rapidly to prevent not just harm to

Nardone and her roommates, but the destruction of evidence: the

cell phone, the stolen keys, and whatever else he had taken, all

evidence of his break in; and (5) he had run down the street back

to his room and was still awake.

  C. The Officers' Second Visit to French's Apartment

           Morse and Fearon returned to French's home. The officers

discussed the best approach to finding and questioning French.

They felt they had probable cause and discussed seeking a warrant.

To obtain a warrant, the officers would have to return to the

police station and prepare an application and request for a

warrant.     They estimated that would take at least half an hour

once back at the station.     They then would have to drive to a

nearby town to get a judge to sign the warrant.




                               - 52 -
            They discussed a further attempt at a knock and talk

and, if French appeared, questioning him.           They had observed that

the lights which had been on were quickly turned off and the

windows were covered, confirming the view that someone was up and

awake.    Morse explained to the other officers that he and Gray had

tried a knock and talk earlier on the first trip to 13 Park and

had gotten no response.      Fearon, who is not a defendant (and whose

actions cannot be attributed to Morse and Gray) expressed his view

that they should attempt again to knock and talk.

            The decision to proceed not with a warrant, but with a

knock and talk, in Gray's view, was based on the fact that it was

faster and easier.        Gray stated that "if we believe somebody is

inside of the residence and we're looking to speak with that

individual and we have facts and circumstances surrounding the

situation that lead us to believe that he is inside of the

residence, we can knock to attempt to have that subject come out

and speak with us."       Gray also stated that the appropriate place

to knock "depends on where the person that you're trying to contact

resides    within   the    dwelling"   and   that   he   believed   it   was

permissible to bang on a window.

            As to Morse, he stated at his deposition that he was

unaware of any standards that place limits on what time of day you

can knock and talk.         Morse was aware that officers may enter

private property in exigent circumstances, which arise where there


                                  - 53 -
is a risk that evidence will be destroyed, a person will be harmed,

or officer safety is at risk.        Morse was also aware that Maine law

permits officers to arrest without a warrant "any person who the

officer    has   probable    cause    to       believe    has   committed   or   is

committing . . . [d]omestic violence assault, domestic violence

criminal   threatening,      domestic      violence       terrorizing,   domestic

violence stalking or domestic violence reckless conduct."                        Me.

Rev. Stat. tit. 17-A, § 15(1)(A)(5-B).               While still at 60 Park,

Morse had said to Officer Fearon that they had enough to "hook"

French on harassment and stalking after his second break-in.

            Having   decided    that       a    further    knock   and   talk    was

appropriate, Morse and Fearon went to a strip of grass on the side

of 13 Park.      Morse stated that he did not know where the property

line was, but acknowledged that he was on the curtilage of 13 Park

when knocking on the window frame.               In deciding to knock at the

window, he factored in that it was an apartment and that French

had non-relative roommates living with him.               Morse's understanding

was that officers can knock several times during a knock and talk,

but must stop before it becomes unreasonable.

            It was not the defendant officers but Fearon who then

knocked on the window frame of French's bedroom window. Only after

that did Morse knock on the window twice.                 The total time of the

two different officers knocking on the window frame was almost

exactly two minutes.        For French to have responded to the window


                                     - 54 -
knocking, he would have had to come out from his bedroom and go to

the front door.

            Gray then knocked on the front door again and announced

their presence.    The knocking had two immediate effects.   One was

that a dog started barking.   The officers said they could not tell

if the dog came from 13 Park or the very nearby neighboring home.

More importantly, within thirty seconds of Gray's knocking at the

front door, another tenant who lived at 13 Park who identified

himself as "Corey," came to the door.   The officers asked if French

was home.   Corey was not sure and asked if Gray wanted him to look

for French. Gray asked him to go look for French.       Corey asked

French to come to the door and French then did so.

            French came outside to speak to the officers. He refused

to acknowledge that he had Nardone's phone, but said that he would

look for it anyways.     The officers did not permit French to go

alone inside to look for the phone, so French asked Corey to

retrieve the phone and told him where to look.     After additional

questioning, Officers Morse and Gray arrested French for burglary

around 5:30 AM.

                                 II.

            "The doctrine of qualified immunity shields      [police

officers] from civil liability so long as their conduct 'does not

violate clearly established statutory or constitutional rights of

which a reasonable person would have known.'"     Mullenix v. Luna,


                               - 55 -
577 U.S. 7, 11 (2015) (quoting Pearson v. Callahan, 555 U.S. 223,

231 (2009)).     To show that a rule is "clearly established," "[i]t

is   not   enough    that    the    rule    is    suggested      by    then-existing

precedent."      Dist. of Columbia v. Wesby, 138 S. Ct. 577, 590

(2018).     Instead, "existing precedent must . . . place[] the

statutory or constitutional question beyond debate."                     Ashcroft v.

al-Kidd, 563 U.S. 731, 741 (2011).                   "This demanding standard

protects 'all but the plainly incompetent or those who knowingly

violate the law.'"          Wesby, 138 S. Ct. at 589 (quoting Malley v.

Briggs, 475 U.S. 335, 341 (1986)).                 The inquiry into whether a

rule is clearly established "must be undertaken in light of the

specific context of the case, not as a broad general proposition,"

and "[s]uch specificity is especially important in the Fourth

Amendment context."         Mullenix, 577 U.S. at 12 (quoting Brosseau v.

Haugen, 543 U.S. 194, 198 (2004) (per curiam)).

            French     and   the    majority      argue   that    Jardines     itself

clearly established that the officers' conduct on September 14,

2016, violated French's constitutional rights.                        I disagree for

several reasons.       First, the holding of Jardines is not applicable

here   because   the    facts      are    entirely   distinct,        and   Jardines'

reasoning relied on facts not present here.               Second, as made clear

by Supreme Court and circuit court decisions published after

Jardines, Jardines' general discussion of the knock and talk

exception was not adequately specific to clearly establish the


                                         - 56 -
purported illegality of the officers' conduct here.               Finally, the

majority seems to posit that the officers' actions somehow forced

French to come to the door.        The majority relies on a self-serving

statement made by French after he instituted this litigation, but

certainly not made to the officers at the time of these events.

This argument by the majority suffers from at least three errors

in itself.      First, the facts do not support this assertion.

Secondly, nothing in Jardines supports it. Thirdly, the majority's

looking at qualified immunity, not from the objective point of

view of the officers on the scene but from the point of view of

French, is clearly error.      On the facts of this case, a reasonable

officer would easily understand that their actions had not forced

or coerced French to come to the door.            There were no threats and

no overbearing of French's will.

            As to the first issue, Jardines concerned the use of a

drug-sniffing dog in the daytime, and its holding, stated at the

end of the opinion, was that "[t]he government's use of trained

police dogs to investigate the home and its immediate surroundings

is   a   'search'   within   the   meaning   of    the   Fourth   Amendment."

Jardines, 569 U.S. at 11-12.        That holding is not applicable here,

where there was no police dog or any other instrumentality used.

            The analysis in Jardines also depended on the fact that

the officers entered the property to gather information on the

curtilage, not to speak with a resident.             E.g., id. at 6 ("[The


                                    - 57 -
Fourth Amendment] right would be of little practical value if the

State's agents could stand in a home's porch or side garden and

trawl for evidence with impunity."); id. at 9 ("The scope of a

license . . . is limited . . . to a specific purpose. . . .   Here,

the background social norms that invite a visitor to the front

door do not invite him there to conduct a search." (emphasis

added)); id. at 9 n.4 ("What [Kentucky v.] King establishes is

that it is not a Fourth Amendment search to approach the home in

order to speak with the occupant, because all are invited to do

that. . . .   But no one is impliedly invited to enter the protected

premises of the home in order to do nothing but conduct a search."

(second emphasis added) (citing 563 U.S. 452, 469-70 (2011)); id.

at 11 ("That the officers learned what they learned only by

physically intruding on Jardines' property to gather evidence is

enough to establish that a search occurred." (emphasis added)).

The court stated that the case turned on "whether the officers had

an implied license to enter the porch, which in turn depend[ed]

upon the purpose for which they entered."   Id. at 10.   The officer

had exceeded the scope of the implied license because his "behavior

objectively reveal[ed] a purpose to conduct a search, which is not

what anyone would think he had license to do."   Id. at 10 (emphasis

added).   In contrast, as the Court explained "the officers could

have lawfully approached [Jardines'] home to knock on the front




                               - 58 -
door in hopes of speaking with him.          Of course, that is not what

they did."       Id. at 7 n.1.

            In the instant case, it is undisputed that the officers

were knocking on the door to try to speak with French, not to

search the property, as in Jardines.           Jardines is not about the

limitations, if any, on the duration or location of a knock and

talk license to contact the resident of a home, and thus could not

clearly    establish    the    purported   illegality   of   the   officers'

conduct.    Cf., e.g., United States v. Walker, 799 F.3d 1361, 1363

(11th Cir. 2015) (citing Jardines for the proposition that officers

exceed the implicit license of the knock and talk exception when

their conduct objectively reveals a purpose to conduct a search).

Jardines also did not concern a situation in which the officers

had to act quickly to ensure the safety of a victim or prevent the

destruction of evidence.         See Kentucky v. King, 563 U.S. 452, 472

(2011) (holding that officers may enter a residence without a

warrant in order to prevent the destruction of evidence).            Nor did

Jardines discuss how the analysis might change when officers are

investigating a crime for which state law authorizes a warrantless

arrest.

            As    to   the    majority's   argument   that   the   purported

illegality of the officers' conduct was clearly established by the

broad "legal principle at the core of Jardines" because "[i]t does

not take 'fine-grained legal knowledge' to understand that the


                                    - 59 -
officers' actions in this case exceeded the implicit authorization

to enter the property of another without a warrant," there are

several problems with this reasoning.       As explained above, the

argument relies on language about the scope of the knock and talk

exception which is not the holding of Jardines or central to

Jardines' analysis.       See Garner, et al., The Law of Judicial

Precedent 26, 82 (2016) (defining scope of judicial holdings).       It

ignores   the   Supreme    Court's   instruction   that   the   clearly

established inquiry "must be undertaken in light of the specific

context of the case" and not "at a high level of generality."

Mullenix, 577 U.S. at 12 (first quoting Brosseau, 543 U.S. at 198;

and then quoting al-Kidd, 563 U.S. at 742).        It also ignores the

language of Jardines itself, which clarifies that the implied

license is only "typically" limited to walking up the front path

of a home and knocking.     Jardines, 569 U.S. at 8.

          Subsequent decisions from the Supreme Court and from our

sister circuits make clear that the purported illegality of the

officers' actions -- including knocking at the window, knocking

multiple times, and knocking late at night -- was not clearly

established by Jardines' general rule.

          In Carrol v. Carman, the Supreme Court held that it had

not been clearly established, and it would not decide, whether

officers could perform a knock and talk "at any entrance that is

open to visitors rather than only the front door."        574 U.S. 13,


                                - 60 -
20 (2014).     By refusing to decide the issue, the Court made clear

that Jardines' description of the implied license -- despite

specifying that "typical" knock and talk would be at the front

door -- did not clearly establish that only a knock at the front

door was acceptable.      Since then, several circuits have held that

officers may knock at various places on the property if they have

reason to believe that they will find a resident.         See, e.g., Covey

v. Assessor of Ohio Cnty., 777 F.3d 186, 193 (4th Cir. 2015) ("An

officer may also bypass the front door (or another entry point

usually used by visitors) when circumstances reasonably indicate

that    the   officer   might   find   the   homeowner   elsewhere   on   the

property"); United States v. Walker, 799 F.3d 1361, 1364 (11th

Cir. 2015) (per curiam) (holding that knock on car window in

carport away from front door was acceptable under knock and talk

exception).

              Against this background, a visitor, knowing that this

was a multi-tenant unit and precisely where French's room was,

could quite reasonably go to his window to knock rather than use

the door.     So could a neighbor who, having received no response at

the front door, knock on a window to get the attention of an

occupant.25     There was absolutely no impediment to stop visitors


       25 The majority argues that this contention is "contrary to
Jardines." This once again misunderstands the qualified immunity
inquiry and Jardines itself. To overcome the defense of qualified
immunity, it is not up to the officers to demonstrate the


                                   - 61 -
from knocking at the window, which was adjacent to the neighbors'

driveway.

            The Eleventh Circuit case United States v. Walker shows

even more clearly that the purported illegality of Officer Gray

and Morse's actions was not clearly established. In Walker, police

officers went to a home and knocked at 9:00 PM and 11:00 PM to

attempt to speak with a resident.   799 F.3d at 1362.   They returned

shortly after 5:00 AM and saw that there were lights on in the

house and in a car parked in a carport thirty feet from the house.

Id.   The officers went to the car and knocked on the car window.

Id.   The man inside the car stepped out, and in the course of his

interaction with the police, the police found counterfeit currency

in his home.    Id. at 1362-63.   The Eleventh Circuit affirmed the

denial of the defendant's motion to suppress evidence discovered

as a result of the third knock and talk on the car window.     Id. at

1364. It first explained that the officers' actions did not exceed

the implied license to knock and talk because their purpose was

"to speak with the homeowner, which is conduct that falls squarely

within the scope of the knock and talk exception" and not to search



constitutionality of their actions, but to French to show that no
reasonable officer in these officers' positions could have thought
that their actions were constitutional. The fact that a visitor
who knew which bedroom was French's could knock on his window in
addition to the door simply goes to the reasonableness of the
officers' doing so and establishes that their actions are entitled
to qualified immunity.


                               - 62 -
the property.   Id. at 1363.   The court then reasoned that going to

the carport was a permissible "small departure from the front door

. . . when seeking to contact the occupants" because "the officers

entered [the carport] because they had reason to believe the

house's occupant was sitting in the car parked inside."          Id. at

1364 (alteration in original) (quoting United States v. Taylor,

458 F.3d 1201, 1205 (11th Cir. 2006)).         The Eleventh Circuit also

rejected the argument that in all circumstances "going to someone's

house before sunrise to knock on the door is unreasonable and

exceeds the implied invitation that underlies the knock and talk

exception."   Id. at 1364.   It explained that the officers' actions

were reasonable because they had seen a light on at 5:04 AM,

suggesting that someone was awake.       Id.

          Given that Walker was decided before the events of this

case, I cannot agree that it was clearly established "beyond

debate" that Morse and Gray's actions here violated the Fourth

Amendment.    al-Kidd, 563 U.S. at 741.          In Walker, the police

approached the home to knock three distinct times, twice at his

front door and once on his car window away from the front porch.

799 F.3d at 1364; see also United States v. White, 928 F.3d 734,

739-41 (8th Cir. 2019) (holding that officers had not violated the

Fourth Amendment by approaching a home multiple times in one day

in an effort to make contact with the property owner).         Officers

Morse and Gray knocked four times.        Each of the knocks in Walker


                                - 63 -
was at night, and one was at 5:00 AM, essentially the same time

that Morse knocked on French's window.    As in Walker, Morse and

Gray had reason to know that French was awake and that they might

reach him by knocking somewhere other than the front door -- here

a bedroom window instead of a car window on the curtilage of the

home.26

          The majority commits further errors when it relies on

French's post-litigation self-serving statements that he felt he

had "no choice" but to answer the door. He made no such assertion

to the officers and he voluntarily answered the door. The majority

attempts to imply that the officers' actions somehow coerced French


     26   The majority does not argue that French revoked his
implied license or that the officers reasonably should have
understood him to have done so. Perhaps this is because French
could have at any time explicitly told the officers to leave, or
had his roommate do so when his roommate answered the door, but
chose not to. At any rate, the determination as to when an implied
license has been revoked is yet another question about the scope
of the implied license left open by Jardines. See United States
v. Smith, No. 16-91-01, 2017 WL 11461045, at *11 (D.N.H. Oct. 18,
2017) ("[T]he First Circuit Court of Appeals has yet to delineate
the contours of revocation."). Not only is there a dearth of case
law on this topic in our circuit, but courts in other circuits
have indicated that the license is difficult to revoke. See United
States v. Carloss, 818 F.3d 988, 996-97 (10th Cir. 2016) (posting
"No Trespassing" sign in yard and "Posted Private Property Hunting,
Fishing, Trapping or Trespassing for Any Purpose Is Strictly
Forbidden Violators Will Be Prosecuted" sign on door did not revoke
implied license for knock and talk); cf. Edens v. Kennedy, 112
Fed. App'x 870, 875 (4th Cir. 2004) (finding police could not knock
and talk where house was fenced in, gate was locked, and "No
Trespassing" sign posted); see also United States v. Holmes, 143
F. Supp. 3d 1252, 1262 (M.D. Fla. 2015) (noting implied license
can be revoked by "express orders from the person in possession"
(citation omitted)).


                              - 64 -
into answering the door.    The majority cannot squarely make this

argument   because   Jardines   says     nothing   about   coercion   --

unsurprisingly, since it is a case fundamentally about searches

conducted in the curtilage of people's homes and not about the

scope of the knock and talk warrant exception.       Nevertheless, the

majority finds that the officers "reenter[ing] the property four

times and [taking] aggressive actions until French came to the

door" was somehow contrary to law clearly established in Jardines.

Jardines simply does not address how many attempts officers who

want to knock and talk may make to get the attention of one occupant

of a multi-occupant house.      In finding that the law was clearly

established, the majority holds without any correct citation that

every reasonable officer would have known reentry onto the property

and "aggressive actions" are foreclosed by Jardines.       This finding

is mistaken in several respects.

           First, it is simply not clearly established law that

repeated entries onto different locations on a property to get the

attention of the person sought are unconstitutionally coercive.

As stated above, in both Walker and White, courts in other circuits

found no constitutional problem with repeated entries onto a

defendant's property.27    Walker, 799 F.3d at 1363-64; White, 928



     27   As for "aggressive actions," the majority provides no
guidance for how this highly subjective term might be defined,
much less any actual cases outlining its scope.


                                - 65 -
F.3d at 739-41.    A reasonable officer could conclude that the

efforts to find French permissibly included going to his window as

well as the front door to knock, and that this was efficient and

hardly "aggressive."     The majority rests its entire case on

Jardines, which does not answer these questions.

          In   cases   from   our   circuit   that   actually   discuss

coercion, we make clear that the law sets a high bar.     For example,

in order for a confession to be said to be coerced, the person

being questioned must have their will "overborne."       United States

v. Jackson, 608 F.3d 100, 103 (1st Cir. 2010) (citing Arizona v.

Fulminante, 499 U.S. 279, 288 (1991)) ; see also United States v.

Genao, 281 F.3d 305, 310 (1st Cir. 2002) (noting that police must

not "apply undue or unusual pressure . . ., use coercive tactics,

or threaten [the defendant] with violence or retaliation if he did

not confess.").   Contrary to French's litigation statements made

in furtherance of his efforts to obtain a damages award from these

officers, there is no support for the contention that the officers'

conduct overbore his will and forced him to come to the door.28      He

did not ask the officers to leave, nor did he ask his roommate to

tell them to go away when his roommate answered the door.


     28   In fact, in his deposition, French stated "I knew I had
the right to not come outside if I didn't want to." As the majority
acknowledges, French had experience with the criminal justice
system before this event, having been arrested previously in
February 2016.    In the same deposition, French stated he had
already been arrested "four times."


                                - 66 -
           Despite the majority's attempts to buttress its argument

by   focusing   on   French's   belated    statement    of    his   subjective

feelings before he came to the door, the proper focus of the

qualified immunity inquiry is whether the officers would have known

their actions were unconstitutional.         The answer, contrary to the

majority, is that a reasonable officer could have thought these

actions     were     constitutional.          In   qualified          immunity

determinations,      "[t]he   dispositive    question    is    'whether    the

violative nature of particular conduct is clearly established."

Mullenix, 577 U.S. at 12 (emphasis in original) (citing al-Kidd,

563 U.S. at 742).

           The majority's entire approach to qualified immunity

runs counter to both the Supreme Court's and this circuit's

precedents.     The "clearly established" inquiry is not supposed to

entail elucidating an abstract principle from a single case and

asking how a reasonable officer would have applied that principle

in a given situation.         Rather, it requires asking whether the

constitutionality of the official's behavior was placed "beyond

debate" by existing precedent.         al-Kidd, 563 U.S. at 7471.          The

inquiry requires "specificity," particularly in Fourth Amendment

cases.    Mullenix, 577 U.S. at 12.        The majority makes clear that

it is not concerned with what it views as trivial details like

"the number of officers present or the hour, location, or length

of the attempted knock and talks."        It should be.       In ignoring the


                                  - 67 -
specifics of the case and the very real questions left open by

Jardines to reach its decision, the majority defines clearly

established law at the "high level of generality" the Supreme Court

has expressly foreclosed.          al-Kidd, 563 U.S. at 742.

             The need for swift action also distinguishes this case

from Jardines and undercuts the majority's argument that general

principles      of     Jardines    clearly       established      the        purported

illegality of the officers' conduct.              There are two basic reasons

for   this    among    many   others.       First,      the   Supreme    Court       has

recognized that officers may enter a residence without a warrant

in order to prevent the destruction of evidence.                  King, 563 U.S.

at 472.      Here, a reasonable officer could have thought that their

conduct did not violate any constitutional rights because a knock

and talk could prevent French from destroying or disposing of

Nardone's phone, keys, and any other evidence of the break-in.

Second, there was an imminent threat to Nardone, and the officers

certainly were allowed to attempt to talk to French in an effort

to secure her safety.         Cf. id. at 460 (recognizing that officers

may enter a home without a warrant to prevent "imminent injury").

             As we have recognized, "the Supreme Court's standard of

reasonableness is comparatively generous to the police in cases

where potential danger, emergency conditions or other exigent

circumstances        are   present."      Roy    v.     Inhabitants     of    City    of

Lewiston,     42   F.3d    691,   695    (1st    Cir.    1994).    We    have    also


                                        - 68 -
recognized      that    deference     to    officers'     decisions       in    these

circumstances      is   particularly       warranted     in    domestic    violence

situations where "violence may be lurking and explode with little

warning."      Fletcher v. Town of Clinton, 196 F.3d 41, 50 (1st Cir.

1999).    The officers here knew of the potential danger to Nardone,

and the potential for destruction of evidence, and they also knew

that getting a warrant would be a lengthy process.                       With these

factors in mind, the officers made the considered determination

that it was reasonable to attempt several knock and talks.

            This   circuit's     recent       decision   in    United     States     v.

Manubolu, No. 20-1871, 2021 WL 4167087 (1st Cir. Sept. 14, 2021),

underscores how long wait times for warrants factor into the

reasonableness determination.              In the aftermath of a car crash,

the court found that police did not violate the defendant's

constitutional rights by conducting a blood draw to check his blood

alcohol levels without a warrant where the procedure for getting

a warrant was "protracted," the blood alcohol evidence in his

bloodstream was dissipating, and the defendant needed medical

attention.       Id.    at   *9-10,    *13.     Under    the    totality       of   the

circumstances, the court found that it was reasonable for the

officer   to    think    exigent      circumstances      existed    to    permit     a

warrantless blood draw.         Id. at *13.       There, the officer knew of

a National Park Service regulation which prohibited warrantless

blood draws absent exigent circumstances.                Id. at *3.        Here, in


                                       - 69 -
contrast, there was no analogous statute since no warrant was

required for a knock and talk.       Given the length of time it would

have taken to get a warrant, the possibility that evidence would

be destroyed, and the potential for harm to Nardone, the officers

here    made    an   objectively     reasonable    decision      under    the

circumstances to continue to attempt to knock and talk.                   The

officers' actions were lawful, but, even if they were not, the

totality of the circumstances informing their decisions is yet

another reason why adherence to the law requires that the grant of

qualified immunity be affirmed.

                                    III.

            The majority's decision, in my view, disincentivizes

police from acting on and taking seriously the complaints of

persons of any gender who credibly seek law enforcement help when

they have been threatened by former romantic partners.             I cannot

agree   that    Jardines   was   sufficiently   analogous   to    place   the

legality of these officers' actions "beyond debate."             In my view,

under controlling Supreme Court precedent, the only correct result

here is the affirmance of the grant of qualified immunity to these

officers.      The officers here acted reasonably in making repeated

efforts to reach French where he was acting erratically and Nardone

explained that the danger to her would increase as French was given

more time to break into and read the contents of her phone.               The

officers knew French was awake despite the time, and it was a


                                   - 70 -
rational choice in a multi-tenant apartment for the officers to

knock on French's bedroom window to try to speak to him.   Nothing

in Jardines or any other case clearly established that these

actions violated the Fourth Amendment.

         I dissent.




                             - 71 -

```

---

## GROUP: content/cases/Gaetjens v. Winnebago County.md  (`case`, 5 assertions)

### content_page

```
---
title: Gaetjens v. Winnebago County
type: case
citation: "4 F.4th 487 (2021)"
parallel_cite: ""
neutral_cite: ""
court: 7th Cir. 2021
court_level: coa
circuit: ca7
year: 2021
date_decided: 2021-07-13
docket: 20-1295
authority_weight: "Binding in-circuit — 7th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4899427/sally-gaetjens-v-winnebago-county-illinois/"
  cluster_id: 4899427
  opinion_id: 4703206
  identity_checked: true
lake:
  record_id: Gaetjens v. Winnebago County
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Emergency Aid]]"
    role: "Recent development — expands/illustrates (Binding in-circuit — 7th Cir.)"
related:
  - "[[Emergency Aid]]"
  - "[[Brigham City v. Stuart]]"
  - "[[Kentucky v. King]]"
tags:
  - case
  - fourth-amendment
  - emergency-aid
  - exigent-circumstances
  - warrantless-entry
  - community-caretaking
holding: "Officers who had an objectively reasonable basis to believe a missing woman was experiencing a medical emergency could enter her home without a warrant under the emergency-aid exception, and their related actions (condemning the noxious home and removing endangered animals) were likewise justified by exigency."
---

# Gaetjens v. Winnebago County

*4 F.4th 487 (7th Cir. 2021)* (No. 20-1295) · U.S. Court of Appeals for the Seventh Circuit · **Binding in-circuit — 7th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4899427 → lead opinion 4703206 (4 F.4th 487, decided 2021-07-13); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Sally Gaetjens, who bred cats in her home, was told by her doctor to go to the hospital and then could not be reached. Her doctor and a neighbor (her listed emergency contact) grew alarmed, and the neighbor called police reporting a possible medical emergency. Officers found packages, untended garbage, and a full mailbox; entering with the neighbor's key, they found the home so noxious it was deemed a public-safety hazard. The county condemned the home and animal-services officers removed dozens of cats. Gaetjens sued under § 1983, and the district court granted the defendants summary judgment.

## Issue
Whether officers' warrantless entry into the home of a missing person believed to be in medical distress — and the ensuing condemnation and removal of animals — violated the Fourth Amendment.

## Rule
The Seventh Circuit affirmed, holding that each intrusion fell within an [[Exigent Circumstances and Hot Pursuit|exigency]] exception governed by an objective-reasonableness standard. The entry to look for Gaetjens fit the emergency-aid exception squarely: "The home entry in this case likewise falls into the heartland of emergency-aid situations. ... His warrantless entry of the Loves Park home thus did not violate the Fourth Amendment." — 4 F.4th at 493–94. The touchstone is whether officers had an objectively reasonable basis to believe someone inside needed immediate aid.

## Application
An officer knew that Gaetjens's doctor and emergency contact could not reach her, that her contact feared a medical emergency, and that mail and garbage were piling up — a "litany of concerning circumstances" more than sufficient to justify entering to check on her welfare. The court separately upheld the home's condemnation (an objectively reasonable belief the premises posed a safety threat) and the removal of the cats (reasonably deemed in imminent danger), each as its own [[Exigent Circumstances and Hot Pursuit|exigency]].

## Conclusion
The grant of summary judgment to the defendants was **affirmed**; the warrantless entry, condemnation, and animal seizures were each justified by [[Exigent Circumstances and Hot Pursuit|exigent circumstances]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Gaetjens* is a recent Seventh Circuit application of the emergency-aid exception (*[[Brigham City v. Stuart]]*), reaffirming that a warrantless home entry to render aid turns on an objectively reasonable belief that an occupant needs immediate help, not on the officer's subjective motive.

## Appears on
- [[Emergency Aid]] — *Recent development — expands/illustrates (Binding in-circuit — 7th Cir.)*

## Sources
- [*Gaetjens v. Winnebago County*, 4 F.4th 487 (7th Cir. 2021)](https://www.courtlistener.com/opinion/4899427/sally-gaetjens-v-winnebago-county-illinois/) — pinpoint: 493–94 (emergency-aid holding); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "915ddc807a2fda64", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "4 F.4th 487 (2021)", "court": "7th Cir. 2021", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Gaetjens v. Winnebago County", "year": "2021"}}
{"assertion_id": "0bed4ea1b0bfcf86", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Officers who had an objectively reasonable basis to believe a missing woman was experiencing a medical emergency could enter her home without a warrant under the emergency-aid exception, and their related actions (condemning the noxious home and removing endangered animals) were likewise justified by exigency.", "title": "Gaetjens v. Winnebago County"}}
{"assertion_id": "f83af6d10dd95f7c", "dimension": "support", "kind": "home_role", "locator": {"home": "Emergency Aid"}, "payload": {"home": "Emergency Aid", "role": "Recent development — expands/illustrates (Binding in-circuit — 7th Cir.)", "title": "Gaetjens v. Winnebago County"}}
{"assertion_id": "320a6717610d8f56", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Gaetjens v. Winnebago County", "varies_by_point": "false"}}
{"assertion_id": "a9e74f98b1c3a405", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 7th Cir.", "title": "Gaetjens v. Winnebago County"}}
```

### lake record — Gaetjens v. Winnebago County

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gaetjens v. Winnebago County",
  "status": "under_review",
  "identity": {
    "case_name": "Sally Gaetjens v. Winnebago County, Illinois",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "Gaetjens v. Winnebago County",
    "court": "7th Cir. 2021",
    "court_id": "ca7",
    "court_level": "coa",
    "circuit": "ca7",
    "state": null,
    "date_decided": "2021-07-13",
    "year": 2021,
    "docket": "20-1295",
    "cluster_id": 4899427,
    "lead_opinion_id": 4703206,
    "sibling_ids": [],
    "absolute_url": "/opinion/4899427/sally-gaetjens-v-winnebago-county-illinois/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "4 F.4th 487",
      "volume": "4",
      "reporter": "F.4th",
      "page": "487",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "4 F.4th 487",
        "volume": "4",
        "reporter": "F.4th",
        "page": "487",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "4 F.4th 487",
    "official_selection": {
      "court_class": "state",
      "selected": "4 F.4th 487",
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
    "date_created": "2026-07-06T05:45:45Z",
    "date_modified": "2026-07-09T05:52:34Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:45:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:45:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:45:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:45:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "gaetjens-v-winnebago-county--4899427",
      "to_record_id": "Gaetjens v. Winnebago County",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Gaetjens v. Winnebago County

```
                               In the

    United States Court of Appeals
                 For the Seventh Circuit
                     ____________________
No. 20‐1295
SALLY GAETJENS,
                                                  Plaintiff‐Appellant,
                                 v.

CITY OF LOVES PARK, et al.,
                                               Defendants‐Appellees.
                     ____________________

         Appeal from the United States District Court for the
           Northern District of Illinois, Western Division.
           No. 16‐cv‐50261 — John Robert Blakey, Judge.
                     ____________________

       ARGUED MAY 27, 2021— DECIDED JULY 13, 2021
                ____________________

   Before KANNE, SCUDDER, and KIRSCH, Circuit Judges.
    KANNE, Circuit Judge. Plaintiﬀ Sally Gaetjens sued various
local government oﬃcials for entering and condemning her
home and confiscating her thirty‐seven cats, all without a
warrant. She’s right that the Fourth Amendment would usu‐
ally prohibit such conduct. But emergencies breed excep‐
tions—and this case is littered with emergencies.
2                                                   No. 20‐1295

    Namely, Gaetjens went missing in action, and Defendants
had reason to believe that she was experiencing a medical
emergency. Plus, when Defendants attempted to check her
home, they deemed it so noxious that it posed a public‐safety
risk. Given these exigencies, the Fourth Amendment did not
require Defendants to wait for judicial approval before acting.
We thus aﬃrm the decision of the district court granting sum‐
mary judgment to Defendants.
                       I. BACKGROUND
    The following facts are undisputed and stated in the light
most favorable to Gaetjens as the nonmoving party. Wonsey v.
City of Chicago, 940 F.3d 394, 399 (7th Cir. 2019) (citing Dayton
v. Oakton Cmty. Coll., 907 F.3d 460, 465 (7th Cir. 2018)).
   Gaetjens bred cats in her home in Loves Park, Illinois. On
December 4, 2014, she visited her doctor and was told to go to
the hospital because of high blood pressure. Later that day,
the doctor couldn’t locate Gaetjens, so she phoned Rosalie
Eads (Gaetjens’s neighbor who was listed as her emergency
contact) to ask for help finding her. Eads called Gaetjens and
knocked on her front door but got no response.
    The next day, Gaetjens was still missing, so Eads called the
Loves Park police and told them that Gaetjens might be expe‐
riencing a medical emergency. Defendant Sergeant Allton
and another oﬃcer went to Gaetjens’s Loves Park home but
could not see anyone inside. They did, though, notice pack‐
ages on the porch, untended garbage, and a full mailbox.
    The police then met up with Eads, who said she had a key
to the Loves Park house and confirmed what she had said on
the phone. With these facts before them, the police asked Eads
for the key so that they could enter to see if Gaetjens was in
No. 20‐1295                                                   3

danger. Eads obliged but also said that she thought perhaps
Gaetjens was at her other home in Rockford.
   The police went into the home but didn’t get far. After
making it about ten feet, intense odors forced them back out.
Allton described the smell as a mix of urine, feces, and maybe
a decomposing body.
    The police then called on the Loves Park Fire Department
to enter the home with breathing devices. Defendant Fire
Chief Foley arrived first, and Allton told him the whole tale.
So Foley approached the cracked front door for himself and
got a whiﬀ of something that could “gag a maggot.” Foley
thus temporarily condemned the home as not fit for human
or animal habitation by placing a placard on the front door
that read: “CONDEMNED[.] This Structure is Unsafe and Its
use or occupancy has been prohibited by the code administra‐
tor. It shall be unlawful for any person to enter such structure
except for the purpose of making the required repairs or re‐
moval.”
   More firefighters soon arrived and went into the home to
look for Gaetjens. But instead of Gaetjens, they found thirty‐
seven cats.
   At that point, the responders summoned Winnebago
County Animal Services to round up the cats because Gaet‐
jens was not allowed inside the condemned house to care for
the clowder herself. Some of the felines proved more diﬃcult
to catch than others. In particular, the male stud, Calaio,
looked ready to attack the workers. So they pulled out metal
“cat grabbers” to trap him.
4                                                    No. 20‐1295

   In the end, Animal Services impounded the cats from De‐
cember 4 to December 13, 2014. Sadly, four cats, including
Calaio, died as a result of the impoundment.
    Based on these events, Gaetjens—who unbeknownst to
the oﬃcers had been in the hospital all along—sued the City
of Loves Park, Winnebago County, and various employees of
each under 28 U.S.C. § 1983. Relevant to this appeal, she al‐
leged that the individual Defendants (Allton, Foley, and three
Animal Services employees) violated her Fourth Amendment
rights by (1) entering her home, (2) condemning her home,
and (3) seizing her cats. She also alleged that the City of Loves
Park and Winnebago County are liable for these violations
under Monell v. Department of Social Services of New York, 436
U.S. 658 (1978).
   The district court granted summary judgment to all De‐
fendants on all claims. Gaetjens now appeals.
                          II. ANALYSIS
   We review a district court’s grant of summary judgment
de novo. Wonsey, 940 F.3d at 399 (citing Dayton, 907 F.3d at
465). In this case, the district court determined that Gaetjens’s
Fourth Amendment claims fail because the individual de‐
fendants are entitled to qualified immunity. We agree that
Gaetjens’s claims fail, but for a more basic reason—the indi‐
vidual defendants did not violate the Fourth Amendment.
   The Fourth Amendment, made applicable to the States
through the Fourteenth Amendment, protects “[t]he right of
the people to be secure in their persons, houses, papers, and
eﬀects, against unreasonable searches and seizures.” U.S.
Const. amend. IV. This protection exists in both the criminal
and civil contexts. Soldal v. Cook County, 506 U.S. 56, 67 (1992).
No. 20‐1295                                                       5

    “[T]he ultimate touchstone of the Fourth Amendment is
‘reasonableness.’” Brigham City v. Stuart, 547 U.S. 398, 403
(2006) (citing Flippo v. West Virginia, 528 U.S. 11, 13 (1999); Katz
v. United States, 389 U.S. 347, 357 (1967)). “[S]earches and sei‐
zures inside a home without a warrant are presumptively un‐
reasonable.” Id. (quoting Groh v. Ramirez, 540 U.S. 551, 559
(2004)). But this “warrant requirement is subject to certain ex‐
ceptions.” Id. (citing Flippo, 528 U.S. at 13; Katz, 389 U.S. at
357).
     One such exception arises when “‘the exigencies of the sit‐
uation’ make the needs of law enforcement so compelling that
[a] warrantless search [or seizure] is objectively reasonable
under the Fourth Amendment.” Mincey v. Arizona, 437 U.S.
385, 394 (1978) (quoting McDonald v. United States, 335 U.S.
451, 456 (1948)) (citing Johnson v. United States, 333 U.S. 10, 14–
15 (1948)). In these situations, one principle governs—“[t]he
need to protect or preserve life or avoid serious injury is jus‐
tification for what would be otherwise illegal absent an exi‐
gency or emergency.” Id. at 392–93 (quoting Wayne v. United
States, 318 F.2d 205, 212 (D.C. Cir. 1963)).
    To determine whether an exigency permitted a warrant‐
less search or seizure in a home, we “conduct[] an objective
review, analyzing whether the government met its burden to
demonstrate that a reasonable officer had a ‘reasonable belief
that there was a compelling need to act and no time to obtain
a warrant.’” United States v. Andrews, 442 F.3d 996, 1000 (7th
Cir. 2006) (quoting United States v. Saadeh, 61 F.3d 510, 516 (7th
Cir. 1995)). This objective review looks at “the totality of facts
and circumstances ‘as they would have appeared to a reason‐
able person in the position of the ... officer—seeing what he saw,
hearing what he heard.’” Bogan v. City of Chicago, 644 F.3d 563,
6                                                     No. 20‐1295

572 (7th Cir. 2011) (quoting Mahoney v. Kesery, 976 F.2d 1054,
1057 (7th Cir. 1992)).
    The exigent circumstances doctrine applies equally to
warrantless searches of a home, seizures of a home, and sei‐
zures of private property within a home. See Sutterfield v. City
of Milwaukee, 751 F.3d 542, 558 (7th Cir. 2014); United States v.
Shrum, 908 F.3d 1219, 1231 (10th Cir. 2018) (“[T]he warrantless
seizure of a home … ‘is per se unreasonable, unless the police
can show that it falls within one of a carefully defined set of
exceptions based on the presence of “exigent circum‐
stances.”’” (quoting Coolidge v. New Hampshire, 403 U.S. 443,
474–75 (1971)) (citing Brigham City, 547 U.S. at 403)); Siebert v.
Severino, 256 F.3d 648, 657 (7th Cir. 2001) (“Exigent circum‐
stances may justify a warrantless seizure of animals.” (citing
DiCesare v. Stuart, 12 F.3d 973, 977 (10th Cir. 1993))).
    Here, all parties agree that Allton “searched” the Loves
Park home by entering it to look for Gaetjens. Likewise, all
agree that Foley “seized” the Loves Park home by placing a
condemnation placard on it and that the Animal Services
workers “seized” Gaetjens’s cats by capturing them. United
States v. Jacobsen, 466 U.S. 109, 113 (1984) (“A ‘seizure’ of prop‐
erty occurs when there is some meaningful interference with
an individual’s possessory interests in that property.”). Fi‐
nally, all agree that Defendants did not obtain warrants or any
other judicial or administrative approval before conducting
these searches and seizures.
    So, to satisfy the Fourth Amendment, Defendants’ war‐
rantless searches and seizures needed to fall into an exception
to the warrant requirement. They all did—each was justified
by an exigent circumstance.
No. 20‐1295                                                    7

    First, Allton (who searched the house) had an objectively
reasonable basis for believing that Gaetjens was experiencing
a medical emergency that required immediate action. Second,
Foley (who seized the house) had an objectively reasonable
basis on which to believe that the Loves Park home posed a
safety threat that required immediate attention. Third, the An‐
imal Services employees (who seized the cats) reasonably de‐
termined that the cats were in imminent danger because they
could not be cared for in the home.
   Last, because none of the individual defendants violated
Gaetjens’s Fourth Amendment rights, her Monell claims fail as
well.
   A. The Home Entry
    In an exigent circumstance often referred to as an “emer‐
gency‐aid” situation, government oﬃcials may enter a home
without a warrant “to ‘render assistance or prevent harm to
persons or property within.’” Sutterfield, 751 F.3d at 558 (quot‐
ing Sheik–Abdi v. McClellan, 37 F.3d 1240, 1244 (7th Cir. 1994)).
In a recent concurring opinion, Justice Kavanaugh provided
“[a] few (non‐exhaustive) examples [that] illustrate” “some
heartland emergency‐aid situations.” Caniglia v. Strom, 141 S.
Ct. 1596, 1604 (2021) (Kavanaugh, J., concurring). The follow‐
ing example is particularly apt for this appeal:
       Suppose that an elderly man is uncharacteristi‐
       cally absent from Sunday church services and
       repeatedly fails to answer his phone throughout
       the day and night. A concerned relative calls the
       police and asks the oﬃcers to perform a well‐
       ness check. Two oﬃcers drive to the man’s
8                                                  No. 20‐1295

       home. They knock but receive no response. May
       the oﬃcers enter the home? Of course.
Id. at 1605 (Kavanaugh, J., concurring); accord United States v.
Tepiew, 859 F.3d 452 (7th Cir. 2017) (permitting police oﬃcers’
warrantless entry into a home on the basis of a report from a
child in the home that her one‐year‐old brother had sustained
a head injury and had a puﬀy face).
    The home entry in this case likewise falls into the heart‐
land of emergency‐aid situations. It is undisputed that Allton
knew that (1) Eads and Gaetjens’s doctor were unable to get
in touch with Gaetjens; (2) the doctor’s oﬃce called Eads be‐
cause she was Gaetjens’s emergency contact; (3) Eads was
concerned that Gaetjens was experiencing a medical emer‐
gency; and (4) Gaetjens’s mail and garbage were piling up.
    If, as Justice Kavanaugh posits, failing to come to church
and answer a phone provides an objectively reasonable basis
for believing that an occupant needs emergency assistance,
then this litany of concerning circumstances facing Allton
more than provided him with the same. His warrantless entry
of the Loves Park home thus did not violate the Fourth
Amendment.
    In response, Gaetjens makes much of the fact that Eads
told Allton that she believed Gaetjens was at her Rockford
home, not her Loves Park home. But that statement just gave
Allton a reason to also look for Eads in her Rockford house; it
in no way contradicted the above facts that gave Allton an ob‐
jectively reasonable basis to enter the Loves Park home.
    B. The Condemnation
    “The exigent circumstances doctrine [also] allows oﬃcers
to enter a home without a warrant … to address a threat to the
No. 20‐1295                                                    9

safety of law enforcement oﬃcers or the general public … .”
Caniglia, 141 S. Ct. at 1603 (Kavanaugh, J., concurring) (citing,
among other cases, Michigan v. Cliﬀord, 464 U.S. 287, 293 & n.4
(1984)). Two precedents guide our analysis of whether Foley
had an objectively reasonable basis for believing that a safety
threat required him to condemn the Loves Park home without
a warrant.
    First, in Wonsey, building inspectors found thirty‐two
building code violations in the plaintiﬀ’s home. 940 F.3d at
398. Based on the “dangerous conditions” that those viola‐
tions presented, the inspectors asked the police to help them
with “emergency evacuations.” Id. The police did so, and then
faced a § 1983 suit from an evacuee for violating her Fourth
Amendment rights. Id. We rejected that claim because the
“police entered her house … to help with an evacuation given
an immediate safety concern.” Id. at 401.
    Second, the Sixth Circuit addressed a similar scenario in
Flatford v. City of Monroe, 17 F.3d 162 (6th Cir. 1994), which we
find persuasive. There, police officers evacuated a residential
apartment building after inspectors determined that it “posed
an immediate danger to its occupants and the public” because
of its dilapidated wooden structure and faulty electrical sys‐
tem. Id. at 171. The court determined that the officers were
entitled to qualified immunity for this warrantless evacuation
because they reasonably believed that their entry was justified
by exigent circumstances. Id. And the court noted that “[t]he
very point of the exigency exception under these circum‐
stances is to allow immediate effective action necessary to
protect the safety of occupants, neighbors, and the public at
large.” Id. at 170.
10                                                 No. 20‐1295

    This case aligns with both Wonsey and Flatford. Allton re‐
ported to Foley that the home was so noxious that the police
could not bear going in more than ten feet. Foley then probed
the front door himself and smelled a stench that could “gag a
maggot.” These circumstances gave Foley a reasonable basis
on which to conclude that the home’s “conditions posed an
immediate danger to its occupants and the public.” Id. at 171.
Thus his reflex to temporarily condemn the home and “pro‐
tect or preserve life” from such danger did not violate the
Fourth Amendment. Mincey, 437 U.S. at 392–93 (quoting
Wayne, 318 F.2d at 212).
     Gaetjens retorts that summary judgment on this claim is
inappropriate because the condition of the home was put in
dispute by the testimony of her friend, Joan Klarner, who tes‐
tified that she did not believe the home posed a health risk
when she visited it several hours before Defendants arrived.
But Klarner’s testimony doesn’t directly dispute the state of
the home as Defendants found it later on that day. More im‐
portant, even if the home was not as bad as Allton made it out
to be, Foley was nonetheless entitled to rely on Allton’s state‐
ments about the condition of the home because Allton had su‐
perior information after entering the home moments earlier.
Cf. Flatford, 17 F.3d at 170 (“[R]equiring officers to second
guess the more informed judgment of a building safety in‐
spector would hinder effective and swift action. Officers
should, therefore, have wide latitude to rely on a building‐
safety official’s expertise where that expert determination ap‐
pears to have some basis in fact.”).
     C. Confiscation of the Cats
    Last, “[e]xigent circumstances may justify a warrantless
seizure of animals” when an oﬃcial reasonably believes that
No. 20‐1295                                                    11

the animals are in “imminent danger.” Siebert, 256 F.3d at 657
(citing DiCesare, 12 F.3d at 977); see also, e.g., Commonwealth v.
Duncan, 7 N.E.3d 469, 471 (Mass. 2014) (finding exigent cir‐
cumstances to seize dogs where the dogs were left out “in se‐
verely inclement winter weather” and “extremely emaci‐
ated”); Hegarty v. Addison Cnty. Humane Soc’y, 848 A.2d 1139,
1143 (Vt. 2004) (permitting the warrantless seizure of a horse
where oﬃcer reasonably believed that the horse’s “health was
in jeopardy and that immediate action was required to protect
her”).
    The imminent danger to animals here was plain—Gaet‐
jens’s thirty‐seven cats could not be cared for in the Loves
Park home because the condemnation placard prevented
Gaetjens from entering the home for that purpose. Given this
situation, the Animal Services oﬃcials’ warrantless entry into
the Loves Park home and the seizure of her cats did not vio‐
late the Fourth Amendment.
   Gaetjens argues in rebuttal that regardless of whether An‐
imal Services could seize her cats, they still violated the
Fourth Amendment by using excessive force when doing so.
Specifically, she alleges that the oﬃcials used a “cat grabber”
that injured and ultimately killed the stud Calaio.
    We have held before that “the use of deadly force against
a household pet is reasonable only if the pet poses an imme‐
diate danger and the use of force is unavoidable.” Viilo v. Eyre,
547 F.3d 707, 710 (7th Cir. 2008) (citing Brown v. Muhlenberg
Township, 269 F.3d 205, 210–11 (3d Cir. 2001)). But that case,
and the cases from this circuit applying its rule, involved of‐
ficers shooting dogs with firearms. This case involved Animal
Services oﬃcials using a cat‐catching tool to catch a cat
(which, according to indisputable testimony, looked ready to
12                                                   No. 20‐1295

“maul” the cat‐catcher). That Calaio died as a result of this
manifestly reasonable tactic is unfortunate, but it does not an
unreasonable seizure make.
    Gaetjens also argues that even if the initial seizure of her
cats was lawful, Animal Services violated her Fourth Amend‐
ment rights by retaining the cats longer than necessary. This
argument fails because we have made clear that the Four‐
teenth Amendment, not the Fourth Amendment, provides the
appropriate basis for challenging post‐seizure procedures for
the retrieval of property. Bell v. City of Chicago, 835 F.3d 736,
741 (7th Cir. 2016).
    As a final note, Gaetjens argues that the district court in‐
correctly granted summary judgment sua sponte to the Animal
Services oﬃcials. While Gaetjens is correct that this procedure
warrants caution, it is permissible when “the losing party is
given notice and an opportunity to come forward with its ev‐
idence.” Jones v. Union Pac. R.R. Co., 302 F.3d 735, 740 (7th Cir.
2002) (citing Celotex Corp. v. Catrett, 477 U.S. 317, 326 (1986);
Goldstein v. Fid. and Guar. Ins. Underwriters, Inc., 86 F.3d 749,
750 (7th Cir. 1996)). Gaetjens has not argued here that she re‐
ceived inadequate notice, nor has she shown that she was de‐
prived of an opportunity to marshal evidence to dispute the
facts relied on in this opinion.
    We therefore conclude that the Animal Services workers,
like the other individual defendants, did not violate Gaet‐
jens’s Fourth Amendment rights.
     D. Monell Liability
    According to the Supreme Court’s decision in Monell, mu‐
nicipalities are sometimes liable for the constitutional viola‐
tions that their employees commit. 436 U.S. at 658. “But a
No. 20‐1295                                                      13

municipality cannot be liable under Monell when there is no
underlying constitutional violation by a municipal em‐
ployee.” Sallenger v. City of Springfield, 630 F.3d 499, 504 (7th
Cir. 2010) (citing King ex rel. King v. E. St. Louis Sch. Dist. 189,
496 F.3d 812, 817 (7th Cir. 2007); Jenkins v. Bartlett, 487 F.3d
482, 492 (7th Cir. 2007)). That’s the case here. Gaetjens’s con‐
stitutional rights were not violated, and thus her Monell claim
cannot succeed.
                        III. CONCLUSION
    For the foregoing reasons, we AFFIRM the judgment of the
district court.

```

---

## GROUP: content/cases/Glossip v. Oklahoma.md  (`case`, 5 assertions)

### content_page

```
---
title: "Glossip v. Oklahoma"
type: case
citation: "604 U.S. 226 (2025)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2025
date_decided: 2025-02-25
docket: 22-7466
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2025-02-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Glossip v. Oklahoma
  varies_by_point: false
  scope_note: "Good law (2025). Applies Napue v. Illinois: the prosecution's knowing failure to correct a key witness's false testimony violated due process and warranted a new trial. Slip opinion subject to formal revision. Distinct from Glossip v. Gross, 576 U.S. 863 (2015) (lethal-injection protocol)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10776870/glossip-v-oklahoma/"
  cluster_id: 10776870
  opinion_id: 11243457
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Napue v. Illinois]]", "[[Giglio v. United States]]", "[[Brady v. Maryland]]", "[[United States v. Bagley]]", "[[Banks v. Dretke]]", "[[Mooney v. Holohan]]"]
aliases: []
tags: ["case", "brady", "giglio", "napue", "false-testimony", "prosecutorial-misconduct", "due-process", "capital", "2025"]
holding: "The prosecution's knowing failure to correct a key witness's false testimony (the State's only direct-evidence witness denied his bipolar diagnosis and lithium prescription) violated the Napue due-process duty to correct false testimony; because the witness's credibility was necessarily determinative, there was a reasonable likelihood the false testimony affected the verdict, entitling the defendant to a new trial."
lake:
  record_id: Glossip v. Oklahoma
  status: verified
  projected_at: 2026-07-06
---

# Glossip v. Oklahoma

*604 U.S. 226 (2025)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Richard Glossip was convicted and sentenced to death for allegedly paying Justin Sneed to beat Barry Van Treese to death at an Oklahoma motel Glossip managed. Sneed — who admitted he did the killing — was the only direct evidence linking Glossip to the murder. At trial Sneed denied that he had been prescribed lithium or seen a psychiatrist, testifying he received lithium after asking for cold medicine. Decades later the State disclosed boxes of withheld documents showing Sneed had been diagnosed with bipolar disorder and prescribed lithium by a jail psychiatrist, and that the prosecutor (Smothermon) knew this. Oklahoma's attorney general confessed error and asked the state court for a new trial, but the Oklahoma Court of Criminal Appeals (OCCA) denied relief, finding no *[[Napue v. Illinois|Napue]]* violation. The Supreme Court stayed Glossip's execution and granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
Whether the prosecution's failure to correct Sneed's false testimony about his psychiatric diagnosis and lithium prescription violated the due-process duty recognized in *[[Napue v. Illinois]]*, entitling Glossip to a new trial (and whether the Court had jurisdiction over the OCCA's procedural ruling).

## Rule
A prosecutor must correct testimony it knows to be false. Under [[Napue v. Illinois]], a conviction knowingly "obtained through use of false evidence" violates the Fourteenth Amendment's Due Process Clause; "[t]o establish a *Napue* violation, a defendant must show that the prosecution knowingly solicited false testimony or knowingly allowed it 'to go uncorrected when it appear[ed].'" — 604 U.S. 226 (slip op., at 16–17). ^pin-226

If shown, materiality is a forgiving, prosecution-burden standard: "a new trial is warranted so long as the false testimony 'may have had an effect on the outcome of the trial,' … that is, if it '"in any reasonable likelihood [could] have affected the judgment of the jury,"'" — *id.* (slip op., at 17) (quoting *Giglio v. United States*, 405 U.S. 150, 154 (1972), in turn quoting *[[Napue v. Illinois|Napue]]*, 360 U.S. at 271). ^pin-226b

False testimony "goes only to the credibility of the witness" can be material, for "[t]he jury's estimate of the truthfulness and reliability of a given witness may well be determinative of guilt or innocence." — *id.* (slip op., at 19) (quoting *Napue*, 360 U.S. at 269).

## Application
The Court first held it had jurisdiction: the OCCA's procedural bar was not an independent and adequate state ground because it turned on the antecedent federal-law ruling that there was no *[[Napue v. Illinois|Napue]]* error. On the merits, the record supported the attorney general's confession of error — Sneed's denial of his lithium prescription and psychiatric treatment was false, and the prosecution (which had access to Sneed's medical and competency records and whose notes referenced "lithium" and "Dr. Trumpet") knew it was false and let it stand. Materiality was clear because "Sneed's testimony was the only direct evidence of Glossip's guilt of capital murder," so "the jury's assessment of Sneed's credibility was necessarily determinative." Correcting the lie would have shown Sneed was willing to lie under oath and would have undercut the prosecution's portrayal of him as harmless, so there was a reasonable likelihood it would have affected the verdict. Additional misconduct (a sequestration violation, destroyed evidence, withheld statements) further undermined confidence in the verdict.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]. The prosecution's failure to correct Sneed's false testimony violated *[[Napue v. Illinois|Napue]]*, and because the Court had jurisdiction and the confession of error was amply supported, a new trial — not a remand for further evidentiary proceedings — was the appropriate remedy.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Sotomayor, J., joined by Roberts, C.J., and Kagan, Kavanaugh, and Jackson, JJ., and by Barrett, J., as to Part II; Barrett, J., concurring in part and dissenting in part; Thomas, J., joined by Alito, J., dissenting; Gorsuch, J., took no part). [[Reading and Citing Cases#slip-opinion|Slip opinion]] subject to formal revision before publication in the U.S. Reports.
- *Glossip* is the most recent SCOTUS application of the [[Napue v. Illinois]] / [[Giglio v. United States]] knowing-false-testimony rule, which descends from [[Mooney v. Holohan]] and runs alongside the [[Brady v. Maryland]] / [[United States v. Bagley]] / [[Banks v. Dretke]] disclosure line. No negative treatment.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Glossip v. Oklahoma*, 604 U.S. 226 (2025) — https://www.courtlistener.com/opinion/10339023/glossip-v-oklahoma/ — pinpoints: slip op., at 2, 16–17, 19 (CL stores the slip opinion "604 U.S. ___ (2025)," subject to formal revision; pins keyed to the official case-start page 226). Internal authorities pinpointed: *Napue*, 360 U.S. at 269, 271; *Giglio*, 405 U.S. at 154.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "63459309da801935", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "604 U.S. 226 (2025)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Glossip v. Oklahoma", "year": "2025"}}
{"assertion_id": "cd6b3179cfe618ca", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The prosecution's knowing failure to correct a key witness's false testimony (the State's only direct-evidence witness denied his bipolar diagnosis and lithium prescription) violated the Napue due-process duty to correct false testimony; because the witness's credibility was necessarily determinative, there was a reasonable likelihood the false testimony affected the verdict, entitling the defendant to a new trial.", "title": "Glossip v. Oklahoma"}}
{"assertion_id": "f4c075e823817b54", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Glossip v. Oklahoma"}}
{"assertion_id": "a77bc531f40ce3bc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2025-02-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Glossip v. Oklahoma", "field_i_validity": "good_law", "scope_note": "Good law (2025). Applies Napue v. Illinois: the prosecution's knowing failure to correct a key witness's false testimony violated due process and warranted a new trial. Slip opinion subject to formal revision. Distinct from Glossip v. Gross, 576 U.S. 863 (2015) (lethal-injection protocol).", "title": "Glossip v. Oklahoma", "varies_by_point": "false"}}
{"assertion_id": "b7a1338484736831", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Glossip v. Oklahoma"}}
```

### lake record — Glossip v. Oklahoma

```json
{
  "schema_version": "s2.v1",
  "record_id": "Glossip v. Oklahoma",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Glossip v. Oklahoma",
    "case_name_short": "Glossip",
    "case_name_full": "",
    "input_case_name": "Glossip v. Oklahoma",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2025-02-25",
    "year": 2025,
    "docket": "22-7466",
    "cluster_id": 10776870,
    "lead_opinion_id": 11243457,
    "sibling_ids": [
      11243457
    ],
    "absolute_url": "/opinion/10776870/glossip-v-oklahoma/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 10339193,
        "score": 120,
        "case_name": "Glossip v. Oklahoma Revisions: 2/25/25"
      },
      {
        "cluster_id": 10339023,
        "score": 120,
        "case_name": "Glossip v. Oklahoma"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "604 U.S. 226",
      "volume": "604",
      "reporter": "U.S.",
      "page": "226",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "604 U.S. 226",
        "volume": "604",
        "reporter": "U.S.",
        "page": "226",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "604 U.S. 226",
    "official_selection": {
      "court_class": "scotus",
      "selected": "604 U.S. 226",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-226",
      "page": null,
      "quote": "--- # Glossip v. Oklahoma *604 U.S. 226 (2025)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Richard Glossip was convicted and sentenced to death for allegedly paying Justin Sneed to beat Barry Van Treese to death at an Oklahoma motel Glossip managed. Sneed \u2014 who admitted he did the killing \u2014 was the only direct evidence linking Glossip to the murder. At trial Sneed denied that he had been prescribed lithium or seen a psychiatrist, testifying he received lithium after asking for cold medicine. Decades later the State disclosed boxes of withheld documents showing Sneed had been diagnosed with bipolar disorder and prescribed lithium by a jail psychiatrist, and that the prosecutor (Smothermon) knew this. Oklahoma's attorney general confessed error and asked the state court for a new trial, but the Oklahoma Court of Criminal Appeals (OCCA) denied relief, finding no *Napue* violation. The Supreme Court stayed Glossip's execution and granted certiorari. ## Issue Whether the prosecution's failure to correct Sneed's false testimony about his psychiatric diagnosis and lithium prescription violated the due-process duty recognized in *Napue v. Illinois*, entitling Glossip to a new trial (and whether the Court had jurisdiction over the OCCA's procedural ruling). ## Rule A prosecutor must correct testimony it knows to be false. Under [[Napue v. Illinois]], a conviction knowingly",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-226b",
      "page": null,
      "quote": "a new trial is warranted so long as the false testimony 'may have had an effect on the outcome of the trial,' \u2026 that is, if it '",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2025-02-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Glossip v. Oklahoma",
    "varies_by_point": false,
    "scope_note": "Good law (2025). Applies Napue v. Illinois: the prosecution's knowing failure to correct a key witness's false testimony violated due process and warranted a new trial. Slip opinion subject to formal revision. Distinct from Glossip v. Gross, 576 U.S. 863 (2015) (lethal-injection protocol).",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11243457) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
        "query": "cites:(11243457)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11243457)",
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
    "complete_query": "cites:(11243457)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11243457,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/glossip-v-oklahoma.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11243457,
        "cited_id": 103610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 108164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 112456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 121172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 145766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 1087618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 2581658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3183080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3803122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3805789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3817059,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3828772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3835480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 4687472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5146505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5148027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5149077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5149899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5515949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 6105120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 6496181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 6671986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 8413606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9323214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9373886,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9405083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9406339,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9416986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9420168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9422312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9422583,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9423348,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9426342,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9426498,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9428656,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9429592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9429915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9430189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9431798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9433091,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9433120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9433984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9434187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9434809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9435084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9796753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9796834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9797364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9821185,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9823487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9841311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9841318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9842050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9842054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9842121,
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
    "date_created": "2026-07-05T05:35:25Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:35:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:35:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:36:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:35:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Glossip v. Oklahoma (truncated)

```
                   PRELIMINARY PRINT

              Volume 604 U. S. Part 1
                             Pages 226–304




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                             February 25, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
226                     OCTOBER TERM, 2024

                                 Syllabus


                    GLOSSIP v. OKLAHOMA

      certiorari to the court of criminal appeals of
                         oklahoma
   No. 22–7466. Argued October 9, 2024—Decided February 25, 2025
In 1997, Justin Sneed beat Barry Van Treese to death with a baseball bat
  at an Oklahoma hotel owned by Van Treese and managed by petitioner
  Richard Glossip. Glossip initially made inconsistent statements to the
  police about Sneed's role in the murder, but he ultimately told police
  that Sneed admitted to killing Van Treese. Sneed later claimed Glossip
  had asked him to murder Van Treese because, among other things,
  Glossip had wanted to steal Van Treese's money. Glossip maintained
  his innocence and refused a plea deal that would have had him avoid the
  death penalty in return for testifying against Sneed. Sneed then testi-
  fed against Glossip at trial in exchange for avoiding the death penalty,
  and Sneed's testimony was the only direct evidence connecting Glossip
  to the murder. The jury convicted Glossip and sentenced him to death.
  The Oklahoma Court of Criminal Appeals (OCCA) overturned that con-
Page Proof Pending Publication
  viction because the defense had been ineffective in challenging Sneed's
  testimony and the remainder of the evidence only weakly corroborated
  Sneed's account. At the retrial, Sneed provided inconsistent testimony
  on potential motives for Glossip's murder. Sneed also denied that he
  had been prescribed lithium or seen a psychiatrist. After the defense
  established (through the State's medical examiner) that Van Treese had
  been attacked with a knife as well as a bat, Sneed testifed that he had
  repeatedly tried to stab Van Treese in the chest with a pocket knife.
  But Sneed had previously denied stabbing Van Treese both when ques-
  tioned by the police as well as at Glossip's frst trial. Glossip moved for
  a mistrial based on the prosecution's failure to notify the defense about
  Sneed's change in testimony, which the trial court denied after the
  prosecution disclaimed any knowledge about the change. Glossip was
  again convicted and sentenced to death, and a closely divided OCCA
  affrmed, holding that circumstantial evidence suggesting Glossip had
  mismanaged the hotel, combined with Glossip's concession that he had
  been dishonest in his initial statements after the murder, suffciently
  corroborated Sneed's testimony that he killed Van Treese at Glossip's
  direction.
     Glossip subsequently fled several unsuccessful habeas petitions.
  Concerns over the integrity of his conviction led a bipartisan group of
                       Cite as: 604 U. S. 226 (2025)                      227

                                  Syllabus

  Oklahoma legislators to commission an independent investigation by a
  law frm, Reed Smith. In June 2022, Reed Smith reported “grave
  doubt” about Glossip's conviction, citing factors such as the prosecution's
  deliberate destruction of key evidence and the false portrayal of Justin
  Sneed as a non-violent “puppet.” The State then disclosed seven boxes
  of previously withheld documents, including letters suggesting Sneed
  had considered recanting and a note from prosecutor Connie Smother-
  mon to Sneed's lawyer noting they should “get to” Sneed to discuss his
  problematic testimony about a knife found in Van Treese's room.
  Glossip fled for post-conviction relief based on this evidence and evi-
  dence revealed by Reed Smith. Glossip also argued that, during his
  second trial, Smothermon had interfered with Sneed's testimony about
  the knife in violation of the rule of sequestration, which prohibits wit-
  nesses from hearing each other's testimony. Oklahoma waived any pro-
  cedural defenses to Glossip's claims, and asked the OCCA to deny the
  claims on their merits. The OCCA denied Glossip's claims as procedur-
  ally barred and meritless.
     The State then discovered additional documents revealing that Sneed
  had been diagnosed with bipolar disorder and prescribed lithium, contra-
  dicting his trial testimony. The attorney general determined that

Page Proof Pending Publication
  Smothermon had knowingly elicited false testimony from Sneed and
  failed to correct it, violating Napue v. Illinois, 360 U. S. 264, which held
  that prosecutors have a constitutional obligation to correct false testi-
  mony. Glossip fled a successive petition for post-conviction relief,
  which the attorney general supported, conceding multiple errors that
  warranted a new trial. The OCCA denied the unopposed petition with-
  out a hearing, holding that Glossip's claims were procedurally barred
  under Oklahoma's Post-Conviction Procedures Act (PCPA), and further
  that the State's concession was not “based in law or fact” because it did
  not create a Napue error. This Court stayed Glossip's execution and
  granted certiorari.
Held:
    1. This Court has jurisdiction to review the OCCA's judgment. The
 independent and adequate state ground doctrine precludes the Court
 from considering a federal question if the state court's decision rests on
 an independent and adequate state-law ground. The OCCA's applica-
 tion of the PCPA was not such a ground, because the OCCA's decision
 to apply the PCPA depended on its antecedent rejection of the attorney
 general's confession of a Napue error, which was based solely on federal
 law. The OCCA held that the confession could not overcome the
 PCPA's limitations because it lacked a basis in law or fact, specifcally
 fnding no Napue error.
228                   GLOSSIP v. OKLAHOMA

                                Syllabus

    Oklahoma precedent confrms that the OCCA normally rejects an at-
 torney general's confession of error only after fnding it unsupported by
 law and the record. By making the application of the PCPA contingent
 on its determination that the attorney general's confession of federal
 constitutional error was baseless, the OCCA made the procedural bar
 dependent on an antecedent ruling on federal law. To the extent that
 the OCCA's reasoning on this point is insuffciently “clear from the face
 of the opinion,” the Court presumes reliance on federal law under Mich-
 igan v. Long, 463 U. S. 1032, 1040–1041. Pp. 242–246.
    2. The prosecution violated its constitutional obligation to correct
 false testimony. Pp. 246–258.
       (a) Under Napue, a conviction obtained through the knowing use
 of false evidence violates the Fourteenth Amendment's Due Process
 Clause. To establish a Napue violation, a defendant must show that
 the prosecution knowingly solicited or allowed false testimony to go
 uncorrected. If a violation is established, a new trial is warranted if
 the false testimony could in any reasonable likelihood have affected the
 jury's judgment; meaning, ordinarily, that the prosecution must estab-
 lish harmlessness beyond a reasonable doubt. United States v. Bagley,
 473 U. S. 667, 680, n. 9; Chapman v. California, 386 U. S. 18, 24. Here,
Page Proof Pending Publication
 Oklahoma's attorney general joins Glossip in asserting a Napue error,
 conceding that Sneed's testimony about his lithium prescription was
 false and that the prosecution knowingly failed to correct it. The rec-
 ord supports that confession of error. Evidence showed that Sneed was
 prescribed lithium to treat bipolar disorder, not after asking for cold
 medicine as he claimed at trial. The evidence likewise establishes that
 the prosecution knew Sneed's testimony was false. The prosecution al-
 most certainly had access to Sneed's medical fle through Sneed's compe-
 tency evaluation. And Smothermon's notes show that she had a pre-
 trial conversation with Sneed at which he mentioned “lithium” and “Dr.
 Trumpet.” The straightforward inference is that Smothermon was
 aware before trial that Sneed had received his lithium prescription from
 Dr. Trombka, a psychiatrist and the sole medical professional at the
 Oklahoma County jail authorized to prescribe lithium.
    Because Sneed's testimony was the only direct evidence of Glossip's
 guilt, the jury's assessment of Sneed's credibility was material and nec-
 essarily determinative. Correcting Sneed's lie would have undermined
 his credibility and revealed his willingness to lie under oath. The false
 testimony also bore on Glossip's guilt because evidence of Sneed's bipo-
 lar disorder, which could trigger impulsive violence when combined with
 his drug use, would have contradicted the prosecution's portrayal of
 Sneed as harmless without Glossip's infuence. Hence there is a reason-
                        Cite as: 604 U. S. 226 (2025)                      229

                                  Syllabus

  able likelihood that correcting Sneed's testimony would have affected
  the judgment of the jury. Napue, 360 U. S., at 271. Additional prose-
  cutorial misconduct, such as violating the rule of sequestration, destroy-
  ing evidence, and withholding witness statements, further undermines
  confdence in the verdict. Consequently, the prosecution's failure to
  correct Sneed's false testimony entitles Glossip to a new trial under
  Napue. Pp. 246–252.
       (b) The OCCA's contrary holding rests on a mistaken interpretation
  of Napue. The OCCA held that there was no violation because the
  defense was aware or should have been aware that Sneed was taking
  lithium. But Sneed's false testimony concerned the reasons for his pre-
  scription, not merely the fact that he had taken lithium. Moreover, the
  Due Process Clause imposes the duty to correct false testimony on the
  State, not the defense. The OCCA's holding that Sneed was likely in de-
  nial of his mental health disorders is beside the point; what matters is that
  the testimony was false and the prosecutor knowingly allowed it to stand.
     Additional arguments in support of the OCCA's position are unpersua-
  sive. Napue does not require that the false testimony itself must have
  directly affected the trial's outcome; Napue requires assessing whether
  the prosecutor's failure to correct the testimony could have contributed
  to the verdict. Also unpersuasive are arguments based on extra-record
Page Proof Pending Publication
  materials and insuffcient time spent interviewing the prosecutor.
     Because the attorney general's confession of error is supported by
  ample evidence, the Court declines to remand this case for further evi-
  dentiary proceedings. When the Court has jurisdiction, a new trial is
  the appropriate remedy for a violation of Napue. Pp. 252–258.
529 P. 3d 218, reversed and remanded.

   Sotomayor, J., delivered the opinion of the Court, in which Roberts,
C. J., and Kagan, Kavanaugh, and Jackson, JJ., joined, and in which
Barrett, J., joined as to Part II. Barrett, J., fled an opinion concur-
ring in part and dissenting in part, post, p. 258. Thomas, J., fled a dis-
senting opinion, in which Alito, J., joined, and in which Barrett, J.,
joined as to Parts IV–A–1, IV–A–2, and IV–A–3, post, p. 262. Gorsuch,
J., took no part in the consideration or decision of the case.

  Seth P. Waxman argued the cause for petitioner. With
him on the briefs were Catherine M. A. Carroll, Zaki
Anwar, Donald R. Knight, Amy P. Knight, John R. Mills,
and Joseph J. Perkovich.
  Paul D. Clement argued the cause for respondent under
this Court's Rule 12.6. With him on the briefs were Gentner
F. Drummond, Attorney General of Oklahoma, Garry M.
230                    GLOSSIP v. OKLAHOMA

                                 Syllabus

Gaskins II, Solicitor General, Matthew D. Rowen, and Jo-
seph J. DeMott.
  Christopher G. Michel, by invitation of the Court, 601 U. S.
1010, argued the cause and fled a brief as amicus curiae in
support of the judgment below. With him on the brief were
Rachel G. Frank, Alex Van Dyke, and Nicholas J. Caluda.*

  *Briefs of amici curiae urging reversal were fled for the District of
Columbia et al. by Brian L. Schwalb, Attorney General of the District
of Columbia, Caroline S. Van Zile, Solicitor General, Ashwin P. Phatak,
Principal Deputy Solicitor General, Graham E. Phillips, Deputy Solicitor
General, and Elissa R. Lowenthal, Assistant Attorney General, and by
the Attorneys General for their respective States as follows: Philip J.
Weiser of Colorado, Kwame Raoul of Illinois, Anthony G. Brown of Mary-
land, Andrea Joy Campbell of Massachusetts, Keith Ellison of Minnesota,
Aaron D. Ford of Nevada, Matthew J. Platkin of New Jersey, Raúl Torrez
of New Mexico, Letitia James of New York, and Ellen F. Rosenblum of
Oregon; for the American Civil Liberties Union et al. by William R.
Weaver, David D. Cole, Brian W. Stull, Randy Alan Bauman, and Megan
Page Proof Pending Publication
Lambert; for Former Members of the Oklahoma Death Penalty Review
Commission by Carter G. Phillips, Virginia A. Seitz, and Jacqueline G.
Cooper; for the Innocence Project by Andrianna D. Kastanek; for the
National Association of Criminal Defense Lawyers by Barbara E. Berg-
man and Hassan Ahmad; for R. Michael Cassidy et al. by Meaghan
VerGow, Joshua Revesz, and Bruce A. Green; for Kenneth T. Cuccinelli
II, by Emmet T. Flood; and for Rep. Kevin McDugle et al. by Gregory
G. Garre.
  Briefs of amici curiae were fled for the State of Texas by Ken Paxton,
Attorney General, Brent Webster, First Assistant Attorney General,
Aaron L. Nielson, Solicitor General, Philip A. Lionberger, Assistant
Solicitor General, and Matthew Ottoway and J. Andrew Mackenzie, Assist-
ant Attorneys General; for the State of Utah et al. by Sean D. Reyes,
Attorney General of Utah, Stanford E. Purser, Solicitor General, Andrew
F. Peterson, Deputy Solicitor General, and Ginger Jarvis and Mark C.
Field, Assistant Solicitors General, and by the Attorneys General for their
respective States as follows: Treg R. Taylor of Alaska, Tim Griffn of
Arkansas, Liz Murrill of Louisiana, Austin Knudsen of Montana, Alan
Wilson of South Carolina, and Jonathan Skrmetti of Tennessee; for the
Criminal Justice Legal Foundation by Kent S. Scheidegger; for Current
and Former State and Federal Prosecutors by David A. Senior and Ann
K. Tria; for Federal Courts Scholars by Melanie L. Bostwick, Thomas M.
                     Cite as: 604 U. S. 226 (2025)               231

                        Opinion of the Court

   Justice Sotomayor delivered the opinion of the Court.
   An Oklahoma jury convicted petitioner Richard Glossip of
paying Justin Sneed to murder Barry Van Treese and sen-
tenced him to death. At trial, Sneed admitted he beat Van
Treese to death, but testifed that Glossip had offered him
thousands of dollars to do so. Glossip confessed he helped
Sneed conceal his crime after the fact, but he denied any
involvement in the murder.
   Nearly two decades later, the State disclosed eight boxes
of previously withheld documents from Glossip's trial.
These documents show that Sneed suffered from bipolar dis-
order, which, combined with his known drug use, could have
caused impulsive outbursts of violence. They also estab-
lished, the State agrees, that a jail psychiatrist prescribed
Sneed lithium to treat that condition, and that the prosecu-
tion allowed Sneed falsely to testify at trial that he had
never seen a psychiatrist. Faced with that evidence, Okla-
homa's attorney general confessed error. Before the Okla-
Page Proof Pending Publication
homa Court of Criminal Appeals (OCCA), the State conceded
that the prosecution's failure to correct Sneed's testimony
violated Napue v. Illinois, 360 U. S. 264 (1959), which held
that prosecutors have a constitutional obligation to correct
false testimony. The attorney general accordingly asked
the court to grant Glossip a new trial. The OCCA declined
to grant relief because, it held, the State's concession was
not “based in law or fact.” 2023 OK CR 5, ¶25, 529 P. 3d
218, 226. Because the prosecution violated its obligations
under Napue, we reverse the judgment below and remand
the case for a new trial.
                              I
                                  A
  Barry Van Treese owned a Best Budget Inn in Tulsa and
in Oklahoma City. Richard Glossip managed the Oklahoma

Bondy, and Katherine M. Kopp; and for Derek Van Treese et al. by Paul
G. Cassell.
232                GLOSSIP v. OKLAHOMA

                      Opinion of the Court

City hotel and lived there with his girlfriend. In the sum-
mer of 1996, Justin Sneed and his stepbrother approached
Glossip and asked him about working for a room. 2 App.
648. Glossip agreed to let them stay in return for help with
maintenance and housekeeping. Sneed, however, had a his-
tory of violence, angry outbursts, and substance abuse that
included marijuana, methamphetamine, cocaine, and acid.
Id., at 700–701. When, on January 6, 1997, Van Treese vis-
ited the inn to collect cash deposits there, Sneed beat him to
death with a baseball bat. See 2007 OK CR 12, ¶¶4–5, 157
P. 3d 143, 147–148 (Glossip II).
   After killing Van Treese, Sneed evaded law enforcement
for several days. Police did promptly interview Glossip,
who told them that Sneed had knocked on his door that night
with a bump on his head “like somebody punched him.”
App. to Response to Petitioner's Succ. Application for Post-
Conviction Relief in No. PCD–2022–819, Tr. of Glossip Police
Page Proof Pending Publication
Interview 15 (Jan. 8, 1997). Glossip added that Sneed had
told him he slipped in the shower. Ibid. Glossip disclaimed
any knowledge of Van Treese's murder, but admitted that he
helped Sneed replace (from the outside) the broken window
of the room where Van Treese's body was later found. The
next day, offcers arrested Glossip in front of an attorney's
offce with approximately $1,700 in cash on him. 1 App. 291–
292. Glossip then admitted Sneed had told him “that he
killed Barry.” Tr. of Glossip Police Interview 10 (Jan. 9,
1997). When confronted with his prior inconsistent state-
ments about the murder and Van Treese's whereabouts,
Glossip said that he had been scared to tell the truth because
he feared his failure to notify the police immediately meant
he was “already involved in it.” Id., at 29–30.
   The State thereafter charged Sneed with capital murder
and Glossip as an accessory after the fact based on his inac-
curate statements to the police. Eventually, police located
and interviewed Sneed, who had $1,680 in bloody cash on
him. See 14 Tr. 18 (May 28, 2004); 15 Tr. 170 (June 1, 2004).
                   Cite as: 604 U. S. 226 (2025)           233

                      Opinion of the Court

The offcers told Sneed that before he “ma[de] up [his] mind
on anything” they wanted him “to hear some of the things”
they “[had] to say,” including that they did not think Sneed
had acted alone and that he should not “take the whole
thing” himself. 2 App. 645–646. “[E]verybody” was mak-
ing Sneed “the scapegoat in this,” they told him—especially
Glossip, who was “putting it on [him] the worst.” Id., at 655.
   Sneed initially responded to the offcers' prompts by at-
tempting to implicate his brother, ibid., but eventually said
that Glossip had wanted to steal Van Treese's money and
that Van Treese's death had been the result of a robbery
gone wrong. Id., at 655–660. Sneed described breaking
into Van Treese's room and beating him with a baseball bat
until he “fgured he was knocked out.” Id., at 665. Accord-
ing to Sneed, he then took Van Treese's car keys, stole an
envelope with approximately $4,000 in cash from his car, and
split the money with Glossip. Id., at 665–669. When off-
Page Proof Pending Publication
cers pressed him on the state of Van Treese's body, Sneed
asserted that, “[a]ctually,” Glossip had asked him to kill Van
Treese so that he “could run the motel without him being
the boss.” Id., at 675.
   Following Sneed's interview, Oklahoma charged Glossip,
too, with capital murder. The prosecution offered Glossip a
deal: plead guilty and avoid the death sentence in return for
testifying against Sneed. See App. to Pet. for Cert. in No.
22–6500, p. 144a. When Glossip refused, maintaining his in-
nocence, the State offered Sneed the same deal, and Sneed
accepted. 2001 OK CR 21, ¶5, 29 P. 3d 597, 599 (Glossip I).
Sneed then testifed at Glossip's trial that he beat Van Treese
to death “because [Glossip] asked him to do it.” Ibid.
When asked whether there was any “particular reason why
[Glossip] wanted to kill [Van Treese]” that night, Sneed re-
plied, “Not that I know of. Every time that Mr. Van Treese
showed up, [Glossip] was wanting me to kill him.” 6 Tr. 89
(June 8, 1998). In closing, the prosecution argued that
Glossip had asked Sneed to kill Van Treese because he be-
234                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

lieved Van Treese planned to fre him for embezzling hotel
profts. 8 Tr. 14–15 (June 10, 1998). The jury convicted
Glossip and sentenced him to death.
   The OCCA unanimously reversed. Sneed's testimony was
the only direct evidence connecting Glossip to the murder, it
held, and “[t]he evidence at trial tending to corroborate
Sneed's testimony was extremely weak.” Glossip I, 29
P. 3d, at 599. Defense counsel's failure to cross-examine
Sneed on his many inconsistent statements was therefore “so
ineffective” as to undermine any “confdence that a reliable
adversarial proceeding took place.” Ibid.
   In 2004, after Glossip rejected another plea offer, 3 App.
720, the State tried him a second time. Several witnesses
confrmed what Glossip had told the police in his second in-
terview: In the hours following Van Treese's killing, Glossip
feigned ignorance and lied about Van Treese's whereabouts.
As in the frst trial, however, only one witness, Justin Sneed,
testifed that Glossip was involved in anything more.1
Page Proof Pending Publication
   This time, moreover, the defense established (through the
State's medical examiner) that Van Treese had been attacked

  1
    The dissent's narrative, which presents as historical fact the testimony
of the prosecution's witnesses at Glossip's second trial, relies heavily on
Sneed's testimony to suggest that Glossip directed the crime and an elabo-
rate coverup. See post, at 262–267 (opinion of Thomas, J.). To the ex-
tent the dissent relies on witnesses other than Sneed, their testimony con-
frms no more than what Glossip himself admitted to the police. As for
Sneed's testimony, the dissent constructs its favored narrative from among
his multiple inconsistent accounts of the murder. See supra, at 232–235;
compare post, at 264 (dissent asserting that “Sneed left [Van Treese's
room] when he thought that he had killed Van Treese”), with 2 App. 665
(Sneed telling police he left Van Treese's room when he thought Van
Treese was “knocked out”); compare post, at 264 (dissent asserting Glossip
told Sneed “they would both be evicted if Glossip lost his job”), with 2
App. 655–665 (Sneed telling police that Van Treese's death was the acci-
dental result of a robbery gone wrong), 6 Tr. 89 (June 8, 1998) (Sneed
testifying that he did not know why Glossip wanted him to kill Van
Treese), and 12 Tr. 75 (May 26, 2004) (Sneed testifying that Glossip had
wanted to rob Van Treese).
                   Cite as: 604 U. S. 226 (2025)           235

                      Opinion of the Court

with a knife as well as with a baseball bat. 1 id., at 239–
245. Although Sneed had denied stabbing Van Treese to the
police and at Glossip's frst trial, he now said that he had
repeatedly tried to stab Van Treese in the chest with a
pocket knife. Glossip II, 157 P. 3d, at 148–149. Because
the prosecution had not notifed the defense about this
change in testimony, Glossip moved for a mistrial. 12 Tr.
105 (May 26, 2004). The trial court denied that motion after
the prosecution attested that the change was news to them,
too. Id., at 107–108 (“The chest thing we're all hearing at
the same time”).
  The prosecution also asked Sneed whether anyone had
prescribed him any medication:
    “Q. After you were arrested, were you placed on any
    type of prescription medication?
    “A. When I was arrested I asked for some Sudafed be-
    cause I had a cold, but then shortly after that somehow
Page Proof Pending Publication
    they ended up giving me Lithium for some reason, I don't
    know why. I never seen no psychiatrist or anything.
    “Q. So you don't know why they gave you that?
    “A. No.” Id., at 64.

Sneed then confrmed that he used illegal drugs including
marijuana and “crank” (methamphetamine) “twice a week”
prior to his arrest. Id., at 64–65. Finally, Sneed testifed
about Glossip's purported motives for killing Van Treese.
He asserted that Glossip had suggested “robbing Barry of
his money,” id., at 75, that he had “told [Sneed] at one point
that with Mr. Van Treese out of the way . . . he would be
able not only [to] manage the motel on Council but also an-
other one they had [in Tulsa],” id., at 89, and that he had
worried he “was going to get fred” because “a couple of the
rooms that were already supposed to be remodeled . . .
weren't,” id., at 95.
  The prosecution weaved these suggestions into its closing
argument along with its original theory that Glossip had
236                  GLOSSIP v. OKLAHOMA

                        Opinion of the Court

wanted Van Treese dead to avoid being fred for embezzle-
ment. See 15 Tr. 65 (June 1, 2004) (arguing Glossip's motive
was “a big wad of around 4,000 bucks of American good Yan-
kee dollars to split with the kid”); id., at 153, 163 (arguing
Glossip was going to be fred because of “missing money”);
id., at 164–165 (arguing Glossip was going to be fred because
of the condition of the rooms). It then argued that Sneed,
“satisfed and contented with [his] humble life,” id., at 68,
had no propensity to violence except at Glossip's direction:
      “[I]t's as if Justin Sneed was a Rottweiler puppy, let's
      say 11 months old, and Richard Glossip was the dog
      trainer. You can sure sick a dog on somebody, but if
      you're going to do that and you send a dog that's not
      trained or is a little bit too young, he might trip and fall,
      he might get scared and run away, he might do some-
      thing stupid, he might not do a good job. But no matter
      how you slice it, no matter how you parse it, the person
Page Proof Pending Publication
      that says `sick `em' is the person that makes the deci-
      sion.” Id., at 73.
   The jury again convicted Glossip of capital murder and
again sentenced him to death.
   A closely divided OCCA affrmed, holding that circumstan-
tial evidence suggesting Glossip had mismanaged the hotel,
combined with the concession that Glossip had been dishon-
est in his initial statements after the murder, suffciently cor-
roborated Sneed's testimony that he killed Van Treese at
Glossip's direction. Glossip II, 157 P. 3d, at 151–153. In
dissent, Judge Chapel and Judge A. Johnson argued that the
majority “overstate[d] the strength of the accomplice corrob-
oration evidence.” Id., at 164–165, 175.
                              B
  Glossip continued to maintain his innocence in the years
after his conviction, fling several habeas petitions in state
and federal court. Although that litigation did not result
in relief, mounting concerns over the integrity of Glossip's
                   Cite as: 604 U. S. 226 (2025)             237

                      Opinion of the Court

conviction drew the attention of the Oklahoma Legislature.
A bipartisan group of 62 Oklahoma legislators retained a law
frm, Reed Smith, to conduct an independent investigation
into the case. Pet. for Cert. 12; App. to Pet. for Cert. 390a–
391a. In June 2022, Reed Smith reported its “grave doubt
as to the integrity of Glossip's murder conviction and death
sentence.” Independent Investigation of State v. Richard E.
Glossip 6 (June 7, 2022). Among other things, Reed Smith
concluded the prosecution had deliberately destroyed “key
physical evidence” before Glossip's retrial, including several
items from the crime scene and the inn's receipts and deposit
books, which could have helped Glossip address the accusa-
tions of embezzlement. Id., at 7, 9, n. 25, 34, 48. Reed
Smith further concluded that the State had “falsely por-
trayed Sneed at trial as a meek and non-violent `puppet,' ”
id., at 10, and that key testimony about Glossip's motive and
actions on the morning after the murder had been provided
Page Proof Pending Publication
by a former police offcer of “ `very limited honesty and in-
tegrity' ” who was jailed for making false statements shortly
after Glossip's second trial, id., at 6–12.
   Two months after Reed Smith's report, the State disclosed
seven boxes of previously withheld documents from Glossip's
trials. Those boxes contained a note the head prosecutor,
Connie Smothermon, sent to Sneed's lawyer before Sneed
testifed at the second trial. Smothermon's note concerned
“a few items that have been testifed to that I needed to
discuss with Justin,” including the “biggest problem,” which
(the note said) was “still the knife.” 3 App. 953. The exam-
iners' testimony about the knife was problematic, Smother-
mon's note explained, because “Justin [told] the police that
the knife fell out of his pocket and that he didn't stab the
victim with it,” yet the victim had “ `lacerations' ” consistent
with the “knife blade.” Ibid. It did not “make much sense”
to Smothermon, moreover, “that Justin could have control of
the bat and a knife” on his own. Ibid. “[W]e should get to
him this afternoon,” the note concluded. Ibid.
238                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

   The boxes further contained letters from Sneed to his at-
torney suggesting he had expressed a desire to recant his
testimony prior to Glossip's second trial. See id., at 811–
816. For example, in a letter dated May 15, 2003, Sneed
wrote to his attorney asking “ `do I have the choice of recant-
ing my testimony at any time during my life,' ” and is “ `there
. . . anything you know, on [Glossip's] court date and about
re-canting.' ” Id., at 815 (emphasis deleted); App. to Pet. for
Cert. in Glossip v. Oklahoma, No. 22–6500, at 192a.2
   Based on this new evidence and the evidence revealed by
Reed Smith, Glossip fled another motion for post-conviction
relief with the OCCA. Among other things, Glossip argued
that, during his second trial, Smothermon had interfered
with Sneed's testimony about the knife in violation of the
rule of sequestration, which prohibits witnesses from hear-
ing each other's testimony. 3 App. 785–882. Oklahoma re-
sponded that Glossip's claims were meritless, but that it
Page Proof Pending Publication
would nonetheless waive any procedural defenses in order to
mitigate the damage from a “media campaign” on Glossip's
behalf. Id., at 717–718. Oklahoma further asked the OCCA
to deny Glossip's claims on their merits so as “to trigger the
state court deference anticipated in [the Antiterrorism and
Effective Death Penalty Act]” in any future federal review.
Id., at 718, n. 7. Noting that it alone would “determine
whether the rules of this Court should be abandoned,” the
OCCA held that Glossip's claims were procedurally barred
as well as meritless. Id., at 775–783.

   2
     The dissent claims Sneed thought the phrase “ `recan[t] my testimony' ”
meant “ `refuse to testify,' ” post, at 272, n. 2, meaning (on the dissent's
view) Sneed asked his lawyer: “If I [testify] again, do I have the choice of
[refusing to testify] at any time during my life?” The dissent further
points to an interview Sneed gave decades later, where (with Glossip's
execution imminent) he denied ever “ `want[ing] to change the truth.' ”
Post, at 271, n. 2. Of course, Sneed's much later denials do not erase his
prior statements about recanting.
                        Cite as: 604 U. S. 226 (2025)                      239

                            Opinion of the Court

   Shortly thereafter, the State “unearthed disturbing reve-
lations about the contents of ” an eighth box of trial docu-
ments “consisting of material it previously prevented the de-
fense from obtaining.” Brief for Respondent 10. “Buried
inside Box 8,” the State says, “was a page of notes handwrit-
ten by Smothermon during a pretrial interview with Sneed,”
indicating “that Sneed had told Smothermon that he was `on
lithium' not by mistake, but in connection with a `Dr. Trum-
pet.' ” Ibid. Oklahoma's attorney general “deduced the
import of these notes in short order”: Only a single psychia-
trist worked in the Oklahoma County jail when Sneed was
held there, and his name was Dr. Larry Trombka. Ibid.;
see also 3 App. 930. A summary of Sneed's medical records
(previously withheld from Glossip's counsel after motion
practice seeking their discovery) showed that Sneed had re-
ceived lithium to treat his undisclosed bipolar disorder.
Brief for Respondent 10; 3 App. 1005. After this discovery,
Page Proof Pending Publication
Dr. Trombka signed an affdavit attesting that he was the
only medical professional at the jail who would have pre-
scribed Sneed lithium. Id., at 1003.
   The attorney general accordingly determined that Sneed
“was not in fact mis-prescribed lithium, but rather diagnosed
with bipolar disorder and treated with lithium under the care
of a psychiatrist”—and “despite her knowledge of these
facts,” Smothermon “elicited false testimony from Sneed” on
that subject. Brief for Respondent 11.3

  3
    Also included in Box 8 were prosecutors' witness interview notes sug-
gesting the State may have omitted certain details from the summaries it
turned over to the defense. For example, one witness apparently told the
prosecution that Glossip had sold him a big screen TV and a couch for
$900, 3 App. 952—a sum that would account for much of the cash Glossip
had on his person at his arrest. That same witness testifed at trial that
he did not know how much money Glossip had received for those sales. 1
id., at 286. Glossip's girlfriend later explained in a post-trial affdavit that
Glossip had been selling their possessions to pay for an attorney. 2 id.,
at 706.
240                    GLOSSIP v. OKLAHOMA

                          Opinion of the Court

  The attorney general thereafter disclosed Box 8 to Glossip
and retained an independent counsel to conduct another re-
view of Glossip's conviction. As relevant here, the inde-
pendent counsel concluded that Smothermon's attempt to in-
terfere with Sneed's testimony about the knife violated the
rule of sequestration, that her failure to turn over Sneed's
statements about his mental health treatment violated
Brady v. Maryland, 373 U. S. 83 (1963), and that her failure
to correct Sneed's false trial testimony that he had been
given lithium after asking for cold medicine violated Napue,
360 U. S. 264. App. to Pet. for Cert. 50a, 58a. His report
concluded:
      “[T]he State must vacate Glossip's conviction due to its
      decades-long failure to disclose what I believe is Brady
      material, correct what I believe was false trial testi-
      mony of its star witness, and what I believe was a viola-
      tion of the Court ordered Rule of Sequestration of wit-
Page Proof Pending Publication
      nesses. . . . In my view, this case is also permeated by
      failures to secure, safeguard and maintain evidence in a
      capital murder case.” Id., at 62a.
   Following the Box 8 disclosure and the independent coun-
sel's recommendation, Glossip fled a successive petition for
post-conviction relief with the OCCA asserting Brady,
Napue, cumulative error, and actual innocence claims.4 The
attorney general fled a “Response in Support of Petitioner's
Successive Application for Post-Conviction Relief.” 3 App.
973. Although the attorney general did not endorse Gloss-
ip's actual innocence claim, he represented that his offce had
“concluded that Justin Sneed . . . made material misstate-
ments to the jury regarding his psychiatric treatment and

  4
    The dissent faults Glossip for “ignor[ing] the lithium issue on direct
appeal” years earlier. Post, at 269. Glossip had no reason to know at
the time of his direct appeal that Smothermon knowingly failed to correct
Sneed's false testimony about why he had been given lithium, however, so
he would have had no occasion to raise his Napue or Brady claims then.
                   Cite as: 604 U. S. 226 (2025)           241

                      Opinion of the Court

the reasons for his lithium prescription,” which the State
had failed to correct in violation of Napue. 3 App. 974. In
addition, the State indicated it was “concerned that there
were multiple and cumulative errors, such as violation of the
rule of sequestration and destruction of evidence, that when
taken together with Sneed's misstatements warrant” a new
trial. Ibid.; see also id., at 977 (“[T]he State believes
Glossip is entitled to post-conviction relief ”); id., at 978
(State is “compelled, consistent with Napue,” to correct mis-
statements); id., at 979 (“[T]he State requests that the Court
vacate Glossip's conviction and that the case be remanded to
the district court”). Because Oklahoma agreed with Glossip
on the pertinent facts, it did not request an evidentiary
hearing.
   The OCCA denied Glossip's unopposed petition without a
hearing. It acknowledged the attorney general's request
that Glossip's conviction be vacated, noting that this conces-
sion alone could not “directly” provide a ground for relief.
Page Proof Pending Publication
529 P. 3d, at 223. The court said the following about the
State's confession of Napue error:
    “Glossip claims that the State failed to disclose evidence
    of Justin Sneed's mental health treatment and that
    Sneed lied about his mental health treatment to the jury.
    Though the State in its response now concedes that this
    alleged false testimony combined with other unspecifed
    cumulative errors warrant postconviction relief, the con-
    cession alone cannot overcome the limitations on succes-
    sive post-conviction review. See 22 O.S. Supp. 2022,
    § 1089(D)(8). The State's concession is not based in law
    or fact.” 529 P. 3d, at 226 (footnote omitted).

The OCCA then applied Oklahoma's Post-Conviction Proce-
dures Act (PCPA) to hold that Glossip's claims were proce-
durally barred. It concluded separately that the evidence
presented by the parties did not “create a Napue error.”
Ibid. (footnote omitted).
242                   GLOSSIP v. OKLAHOMA

                         Opinion of the Court

   This Court thereafter stayed Glossip's execution at the
joint request of the parties and granted certiorari to consider
Glossip's Brady and Napue claims and the effect of the attor-
ney general's confession of error.5 601 U. S. 999 (2024).
The Court also requested argument on an additional ques-
tion: whether the OCCA's holding that the PCPA precluded
post-conviction relief is an adequate and independent state-
law ground for the judgment.
   Because Oklahoma agrees with Glossip on the merits of
his appeal, the Court appointed Christopher Michel as ami-
cus curiae to defend the judgment below. 601 U. S. 1010
(2024). He has ably discharged his responsibilities.

                                  II
                                  A
   We begin with this Court's jurisdiction to review the
Page Proof Pending Publication
OCCA's judgment. “ `This Court will not take up a question
of federal law presented in a case “if the decision of [the
state] court rests on a state law ground that is independent
of the federal question and adequate to support the judg-
ment.” ' ” Cruz v. Arizona, 598 U. S. 17, 25 (2023) (quoting
Lee v. Kemna, 534 U. S. 362, 375 (2002)). “In the context of
direct review of a state court judgment, the independent and
adequate state ground doctrine is jurisdictional.” Coleman
v. Thompson, 501 U. S. 722, 729 (1991). A state ground of
decision is independent only when it does not depend on a
federal holding, Foster v. Chatman, 578 U. S. 488, 498 (2016),
and also is not intertwined with questions of federal law,
Michigan v. Long, 463 U. S. 1032, 1040–1041 (1983).
“[W]hen the adequacy and independence of any possible
state law ground is not clear from the face of the opinion, we
will accept as the most reasonable explanation that the state

  5
   Because the Court grants relief under Napue, the Court need not reach
the merits of Glossip's Brady claim.
                   Cite as: 604 U. S. 226 (2025)            243

                      Opinion of the Court

court decided the case the way it did because it believed that
federal law required it to do so.” Ibid.
   Amicus argues this Court lacks jurisdiction because the
OCCA held that Glossip's claims were barred under the
PCPA, and the PCPA is “a paradigmatic independent and
adequate state-law ground.” Brief for Court-Appointed
Amicus Curiae 13. That argument fails because it over-
looks an antecedent holding that turned on federal law. The
OCCA frst rejected the attorney general's confession of
Napue error, deeming it meritless and therefore incapable of
“overcom[ing]” application of the PCPA. 529 P. 3d, at 226.
Only then did it apply the PCPA to Glossip. Because the
OCCA's decision to reject the attorney general's confession
of error rested exclusively on federal law, so too did its sub-
sequent decision to apply the PCPA.
   In his brief to the OCCA, the attorney general disclaimed
reliance on any procedural defenses, including the PCPA.
Page Proof Pending Publication
Instead, the attorney general “concede[d] error under
Napue,” 3 App. 978, acknowledging that, as a matter of fed-
eral law, the prosecution's knowing failure to correct Sneed's
“material misstatements” entitled Glossip to a new trial.
Id., at 977, 978, 979. The OCCA held that this confession of
Napue error could not “overcome the [PCPA's] limitations on
successive post-conviction review” because it was “not based
in law or fact.” 529 P. 3d, at 226. Specifcally, the OCCA
concluded that the underlying evidence “d[id] not create a
Napue error.” Ibid. (footnote omitted). Thus, the OCCA's
application of the PCPA over the attorney general's confes-
sion of error depended on its determination that no Napue
violation had occurred. That was a federal holding, and it
was the only reason the OCCA provided for its conclusion
that the attorney general's confession could not “overcome”
the PCPA. 529 P. 3d, at 226. The PCPA therefore poses
no impediment to our review in this case.
   Oklahoma precedent involving confessions of error by an
attorney general confrms this reading. As the OCCA has
244                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

repeatedly explained, it will normally reject an attorney
general's confession of error only after fnding that it lacks a
basis in the law and in the record. See, e. g., Bindrum v.
State, 27 Okla. Crim. 372, 228 P. 168 (1924) (“Where the At-
torney General confesses error, th[e] court will examine the
record, and, if the confession is sustained thereby, and is well
founded in law, the conviction will be reversed” (syllabus by
the court)).6 Otherwise, if the confession of error is sup-
ported by the law and the record, the OCCA will reverse
the underlying conviction and remand for a new trial.7 Ibid.
The OCCA applied that same rule here: It rejected the attor-
ney general's confession of error as having no basis “in law
or fact,” and explained that it would therefore apply the
PCPA. 529 P. 3d, at 226.
  In doing so, the OCCA “made application of the procedural
bar depend on an antecedent ruling on federal law, that is,
on the determination of whether federal constitutional error
ha[d] been committed.” Ake v. Oklahoma, 470 U. S. 68, 75
Page Proof Pending Publication
(1985). After all, it made application of the PCPA contin-

   6
     See also Raymer v. State, 27 Okla. Crim. 398, 228 P. 500 (1924) (“Where
the Attorney General confesses error, th[e] court will examine the record,
and, if the confession is sustained thereby and is well founded in law, the
conviction will be reversed” (syllabus by the court)); Dorsett v. State, 16
Okla. Crim. 65, 69, 180 P. 557, 558 (1919) (reversing conviction because
“the confession of error [of the attorney general] is well founded” in law);
Whittemore v. State, 26 Okla. Crim. 338, 223 P. 890 (1924) (per curiam)
(same); Day v. State, 352 P. 2d 935 (OCCA 1960) (“Where the Attorney
General confesses error, Court of Criminal Appeals will examine the rec-
ord, and, if confession is sustained thereby, and is well founded in law,
conviction will be reversed” (syllabus by the court)); Casey v. State, 440
P. 2d 208, 209 (OCCA 1968) (“When the Attorney General confesses error,
this Court will carefully examine the record for fundamental error”); Mc-
Connell v. State, 485 P. 2d 764, 765 (OCCA 1971) (similar); One Ford Tour-
ing Car v. State, 100 Okla. 267, 268, 229 P. 231, 232 (1924) (establishing
identical rule in civil forfeiture context).
   7
     The PCPA would not stand in the way of a reversal under this rule
because it is not a jurisdictional bar. See Valdez v. State, 2002 OK CR
20, ¶¶24–28, 46 P. 3d 703, 710.
                    Cite as: 604 U. S. 226 (2025)             245

                       Opinion of the Court

gent on its determination that the attorney general's confes-
sion of federal constitutional error had no basis in law or
fact. To the extent that the OCCA's reasoning on this point
is insuffciently “clear from the face of the opinion,” we none-
theless presume reliance on federal law under Michigan v.
Long, 463 U. S., at 1040–1041. This Court therefore has ju-
risdiction to review the judgment below.

                                 B
   The dissent dismisses all this as an “invent[ed] . . . federal
holding that the OCCA never made.” Post, at 279. As the
dissent sees it, the OCCA rejected the attorney general's
confession of error because (the dissent says) the State failed
adequately to address all of the PCPA's procedural require-
ments. See post, at 280. The OCCA plainly held that the
attorney general's confession was “not based in law or fact,”
529 P. 3d, at 226, however, forcing the dissent to provide
Page Proof Pending Publication
an awkward explanation that this holding about a federal
confession of error on the merits was only about the PCPA's
state-law, procedural requirements. Post, at 280. Yet the
State expressly attempted to waive those procedural re-
quirements by arguing that Glossip was entitled to a new
trial. 3 App. 979 (“[T]he State requests that the Court va-
cate Glossip's conviction and that the case be remanded to
the district court”). So to explain away the “based in law
or fact” language, the dissent must proceed on the assump-
tion that Oklahoma law requires applicants to satisfy the
PCPA's nonjurisdictional provisions even when the State
waives them and even if the State's confession of constitu-
tional error is otherwise meritorious—notwithstanding the
many other contexts where the OCCA privileges meritorious
confessions of error. See n. 6, supra (collecting cases); App.
to Brief for National Association of Criminal Defense Law-
yers as Amicus Curiae 1a–21a (cataloging the OCCA's deci-
sions in the 298 confession-of-error cases predating Glossip's,
all of which resulted in relief).
246                 GLOSSIP v. OKLAHOMA

                      Opinion of the Court

  That assumption is hardly “clear from the face of the opin-
ion” below. Long, 463 U. S., at 1041. Thus, we must “ac-
cept as the most reasonable explanation that the state court
decided the case the way it did because it believed that fed-
eral law required it to do so.” Ibid.

                              III
                              A
   Turning to the merits, we conclude that the prosecution
violated its constitutional obligation to correct false
testimony.
   In Napue v. Illinois, this Court held that a conviction
knowingly “obtained through use of false evidence” violates
the Fourteenth Amendment's Due Process Clause. 360
U. S., at 269. To establish a Napue violation, a defendant
must show that the prosecution knowingly solicited false tes-
timony or knowingly allowed it “to go uncorrected when it
Page Proof Pending Publication
appear[ed].” Ibid. If the defendant makes that showing, a
new trial is warranted so long as the false testimony “may
have had an effect on the outcome of the trial,” id., at 272—
that is, if it “ `in any reasonable likelihood [could] have af-
fected the judgment of the jury,' ” Giglio v. United States,
405 U. S. 150, 154 (1972) (quoting Napue, 360 U. S., at 271).
In effect, this materiality standard requires “ ` “the benef-
ciary of [the] constitutional error to prove beyond a reason-
able doubt that the error complained of did not contribute to
the verdict obtained.” ' ” United States v. Bagley, 473 U. S.
667, 680, n. 9 (1985) (quoting Chapman v. California, 386
U. S. 18, 24 (1967)).
   Here, Oklahoma's attorney general joins Glossip in assert-
ing a Napue error, conceding both that Sneed's testimony
was false and that the prosecution knowingly failed to cor-
rect it. The record supports that confession of error. A
summary of Sneed's medical records created by the local
sheriff 's department establishes that someone diagnosed
Sneed with bipolar disorder and prescribed him lithium. 3
                    Cite as: 604 U. S. 226 (2025)             247

                       Opinion of the Court

App. 1005. Dr. Trombka, a psychiatrist, attested in a sworn
affdavit that he was the only medical professional at the
Oklahoma County jail who would have issued Sneed that pre-
scription. Id., at 930–931. Dr. Trombka also confrmed,
and nobody contests, that lithium is used only in psychiatric
treatments and not for dental pain (as Sneed said at a pre-
trial hearing) or a cold (as Sneed testifed at Glossip's trial).
Ibid. Nor would anyone confuse lithium with Sudafed,
which is a cold medication. Ibid. Sneed's trial testimony
that he had been given lithium after asking for Sudafed and
had “never seen no psychiatrist or anything” was therefore
false.
   The evidence likewise establishes that the prosecution
knew Sneed's statements were false as he testifed to them.
The prosecution almost certainly had access to Sneed's medi-
cal fle, which would have listed both the lithium prescription
and the bipolar diagnosis. Among other things, those rec-
Page Proof Pending Publication
ords would have been provided to the State as part of
Sneed's competency evaluation, id., at 931, and the State op-
posed Glossip's discovery request of Sneed's medical fles on
its merits, 2 id., at 622–623; 3 id., at 933. As amicus and
the dissent emphasize, moreover, “[l]ithium is prescribed
only for mood disorders.” Brief for Court-Appointed Ami-
cus Curiae 14; post, at 268 (“It is undisputed that lithium's
sole medical purpose, both in 1997 and today, is to treat bipo-
lar disorder and other mental health disorders”). Yet the
prosecution knew that Sneed had previously told a compe-
tency evaluator that he had been prescribed lithium “after
his tooth was pulled,” 2 App. 700; that statement was part
of a competency record to which both the State and Glossip
had access, id., at 698–703. Prosecutors then heard Sneed
testify to a different version of events at trial: that the lith-
ium had been given to him after he asked for Sudafed be-
cause he had a cold. 1 id., at 312.
   In addition, Smothermon's notes show that she had a pre-
trial conversation with Sneed at which he mentioned “lith-
248                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

ium” and “Dr. Trumpet.” 3 id., at 927. Glossip argues, and
the attorney general admits, that this shows Sneed told
Smothermon that Dr. Trumpet (meaning Dr. Trombka) had
prescribed him lithium. As just discussed, the record shows
that, in fact, Dr. Trombka did diagnose Sneed with bipolar
disorder and prescribe him lithium. Sneed plainly discussed
these matters with the prosecution. In that private conver-
sation, he would have had little to gain from prevaricating
about his prescriptions, nor do the notes suggest he did any-
thing of the kind. The straightforward inference is that
Sneed told Smothermon that Dr. Trombka had prescribed
him the lithium.8
   That leaves materiality. Evidence can be material even if
it “goes only to the credibility of the witness,” Napue, 360
U. S., at 269; indeed, “[t]he jury's estimate of the truthfulness
and reliability of a given witness may well be determinative
of guilt or innocence,” ibid. Because Sneed's testimony was
the only direct evidence of Glossip's guilt of capital murder,
Page Proof Pending Publication
the jury's assessment of Sneed's credibility was necessarily
determinative here. Besides Sneed, no other witness and
no physical evidence established that Glossip orchestrated
Van Treese's murder. Thus, the jury could convict Glossip
only if it believed Sneed.
   Had the prosecution corrected Sneed on the stand, his
credibility plainly would have suffered. That correction
would have revealed to the jury not just that Sneed was
untrustworthy (as amicus points out, the jury already knew
he repeatedly lied to the police), but also that Sneed was
  8
    The dissent claims Sneed instead repeated his prior false statement
that he had been given the lithium after having his tooth pulled. See
post, at 273, 274, n. 3, 286, n. 6, 302–303. Yet the dissent's only source for
this theory, Smothermon's co-counsel Gary Ackley, acknowledged under
oath that he knew lithium was not a pain medication, 3 App. 940, meaning
he would have known this story, too, to be wrong. In any event, even if
the prosecution did believe Sneed had been given lithium for a toothache,
that still would have put them on notice that Sneed's testimony at trial
(about receiving lithium after asking for cold medication) was false.
                   Cite as: 604 U. S. 226 (2025)            249

                      Opinion of the Court

willing to lie to them under oath. Such a revelation would
be signifcant in any case, and was especially so here where
Sneed was already “nobody's idea of a strong witness.”
Brief for Court-Appointed Amicus Curiae 37. Even if
Sneed's bipolar disorder were wholly irrelevant, as amicus
argues, his willingness to lie about it to the jury was not.
“ `A lie is a lie, no matter what its subject.' ” Napue, 360
U. S., at 269–270 (quoting People v. Savvides, 1 N. Y. 2d 554,
557, 136 N. E. 2d 853, 854–855 (1956)).
   Sneed's false testimony also bore on Glossip's guilt in a
more direct way. As Smothermon's co-counsel Gary Ackley
has conceded, it “would have been an important fact for the
defense to know” that Sneed had been prescribed lithium to
treat bipolar disorder. 3 App. 940. After the Box 8 disclo-
sures, Dr. Trombka explained to Glossip's counsel that bipo-
lar disorder symptoms “can be exacerbated by illicit drug
use, such as methamphetamine,” to “cause an individual to be
Page Proof Pending Publication
more paranoid or potentially violent.” Id., at 932. Sneed
admitted at trial that he regularly used drugs, including
methamphetamine. His diagnosis with a disorder that could
trigger impulsive violence when combined with drug use
thus would have undermined the prosecution's theory that
Sneed was harmless on his own—a Rottweiler puppy be-
holden to his trainer. 15 Tr. 73 (June 1, 2004). That theory
was an important part of the prosecution's case and featured
prominently in its opening and closing statements. See, e.g.,
3 Tr. 209 (May 13, 2004) (arguing in opening that Sneed was
“pretty content . . . to do whatever it is that Richard Glossip
wanted him to do”); 15 Tr. 69–74 (June 1, 2004) (emphasizing
in closing that Sneed would have never committed murder
without Glossip). Hence there is a reasonable likelihood
that correcting Sneed's testimony would have affected the
judgment of the jury. Napue, 360 U. S., at 271.
   Amicus objects that “the jury already knew that Sneed
had been prescribed lithium, used illegal drugs, and behaved
impulsively; he admitted that he beat a man to death with a
250                 GLOSSIP v. OKLAHOMA

                      Opinion of the Court

baseball bat in the middle of the night with no advanced
planning.” Brief for Court-Appointed Amicus Curiae 36.
As amicus sees it, the additional evidence provided by
Sneed's lie and his treatment for bipolar disorder could
hardly have made a difference in light of so much other im-
peaching evidence. Id., at 36–37. Of course, at trial, the
prosecution urged the jury to believe just the opposite: that
despite his prior dishonesty and violence, Sneed was now
telling the truth. See, e. g., 15 Tr. 153–155 (June 1, 2004).
A prosecutor's midtrial revelation that Sneed lied on the
stand would have signifcantly undercut that argument.
   In any event, amicus's position is self-defeating. If the
evidence impeaching Sneed's credibility was already over-
whelming, then no reasonable jury could have convicted
Glossip in the frst place, given that the prosecution's case
rested centrally on Sneed's credibility. Amicus appears to
assume the jury would have believed Sneed no matter what.
Page Proof Pending Publication
Such an assumption has no place in a materiality analysis,
which asks what a reasonable decisionmaker would have
done with the new evidence. See Wearry v. Cain, 577 U. S.
385, 393–394 (2016) (per curiam) (rejecting argument that
evidence was immaterial because witness's credibility was
“already impugned”); cf. Strickland v. Washington, 466 U. S.
668, 695 (1984).
   Although the prosecution's failure to correct Sneed's false
testimony was a material Napue violation on its own, addi-
tional conduct by the prosecution further undermines conf-
dence in the verdict. The attorney general has confessed
to “ `violation of the rule of sequestration' ” with respect to
Smothermon's apparent midtrial attempt to speak with
Sneed about the knife, as well as to “ `destruction of evi-
dence,' ” including the hotel's fnancial records and items
Glossip and Sneed allegedly handled in Van Treese's room.
See Brief for Respondent 13; 3 App. 935 (prosecutor Ackley
attesting under oath that “I was informed that a box of evi-
dence containing 10 items was destroyed by the Oklahoma
                       Cite as: 604 U. S. 226 (2025)                    251

                           Opinion of the Court

City Police Department. . . . It is likely that I was aware of
that fact during the 2004 retrial . . . . That this happened
horrifes me”); Independent Investigation of State v. Richard
E. Glossip, at 7, 12–13, 41–43 (cataloging destroyed items).
In addition, the eight boxes of documents released to Glossip
included statements from Sneed evincing a desire to recant
his testimony and witness notes with details not previously
turned over to the defense. For example, the fles suggest
one witness told the prosecution (contrary to his trial testi-
mony) that Glossip sold him a couch and a TV for $900. 3
App. 952. That evidence would have supported Glossip's ac-
count of the cash he carried at his arrest outside an attor-
ney's offce: that he had sold his possessions to pay for an
attorney. See 2 id., at 706. Because prejudice analysis re-
quires a “cumulative evaluation” of all the evidence, whether
or not that evidence is before the Court in the form of an
independent claim for relief, these documents reinforce our
conclusion that the Napue error here prejudiced the defense.
Page Proof Pending Publication
Kyles v. Whitley, 514 U. S. 419, 441 (1995).9

  9
    The dissent's attempts to minimize these issues are unpersuasive.
Sneed's letter inquiring about “ `the choice of recanting my testimony,' ” 3
App. 815, disproves the dissent's assertion that “there is no evidence that
Sneed wished to `recant' his testimony.” Post, at 293. That Glossip re-
called receiving only $490 for his possessions during his frst trial does
not absolve the prosecution from its ordinary duty to disclose inconsistent
statements by its witnesses. Contra, ibid. The State's conceded seques-
tration violation also is not merely an insignifcant state-law issue, post,
at 292; like any other attorney, a prosecutor may not seek to infuence the
content of a witness's testimony. See, e. g., Geders v. United States, 425
U. S. 80, 90, n. 3 (1976) (“An attorney must respect the important ethical
distinction between discussing testimony and seeking improperly to in-
fuence it”). The dissent labors to discredit certain “handwritten notes”
on which neither Glossip nor this Court relies, see post, at 293, n. 8, but
Smothermon undisputedly wrote to Sneed's counsel that she needed to
“get to” him “to discuss” his problematic testimony about the knife. 3
App. 953. The next day, Sneed's testimony corrected the very problem
raised by Smothermon's letter. Smothermon nonetheless disclaimed any
knowledge of Sneed's change in testimony when Glossip objected. 12 Tr.
252                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

  For these reasons, we conclude that the prosecution's fail-
ure to correct Sneed's trial testimony violated the Due Proc-
ess Clause. Glossip is entitled to a new trial.

                                    B
   The OCCA's contrary holding rested on a mistaken inter-
pretation of Napue. According to the OCCA, there was no
violation because the defense “was aware or should have
been aware that Sneed was taking lithium at the time of
trial,” and the prosecution could not have “knowingly con-
cealed” something the defense already knew. 529 P. 3d, at
226. As an initial matter, Sneed's false testimony concerned
the reasons for his lithium prescription, not the mere fact
that he had taken it. Glossip's counsel was aware of the
latter, not of the former. In any event, the Due Process
Clause imposes “ `the responsibility and duty to correct' ”
false testimony on “representatives of the State,” not on de-
fense counsel. Napue, 360 U. S., at 269–270 (quoting Sav-
Page Proof Pending Publication
vides, 1 N. Y. 2d, at 557, 136 N. E., at 854).
   The OCCA also held that Sneed's testimony was not
“clearly false” because Sneed was “more than likely in denial
of his mental health disorders.” 529 P. 3d, at 226, 227. It
is not apparent why the OCCA thought Sneed was in denial,
nor why such denial should have caused Sneed to believe
that he had never seen a psychiatrist, when in fact he had.
Even supposing it did, however, Sneed's beliefs are beside
the point. What matters is that his testimony was false and
a prosecutor knowingly let it stand nonetheless. Napue, 360
U. S., at 269 (“[I]t is established that a conviction obtained
through use of false evidence, known to be such by repre-
sentatives of the State, must fall under the Fourteenth
Amendment”).

107–108 (May 26, 2004). Finally, not even the original prosecutors dispute
that the police destroyed key evidence before Glossip's retrial; the dissent
nonetheless dismisses that claim, undisputed for over two decades, as this
Court's “own creation.” Post, at 292–293.
                       Cite as: 604 U. S. 226 (2025)                     253

                           Opinion of the Court

   The dissent's arguments in support of the OCCA's conclu-
sions fare no better. As an initial matter, even the dissent
does not dispute that Sneed falsely testifed he had never
seen a psychiatrist. See post, at 290 (suggesting Sneed
“misremembered” that a psychiatrist prescribed him lithium
to treat bipolar disorder). The dissent does maintain that
other aspects of Sneed's statement were true, noting that
because Sneed was in denial about his diagnosis, his “state-
ment about his own knowledge was not false.” Post, at 291.
Sneed's statement that he asked for “Sudafed” to treat “a
cold” and was given lithium instead, 12 Tr. 64 (May 26, 2004),
was not, however, a statement “about his own knowledge.”
Even if Sneed himself did not believe that he suffered from
bipolar disorder, moreover, that would not render true his
assertion that he had no idea why his doctor thought he
needed lithium.
   The dissent next claims that the false testimony must itself
have directly affected the trial's outcome to be material
Page Proof Pending Publication
under Napue. Post, at 288 (“[T]he relevant inquiry under
Napue is whether the content of the false testimony at issue
is material”). As Napue made clear, however, “ `[a] lie is a
lie, no matter what its subject.' ” 360 U. S., at 269–270
(quoting Savvides, 1 N. Y. 2d, at 557, 136 N. E. 2d, at 854–
855). Nothing in Napue requires ignoring the fact of
Sneed's perjury in the prejudice analysis. To the contrary,
materiality instead always requires courts to assess whether
“the error complained of ” could have contributed to the ver-
dict. Chapman, 386 U. S., at 24; Bagley, 473 U. S., at 680,
n. 9. Here, the prosecutor's failure to correct Sneed's false
testimony is the relevant error, so the Court asks whether a
correction could have made a material difference. The an-
swer is clearly yes. See supra, at 247–252.10
  10
     The dissent also argues Sneed's lithium use was immaterial because
“the defense chose not to turn” it “into an impeachment issue,” post, at 288,
but each premise in that argument is mistaken. First, the defense did not
choose “not to raise Sneed's mental condition,” post, at 287; they asked him
254                    GLOSSIP v. OKLAHOMA

                          Opinion of the Court

   The remaining arguments offered in defense of the OCCA's
position are likewise unpersuasive. In an amicus brief, the
Van Treese family argues that it was Glossip's counsel who
asked Sneed about his lithium prescription, and that Smoth-
ermon's notes reveal only that Sneed relayed those questions
to Smothermon. See Brief for Victim Family Members as
Amici Curiae 7–22. That argument relies heavily on extra-
record materials not properly before the Court, including a
recent unsworn statement from Smothermon adopting the
family's interpretation of the notes. (The dissent, which
criticizes the independent counsel for “impugning” the trial
prosecutors' reputation, post, at 276, justifes its reliance on
these materials by accusing the Oklahoma attorney general
of “collusively exclud[ing]” them from the record, see post,
at 303.) Nor would accepting the family's account change
the Napue analysis. Whatever the impetus for the conver-
sation, the family agrees that Sneed and Smothermon dis-
Page Proof Pending Publication
cussed Dr. Trombka and lithium. The natural inference is
that Sneed explained to Smothermon the circumstances that
led to his lithium use. To avoid that inference, the family in
turn suggests both that Sneed was never diagnosed with bi-
polar disorder in the frst place, Brief for Victim Family
Members as Amici Curiae 17, and that Glossip's counsel
“knew about [Dr. Trombka] more than two decades ago,” id.,
at 21. Yet for the reasons previously explained, defense
counsel's purported knowledge of Dr. Trombka's existence is
irrelevant, and the prison medical record supports the attor-

about it in cross-examination and Sneed repeated his false testimony. See
13 Tr. 15 (May 27, 2004). Second, the defense did not know during trial
that Sneed had been diagnosed with bipolar disorder; to the contrary,
Glossip later sought (and the State successfully opposed) discovery on that
issue. 2 App. 621–622. Third, even if the defense had made a conscious
choice not to raise the (then-uncertain) reasons for Sneed's lithium use,
that would be irrelevant to the prosecution's duty to correct false testi-
mony “when it appears.” Napue, 360 U. S., at 269.
                   Cite as: 604 U. S. 226 (2025)           255

                      Opinion of the Court

ney general's concession that Sneed received a lithium pre-
scription as treatment for his bipolar disorder.
   The family also maintains (and the dissent agrees) that
Reed Smith and the independent counsel spent insuffcient
time interviewing Smothermon. Neither the family nor
Smothermon raised that objection before the OCCA, nor
does anyone now explain its relevance to the Napue analy-
sis. The argument is also unpersuasive on its own terms.
Both investigators spoke to Smothermon. When they did,
Smothermon did not provide the account she now endorses:
that Sneed relayed to her a conversation with Glossip's coun-
sel about Dr. Trombka and lithium. Instead, during a third
interview, Smothermon asked the independent counsel “why
he thought it was Dr Trombka and not Dr Trumpet the jazz
musician and I was making a personal note or something
else.” App. to Brief for Victim Family Members as Amici
Curiae 31a. There is no compelling evidence that a fourth
Page Proof Pending Publication
or ffth consultation with Smothermon would have yielded
materially different results.
   The Court-appointed amicus, for his part, largely aban-
dons the OCCA's reasoning and focuses instead on ambigu-
ities in Smothermon's notes. Amicus maintains that too
many inferential steps separate those notes from the conclu-
sion that Sneed lied on the stand and that Smothermon knew
it. For example, amicus argues that “the parties do not ex-
plain the basis for their asserted link between `Dr. Trumpet?'
and Trombka,” reiterating Smothermon's earlier statements
that she “ `is not convinced that Dr. Trombka and “Dr. Trum-
pet” are the same person.' ” Brief for Court-Appointed
Amicus Curiae 32. As already explained, however, there is
ample evidence in the record before this Court supporting
the inference that Smothermon knew about Sneed's psychiat-
ric treatment and lithium prescription, including the prison
medical record, Dr. Trombka's attestations, and Smother-
mon's own notes.
256                   GLOSSIP v. OKLAHOMA

                         Opinion of the Court

   Because ample evidence supports the attorney general's
confession of error in this Court, there also is no need to
remand for further evidentiary proceedings at the OCCA.
Indeed, that such proceedings are not necessary is the one
point on which Glossip, Oklahoma, amicus, and the OCCA
unanimously agree. See Tr. of Oral Arg. 108 (amicus con-
ceding that “I guess we all agree that [an evidentiary hear-
ing is] not . . . that it's not necessary”). The partial concur-
rence suggests this Court should nonetheless remand for
further proceedings on the ground that the evidence does not
remove all doubt that the attorney general's view of the rec-
ord is correct. Post, at 262 (Barrett, J., concurring in part
and dissenting in part). Yet for the reasons already ex-
plained, the record establishes a violation of Napue. See
supra, at 246–252. This Court has not required an eviden-
tiary record free of doubt to fnd a Napue violation in any
case, much less when an attorney general confesses that his
own offce erroneously obtained a capital conviction.11
Page Proof Pending Publication
                                   C
   Finally, the dissent maintains this Court lacks the author-
ity to remand for a new trial, but its analysis proves the
contrary. The dissent emphasizes that “ `[o]ur only power
over state judgments is to correct them to the extent that
they incorrectly adjudge federal rights.' ” Post, at 294 (quot-
ing Herb v. Pitcairn, 324 U. S. 117, 125–126 (1945)). It further
  11
    The dissent would order a hearing to provide “the Van Treese family
[with] the opportunity to present its case.” Post, at 303 (opinion of
Thomas, J.). The family has not requested an evidentiary hearing (or
participation in one) at any stage before the OCCA and does not request
that relief before this Court. Nor has the OCCA ever extended Oklaho-
ma victims' right to participate in criminal proceedings to state post-
conviction hearings. Cf. post, at 303–304. The request to do so here is
the dissent's alone. In any event, this Court does not “cast aside the
family's interests,” on procedural or any other grounds. Post, at 304.
For the reasons already explained, considering the evidence submitted by
the family would not change the outcome. See supra, at 255.
                   Cite as: 604 U. S. 226 (2025)           257

                      Opinion of the Court

agrees that, where a state court relies on a procedural rule
whose application turns on “whether federal constitutional
error has been committed,” Ake, 470 U. S., at 75, this Court
may remand for a new trial if it “ha[s] confdence that no
other state ground could support the decision below,” post,
at 300. Those principles describe this case.
   As explained above, the OCCA “incorrectly adjudge[d]”
Glossip's “federal rights.” Herb, 324 U. S., at 126. In doing
so, it relied on a procedural rule whose application turned on
the merits of a federal claim: “ `Where the Attorney General
confesses error, [the OCCA] will examine the record, and, if
the confession is sustained thereby, and is well founded in
law, the conviction will be reversed.' ” See supra, at 244
(quoting Bindrum, 27 Okla. Crim., at 372, 228 P., at 168, and
collecting authorities). Here, the attorney general “con-
cede[d] error under Napue,” 3 App. 978, and the OCCA re-
jected that confession because it wrongly concluded that no
Page Proof Pending Publication
such federal error had occurred. See supra, at 244. Be-
cause the Napue confession was “well founded in law,” it fol-
lows that “the conviction will be reversed.” Bindrum, 27
Okla. Crim., at 372, 228 P., at 168. Accordingly, all that re-
mains below is to vacate the conviction, and a new trial fol-
lows a fortiori.
   The dissent concludes otherwise because, in its view, a re-
mand for further consideration of alternative state grounds
is mandatory in every case where Michigan v. Long resolves
lingering doubt over the Court's jurisdiction. Post, at 295–
296. Long describes the circumstances under which this
Court has jurisdiction to review a state-court judgment; it
does not limit the Court's remedial authority over an estab-
lished federal constitutional violation. Nor does any other
precedent support the dissent's rule. That state courts who
“grant relief to criminal defendants” under an erroneous in-
terpretation of federal law may later grant relief “as a mat-
ter of [more protective] state law,” Kansas v. Carr, 577 U. S.
108, 128 (2016) (Sotomayor, J., dissenting), plainly does not
258                 GLOSSIP v. OKLAHOMA

                     Opinion of Barrett, J.

deprive this Court of the authority to grant relief where it
fnds a federal violation, contra, post, at 295–296; cf. Arizona
v. Evans, 514 U. S. 1, 8 (1995) (“Under [Michigan v. Long] state
courts are absolutely free to interpret state constitutional
provisions to accord greater protection to individual rights
than do similar provisions of the United States Constitution”).
   The dissent inverts this precedent, asserting that state
courts should always have another opportunity to identify
additional grounds for denying relief, even where this Court
has found a federal constitutional violation. Yet there is no
reason to allow state courts a second (or third, or fourth) bite
at the apple to identify alternative state grounds for their
decision in every case involving a dependent ground. The
facts as conceded by the attorney general and supported by
the record establish a violation of Napue. A new trial is the
remedy for a Napue violation. See Giglio, 405 U. S., at 155.
Here, this Court has jurisdiction and a Napue violation oc-
curred. Thus, Glossip is entitled to a new trial. See Ake,
Page Proof Pending Publication
470 U. S., at 86–87 (vacating conviction and remanding case
to the OCCA under similar circumstances).

                         *     *     *
   The judgment of the Oklahoma Court of Criminal Appeals
is reversed, and the case is remanded for further proceedings
not inconsistent with this opinion.
                                              It is so ordered.

   Justice Gorsuch took no part in the consideration or de-
cision of this case.
  Justice Barrett, concurring in part and dissenting in
part.
  While I agree with much of the Court's analysis, I would
not order the Oklahoma Court of Criminal Appeals (OCCA)
to set aside Richard Glossip's conviction. The OCCA did
not make factual fndings on the most important questions,
                    Cite as: 604 U. S. 226 (2025)             259

                      Opinion of Barrett, J.

and the record is open to multiple plausible interpreta-
tions. Consistent with our ordinary practice, the Court
should have corrected the OCCA's misstatement of Napue v.
Illinois and remanded this case for further proceedings.
360 U. S. 264 (1959). Instead, the Court has drawn its own
conclusions about what the record shows, thereby exceeding
its role.
   I begin with the common ground. At the threshold, I
agree with the Court's jurisdictional holding and therefore
join Part II of its opinion. We lack jurisdiction to review a
state court's adjudication of federal claims if the state court's
decision “rests on a state law ground that is independent of
the federal question and adequate to support the judgment.”
Coleman v. Thompson, 501 U. S. 722, 729 (1991). But when
a state-law ground of decision is intertwined with analysis
of a federal question, we will treat the decision as independ-
ent only if the state court “make[s] clear by a plain state-
Page Proof Pending Publication
ment” that its resolution of the state-law question does not
depend on its resolution of the federal question. Michigan
v. Long, 463 U. S. 1032, 1041 (1983). Though it is a closer
question for me than it is for the Court, I agree that the
OCCA's opinion does not clear this bar. True, the OCCA
rejected Glossip's application based on state-law procedural
limits on postconviction relief. But the opinion can be read
to say that the OCCA refused to accept the attorney gener-
al's waiver of this procedural bar because his confession of
error was not “based in law.” 2023 OK CR 5, ¶25, 529 P. 3d
218, 226. If that is what the OCCA meant, then its reliance
on state law depended on the merits of Glossip's federal
claims. After all, if the trial contained federal constitutional
error, then the attorney general's confession of error may
have been “based in law.” Because the opinion lacks a
“plain statement” clarifying that the OCCA's reliance on
state law was truly independent of its assessment of Gloss-
ip's federal claims, the Court rightly proceeds to the merits.
Michigan, 463 U. S., at 1041.
260                 GLOSSIP v. OKLAHOMA

                     Opinion of Barrett, J.

   I also share the Court's view that the OCCA misapplied
Napue. The OCCA appeared to think that Justin Sneed's
testimony “was not clearly false” because he “was more than
likely in denial of his mental health disorders.” 529 P. 3d,
at 227. But for purposes of Napue, the question is not
whether a witness subjectively thought he was lying—it is
whether the prosecution knowingly presented untrue testi-
mony. The OCCA also stated that Sneed's “known mental
health treatment evidence” would not have created a “rea-
sonable probability that the result of the proceeding would
have been different had Sneed's testimony regarding his use
of lithium been further developed at trial.” 529 P. 3d, at
227. Yet the OCCA ignored the critical fact that—had the
prosecutor, Connie Smothermon, corrected Sneed's testi-
mony—the jury would have learned that Sneed made a false
statement on the stand. Sneed's testimony was the primary
evidence that the State offered to prove that Glossip planned
Page Proof Pending Publication
the murder. Faced with a prosecutor forced to correct her
star witness, a juror might have disbelieved Sneed's testi-
mony in its entirety. And if a juror went from belief to dis-
belief in Sneed, she might have changed her ultimate assess-
ment of whether the State had proved Glossip's guilt beyond
a reasonable doubt. So if Sneed really did give false testi-
mony, and if Smothermon really did knowingly allow that
testimony to go uncorrected, then Smothermon violated
Glossip's due process rights under Napue. The OCCA's con-
trary statements were wrong as a matter of federal law.
   I part ways with the Court on what comes next. In exer-
cising our appellate function, it is not our role to fnd facts;
instead, we review the factual fndings of lower courts, sub-
ject to a deferential standard of appellate review. See Price
v. Johnston, 334 U. S. 266, 291 (1948). This practice makes
good sense. This Court is well equipped to answer ques-
tions of federal law; it is ill equipped either to determine the
credibility of witnesses or to master voluminous trial rec-
ords. Other actors in our judicial system—including, where
                      Cite as: 604 U. S. 226 (2025)                  261

                         Opinion of Barrett, J.

appropriate, state courts like the OCCA—better serve these
functions, as our standard of review refects. In this case,
however, the Court has chosen to function as the initial
factfnder.
   To establish a violation of Napue, Glossip must show that
(1) Sneed gave false testimony and (2) Smothermon knew
that the testimony was false. To make these showings,
Glossip relies largely on notes taken by Smothermon, an af-
fdavit from Dr. Trombka, and a “medical information sheet.”
According to the Court, these documents clearly demon-
strate that (1) Sneed lied when he said that he did not know
why he had been given lithium and that he had never seen a
psychiatrist and (2) Smothermon knew that both of these
statements were lies. See ante, at 246–248, 255. Thus, the
Court concludes, there is no need for the OCCA to make its
own factual fndings.*

Page         Proof Pending Publication
  *The Court suggests that this shortcut is appropriate because Glossip,
the attorney general, the Court-appointed amicus, and the OCCA “unani-
mously agree” that the record is suffciently developed. Ante, at 256. I
do not think that this assertion fairly captures the views of either the
amicus or the OCCA. When asked whether he “object[ed] to an eviden-
tiary hearing,” amicus—whom we appointed to defend the judgment
below in this Court—expressed doubt that he “ha[d] standing to object to
an evidentiary hearing.” Tr. of Oral Arg. 107–108. When pushed on the
point, he responded that the current record supports affrmance “based on
the evidence that [Glossip has] chosen to present and particularly given
that he's now told you he wants the case decided on the current record
[and] without an evidentiary hearing.” Id., at 109 (emphasis added). In
other words, amicus simply stated that the current record did not support
Glossip's claim—not that the record was in any objective sense already
fully developed. Moreover, the question here is not only whether further
factual development is warranted, but also which court should fnd facts
in the frst instance. Amicus certainly did not concede that this Court,
rather than the OCCA, should play that role on this record. As for the
OCCA, its lack of explanation of the facts cannot be divorced from its
erroneous view of Napue. Nothing in its opinion indicates what it would
make of this record evidence if it confronted the relevant questions
under Napue.
262                GLOSSIP v. OKLAHOMA

                     Thomas, J., dissenting

   I respectfully disagree. Smothermon's notes, taken dur-
ing a jailhouse interview of Sneed, consist of the words “on
Lithium?” and “Dr Trumpet?” 3 App. 927. These notes
are hardly clear, and there are competing explanations of
what they mean. Glossip, the Oklahoma attorney general,
and the Court argue that they demonstrate Smothermon's
knowledge that Sneed had lied about Dr. Trombka's prescrib-
ing him lithium for bipolar disorder. See ante, at 247–248,
255. The Van Treese amicus brief and Justice Thomas
contend that the notes instead refect Sneed's account of a
conversation with Glossip's lawyers, who had asked Sneed
whether he had received lithium from a “Dr Trumpet.” See
post, at 272–275, and n. 3 (dissenting opinion). There are
other possibilities too: For instance, perhaps Smothermon
was confused by references to “Dr Trumpet” and lithium but
never investigated the issue further. Neither Dr. Trombka's
affdavit nor the attached medical information sheet nor any
of the other record evidence discussed by the Court fore-
Page Proof Pending Publication
closes any of these possibilities.
   When the record is susceptible to multiple plausible infer-
ences, this Court should not be in the business of choosing
between them. It should have corrected the OCCA's mis-
statements of federal law and vacated the judgment, leaving
next steps—including the decision whether to conduct an ev-
identiary hearing—to the OCCA. By doing otherwise, the
Court has both displaced the OCCA as factfnder and poten-
tially overridden state-law constraints on the OCCA's reme-
dial authority. See post, at 293–301 (Thomas, J., dissent-
ing). Because the Court has exceeded its appellate role, I
respectfully dissent in part.

  Justice Thomas, with whom Justice Alito joins, and
with whom Justice Barrett joins as to Parts IV–A–1, IV–
A–2, and IV–A–3, dissenting.
  Richard Glossip—a convicted murderer twice sentenced to
death by Oklahoma juries—challenges the denial of his ffth
                  Cite as: 604 U. S. 226 (2025)           263

                     Thomas, J., dissenting

application for state post-conviction relief. Although
Glossip won the support of Oklahoma's new attorney general,
he failed to persuade either body with authority to grant
him relief: The Oklahoma Court of Criminal Appeals (OCCA)
denied Glossip's application as both procedurally defcient
and nonmeritorious, and Oklahoma's Pardon and Parole
Board denied clemency. Because this Court lacks the power
to override these denials, that should have marked the end
of the road for Glossip. Instead, the Court stretches the law
at every turn to rule in his favor. At the threshold, it con-
cocts federal jurisdiction by misreading the decision below.
On the merits, it fnds a due process violation based on pat-
ently immaterial testimony about a witness's medical condi-
tion. And, for the remedy, it orders a new trial in violation
of black-letter law on this Court's power to review state-
court judgments. I respectfully dissent.

Page Proof Pending
              I
                   Publication
                               A
  This case arises from the 1997 murder of Barry Van
Treese, the owner of an Oklahoma City motel. Beginning
in 1995, Glossip began working for Van Treese as the motel's
manager. 4 Tr. 182–183 (May 14, 2004). In that capacity,
Glossip unoffcially hired 19-year-old Justin Sneed to be the
motel's handyman. Glossip did not pay Sneed; instead,
he let him live at the motel free of charge and occasionally
bought him food. Id., at 43–44; 5 Tr. 67–70 (May 17, 2004);
2 App. 644. In late 1996, Van Treese learned of discre-
pancies in Glossip's accounting suggesting that Glossip had
been allowing guests to stay at the motel off the books and
pocketing the money for himself. 4 Tr. 63, 68–71 (May 14,
2004); 7 Tr. 35, 39–40, 45–49 (May 19, 2004); 11 Tr. 172–173
(May 25, 2004). During a visit to the motel on January
6, 1997, Van Treese confronted Glossip about this issue,
and, having discovered unregistered guests staying at the
264                GLOSSIP v. OKLAHOMA

                     Thomas, J., dissenting

motel, he threatened to report Glossip to the police un-
less Glossip produced receipts for their rooms. 8 Tr. 82
(May 20, 2004).
   Hours later, after Van Treese had gone to bed, Sneed en-
tered Van Treese's motel room and repeatedly beat him over
the head with a baseball bat. 2 App. 662–664; 11 Tr. 55 (May
25, 2004). Sneed left when he thought that he had killed
Van Treese, although the State's forensic pathologist later
determined that Van Treese had initially survived the at-
tack, and died several hours later after slowly bleeding out.
Id., at 55–57, 61; App. to Response to Petitioner's Succ. Ap-
plication for Post-Conviction Relief in No. PCD–2022–819
(OCCA), Tr. of Glossip Police Interview 10 (Jan. 9, 1997).
Following his arrest, Sneed explained to police that Glossip
had urged him to kill Van Treese. 2 App. 645, 660. Accord-
ing to Sneed, Glossip told him that they would both be
evicted if Glossip lost his job, and Glossip had promised to
Page Proof Pending Publication
pay him $10,000 for carrying out the murder. 12 Tr. 95–96,
98 (May 26, 2004).
   Shortly after the attack, Sneed went to Glossip's motel
room and informed him that he had killed Van Treese. Tr.
of Glossip Police Interview 10 (Jan. 9, 1997). Glossip began
directing a coverup. On Sneed's account, Glossip frst told
Sneed to clean up glass shards from a window that Sneed
had broken during the attack. 12 Tr. 122 (May 26, 2004).
Glossip also sent Sneed to retrieve about $4,000 in cash from
Van Treese's car, and then to abandon the car in a nearby
credit union parking lot. Id., at 124, 129. When Sneed re-
turned, the two divided the cash. Id., at 128–129. They
then entered Van Treese's room, whereupon Glossip directed
Sneed to tape a shower curtain over the broken window and
run the air conditioning at full blast to eliminate any odor.
Id., at 130, 132. Glossip then dispatched Sneed to buy plexi-
glass, which the pair installed over the broken window on
the morning of January 7. Tr. of Glossip Police Interview
                        Cite as: 604 U. S. 226 (2025)                      265

                           Thomas, J., dissenting

14–15 (Jan. 9, 1997); 4 Tr. 163–165 (May 14, 2004); 13 Tr. 126
(May 27, 2004).1
  Glossip took additional steps to cover up the murder. He
told multiple witnesses that the window in Van Treese's
room was broken because two drunks had stayed there the
night before and smashed it in a brawl. 5 Tr. 85 (May 17,
2004); 7 Tr. 64 (May 19, 2004); 9 Tr. 46, 206 (May 21, 2004);
11 Tr. 188–189 (May 25, 2004). He told the housekeeper that
she did not need to clean the downstairs rooms—including
Van Treese's room. 8 Tr. 122–123 (May 20, 2004). Instead,
as Glossip explained to another employee and a motel resi-
dent, he and Sneed would cover those rooms. 7 Tr. 64 (May
19, 2004); 9 Tr. 49 (May 21, 2004). Glossip had never taken
such steps before. 8 Tr. 122–123 (May 20, 2004). He also
told various witnesses that he had seen Van Treese alive and
   1
     Despite its consistent theme that Sneed's testimony is too implausible
to sustain Glossip's conviction, the majority feels the need to bolster its
Page Proof Pending Publication
account by fnding “inconsisten[cies]” in his testimony that are not genu-
ine. Ante, at 234, n. 1. There is no contradiction in Sneed's claims that
he committed the murder as part of a robbery and that he did so to avoid
being “ `evicted if Glossip lost his job.' ” Ibid. At both of Glossip's trials,
Sneed consistently testifed that Glossip proposed taking the cash Van
Treese had with him and that Glossip told him that they would get evicted
if he did not kill Van Treese. 12 Tr. 95–96, 98, 124 (May 26, 2004); 6 Tr.
89–90, 95–96 (June 8, 1998). Contemporaneous evidence supports both
motivations. In his confession to police, Sneed stated that Glossip had
proposed killing Van Treese and taking the cash that Van Treese had with
him. 2 App. 675. And, two days after the murder, Glossip told police
that Sneed had committed the murder in part because “[h]e thought Barry
[Van Treese] was going to throw him out in the street.” Tr. of Glossip
Police Interview 13 (Jan. 9, 1997). Nor did Sneed ever claim that “he did
not know why Glossip wanted him to kill Van Treese.” Ante, at 234, n. 1.
He testifed only that he did not know “why Mr. Glossip wanted to kill
Mr. Van Treese on this particular night,” because “[e]very time that
Mr. Van Treese showed up, [Glossip] was wanting me to kill him.” 6 Tr.
89 (June 8, 1998) (emphasis added). As noted, Sneed clearly testifed at
the same trial that Glossip wanted Sneed to kill Van Treese so that they
would not be evicted. Id., at 90.
266                 GLOSSIP v. OKLAHOMA

                      Thomas, J., dissenting

well around 7 o'clock that morning. 4 Tr. 99 (May 14, 2004);
7 Tr. 62–63 (May 19, 2004); 9 Tr. 194 (May 21, 2004); 11 Tr.
126–127, 182–183 (May 25, 2004).
   That afternoon, the credit union called the motel to report
that Van Treese's car had been abandoned in its parking lot.
7 Tr. 70 (May 19, 2004). At that point, it became clear
to the motel's staff that Van Treese was missing. Id., at
72–74. Shortly thereafter, Glossip returned to the motel
from a shopping trip, during which he had made several
large purchases, including an engagement ring for his girl-
friend. Id., at 74; 14 Tr. 41 (May 28, 2004). He then pur-
ported to search the rooms and surrounding area for Van
Treese. 5 Tr. 97 (May 17, 2004); 9 Tr. 192–193 (May 21,
2004); 11 Tr. 185–186, 190 (May 25, 2004). He even assured
Van Treese's wife over the phone that everything was fne
and that he had seen Van Treese that morning. 4 Tr. 99–
100 (May 14, 2004).
Page Proof Pending Publication
   Glossip later repeated to a local police offcer the story that
two drunks had broken the window and that he had seen
Van Treese that morning. 9 Tr. 194, 206–207 (May 21, 2004).
Unpersuaded, the offcer checked the room with the broken
window and discovered Van Treese's body. Id., at 220, 224–
225; 11 Tr. 191, 194 (May 25, 2004). Glossip immediately told
the offcer that he suspected that Sneed had something to do
with the murder, explaining that he had heard glass breaking
and that Sneed had banged on his door, but he did not claim
to know anything more. 9 Tr. 233 (May 21, 2004).
   Homicide detectives interviewed Glossip later that night.
Tr. of Glossip Police Interview 1, 10–11 (Jan. 8, 1997). He
denied knowing that Van Treese had been murdered before
the body was discovered. Id., at 70, 86. And, he vacillated
between doubting that Sneed was involved and asserting
that he likely was. Id., at 27–28, 69–70.
   On the morning of January 8, Glossip began to sell all his
possessions, telling multiple witnesses that he would like to
leave town. 8 Tr. 88 (May 20, 2004); 11 Tr. 199 (May 25,
                   Cite as: 604 U. S. 226 (2025)           267

                     Thomas, J., dissenting

2004). On January 9, police picked up Glossip after he failed
to appear for a meeting with homicide detectives. 12 Tr. 7
(May 26, 2004). He had $1,757 in cash on his person and
no explanation for how he—living paycheck to paycheck and
having made only $490 from selling his possessions the pre-
vious day—had so much cash. Id., at 12–13; 14 Tr. 43–44
(May 28, 2004); 15 Tr. 17, 93 (June 1, 2004).
   Glossip sat for a second interview with homicide detectives
later that day. Tr. of Glossip Police Interview 1 (Jan. 9,
1997). This time, although continuing to deny that he had
ordered Sneed to kill Van Treese, Glossip admitted that
Sneed had told him about the murder just after committing
it, and that he had instructed Sneed to clean up the glass
and repair the window. Id., at 13–14, 36. Glossip also ad-
mitted that Van Treese “was upset because the motel wasn't
doing as well as it could.” Id., at 32. When asked why he
hid the murder, Glossip denied doing so to protect Sneed.
Page Proof Pending Publication
He said he covered up the murder instead to protect himself,
because he “was involved in it” and risked losing his girl-
friend otherwise. Id., at 29–30.
   During this interview, Glossip also tried to minimize his
involvement in the crime by insisting that he had not gone
inside Van Treese's hotel room after the attack. Id., at 18;
see also ante, at 232 (emphasizing this denial). At trial,
however, a motel resident testifed that, on the morning of
January 7, Glossip had said that he and Sneed had been “in
the room” after the window was broken. 9 Tr. 120 (May
21, 2004).
   Police arrested Sneed fve days later and charged him with
capital murder. 2 App. 644–645. He had $1,680 in cash in
his possession. 14 Tr. 12–18 (May 28, 2004). At frst, Sneed
denied involvement, claiming that his brother and Glossip
had once discussed the idea but that it never went beyond
talk. 2 App. 655–657. Later in the interview, however,
Sneed confessed to murdering Van Treese at Glossip's insti-
gation. Id., at 660, 664.
268                 GLOSSIP v. OKLAHOMA

                     Thomas, J., dissenting

                               B
                                1
   Glossip was convicted and sentenced to death in 1998, but
the OCCA ordered a retrial based on ineffective assistance
of counsel. 2001 OK CR 21, 29 P. 3d 597.
   At his second trial in 2004, a jury convicted Glossip again,
and the judge again sentenced him to death. Sneed testifed
against Glossip during the guilt phase, as he had at the frst
trial. While Sneed was providing background information
about himself at the outset of this testimony, the State's lead
prosecutor, Connie Smothermon, asked him whether he had
received any “prescription medication” after being arrested.
12 Tr. 63–64 (May 26, 2004). Sneed responded that he had
briefy been prescribed “Lithium for some reason, I don't
know why. I never seen no psychiatrist or anything.” Id.,
at 64. The matter did not come up again during the trial.
   It would not have been challenging for the parties to de-
Page Proof Pending Publication
duce the reason for Sneed's lithium prescription. It is un-
disputed that lithium's sole medical purpose, both in 1997 and
today, is to treat bipolar disorder and other mental health
disorders. See ante, at 247. Were there any doubt about
Sneed's condition, records long available to both sides resolve
it. In 1997, Sneed underwent a pretrial competency evalua-
tion with forensic psychologist Dr. Edith King. Dr. King's
report strongly suggested that although Sneed himself may
have been in denial, he was taking lithium to treat bipo-
lar disorder or a similar condition. During his evaluation,
Sneed asserted that he “d[id] not think he ha[d] any serious
mental problems.” 2 App. 701. And, he reported he was
given the lithium, apparently by mistake, “after his tooth
was pulled.” Id., at 700. Dr. King felt otherwise. Con-
cluding that Sneed qualifed as a “mentally ill person or a
person requiring treatment,” ibid., she determined that he
likely had “an atypical mood swing disorder in his past char-
acterized by `ups and downs' including anger outburst.” Id.,
                   Cite as: 604 U. S. 226 (2025)            269

                     Thomas, J., dissenting

at 702. “His present medication [i.e., the lithium] is prob-
ably helping him control his moods.” Ibid.
   The defense was well aware of this report before Glossip's
second trial. In fact, on direct appeal of his frst conviction,
Glossip's appellate counsel had faulted his trial counsel for
not using Dr. King's report to show the jury that Sneed was
taking lithium to control his anger. 1 id., at 18. Neverthe-
less, after the OCCA vacated his frst conviction, Glossip de-
clined to seek further pretrial discovery on the issue or raise
it during his second trial.
   After his second conviction and sentence, Glossip ignored
the lithium issue on direct appeal, instead raising a general
suffciency-of-the-evidence challenge. The OCCA unani-
mously rejected that challenge, fnding that there was suff-
cient evidence to convict and that the State had satisfed an
additional state-law requirement for corroborative evidence
where a conviction rests on accomplice testimony. 2007 OK
CR 12, ¶¶47–53, 157 P. 3d 143, 153–154. Two judges dis-
Page Proof Pending Publication
sented on different grounds but “agree[d] with the majority
that the State presented a strong circumstantial case against
Glossip.” Id., at 175 (Chapel, J.); see also ibid. (A. John-
son, J.).
                               2
   Glossip has spent the past two decades challenging his con-
viction and sentence through direct appeal, state and federal
collateral proceedings, and civil litigation under Rev. Stat.
§ 1979, 42 U. S. C. § 1983. Throughout that time, no court
has “determined error in [his] trial proceeding” or found that
“there [has] been a showing of actual innocence.” 2023 OK
CR 5, ¶2, 529 P. 3d 218, 229 (Lumpkin, J., specially concur-
ring). And, for almost that entire duration, the Oklahoma
attorney general has steadfastly defended the verdict and
sentence, insisting that the evidence the State presented in
1998 and 2004 has never “been credibly rebutted.” 3 App.
769.
270                 GLOSSIP v. OKLAHOMA

                      Thomas, J., dissenting

   In 2022, as Glossip's execution date approached, a group of
Oklahoma legislators opposed to his execution commissioned
the law frm Reed Smith LLP to conduct an independent
investigation of his case. The frm, which is publicly com-
mitted to “fghting the death penalty,” id., at 709, n. 3 (alter-
ation and internal quotation marks omitted), issued a fnal
report expressing “grave doubt as to the integrity of Gloss-
ip's murder conviction and death sentence,” Independent In-
vestigation of State v. Richard E. Glossip 6 (June 7, 2022)
(Reed Smith Report). The attorney general vigorously dis-
agreed. In subsequent post-conviction flings, the State as-
serted that the report was “built on assumptions, half-truths,
and (in some cases) outright falsehoods,” 3 App. 769, and
criticized its fndings at length, see id., at 754–769.
   In response to the Reed Smith Report, the attorney gener-
al's offce released all its fles from the case to Glossip, except
for one box of attorney work product. Based on this infor-
Page Proof Pending Publication
mation, Glossip fled a fourth motion for post-conviction relief
in the OCCA, raising two overarching claims. The frst
claim was that the State violated Brady v. Maryland, 373
U. S. 83 (1963), by withholding evidence that Sneed consid-
ered recanting his original testimony before the second trial.
The second claim was that Smothermon, the lead prosecutor,
committed misconduct and violated the rule of sequestration
(which prohibits witnesses from hearing other witnesses' tes-
timony) during trial. After the State's forensic pathologist
testifed that there was evidence Sneed used a knife in addi-
tion to the bat during the murder, Smothermon sent a memo-
randum to Sneed's attorney highlighting ways in which this
testimony was hard to square with some of Sneed's earlier
statements. Glossip thus claimed Smothermon violated the
rule of sequestration by conveying witness statements for
the purpose of coaching Sneed into altering his testimony to
ft the forensic evidence. Attorney General John O'Connor
opposed the application, urging the OCCA not to be cowed
                        Cite as: 604 U. S. 226 (2025)                      271

                           Thomas, J., dissenting

by the ongoing “public relations campaign” to “falsely” pres-
ent Glossip as “innocent.” 3 App. 717.
   The OCCA unanimously denied the application. Under
Oklahoma's Post-Conviction Procedure Act (PCPA), Glossip's
post-conviction application could not proceed unless he could
show (1) that the “factual basis for the claim” was previously
unavailable and (2) that, but for the alleged error, no rea-
sonable jury would have convicted him or sentenced him
to death. Okla. Stat., Tit. 22, § 1089(D)(8)(b) (2024). The
OCCA held that both claims failed the frst requirement be-
cause they were not based on new information. It also held
that Glossip's claims failed on the merits.
   As to the recantation claim, the OCCA held that Glossip's
frst claim was procedurally barred because the defense
knew even before the 2004 trial that Sneed was reluctant to
testify again. 3 App. 777. In fact, one of Glossip's attor-
neys had even visited Sneed before trial in an effort to per-
suade him not to testify. Ibid. On the merits, there was
Page Proof Pending Publication
“no evidence that Sneed had any desire to recant or change
his testimony.” Id., at 776. Sneed had even told Reed
Smith that “ `recant[ing]' ” was “ `impossible because I told the
truth.' ” Id., at 724. Sneed was reluctant to testify because
he wanted to obtain a better plea deal or to avoid the disrup-
tion to his life that testifying would cause. Id., at 776.2

  2
    The majority points to a letter from Sneed to his attorney in which Sneed
raised the prospect of “ ` “recanting” ' ” his trial testimony. Ante, at 238
(quoting 3 App. 815). But, in two subsequent interviews with Reed Smith
attorneys, Sneed made clear that, although he wanted to avoid testifying
again if possible, he continued to stand by the truth of his earlier testimony:
  “[REED SMITH ATTORNEY]: Yeah. Well, I think the bottom line
here, the most important things that we needed to clarify was like when
you're talking about recanting, you're not talking about changing your
story about what happened. Have you ever indicated to anybody that
you ever wanted to change your story about what happened?
  “JUSTIN SNEED: No, sir. I have not ever indicated that I wanted to
change the truth of him applying pressure to me.” App. to Response to
272                    GLOSSIP v. OKLAHOMA

                         Thomas, J., dissenting

  Turning to the sequestration claim, the OCCA pointed out
that Smothermon had acknowledged at trial that she had
spoken with Sneed's counsel, so the claim likewise lacked a
new factual basis. Id., at 780; see 12 Tr. 107–108 (May 26,
2004). On the merits, the court held that Oklahoma's se-
questration statute does not prohibit counsel from discussing
with a witness other witnesses' testimony. 3 App. 781.
Federal courts have similarly interpreted the federal seques-
tration rule to permit “witnesses . . . to discuss the case”
with “counsel for either side.” 2A C. Wright & P. Henning,
Federal Practice and Procedure § 416, p. 195, and n. 29 (4th
ed. 2009) (collecting cases). And, nothing in Smothermon's
memorandum indicates she was encouraging Sneed to lie. 3
App. 781–782.
                               3
  In January 2023, Gentner Drummond became Oklahoma's
attorney general. During his frst month in offce, Drum-
Page Proof Pending Publication
mond released the fnal box of evidence (Box 8) to Glossip.
He also appointed Rex Duncan, a personal friend and cam-
paign donor, as independent counsel to reexamine the legiti-
macy of Glossip's conviction.
  Among the materials released in Box 8 were handwritten
notes taken by Smothermon and her co-counsel Gary Ackley
during a 2003 meeting between them, Sneed, and Sneed's
attorney.

Petitioner's Succ. Application for Post-Conviction Relief in No. PCD–
2022–819 (OCCA), Tr. of Sneed Reed Smith Interview 46–47 (Aug. 15,
2022).
   See also id., Tr. of Sneed Reed Smith Interview 24 (Sept. 7, 2022)
(“There isn't any way of really making up some [new] storyline that isn't
going to cover all the evidence that is already there . . . ”). Sneed has
never on any occasion indicated that his testimony that Glossip directed
him to kill Van Treese was false, see 3 App. 724–725, and the majority
cites no such occasion. The best explanation for Sneed's letter, and the
one that the OCCA credited as factual, is thus that Sneed, an eighth-grade
dropout, used the phrase “recanting my testimony” imprecisely to mean
“refuse to testify.” Id., at 725, and n. 13, 776.
                     Cite as: 604 U. S. 226 (2025)          273

                       Thomas, J., dissenting

   Glossip's counsel quickly seized on Smothermon's notes.
In the top left corner of the notes, Smothermon had written
“on Lithium?” and “Dr Trumpet?” See Figure 1, infra.
According to Glossip's counsel, these phrases meant that
Sneed had admitted during the meeting that he had been
prescribed lithium by Dr. Lawrence Trombka, the psychia-
trist at the Oklahoma County Jail.
   Smothermon and Ackley disagree with this interpretation.
They assert before this Court that, during the meeting,
Sneed recounted two interviews that he previously had with
members of Glossip's defense team. In context, Smother-
mon's notes simply record that Sneed told her that Glossip's
defense team had asked him about his use of lithium and
about “Dr Trumpet.” The prosecutors claim that this fact
is apparent from the other notes on the page and from
Ackley's notes, both of which refer to details of these prior
interviews. Ackley's notes also highlight the phrase “ `tooth
pulled.' ” 3 App. 940. The prosecutors' interpretation of
Page Proof Pending Publication
their own notes thus suggests that Sneed recounted that he
had responded to questions about lithium and Dr. Trombka




Figure 1. Smothermon's handwritten notes. See 3 App. 927.
274                     GLOSSIP v. OKLAHOMA

                           Thomas, J., dissenting

with his earlier story that he was prescribed lithium in
error after having his tooth pulled. This interpretation
is explained at great length by the Van Treese family's
brief. See Brief for Victim Family Members as Amici
Curiae 7–22.3 And, as of yet, no one—including the par-
  3
    According to Smothermon, her notes refect two visits (“2X”) by de-
fense representatives—with notes about the two visits separated by a ho-
rizontal line. According to the notes above the line, Sneed's frst visitors
were “women,” one of whom was an investigator (“invest.”) who may have
been heavy set (“heavy set?”). These visitors may have been involved in
Glossip's earlier direct “appeal.” These women asked Sneed whether he
was “on Lithium?” and about a “Dr Trumpet?” The notes also document
a discussion of a “waiver for records,” “IQ test,” and “GED. VoTech.”
Similarly, Ackley's notes record that the “W[itness, i.e., Sneed,] was visited
by 2 women who said they rep Glossip.” They were “heavy,” “1 `Inv.' &
1 `Atty,' ” who may have been on Sneed's “Appellate” team. These two
women asked Sneed about lithium (“Li”), and he responded with some-
thing about getting his “ `tooth pulled.' ” Brief for Victim Family Mem-
bers as Amici Curiae 9–12.
Page Proof Pending Publication
   These notes correspond to Sneed's 2001 meeting with Wyndi Hobbs
(Glossip's post-conviction counsel) and an investigator named Lisa Cooper,
which was documented in the record of Glossip's fourth post-conviction
application. See 3 App. 729–730. At this meeting, Sneed “ `signed re-
leases for juvenile, jail, prison and criminal records,' ” id., at 729, which
corresponds to the “waiver for records” mentioned in Smothermon's notes.
Sneed later wrote a letter to Cooper to ensure that she received informa-
tion about his participation in a “vo-tech program,” id., at 730, which cor-
responds to the reference to “GED. VoTech.”
   According to Smothermon's notes below the line, Sneed's second visit
was from a “man” named “Burch” who tried to “con [him] out” of giving
“testimony” against Glossip. Burch “gave [Sneed a] case.” Ackley's
notes likewise indicate that Sneed “[l]ater” met with “1 guy” named
“Burch.” Sneed said of the meeting, ` “Basically all he was trying to do
was con me out of not [sic] getting onto the stand.' ” Brief for Victim
Family Members as Amici Curiae 9–13 (alteration in original).
   The flings from Glossip's fourth application also recount that Lynne
Burch, one of Glossip's attorneys, met with Sneed after the OCCA vacated
Glossip's frst conviction. 3 App. 731. Burch told Sneed “ `he didn't have
to testify' ” in Glossip's second trial, and (in line with Smothermon's notes)
gave Sneed a case, State v. Dyer, 2001 OK CR 31, 34 P. 3d 652, holding
that the State could not renege on a plea agreement for refusing to testify
at a codefendant's second trial. 3 App. 731–732.
                   Cite as: 604 U. S. 226 (2025)           275

                     Thomas, J., dissenting

ties and the majority—has attempted to refute it on the
merits.
   Based on Smothermon's notes, Glossip fled a ffth post-
conviction application in the OCCA in March 2023. He
framed the notes as new evidence of Sneed's previously un-
known bipolar disorder. Glossip attached an affdavit from
Dr. Trombka stating that he was the only person who would
have prescribed lithium while Sneed was in jail. Glossip
also attached what appears to be a jail record indicating that
Sneed has bipolar disorder. He argued that the State's re-
fusal to produce these notes before trial violated Brady, on
the theory that he could have used Sneed's condition to im-
peach his testimony.
   At the same time, Glossip recognized that he would need
additional evidence to prove his theory. Together with his
application, Glossip also fled a motion for an evidentiary
hearing, in which he sought to call Smothermon and Ackley
as witnesses. Motion for Evidentiary Hearing in No. PCD–
Page Proof Pending Publication
2023–267 (OCCA), p. 2. Glossip explained in the motion that
“the resolution” of his Brady claim “turns in part on inter-
pretation of prosecutors' notes.” Motion for Evidentiary
Hearing, at 1. “Without their testimony,” he acknowledged,
“any fnding about what they meant or what the attorneys
did or did not know when they wrote them would be specula-
tion.” Id., at 1–2.
   Independent Counsel Duncan, on the other hand, deter-
mined that no further evidence was needed. Duncan re-
leased his fnal report shortly after Glossip fled his ffth
application. He agreed that the State violated Glossip's
Brady rights and asserted that Smothermon's failure to cor-
rect Sneed's testimony amounted to a due process violation
under Napue v. Illinois, 360 U. S. 264 (1959). Duncan based
his conclusions on the speculation that “seasoned capital
homicide prosecutors . . . could be expected” to know that
“Trumpet” referred to Dr. Trombka and that Dr. Trombka
was the psychiatrist at the Oklahoma County Jail. App. to
Reply Brief in Support of Pet. for Cert. 23a. He then con-
276                    GLOSSIP v. OKLAHOMA

                         Thomas, J., dissenting

cluded the report with praise for Drummond, stating that
Drummond's “decision to seek a stay of execution and more
thoroughly examine this case may be the bravest leadership
decision I've ever witnessed.” Id., at 30a.
   Notably, Duncan failed to give Smothermon a meaningful
opportunity to explain what her notes may have meant or
what she knew about Sneed's medical history. Instead, he
discussed the matter with her only once, during a 3-minute
phone call. App. to Brief for Victim Family Members as
Amici Curiae 31a. Worse, he gave Smothermon no chance
to review the decades-old notes before asking her to explain
them during the brief call. Ibid. Drummond was likewise
uninterested in hearing from the attorney he and Duncan
were impugning. Following Duncan's report, both Smother-
mon and the Van Treese family contacted Drummond's offce
to request that Drummond speak with Smothermon about
the notes. Id., at 6a–7a, 71a. Their pleas were ignored.4
  At the attorney general's behest, the State supported
Page Proof Pending Publication
Glossip's post-conviction application. It argued that Smoth-
ermon's notes proved that the prosecutors violated Brady
and Napue, and that Glossip was entitled to relief under the
State's PCPA. It neglected to address, however, the strin-
gent limitations that the PCPA imposes on such subsequent
applications. See § 1089(D)(8)(b).

  4
    The majority insists that Smothermon had a fair opportunity to explain
her notes because she met once with attorneys at the Reed Smith law frm
and had an earlier, longer phone call with Duncan. Ante, at 255. But,
the Reed Smith meeting occurred before the release of Box 8. See Reed
Smith Report 80, n. 321 (noting that the Reed Smith meeting occurred in
May 2022, eight months before Box 8 was released in January 2023).
And—by his own admission—Duncan “forgot to ask” Smothermon about
“Dr. Larry Trombka” during his earlier, longer phone call. App. to Brief
for Victim Family Members as Amici Curiae 32a. The majority also
faults Smothermon for not having an explanation ready during the 3-
minute phone call. Ante, at 255. But, without giving Smothermon an
opportunity to review the notes, it was unreasonable to expect her instan-
taneously to recall their meaning 20 years later.
                  Cite as: 604 U. S. 226 (2025)           277

                     Thomas, J., dissenting

   The OCCA unanimously denied Glossip's ffth post-
conviction application. The court frst held that Glossip had
not satisfed either requirement of § 1089(D)(8)(b), and thus
that the Brady and Napue claims were procedurally barred.
529 P. 3d, at 226. The OCCA then held that both claims also
failed on the merits. No Brady violation occurred, the court
explained, because Sneed's 1997 pretrial competency report
already informed the defense of Sneed's prescription and
condition. The OCCA determined that defense counsel had
likely made a strategic decision not to base a defense on
them. 529 P. 3d, at 226. Nor was there any Napue viola-
tion, according to the court, because Sneed's testimony “was
not clearly false” and, in any event, was not material given
defense counsel's choice not to raise Sneed's condition. 529
P. 3d, at 226–227. After the OCCA issued its decision, Okla-
homa's Pardon and Parole Board denied clemency.
                             II
Page Proof Pending Publication
   As an initial matter, we lack jurisdiction to review this
case. “This Court from the time of its foundation has ad-
hered to the principle that it will not review judgments of
state courts that rest on adequate and independent state
grounds.” Herb v. Pitcairn, 324 U. S. 117, 125 (1945). “Be-
cause this Court has no power to review a state law deter-
mination that is suffcient to support the judgment, resolu-
tion of any independent federal ground for the decision could
not affect the judgment and would therefore be advisory.”
Coleman v. Thompson, 501 U. S. 722, 729 (1991). Thus, on
direct review of a state-court judgment, the presence of an
adequate and independent state ground imposes a “jurisdic-
tional” limitation. Ibid. The decision below rests on such
grounds, and the majority concludes otherwise only by
grossly mischaracterizing the state court's analysis.
                             A
  The PCPA authorizes a criminal defendant to collaterally
challenge his conviction on the ground that it violates the
278                 GLOSSIP v. OKLAHOMA

                      Thomas, J., dissenting

Federal Constitution. Okla. Stat., Tit. 22, § 1080(1). But,
given the extraordinary nature of collateral challenges, the
statute also imposes a variety of restrictions on relief. In
capital cases, the applicant must establish not just a constitu-
tional violation, but also, among other requirements, that his
claim “could not have been raised in a direct appeal” and that
“the outcome of the trial would have been different but for
the errors or that the defendant is factually innocent.”
§ 1089(C).
   

[...TRUNCATED 59914 of 179914 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Goldey v. Fields.md  (`case`, 5 assertions)

### content_page

```
---
title: Goldey v. Fields
type: case
citation: "606 U.S. 942 (2025)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2025
date_decided: ""
docket: 24-809
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
  opinion_url: "https://www.courtlistener.com/opinion/10776815/goldey-v-fields/"
  cluster_id: 10776815
  opinion_id: null
  identity_checked: true
lake:
  record_id: Goldey v. Fields
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
  - bivens
  - eighth-amendment
  - excessive-force
  - prisoner-litigation
  - federal-officer-liability
holding: "Bivens does not extend to allow a federal prisoner's Eighth Amendment excessive-force claim for damages against federal prison officials; the claim arises in a new Bivens context and special factors — Congress's active but remedy-free legislation in prisoner litigation, risks to prison operations, and existing alternative remedies — counsel against recognizing an implied damages action."
---

# Goldey v. Fields

*606 U.S. 942 (2025)* (No. 24-809) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10776815 → opinion 11243402 (per curiam); quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Andrew Fields, a federal prisoner at the U.S. Penitentiary in Lee County, Virginia, was placed in solitary confinement, where he alleges prison officials physically abused him during periodic checks. He sued Bureau of Prisons officials for damages under *[[Bivens v. Six Unknown Named Agents|Bivens]]*, claiming excessive force in violation of the Eighth Amendment. The District Court dismissed the complaint, holding that Fields lacked a *[[Bivens v. Six Unknown Named Agents|Bivens]]* cause of action because the claim arose in a new context. A divided Fourth Circuit reversed, concluding that no special factors counseled against extending *[[Bivens v. Six Unknown Named Agents|Bivens]]*; Judge Richardson dissented. The prison officials, supported by the United States as amicus, sought review.

## Issue
Whether *[[Bivens v. Six Unknown Named Agents|Bivens]]* supplies an implied damages remedy for a federal prisoner's Eighth Amendment excessive-force claim against federal prison officials.

## Rule
Recognizing a cause of action under *[[Bivens v. Six Unknown Named Agents|Bivens]]* is "a disfavored judicial activity," and for more than four decades the Court has declined more than ten times to extend *[[Bivens v. Six Unknown Named Agents|Bivens]]* to new contexts. Courts apply a two-step test: whether the claim arises in "a new *Bivens* context" — one "different in a meaningful way" from the three contexts the Court has recognized — and, if so, whether any "special factors" counsel hesitation, with the ultimate question being whether Congress or the courts should create the remedy. Applying that test, the Court held: "*Bivens* does not extend to allow an Eighth Amendment excessive-force claim for damages against federal prison officials." — 606 U.S. at 942. ^pin-942

## Application
A federal prisoner's Eighth Amendment excessive-force claim is a new *[[Bivens v. Six Unknown Named Agents|Bivens]]* context — none of the three recognized contexts involved such a claim — and special factors foreclose an implied remedy. Congress has legislated extensively in the area of prisoner litigation (including the Prison Litigation Reform Act) yet has never created a statutory damages action for such claims; extending *[[Bivens v. Six Unknown Named Agents|Bivens]]* could have negative consequences for prison operations; and federal prisoners already have alternative remedial procedures, such as the Bureau of Prisons' administrative-remedy program. Those considerations counsel leaving any new damages remedy to Congress rather than the courts.

## Conclusion
The judgment of the Fourth Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. The opinion was **[[Common Legal Terms#per-curiam|per curiam]]**.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Goldey* continues the Court's post-*[[Ziglar v. Abbasi]]* / *[[Egbert v. Boule]]* trajectory of confining *[[Bivens v. Six Unknown Named Agents|Bivens]]* to its three recognized contexts and refusing new implied damages remedies against federal officers — here, foreclosing Eighth Amendment excessive-force claims by federal prisoners.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Goldey v. Fields*, 606 U.S. 942 (2025)](https://www.courtlistener.com/opinion/10776815/goldey-v-fields/) — pinpoint: 942 (holding, per curiam); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c689bd0ec249fce5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "606 U.S. 942 (2025)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Goldey v. Fields", "year": "2025"}}
{"assertion_id": "65de7b8a434590bc", "dimension": "support", "kind": "home_role", "locator": {"home": "Suing Federal Officers"}, "payload": {"home": "Suing Federal Officers", "role": "Recent development", "title": "Goldey v. Fields"}}
{"assertion_id": "c3b919a408946752", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Bivens does not extend to allow a federal prisoner's Eighth Amendment excessive-force claim for damages against federal prison officials; the claim arises in a new Bivens context and special factors — Congress's active but remedy-free legislation in prisoner litigation, risks to prison operations, and existing alternative remedies — counsel against recognizing an implied damages action.", "title": "Goldey v. Fields"}}
{"assertion_id": "307ddd7c94fe8f34", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Goldey v. Fields", "varies_by_point": "false"}}
{"assertion_id": "bef5b920d3cbb57a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Goldey v. Fields"}}
```

### lake record — Goldey v. Fields

```json
{
  "schema_version": "s2.v1",
  "record_id": "Goldey v. Fields",
  "status": "under_review",
  "identity": {
    "case_name": "Goldey v. Fields",
    "case_name_short": "Goldey",
    "case_name_full": "",
    "input_case_name": "Goldey v. Fields",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2025,
    "docket": "24-809",
    "cluster_id": 10776815,
    "lead_opinion_id": 11243402,
    "sibling_ids": [],
    "absolute_url": "/opinion/10776815/goldey-v-fields/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "606 U.S. 942",
      "volume": "606",
      "reporter": "U.S.",
      "page": "942",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "606 U.S. 942",
        "volume": "606",
        "reporter": "U.S.",
        "page": "942",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "606 U.S. 942",
    "official_selection": {
      "court_class": "scotus",
      "selected": "606 U.S. 942",
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
    "date_created": "2026-07-06T12:13:01Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:13:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:13:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "goldey-v-fields--10776815",
      "to_record_id": "Goldey v. Fields",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Goldey v. Fields

```
                   PRELIMINARY PRINT

              Volume 606 U. S. Part 2
                             Pages 942–945




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                                June 30, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
942                     OCTOBER TERM, 2024

                               Per Curiam


 GOLDEY, ASSOCIATE WARDEN, et al. v. FIELDS
                   et al.
   on petition for writ of certiorari to the united
    states court of appeals for the fourth circuit
                   No. 24–809. Decided June 30, 2025
Prison offcials at the U. S. Penitentiary in Lee County, Virginia, placed
  respondent Fields in solitary confnement. Fields alleges that during
  periodic checks, offcials physically abused him. Fields sued the Bureau
  of Prisons and prison offcials for damages, claiming excessive force in
  violation of the Eighth Amendment. The District Court dismissed
  Fields's complaint, determining he lacked a cause of action under Bivens
  v. Six Unknown Fed. Narcotics Agents, 403 U. S. 388. The Fourth Cir-
  cuit reversed, concluding that Fields could proceed with his Eighth
  Amendment excessive-force claim for damages.
Held: Bivens does not extend to allow an Eighth Amendment excessive-
  force claim for damages against federal prison offcials. For 45 years,
  this Court has consistently declined to extend Bivens to new contexts.
Page Proof Pending Publication
  This case arises in a new context, and special factors counsel against
  recognizing an implied Bivens cause of action for Eighth Amendment
  excessive-force violations. Congress has actively legislated in prisoner
  litigation but has not enacted a statutory cause of action for money
  damages. Extending Bivens to excessive-force claims could have nega-
  tive consequences for prison operations, and alternative remedial proce-
  dures already exist for federal prisoners.
Certiorari granted; 109 F. 4th 264, reversed and remanded.

  Per Curiam.
  In Bivens v. Six Unknown Fed. Narcotics Agents, 403
U. S. 388 (1971), this Court recognized an implied cause of
action for damages against federal offcers for certain alleged
violations of the Fourth Amendment. The Court subse-
quently recognized two additional contexts where implied
Bivens causes of action were permitted, neither of which was
an Eighth Amendment excessive-force claim. After 1980,
we have declined more than 10 times to extend Bivens to
cover other constitutional violations. Those many post-1980
Bivens “cases have made clear that, in all but the most un-
                   Cite as: 606 U. S. 942 (2025)            943

                           Per Curiam

usual circumstances, prescribing a cause of action is a job for
Congress, not the courts.” Egbert v. Boule, 596 U. S. 482,
486 (2022). Despite those precedents, the U. S. Court of Ap-
peals for the Fourth Circuit permitted the plaintiff here
to maintain an Eighth Amendment excessive-force Bivens
claim for damages against federal prison offcials.
   This case began when prison offcials at the U. S. Peniten-
tiary in Lee County, Virginia, ordered that plaintiff Andrew
Fields be placed in solitary confnement. Prison offcials
monitored Fields while he was isolated. Fields alleges that
during their periodic checks, offcials would “physically
abuse” him. Fields v. Federal Bureau of Prisons, 109 F. 4th
264, 268 (CA4 2024).
   Fields sued the Bureau of Prisons (BOP), the prison war-
den, and several prison offcials in federal court for damages,
claiming that certain prison offcials used excessive force
against him in violation of the Eighth Amendment. The
Page Proof Pending Publication
U. S. District Court for the Western District of Virginia dis-
missed Fields's complaint. As relevant here, the court de-
termined that Fields lacked a cause of action under Bivens.
Because “the Supreme Court has never ruled that a damages
remedy exists for claims of excessive force by BOP offcers
against an inmate,” the District Court had “no diffculty in
concluding that these claims arise in a new context” and that
a Bivens remedy was unavailable. App. to Pet. for Cert.
49a; see id., at 45a–54a.
   Fields appealed. In a divided decision, the Fourth Circuit
reversed in relevant part, concluding that Fields could pro-
ceed with his Eighth Amendment excessive-force claim for
damages. The Court of Appeals determined that no “special
factors counseled against extending Bivens” here. 109
F. 4th, at 270.
   Judge Richardson dissented and stated: “A faithful applica-
tion of our precedent and the Supreme Court's leads squarely
to the conclusion that we cannot create a new Bivens action
here.” Id., at 283.
944                  GOLDEY v. FIELDS

                          Per Curiam

   After the Fourth Circuit denied rehearing en banc, prison
offcials sought review in this Court, with the support of the
United States as amicus curiae. We now grant the petition
for certiorari and reverse.
   This Court has repeatedly emphasized that “recognizing a
cause of action under Bivens is `a disfavored judicial activ-
ity.' ” Egbert, 596 U. S., at 491. To determine whether a
Bivens claim may proceed, the Court has applied a two-step
test. First, the Court asks whether the case presents “a
new Bivens context”—that is, whether the case “is different
in a meaningful way” from the cases in which this Court has
recognized a Bivens remedy. Ziglar v. Abbasi, 582 U. S.
120, 139 (2017); see Carlson v. Green, 446 U. S. 14 (1980);
Davis v. Passman, 442 U. S. 228 (1979); Bivens, 403 U. S. 388.
   Second, if so, we then ask whether there are “special fac-
tors” indicating that “the Judiciary is at least arguably less
equipped than Congress to `weigh the costs and benefts of
Page Proof Pending Publication
allowing a damages action to proceed.' ” Egbert, 596 U. S.,
at 492. That analysis is anchored in “separation-of-powers
principles.” Ziglar, 582 U. S., at 135.
   This case arises in a new context, and “special factors”
counsel against recognizing an implied Bivens cause of action
for Eighth Amendment excessive-force violations. To begin
with, Congress has actively legislated in the area of prisoner
litigation but has not enacted a statutory cause of action for
money damages. See Ziglar, 582 U. S., at 148–149. In ad-
dition, extending Bivens to allow an Eighth Amendment
claim for excessive force could have negative systemic con-
sequences for prison offcials and the “inordinately diffcult
undertaking” of running a prison. Turner v. Safey, 482
U. S. 78, 84–85 (1987). Moreover, “an alternative remedial
structure” already exists for aggrieved federal prisoners.
Ziglar, 582 U. S., at 137; see Correctional Services Corp. v.
Malesko, 534 U. S. 61, 74 (2001). The existence of such al-
ternative remedial procedures counsels against allowing
                   Cite as: 606 U. S. 942 (2025)                 945

                           Per Curiam

Bivens suits even if such “procedures are `not as effective as
an individual damages remedy.' ” Egbert, 596 U. S., at 498.
   For the past 45 years, this Court has consistently declined
to extend Bivens to new contexts. See Egbert, 596 U. S., at
490–491. We do the same here. The petition for certiorari
is granted, the judgment of the U. S. Court of Appeals for
the Fourth Circuit is reversed, and the case is remanded for
further proceedings consistent with this opinion.

                                                   It is so ordered.




Page Proof Pending Publication
                           Reporter’s Note

   The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
Page Proof Pending Publication
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
the Court. Other revisions may include adjustments to formatting, cap-
tions, citation form, and any errant punctuation. The following additional
edits were made:

None

```

---
