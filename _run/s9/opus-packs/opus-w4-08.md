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

## GROUP: _overhaul2/lake/cases/French v. Merrill.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "9a3eca45c8cae6de", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "French v. Merrill"}, "payload": {"all": [{"cite": "15 F.4th 116", "page": "116", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "15"}], "display": "15 F.4th 116", "official": {"cite": "15 F.4th 116", "page": "116", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "15"}, "official_selection_present": true, "record_id": "French v. Merrill"}}
{"assertion_id": "552c797a5124100f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op39a", "record_id": "French v. Merrill"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op39a", "pinpoint_status": "slip-only", "quote": "The officers in this case, like the officers in Jardines, in the absence of any license to do so, 'physically intrud[ed]' on a suspect's property repeatedly and engaged in intrusive conduct that no reasonable visitor could have understood as impliedly authorized by a resident.", "quote_fidelity": "mismatch", "record_id": "French v. Merrill", "star_marker": null}}
{"assertion_id": "771b0a87660f773f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op39", "record_id": "French v. Merrill"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op39", "pinpoint_status": "slip-only", "quote": "During a final visit around 5:00 a.m., officers went onto the property, knocked on the front door and then on French's bedroom window, peered through a drawn window covering, and shined a flashlight inside. French sued under § 1983, and the officers asserted qualified immunity, contending their conduct did not violate clearly established Fourth Amendment law. ## Issue Whether officers who repeatedly entered the curtilage of a home and engaged in intrusive, pre-dawn conduct in the course of attempted knock and talks exceeded the implied social license — and whether [[Florida v. Jardines]] clearly established the unlawfulness of that conduct. ## Rule The knock-and-talk exception is bounded by the implied social license, which is limited in both area and purpose. The court explained that the license's scope", "quote_fidelity": "mismatch", "record_id": "French v. Merrill", "star_marker": null}}
{"assertion_id": "8a722c96db184746", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "French v. Merrill"}, "payload": {"as_of_content": "2021-10-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "French v. Merrill", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/G. M. Leasing Corp. v. United States.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: G. M. Leasing Corp. v. United States
type: case
citation: "429 U.S. 338 (1977)"
parallel_cite: "97 S. Ct. 619; 50 L. Ed. 2d 530; 39 A.F.T.R.2d (RIA) 475"
neutral_cite: 1977 U.S. LEXIS 33
court: U.S.
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-01-12
docket: 75-235
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
  opinion_url: "https://www.courtlistener.com/opinion/109579/g-m-leasing-corp-v-united-states/"
  cluster_id: 109579
  opinion_id: null
  identity_checked: true
lake:
  record_id: G. M. Leasing Corp. v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Curtilage]]"
    role: Key
related:
  - "[[Curtilage]]"
  - "[[The Warrant Requirement]]"
  - "[[Florida v. White]]"
  - "[[Camara v. Municipal Court]]"
tags:
  - case
  - fourth-amendment
  - warrant-requirement
  - commercial-premises
  - tax-levy
holding: "Warrantless seizure of a taxpayer's automobiles from public streets and lots to satisfy a tax levy involves no Fourth Amendment search and needs no warrant, but a warrantless entry into the taxpayer's private business offices to seize books and records is an unreasonable intrusion the Fourth Amendment forbids absent a warrant."
---

# G. M. Leasing Corp. v. United States

*429 U.S. 338 (1977)* (No. 75-235) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109579 → lead opinion 109579; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
After assessing jeopardy income-tax deficiencies against Norman Chreske, IRS agents — acting without a warrant — seized several automobiles held in the name of G. M. Leasing Corp. (found to be Chreske's alter ego) from public streets and parking lots to satisfy the levy, and separately entered the corporation's business offices and seized books and records. G. M. Leasing sued, contending that both the seizure of the cars and the entry into and search of its offices violated the Fourth Amendment.

## Issue
Whether the Fourth Amendment required a warrant (1) to seize the taxpayer's automobiles from public places to enforce a tax levy, and (2) to enter the corporation's private business offices to seize its books and records.

## Rule
The Court analyzed the two intrusions separately. As to the vehicles, a levy on property located in public places is not a search and needs no warrant: "The seizures of the automobiles in this case took place on public streets, parking lots, or other open places, and did not involve any invasion of privacy." — 429 U.S. at 351. ^pin-351

As to the offices, the result was different: "The seizure of the books and records, however, involved intrusion into the privacy of petitioner's offices." — 429 U.S. at 352. ^pin-352

Private commercial premises fall within the Fourth Amendment's protection, and the settled rule is that "except in certain carefully defined classes of cases, a search of private property without proper consent is 'unreasonable' unless it has been authorized by a valid search warrant" — a requirement the Government's tax-collection purpose did not dispense with.

## Application
Because the automobiles were seized from public streets and lots, the levy invaded no privacy interest and required no warrant. But the agents' forced, warrantless entry into the corporation's offices to search for and seize its records intruded on a constitutionally protected private space. Nothing about the tax assessment or the summary-levy power justified that entry without a warrant, so the office intrusion violated the Fourth Amendment even though the underlying levy was lawful.

## Conclusion
The judgment was **affirmed in part and reversed in part**, and the case **[[Reading and Citing Cases#on-remand|remanded]]**: the warrantless seizure of the automobiles was upheld, while the warrantless entry into the offices and seizure of the books and records was held unconstitutional. Blackmun, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *G. M. Leasing* remains a foundational statement that business premises enjoy Fourth Amendment protection and that an administrative or tax-collection objective does not relax the warrant requirement for entering them — while property seized from public places to satisfy a levy implicates no privacy interest at all.

## Appears on
- [[Curtilage]] — *Key*

## Sources
- [*G. M. Leasing Corp. v. United States*, 429 U.S. 338 (1977)](https://www.courtlistener.com/opinion/109579/g-m-leasing-corp-v-united-states/) — pinpoint: 351 (public-place seizure, no invasion of privacy), 352 (intrusion into the privacy of the offices); Opinion of the Court, Blackmun, J.; quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2368edbc4706d2b0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "G. M. Leasing Corp. v. United States"}, "payload": {"all": [{"cite": "429 U.S. 338", "page": "338", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "429"}, {"cite": "97 S. Ct. 619", "page": "619", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "50 L. Ed. 2d 530", "page": "530", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "50"}, {"cite": "1977 U.S. LEXIS 33", "page": "33", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}, {"cite": "39 A.F.T.R.2d (RIA) 475", "page": "475", "reporter": "A.F.T.R.2d (RIA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "39"}], "display": "429 U.S. 338", "official": {"cite": "429 U.S. 338", "page": "338", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "429"}, "official_selection_present": true, "record_id": "G. M. Leasing Corp. v. United States"}}
{"assertion_id": "efe0e883b645a619", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "G. M. Leasing Corp. v. United States"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "G. M. Leasing Corp. v. United States", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — G. M. Leasing Corp. v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "G. M. Leasing Corp. v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "G. M. Leasing Corp. v. United States",
    "case_name_short": "GM Leasing",
    "case_name_full": "G. M. LEASING CORP. Et Al. v. UNITED STATES Et Al.",
    "input_case_name": "G. M. Leasing Corp. v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-01-12",
    "year": 1977,
    "docket": "75-235",
    "cluster_id": 109579,
    "lead_opinion_id": 9426638,
    "sibling_ids": [],
    "absolute_url": "/opinion/109579/g-m-leasing-corp-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 338",
      "volume": "429",
      "reporter": "U.S.",
      "page": "338",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 619",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 530",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 A.F.T.R.2d (RIA) 475",
        "volume": "39",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "475",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 33",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "33",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 338",
        "volume": "429",
        "reporter": "U.S.",
        "page": "338",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 619",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 530",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 33",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "33",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 A.F.T.R.2d (RIA) 475",
        "volume": "39",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "475",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 338",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 338",
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
    "date_created": "2026-07-07T13:25:41Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:25:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:25:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:25:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:25:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "g-m-leasing-corp-v-united-states--109579",
      "to_record_id": "G. M. Leasing Corp. v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — G. M. Leasing Corp. v. United States

```
<opinion type="majority">
<author id="b490-7">Mr. Justice Blackmun</author>
<p id="AUy3">delivered the opinion of the Court.</p>
<p id="b490-8">We granted certiorari in this case, <span class="citation multiple-matches"><a href="/c/U.%20S./423/1031/">423 U. S. 1031</a></span> (1975), limited to the Fourth Amendment issue arising in the context of seizures of property in partial satisfaction of income tax assessments.<footnotemark>1</footnotemark></p>
<p id="b490-9">I</p>
<p id="b490-10">Petitioner G. M. Leasing Corp. is a Utah corporation organized in April 1972; among its stated business purposes is the leasing of automobiles. George I. Norman, Jr., although apparently not an incorporator, officer, or director of petitioner, was its general manager.</p>
<p id="b490-11">In 1971 Norman was tried and convicted in the United States District Court for the District of Colorado on two counts of aiding and abetting a misapplication of funds from a federally insured bank, in violation of 18 U. S. C. § § 2 and 656. He was sentenced to two concurrent two-year terms of imprisonment. On appeal, his conviction was affirmed. <em>United States </em>v. <em>Cooper, </em><span class="citation" data-id="304880"><a href="/opinion/304880/united-states-v-donald-s-cooper/#651" aria-description="Citation for case: United States v. Donald S. Cooper">464 F. 2d 648, 651-652</a></span> (CA10 1972). This Court denied certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./409/1107/">409 U. S. 1107</a></span> (1973).</p>
<p id="b491-4"><page-number citation-index="1" label="341">*341</page-number>Norman and his wife, on November 15, 1971,<footnotemark>2</footnotemark> filed a joint income tax Form 1040 for the calendar year 1970 on which, apart from their names, address, social security numbers, occupations, and dependents, they indicated only that their tax for that year, “ [estimated,” was $280,000. The sum of $289,800 was transmitted when the form was filed and was placed by the Internal Revenue Service in a suspense account for future credit. Apart from the naked figure of estimated tax, the return contained no information as to income or deductions. App. 94.</p>
<p id="b491-5">The Normans also sought and were granted an extension of time within which to file their return for the calendar year 1971. A check for $405,125 was given to the Service on April 15, 1972, for application on their 1971 tax. This check evidently was dishonored. Although further extensions of time were granted, neither of the Normans ever filed a 1971 return.</p>
<p id="b491-6">In October 1972, after Norman’s conviction was affirmed by the Tenth Circuit, the Service assigned the Norman account for 1970 and 1971 to Agent P. J. Clayton for investigation. Mr. Clayton, however, took no immediate action. <em>Id., </em>at 66; Tr. of Oral Arg. 24 — 25.</p>
<p id="b491-7">In March 1973, after Norman’s petition for a writ of certiorari had been denied, and after his petition for rehearing had also been denied, <span class="citation multiple-matches"><a href="/c/U.%20S./410/959/">410 U. S. 959</a></span> (1973), he surrendered to the United States Marshal for the serving of his sentence. By a ruse, however, he immediately disappeared. Tr. of Oral Arg. 6. Norman thereupon became a fugitive from justice; he was still one at the time of the oral argument. App. 15; Brief for Petitioners 5; Tr. of Oral Arg. 5-6.</p>
<p id="b491-8">Upon Norman’s becoming a fugitive, the Service activated its investigation. On March 19, it determined deficiencies in Norman’s income tax liability for 1970 and 1971 in the <page-number citation-index="1" label="342">*342</page-number>amounts of $406,099.34 and $545,310.59, respectively.<footnotemark>3</footnotemark> App. 95. These were based solely on information from third parties concerning the amount of stock sales Norman made through various brokerage houses. <em>Id., </em>at 30, 67.<footnotemark>4</footnotemark> Because of Norman’s failure to file appropriate returns and because of his fugitive status, collection of the taxes as so determined was regarded by the Service as in jeopardy; the deficiencies, therefore, were assessed forthwith pursuant to the authority granted by § 6861 (a) of the Internal Revenue Code of 1954, <span class="citation no-link">26 U. S. C. § 6861</span> (a).<footnotemark>5</footnotemark></p>
<p id="b492-5">The following day revenue agents called at the Norman residence in Salt Lake City to endeavor to collect the taxes. <page-number citation-index="1" label="343">*343</page-number>Mrs. Norman answered the door. The agents informed her of the jeopardy assessments and demanded payment. No payment was forthcoming, and Mrs. Norman suggested that the agents get in touch with her attorney. App. 56. Thereafter, pursuant to their authority under § 6331 of the Code, the agents filed notice of tax liens with the Salt Lake County Recorder’s Office and levied on a bank account of Norman. App. 95, 58.</p>
<p id="b493-5">While the agents were at the Norman residence, they observed automobiles parked in the driveway. Later, upon checking with the Utah Motor Vehicle Division, they learned that these vehicles were registered in the name of petitioner or in the name of another corporation owned by Norman, and that no automobile was registered in Norman’s name or in that of his wife. <em>Id., </em>at' 73-74. They also learned that petitioner had no license to conduct business within Salt Lake County and had no telephone listing. <em>Id., </em>at 74. It was further ascertained that, pursuant to the request of the Utah Department of Employment Security, petitioner had filed a Status Report. That report described the corporation’s principal business activity as “Leasing Luxury Automobiles, Boats, etc.” It recited that the corporation’s “average number of employees” was zero and that it had paid no wages while it was in existence during the last three quarters of 1972 or thus far in 1973. <em>Id., </em>at 91-92. On its Utah Sales and Use Tax Return for the second quarter of 1972, the corporation reported no sales. <em>Id., </em>at 93. The agents regarded the automobiles seen at the Norman residence as “show” or “collector” cars and not the type “that would normally be used in a leasing business.” <em>Id., </em>at 74.</p>
<p id="b493-6">All these facts suggested to the agents that petitioner corporation was not engaged in any business activity but, instead, was Norman’s alter ego and a repository of at least some of his personal assets. The agents consulted with the Service’s Regional Counsel. With his concurrence, <page-number citation-index="1" label="344">*344</page-number>the conclusion was drawn that the assets of the corporation actually belonged to Norman. Accordingly, the decision was made to levy upon and seize automobiles titled in petitioner’s name in partial satisfaction of the assessments against Norman. <em>Id., </em>at 75-76.</p>
<p id="b494-5">On or about March 21, two days after the jeopardy assessments, revenue officers, without a warrant, seized several automobiles. Among them were a 1972 Stutz, a Rolls Royce Phantom V, a 1930 Rolls Royce Phantom I, two 1971 Stutzes, and a Jaguar. Three were taken at two different locations in Salt Lake City; two at the Century Plaza parking lot in Los Angeles, Cal.; and one near Norman’s residence in Salt Lake City. <em>Id., </em>at 121, 129; Tr. of Oral Arg. 13-14. None of the ears was on property in which petitioner had an interest. All were registered in petitioner’s name. App. 75-76. The officers left a Chevrolet and 'a station wagon for the personal use of Mrs. Norman and her family.<footnotemark>6</footnotemark> <em>Id., a.t 58.</em></p>
<p id="b494-6">Also on March 21, revenue officers went to petitioner’s office'in Salt Lake County to levy on property subject to seizure, including the building itself. <em>Id., </em>at 19. They had information that one, and possibly two, luxury automobiles might be there. Upon learning that a car was in the garage on the premises, they telephoned their superior, Bert Apple-gate, and asked him to come out to assist. <em>Id., </em>at 77-79. The premises consisted of a cottage-type building and the garage. When Applegate arrived, a locksmith was there. He already had removed the lock from the garage door <page-number citation-index="1" label="345">*345</page-number>at the direction of the officers. A Stutz automobile was inside. The locksmith also had removed the lock on the cottage’s rear door. <em>Id., </em>at 80-81.</p>
<p id="b495-5">Applegate entered the cottage. He observed that its outward appearance was such that it could be a residence. He noticed a kitchen. He instructed the officers not to proceed with the seizure of any property there until the status of the cottage could be confirmed.<footnotemark>7</footnotemark> <em>Id., </em>at 81, 23-24. The officers then left the cottage without taking anything, and its lock was replaced. <em>Id., </em>at 82.</p>
<p id="b495-6">While the officers were in the cottage, Norman’s son, George I. Norman III, age 19, and listed as a dependent on the 1970 Form 1040, appeared. He told the officers that the Stutz belonged to the petitioner corporation, and not to Norman. <em>Id., </em>at 80, 34. He testified that he was living at the cottage “as security.” <em>Id., </em>at 34. He was asked to provide evidence as to the car’s ownership. A decision was made not to seize the automobile at that 'time.</p>
<p id="b495-7">Information then came to Applegate, primarily from a Mr. Redd who was a contractor for Norman, that the cottage was a place of business and not a residence. <em>Id., </em>at 79. In addition, there was activity at the cottage that night; the lights were on and boxes were being moved. The next morning the Stutz was not in the garage.<footnotemark>8</footnotemark> <em>Id., </em>at 83. Sometime during the next two days, a decision was made to seize the cottage, its furnishings and any other assets there.<footnotemark>9</footnotemark> On <page-number citation-index="1" label="346">*346</page-number>March 23,<footnotemark>10</footnotemark> agents, acting without a warrant, and with the assistance of locksmiths and the equipment of a private van and storage firm, entered the cottage and removed its remaining contents, including furnishings and books and records. An inventory was made of the property so seized. The agents hoped to examine the books and records to see if they contained’stock certificates or information concerning the location of other assets. The Regional Counsel, however, instructed them to pack the books and records, seal the boxes, and remove them to a safe storage place. <em>Id., </em>at 83-88.</p>
<p id="b496-5">In May, petitioner corporation instituted this suit. JBy its amended complaint it asserted a claim for wrongful levy, with a request for the return of the automobiles; a claim for suppression of all evidence obtained from the seized documents; and a claim against the agents for damages. <em>Id., </em>at 105-112. It alleged that the assessments were arbitrary and capricious, that petitioner was not an alter ego of Norman, and that the levy upon its premises and the contents violated the Fourth Amendment. <em>Ibid.</em></p>
<p id="b496-6">Shortly thereafter, the Service returned to the cottage the originals of the records and documents that had been seized. In the meantime, however, they had been photocopied.<footnotemark>11</footnotemark> By a second amendment to petitioner’s complaint, <em>id., </em>at 124, punitive damages, among other relief, were requested.</p>
<p id="b496-7">Norman’s son filed a complaint in intervention, <em>id., </em>at 112-117, alleging essentially the same facts and requesting <page-number citation-index="1" label="347">*347</page-number>similar relief. The District Court allowed his intervention. The Government then filed a counterclaim seeking foreclosure of the tax liens against the property held in petitioner’s name. <em>Id., </em>at 127-134.</p>
<p id="b497-5">At the ensuing trial before the court without a jury there was testimony that Norman himself originally held title to some of the automobiles registered in petitioner’s name, <em>id., </em>at 37; that petitioner had no employees and did not lease any cars, <em>id., </em>at 37, 39; that petitioner’s only assets were luxury or vintage model automobiles; that the cars had not been transferred to it until at or near the end of 1972; and that petitioner never issued any stock, held any director’s meetings, or engaged in any business.<footnotemark>12</footnotemark> <em>Id., </em>at 43-45.</p>
<p id="b497-6">The District Court entered judgment for petitioner and for the intervenor. It found that the premises in question were the offices of petitioner and the residence of the intervenor; that the revenue-officer defendants had no&gt; search warrant; that they forcibly entered the premises on March 23 and again on March 25;<footnotemark>13</footnotemark> that they made the entry, search, and seizure “knowing full well that they were violating the rights” of petitioner, the intervenor, “and others”; that Agent Clayton committed the entry “maliciously”; that the defendants returned the books and records that had been seized but photocopied them and retained the photocopies; that the defendants levied upon and seized all the assets of petitioner, including seven automobiles and a bank account; that they disposed of two of the automobiles and stored the others in Salt Lake City; that the assessments of taxes, penalties, and interest against Norman and his wife for 1970 and 1971 were erroneous; that Norman and his wife had no liability for federal income tax, penalties, <page-number citation-index="1" label="348">*348</page-number>or interest for those years; that petitioner had “engaged in substantial business activity in preparation for its business purpose of leasing automobiles”; that it was not controlled solely by Norman or his wife; that it was not an alter ego of Norman or his wife; and that it was not their nominee. The court concluded that the revenue-officer defendants committed an illegal search and seizure of petitioner’s offices and the intervenor’s residence, in violation of the Fourth Amendment; that the photocopies of the seized books and records in the possession of the Service should be destroyed because am&amp;.use of them would be illegal; that petitioner and the intervenor were entitled to general and punitive damages in amounts to be determined; that the Government’s counterclaim should be dismissed with prejudice; that the Service should return all the seized assets of petitioner and of the intervenor; and that judgment should be awarded against the United States in favor of petitioner for the value of the two automobiles that had been sold. <em>Id., </em>at 136-142. Judgment, including injunctive relief for the return of the automobiles and the books and records, and for the destruction of the photocopies, was entered accordingly. <em>Id., </em>at 142-144.</p>
<p id="b498-5">The Court of Appeals, for the most part, reversed. <span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,...">514 F. 2d 935</a></span> (CA10 1975). It ruled that the evidence conclusively established that petitioner was Norman’s alter ego so that its assets could be seized to satisfy Norman’s income tax liability; that the District Court’s finding to the contrary was clearly erroneous; that petitioner had not sustained its burden of proving the assessments to be erroneous; and that the trial court erred in invalidating, the assessments and in dismissing the Government’s counterclaim. In regard to the claim of illegal search and seizures, the Court of Appeals held:</p>
<blockquote id="b498-6">“The refusal to pay authorized appellants to collect the tax by levy, and this included the power of 'seizure by any means.’ Thus appellants were acting pursuant to <page-number citation-index="1" label="349">*349</page-number>statute and did not commit an illegal search. The trial court’s order returning the assets and suppressing the documents is improper.” (Footnote omitted.) <span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/#941" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,..."><em>Id., </em>at 941</a></span>.</blockquote>
<p id="b499-5">The c(3urt also ruled that there was no evidence to support the trial court’s finding that Clayton’s participation “was of a malicious character.” <em><span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,...">Ibid.</a></span> </em>In accord with a concession by the Government, the Court of Appeals affirmed the trial court’s judgment insofar as it ordered the return of certain shares of stock to the intervenor.<footnotemark>14</footnotemark></p>
<p id="b499-6">II</p>
<p id="b499-7">A. Section 6331 (a) of the 1954 Code authorizes the Secretary or his delegate to collect taxes “by levy upon all property and rights to property” belonging to a person who “neglects or refuses to pay” any tax “or on which there is a lien ... for the payment of such tax.”<footnotemark>15</footnotemark> Section 6331 (b), <page-number citation-index="1" label="350">*350</page-number>and §7701 (a) (21) as well, define “levy” as including “the power of distraint and seizure by any means.” Both real estate and personal property, tangible and intangible, are subject to levy. Levy upon tangible property normally is effected by service of forms of levy or notice of levy and physical seizure of the property. Where that is not feasible, the property is posted or tagged. Because intangible property is not susceptible of physical seizure, posting, or tagging, levy upon it is effected by serving the appropriate form upon the party holding the property or rights to property. See <span class="citation no-link">Treas. Reg. § 301.6331-1</span> (a)(1), <span class="citation no-link">26 CFR § 301.6331-1</span> (a)(1) (1976). See also <em>Phelps </em>v. <em>United States, </em><span class="citation" data-id="109249"><a href="/opinion/109249/phelps-v-united-states/#335" aria-description="Citation for case: Phelps v. United States">421 U. S. 330, 335-337</a></span> (1975). And the Court has recognized that compulsion on the part of the Service occasionally is required in the enforcement of the revenue laws. See <em>United States </em>v. <em>Bisceglia, </em><span class="citation" data-id="9425992"><a href="/opinion/109190/united-states-v-bisceglia/#145" aria-description="Citation for case: United States v. Bisceglia">420 U. S. 141, 145</a></span> (1975). Indeed, one may readily acknowledge that the existence of the levy power is an essential part of our self-assessment tax system and that it enhances voluntary compliance in the collection of taxes that this Court has described as “the life-blood of government, and their prompt and certain availability an imperious need.” <em>Bull </em>v. <em>United States, </em><span class="citation" data-id="102455"><a href="/opinion/102455/bull-v-united-states/#259" aria-description="Citation for case: Bull v. United States">295 U. S. 247, 259</a></span> (1935).</p>
<p id="b500-4">Under § 6321 of the Code,<footnotemark>16</footnotemark> the assessments against Norman were a lien in favor of the United States upon all property <page-number citation-index="1" label="351">*351</page-number>belonging to Norman. If petitioner was Norman’s alter ego, it had no countervailing effect for purposes of his federal income tax. <em>Griffiths </em>v. <em>Commissioner, </em><span class="citation" data-id="103261"><a href="/opinion/103261/griffiths-v-commissioner/" aria-description="Citation for case: Griffiths v. Commissioner">308 U. S. 355</a></span> (1939); <em>Higgins </em>v. <em>Smith, </em><span class="citation" data-id="9419068"><a href="/opinion/103275/higgins-v-smith/#476" aria-description="Citation for case: Higgins v. Smith">308 U. S. 473, 476</a></span> (1940). It would then follow that the Service could properly regard petitioner’s assets as Norman’s property subject to the lien under § 6321, and the Service would be empowered, under § 6331, to levy upon assets held in petitioner’s name in satisfaction of Norman’s income tax liability. See <em>United States </em>v. <em>Plastic Electro-Finishing Corp., </em><span class="citation" data-id="1969224"><a href="/opinion/1969224/united-states-v-plastic-electro-finishing-corporation/#333" aria-description="Citation for case: United States v. Plastic Electro-Finishing Corporation">313 F. Supp. 330, 333-334</a></span> (EDNY 1970), aff’d, <span class="citation no-link">71-1 USTC ¶9421</span> (CA2 1971).</p>
<p id="b501-5">B. Our grant of certiorari was limited to the Fourth Amendment issue, and we declined to review petitioner’s and Norman’s son’s claims that the assessments and levies should have been voided and that petitioner was not Norman’s alter ego. Pet. for Cert. 2, 3.<footnotemark>17</footnotemark> We therefore approach this case accepting the Court of Appeals’ determinations that the assessments and levies were valid and that petitioner was Norman’s alter ego. Those facts necessarily establish probable cause to believe that assets held by petitioner were properly subject to seizure in satisfaction of the assessments. Petitioner does not claim that' there was no probable cause to believe that the automobiles were held by petitioner, nor does it claim that there was no probable cause to believe that its offices would contain other seizable goods. There being probable cause for the search and seizures, the only questions before the Court are whether warrants were required to malee “reasonable” either the seizures of the cars or the entry into and seizure of goods in the cottage.</p>
<p id="b501-6">C. The seizures of the automobiles in this case took place on public streets, parking lots, or other open places, and did not involve any invasion of privacy. In <em>Murray’s Lessee </em>v. <page-number citation-index="1" label="352">*352</page-number><em>Hoboken Land &amp; Improv. Co., </em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">18 How. 272</a></span> (1856), this Court held that a judicial warrant is not required for the seizure of a debtor’s land in satisfaction of a claim of the United States. The seizure in <em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">Murray’s Lessee</a></span> </em>was made through a transfer of title which did not involve an invasion of privacy. The warrantless seizures of the automobiles in this case are governed by the same principles and therefore were not unconstitutional. See also <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924) (liquor seized in open field).<footnotemark>18</footnotemark></p>
<p id="b502-5">D. The seizure of the books and records, however, involved intrusion into the privacy of petitioner’s offices. Significantly, the Court has said:</p>
<blockquote id="b502-6">“[0]ne governing principle, justified by history and by current experience, has consistently been followed: except in certain carefully defined classes of cases, a search <page-number citation-index="1" label="353">*353</page-number>of private property without proper consent is 'unreasonable’ unless it has been authorized by a valid search warrant.” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span> (1967).</blockquote>
<p id="b503-5">See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span>, 45A-455 (1971); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#512" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 512</a></span> (White, J., concurring and dissenting) ; <em>Stoner </em>v. <em>California, </em><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span> (1964); <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span> (1951); <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948); <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> (1925).</p>
<p id="b503-6">The respondents do not contend that business premises are not protected by the Fourth Amendment. Such a proposition could not be defended in light of this Court’s clear holdings to the contrary. <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967); <em>Go-Bart Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931); <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920). Nor can it be claimed that corporations are without some Fourth Amendment rights. <em>Go-Bart Co. </em>v. <em>United States, supra; Silverthorne Lumber Co. </em>v. <em>United States, supra; Oklahoma Press Pub. Co. </em>v. <em>Walling, </em><span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/#205" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186, 205-206</a></span> (1946); <em>Hale </em>v. <em>Henkel, </em><span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#75" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 75-76</a></span> (1906). Cf. <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21</a></span> (1974); <em>Federal Trade Comm’n </em>v. <em>American Tobacco Co., </em><span class="citation" data-id="100375"><a href="/opinion/100375/federal-trade-commission-v-american-tobacco-co/#305" aria-description="Citation for case: Federal Trade Commission v. American Tobacco Co.">264 U. S. 298, 305-306</a></span> (1924); <em>Wilson </em>v. <em>United States, </em><span class="citation" data-id="1293085"><a href="/opinion/1293085/wilson-v-united-states/#375" aria-description="Citation for case: Wilson v. United States">221 U. S. 361, 375-376</a></span> (1911); <em>Consolidated Rendering Co. </em>v. <em>Vermont, </em><span class="citation" data-id="96746"><a href="/opinion/96746/consolidated-rendering-co-v-vermont/#553" aria-description="Citation for case: Consolidated Rendering Co. v. Vermont">207 U. S. 541, 553-554</a></span> (1908).</p>
<p id="b503-7">The Court, of course, has recognized that a business, by its special nature and voluntary existence, may open itself to intrusions that would not be permissible in a purely private context. Thus, in <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972), a warrantless search of a locked storeroom during business hours, pursuant to the inspection procedure authorized by the Gun Control Act of 1968, <span class="citation no-link">18 U. S. C. § 923</span> (g), was upheld:</p>
<blockquote id="b503-8">“When a dealer chooses to engage in this pervasively <page-number citation-index="1" label="354">*354</page-number>regulated business and to accept a federal license, he does so with the knowledge that his business records, firearms, and ammunition will be subject to effective inspection.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</blockquote>
<p id="b504-5">See also <em>Colonnade Catering Corp. </em>v. <em>United </em>States, <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970) (Congress has broad authority to fashion standards of reasonableness for searches and seizures to regulate the liquor industry but failed in that case to authorize a warrantless search).</p>
<p id="b504-6">In the present case, however, the intrusion into petitioner’s privacy was not based on the nature of its business, its license, or any regulation of its activities. Rather, the intrusion is claimed to be justified on the ground that petitioner’s assets were seizable to satisfy tax assessments. This involves nothing more than the normal enforcement of the tax laws, and we find no justification for treating petitioner differently in these circumstances simply because it is a corporation.</p>
<p id="b504-7">The respondents argue that there is a broad exception to the Fourth Amendment that allows warrantless intrusions into privacy in the furtherance of enforcement of the tax laws. We recognize that the “Power to lay and collect Taxes” is a specifically enunciated power of the Federal Government, Const., Art. I, § 8, cl. 1, and that the First Congress, which proposed the adoption of the Bill of Rights, also provided that certain taxes could be “levied by distress and sale of goods of the person or persons refusing or neglecting to pay.” Act of Mar. 3, 1791, c. 15, § 23, <span class="citation no-link">1 Stat. 204</span>. This, however, relates to warrantless seizures rather than to warrantless searches. It is one thing to seize without a warrant property resting in an open area or seizable by levy without an intrusion into privacy, and it is quite another thing to effect a warrantless seizure of property, even that owned by a corporation, situated on private premises to which access is not otherwise available for the seizing officer.</p>
<p id="b505-4"><page-number citation-index="1" label="355">*355</page-number>Indeed, one of the primary evils intended to be eliminated by the Fourth Amendment was the massive intrusion on privacy undertaken in the collection of taxes pursuant to general warrants and writs of assistance.<footnotemark>19</footnotemark> As Madison argued, urging the adoption of a Bill of Rights to restrain the Federal Government:</p>
<blockquote id="b505-5">“The General Government has a right to pass all laws which shall be necessary to collect its revenue; the means for enforcing the collection are within the direction of the Legislature: may not general warrants be considered necessary for this purpose, as well as for some purposes which it was supposed at the framing of their constitutions the State Governments had in view? If there was reason for restraining the State Governments from exercising this power, there is like reason for restraining the Federal Government.” 1 Annals of Cong. 438 (1834 ed.).</blockquote>
<p id="b505-6">The respondents urge that the history of the common law in England and the laws in several States prior to the adoption of the Bill of Rights support the view that the Fourth Amendment was not intended to cover intrusions into privacy in the enforcement of the tax laws. We do not find in the cited materials anything approaching the clear evidence that would be required to create so great an exception to the Fourth Amendment’s protections against warrantless intrusions into privacy.</p>
<p id="b505-7">The respondents also rely upon certain dicta in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886) <footnotemark>20</footnotemark> (subpoena of private <page-number citation-index="1" label="356">*356</page-number>papers impermissible). But see <em>Fisher </em>v. <em>United States, 425 </em>U. S. 391, 408-411 (1976), and <em>Andresen </em>v. <em>Maryland, </em><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#471" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463, 471-472</a></span> (1976). We do not find in <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span> </em>any direct holding that the warrant protections of the Fourth Amendment do not apply to invasions of privacy in furtherance of tax collection. Insofar as language in <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span> </em>might be read so to state, we decline to follow those dicta into rejection of the basic governing principle that has shaped Fourth Amendment law.</p>
<p id="b506-5">Finally, the respondents argue that warrantless searches are justified by congressional enactment, as were the searches in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span> </em>and <em>Colonnade. </em>The statute, § 6331 (b) of the Code, <span class="citation no-link">26 U. S. C. § 6331</span> (b), authorizes “distraint and seizure by any means.” See n. 15, <em>supra. </em>Read narrowly, it au<page-number citation-index="1" label="357">*357</page-number>thorizes the use of every means to deprive the taxpayer of use, enjoyment, or title to property (e. <em>g., </em>transferring title, asportation, immobilization). It does not refer to warrant-less intrusions into privacy. The respondents, however, would have us read the statute to authorize such warrant-less intrusions. They assert that a statute of that kind is permissible in light of the considerations discussed in <em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span> </em>and <em>See. </em>Examination of the statute shows that quite the opposite is true.</p>
<p id="b507-5">The respondents recognize that one of the Court’s critical concerns in <em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span> </em>and <em>See </em>was the discretion of the seizing officers. Brief for Respondents 66. Yet § 6331 clearly gives the Secretary or his delegate discretion as to what property to seize. If more than one location is involved, the Secretary will choose which dwelling will be invaded. If property is to be found both in public places and in private areas, the Secretary may choose which to seize. This hardly can be called a restraint on discretion. The respondents also recognize the concern with the existence of questions of disputed fact. They argue that in the seizure situation there are no such questions; yet in the present case the agents’ confusion over whether the premises were an office or a residence demonstrates the contrary.</p>
<p id="b507-6">The respondents assert that the burden on the Government of obtaining a warrant is a relevant factor. Brief for Respondents 67-68. They suggest that the burden is great here because the Government is dealing with persons who may attempt to put their property beyond reach. Yet the statute authorizes distraint and seizure whenever a taxpayer <em>neglects </em>or refuses to pay his tax, and regardless of any indication of risk of concealment. The statute simply does not focus on situations involving a need for rapid action.</p>
<p id="b507-7">The respondents argue that the interest in the collection of taxes is such as to bring this case within the reasoning of <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span> </em>and <em>Colonnade. </em>Those cases involved voluntary <page-number citation-index="1" label="358">*358</page-number>participation in a highly regulated activity. Section 6331, however, covers all defaults on all taxes, and we are unwilling to hold that the mere interest in the collection of taxes is sufficient to justify a statute declaring <em>per se </em>exempt from the warrant requirement every intrusion into privacy made in furtherance of any tax seizure.</p>
<p id="b508-5">The respondents suggest that the privacy interest in business premises is less than that in a private home., Even if correct, the assertion is irrelevant with respect to the intent of the statute, for the statute makes no distinction between business properties and dwelling areas. If it authorizes entries at all, it authorizes entries into both business premises and private homes.</p>
<p id="b508-6">The respondents offer no legislative history in support of their reading of § 6331, and to give the statute that reading would call its constitutionality into serious question. We therefore decline to read it as giving <em>carte blanche </em>for warrantless invasions of privacy. Rather, we give it its natural reading, namely, as an authorization for all forms of <em>seizure, </em>but as silent on the subject of intrusions into privacy.</p>
<p id="b508-7">The intrusion into petitioner’s office is therefore governed by the normal Fourth Amendment rule that “except in certain carefully defined classes of cases, a search of private property without proper consent is 'unreasonable’ unless it has been authorized by a valid search warrant.” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528-529</a></span>.</p>
<p id="b508-8">As an alternative to their argument that a new exception to the warrant requirement should be recognized, the respondents assert that the facts of this case bring it within the “exigent circumstances” exception to the warrant requirement.<footnotemark>21</footnotemark> The agents’ own actions, however, in their <page-number citation-index="1" label="359">*359</page-number>delay for two days following their first entry, and for more than one day following the observation of materials being moved from the office, before they made the entry during which they seized the records, are sufficient to support the District Court’s implicit finding that there were no exigent circumstances in this case.</p>
<p id="b509-5">We therefore conclude that the warrantless entry into petitioner’s office was in violation of the commands of the Fourth Amendment.</p>
<p id="b509-6">Ill</p>
<p id="b509-7">This takes us to the issue of remedy. Specifically, petitioner, by its second amended complaint, prayed for (a) the return of the photocopies of the books and records; (b) the return of the automobiles; (c) a declaration that petitioner is not the alter ego of Norman or of Mrs. Norman; (d) the suppression of all evidence obtained from the books And records; (e) the suppression of the automobiles as evidence; (f) the release of all levies; and (g) general and punitive damages against the individual defendant-agents. App, 123-124.</p>
<p id="b509-8">The alter ego issue, as has been noted, was denied review. The books and' records were returned, and the photocopies concededly have been destroyed; that claim, thus, is moot. We have decided the issue of the legality of the seizure of the automobiles adversely to petitioner. The suppression issue, as to the books and records, obviously is premature and may be considered if and when proceedings arise in which the Government seeks to use the documents or information obtained from them. See <em>Meister </em>v. <em>United </em>States, <span class="citation" data-id="8879056"><a href="/opinion/8892725/meister-v-united-states/#269" aria-description="Citation for case: Meister v. United States">397 F. 2d 268, 269</a></span> (CA3 1968); <em>Hill </em>v. <em>United States, </em><span class="citation multiple-matches"><a href="/c/F.%202d/346/175/">346 F. 2d 175</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./382/956/">382 U. S. 956</a></span> (1965). And the irreparable injury required to support a motion to suppress, under Fed. Rule Crim. Proc. 41 (e), on equitable grounds in advance of any proceedings, has not been dem<page-number citation-index="1" label="360">*360</page-number>onstrated. <em>Hunsucker </em>v. <em>Phinney, </em><span class="citation" data-id="9460619"><a href="/opinion/319298/louis-sager-hunsucker-jr-v-robert-l-phinney-district-director-of/#34" aria-description="Citation for case: Louis Sager Hunsucker, Jr. v. Robert L. Phinney, District...">497 F. 2d 29, 34</a></span> (CA5 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/927/">420 U. S. 927</a></span> (1975).</p>
<p id="b510-5">This leaves only the issue of damages against the individual agents. The District Court found that Agent Clayton “maliciously committed said forced entry, and search and seizure,” App. 138, and concluded that he and other individual defendants acted “knowing full well that they were violating the rights of” petitioner. <em>Ibid. </em>It concluded that petitioner was entitled to judgment for those actions. The Court of Appeals, in the context of its holding that the entry and search were not illegal, ruled that the finding of maliciousness on the part of Clayton was unsupported by any evidence in the record and was clearly erroneous. <span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/#940" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,...">514 F. 2d, at 940-941</a></span>. It also reversed the judgment awarding petitioner damages. <span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/#942" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,..."><em>Id., </em>at 942</a></span>.</p>
<p id="b510-6">We have held above, however, that a warrant should have been obtained, under the circumstances of this case, before the forcible entry was effected. This brings into focus and for consideration this Court’s decision in <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971), and the reservation there of the immunity question. The Government suggests that, assuming a violation of the Fourth Amendment by the agents, petitioner is not entitled to money damages if the agents acted in good faith; that good faith was supported by the “apparent fact” that the agents’ conduct was in conformity with standard Service procedures based upon <em>Murray’s Lessee, supra; </em>and that the record justifies the conclusion that the agents acted in good faith. That may well be, but we conclude that this aspect of the facts, the existence of proof of any injury to petitioner resulting from the entry and the temporary seizure of the books and records, and the immunity issue all should be addressed in the first instance by the Court of Appeals and, if it so directs, by the District Court.</p>
<p id="b511-4"><page-number citation-index="1" label="361">*361</page-number>The judgment of the Court of Appeals is therefore affirmed in part and reversed in part, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b511-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b490-12"> The Fourth Amendment reads:</p>
<blockquote id="b490-13">“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
</footnote>
<footnote label="2">
<p id="b491-9"> Four extensions of time for filing had been granted. App. 99.</p>
</footnote>
<footnote label="3">
<p id="b492-6"> At the same time, the Service determined deficiencies in Mrs. Norman’s income tax liability for 1970 and 1971 in the amounts of $69,265.04 and $84,873.50, respectively. <em>Id., </em>at 96. Those deficiencies are not at issue in this case.</p>
</footnote>
<footnote label="4">
<p id="b492-7"> Agent Clayton, called as a witness for the petitioner in the present case, on cross-examination answered “No” to the question whether he was “able to get any cooperation at all” from Mr. Norman. <em>Id., </em>at 30. When later called as a witness on behalf of the respondents, Clayton also gave a negative answer to the question whether he had received “any information from the taxpayer or his accountant or representative.” <em>Id., </em>at 66.</p>
<p id="b492-8">Petitioner protests any adverse inference that might flow from this testimony and asserts that there is no evidence that Clayton requested assistance from Norman or his representatives who had filed powers of attorney with the Service. Reply Brief for Petitioners 3-4. Counsel for respondents at oral argument stated: “I want to correct any wrong implication if there is one, that they received no cooperation from Mr. Norman. . . . [N]obody had asked him prior to that time [his becoming a fugitive] for cooperation.” Tr. of Oral Arg. 25.</p>
</footnote>
<footnote label="5">
<p id="b492-9"> Jeopardy assessments of the determined deficiencies in Mrs. Norman’s taxes were also made on March 19. App. 97.</p>
<p id="b492-10">The notice which is required after jeopardy assessment by § 6861 (b) of the Code enables the taxpayer to file a petition with the United States Tax Court for a redetermination of the deficiency. See <em>Laing </em>v. <em>United States, </em><span class="citation" data-id="9426233"><a href="/opinion/109340/laing-v-united-states/" aria-description="Citation for case: Laing v. United States">423 U. S. 161</a></span> (1976). A timely notice was sent to Norman, and a petition was filed on his behalf with the Tax Court. His case awaits trial there (Docket No. 6000-73).</p>
</footnote>
<footnote label="6">
<p id="b494-7"> The two automobiles seized in Los Angeles were a two-door tan Stutz, valued at $30,000, and a four-door burgundy Stutz, valued at $100,000. They were financed by loans from Murray First Thrift. Following the levy, Murray foreclosed its own liens and arranged with Norman’s attorney for the sale of the automobiles. App. 33, 122. It appears that the Government did not participate in those transactions and received no portion of the proceeds of the sales.</p>
</footnote>
<footnote label="7">
<p id="b495-8"> The Internal Revenue Service Manual, ¶ 5341.1, instructs that if an occupant of a private residence denies a revenue officer permission to enter, the officer should not attempt entry by force.</p>
</footnote>
<footnote label="8">
<p id="b495-9"> The Service later found this particular automobile at another location. App. 83. It had been moved by Norman’s son after the revenue agents had left on March 21. <em>Id., </em>at 34.</p>
</footnote>
<footnote label="9">
<p id="b495-10"> Title to the cottage was in the name of Real Estate, Inc., a corporation the Service determined to be the alter ego of Mrs. Norman. <em>Id., </em>at 97. That corporation is not a party to the present suit and the relief petitioner requests does not include the return of the cottage.</p>
</footnote>
<footnote label="10">
<p id="b496-8"> There is some evidence in the record that this took place on March 22 rather than March 23. <em>Id., </em>at 34, 59, 77.</p>
</footnote>
<footnote label="11">
<p id="b496-9"> The respondents in their brief state that while the case was pending on appeal to the Tenth Circuit the Service voluntarily destroyed all existing photocopies of the seized books and records. Brief for Respondents 16 n. 9, 76-77, and n. 43. Petitioner concedes that the seized documents have been returned and the photocopies destroyed. Tr. of Oral Arg. <em>14r-15.</em></p>
</footnote>
<footnote label="12">
<p id="b497-7"> There was conflicting testimony as to whether stock was issued. 1 Tr. 52-53.</p>
</footnote>
<footnote label="13">
<p id="b497-8"> This date appears to be an error. See also n. 10, <em>supra.</em></p>
</footnote>
<footnote label="14">
<p id="b499-8"> This portion of the judgment of the Court of Appeals affirming the trial court is not before us. Neither is any right of the intervenor at issue here. Tr. of Oral Arg. 13.</p>
</footnote>
<footnote label="15">
<p id="b499-9"> Section 6331 reads in part:</p>
<blockquote id="b499-10">“(a) Authority of Secretary or delegate.</blockquote>
<blockquote id="b499-11">“If any person liable to pay any tax neglects or refuses to pay the same within 10 days after notice and demand, it shall be lawful for the Secretary or his delegate to collect such tax (and such further sum as shall be sufficient to cover the expenses of the levy) by levy upon all property and rights to property (except such property as is exempt under section 6334) belonging to such person or on which there is a lien provided in this chapter for the payment of such tax. ... If the Secretary or his delegate makes a finding that the collection of such tax is in jeopardy, notice and demand for immediate payment of such tax may be made by the Secretary or his delegate and, upon failure or refusal to pay such tax, collection thereof by levy shall be lawful without regard to the 10-day period provided in this section.</blockquote>
<blockquote id="b499-12">“(b) Seizure and sale of property.</blockquote>
<blockquote id="b499-13">“The term ‘levy’ as used in this title includes the power of distraint and seizure by any means. A levy shall extend only to property pos<page-number citation-index="1" label="350">*350</page-number>sessed and obligations existing at the time thereof. In any case in which the Secretary or his delegate may levy upon property or rights to property, he may seize and sell such property or rights to property (whether real or personal, tangible or intangible).”</blockquote>
</footnote>
<footnote label="16">
<p id="b500-6"> Section 6321 reads:</p>
<blockquote id="b500-7">“If any person liable to pay any tax neglects or refuses to pay the same after demand, the amount (including any interest, additional amount, addition to tax, or assessable penalty, together with any costs that may accrue in addition thereto) shall be a lien in favor of the United States upon all property and rights to property, whether real or personal, belonging to such person.”</blockquote>
</footnote>
<footnote label="17">
<p id="b501-7"> This effectuated a denial of the son’s petition for certiorari.</p>
</footnote>
<footnote label="18">
<p id="b502-7"> If additional support were needed for this result, it is found in the Court’s decisions sustaining the right of the Government to collect taxes by summary administrative proceedings. Thus, in <em>Bull </em>v. <em>United States, </em><span class="citation" data-id="102455"><a href="/opinion/102455/bull-v-united-states/#260" aria-description="Citation for case: Bull v. United States">295 U. S. 247, 260</a></span> (1935), it was stated that a tax assessment “is given the force of a judgment, and if the amount assessed is not paid when due, administrative officials may seize the debtor’s property to satisfy the debt.” See also <em>Cheatham </em>v. <em>United States, </em><span class="citation" data-id="89244"><a href="/opinion/89244/cheatham-v-united-states/#87" aria-description="Citation for case: Cheatham v. United States">92 U. S. 85, 87-90</a></span> (1876); <em>State Railroad Tax Cases, </em><span class="citation" data-id="89311"><a href="/opinion/89311/taylor-v-secor/#612" aria-description="Citation for case: Taylor v. Secor">92 U. S. 575, 612-615</a></span> (1876); <em>Graham </em>v. <em>Du Pont, </em><span class="citation" data-id="100215"><a href="/opinion/100215/graham-v-du-pont/#255" aria-description="Citation for case: Graham v. Du Pont">262 U. S. 234, 255</a></span> (1923). The rationale underlying these decisions, of course, is that the very existence of government depends upon the prompt collection of the revenues. In <em>Phillips </em>v. <em>Commissioner, </em><span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/#596" aria-description="Citation for case: Phillips v. Commissioner">283 U. S. 589, 596-597</a></span> (1931), the Court rejected a constitutional challenge to the statutory system under which taxes may be collected summarily without a pre-seizure judicial hearing. It was held that as long as there was an adequate opportunity for a post-seizure determination of the taxpayer’s rights, the statute met the requirements of due process. See <em>Commissioner </em>v. <em>Shapiro, </em><span class="citation" data-id="9426305"><a href="/opinion/109396/commissioner-v-shapiro/#630" aria-description="Citation for case: Commissioner v. Shapiro">424 U. S. 614, 630-633</a></span> (1976); <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#91" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 91-92</a></span> (1972). These cases, of course, center upon the Due Process Clause rather than the Fourth Amendment, but the constitutional analysis is similar and yields a like result. It is to be noted that the Court in <span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/#596" aria-description="Citation for case: Phillips v. Commissioner"><em>Phillips, 283 </em>U. S., at 596</a></span>, cited <em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">Murray’s Lessee</a></span> </em>with approval as a case which sustained proceedings “more summary in character” and “involving less directly the obligation of the taxpayer.”</p>
</footnote>
<footnote label="19">
<p id="b505-8"> See T. Taylor, Two Studies in Constitutional Interpretation 41 (1969); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 51-78 (1937); J. Landynski, Search and Seizure and the Supreme Court 30-42 (1966).</p>
</footnote>
<footnote label="20">
<p id="b505-9"> In <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>, </em>the Court stated:</p>
<p id="b505-10">“The search for and seizure of stolen or forfeited goods, or goods liable to duties and concealed to avoid the payment thereof, are totally different <page-number citation-index="1" label="356">*356</page-number>things from a search for and seizure of a man’s private books and papers for the purpose of obtaining information therein contained, or of using them as evidence against him.” <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S., at 623</a></span>.</p>
<p id="b506-7">The Court's concern in <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span> </em>was with establishing the impermissibility of the subpoena of papers. It was not concerned with the warrant requirement for entry into- private places. The'Court, however, did say:</p>
<p id="b506-8">“The entry upon premises, made by a sheriff or other officer of the law, for the purpose of seizing goods and chattels <em>by virtue of a judicial writ, </em>such as an attachment, a sequestration, or an execution, is not within the prohibition of the Fourth or Fifth Amendment, or any other clause of the Constitution.” <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States"><em>Id., </em>at 624</a></span> (emphasis added).</p>
<p id="b506-9">The Court was not concerned with, and therefore did not explain, whether the “judicial writ” referred to above was necessary in order to meet the warrant requirements. The opinion does describe the “obnoxious writs of assistance” against which the Fourth Amendment was designed to protect. This description gives an indication of the types of tax-enforcement actions that the Amendment’s protections were intended to reach:</p>
<p id="b506-10">“Even the act under which the obnoxious writs of assistance were issued did not go as far as this, but' only authorized the examination of ships and vessels, and persons found therein, for the purpose of finding goods prohibited to be imported or exported, or on which the duties were not paid, and to enter into and search any suspected vaults, cellars, or warehouses for such goods." (Footnote omitted.) <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States"><em>Id., </em>at 623</a></span>.</p>
</footnote>
<footnote label="21">
<p id="b508-9"> There is no claim that any"'other exception to the warrant requirement, such as “hot pursuit,” “plain view,” or “pursuant to an arrest,” is applicable here.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Gaetjens v. Winnebago County.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "c93255c2b0ed1a31", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Gaetjens v. Winnebago County"}, "payload": {"all": [{"cite": "4 F.4th 487", "page": "487", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "4"}], "display": "4 F.4th 487", "official": {"cite": "4 F.4th 487", "page": "487", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "4"}, "official_selection_present": true, "record_id": "Gaetjens v. Winnebago County"}}
{"assertion_id": "fb6184f2ed6f3068", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Gaetjens v. Winnebago County"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Gaetjens v. Winnebago County", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Gardner v. Broderick.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Gardner v. Broderick"
type: case
citation: "392 U.S. 273 (1968)"
parallel_cite: "88 S. Ct. 1913; 20 L. Ed. 2d 1082"
neutral_cite: 1968 U.S. LEXIS 1351
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-06-10
docket: 635
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gardner v. Broderick
  varies_by_point: false
  scope_note: "Good law; the Garrity companion drawing the line between firing an employee for asserting the privilege (barred) and compelling job-related answers under use immunity (permitted)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107738/gardner-v-broderick/"
  cluster_id: 107738
  opinion_id: 107738
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Key — Progeny / Refinement"
related: ["[[Garrity v. New Jersey]]", "[[Lefkowitz v. Turley]]", "[[Kalkines v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "public-employee", "garrity", "immunity-waiver"]
holding: "A public employee (here a police officer) may not be dismissed solely for refusing to waive his Fifth Amendment immunity; but he may be required to answer questions specifically, directly, and narrowly related to his official duties under a grant of use immunity, and discharged if he refuses to answer those."
lake:
  record_id: Gardner v. Broderick
  status: verified
  projected_at: 2026-07-06
---

# Gardner v. Broderick

*392 U.S. 273 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gardner, a New York City police officer, was called before a grand jury investigating police corruption. He was advised of his privilege against self-incrimination but was asked to sign a "waiver of immunity" that would have allowed his compelled testimony to be used to prosecute him. He refused to sign and was discharged from the force under a City Charter provision mandating dismissal of any officer who refuses to waive immunity. He challenged the dismissal as a penalty for exercising his Fifth Amendment privilege.

## Issue
Whether a police officer may be dismissed solely because he refused to waive his constitutional privilege against self-incrimination — that is, refused to sign a waiver of immunity — before a grand jury investigating his conduct.

## Rule
An employee may not be fired merely for asserting the privilege: "the mandate of the great privilege against self-incrimination does not tolerate the attempt, regardless of its ultimate effectiveness, to coerce a waiver of the immunity it confers on penalty of the loss of employment." — 392 U.S. at 279. ^pin-279

But the employer may compel job-related answers under immunity: "If appellant, a policeman, had refused to answer questions specifically, directly, and narrowly relating to the performance of his official duties, without being required to waive his immunity with respect to the use of his answers or the fruits thereof in a criminal prosecution of himself, . . . the privilege against self-incrimination would not have been a bar to his dismissal." — *Id.* at 278. ^pin-278

## Application
Gardner was not discharged for refusing to give an account of his official conduct under a grant of immunity; he was discharged for refusing to sign a blanket waiver that would have stripped the immunity protecting his compelled testimony from use in a criminal prosecution. Because the City conditioned his continued employment on surrendering the privilege itself — rather than on answering duty-related questions while keeping the immunity — his dismissal penalized the exercise of a constitutional right and could not stand.

## Conclusion
The dismissal was unconstitutional and was reversed. *Gardner* refines [[Garrity v. New Jersey]]: a public employer may require an officer to answer questions narrowly related to his official duties under a grant of use immunity (and discharge him for refusing), but may not fire him simply for refusing to waive that immunity.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Gardner* is good law and, with [[Lefkowitz v. Turley]], fixes the rule that the State may compel duty-related answers only under immunity, never by forcing a waiver. The federal counterpart warning is articulated in [[Kalkines v. United States]].

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Key — Progeny / Refinement*

## Sources
- *Gardner v. Broderick*, 392 U.S. 273 (1968) — https://www.courtlistener.com/opinion/107738/gardner-v-broderick/ — pinpoints: 278, 279.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0db2297c508f481a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Gardner v. Broderick"}, "payload": {"all": [{"cite": "392 U.S. 273", "page": "273", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "392"}, {"cite": "88 S. Ct. 1913", "page": "1913", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "20 L. Ed. 2d 1082", "page": "1082", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "20"}, {"cite": "1968 U.S. LEXIS 1351", "page": "1351", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1968"}], "display": "392 U.S. 273", "official": {"cite": "392 U.S. 273", "page": "273", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "392"}, "official_selection_present": true, "record_id": "Gardner v. Broderick"}}
{"assertion_id": "7ef2188c7cf8710d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-278", "record_id": "Gardner v. Broderick"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-278", "pinpoint_status": "slip-only", "quote": "If appellant, a policeman, had refused to answer questions specifically, directly, and narrowly relating to the performance of his official duties, without being required to waive his immunity with respect to the use of his answers or the fruits thereof in a criminal prosecution of himself, . . . the privilege against self-incrimination would not have been a bar to his dismissal.", "quote_fidelity": "mismatch", "record_id": "Gardner v. Broderick", "star_marker": null}}
{"assertion_id": "9d5c7cf111312b14", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-279", "record_id": "Gardner v. Broderick"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-279", "pinpoint_status": "slip-only", "quote": "that would have allowed his compelled testimony to be used to prosecute him. He refused to sign and was discharged from the force under a City Charter provision mandating dismissal of any officer who refuses to waive immunity. He challenged the dismissal as a penalty for exercising his Fifth Amendment privilege. ## Issue Whether a police officer may be dismissed solely because he refused to waive his constitutional privilege against self-incrimination — that is, refused to sign a waiver of immunity — before a grand jury investigating his conduct. ## Rule An employee may not be fired merely for asserting the privilege:", "quote_fidelity": "mismatch", "record_id": "Gardner v. Broderick", "star_marker": null}}
{"assertion_id": "cd2110d63c4d3ece", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Gardner v. Broderick"}, "payload": {"as_of_content": "1968-06-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Gardner v. Broderick", "scope_note": "Good law; the Garrity companion drawing the line between firing an employee for asserting the privilege (barred) and compelling job-related answers under use immunity (permitted).", "varies_by_point": false}}
```

### lake record — Gardner v. Broderick

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gardner v. Broderick",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gardner v. Broderick",
    "case_name_short": "Gardner",
    "case_name_full": "GARDNER v. BRODERICK, POLICE COMMISSIONER OF THE CITY OF NEW YORK, Et Al.",
    "input_case_name": "Gardner v. Broderick",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-10",
    "year": 1968,
    "docket": "635",
    "cluster_id": 107738,
    "lead_opinion_id": 107738,
    "sibling_ids": [
      107738
    ],
    "absolute_url": "/opinion/107738/gardner-v-broderick/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8970907,
        "score": 20,
        "case_name": "Gardner v. Broderick"
      },
      {
        "cluster_id": 8970362,
        "score": 20,
        "case_name": "Gardner v. Broderick"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "392 U.S. 273",
      "volume": "392",
      "reporter": "U.S.",
      "page": "273",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1913",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1913",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1082",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1082",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1351",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1351",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 273",
        "volume": "392",
        "reporter": "U.S.",
        "page": "273",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1913",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1913",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1082",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1082",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1351",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1351",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "392 U.S. 273",
    "official_selection": {
      "court_class": "scotus",
      "selected": "392 U.S. 273",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-279",
      "page": null,
      "quote": "that would have allowed his compelled testimony to be used to prosecute him. He refused to sign and was discharged from the force under a City Charter provision mandating dismissal of any officer who refuses to waive immunity. He challenged the dismissal as a penalty for exercising his Fifth Amendment privilege. ## Issue Whether a police officer may be dismissed solely because he refused to waive his constitutional privilege against self-incrimination \u2014 that is, refused to sign a waiver of immunity \u2014 before a grand jury investigating his conduct. ## Rule An employee may not be fired merely for asserting the privilege:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-278",
      "page": null,
      "quote": "If appellant, a policeman, had refused to answer questions specifically, directly, and narrowly relating to the performance of his official duties, without being required to waive his immunity with respect to the use of his answers or the fruits thereof in a criminal prosecution of himself, . . . the privilege against self-incrimination would not have been a bar to his dismissal.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gardner v. Broderick",
    "varies_by_point": false,
    "scope_note": "Good law; the Garrity companion drawing the line between firing an employee for asserting the privilege (barred) and compelling job-related answers under use immunity (permitted).",
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
        "journal_ref": "Gardner v. Broderick:lane1_negative"
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
        "journal_ref": "Gardner v. Broderick:lane1_negative"
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
        "journal_ref": "Gardner v. Broderick:lane1_negative"
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
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sher v. U.S. Department of Veterans Affairs",
          "cluster_id": 202763,
          "cite": [
            "488 F.3d 489",
            "26 I.E.R. Cas. (BNA) 243",
            "2007 U.S. App. LEXIS 12365",
            "90 Empl. Prac. Dec. (CCH) 43,067",
            "100 Fair Empl. Prac. Cas. (BNA) 1495",
            "2007 WL 1532655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re Verbois",
          "cluster_id": 1451583,
          "cite": [
            "10 S.W.3d 825",
            "2000 Tex. App. LEXIS 1263",
            "2000 WL 216934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Burlington Police Officers' Ass'n v. City of Burlington",
          "cluster_id": 8209509,
          "cite": [
            "166 Vt. 581",
            "689 A.2d 1071",
            "1996 Vt. LEXIS 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Serafino v. Hasbro, Inc.",
          "cluster_id": 196719,
          "cite": [
            "82 F.3d 515",
            "1996 U.S. App. LEXIS 8849",
            "70 Fair Empl. Prac. Cas. (BNA) 917",
            "1996 WL 187381"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. U.S. Department of the Treasury",
          "cluster_id": 6491,
          "cite": [
            "25 F.3d 237"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re Moses",
          "cluster_id": 1882575,
          "cite": [
            "792 F. Supp. 529",
            "1992 U.S. Dist. LEXIS 8685",
            "23 Bankr. Ct. Dec. (CRR) 137",
            "1992 WL 132012"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Steven M. Asherman v. Larry Meachum, Commissioner, Connecticut Department of Correction",
          "cluster_id": 578610,
          "cite": [
            "957 F.2d 978",
            "1992 U.S. App. LEXIS 2101"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Matt v. Larocca",
          "cluster_id": 5689113,
          "cite": [
            "71 N.Y.2d 154",
            "524 N.Y.S.2d 180",
            "518 N.E.2d 1172",
            "1987 N.Y. LEXIS 19884"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lonnie Benjamin and Harold Hicken v. The City of Montgomery",
          "cluster_id": 466179,
          "cite": [
            "785 F.2d 959",
            "1986 U.S. App. LEXIS 23631"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lybarger v. City of Los Angeles",
          "cluster_id": 1206957,
          "cite": [
            "710 P.2d 329",
            "40 Cal. 3d 822",
            "221 Cal. Rptr. 529",
            "1985 Cal. LEXIS 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clarence Leon Taylor, Jr. v. E. Parry Best, Lt. D.W. Smith, Paul Mills L.T. Lester",
          "cluster_id": 442995,
          "cite": [
            "746 F.2d 220",
            "1984 U.S. App. LEXIS 18178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Acceptance Company of America v. Joseph S. Bathalter, Jr.",
          "cluster_id": 417757,
          "cite": [
            "705 F.2d 924",
            "36 Fed. R. Serv. 2d 447",
            "1983 U.S. App. LEXIS 28695"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re the Claim of Altieri",
          "cluster_id": 5999349,
          "cite": [
            "92 A.D.2d 1028",
            "461 N.Y.S.2d 436",
            "1983 N.Y. App. Div. LEXIS 17429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "STATE DEPT. OF HIGHWAY SAF., ETC. v. Zimmer",
          "cluster_id": 1729887,
          "cite": [
            "398 So. 2d 463"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefkowitz v. Turley",
          "cluster_id": 108882,
          "cite": [
            "38 L. Ed. 2d 274",
            "94 S. Ct. 316",
            "414 U.S. 70",
            "1973 U.S. LEXIS 132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Couch v. United States",
          "cluster_id": 108650,
          "cite": [
            "34 L. Ed. 2d 548",
            "93 S. Ct. 611",
            "409 U.S. 322",
            "1973 U.S. LEXIS 23",
            "31 A.F.T.R.2d (RIA) 477"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kordel",
          "cluster_id": 108066,
          "cite": [
            "25 L. Ed. 2d 1",
            "90 S. Ct. 763",
            "397 U.S. 1",
            "1970 U.S. LEXIS 71",
            "13 Fed. R. Serv. 2d 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Filarsky v. Delia",
          "cluster_id": 798512,
          "cite": [
            "182 L. Ed. 2d 662",
            "132 S. Ct. 1657",
            "566 U.S. 377",
            "2012 U.S. LEXIS 3105"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brooks v. Tennessee",
          "cluster_id": 108551,
          "cite": [
            "32 L. Ed. 2d 358",
            "92 S. Ct. 1891",
            "406 U.S. 605",
            "1972 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuller v. Oregon",
          "cluster_id": 109043,
          "cite": [
            "40 L. Ed. 2d 642",
            "94 S. Ct. 2116",
            "417 U.S. 40",
            "1974 U.S. LEXIS 55"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Apfelbaum",
          "cluster_id": 110216,
          "cite": [
            "63 L. Ed. 2d 250",
            "100 S. Ct. 948",
            "445 U.S. 115",
            "1980 U.S. LEXIS 87"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bennie Lenard, Cross-Appellant v. Robert Argento & Joseph Sansone v. Village of Melrose Park",
          "cluster_id": 414191,
          "cite": [
            "699 F.2d 874"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pillsbury Co. v. Conboy",
          "cluster_id": 110821,
          "cite": [
            "74 L. Ed. 2d 430",
            "103 S. Ct. 608",
            "459 U.S. 248",
            "1983 U.S. LEXIS 124",
            "35 Fed. R. Serv. 2d 669",
            "51 U.S.L.W. 4061",
            "12 Fed. R. Serv. 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edith Libutti, Doing Business as Lion Crest Stable, a Sole Proprietorship v. United States",
          "cluster_id": 736205,
          "cite": [
            "107 F.3d 110",
            "79 A.F.T.R.2d (RIA) 1240",
            "1997 U.S. App. LEXIS 3060"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William L. O'Brien v. Robert J. Digrazia",
          "cluster_id": 340425,
          "cite": [
            "544 F.2d 543",
            "1976 U.S. App. LEXIS 6330"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Carroll",
          "cluster_id": 2285969,
          "cite": [
            "772 A.2d 45",
            "339 N.J. Super. 429"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Veal",
          "cluster_id": 73222,
          "cite": [
            "153 F.3d 1233",
            "1998 U.S. App. LEXIS 38861",
            "1998 WL 564374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vincent E. Scott v. United States",
          "cluster_id": 287590,
          "cite": [
            "419 F.2d 264",
            "135 U.S. App. D.C. 377",
            "1969 U.S. App. LEXIS 8942"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107738) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTg0NzM2MDAwMDAmcz01OTg1NDM3JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107738%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 18,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 19,
        "triage_snippet_classified": 181
      },
      "lane2_top_cited": {
        "query": "cites:(107738)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04OCZzPTY1NzM0MSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107738%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107738)",
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
    "complete_query": "cites:(107738)",
    "indexed_citing_opinions": 488,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107738,
        "count": 488,
        "count_source": "search"
      }
    ],
    "citation_count": 696,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gardner-v-broderick.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQ4MDA2NzYmcz0zMTYwMDQwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107738%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107738,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 107336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 107337,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 2591177,
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
    "date_created": "2026-07-05T05:04:47Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:06:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:06:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:12:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:06:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gardner v. Broderick

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b316-6">
  Me. Justice Fortas
 </author>
<p id="A0r">
  delivered the opinion of the Court.
 </p>
<p id="b316-7">
  Appellant brought this action in the Supreme Court of the State of New York seeking reinstatement as a New York City patrolman and back pay. He claimed he was unlawfully dismissed because he refused to waive his privilege against self-incrimination. In August 1965, pursuant to subpoena, appellant appeared before a New York County grand jury which was investigating alleged bribery and corruption of police officers in connection with unlawful gambling operations. He was advised that the grand jury proposed to examine him concerning the performance of his official duties. He was advised of his privilege against self-incrimination,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  but he was asked to sign a “waiver of immunity” after being told that he would be fired if he did not sign.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Following
  <span citation-index="1" class="star-pagination" label="275"> 
   *275
   </span>
  his refusal, he was given an administrative hearing and was discharged solely for this refusal, pursuant to § 1123 of the New York City Charter.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b318-5">
<span citation-index="1" class="star-pagination" label="276"> 
   *276
   </span>
  The New York Supreme Court dismissed his petition for reinstatement, 27 App. Div. 2d 800, 279 N. Y. S. 2d 150 (1967), and the New York Court of Appeals affirmed. 20 N. Y. 2d 227, <span class="citation" data-id="5523781"><a href="/opinion/5676083/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">229 N. E. 2d 184</a></span> (1967). We noted probable jurisdiction. <span class="citation multiple-matches"><a href="/c/U.%20S./390/918/">390 U. S. 918</a></span> (1968).
 </p>
<p id="b318-6">
  Our decisions establish beyond dispute the breadth of the privilege to refuse to respond to questions when the result may be self-incriminatory, and the need fully to implement its guaranty. See
  <em>
   Spevack
  </em>
  v.
  <em>
   Klein,
  </em>
  <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/" aria-description="Citation for case: Spevack v. Klein">385 U. S. 511</a></span> (1967);
  <em>
   Counselman
  </em>
  v.
  <em>
   Hitchcock,
  </em>
  <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#585" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 585-586</a></span> (1892);
  <em>
   Albertson
  </em>
  v.
  <em>
   SACB,
  </em>
  <span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/#80" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70, 80</a></span> (1965). The privilege is applicable to state as well as federal proceedings.
  <em>
   Malloy
  </em>
  v.
  <em>
   Hogan,
  </em>
  <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964);
  <em>
   Murphy
  </em>
  v.
  <em>
   Waterfront Commission,
  </em>
  <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52</a></span> (1964). The privilege may be waived in appropriate circumstances if the waiver is knowingly and voluntarily made. Answers may be compelled regardless of the privilege if there is immunity from federal and state use of the compelled testimony or its fruits in connection with a criminal prosecution against the person testifying.
  <em>
   Counselman
  </em>
  v.
  <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#585" aria-description="Citation for case: Counselman v. Hitchcock"><em>
   Hitchcock, supra,
  </em>
  at 585-586</a></span>;
  <em>
   Murphy
  </em>
  v.
  <em>
   Waterfront Commission, supra,
  </em>
  at 79.
 </p>
<p id="b318-7">
  The question presented in the present case is whether a policeman who refuses to waive the protections which the privilege gives him may be dismissed from office because of that refusal.
 </p>
<p id="b318-8">
  About a year and a half after New York City discharged petitioner for his refusal to waive this immunity, we decided
  <em>
   Garrity
  </em>
  v.
  <em>
   New Jersey, 385
  </em>
  U. S. 493 (1967). In that case, we held that when a policeman had been compelled to testify by the threat that otherwise he would be removed from office, the testimony that he gave could not be used against him in a subsequent prosecution. Garrity had not signed a waiver of immunity and no immunity statute was applicable in the circumstances.
  <span citation-index="1" class="star-pagination" label="277"> 
   *277
   </span>
  Our holding was summarized in the following statement (at 500):
 </p>
<blockquote id="b319-5">
  “We now hold the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic.”
 </blockquote>
<p id="b319-6">
  The New York Court of Appeals considered that
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
  </em>
  did not control the present case. It is true that
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
  </em>
  related to the attempted use of compelled testimony. It did not involve the precise question which is presented here: namely, whether a State may discharge an officer for refusing to waive a right which the Constitution guarantees to him. The New York Court of Appeals also distinguished our post
  <em>
   -Garrity
  </em>
  decision in
  <em>
   Spevack
  </em>
  v.
  <em>
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/" aria-description="Citation for case: Spevack v. Klein">Klein, supra.</a></span>
  </em>
  In
  <em>
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/" aria-description="Citation for case: Spevack v. Klein">Spevack</a></span>,
  </em>
  we ruled that a lawyer could not be disbarred solely because he refused to testify at a disciplinary proceeding on the ground that his testimony would tend to incriminate him. The Court of Appeals concluded that
  <em>
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/" aria-description="Citation for case: Spevack v. Klein">Spevack</a></span>
  </em>
  does not control the present case because different considerations apply in the case of a public official such as a policeman. A lawyer, it stated, although licensed by the state is not an employee. This distinction is now urged upon us. It is argued that although a lawyer could not constitutionally be confronted with Hobson’s choice between self-incrimination and forfeiting his means of livelihood, the same principle should not protect a policeman. Unlike the lawyer, he is directly, immediately, and entirely responsible to the city or State which is his employer. He owes his entire loyalty to it. He has no other “client” or principal. He is a trustee of the public interest, bearing
  <span citation-index="1" class="star-pagination" label="278"> 
   *278
   </span>
  the burden of great and total responsibility to his public employer. Unlike the lawyer who is directly responsible to his client, the policeman is either responsible to the State or to no one.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b320-5">
  We agree that these factors differentiate the situations. If appellant, a policeman, had refused to answer questions specifically, directly, and narrowly relating to the performance of his official duties,
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  without being required to waive his immunity with respect to the use of his answers or the fruits thereof in a criminal prosecution of himself,
  <em>
   Garrity
  </em>
  v.
  <em>
   New <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Jersey, supra,</a></span>
  </em>
  the privilege against self-incrimination would not have been a bar to his dismissal.
 </p>
<p id="b320-6">
  The facts of this case, however, do not present this issue. Here, petitioner was summoned to testify before a grand jury in an investigation of alleged criminal conduct. He was discharged from office, not for failure to answer relevant questions about his official duties, but for refusal to waive a constitutional right. He was dismissed for failure to relinquish the protections of the privilege against self-incrimination. The Constitution of New York State and the City Charter both expressly provided that his failure to do so, as well as his failure to testify, would result in dismissal from his job. He was dismissed solely for his refusal to waive the immunity to which he is entitled if he is required to testify despite his constitutional privilege;
  <em>
   Garrity
  </em>
  v.
  <em>
   New <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Jersey, supra.</a></span>
  </em>
</p>
<p id="b320-7">
  We need not speculate whether, if appellant had executed the waiver of immunity in the circumstances, the effect of our subsequent decision in
  <em>
   Garrity
  </em>
  v.
  <em>
   New <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Jersey, supra,</a></span>
  </em>
  would have been to nullify the effect of
  <span citation-index="1" class="star-pagination" label="279"> 
   *279
   </span>
  the waiver. New York City discharged him for refusal to execute a document purporting to waive his constitutional rights and to permit prosecution of himself on the basis of his compelled testimony. Petitioner could not have assumed — and certainly he was not required to assume — that he was being asked to- do an idle act of no legal effect. In any event, the mandate of the great privilege against self-incrimination does not tolerate the attempt, regardless of its ultimate effectiveness, to coerce a waiver of the immunity it confers on penalty of the loss of employment. It is clear that petitioner’s testimony was demanded before the grand jury in part so that it might be used to prosecute him, and not solely for the purpose of securing an accounting of his performance of his public trust. If the latter had been the only purpose, there would have been no reason to seek to compel petitioner to waive his immunity.
 </p>
<p id="b321-5">
  Proper regard for the history and meaning of the privilege against self-incrimination,
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  applicable to the States under our decision in
  <em>
   Malloy
  </em>
  v.
  <em>
   Hogan,
  </em>
  <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), and for the decisions of this Court,
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  dictate the conclusion that the provision of the New York City Charter pursuant to which petitioner was dismissed cannot stand. Accordingly, the judgment is
 </p>
<p id="b321-6">
<em>
   Reversed.
  </em>
</p>
<judges id="b321-7">
  Mr. Justice Black concurs in the result.
 </judges>
<p id="b321-8">
  [For opinion of Mr. Justice Harlan, concurring in the result, see
  <em>
   post,
  </em>
  p. 285.]
 </p>







<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b316-8">
   The Assistant District Attorney said to appellant:
  </p>
<blockquote id="b316-9">
   “You understand . . . that under the Constitution of the United States, as well as the Constitution of New York, no one can be compelled to testify against himself, and that he has a right, the absolute right to refuse to answer any questions that would tend to incriminate him?”
  </blockquote>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b316-10">
   Appellant was told:
  </p>
<blockquote id="b316-11">
   “You understand . . . that under the Constitution of New York, as well as the Charter of the City of New York, ... a public officer, which includes a police officer, when called before a Grand Jury to answer questions concerning the conduct of his public office and the performance of his duties is required to sign a waiver of immunity if he wishes to retain that public office?”
  </blockquote>
<p id="b316-12">
   The document appellant was asked to sign was phrased as follows:
  </p>
<blockquote id="b316-13">
   “I . . . do hereby waive all benefits, privileges, rights and immunity which I would otherwise obtain from indictment, prosecution, and punishment for or on account of, regarding or relating to any matter, transaction or things, concerning the conduct of my office or the
   <span citation-index="1" class="star-pagination" label="275"> 
    *275
    </span>
   performance of my official duties, or the property, government or affairs of the State of New York or of any county included within its territorial limits, or the nomination, election, appointment or official conduct of any officer of the city or of any such county, concerning any of which matters, transactions or things I may testify or produce evidence documentary or otherwise, before the [blank] Grand Jury in the County of New York, in the investigation being conducted by said Grand Jury.”
  </blockquote>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b317-12">
   That section provides:
  </p>
<blockquote id="b317-13">
   “If any councilman or other officer or employee of the city shall, after lawful notice or process, wilfully refuse or fail to appear before any court or judge, any legislative committee, or any officer, board or body authorized to conduct any hearing or inquiry, or having appeared shall refuse to testify or to answer any question regarding the property, government or affairs of the city or of any county included within its territorial limits, or regarding the nomination, election, appointment or official conduct of any officer or employee of the city or of any such county, on the ground that his answer would tend to incriminate him, or shall refuse to waive immunity from prosecution on account of any such matter in relation to which he may be asked to testify upon .any such hearing or inquiry, his term or tenure of office or employment shall terminate and such office or employment shall be vacant, and he shall not be eligible to election or appointment to any office or employment under the city or any agency.”
  </blockquote>
<p id="b317-14">
   Section 6 of Article I of the New York Constitution provides:
  </p>
<blockquote id="b317-15">
   “No person shall be . . . compelled in any criminal case to be a witness against himself, providing, that any public officer who, upon being called before a grand jury to testify concerning the conduct of his present office ... or the performance of his official duties . . . refuses to sign a waiver of immunity against subsequent criminal prosecution, or to answer any relevant question concerning such matters before such grand jury, shall by virtue of such refusal, be disqualified from holding any other public office or public employment for a period of five years . . . and shall be removed from his present office by the appropriate authority or shall forfeit his present office at the suit of the attorney-general.”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b320-8">
   Cf.
   <em>
    Spevack
   </em>
   v.
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/#519" aria-description="Citation for case: Spevack v. Klein"><em>
    Klein, supra,
   </em>
   at 519-520</a></span> (concurring in judgment).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b320-9">
   The statements in my separate opinion in
   <em>
    Spevack
   </em>
   v.
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/#519" aria-description="Citation for case: Spevack v. Klein"><em>
    Klein, supra,
   </em>
   at 519-520</a></span>, to which the New York Court of Appeals referred, are expressly limited to situations of this kind.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b321-9">
   See
   <em>
    Miranda
   </em>
   v.
   <em>
    Arizona,
   </em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 458-466</a></span> (1966), and authorities cited therein.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b321-10">
   See,
   <em>
    e. g., Griffin
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965);
   <em>
    Malloy
   </em>
   v.
   <em>
    <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Hogan, supra.</a></span>
   </em>
</p>
</div></div></opinion>
```

---
