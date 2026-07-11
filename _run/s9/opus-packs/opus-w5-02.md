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

## GROUP: _overhaul2/lake/cases/Graham v. Barnette.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Graham v. Barnette"
type: case
citation: "5 F.4th 872 (2021)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 8th Circuit"
court_level: coa
circuit: 8th
year: 2021
date_decided: 2021-07-16
docket: 19-2512
authority_weight: "Binding in-circuit — 8th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2021-07-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Graham v. Barnette
  varies_by_point: false
  scope_note: "Good law; decided on remand from the Supreme Court in light of Caniglia v. Strom. Holds that post-Caniglia the 'community caretaking' label for psychiatric seizures is a category error and that probable cause of dangerousness governs."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4900401/teresa-graham-v-shannon-barnette/"
  cluster_id: 4900401
  opinion_id: 4704180
  identity_checked: true
homes:
  - page: "[[Community Caretaking]]"
    role: "Key — Progeny / Limit"
related: ["[[Caniglia v. Strom]]", "[[United States v. Garner]]", "[[United States v. Rideau]]", "[[Cady v. Dombrowski]]"]
aliases: ["Teresa Graham v. Shannon Barnette", "Graham v. Barnette (8th Cir. 2021)"]
tags: ["case", "fourth-amendment", "community-caretaking", "mental-health-seizure", "probable-cause", "qualified-immunity", "eighth-circuit", "persons-in-public"]
holding: "After Caniglia v. Strom, using the 'community caretaking' label for warrantless psychiatric seizures is a category error; a seizure of a person for an emergency mental-health evaluation is reasonable under the Fourth Amendment only on probable cause that the person is mentally ill and dangerous to herself or others (though the officers received qualified immunity because that standard was not clearly established in the circuit)."
lake:
  record_id: Graham v. Barnette
  status: verified
  projected_at: 2026-07-09
---

# Graham v. Barnette

*5 F.4th 872 (8th Cir. 2021)* · U.S. Court of Appeals, 8th Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a series of escalating 911 calls on May 25, 2017 — including an anonymous caller claiming to be Teresa Graham's cousin who requested a "welfare check" and referenced a possible mental-health history — Sergeant Barnette ordered Minneapolis officers to take Graham into custody for an emergency mental-health evaluation under Minnesota's civil-commitment statute. The officers entered Graham's home, seized her, and transported her to a hospital, all without a warrant. Graham sued the officers and the City under 42 U.S.C. § 1983. The district court granted the officers summary judgment; the Eighth Circuit affirmed in 2020 (970 F.3d 1075), and the Supreme Court [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] for reconsideration in light of [[Caniglia v. Strom]].

## Issue
[[Reading and Citing Cases#on-remand|On remand]] after *[[Caniglia v. Strom|Caniglia]]*, whether the "community caretaking" framing supports a warrantless seizure of a person for a mental-health evaluation, and what Fourth Amendment standard governs such a seizure.

## Rule
After *[[Caniglia v. Strom|Caniglia]]*, the "community caretaking" label does not fit a psychiatric seizure. "Now that *Caniglia* has made clear that 'there is no overarching "[[Community Caretaking|community caretaking]]" doctrine,' . . . our use of that label seems to be a category error." — *Graham v. Barnette*, 5 F.4th 872 (8th Cir. 2021) (slip op., at 10). ^pin-op10

The governing standard is probable cause of dangerousness: "we again conclude that probable cause of dangerousness is the standard that must be met for a warrantless mental-health seizure to be reasonable under the Fourth Amendment." — *Id.* (slip op., at [10](https://www.courtlistener.com/opinion/4900401/teresa-graham-v-shannon-barnette/#:~:text=we%20again%20conclude%20that%20probable)). ^pin-op10a

The court noted that "[a]t least nine of our sister circuits have held that the Fourth Amendment requires probable cause that a person is mentally ill and dangerous to herself or others for a seizure for an emergency mental-health evaluation to be reasonable." — *Id.* (slip op., at 10-11). ^pin-op10b

## Application
On these facts, the court reaffirmed (prong one) that the officers needed probable cause that Graham was mentally ill and dangerous to herself or others to seize her for a mental-health evaluation, and it rejected the "community caretaking" label as the analytic frame. *[[Caniglia v. Strom|Caniglia]]* did not disturb that reasoning, because the Supreme Court there "refrain[ed]" from addressing the standards for "emergency seizures for psychiatric treatment, observation, or stabilization." But because Eighth Circuit case law had previously been ambiguous — some precedents suggesting a lower "reasonable belief" standard — the probable-cause-of-dangerousness rule was not clearly established at the time of Graham's seizure, so the officers were entitled to [[Qualified Immunity|qualified immunity]] on that claim.

## Conclusion
The Eighth Circuit again affirmed summary judgment for the officers on qualified-immunity grounds, while holding that probable cause of dangerousness — not a "community caretaking" rationale — is the standard a warrantless mental-health seizure must satisfy under the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 8th Cir.**
- *Graham* is the Eighth Circuit's post-*[[Caniglia v. Strom|Caniglia]]* **limit** on the caretaking framing: it treats the "community caretaking" label for psychiatric seizures as a category error and routes such seizures through **probable cause of dangerousness**. It builds on [[Caniglia v. Strom]] (no freestanding community-caretaking entry into the home) and stands alongside the persons-in-public caretaking-detention line of [[United States v. Garner]] (10th Cir.) and [[United States v. Rideau]] (5th Cir.), which address brief caretaking detentions rather than full psychiatric seizures.

## Appears on
- [[Community Caretaking]] — *Key — Progeny / Limit*

## Sources
- *Graham v. Barnette*, 5 F.4th 872 (8th Cir. 2021) — https://www.courtlistener.com/opinion/4900401/teresa-graham-v-shannon-barnette/ — pinpoints given as slip-opinion pages (slip op., at 10-11); CourtListener carries the slip opinion (cluster 4900401 → opinion 4704180).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "07fab6a12b3c69e0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Graham v. Barnette"}, "payload": {"all": [{"cite": "5 F.4th 872", "page": "872", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "5"}], "display": "5 F.4th 872", "official": {"cite": "5 F.4th 872", "page": "872", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "5"}, "official_selection_present": true, "record_id": "Graham v. Barnette"}}
{"assertion_id": "09b25fdf76a96e7a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op10b", "record_id": "Graham v. Barnette"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op10b", "pinpoint_status": "slip-only", "quote": "[a]t least nine of our sister circuits have held that the Fourth Amendment requires probable cause that a person is mentally ill and dangerous to herself or others for a seizure for an emergency mental-health evaluation to be reasonable.", "quote_fidelity": "mismatch", "record_id": "Graham v. Barnette", "star_marker": null}}
{"assertion_id": "507a92ccda1e39a9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op10", "record_id": "Graham v. Barnette"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op10", "pinpoint_status": "slip-only", "quote": "framing supports a warrantless seizure of a person for a mental-health evaluation, and what Fourth Amendment standard governs such a seizure. ## Rule After *Caniglia*, the", "quote_fidelity": "mismatch", "record_id": "Graham v. Barnette", "star_marker": null}}
{"assertion_id": "7923c7806c5f0eb7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op10a", "record_id": "Graham v. Barnette"}, "payload": {"fragment": "#:~:text=we%20again%20conclude%20that%20probable", "page": null, "pin_id": "pin-op10a", "pinpoint_status": "star-verified", "quote": "we again conclude that probable cause of dangerousness is the standard that must be met for a warrantless mental-health seizure to be reasonable under the Fourth Amendment.", "quote_fidelity": "matched", "record_id": "Graham v. Barnette", "star_marker": "1"}}
{"assertion_id": "85bfd2b34453da7d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Graham v. Barnette"}, "payload": {"as_of_content": "2021-07-16", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Graham v. Barnette", "scope_note": "Good law; decided on remand from the Supreme Court in light of Caniglia v. Strom. Holds that post-Caniglia the 'community caretaking' label for psychiatric seizures is a category error and that probable cause of dangerousness governs.", "varies_by_point": false}}
```

### lake record — Graham v. Barnette

```json
{
  "schema_version": "s2.v1",
  "record_id": "Graham v. Barnette",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Teresa Graham v. Shannon Barnette",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "Graham v. Barnette",
    "court": "U.S. Court of Appeals, 8th Circuit",
    "court_id": "ca8",
    "court_level": "coa",
    "circuit": "8th",
    "state": null,
    "date_decided": "2021-07-16",
    "year": 2021,
    "docket": "19-2512",
    "cluster_id": 4900401,
    "lead_opinion_id": 4704180,
    "sibling_ids": [
      4704180
    ],
    "absolute_url": "/opinion/4900401/teresa-graham-v-shannon-barnette/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "5 F.4th 872",
      "volume": "5",
      "reporter": "F.4th",
      "page": "872",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "5 F.4th 872",
        "volume": "5",
        "reporter": "F.4th",
        "page": "872",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "5 F.4th 872",
    "official_selection": {
      "court_class": "coa",
      "selected": "5 F.4th 872",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op10",
      "page": null,
      "quote": "framing supports a warrantless seizure of a person for a mental-health evaluation, and what Fourth Amendment standard governs such a seizure. ## Rule After *Caniglia*, the",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op10a",
      "page": null,
      "quote": "we again conclude that probable cause of dangerousness is the standard that must be met for a warrantless mental-health seizure to be reasonable under the Fourth Amendment.",
      "star_marker": "1",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 21278,
      "fragment": "#:~:text=we%20again%20conclude%20that%20probable",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-op10b",
      "page": null,
      "quote": "[a]t least nine of our sister circuits have held that the Fourth Amendment requires probable cause that a person is mentally ill and dangerous to herself or others for a seizure for an emergency mental-health evaluation to be reasonable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-07-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Graham v. Barnette",
    "varies_by_point": false,
    "scope_note": "Good law; decided on remand from the Supreme Court in light of Caniglia v. Strom. Holds that post-Caniglia the 'community caretaking' label for psychiatric seizures is a category error and that probable cause of dangerousness governs.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Marcus Mitchell v. Kyle Kirchmeier",
          "cluster_id": 6450805,
          "cite": [
            "28 F.4th 888"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Christopher De Rossitte v. Correct Care Solutions, Inc.",
          "cluster_id": 5668863,
          "cite": [
            "22 F.4th 796"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Courtney Saunders v. Kyle Thies",
          "cluster_id": 6619908,
          "cite": [
            "38 F.4th 701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eric Poemoceah v. Morton County",
          "cluster_id": 10124806,
          "cite": [
            "117 F. 4th 1049"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kelly Martin v. Jordan Turner",
          "cluster_id": 9415009,
          "cite": [
            "73 F.4th 1007"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Devin Ledbetter v. B. Helmers",
          "cluster_id": 10372074,
          "cite": [
            "133 F.4th 788"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cory Sessler v. City of Davenport, Iowa",
          "cluster_id": 9506531,
          "cite": [
            "102 F.4th 876"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monica Perkins v. City of Des Moines",
          "cluster_id": 10804290,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tyrone Cameron v. City of Des Moines",
          "cluster_id": 10800891,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Teulilo",
          "cluster_id": 10798023,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tara McNeally v. HomeTown Bank",
          "cluster_id": 10706938,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jennifer Harmon v. Second Judicial Circuit of the State of Missouri",
          "cluster_id": 10312599,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dywan Conley",
          "cluster_id": 9404331,
          "cite": [
            "69 F.4th 519"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4704180) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca8)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(4704180)",
        "reviewed": 13,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 13,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4704180)",
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
    "complete_query": "cites:(4704180)",
    "indexed_citing_opinions": 13,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4704180,
        "count": 13,
        "count_source": "search"
      }
    ],
    "citation_count": 50,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/graham-v-barnette.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 13,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4704180,
        "cited_id": 89833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 169087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 178217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 197278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 218764,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 288616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 301743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 403636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 580786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 601532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 617079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 620238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 622303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 712235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 738277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 743603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 786941,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 787644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 793704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 794431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 795126,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 797197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 797743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 798058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 799248,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1027858,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1274696,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1348291,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1378661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1808076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1836506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2668794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2670795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2677985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2718042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2801435,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2804087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2973307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 3194110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4148210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4155743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4238107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4307201,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4307919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4386310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4525061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4543039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4556124,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4669130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4687473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 7261027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 8413948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 8415460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9226038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9420390,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9427218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9427232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9427599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9430599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9431119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9431589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9434540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9494088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9497489,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9500600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9569092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9799674,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9805636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9811318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9820073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9821360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9842136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9873109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9878125,
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
    "date_created": "2026-07-05T05:49:51Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:51:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Graham v. Barnette

```
               United States Court of Appeals
                          For the Eighth Circuit
                      ___________________________

                              No. 19-2512
                      ___________________________

                              Teresa M. Graham

                                   Plaintiff - Appellant

                                      v.

Sgt. Shannon L. Barnette; Officer Amanda Sanchez; Officer Mohamed Noor; City
                                 of Minneapolis

                                 Defendants - Appellees
                               ____________

                             State of Minnesota

                                    Amicus Curiae
                               ____________

                   Appeal from United States District Court
                        for the District of Minnesota
                               ____________

                           Submitted: July 12, 2021
                             Filed: July 16, 2021
                                ____________

Before GRUENDER, WOLLMAN, and KOBES, Circuit Judges.
                       ____________

GRUENDER, Circuit Judge.
       Teresa Graham sued Sergeant Shannon Barnette, Officer Mohamed Noor, and
Officer Amanda Sanchez (“the officers”), as well as the City of Minneapolis (“the
City”), under 42 U.S.C. § 1983 and Minnesota state law after the officers entered
her home, seized her, and transported her to a hospital for a mental-health evaluation,
all without a warrant. The district court 1 granted the officers and the City summary
judgment. Graham appealed. We affirmed. Graham v. Barnette, 970 F.3d 1075,
1082 (8th Cir. 2020). The Supreme Court subsequently vacated our judgment and
remanded the case for reconsideration in light of Caniglia v. Strom, 593 U.S. ---, 141
S. Ct. 1596 (2021). Graham v. Barnette, 593 U.S. ---, 2021 WL 2301963, at *1
(U.S. June 7, 2021). We have done so and once again affirm. Our prior opinion in
this case is hereby vacated, and this opinion is substituted for it.

                                          I.

      “We recount the facts of this case in the light most favorable to [Graham], the
non-moving party.” Meehan v. Thompson, 763 F.3d 936, 938 (8th Cir. 2014). In so
doing, we rely on the factual findings of the district court, see Saylor v. Nebraska,
812 F.3d 637, 642 (8th Cir. 2016), as well as audio and video recordings of the
relevant events, see Meehan, 763 F.3d at 938.

       At approximately 10:00 a.m. on May 25, 2017, Graham called 911 and
reported that a man was smoking marijuana on a retaining wall behind her home. A
City police officer arrived at Graham’s address later that morning, saw no one, and
left without following up with Graham. Several hours later, Graham called the
police again and left a voicemail for the precinct’s commander, complaining that
officers did not respond to her emergency call and referencing an email she sent
earlier in the day regarding the police department’s failure to respond to a different
report she had filed. Around 6:00 p.m., a police officer returned Graham’s call and



      1
      The Honorable Joan N. Ericksen, United States District Judge for the District
of Minnesota.

                                         -2-
informed her that officers had investigated her complaint regarding the unidentified
man in her backyard.

      Things then took an unusual turn. At 6:11 p.m., an anonymous informant
claiming to be Graham’s cousin called 911 and reported that Graham had called him
at work to threaten him and his family. He told the 911 operator that “this is not an
emergency” and that he “did not think [Graham] was going to do anything.” Even
so, he requested a “welfare check” because he believed Graham had a history of
mental-health issues. The operator summarized the call for the responding officers
in a comment to the incident report that read, “CLRS COUSIN WHO JUST
CALLED HIM AT WORK AND THREATENED HIM AND HIS FAMILY.” The
operator also noted that the individual requested a welfare check on Graham and that
Graham’s mental-health diagnosis was unknown.

       Two hours later, Officers Noor and Sanchez arrived at Graham’s home.
Officer Sanchez recorded the encounter using a body camera. When Graham
answered the door, she demanded to know who requested the welfare check, claimed
she was being slandered, retrieved her phone to videotape the officers, accused the
police of harassing her because of her earlier complaints, and then demanded that
the officers leave. The officers apologized for disturbing Graham, left her home,
and noted in their incident report that they were unable to “check on her welfare”
because of her insistence that they leave but concluded she “appeared to be AOK.”

      But the interaction between Graham and the police did not end there. At 9:05
p.m., a 911 operator reported that Graham had called three more times since the
welfare check. Graham first called at 8:20 p.m. to complain about what she viewed
as the officers harassing her in retaliation for her previous calls. The operator
described Graham as agitated as well as aggressive and suggested that Graham was
not making sense. Approximately fifteen minutes later, Sergeant Barnette returned
Graham’s call, and the two spoke briefly about Graham’s concerns. At 8:40 p.m.,
Graham called 911 again, asking to be connected to the Edina police department.
Twenty minutes later, she called once more and made the same request.


                                         -3-
       At this time, Sergeant Barnette ordered Officers Noor and Sanchez to take
Graham into custody for an emergency mental-health evaluation as authorized by
Minnesota’s Civil Commitment and Treatment Act (“MCCTA”), Minn. Stat.
§ 253B.05, subd. 2(a) (2017), which permits an officer to seize a person for an
emergency mental-health evaluation “if the officer has reason to believe . . . that the
person is mentally ill . . . and in danger of injuring self or others if not immediately
detained.” In ordering the seizure, Sergeant Barnette relied on the officers’
interactions with Graham throughout the day, the anonymous report that Graham
had threatened her cousin, and Sergeant Barnette’s own previous interactions with
Graham through which Sergeant Barnette claimed to be aware of “some mental
health history” and a history of restraining orders.

      The officers arrived for a second time at Graham’s home at 9:40 p.m. By this
time, one of Graham’s family members—a state police officer—had warned the
Edina police department that Graham may fight with police, and Sergeant Barnette
decided to join Officers Noor and Sanchez at Graham’s home. The officers wore
body cameras that recorded the encounter.

       When the officers arrived, Graham opened the interior front door but left her
storm door locked and shut. Graham appeared angry, told the officers that she did
not call them for help, demanded that they leave her property, and slammed the front
door. Sergeant Barnette then removed the screen from the storm door to allow entry
should Graham reopen the interior door. With the interior door closed, Graham told
the officers she was fine. She then called 911 to complain that the officers would
not leave. After an extended discussion with the officers through the door, Graham
reopened the door, at which point the officers entered her home through the then-
screenless storm door and held Graham by each arm. During the encounter in her
home, Graham did not resist or threaten the officers, but she did criticize them and
threaten to sue them, alleging they were kidnapping her because of her complaints.

      After several minutes, the officers placed Graham in an ambulance, noting in
the relevant paperwork that they took Graham into custody because she


                                          -4-
“continuously called 911 and per dispatchers was verbally agitated and not making
sense.” Graham was then transported to Southdale Fairview Hospital, where she
was evaluated and subsequently discharged after an examination demonstrated that,
while she exhibited “some paranoid behavior” and was “royally pissed,” she was
“somewhat rational” and, according to the examining physician, not “hold-able.”

      Graham brought suit, asserting (as relevant here) claims under 42 U.S.C.
§ 1983 on the basis that the officers violated her Fourth Amendment rights by
conducting an unreasonable search and seizure and that they violated her First
Amendment rights by arresting her in retaliation for protected speech. 2 She also
brought § 1983 claims against the City under Monell v. Department of Social
Services, 436 U.S. 658, 690 (1978), alleging that the City’s policy regarding seizures
for emergency mental-health evaluations caused the officers’ unconstitutional
conduct and that the City’s failure to train the officers resulted in their
unconstitutional conduct. Finally, Graham brought Minnesota state-law claims
against the officers for false imprisonment, battery, assault, and negligence.

       The district court entered summary judgment in favor of the officers, granting
them qualified immunity on Graham’s Fourth Amendment claims, finding that
Graham had not established a triable issue of fact regarding her retaliatory-arrest
claim, and granting the officers statutory and official immunity on Graham’s state-
law claims. The district court also entered summary judgment in favor of the City,
determining that the City’s policy concerning seizures for emergency mental-health
evaluations was not facially unconstitutional and that Graham did not plead facts
sufficient to support a claim for failure to train.

     Graham appealed. We previously affirmed the district court’s judgment. See
Graham, 970 F.3d at 1082. Graham then petitioned for a writ of certiorari, arguing

      2
       Graham also raised claims of excessive force, property damage, and
conspiracy before the district court, but she did not raise them on appeal and has thus
abandoned them. See Griffith v. City of Des Moines, 387 F.3d 733, 739 (8th Cir.
2004).

                                         -5-
(as relevant here) that the doctrine we relied on to find that the officers’ warrantless
entry was reasonable under the Fourth Amendment—the so-called community-
caretaking or community-caretaker exception—did not apply to the home. 3 While
Graham’s petition was pending, the Supreme Court decided Caniglia, where it
explained that this “exception” is not actually a “standalone doctrine that justifies
warrantless searches and seizures in the home.” 141 S. Ct. at 1598. Subsequently,
it granted Graham’s certiorari petition, vacated our prior judgment in Graham’s
appeal, and remanded the matter to us for further consideration in light of Caniglia.
Graham, 2021 WL 2301963, at *1. We have reconsidered this appeal in light of
Caniglia, and we once again affirm the district court’s judgment.

                                          II.

       We first consider the district court’s grant of summary judgment to the officers
and the City on Graham’s § 1983 claims. “We review the district court’s grant of
summary judgment and qualified immunity rulings de novo.” Samuelson v. City of
New Ulm, 455 F.3d 871, 875 (8th Cir. 2006). Summary judgment is proper if, when
viewing the facts in the light most favorable to the nonmoving party, see Mullenix
v. Luna, 577 U.S. ---, 136 S. Ct. 305, 307 (2015) (per curiam), “the movant shows
that there is no genuine dispute as to any material fact and the movant is entitled to
judgment as a matter of law,” Fed. R. Civ. P. 56(a). A genuine dispute exists “if the
evidence is such that a reasonable jury could return a verdict for the nonmoving
party.” Anderson v. Liberty Lobby, Inc., 477 U.S. 242, 248 (1986).




      3
       As she did before us, Graham also argued in her certiorari petition that the
doctrine of qualified immunity should be modified or “overruled.” This argument
remains foreclosed by Supreme Court and Eighth Circuit precedent. See, e.g., White
v. Pauly, 580 U.S. ---, 137 S. Ct. 548, 551 (2017) (per curiam); Lane v. Nading, 927
F.3d 1018, 1022 (8th Cir. 2019).

                                          -6-
                                        A.

       Graham first argues that the officers violated her clearly established Fourth
Amendment right to be free from an unreasonable search by entering her home. Pre-
Caniglia, the officers responded that their warrantless entry into her home was
reasonable under the community-caretaking exception but that, even if it was not,
they were entitled to qualified immunity as to this claim because it was not clearly
established that their actions were unreasonable in the circumstances.

       A law-enforcement officer is entitled to qualified immunity unless “(1) the
facts, viewed in the light most favorable to the plaintiff, demonstrate the deprivation
of a constitutional or statutory right; and (2) the right was clearly established at the
time of the deprivation.” Walton v. Dawson, 752 F.3d 1109, 1116 (8th Cir. 2014).
Due to the “dearth of community caretaking cases,” the district court bypassed the
first prong of the analysis, see Reichle v. Howards, 566 U.S. 658, 664 (2012),
concluding instead that the law was not clearly established that the officers violated
Graham’s Fourth Amendment rights by entering her home without a warrant
pursuant to the community-caretaking exception. Previously, we opted to affirm
under the first prong, see, e.g., Greenman v. Jessen, 787 F.3d 882, 887 & n.10 (8th
Cir. 2015), concluding that the officers’ warrantless entry was sufficiently justified
and thus reasonable under the community-caretaking exception, Graham, 970 F.3d
at 1084-86. But Caniglia rendered our prior rationale untenable insofar as it
explained that “community caretaking” was not a “standalone doctrine” that could
justify warrantless entry into the home. See 141 S. Ct. at 1598. Accordingly, we
now affirm the district court’s grant of summary judgment under the second prong
of the qualified-immunity analysis.

       For purposes of the second prong, we look to “the legal rules that were clearly
established at the time” the action at issue was taken. Davis v. Hall, 375 F.3d 703,
711 (8th Cir. 2004) (internal quotation marks omitted); see also Anderson v.
Creighton, 483 U.S. 635, 640 (1987) (noting that this analysis turns on whether the
unlawfulness of the official’s actions was apparent “in the light of pre-existing law”).


                                          -7-
In other words, this inquiry “does not take into account later . . . changes in the law.”
Jackson v. Humphrey, 776 F.3d 1232, 1242 (11th Cir. 2015).

       On May 25, 2017, it was well established in this circuit that the community-
caretaking exception was a standalone doctrine that alone could justify warrantless
entry into a home. See, e.g., United States v. Smith, 820 F.3d 356, 360 (8th Cir.
2016); Burke v. Sullivan, 677 F.3d 367, 372 (8th Cir. 2012); United States v.
Quezada, 448 F.3d 1005, 1007 (8th Cir. 2006). And, in the circumstances present
here, the officers’ warrantless entry did not violate Graham’s Fourth Amendment
rights under our then-extant community-caretaking jurisprudence. As we previously
explained:

      Affording the officers “substantial latitude in interpreting and drawing
      inferences from factual circumstances,” United States v. Washington,
      109 F.3d 459, 465 (8th Cir. 1997), we . . . conclude that the warrantless
      entry into Graham’s home was justified by a reasonable belief that
      Graham was experiencing a mental health emergency and might harm
      herself or others if not detained, see Quezada, 448 F.3d at 1007. The
      officers could reasonably believe that Graham had recently made some
      sort of threat to her cousin; she had called 911 five times that day and
      three times within two hours; and the operator had noted that she was
      “not making sense” and that each time she was argumentative,
      uncooperative, and agitated; Sergeant Barnette knew Graham had a
      history of restraining orders; and a second member of Graham’s family
      warned the police department that she may fight the officers. When the
      officers arrived at her home the second time, Graham was agitated and
      refused to talk with them. She initially stated that she had not called
      the police—even though Sergeant Barnette identified herself and
      explained that she and Graham had spoken shortly before. When the
      officers tried to enter, Graham slammed the door and called 911 again
      even as the officers attempted to explain, as one officer put it, “we are
      911.”

      “When viewed collectively, these facts could lead a reasonable police
      officer to conclude there was either a threat of violence or an emergency
      requiring attention.” Burke[, 677 F.3d at 372]. . . .



                                          -8-
      Finally, once inside the home, the officers did not expand the scope of
      their search beyond that which was justified by the emergency. “The
      justification for the officers’ entry ar[ose] from their obligation to help
      those in danger and ensure the safety of the public,” and the officers
      “carefully tailored” “the scope of the encounter” so as to “satisfy th[at]
      purpose.” Smith, 820 F.3d at 361-62. Upon entry, they immediately
      located Graham, secured her person so she could not harm herself or
      anyone else, and limited their entry to this purpose rather than, say,
      searching throughout the rest of her home or rummaging through her
      belongings. See id. (explaining that the scope of the entry and search
      in the emergency-aid context must be limited to determining whether
      an emergency exists).

      The officers thus acted reasonably when entering Graham’s home.

Graham, 970 F.3d at 1085-86.

       We need not and do not unpack today Caniglia’s full ramifications for our
community-caretaking jurisprudence. Cf. Caniglia, 141 S. Ct. at 1603 (Kavanaugh,
J., concurring) (noting that the “Fourth Amendment issue” presented by warrantless
home entries done for noninvestigatory, “community caretaking” purposes is “more
labeling than substance”). Rather, we decide only that the officers’ warrantless entry
was reasonable under “the legal rules that were clearly established” in this circuit on
May 25, 2017. See Davis, 375 F.3d at 711 (internal quotation marks omitted). While
Caniglia made clear that “community caretaking” was not its own Fourth
Amendment exception that alone could justify warrantless entry into the home,
“Caniglia did not address” what “rights were clearly established” under “pre-
existing circuit law.” Luer v. Cnty. of St. Louis, --- F.4th ---, 2021 WL 2285499, at
*1 (8th Cir. June 3, 2021). Accordingly, we affirm the district court’s grant of
summary judgment on the basis of qualified immunity to the officers with respect to
Graham’s Fourth Amendment warrantless-entry claim.




                                         -9-
                                          B.

        Graham next contends that the officers violated her Fourth Amendment right
to be free from unreasonable seizures when they seized her for a mental-health
evaluation without probable cause to believe that she was a danger to herself or
others. She also argues that probable cause was the clearly established standard at
the time, meaning the officers are not entitled to qualified immunity as to this claim.
Alternatively, she argues that even if this circuit’s standard for evaluating mental-
health seizures is a lower, “reasonable belief” standard, the officers still lacked such
justification to seize her for a mental-health evaluation under clearly established law
and thus should not be granted qualified immunity even under this lower standard.

       Although the district court agreed with Graham that the officers needed
probable cause of dangerousness to seize her for a mental-health evaluation and
lacked such probable cause, it found that the probable-cause standard was not clearly
established. Accordingly, the district court granted the officers qualified immunity
as to this claim. On appeal, the officers (joined by the State of Minnesota as amicus
curiae) contended that, under circuit precedent, the officers needed only reasonable
belief of dangerousness to seize her, and the officers argued that they had such
reasonable belief here. The officers also argued that they were entitled to qualified
immunity as to this claim because their seizure of Graham did not violate clearly
established law.

      Previously, we agreed with the district court that, although our case law had
engendered some confusion about the proper standard, “only probable cause that a
person poses an emergent danger . . . to herself or others” could justify a warrantless
mental-health seizure. Graham, 970 F.3d at 1088-89. But, given the ambiguity in
our case law about this issue, we held that, even if the officers lacked the requisite
probable cause, they could still be entitled to qualified immunity because the
probable-cause standard was not clearly established. Id. at 1090. And we ultimately
concluded that the officers were entitled to qualified immunity because their actions



                                         -10-
did not violate clearly established law under the lower reasonable-belief standard
that some of our precedents had suggested applied here. Id. at 1090-91.

       In our prior discussion of this issue, we used the “community caretaking” label
to discuss the standard under which warrantless mental-health seizures are
permissible under the Fourth Amendment. Id. at 1088. Now that Caniglia has made
clear that “there is no overarching ‘community caretaking’ doctrine,” 141 S. Ct. at
1600 (Alito, J., concurring), our use of that label seems to be a category error. That
said, the Court in Caniglia “refrain[ed]” from addressing generally the standards
governing “emergency seizures for psychiatric treatment, observation, or
stabilization.” Id. at 1601 (Alito, J., concurring). Thus, Caniglia did not affect the
substance of our reasoning or holdings on the issues Graham raises regarding her
warrantless seizure. Accordingly, we once again conclude that (1) probable cause
of dangerousness is the requisite standard; (2) assuming the officers lacked probable
cause here, they may still be entitled to qualified immunity given the ambiguity in
our case law about the requisite standard; and (3) the officers are entitled to qualified
immunity because their actions did not violate clearly established law under the
lower reasonable-belief standard some of our precedents suggested was the requisite
standard.

                                           1.

      First, we again conclude that probable cause of dangerousness is the standard
that must be met for a warrantless mental-health seizure to be reasonable under the
Fourth Amendment.

       At least nine of our sister circuits have held that the Fourth Amendment
requires probable cause that a person is mentally ill and dangerous to herself or
others for a seizure for an emergency mental-health evaluation to be reasonable. See,
e.g., Myers v. Patterson, 819 F.3d 625, 632 (2d Cir. 2016); Cantrell v. City of
Murphy, 666 F.3d 911, 923 (5th Cir. 2012); Roberts v. Spielman, 643 F.3d 899, 905
(11th Cir. 2011); Cloaninger ex rel. Estate of Cloaninger v. McDevitt, 555 F.3d 324,


                                          -11-
334 (4th Cir. 2009); Meyer v. Bd. of Cnty. Comm’rs of Harper Cnty., 482 F.3d 1232,
1239 (10th Cir. 2007); Ahern v. O’Donnell, 109 F.3d 809, 817 (1st Cir. 1997);
Monday v. Oullette, 118 F.3d 1099, 1102 (6th Cir. 1997); Sherman v. Four Cnty.
Counseling Ctr., 987 F.2d 397, 401-02 (7th Cir. 1993); Maag v. Wessler, 960 F.2d
773, 775-76 (9th Cir. 1991) (per curiam); see also Cole v. Town of Morristown, 627
F. App’x 102, 106-07 (3d Cir. 2015) (upholding as reasonable a mental-health
seizure because “the police . . . had probable cause to believe” the plaintiff “was
dangerous”); In re Barnard, 455 F.2d 1370, 1373-74 (D.C. Cir. 1971) (finding that
a plaintiff was seized within the meaning of the Fourth Amendment when taken into
custody for an involuntary mental-health evaluation and explaining that such
seizures are unconstitutional “unless supported by probable cause”). These courts
have uniformly determined that “a seizure of a person for an emergency mental
health evaluation raises concerns that are closely analogous to those implicated by a
criminal arrest, and both are equally intrusive.” See Pino v. Higgs, 75 F.3d 1461,
1468 (10th Cir. 1996).

       Some of these circuits have thought we were first movers in this area, pointing
to Harris v. Pirch, 677 F.2d 681 (8th Cir. 1982), while holding that the right to be
free from seizures for an emergency mental-health evaluation without probable
cause of dangerousness was clearly established. See, e.g., Maag, 960 F.2d at 776.
But neither Pirch nor our later cases are so clear. In Pirch, we determined that an
officer was entitled to qualified immunity after effectuating a mental-health seizure,
and in so doing we commented that “when a court evaluates police conduct relating
to an arrest its guideline is good faith and probable cause.” 677 F.2d at 686 (brackets
omitted). But, because we were evaluating whether an officer complied with a
Missouri statute that used the phrase “reasonable cause,” id. at 684, we held that the
officer was immune from suit because he acted in “good faith and had reasonable
cause” to believe the plaintiff overdosed without explaining whether reasonable
cause was as rigorous a standard as probable cause, id. at 689. Compare Navarette
v. California, 572 U.S. 393, 404 (2014) (using “reasonable cause” and “reasonable
suspicion” interchangeably to justify an investigative stop), with Stacey v. Emery,
97 U.S. 642, 646 (1878) (“If there was a probable cause of seizure, there was a


                                         -12-
reasonable cause. If there was a reasonable cause of seizure, there was a probable
cause.”).

       Since Pirch, we have never held that reasonable belief is sufficient, nor have
we held that probable cause is required, to justify a mental-health seizure. We have
instead suggested that reasonable belief is sufficient to justify some noninvestigatory
seizures while intimating that probable cause is required in other instances.4
Compare Winters v. Adams, 254 F.3d 758, 764, 766 (8th Cir. 2001) (upholding a
brief detention of an intoxicated individual under the community-caretaking
exception and analogizing the officers’ decision to “investigate” and “briefly detain”
to investigative stops), Samuelson, 455 F.3d at 874 (finding “objectively reasonable”
the officers’ decision to transport the plaintiff to a hospital for evaluation due to his
“incoherent” statements after he was mistakenly arrested and in police custody for
breaking into his own garage), and Burke, 677 F.3d at 372-73 (stating that a “brief
detention” based on reasonable belief that it was necessary to secure the safety of an
individual “was lawful”), with Meehan, 763 F.3d at 943 (articulating a
reasonableness balancing test under the community-caretaking exception but
framing the ultimate question as one concerning whether the facts at issue gave the
officer acting “in his capacity as community caretaker” “probable cause to arrest”
the individual), and United States v. Harris, 747 F.3d 1013, 1017, 1019 (8th Cir.
2014) (same).



      4
       Amicus Minnesota argues that we rejected the probable-cause standard for
emergency mental-health seizures in Collins v. Bellinghausen, 153 F.3d 591, 596
(8th Cir. 1998), but this is not so. Instead, when evaluating the plaintiff’s Fourth
Amendment claim, we held that officers acted reasonably when they entered a home
to seize a vulnerable adult that the officers “reasonably believe[d]” needed
immediate aid. Id. And, in the context of evaluating the plaintiff’s claim that the
defendants violated her Fourteenth Amendment right to due process, we stated that
the “probable cause” requirement necessary to justify the initiation of involuntary
commitment proceedings under Iowa law was “irrelevant” to our analysis of what
the Due Process Clause demands—an issue itself distinct from what the Fourth
Amendment requires. See id.

                                          -13-
       We think the through line of these cases is straightforward. As in the criminal
context of an investigative stop, when officers act in a noninvestigatory capacity,
they may briefly detain an individual to ensure her safety and that of the officers or
the public when the officer reasonably believes that an emergency exists requiring
the officer’s attention. But, as with other police functions, all seizures—whether
brief detentions or arrests—done for noninvestigatory purposes are governed by the
Fourth Amendment’s reasonableness balancing test. As a result, the greater the
intrusion on a citizen, the greater the justification required for that intrusion to be
reasonable. Thus, if the detention evolves into an arrest, it must be justified by
probable cause. This balancing test, ever attuned to the nature and quality of the
intrusion, comports with the Supreme Court’s instruction that reasonableness is the
touchstone of the Fourth Amendment. See Smith, 820 F.3d at 360-62 (articulating a
similar rule in the context of community-caretaking searches).

        Our decision in Harris illustrates this point. There, we stated that a “seizure
of a person by a police officer acting in the officer’s noninvestigatory capacity is
reasonable if the governmental interest in the police officer’s exercise of [the
officer’s] community caretaking function, based on specific articulable facts,
outweighs the individual’s interest in being free from arbitrary government
interference.” 747 F.3d at 1017 (internal quotation marks omitted). But we also
explained that even when an officer is operating in a noninvestigatory capacity,
“[t]he scope of [an] encounter must be carefully tailored to satisfy the purpose of the
initial detention, and the police must allow the person to proceed once the officer
has completed the officer’s inquiry, unless, of course, the officer obtains further
reason to justify the stop.” Id. We continued to analyze the initial encounter and
brief detention under the standard of reasonable belief, which we analogized to the
standard required for a Terry stop, but we concluded that the later arrest of the
individual was reasonable because, in the course of the encounter, the officers
developed probable cause. Id. at 1019; see also Terry v. Ohio, 392 U.S. 1, 13 (1969)
(“Encounters are initiated by the police for a wide variety of purposes, some of which
are wholly unrelated to a desire to prosecute for crime.”).



                                         -14-
       Accordingly, we now make explicit that which has long been implicit in our
case law and align our circuit with the unanimous consensus in all other circuits. We
conclude that only probable cause that a person poses an emergent danger—that is,
one calling for prompt action—to herself or others can tip the scales of the Fourth
Amendment’s reasonableness balancing test in favor of the government when it
arrests an individual for a mental-health evaluation because only probable cause
constitutes a sufficient “governmental interest” to outweigh a person’s “interest in
freedom.”5 See Harris, 747 F.3d at 1017; Dunaway v. New York, 442 U.S. 200, 208
(1979) (“The long-prevailing standards of probable cause embod[y] the best
compromise that has been found for accommodating the often opposing interests in
safeguarding citizens from rash and unreasonable interferences with privacy and in
seeking to give fair leeway for enforcing the law in the community’s protection.”
(internal quotation marks and brackets omitted)). Officers have probable cause to
arrest a person for a mental-health evaluation when “the facts and circumstances
within . . . the officers’ knowledge and of which they had reasonably trustworthy
information are sufficient . . . to warrant a man of reasonable caution” to believe that
the person poses an emergent danger to himself or others. Cf. Baribeau v. City of
Minneapolis, 596 F.3d 465, 474 (8th Cir. 2010) (quoting Brinegar v. United States,
338 U.S. 160, 175 (1949)); Cantrell, 666 F.3d at 923 (articulating a similar
standard); Cloaninger, 555 F.3d at 334 (same).

       Our confidence that the Fourth Amendment demands probable cause of
dangerousness to effectuate a mental-health arrest in this case is reinforced by the
location of this arrest: Graham’s home. As the Supreme Court has emphasized, “the
right of a man to retreat into his own home and there be free from unreasonable
government intrusion stands at the very core of the Fourth Amendment.” Groh v.
Ramirez, 540 U.S. 551, 559 (2004) (internal quotation marks and brackets omitted).

      5
       Of course, we do not mean arrest in the traditional criminal sense. Instead,
we agree with our sister circuits that taking a person into custody for an emergency
mental-health evaluation “raises concerns that are closely analogous to those
implicated by a criminal arrest, and both are equally intrusive.” See Pino, 75 F.3d
at 1468.

                                         -15-
For this reason, the Court has “drawn a firm line at the entrance to the house,” and
absent a warrant or probable cause and exigent circumstances, police may not seize
a person in her home. Payton v. New York, 445 U.S. 573, 590 (1980).

                                           2.

       Second, we again conclude that the probable-cause standard was not clearly
established in our jurisprudence, meaning the officers may still be entitled to
qualified immunity even if they seized Graham without probable cause of
dangerousness.

       “To be clearly established, a legal principle must have a sufficiently clear
foundation in then-existing precedent.” See District of Columbia v. Wesby, 583 U.S.
---, 138 S. Ct. 577, 589 (2018). This generally requires a plaintiff to “point to
existing circuit precedent that involves sufficiently ‘similar facts’ to ‘squarely
govern’” the officers’ conduct in the specific circumstances at issue, see Boudoin v.
Harsson, 962 F.3d 1034, 1040 (8th Cir. 2020) (brackets omitted), or, in the absence
of binding precedent, to present “a robust consensus of cases of persuasive
authority” constituting settled law, see De La Rosa v. White, 852 F.3d 740, 745 (8th
Cir. 2017). The plaintiff has the burden to prove that a right was clearly established
at the time of the alleged violation. Wilson v. Lamp, 901 F.3d 981, 986 (8th Cir.
2018).

       Here, Graham cannot point to existing Eighth Circuit precedent that clearly
establishes the probable-cause standard because of the ambiguity in our case law
highlighted above. Indeed, in her briefing, Graham conceded as much, arguing that
Pirch clearly established the standard of probable cause but noting that our case law
“does create confusion.” And during oral argument, Graham’s counsel specifically
asked this court to “make clear” that probable cause is required in this circuit because
“there hasn’t been a case that has directly stated what the requirement is for a mental
health hold.” A right is not clearly established by “controlling authority” merely



                                         -16-
because it may be “suggested by then-existing precedent.” See Wesby, 138 S. Ct. at
589-90.

       Neither is this an instance in which every reasonable officer would have
known that his conduct was unlawful due to a robust consensus of authority from
other circuits. Though, at the time the officers seized Graham, several other circuits
had determined that probable cause was the constitutional standard required to
justify a mental-health arrest, our case law was not merely silent on the issue;
instead, we had created ambiguity concerning the answer, suggesting that reasonable
belief might be sufficient to satisfy the demands of the Fourth Amendment. See
Lane v. Franks, 573 U.S. 228, 243-46 (2014) (concluding that an official was entitled
to qualified immunity because, although decisions from other circuits took one side
of an intracircuit debate, the intracircuit panel decisions conflicted). “No matter how
carefully a reasonable officer read” our precedent “beforehand, that officer could not
know that” the conduct at issue would violate our circuit’s “test.” See City & Cnty.
of San Francisco v. Sheehan, 575 U.S. 600, 616 (2015). This determination is
enough to resolve this issue as the officers are entitled to qualified immunity unless
the right is established “beyond debate.” See Ashcroft v. al-Kidd, 563 U.S. 731, 741
(2011).

                                          3.

      Third, we again conclude that the officers are entitled to qualified immunity
because their actions did not violate clearly established law under the more lenient
reasonable-belief standard that some of our precedents had suggested was the
requisite standard governing warrantless mental-health seizures.

       Graham contends that even if the probable-cause standard was not clearly
established, no reasonable officer could have believed that it was lawful to seize her
because the facts known to the officers after they entered her home did not support
even the lower standard of reasonable belief that she presented an emergent danger
to herself or others. We disagree. We do not think that only a “plainly incompetent”


                                         -17-
officer could conclude he had arguable reasonable belief. See Mullenix, 136 S. Ct.
at 308; Waters v. Madson, 921 F.3d 725, 736 (8th Cir. 2019) (explaining that even
if officers lack reasonable suspicion for an investigative stop, they are entitled to
qualified immunity if they had arguable reasonable suspicion).

       Reasonable belief “is a less exacting standard than probable cause,” Quezada,
448 F.3d at 1007, and, to be reasonable, an officer’s belief must be supported by
specific, articulable facts, see United States v. Sanders, 956 F.3d 534, 539 (8th Cir.
2020). Here, the officers believed that Graham had threatened a family member,
and a second family member warned she might fight the officers; Graham called 911
repeatedly over the previous two hours, and the operator reported that her calls were
nonsensical; Graham denied calling the police when the officers arrived; and
Graham appeared confused as to why the officers were at her home. Although
Graham maintained that she was not a threat to herself or others, the officers were
not required to believe her, particularly considering her agitated state and the prior
reports of threats.

       Thus, at the very least, the facts known to the officers at the time were
sufficient to support arguable reasonable belief that Graham was experiencing a
mental-health crisis and presented an emergent danger to herself or others. Cf.
Ryburn v. Huff, 565 U.S. 469, 476-77 (2012) (“[I]t is a matter of common sense that
a combination of events each of which is mundane when viewed in isolation may
paint an alarming picture.”). Graham has offered no precedent that squarely governs
these facts such that, when considering the officers’ “observations as a whole,”
Waters, 921 F.3d at 736, every reasonable officer would have known that he lacked
a reasonable belief that Graham was an emergent danger to herself or others, see
Wesby, 138 S. Ct. at 590 (explaining that, for the law to be clearly established, a
reasonable officer must be able to interpret precedent “to establish the particular rule
the plaintiff seeks to apply” and to determine that such “legal principle clearly
prohibit[s] the officer’s conduct in the particular circumstances before him”).




                                         -18-
                                     *      *      *

       The “principle at the heart” of the clearly established requirement is that “state
actors are liable only for transgressing bright lines, not for making bad guesses in
gray areas.” L.G. ex rel. M.G. v. Columbia Pub. Schs., 990 F.3d 1145, 1148 (8th
Cir. 2021). For the foregoing reasons, we conclude that, in warrantlessly seizing
Graham for a mental-health evaluation, the officers may have made a bad guess in a
gray area, but they did not transgress any “bright lines” so as to lose the protection
of qualified immunity. Accordingly, we affirm the district court’s grant of qualified
immunity to the officers regarding Graham’s warrantless-seizure claim.

                                           C.

       Graham next claims that the district court erred in granting summary judgment
to the officers on Graham’s claim of retaliatory arrest because, according to Graham,
she presented sufficient evidence of retaliatory intent to create a triable issue of fact.
We disagree.

       “[T]he law is settled that as a general matter the First Amendment prohibits
government officials from subjecting an individual to retaliatory actions . . . for
speaking out.” Hoyland v. McMenomy, 869 F.3d 644, 655 (8th Cir. 2017). To
establish a First Amendment retaliatory-arrest claim, a plaintiff must show that
(1) she engaged in protected activity, (2) a government official took an adverse
action against her that would chill a person of ordinary firmness from continuing in
the activity, (3) the adverse action was caused by the exercise of the protected
activity, and (4) the government official lacked probable cause or arguable probable
cause. Peterson v. Kopp, 754 F.3d 594, 602 (8th Cir. 2014).

       To survive summary judgment, a plaintiff must show that a reasonable jury
could find that a retaliatory motive of the government official was a “but-for cause”
of the adverse action, “meaning that the adverse action against the plaintiff would
not have been taken absent the retaliatory motive.” Nieves v. Bartlett, 587 U.S. ---,


                                          -19-
139 S. Ct. 1715, 1722 (2019) (“It is not enough to show that an official acted with a
retaliatory motive and that the plaintiff was injured—the motive must cause the
injury.”). “The causal connection is generally a jury question, but it can provide a
basis for summary judgment when the question is so free from doubt as to justify
taking it from the jury.” Revels v. Vincenz, 382 F.3d 870, 876 (8th Cir. 2004)
(internal quotation marks omitted).

       For instance, in Baribeau, we denied officers qualified immunity on a claim
of unreasonable seizure when they arrested and detained protestors without arguable
probable cause to believe the protestors either engaged in disorderly conduct or
displayed a simulated bomb. 596 F.3d at 481. Even so, we granted the officers
summary judgment on the plaintiffs’ retaliatory-arrest claim because no “reasonable
jury could find that retaliatory animus was a . . . ‘but-for’ cause” of the arrests where
the evidence demonstrated that the officers made the arrest after observing a young
girl become frightened by the plaintiffs’ appearance, and because the evidence
demonstrated that the decision to arrest the plaintiffs was “based on an actual but
overly exaggerated belief that the plaintiffs violated the WMD statute.” Id.

       Given the information available to the officers in this case, we likewise
determine that no reasonable jury could conclude that retaliatory animus was a but-
for cause of Graham’s arrest. As in Baribeau, there is no evidence that the officers’
actions were based on anything other than perhaps “an actual but overly exaggerated
belief” that Graham was experiencing a mental-health emergency and presented a
threat either to herself or to others. And though the temporal proximity of Graham’s
protected activity and her subsequent arrest is relevant, it is not enough on its own
to create a triable issue of fact regarding cause where no other record evidence
supports finding a retaliatory motive and there is evidence that the officers acted in
good faith. See Wilson v. Northcutt, 441 F.3d 586, 592 (8th Cir. 2006) (“Temporal
proximity is relevant but not dispositive.”); see also Williams v. City of Carl
Junction, 480 F.3d 871, 877-78 (8th Cir. 2007) (holding that the plaintiff had not
demonstrated retaliatory animus sufficient to support a retaliatory-prosecution claim
under the First Amendment where he “presented no evidence”—other than the


                                          -20-
traffic ticket itself—“that the officer who issued [the] citation harbored any
retaliatory animus against him”).

     Thus, the district court properly granted the officers summary judgment on
Graham’s retaliatory-arrest claim.

                                          D.

       Graham next contends that the City’s policy concerning seizures for an
emergency mental-health evaluation caused the officers to violate her Fourth
Amendment rights because the policy was facially unconstitutional. In the
alternative, Graham argues that the City should be liable because it was
deliberatively indifferent to her constitutional rights and failed to train the officers
properly. We conclude that the district court did not err in granting the City
summary judgment.

       “A municipality may be liable under § 1983 where ‘action pursuant to official
municipal policy of some nature caused a constitutional tort.’” Hollingsworth v. City
of St. Ann, 800 F.3d 985, 991-92 (8th Cir. 2015) (quoting Monell, 436 U.S. at 691).
When a city’s policy is facially unconstitutional, we have recognized that “resolving
[the] issues of fault and causation is straightforward.” Szabla v. City of Brooklyn
Park, 486 F.3d 385, 389-90 (8th Cir. 2007) (en banc). In that instance, “[t]o establish
a constitutional violation, no evidence is needed other than a statement of the
municipal policy and its exercise.” Id.

       The relevant portion of the MCCTA provides that an officer may seize a
person for an emergency mental-health evaluation and transport that person to “a
licensed physician or treatment facility if the officer has reason to believe . . . that
the person is mentally ill . . . and in danger of injuring self or others if not
immediately detained.” Minn. Stat. § 253B.05, subd. 2(a) (emphasis added). In
compliance with the statute, the City’s policy allows an officer to take a person with
mental illness into custody “if there is a reason to believe the person poses a threat


                                         -21-
to himself or others.” The policy further directs that “[t]he threat does not have to
be imminent.”

       The district court initially denied the City summary judgment, determining
that the phrase “reason to believe” was inconsistent with the Fourth Amendment’s
probable-cause requirement for a mental-health seizure. After the City filed a
motion for reconsideration, the district court determined that it had “made a manifest
error of law” by failing to construe the phrase “reason to believe” to require probable
cause.

       We agree that the policy is not facially unconstitutional. First, “reason to
believe” is commonly used to mean probable cause. For instance, in United States
v. Quintana, we analyzed the meaning of the phrase “reason to believe” in a federal
immigration statute relating to arrests of undocumented aliens and concluded that
the phrase means “constitutionally required probable cause.” 623 F.3d 1237, 1239
(8th Cir. 2010); see also United States v. Stead, 422 F.2d 183, 184 n.1 (8th Cir. 1970)
(per curiam) (“Probable cause exists since a prudent man would have had reason to
believe that this defendant had committed a felony.”). Other circuits have come to
similar conclusions when interpreting statutes governing mental-health seizures. In
Cantrell, for example, the Fifth Circuit interpreted the Texas Health and Safety
Code’s use of “reason to believe” to require probable cause. 666 F.3d at 923.

       Second, the policy’s language stating that the threat presented “does not have
to be imminent” does not make the policy facially unconstitutional. To be sure, a
mental-health seizure must be justified by probable cause that the person subject to
the arrest presents an emergent threat of harm to herself or others, but government
officials need not wait to intervene until an individual is a split second away from
harming herself or others. See Meyers v. Comm’r of Soc. Sec. Admin., 801 F. App’x
90, 95 (4th Cir. 2020) (per curiam) (“‘Imminent’ means ‘threatening to occur
immediately; dangerously impending’ or ‘[a]bout to take place.’” (quoting Black’s
Law Dictionary (11th ed. 2019)); United States v. Hardeman, 449 F. App’x 408, 410
(5th Cir. 2011) (per curiam) (defining imminent as “impending; on the point of


                                         -22-
happening”). The Fourth Amendment does not demand that police wait until a
suicidal citizen has raised a gun to her temple before officers may intervene. See
Caniglia, 141 S. Ct. at 1604 (Kavanaugh, J., concurring) (explaining that “the
Court’s exigency precedents” do not require that the harm be “mere moments
away”). Instead, it requires only that a prudent person would have reason to believe
that the individual subject to the seizure presents a threat to herself or others such
that an order of a court or other authority cannot be obtained in time to prevent the
anticipated harm or injury. See Michigan v. Tyler, 436 U.S. 499, 509 (1978)
(explaining that police may rely on the exigent-circumstances or emergency-aid
exceptions when “there is compelling need for official action and no time to secure
a warrant”); Caniglia, 141 S. Ct. at 1602 (Alito, J., concurring) (noting that
circumstances are “exigent” when “there is not enough time to get a warrant”). As
a result, the policy is not facially unconstitutional because it does “not affirmatively
sanction” an unconstitutional action. See Szabla, 486 F.3d at 392.

       Where an official policy is lawful on its face, a plaintiff nevertheless may
establish liability by showing that a municipality caused the constitutional violation
by providing “inadequate training” for its employees. Parrish v. Ball, 594 F.3d 993,
997 (8th Cir. 2010). To establish such liability, a plaintiff must show that (1) the
municipality’s “training practices [were] inadequate,” (2) the municipality was
“deliberately indifferent” to the plaintiff’s rights when adopting the training
practices such that the “failure to train reflects a deliberate or conscious choice,” and
(3) the plaintiff’s injury was “actually caused” by the “alleged deficiency” in the
training practices. Id.

        Graham has not met this standard for two reasons. First, she advances no
evidence concerning other mental-health seizures, so she has not shown a history of
the City’s officers committing unreasonable seizures such that the need for
additional training was plain. See Bd. of Cnty. Comm’rs of Bryan Cnty. v. Brown,
520 U.S. 397, 407-08 (1997). The Supreme Court has held that a “pattern of similar
constitutional violations” is “ordinarily necessary” to establish municipal
liability, Connick v. Thompson, 563 U.S. 51, 62 (2011), unless “the need for more


                                          -23-
or different training is so obvious and the inadequacy [is] so likely to result in the
violation of constitutional rights” that the municipality can be said to have been
“deliberatively indifferent to the need,” City of Canton v. Harris, 489 U.S. 378, 390
(1989). Here, there is no evidence of past violations, and what happened to Graham
is not “so obviously” the consequence of a systemic lack of training, as opposed to
the decisions of individual officers, that the need for different or additional training
was plain. See Dick v. Watonwan Cnty., 738 F.2d 939, 942 (8th Cir. 1984) (noting
that an “isolated incident” is “not enough to establish a policy or custom”).

       Second, “the lack of clarity in the law” concerning the appropriate standard of
cause needed to justify a mental-health hold “precludes a finding that the
municipality had an unconstitutional policy at all, because its policymakers cannot
properly be said to have exhibited a policy of deliberate indifference to
constitutional rights that were not clearly established.” Szabla, 486 F.3d at 394; see
also Hollingsworth, 800 F.3d at 992 (“While a single constitutional violation arising
out of a lack of safeguards or training may be sufficient to establish deliberate
indifference where the need for such safeguards or training is obvious, a
municipality cannot exhibit fault rising to the level of deliberate indifference to a
constitutional right when that right has not yet been clearly established.” (internal
quotation marks omitted)). In other words, because the right at issue was not clearly
established, Graham cannot meet the “demand that deliberate indifference in fact be
deliberate.” Arrington-Bey v. City of Bedford Heights, 858 F.3d 988, 995 (6th Cir.
2017) (discussing and adopting the Eighth Circuit’s approach).

       Accordingly, the district court correctly entered summary judgment in favor
of the City on Graham’s Monell claims.

                                          III.

       We next consider the district court’s grant of summary judgment to the
officers on Graham’s state-law claims. Graham contends that the district court
improperly granted summary judgment to the officers on her claims of false


                                         -24-
imprisonment, battery, assault, and negligence because it erroneously concluded that
they were entitled to statutory and official immunity under Minnesota law. We
review de novo the application of state statutory and official immunity. See Boudoin,
962 F.3d at 1044; Johnson v. City of Minneapolis, 901 F.3d 963, 972 (8th Cir. 2018).
We conclude that the district court did not err.

      The MCCTA includes a statute-specific immunity section that provides:

      All persons acting in good faith, upon either actual knowledge or
      information thought by them to be reliable, who act pursuant to any
      provision of this chapter or who procedurally or physically assist in the
      commitment of any individual, pursuant to this chapter, are not subject
      to any civil or criminal liability under this chapter.

Minn. Stat. § 253B.23, subd. 4. Thus, all persons who in good faith participate in
the civil-commitment process, including by seizing someone for an emergency
mental-health evaluation, are immune from any civil or criminal liability, regardless
of whether the detained person is actually committed. Losen v. Allina Health Sys.,
767 N.W.2d 703, 709 (Minn. Ct. App. 2009) (holding that the MCCTA
“encompasses the good-faith decision whether to place an emergency hold on a
proposed patient, even if the result of that decision is that no hold is placed”). The
grant of immunity provides complete immunity from suit. Dokman v. Cnty. of
Hennepin, 637 N.W.2d 286, 297 (Minn. Ct. App. 2001).

       Just as Graham has not demonstrated a triable issue of fact as to whether the
officers had the requisite retaliatory animus to support her First Amendment
retaliatory-arrest claim, she has not shown a triable issue of fact regarding the good-
faith belief of the officers when they seized her for a mental-health evaluation. See
supra Section II.C. She simply advances no evidence that the officers acted in bad
faith. They are thus entitled to statutory immunity.

     For similar reasons, the officers also are entitled to official immunity. Under
Minnesota law, a public official is entitled to official immunity when his conduct


                                         -25-
requires the exercise of discretion or judgment and there is no evidence that he acted
maliciously or in bad faith. Johnson v. Morris, 453 N.W.2d 31, 41 (Minn. 1990);
Elwood v. Rice Cnty., 423 N.W.2d 671, 679 (Minn. 1988). “In determining whether
an official has committed a malicious wrong, we consider whether the official has
intentionally committed an act that he or she had reason to believe is prohibited.”
Hassan v. City of Minneapolis, 489 F.3d 914, 920 (8th Cir. 2007). Here, the officers
could not have acted in a manner that they believed to be unlawful when seizing
Graham because, as discussed above, the law was not clearly established. See id.

                                         IV.

     For the foregoing reasons, we affirm the district court’s grant of summary
judgment.
                          __________________________




                                        -26-

```

---

## GROUP: _overhaul2/lake/cases/Graham v. Connor.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Graham v. Connor"
type: case
citation: "490 U.S. 386 (1989)"
parallel_cite: "109 S. Ct. 1865; 104 L. Ed. 2d 443; 57 U.S.L.W. 4513"
neutral_cite: 1989 U.S. LEXIS 2467
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-05-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-05-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Graham v. Connor
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112257/graham-v-connor/"
  cluster_id: 112257
  opinion_id: 112257
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Anchor"
related: ["[[Tennessee v. Garner]]", "[[Scott v. Harris]]", "[[Saucier v. Katz]]"]
aliases: []
tags: ["case", "fourth-amendment", "excessive-force", "section-1983", "objective-reasonableness", "seizure"]
holding: "Excessive-force § 1983 claims arising from an arrest, stop, or other seizure are analyzed under the Fourth Amendment's 'objective…"
lake:
  record_id: Graham v. Connor
  status: verified
  projected_at: 2026-07-09
---

# Graham v. Connor

*490 U.S. 386 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Graham, a diabetic, asked a friend to drive him to a store for orange juice to counter an insulin reaction. Seeing Graham hurry in and out, Officer Connor made an investigative stop. During the encounter officers handcuffed Graham, disregarded explanations about his diabetic condition, and used force that caused injuries. Graham sued under § 1983 for excessive force. The lower courts analyzed the claim under a substantive-due-process "good faith / malicious and sadistic" test drawn from *[[Johnson v. Glick]]*.

## Issue
What constitutional standard governs a § 1983 claim that law enforcement officers used excessive force in the course of an arrest, investigatory stop, or other seizure.

## Rule
Such claims are governed by the Fourth Amendment's objective-reasonableness standard, not substantive due process. "[A]ll claims that law enforcement officers have used excessive force — deadly or not — in the course of an arrest, investigatory stop, or other 'seizure' of a free citizen should be analyzed under the Fourth Amendment and its 'reasonableness' standard, rather than under a 'substantive due process' approach." — 490 U.S. at 395. ^pin-395

Reasonableness is judged objectively and from the officer's on-scene vantage: "The 'reasonableness' of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight." — *Id.* at 396. ^pin-396

The inquiry weighs the facts of each case, "including the severity of the crime at issue, whether the suspect poses an immediate threat to the safety of the officers or others, and whether he is actively resisting arrest or attempting to evade arrest by flight." — [*Id.*](https://www.courtlistener.com/opinion/112257/graham-v-connor/#:~:text=including%20the%20severity%20of%20the) ^pin-396a

## Application
Graham's claim arose from an investigatory stop and the force used during it — a Fourth Amendment "seizure" — so it had to be assessed under the objective-reasonableness standard rather than the *[[Johnson v. Glick]]* due-process test the Court of Appeals applied. Because the lower courts used a standard turning on the officers' subjective good or bad faith, the case was [[Reading and Citing Cases#on-remand|remanded]] for analysis under the proper Fourth Amendment framework.

## Conclusion
Excessive-force claims arising from a seizure are governed by Fourth Amendment objective reasonableness; the judgment applying a substantive-due-process test was [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Graham*'s objective-reasonableness standard and three-factor balancing govern excessive-force claims and frame the merits question in qualified-immunity analysis; it builds on [[Tennessee v. Garner]].

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Anchor*

## Sources
- *Graham v. Connor*, 490 U.S. 386 (1989) — https://www.courtlistener.com/opinion/112257/graham-v-connor/ — pinpoints: 395, 396.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "34e289300c134906", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Graham v. Connor"}, "payload": {"all": [{"cite": "490 U.S. 386", "page": "386", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "490"}, {"cite": "109 S. Ct. 1865", "page": "1865", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "104 L. Ed. 2d 443", "page": "443", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "1989 U.S. LEXIS 2467", "page": "2467", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1989"}, {"cite": "57 U.S.L.W. 4513", "page": "4513", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "57"}], "display": "490 U.S. 386", "official": {"cite": "490 U.S. 386", "page": "386", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "490"}, "official_selection_present": true, "record_id": "Graham v. Connor"}}
{"assertion_id": "8d33102d2ee42bbb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-396", "record_id": "Graham v. Connor"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-396", "pinpoint_status": "slip-only", "quote": "The 'reasonableness' of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight.", "quote_fidelity": "mismatch", "record_id": "Graham v. Connor", "star_marker": null}}
{"assertion_id": "d82c528653841427", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-396a", "record_id": "Graham v. Connor"}, "payload": {"fragment": "#:~:text=including%20the%20severity%20of%20the", "page": null, "pin_id": "pin-396a", "pinpoint_status": "star-verified", "quote": "including the severity of the crime at issue, whether the suspect poses an immediate threat to the safety of the officers or others, and whether he is actively resisting arrest or attempting to evade arrest by flight.", "quote_fidelity": "matched", "record_id": "Graham v. Connor", "star_marker": "396"}}
{"assertion_id": "dcda0beea11e9882", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-395", "record_id": "Graham v. Connor"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-395", "pinpoint_status": "slip-only", "quote": "test drawn from *Johnson v. Glick*. ## Issue What constitutional standard governs a § 1983 claim that law enforcement officers used excessive force in the course of an arrest, investigatory stop, or other seizure. ## Rule Such claims are governed by the Fourth Amendment's objective-reasonableness standard, not substantive due process.", "quote_fidelity": "mismatch", "record_id": "Graham v. Connor", "star_marker": null}}
{"assertion_id": "8fc0f62aa84d4c5f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Graham v. Connor"}, "payload": {"as_of_content": "1989-05-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Graham v. Connor", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Graham v. Connor

```json
{
  "schema_version": "s2.v1",
  "record_id": "Graham v. Connor",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Graham v. Connor",
    "case_name_short": "Graham",
    "case_name_full": "GRAHAM v. CONNOR Et Al.",
    "input_case_name": "Graham v. Connor",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-05-15",
    "year": 1989,
    "docket": null,
    "cluster_id": 112257,
    "lead_opinion_id": 112257,
    "sibling_ids": [
      112257,
      9431666,
      9431667
    ],
    "absolute_url": "/opinion/112257/graham-v-connor/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9083940,
        "score": 20,
        "case_name": "Graham v. Connor"
      },
      {
        "cluster_id": 9083939,
        "score": 20,
        "case_name": "Graham v. Connor"
      },
      {
        "cluster_id": 9083419,
        "score": 20,
        "case_name": "Graham v. Connor"
      },
      {
        "cluster_id": 9083418,
        "score": 20,
        "case_name": "Graham v. Connor"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "490 U.S. 386",
      "volume": "490",
      "reporter": "U.S.",
      "page": "386",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1865",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1865",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 L. Ed. 2d 443",
        "volume": "104",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4513",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4513",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 2467",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "2467",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "490 U.S. 386",
        "volume": "490",
        "reporter": "U.S.",
        "page": "386",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1865",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1865",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 L. Ed. 2d 443",
        "volume": "104",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 2467",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "2467",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4513",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4513",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "490 U.S. 386",
    "official_selection": {
      "court_class": "scotus",
      "selected": "490 U.S. 386",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-395",
      "page": null,
      "quote": "test drawn from *Johnson v. Glick*. ## Issue What constitutional standard governs a \u00a7 1983 claim that law enforcement officers used excessive force in the course of an arrest, investigatory stop, or other seizure. ## Rule Such claims are governed by the Fourth Amendment's objective-reasonableness standard, not substantive due process.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-396",
      "page": null,
      "quote": "The 'reasonableness' of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-396a",
      "page": null,
      "quote": "including the severity of the crime at issue, whether the suspect poses an immediate threat to the safety of the officers or others, and whether he is actively resisting arrest or attempting to evade arrest by flight.",
      "star_marker": "396",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19548,
      "fragment": "#:~:text=including%20the%20severity%20of%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-05-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Graham v. Connor",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Scott v. Harris",
          "cluster_id": 145738,
          "cite": [
            "167 L. Ed. 2d 686",
            "127 S. Ct. 1769",
            "550 U.S. 372",
            "2007 U.S. LEXIS 4748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albright v. Oliver",
          "cluster_id": 112924,
          "cite": [
            "127 L. Ed. 2d 114",
            "114 S. Ct. 807",
            "510 U.S. 266",
            "1994 U.S. LEXIS 1319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Seiter",
          "cluster_id": 112626,
          "cite": [
            "115 L. Ed. 2d 271",
            "111 S. Ct. 2321",
            "501 U.S. 294",
            "1991 U.S. LEXIS 3490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Sacramento v. Lewis",
          "cluster_id": 118214,
          "cite": [
            "140 L. Ed. 2d 1043",
            "118 S. Ct. 1708",
            "523 U.S. 833",
            "1998 U.S. LEXIS 3404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Lacey v. Joseph Arpaio",
          "cluster_id": 807646,
          "cite": [
            "693 F.3d 896"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tolan v. Cotton",
          "cluster_id": 2672535,
          "cite": [
            "188 L. Ed. 2d 895",
            "134 S. Ct. 1861",
            "2014 U.S. LEXIS 3112",
            "82 U.S.L.W. 4358",
            "572 U.S. 650",
            "88 Fed. R. Serv. 3d 765",
            "24 Fla. L. Weekly Fed. S 731",
            "2014 WL 1757856"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kingsley v. Hendrickson",
          "cluster_id": 2811847,
          "cite": [
            "576 U.S. 389",
            "135 S. Ct. 2466",
            "192 L. Ed. 2d 416",
            "2015 U.S. LEXIS 4073",
            "25 Fla. L. Weekly Fed. S 401",
            "83 U.S.L.W. 4515"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Koon v. United States",
          "cluster_id": 118044,
          "cite": [
            "135 L. Ed. 2d 392",
            "116 S. Ct. 2035",
            "518 U.S. 81",
            "1996 U.S. LEXIS 3877"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullenix v. Luna",
          "cluster_id": 3153112,
          "cite": [
            "577 U.S. 7",
            "136 S. Ct. 305",
            "193 L. Ed. 2d 255",
            "2015 U.S. LEXIS 7160",
            "84 U.S.L.W. 4003",
            "25 Fla. L. Weekly Fed. S 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City of Los Angeles",
          "cluster_id": 7092482,
          "cite": [
            "250 F.3d 668",
            "2001 WL 468408"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brosseau v. Haugen",
          "cluster_id": 137736,
          "cite": [
            "160 L. Ed. 2d 583",
            "125 S. Ct. 596",
            "543 U.S. 194",
            "2004 U.S. LEXIS 8275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thaddeus-X and Earnest Bell, Jr. v. Blatter",
          "cluster_id": 763587,
          "cite": [
            "175 F.3d 378",
            "1999 U.S. App. LEXIS 3497",
            "1999 WL 114379"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Pauly",
          "cluster_id": 4374579,
          "cite": [
            "580 U.S. 73",
            "196 L. Ed. 2d 463",
            "2017 U.S. LEXIS 5",
            "137 S. Ct. 548",
            "26 Fla. L. Weekly Fed. S 409",
            "85 U.S.L.W. 4027",
            "2017 WL 69170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City Of Los Angeles",
          "cluster_id": 773312,
          "cite": [
            "250 F.3d 668",
            "2001 Cal. Daily Op. Serv. 3507",
            "2001 Daily Journal DAR 4351",
            "56 Fed. R. Serv. 698",
            "2001 U.S. App. LEXIS 8150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Christopher J. Weiland v. Palm Beach County Sheriff's Office",
          "cluster_id": 2815299,
          "cite": [
            "792 F.3d 1313",
            "92 Fed. R. Serv. 3d 378",
            "2015 U.S. App. LEXIS 11750",
            "2015 WL 4098270"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 4247081,
          "cite": [
            "833 F.3d 1060",
            "2016 U.S. App. LEXIS 14950",
            "2016 WL 4268955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lanier",
          "cluster_id": 118098,
          "cite": [
            "137 L. Ed. 2d 432",
            "117 S. Ct. 1219",
            "520 U.S. 259",
            "1997 U.S. LEXIS 2079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen King v. Eric Taylor",
          "cluster_id": 808337,
          "cite": [
            "694 F.3d 650",
            "2012 WL 3968371",
            "2012 U.S. App. LEXIS 19109"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tracy v. Freshwater",
          "cluster_id": 177179,
          "cite": [
            "623 F.3d 90",
            "2010 U.S. App. LEXIS 21238",
            "2010 WL 4008747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisela v. Hughes",
          "cluster_id": 4482892,
          "cite": [
            "584 U.S. 100",
            "138 S. Ct. 1148",
            "200 L. Ed. 2d 449",
            "2018 U.S. LEXIS 2066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plumhoff v. Rickard",
          "cluster_id": 2675750,
          "cite": [
            "188 L. Ed. 2d 1056",
            "134 S. Ct. 2012",
            "2014 U.S. LEXIS 3816",
            "82 U.S.L.W. 4394",
            "572 U.S. 765",
            "24 Fla. L. Weekly Fed. S 790",
            "2014 WL 2178335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
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
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112257 OR 9431666 OR 9431667) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzA2ODMyMDAwMDAwJnM9OTQ3MTU4NyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112257+OR+9431666+OR+9431667%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      },
      "lane2_top_cited": {
        "query": "cites:(112257 OR 9431666 OR 9431667)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDI4JnM9MjgwMTQzNSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112257+OR+9431666+OR+9431667%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112257 OR 9431666 OR 9431667)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzI4MzQ1NjAwMDAwJnM9MTAxMzE3NjMmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112257+OR+9431666+OR+9431667%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112257 OR 9431666 OR 9431667)",
    "indexed_citing_opinions": 5378,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112257,
        "count": 4465,
        "count_source": "search"
      },
      {
        "opinion_id": 9431666,
        "count": 1007,
        "count_source": "search"
      },
      {
        "opinion_id": 9431667,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 16638,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/graham-v-connor.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjY2MDU5MSZzPTg3MTI4MzImdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28112257+OR+9431666+OR+9431667%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112257,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 109561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 110132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 111610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 312370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 459830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 493625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 498147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 1558828,
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
    "date_created": "2026-07-05T05:51:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:52:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:52:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:55:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:52:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Graham v. Connor

```
<div>
<center><b><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span> (1989)</b></center>
<center><h1>GRAHAM<br>
v.<br>
CONNOR ET AL.</h1></center>
<center>No. 87-6571.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 21, 1989</center>
<center>Decided May 15, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FOURTH CIRCUIT
<p><span class="star-pagination">*388</span> <i>H. Gerald Beaver</i> argued the cause for petitioner. On the briefs was <i>Richard B. Glazier.</i></p>
<p><i>Mark I. Levy</i> argued the cause for respondents. On the brief was <i>Frank B. Aycock III.</i><sup>[*]</sup></p>
<p><i>Lacy H. Thornburg,</i> Attorney General of North Carolina, <i>Isaac T. Avery III,</i> Special Deputy Attorney General, and <i>Linda Anne Morris,</i> Assistant Attorney General, filed a brief for the State of North Carolina as <i>amicus curiae</i> urging affirmance.</p>
<p>CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>This case requires us to decide what constitutional standard governs a free citizen's claim that law enforcement officials used excessive force in the course of making an arrest, investigatory stop, or other "seizure" of his person. We hold that such claims are properly analyzed under the Fourth Amendment's "objective reasonableness" standard, rather than under a substantive due process standard.</p>
<p>In this action under <span class="citation no-link">42 U. S. C. § 1983</span>, petitioner Dethorne Graham seeks to recover damages for injuries allegedly sustained when law enforcement officers used physical force against him during the course of an investigatory stop. Because the case comes to us from a decision of the Court of Appeals affirming the entry of a directed verdict for respondents, we take the evidence hereafter noted in the light most favorable to petitioner. On November 12, 1984, Graham, a diabetic, felt the onset of an insulin reaction. He asked a friend, William Berry, to drive him to a nearby convenience store so he could purchase some orange juice to counteract the reaction. Berry agreed, but when Graham entered the store, he saw a number of people ahead of him in the checkout <span class="star-pagination">*389</span> line. Concerned about the delay, he hurried out of the store and asked Berry to drive him to a friend's house instead.</p>
<p>Respondent Connor, an officer of the Charlotte, North Carolina, Police Department, saw Graham hastily enter and leave the store. The officer became suspicious that something was amiss and followed Berry's car. About one-half mile from the store, he made an investigative stop. Although Berry told Connor that Graham was simply suffering from a "sugar reaction," the officer ordered Berry and Graham to wait while he found out what, if anything, had happened at the convenience store. When Officer Connor returned to his patrol car to call for backup assistance, Graham got out of the car, ran around it twice, and finally sat down on the curb, where he passed out briefly.</p>
<p>In the ensuing confusion, a number of other Charlotte police officers arrived on the scene in response to Officer Connor's request for backup. One of the officers rolled Graham over on the sidewalk and cuffed his hands tightly behind his back, ignoring Berry's pleas to get him some sugar. Another officer said: "I've seen a lot of people with sugar diabetes that never acted like this. Ain't nothing wrong with the M. F. but drunk. Lock the S. B. up." App. 42. Several officers then lifted Graham up from behind, carried him over to Berry's car, and placed him face down on its hood. Regaining consciousness, Graham asked the officers to check in his wallet for a diabetic decal that he carried. In response, one of the officers told him to "shut up" and shoved his face down against the hood of the car. Four officers grabbed Graham and threw him headfirst into the police car. A friend of Graham's brought some orange juice to the car, but the officers refused to let him have it. Finally, Officer Connor received a report that Graham had done nothing wrong at the convenience store, and the officers drove him home and released him.</p>
<p><span class="star-pagination">*390</span> At some point during his encounter with the police, Graham sustained a broken foot, cuts on his wrists, a bruised forehead, and an injured shoulder; he also claims to have developed a loud ringing in his right ear that continues to this day. He commenced this action under <span class="citation no-link">42 U. S. C. § 1983</span> against the individual officers involved in the incident, all of whom are respondents here,<sup>[1]</sup> alleging that they had used excessive force in making the investigatory stop, in violation of "rights secured to him under the Fourteenth Amendment to the United States Constitution and <span class="citation no-link">42 U. S. C. § 1983</span>." Complaint ¶ 10, App. 5.<sup>[2]</sup> The case was tried before a jury. At the close of petitioner's evidence, respondents moved for a directed verdict. In ruling on that motion, the District Court considered the following four factors, which it identified as "[t]he factors to be considered in determining when the excessive use of force gives rise to a cause of action under § 1983": (1) the need for the application of force; (2) the relationship between that need and the amount of force that was used; (3) the extent of the injury inflicted; and (4) "[w]hether the force was applied in a good faith effort to maintain and restore discipline or maliciously and sadistically for the very purpose of causing harm." <span class="citation" data-id="1558828"><a href="/opinion/1558828/graham-v-city-of-charlotte/#248" aria-description="Citation for case: Graham v. City of Charlotte">644 F. Supp. 246, 248</a></span> (WDNC 1986). Finding that the amount of force used by the officers was "appropriate under the circumstances," that "[t]here was no discernable injury inflicted," and that the force used "was not applied maliciously or sadistically for the very purpose of causing harm," but in "a good faith effort to maintain or restore order in the face of a potentially explosive <span class="star-pagination">*391</span> situation." <span class="citation" data-id="1558828"><a href="/opinion/1558828/graham-v-city-of-charlotte/#248" aria-description="Citation for case: Graham v. City of Charlotte"><i>id.,</i> at 248-249</a></span>, the District Court granted respondents' motion for a directed verdict.</p>
<p>A divided panel of the Court of Appeals for the Fourth Circuit affirmed. <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d 945</a></span> (1987). The majority ruled first that the District Court had applied the correct legal standard in assessing petitioner's excessive force claim. <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B...."><i>Id.,</i> at 948-949</a></span>. Without attempting to identify the specific constitutional provision under which that claim arose,<sup>[3]</sup> the majority endorsed the four-factor test applied by the District Court as generally applicable to all claims of "constitutionally excessive force" brought against governmental officials. <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B...."><i>Id.,</i> at 948</a></span>. The majority rejected petitioner's argument, based on Circuit precedent,<sup>[4]</sup> that it was error to require him to prove that the allegedly excessive force used against him was applied "maliciously and sadistically for the very purpose of causing harm."<sup>[5]</sup><i><span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">Ibid.</a></span></i> Finally, the majority held that a reasonable jury applying the four-part test it had just endorsed <span class="star-pagination">*392</span> to petitioner's evidence "could not find that the force applied was constitutionally excessive." <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#949" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B...."><i>Id.,</i> at 949-950</a></span>. The dissenting judge argued that this Court's decisions in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), and <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), required that excessive force claims arising out of investigatory stops be analyzed under the Fourth Amendment's "objective reasonableness" standard. <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#950" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 950-952</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./488/816/">488 U. S. 816</a></span> (1988), and now reverse.</p>
<p>Fifteen years ago, in <i>Johnson</i> v. <i>Glick,</i> <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">481 F. 2d 1028</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1033/">414 U. S. 1033</a></span> (1973), the Court of Appeals for the Second Circuit addressed a § 1983 damages claim filed by a pretrial detainee who claimed that a guard had assaulted him without justification. In evaluating the detainee's claim, Judge Friendly applied neither the Fourth Amendment nor the Eighth, the two most textually obvious sources of constitutional protection against physically abusive governmental conduct.<sup>[6]</sup> Instead, he looked to "substantive due process," holding that "quite apart from any `specific' of the Bill of Rights, application of undue force by <span class="star-pagination">*393</span> law enforcement officers deprives a suspect of liberty without due process of law." <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1032" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1032</a></span>. As support for this proposition, he relied upon our decision in <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952), which used the Due Process Clause to void a state criminal conviction based on evidence obtained by pumping the defendant's stomach. <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1032" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1032-1033</a></span>. If a police officer's use of force which "shocks the conscience" could justify setting aside a criminal conviction, Judge Friendly reasoned, a correctional officer's use of similarly excessive force must give rise to a due process violation actionable under § 1983. <i>Ibid.</i> Judge Friendly went on to set forth four factors to guide courts in determining "whether the constitutional line has been crossed" by a particular use of force  the same four factors relied upon by the courts below in this case. <i>Id.,</i> at 1033.</p>
<p>In the years following <i>Johnson</i> v. <i><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></i><i>,</i> the vast majority of lower federal courts have applied its four-part "substantive due process" test indiscriminately to all excessive force claims lodged against law enforcement and prison officials under § 1983, without considering whether the particular application of force might implicate a more specific constitutional right governed by a different standard.<sup>[7]</sup> Indeed, many courts have seemed to assume, as did the courts below in this case, that there is a generic "right" to be free from excessive force, grounded not in any particular constitutional provision but rather in "basic principles of § 1983 jurisprudence."<sup>[8]</sup></p>
<p>We reject this notion that all excessive force claims brought under § 1983 are governed by a single generic standard. As we have said many times, § 1983 "is not itself a <span class="star-pagination">*394</span> source of substantive rights," but merely provides "a method for vindicating federal rights elsewhere conferred." <i>Baker</i> v. <i>McCollan,</i> <span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#144" aria-description="Citation for case: Baker v. McCollan">443 U. S. 137, 144, n. 3</a></span> (1979). In addressing an excessive force claim brought under § 1983, analysis begins by identifying the specific constitutional right allegedly infringed by the challenged application of force. See <i>id.,</i> at 140 ("The first inquiry in any § 1983 suit" is "to isolate the precise constitutional violation with which [the defendant] is charged").<sup>[9]</sup> In most instances, that will be either the Fourth Amendment's prohibition against unreasonable seizures of the person, or the Eighth Amendment's ban on cruel and unusual punishments, which are the two primary sources of constitutional protection against physically abusive governmental conduct. The validity of the claim must then be judged by reference to the specific constitutional standard which governs that right, rather than to some generalized "excessive force" standard. See <i>Tennessee</i> v. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner"><i>Garner, supra,</i> at 7-22</a></span> (claim of excessive force to effect arrest analyzed under a Fourth Amendment standard); <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#318" aria-description="Citation for case: Whitley v. Albers">475 U. S. 312, 318-326</a></span> (1986) (claim of excessive force to subdue convicted prisoner analyzed under an Eighth Amendment standard).</p>
<p>Where, as here, the excessive force claim arises in the context of an arrest or investigatory stop of a free citizen, it is most properly characterized as one invoking the protections of the Fourth Amendment, which guarantees citizens the right "to be secure in their persons . . . against unreasonable. . . seizures" of the person. This much is clear from our decision in <i>Tennessee</i> v. <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner, supra</a></span></i><i>.</i> In <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span>,</i> we addressed a claim that the use of deadly force to apprehend a fleeing suspect who did not appear to be armed or otherwise dangerous violated the suspect's constitutional rights, notwithstanding the existence of probable cause to arrest. <span class="star-pagination">*395</span> Though the complaint alleged violations of both the Fourth Amendment and the Due Process Clause, see <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#5" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 5</a></span>, we analyzed the constitutionality of the challenged application of force solely by reference to the Fourth Amendment's prohibition against unreasonable seizures of the person, holding that the "reasonableness" of a particular seizure depends not only on <i>when</i> it is made, but also on <i>how</i> it is carried out. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 7-8</a></span>. Today we make explicit what was implicit in <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i>'s analysis, and hold that <i>all</i> claims that law enforcement officers have used excessive force  deadly or not  in the course of an arrest, investigatory stop, or other "seizure" of a free citizen should be analyzed under the Fourth Amendment and its "reasonableness" standard, rather than under a "substantive due process" approach. Because the Fourth Amendment provides an explicit textual source of constitutional protection against this sort of physically intrusive governmental conduct, that Amendment, not the more generalized notion of "substantive due process," must be the guide for analyzing these claims.<sup>[10]</sup></p>
<p><span class="star-pagination">*396</span> Determining whether the force used to effect a particular seizure is "reasonable" under the Fourth Amendment requires a careful balancing of " `the nature and quality of the intrusion on the individual's Fourth Amendment interests' " against the countervailing governmental interests at stake. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#8" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 8</a></span>, quoting <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983). Our Fourth Amendment jurisprudence has long recognized that the right to make an arrest or investigatory stop necessarily carries with it the right to use some degree of physical coercion or threat thereof to effect it. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22-27</a></span>. Because "[t]he test of reasonableness under the Fourth Amendment is not capable of precise definition or mechanical application," <i>Bell</i> v. <i>Wolfish,</i> <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#559" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 559</a></span> (1979), however, its proper application requires careful attention to the facts and circumstances of each particular case, including the severity of the crime at issue, whether the suspect poses an immediate threat to the safety of the officers or others, and whether he is actively resisting arrest or attempting to evade arrest by flight. See <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#8" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 8-9</a></span> (the question is "whether the totality of the circumstances justifie[s] a particular sort of . . . seizure").</p>
<p>The "reasonableness" of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight. See <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 20-22</a></span>. The Fourth Amendment is not violated by an arrest based on probable cause, even though the wrong person is arrested, <i>Hill</i> v. <i>California,</i> <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U. S. 797</a></span> (1971), nor by the mistaken execution of a valid search warrant on the wrong premises, <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79</a></span> (1987). With respect to a claim of excessive force, the same standard of reasonableness at the moment applies: "Not every push or shove, even if it may later seem unnecessary in the peace of a judge's chambers," <i>Johnson</i> v. <i>Glick,</i> <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1033" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1033</a></span>, violates the Fourth Amendment. The calculus of reasonableness must embody <span class="star-pagination">*397</span> allowance for the fact that police officers are often forced to make split-second judgments  in circumstances that are tense, uncertain, and rapidly evolving  about the amount of force that is necessary in a particular situation.</p>
<p>As in other Fourth Amendment contexts, however, the "reasonableness" inquiry in an excessive force case is an objective one: the question is whether the officers' actions are "objectively reasonable" in light of the facts and circumstances confronting them, without regard to their underlying intent or motivation. See <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#137" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 137-139</a></span> (1978); see also <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 21</a></span> (in analyzing the reasonableness of a particular search or seizure, "it is imperative that the facts be judged against an objective standard"). An officer's evil intentions will not make a Fourth Amendment violation out of an objectively reasonable use of force; nor will an officer's good intentions make an objectively unreasonable use of force constitutional. See <i>Scott</i> v. <i>United States, supra,</i> at 138, citing <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973).</p>
<p>Because petitioner's excessive force claim is one arising under the Fourth Amendment, the Court of Appeals erred in analyzing it under the four-part <i>Johnson</i> v. <i><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></i> test. That test, which requires consideration of whether the individual officers acted in "good faith" or "maliciously and sadistically for the very purpose of causing harm," is incompatible with a proper Fourth Amendment analysis. We do not agree with the Court of Appeals' suggestion, see <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 948</a></span>, that the "malicious and sadistic" inquiry is merely another way of describing conduct that is objectively unreasonable under the circumstances. Whatever the empirical correlations between "malicious and sadistic" behavior and objective unreasonableness may be, the fact remains that the "malicious and sadistic" factor puts in issue the subjective motivations of the individual officers, which our prior cases make clear has no bearing on whether a particular seizure is "unreasonable" under the Fourth Amendment. Nor do we agree with the <span class="star-pagination">*398</span> Court of Appeals' conclusion, see <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B...."><i>id.,</i> at 948, n. 3</a></span>, that because the subjective motivations of the individual officers are of central importance in deciding whether force used against a convicted prisoner violates the Eighth Amendment, see <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 320-321</a></span>,<sup>[11]</sup> it cannot be reversible error to inquire into them in deciding whether force used against a suspect or arrestee violates the Fourth Amendment. Differing standards under the Fourth and Eighth Amendments are hardly surprising: the terms "cruel" and "punishments" clearly suggest some inquiry into subjective state of mind, whereas the term "unreasonable" does not. Moreover, the less protective Eighth Amendment standard applies "only after the State has complied with the constitutional guarantees traditionally associated with criminal prosecutions." <i>Ingraham</i> v. <i>Wright,</i> <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#671" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651, 671</a></span>, <span class="star-pagination">*399</span> n. 40 (1977). The Fourth Amendment inquiry is one of "objective reasonableness" under the circumstances, and subjective concepts like "malice" and "sadism" have no proper place in that inquiry.<sup>[12]</sup></p>
<p>Because the Court of Appeals reviewed the District Court's ruling on the motion for directed verdict under an erroneous view of the governing substantive law, its judgment must be vacated and the case remanded to that court for reconsideration of that issue under the proper Fourth Amendment standard.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BLACKMUN, with whom JUSTICE BRENNAN and JUSTICE MARSHALL join, concurring in part and concurring in the judgment.</p>
<p>I join the Court's opinion insofar as it rules that the Fourth Amendment is the primary tool for analyzing claims of excessive force in the prearrest context, and I concur in the judgment remanding the case to the Court of Appeals for reconsideration of the evidence under a reasonableness standard. In light of respondents' concession, however, that the pleadings in this case properly may be construed as raising a Fourth Amendment claim, see Brief for Respondents 3, I see no reason for the Court to find it necessary further to reach out to decide that prearrest excessive force claims are to be analyzed under the Fourth Amendment <i>rather than</i> under a <span class="star-pagination">*400</span> substantive due process standard. I also see no basis for the Court's suggestion, <i>ante,</i> at 395, that our decision in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), implicitly so held. Nowhere in <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> is a substantive due process standard for evaluating the use of excessive force in a particular case discussed; there is no suggestion that such a standard was offered as an alternative and rejected.</p>
<p>In this case, petitioner apparently decided that it was in his best interest to disavow the continued applicability of substantive due process analysis as an alternative basis for recovery in prearrest excessive force cases. See Brief for Petitioner 20. His choice was certainly wise as a matter of litigation strategy in his own case, but does not (indeed, cannot be expected to) serve other potential plaintiffs equally well. It is for that reason that the Court would have done better to leave that question for another day. I expect that the use of force that is not demonstrably unreasonable under the Fourth Amendment only rarely will raise substantive due process concerns. But until I am faced with a case in which that question is squarely raised, and its merits are subjected to adversary presentation, I do not join in foreclosing the use of substantive due process analysis in prearrest cases.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the United States by <i>Solicitor General Fried, Assistant Attorney General Reynolds, Deputy Assistant Attorney General Clegg, David L. Shapiro, Brian J. Martin,</i> and <i>David K. Flynn;</i> and for the American Civil Liberties Union et al. by <i>Steven R. Shapiro.</i></p>
<p>[1]  Also named as a defendant was the city of Charlotte, which employed the individual respondents. The District Court granted a directed verdict for the city, and petitioner did not challenge that ruling before the Court of Appeals. Accordingly, the city is not a party to the proceedings before this Court.</p>
<p>[2]  Petitioner also asserted pendent state-law claims of assault, false imprisonment, and intentional infliction of emotional distress. Those claims have been dismissed from the case and are not before this Court.</p>
<p>[3]  The majority did note that because Graham was not an incarcerated prisoner, "his complaint of excessive force did not, therefore, arise under the eighth amendment." <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 948, n. 3</a></span>. However, it made no further effort to identify the constitutional basis for his claim.</p>
<p>[4]  Petitioner's argument was based primarily on <i>Kidd</i> v. <i>O'Neil,</i> <span class="citation" data-id="459830"><a href="/opinion/459830/dennis-ray-kidd-v-robert-oneil-mike-lomonaco-fairfax-county-police-dept/" aria-description="Citation for case: Dennis Ray Kidd v. Robert O&#x27;Neil Mike Lomonaco Fairfax...">774 F. 2d 1252</a></span> (CA4 1985), which read this Court's decision in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), as mandating application of a Fourth Amendment "objective reasonableness" standard to claims of excessive force during arrest. See <span class="citation" data-id="459830"><a href="/opinion/459830/dennis-ray-kidd-v-robert-oneil-mike-lomonaco-fairfax-county-police-dept/#1254" aria-description="Citation for case: Dennis Ray Kidd v. Robert O&#x27;Neil Mike Lomonaco Fairfax...">774 F. 2d, at 1254-1257</a></span>. The reasoning of <i><span class="citation" data-id="459830"><a href="/opinion/459830/dennis-ray-kidd-v-robert-oneil-mike-lomonaco-fairfax-county-police-dept/" aria-description="Citation for case: Dennis Ray Kidd v. Robert O&#x27;Neil Mike Lomonaco Fairfax...">Kidd</a></span></i> was subsequently rejected by the en banc Fourth Circuit in <i>Justice</i> v. <i>Dennis,</i> <span class="citation" data-id="9476991"><a href="/opinion/498147/gary-w-justice-v-john-w-dennis-individually-and-in-his-official/#383" aria-description="Citation for case: Gary W. Justice v. John W. Dennis, Individually and in...">834 F. 2d 380, 383</a></span> (1987), cert. pending, No. 87-1422.</p>
<p>[5]  The majority noted that in <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">475 U. S. 312</a></span> (1986), we held that the question whether physical force used against convicted prisoners in the course of quelling a prison riot violates the Eighth Amendment "ultimately turns on `whether force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm.' " <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 948, n. 3</a></span>, quoting <i>Whitley</i> v. <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers"><i>Albers, supra,</i> at 320-321</a></span>. Though the Court of Appeals acknowledged that petitioner was not a convicted prisoner, it thought it "unreasonable . . . to suggest that a conceptual factor could be central to one type of excessive force claim but reversible error when merely considered by the court in another context." <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 948, n. 3</a></span>.</p>
<p>[6]  Judge Friendly did not apply the Eighth Amendment's Cruel and Unusual Punishments Clause to the detainee's claim for two reasons. First, he thought that the Eighth Amendment's protections did not attach until after conviction and sentence. <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1032" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1032</a></span>. This view was confirmed by <i>Ingraham</i> v. <i>Wright,</i> <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#671" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651, 671, n. 40</a></span> (1977) ("Eighth Amendment scrutiny is appropriate only after the State has complied with the constitutional guarantees traditionally associated with criminal prosecutions"). Second, he expressed doubt whether a "spontaneous attack" by a prison guard, done without the authorization of prison officials, fell within the traditional Eighth Amendment definition of "punishments." <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1032" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1032</a></span>. Although Judge Friendly gave no reason for not analyzing the detainee's claim under the Fourth Amendment's prohibition against "unreasonable . . . seizures" of the person, his refusal to do so was apparently based on a belief that the protections of the Fourth Amendment did not extend to pretrial detainees. See <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1033" aria-description="Citation for case: Johnson v. Glick"><i>id.,</i> at 1033</a></span> (noting that "most of the courts faced with challenges to the conditions of <i>pretrial</i> detention have primarily based their analysis directly on the due process clause"). See n. 10, <i>infra.</i></p>
<p>[7]  See Freyermuth, Rethinking Excessive Force, 1987 Duke L. J. 692, 694-696, and nn. 16-23 (1987) (collecting cases).</p>
<p>[8]  See <i>Justice</i> v. <i>Dennis, supra,</i> at 382 ("There are . . . certain basic principles in section 1983 jurisprudence as it relates to claims of excessive force that are beyond question [,] [w]hether the factual circumstances involve an arrestee, a pretrial detainee or a prisoner").</p>
<p>[9]  The same analysis applies to excessive force claims brought against federal law enforcement and correctional officials under <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971).</p>
<p>[10]  A "seizure" triggering the Fourth Amendment's protections occurs only when government actors have, "by means of physical force or show of authority, . . . in some way restrained the liberty of a citizen," <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19, n. 16</a></span> (1968); see <i>Brower</i> v. <i>County of Inyo,</i> <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#596" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593, 596</a></span> (1989).
</p>
<p>Our cases have not resolved the question whether the Fourth Amendment continues to provide individuals with protection against the deliberate use of excessive physical force beyond the point at which arrest ends and pretrial detention begins, and we do not attempt to answer that question today. It is clear, however, that the Due Process Clause protects a pretrial detainee from the use of excessive force that amounts to punishment. See <i>Bell</i> v. <i>Wolfish,</i> <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#535" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 535-539</a></span> (1979). After conviction, the Eighth Amendment "serves as the primary source of substantive protection . . . in cases . . . where the deliberate use of force is challenged as excessive and unjustified." <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#327" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 327</a></span>. Any protection that "substantive due process" affords convicted prisoners against excessive force is, we have held, at best redundant of that provided by the Eighth Amendment. <i><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">Ibid.</a></span></i></p>
<p>[11]  In <i><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">Whitley</a></span>,</i> we addressed a § 1983 claim brought by a convicted prisoner, who claimed that prison officials had violated his Eighth Amendment rights by shooting him in the knee during a prison riot. We began our Eighth Amendment analysis by reiterating the long-established maxim that an Eighth Amendment violation requires proof of the " ` "unnecessary and wanton infliction of pain." ' " <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#319" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 319</a></span>, quoting <i>Ingraham</i> v. <i>Wright,</i> <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#670" aria-description="Citation for case: Ingraham v. Wright">430 U. S., at 670</a></span>, in turn quoting <i>Estelle</i> v. <i>Gamble,</i> <span class="citation" data-id="9426610"><a href="/opinion/109561/estelle-v-gamble/#103" aria-description="Citation for case: Estelle v. Gamble">429 U. S. 97, 103</a></span> (1976). We went on to say that when prison officials use physical force against an inmate "to restore order in the face of a prison disturbance, . . . the question whether the measure taken inflicted unnecessary and wanton pain . . . <i>ultimately turns</i> on `whether the force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm.' " <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 320-321</a></span> (emphasis added), quoting <i>Johnson</i> v. <i>Glick,</i> <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1033" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1033</a></span>. We also suggested that the other prongs of the <i>Johnson</i> v. <i><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></i> test might be useful in analyzing excessive force claims brought under the Eighth Amendment. <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#321" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 321</a></span>. But we made clear that this was so <i>not</i> because Judge Friendly's four-part test is some talismanic formula generally applicable to all excessive force claims, but because its four factors help to focus the central inquiry in the Eighth Amendment context, which is whether the particular use of force amounts to the "unnecessary and wanton infliction of pain." See <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers"><i>id.,</i> at 320-321</a></span>. Our endorsement of the <i>Johnson</i> v. <i><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></i> test in <i><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">Whitley</a></span></i> thus had no implications beyond the Eighth Amendment context.</p>
<p>[12]  Of course, in assessing the credibility of an officer's account of the circumstances that prompted the use of force, a factfinder may consider, along with other factors, evidence that the officer may have harbored ill-will toward the citizen. See <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#139" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 139, n. 13</a></span> (1978). Similarly, the officer's <i>objective</i> "good faith"  that is, whether he could reasonably have believed that the force used did not violate the Fourth Amendment  may be relevant to the availability of the qualified immunity defense to monetary liability under § 1983. See <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635</a></span> (1987). Since no claim of qualified immunity has been raised in this case, however, we express no view on its proper application in excessive force cases that arise under the Fourth Amendment.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Griffin v. Wisconsin.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Griffin v. Wisconsin"
type: case
citation: "483 U.S. 868 (1987)"
parallel_cite: "107 S. Ct. 3164; 97 L. Ed. 2d 709; 55 U.S.L.W. 5156"
neutral_cite: 1987 U.S. LEXIS 2897
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-06-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Griffin v. Wisconsin
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111959/griffin-v-wisconsin/"
  cluster_id: 111959
  opinion_id: 9431137
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Knights]]", "[[Samson v. California]]", "[[New Jersey v. T.L.O.]]"]
aliases: []
tags: ["case", "fourth-amendment", "special-needs", "probation", "warrantless-search", "reasonable-grounds"]
holding: "A warrantless search of a probationer's home pursuant to a valid regulation is reasonable when supported by \"reasonable grounds\";…"
lake:
  record_id: Griffin v. Wisconsin
  status: verified
  projected_at: 2026-07-06
---

# Griffin v. Wisconsin

*483 U.S. 868 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Griffin was on probation in Wisconsin, where a state regulation permitted a probation officer, with supervisory approval, to search a probationer's home without a warrant when there were "reasonable grounds" to believe contraband was present. Acting on a police detective's tip that Griffin might have a gun, probation officers searched his apartment and found a handgun. Griffin, a convicted felon, was charged with firearm possession and moved to suppress.

## Issue
Whether a warrantless search of a probationer's home, conducted under a state regulation permitting such searches on "reasonable grounds," satisfies the Fourth Amendment.

## Rule
Yes. Supervising probationers is a special need beyond ordinary law enforcement that justifies departing from the warrant and probable-cause requirements. "A State's operation of a probation system, like its operation of a school, government office or prison, or its supervision of a regulated industry, likewise presents 'special needs' beyond normal law enforcement that may justify departures from the usual warrant and probable-cause requirements." — 483 U.S. at 873–874. ^pin-873

Applying that principle: "We think it clear that the special needs of Wisconsin's probation system make the warrant requirement impracticable and justify replacement of the standard of probable cause by 'reasonable grounds,' as defined by the Wisconsin Supreme Court." — *Id.* at 876. ^pin-876

## Application
Griffin's status as a probationer placed him within a closely supervised system whose special needs made obtaining a warrant impracticable. Because the search was conducted under a valid regulation, with supervisory approval and on the "reasonable grounds" supplied by the detective's tip about a gun, it satisfied the Fourth Amendment even without a warrant or full probable cause.

## Conclusion
The warrantless probation search was reasonable; the conviction and the denial of suppression were affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Griffin*'s special-needs rationale for supervising probationers was carried forward in later probation/parole-search cases such as [[United States v. Knights]] and [[Samson v. California]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Griffin v. Wisconsin*, 483 U.S. 868 (1987) — https://www.courtlistener.com/opinion/111959/griffin-v-wisconsin/ — pinpoints: 873, 876.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e4151cb2cea4946b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Griffin v. Wisconsin"}, "payload": {"all": [{"cite": "483 U.S. 868", "page": "868", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "483"}, {"cite": "107 S. Ct. 3164", "page": "3164", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "97 L. Ed. 2d 709", "page": "709", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "1987 U.S. LEXIS 2897", "page": "2897", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "55 U.S.L.W. 5156", "page": "5156", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "483 U.S. 868", "official": {"cite": "483 U.S. 868", "page": "868", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "483"}, "official_selection_present": true, "record_id": "Griffin v. Wisconsin"}}
{"assertion_id": "1f1cbea61a8ffa43", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-873", "record_id": "Griffin v. Wisconsin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-873", "pinpoint_status": "slip-only", "quote": "satisfies the Fourth Amendment. ## Rule Yes. Supervising probationers is a special need beyond ordinary law enforcement that justifies departing from the warrant and probable-cause requirements.", "quote_fidelity": "mismatch", "record_id": "Griffin v. Wisconsin", "star_marker": null}}
{"assertion_id": "b5b5b9fcd9e565dd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-876", "record_id": "Griffin v. Wisconsin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-876", "pinpoint_status": "slip-only", "quote": "We think it clear that the special needs of Wisconsin's probation system make the warrant requirement impracticable and justify replacement of the standard of probable cause by 'reasonable grounds,' as defined by the Wisconsin Supreme Court.", "quote_fidelity": "mismatch", "record_id": "Griffin v. Wisconsin", "star_marker": null}}
{"assertion_id": "3f380cb734f6ebbf", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Griffin v. Wisconsin"}, "payload": {"as_of_content": "1987-06-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Griffin v. Wisconsin", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Griffin v. Wisconsin

```json
{
  "schema_version": "s2.v1",
  "record_id": "Griffin v. Wisconsin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Griffin v. Wisconsin",
    "case_name_short": "Griffin",
    "case_name_full": "Griffin v. Wisconsin",
    "input_case_name": "Griffin v. Wisconsin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-06-26",
    "year": 1987,
    "docket": null,
    "cluster_id": 111959,
    "lead_opinion_id": 9431137,
    "sibling_ids": [
      111959,
      9431137,
      9431138,
      9431139
    ],
    "absolute_url": "/opinion/111959/griffin-v-wisconsin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9065918,
        "score": 20,
        "case_name": "Griffin v. Wisconsin"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "483 U.S. 868",
      "volume": "483",
      "reporter": "U.S.",
      "page": "868",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 3164",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "3164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 L. Ed. 2d 709",
        "volume": "97",
        "reporter": "L. Ed. 2d",
        "page": "709",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 5156",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "5156",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 2897",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2897",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "483 U.S. 868",
        "volume": "483",
        "reporter": "U.S.",
        "page": "868",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 3164",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "3164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 L. Ed. 2d 709",
        "volume": "97",
        "reporter": "L. Ed. 2d",
        "page": "709",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 2897",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2897",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 5156",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "5156",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "483 U.S. 868",
    "official_selection": {
      "court_class": "scotus",
      "selected": "483 U.S. 868",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-873",
      "page": null,
      "quote": "satisfies the Fourth Amendment. ## Rule Yes. Supervising probationers is a special need beyond ordinary law enforcement that justifies departing from the warrant and probable-cause requirements.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-876",
      "page": null,
      "quote": "We think it clear that the special needs of Wisconsin's probation system make the warrant requirement impracticable and justify replacement of the standard of probable cause by 'reasonable grounds,' as defined by the Wisconsin Supreme Court.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Griffin v. Wisconsin",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 10018723,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 5144554,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane1_negative"
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
        "journal_ref": "Griffin v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stenhoff",
          "cluster_id": 4609284,
          "cite": [
            "2019 ND 106",
            "925 N.W.2d 429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chandler",
          "cluster_id": 7318545,
          "cite": [
            "164 F. Supp. 3d 368",
            "2016 U.S. Dist. LEXIS 17682",
            "2016 WL 614679"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Moore",
          "cluster_id": 3168462,
          "cite": [
            "473 Mass. 481",
            "43 N.E.3d 294"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Hill",
          "cluster_id": 2769569,
          "cite": [
            "776 F.3d 243"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gall v. United States",
          "cluster_id": 145843,
          "cite": [
            "169 L. Ed. 2d 445",
            "128 S. Ct. 586",
            "552 U.S. 38",
            "2007 U.S. LEXIS 13083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skinner v. Railway Labor Executives' Assn.",
          "cluster_id": 112219,
          "cite": [
            "103 L. Ed. 2d 639",
            "109 S. Ct. 1402",
            "489 U.S. 602",
            "1989 U.S. LEXIS 1568",
            "4 I.E.R. Cas. (BNA) 224",
            "1989 CCH OSHD 28,476",
            "57 U.S.L.W. 4324",
            "13 OSHC (BNA) 2065",
            "130 L.R.R.M. (BNA) 2857",
            "49 Empl. Prac. Dec. (CCH) 38,791"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Buie",
          "cluster_id": 112384,
          "cite": [
            "108 L. Ed. 2d 276",
            "110 S. Ct. 1093",
            "494 U.S. 325",
            "1990 U.S. LEXIS 1176"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Caballes",
          "cluster_id": 137742,
          "cite": [
            "160 L. Ed. 2d 842",
            "125 S. Ct. 834",
            "543 U.S. 405",
            "2005 U.S. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Doe",
          "cluster_id": 127899,
          "cite": [
            "155 L. Ed. 2d 164",
            "123 S. Ct. 1140",
            "538 U.S. 84",
            "2003 U.S. LEXIS 1949"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knights",
          "cluster_id": 118468,
          "cite": [
            "151 L. Ed. 2d 497",
            "122 S. Ct. 587",
            "534 U.S. 112",
            "2001 U.S. LEXIS 10950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vernonia School District 47J v. Acton",
          "cluster_id": 117964,
          "cite": [
            "132 L. Ed. 2d 564",
            "115 S. Ct. 2386",
            "515 U.S. 646",
            "1995 U.S. LEXIS 4275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas Omar Midgette",
          "cluster_id": 796984,
          "cite": [
            "478 F.3d 616",
            "2007 U.S. App. LEXIS 4153",
            "2007 WL 572127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dubbs Ex Rel. Dubbs v. Head Start, Inc.",
          "cluster_id": 163684,
          "cite": [
            "336 F.3d 1194",
            "2003 U.S. App. LEXIS 14578",
            "2003 WL 21690533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Shreck",
          "cluster_id": 2509432,
          "cite": [
            "107 P.3d 1048",
            "2004 WL 2137067"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Bd. of Probation and Parole v. Scott",
          "cluster_id": 118235,
          "cite": [
            "141 L. Ed. 2d 344",
            "118 S. Ct. 2014",
            "524 U.S. 357",
            "1998 U.S. LEXIS 4037"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 118414,
          "cite": [
            "149 L. Ed. 2d 205",
            "121 S. Ct. 1281",
            "532 U.S. 67",
            "2001 U.S. LEXIS 2460",
            "2001 Daily Journal DAR 2839",
            "2001 Colo. J. C.A.R. 1427",
            "14 Fla. L. Weekly Fed. S 152",
            "69 U.S.L.W. 4184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McCullough",
          "cluster_id": 2594742,
          "cite": [
            "6 P.3d 774",
            "2000 Colo. J. C.A.R. 3950",
            "2000 Colo. LEXIS 817",
            "2000 WL 870824"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
          "cluster_id": 121171,
          "cite": [
            "153 L. Ed. 2d 735",
            "122 S. Ct. 2559",
            "536 U.S. 822",
            "2002 U.S. LEXIS 4882",
            "2002 Cal. Daily Op. Serv. 5761",
            "2002 Daily Journal DAR 7275",
            "70 U.S.L.W. 4737",
            "15 Fla. L. Weekly Fed. S 483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bliss v. Franco",
          "cluster_id": 167399,
          "cite": [
            "446 F.3d 1036",
            "64 Fed. R. Serv. 3d 781",
            "2006 U.S. App. LEXIS 10342",
            "2006 WL 1075595"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Olguin",
          "cluster_id": 2512145,
          "cite": [
            "45 Cal. 4th 375",
            "198 P.3d 1",
            "87 Cal. Rptr. 3d 199",
            "2008 Cal. LEXIS 14603"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Haymond",
          "cluster_id": 4632951,
          "cite": [
            "588 U.S. 634",
            "139 S. Ct. 2369",
            "204 L. Ed. 2d 897",
            "2019 U.S. LEXIS 4398"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Williams",
          "cluster_id": 1518571,
          "cite": [
            "832 A.2d 962",
            "574 Pa. 487",
            "2003 Pa. LEXIS 1746"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Firth",
          "cluster_id": 2588015,
          "cite": [
            "205 P.3d 445",
            "2008 Colo. App. LEXIS 1398",
            "2008 WL 4140588"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sewn Newton",
          "cluster_id": 786350,
          "cite": [
            "369 F.3d 659",
            "2004 U.S. App. LEXIS 10343",
            "2004 WL 1161747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gates v. Texas Deparment of Protective & Regulatory Services",
          "cluster_id": 62905,
          "cite": [
            "537 F.3d 404",
            "2008 WL 2875378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Du v. Commonwealth",
          "cluster_id": 4258780,
          "cite": [
            "790 S.E.2d 493",
            "292 Va. 555",
            "2016 Va. LEXIS 130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Griffin v. Wisconsin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111959 OR 9431137 OR 9431138 OR 9431139) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDEwOTk4NDAwMDAwJnM9MjczNzE4NyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111959+OR+9431137+OR+9431138+OR+9431139%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111959 OR 9431137 OR 9431138 OR 9431139)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTcmcz0xMjU4OTY1JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111959+OR+9431137+OR+9431138+OR+9431139%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111959 OR 9431137 OR 9431138 OR 9431139)",
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
    "complete_query": "cites:(111959 OR 9431137 OR 9431138 OR 9431139)",
    "indexed_citing_opinions": 1045,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111959,
        "count": 915,
        "count_source": "search"
      },
      {
        "opinion_id": 9431137,
        "count": 158,
        "count_source": "search"
      },
      {
        "opinion_id": 9431138,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431139,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2150,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/griffin-v-wisconsin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNTU1MjYmcz01ODA4Mzg0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111959+OR+9431137+OR+9431138+OR+9431139%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111959,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 108606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 111904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 111913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 1254526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 1756304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111959,
        "cited_id": 2131359,
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
    "date_created": "2026-07-05T05:55:14Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:55:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:55:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:58:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:55:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Griffin v. Wisconsin

```
<opinion type="majority">
<author id="b920-4"><page-number citation-index="1" label="870">*870</page-number>Justice Scalia</author>
<p id="AKj">delivered the opinion of the Court.</p>
<p id="b920-5">Petitioner Joseph Griffin, who was on probation, had his home searched by probation officers acting without a warrant. The officers found a gun that later served as the basis of Griffin’s conviction of a state-law weapons offense. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./479/1005/">479 U. S. 1005</a></span> (1986), to consider whether this search violated the Fourth Amendment.</p>
<p id="b920-6">I</p>
<p id="b920-7">On September 4, 1980, Griffin, who had previously been convicted of a felony, was convicted in Wisconsin state court of resisting arrest, disorderly conduct, and obstructing an officer. He was placed on probation.</p>
<p id="b920-8">Wisconsin law puts probationers in the legal custody of the State Department of Health and Social Services and renders them “subject . . . to . . . conditions set by the court and rules and regulations established by the department.” <span class="citation no-link">Wis. Stat. § 973.10</span>(1) (1985-1986). One of the Department’s regulations permits any probation officer to search a proba<page-number citation-index="1" label="871">*871</page-number>tioner’s home without a warrant as long as his supervisor approves and as long as there are “reasonable grounds” to believe the presence of contraband — including any item that the probationer cannot possess under the probation conditions. <span class="citation no-link">Wis. Admin. Code HSS §§ 328.21</span>(4), 328.16(1) (1981).<footnotemark>1</footnotemark> The rule provides that an officer should consider a variety of factors in determining whether “reasonable grounds” exist, among which are information provided by an informant, the reliability and specificity of that information, the reliability of the informant (including whether the informant has any incentive to supply inaccurate information), the officer’s own experience with the probationer, and the “need to verify compliance with rules of supervision and state and federal law.” HSS §328.21(7). Another regulation makes it a violation of the terms of probation to refuse to consent to a home search. HSS § 328.04(3)(k). And still another forbids a probationer to possess a firearm without advance approval from a probation officer. HSS § 328.04(3)(j).</p>
<p id="b921-5">On April 5, 1983, while Griffin was still on probation, Michael Lew, the supervisor of Griffin’s probation officer, received information from a detective on the Beloit Police Department that there were or might be guns in Griffin’s apartment. Unable to secure the assistance of Griffin’s own probation officer, Lew, accompanied by another probation officer and three plainclothes policemen, went to the apartment. When Griffin answered the door, Lew told him who they were and informed him that they were going to search his home. During the subsequent search — carried out entirely by the probation officers under the authority of Wisconsin’s probation regulation — they found a handgun.</p>
<p id="b922-4"><page-number citation-index="1" label="872">*872</page-number>Griffin was charged with possession of a firearm by a convicted felon, which is itself a felony. <span class="citation no-link">Wis. Stat. §941.29</span>(2) (1985-1986). He moved to suppress the evidence seized during the search. The trial court denied the motion, concluding that no warrant was necessary and that the search was reasonable. A jury convicted Griffin of the firearms violation, and he was sentenced to two years’ imprisonment. The conviction was affirmed by the Wisconsin Court of Appeals, <span class="citation" data-id="9678218"><a href="/opinion/1756304/state-v-griffin/" aria-description="Citation for case: State v. Griffin">126 Wis. 2d 183</a></span>, <span class="citation" data-id="9678218"><a href="/opinion/1756304/state-v-griffin/" aria-description="Citation for case: State v. Griffin">376 N. W. 2d 62</a></span> (1985).</p>
<p id="b922-5">On further appeal, the Wisconsin Supreme Court also affirmed. It found denial of the suppression motion proper because probation diminishes a probationer’s reasonable expectation of privacy — so that a probation officer may, consistent with the Fourth Amendment, search a probationer’s home without a warrant, and with only “reasonable grounds” (not probable cause) to believe that contraband is present. It held that the “reasonable grounds” standard of Wisconsin’s search regulation satisfied this “reasonable grounds” standard of the Federal Constitution, and that the detective’s tip established “reasonable grounds” within the meaning of the regulation, since it came from someone who had no reason to supply inaccurate information, specifically identified Griffin, and suggested a need to verify Griffin’s compliance with state law. <span class="citation" data-id="9585432"><a href="/opinion/1254526/state-v-griffin/#52" aria-description="Citation for case: State v. Griffin">131 Wis. 2d 41, 52-64</a></span>, <span class="citation" data-id="9585432"><a href="/opinion/1254526/state-v-griffin/#539" aria-description="Citation for case: State v. Griffin">388 N. W. 2d 535, 539-544</a></span> (1986).</p>
<p id="b922-6">II</p>
<p id="b922-7">We think the Wisconsin Supreme Court correctly concluded that this warrantless search did not violate the Fourth Amendment. To reach that result, however, we find it unnecessary to embrace a new principle of law, as the Wisconsin court evidently did, that any search of a probationer’s home by a probation officer satisfies the Fourth Amendment as long as the information possessed by the officer satisfies a federal “reasonable grounds” standard. As his sentence for the commission of a crime, Griffin was committed to the legal custody of the Wisconsin State Department of Health and <page-number citation-index="1" label="873">*873</page-number>Social Services, and thereby made subject to that Department’s rules and regulations. The search of Griffin’s home satisfied the demands of the Fourth Amendment because it was carried out pursuant to a regulation that itself satisfies the Fourth Amendment’s reasonableness requirement under well-established principles.</p>
<p id="b923-5">A</p>
<p id="b923-6">A probationer’s home, like anyone else’s, is protected by the Fourth Amendment’s requirement that searches be “reasonable.” Although we usually require that a search be undertaken only pursuant to a warrant (and thus supported by probable cause, as the Constitution says warrants must be), see, <em>e. g., Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980), we have permitted exceptions when “special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable.” <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 351</a></span> (1985) (Blackmun, J., concurring in judgment). Thus, we have held that government employers and supervisors may conduct warrantless, work-related searches of employees’ desks and offices without probable cause, <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987), and that school officials may conduct warrantless searches of some student property, also without probable cause, <em>New Jersey </em>v. <em>T. L. O., swpra. </em>We have also held, for similar reasons, that in certain circumstances government investigators conducting searches pursuant to a regulatory scheme need not adhere to the usual warrant or probable-cause requirements as long as their searches meet “reasonable legislative or administrative standards.” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 538</a></span> (1967). See <em>New York </em>v. <em>Burger, </em><span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#702" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 702-703</a></span> (1987); <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#602" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 602</a></span> (1981); <em>United States </em>v. <em>Biswell, </em>406 XJ. S. 311, 316 (1972).</p>
<p id="b923-7">A State’s operation of a probation system, like its operation of a school, government office or prison, or its supervision of a regulated industry, likewise presents “special <page-number citation-index="1" label="874">*874</page-number>needs” beyond normal law enforcement that may justify departures from the usual warrant and probable-cause requirements. Probation, like incarceration, is “a form of criminal sanction imposed by a court upon an offender after verdict, finding, or plea of guilty.” G. Killinger, H. Kerper, &amp; P. Cromwell, Probation and Parole in the Criminal Justice System 14 (1976); see also <span class="citation no-link">18 U. S. C. § 3651</span> (1982 ed. and Supp. III) (probation imposed instead of imprisonment); <span class="citation no-link">Wis. Stat. § 973.09</span> (1985-1986) (same).<footnotemark>2</footnotemark> Probation is simply one point (or, more accurately, one set of points) on a continuum of possible punishments ranging from solitary confinement in a maximum-security facility to a few hours of mandatory community service. A number of different options lie between those extremes, including confinement in a medium- or minimum-security facility, work-release programs, “halfway houses,” and probation — which can itself be more or less confining depending upon the number and severity of restrictions imposed. See, <em>e. g., </em><span class="citation no-link">18 U. S. C. §3563</span> (1982 ed., Supp. III) (effective Nov. 1, 1987) (probation conditions authorized in federal system include requiring probationers to avoid commission of other crimes; to pursue employment; to avoid certain occupations, places, and people; to spend evenings or weekends in prison; and to avoid narcotics or excessive use of alcohol). To a greater or lesser degree, it is always true of probationers (as we have said it to be true of parolees) that they do not enjoy “the absolute liberty to which every citizen is entitled, but only . . . conditional liberty properly dependent on observance of special [probation] restrictions.” <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#480" aria-description="Citation for case: Morrissey v. Brewer">408 U. S. 471, 480</a></span> (1972).</p>
<p id="b925-4"><page-number citation-index="1" label="875">*875</page-number>These restrictions are meant to assure that the probation serves as a period of genuine rehabilitation and that the community is not harmed by the probationer’s being at large. See <em>State </em>v. <em>Tarrell, </em><span class="citation" data-id="9723296"><a href="/opinion/2131359/state-v-tarrell/#652" aria-description="Citation for case: State v. Tarrell">74 Wis. 2d 647, 652-653</a></span>, <span class="citation" data-id="9723296"><a href="/opinion/2131359/state-v-tarrell/#700" aria-description="Citation for case: State v. Tarrell">247 N. W. 2d 696, 700</a></span> (1976). These same goals require and justify the exercise of supervision to assure that the restrictions are in fact observed. Recent research suggests that more intensive supervision can reduce recidivism, see Petersilia, Probation and Felony Offenders, <span class="citation no-link">49 Fed. Probation 9</span> (June 1985), and the importance of supervision has grown as probation has become an increasingly common sentence for those convicted of serious crimes, see <span class="citation no-link"><em>id., </em>at 4</span>. Supervision, then, is a “special need” of the State permitting a degree of impingement upon privacy that would not be constitutional if applied to the public at large. That permissible degree is not unlimited, however, so we next turn to whether it has been exceeded here.</p>
<p id="b925-5">B</p>
<p id="b925-6">In determining whether the “special needs” of its probation system justify Wisconsin’s search regulation, we must take that regulation as it has been interpreted by state corrections officials and state courts. As already noted, the Wisconsin Supreme Court — the ultimate authority on issues of Wisconsin law — has held that a tip from a police detective that Griffin “had” or “may have had” an illegal weapon at his home constituted the requisite “reasonable grounds.” See <span class="citation" data-id="9585432"><a href="/opinion/1254526/state-v-griffin/#64" aria-description="Citation for case: State v. Griffin">131 Wis. 2d, at 64</a></span>, <span class="citation" data-id="9585432"><a href="/opinion/1254526/state-v-griffin/#544" aria-description="Citation for case: State v. Griffin">388 N. W. 2d, at 544</a></span>. Whether or not we would choose to interpret a similarly worded federal regulation in that fashion, we are bound by the state court’s interpretation, which is relevant to our constitutional analysis only insofar as it fixes the meaning of the regulation.<footnotemark>3</footnotemark> We <page-number citation-index="1" label="876">*876</page-number>think it clear that the special needs of Wisconsin’s probation system make the warrant requirement impracticable and justify replacement of the standard of probable cause by “reasonable grounds,” as defined by the Wisconsin Supreme Court.</p>
<p id="b926-5">A warrant requirement would interfere to an appreciable degree with the probation system, setting up a magistrate rather than the probation officer as the judge of how close a supervision the probationer requires. Moreover, the delay inherent in obtaining a warrant would make it more difficult for probation officials to respond quickly to evidence of misconduct, see <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#340" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 340</a></span>, and would reduce the deterrent effect that the possibility of expeditious searches would otherwise create, see <em>New York </em>v. <em>Burger, </em><span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#710" aria-description="Citation for case: New York v. Burger">482 U. S., at 710</a></span>; <em>United States </em>v. <em>Biswell, </em>406 U. S., at 316. By way of analogy, one might contemplate how parental custodial authority would be impaired by requiring judicial approval for search of a minor child’s room. And on the other side of the equation — the effect of dispensing with a warrant upon the probationer: Although a probation officer is not an impartial magistrate, neither is he the police officer who normally conducts searches against the ordinary citizen. He is an employee of the State Department of Health and Social Services who, while assuredly charged with protecting the public interest, is also supposed to have in mind the welfare of the probationer (who in the regulations is called a “client,” HSS § 328.03(5)). The applicable regulations require him, for example, to “[p]rovid[e] individualized counseling designed to foster growth and development of the client as necessary,” HSS § 328.04(2)(i), and “[m]onito[r] the <page-number citation-index="1" label="877">*877</page-number>client’s progress where services are provided by another agency and evaluate] the need for continuation of the services,” HSS §328.04(2)(o). In such a setting, we think it reasonable to dispense with the warrant requirement.</p>
<p id="b927-5">Justice Blackmun’s dissent would retain a judicial warrant requirement, though agreeing with our subsequent conclusion that reasonableness of the search does not require probable cause. This, however, is a combination that neither the text of the Constitution nor any of our prior decisions permits. While it is possible to say that Fourth Amendment reasonableness demands probable cause without a judicial warrant, the reverse runs up against the constitutional provision that “no Warrants shall issue, but upon probable cause.” Arndt. 4. The Constitution prescribes, in other words, that where the matter is of such a nature as to require a judicial warrant, it is also of such a nature as to require probable cause. Although we have arguably come to permit an exception to that prescription for administrative search warrants,<footnotemark>4</footnotemark> which may but do not necessarily have to be issued by courts,<footnotemark>8</footnotemark> we have never done so for constitutionally mandated judicial <page-number citation-index="1" label="878">*878</page-number>warrants. There it remains true that “[i]f a search warrant be constitutionally required, the requirement cannot be flexibly interpreted to dispense with the rigorous constitutional restrictions for its issue.” <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#373" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 373</a></span> (1959). Justice Blackmun neither gives a justification for departure from that principle nor considers its implications for the body of Fourth Amendment law.</p>
<p id="b928-5">We think that the probation regime would also be unduly disrupted by a requirement of probable cause. To take the facts of the present case, it is most unlikely that the unauthenticated tip of a police officer — bearing, as far as the record shows, no indication whether its basis was firsthand knowledge or, if not, whether the firsthand source was reliable, and merely stating that Griffin “had or might have” guns in his residence, not that he certainly had them — would meet the ordinary requirement of probable cause. But this is different from the ordinary case in two related respects: First, even more than the requirement of a warrant, a probable-cause requirement would reduce the deterrent effect of the supervisory arrangement. The probationer would be assured that so long as his illegal (and perhaps socially dangerous) activities were sufficiently concealed as to give rise to no more than reasonable suspicion, they would go undetected and uncorrected. The second difference is well reflected in the regulation specifying what is to be considered “[i]n deciding whether there are reasonable grounds to believe ... a client’s living quarters or property contain contraband,” HSS §328.21(7). The factors include not only the usual elements that a police officer or magistrate would consider, such as the detail and consistency of the information suggesting the presence of contraband and the reliability and motivation to dissemble of the informant, HSS §§328.21(7) (c), (d), but also “[ijnformation provided by the client which is relevant to whether the client possesses contraband,” and “[t]he experience of a staff member with that client or in a <page-number citation-index="1" label="879">*879</page-number>similar circumstance.” HSS §§ 328.21(7)(f), (g). As was true, then, in <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987), and <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325</a></span> (1985), we deal with a situation in which there is an ongoing supervisory relationship —and one that is not, or at least not entirely, adversarial— between the object of the search and the decisionmaker.<footnotemark>6</footnotemark></p>
<p id="b929-5">In such circumstances it is both unrealistic and destructive of the whole object of the continuing probation relationship to insist upon the same degree of demonstrable reliability of particular items of supporting data, and upon the same degree of certainty of violation, as is required in other contexts. In some cases — especially those involving drugs or illegal weapons — the probation agency must be able to act based upon a lesser degree of certainty than the Fourth Amendment would otherwise require in order to intervene before a probationer does damage to himself or society. The agency, moreover, must be able to proceed on the basis of its entire experience with the probationer, and to assess probabilities in the light of its knowledge of his life, character, and circumstances.</p>
<p id="b929-6">To allow adequate play for such factors, we think it reasonable to permit information provided by a police officer,<footnotemark>7</footnotemark> <page-number citation-index="1" label="880">*880</page-number>whether or not on the basis of firsthand knowledge, to support a probationer search. The same conclusion is suggested by the fact that the police máy be unwilling to disclose their confidential sources to probation personnel. For the same reason, and also because it is the very assumption of the institution of probation that the probationer is in need of rehabilitation and is more likely than the ordinary citizen to violate the law, we think it enough if the information provided indicates, as it did here, only the likelihood (“had or might have guns”) of facts justifying the search.<footnotemark>8</footnotemark></p>
<p id="b930-5">The search of Griffin’s residence was “reasonable” within the meaning of the Fourth Amendment because it was conducted pursuant to a valid regulation governing probationers. This conclusion makes it unnecessary to consider whether, as the court below held and the State urges, <em>any </em>search of a probationer’s home by a probation officer is lawful when there are “reasonable grounds” to believe contraband is present. For the foregoing reasons, the judgment of the Wisconsin Supreme Court is</p>
<p id="b930-6">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b921-6"> HSS § 328 was promulgated in December 1981 and became effective on January 1, 1982. Effective May 1, 1986, HSS § 328.21 was repealed and repromulgated with somewhat different numbering and without relevant substantive changes. See <span class="citation" data-id="9585432"><a href="/opinion/1254526/state-v-griffin/#60" aria-description="Citation for case: State v. Griffin">131 Wis. 2d 41, 60, n. 7</a></span>, <span class="citation" data-id="9585432"><a href="/opinion/1254526/state-v-griffin/#542" aria-description="Citation for case: State v. Griffin">388 N. W. 2d 535, 542, n. 7</a></span> (1986). This opinion will cite the old version of § 328.21, which was in effect at the time of the search.</p>
</footnote>
<footnote label="2">
<p id="b924-5"> We have recently held that prison regulations allegedly infringing constitutional rights are themselves constitutional as long as they are “ ‘reasonably related to legitimate penological interests.’” <em>O’Lone </em>v. <em>Estate of Shabazz, </em><span class="citation" data-id="9431021"><a href="/opinion/111913/olone-v-estate-of-shabazz/#349" aria-description="Citation for case: O&#x27;Lone v. Estate of Shabazz">482 U. S. 342, 349</a></span> (1987) (quoting <em>Turner </em>v. <em>Safley, </em><span class="citation" data-id="9431005"><a href="/opinion/111904/turner-v-safley/#89" aria-description="Citation for case: Turner v. Safley">482 U. S. 78, 89</a></span> (1987)). We have no occasion in this case to decide whether, as a general matter, that test applies to probation regulations as well.</p>
</footnote>
<footnote label="3">
<p id="b925-7"> If the regulation in question established a standard of conduct to which the probationer had to conform on pain of <em>penalty </em>— e. <em>g., </em>a restriction on his movements — the state court could not constitutionally adopt so unnatural an interpretation of the language that the regulation would fail to provide adequate notice. Cf. <em>Kolender </em>v. <em>Lawson, </em><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/#357" aria-description="Citation for case: Kolender v. Lawson">461 U. S. 352, 357-358</a></span> (1983); <em>Lambert </em>v. <em>California, </em><span class="citation" data-id="9421523"><a href="/opinion/105596/lambert-v-california/#228" aria-description="Citation for case: Lambert v. California">355 U. S. 225, 228</a></span> (1957). That is not an <page-number citation-index="1" label="876">*876</page-number>issue here since, even though the petitioner would be in violation of his probation conditions (and subject to the penalties that entails) if he failed to consent to any search that the regulation authorized, see HSS §328.04(3)(k), nothing in the regulation or elsewhere required him to be advised, at the time of the request for search, what the probation officer’s “reasonable grounds” were, any more than the ordinary citizen has to be notified of the grounds for “probable cause” or “exigent circumstances” searches before they may be undertaken.</p>
</footnote>
<footnote label="4">
<p id="b927-6"><em> </em>In the administrative search context, we formally require that administrative warrants be supported by “probable cause,” because in that context we use that term as referring not to a quantum of evidence, but merely to a requirement of reasonableness. See, <em>e. g., Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#320" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 320</a></span> (1978); <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967). In other contexts, however, we use “probable cause” to refer to a quantum of evidence for the belief justifying the search, to be distinguished from a lesser quantum such as “reasonable suspicion.” See <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#724" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709, 724</a></span> (1987) (plurality); <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 341-342</a></span> (1985). It is plainly in this sense that the dissent uses the term. See, <em>e. g., post, </em>at 881-883 (less than probable cause means “a reduced level of suspicion”).</p>
<p id="b927-7">5 See <em>Marshall </em>v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#307" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Barlow’s, Inc., supra, </em>at 307</a></span> (“We hold that. . . the Act is unconstitutional insofar as it purports to authorize inspections without warrant or its equivalent”). The “neutral magistrate,” <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Camara, supra, </em>at 532</a></span>, or “neutral officer,” <em>Marshall </em>v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Barlow’s, Inc., supra, </em>at 323</a></span>, envisioned by our administrative search cases is not necessarily the “neutral judge,” <em>post, </em>at 887, envisioned by the dissent.</p>
</footnote>
<footnote label="6">
<p id="b929-7"> It is irrelevant whether the probation authorities relied upon any peculiar knowledge which they possessed of petitioner in deciding to conduct the present search. Our discussion pertains to the reasons generally supporting the proposition that the search decision should be left to the expertise of probation authorities rather than a magistrate, and should be supportable by a lesser quantum of concrete evidence justifying suspicion than would be required to establish probable cause. That those reasons may not obtain in a particular case is of no consequence. We may note, nonetheless, that the dissenters are in error to assert as a fact that the probation authorities made no use of special knowledge in the present case, <em>post, </em>at 890. All we know for certain is that the petitioner’s probation officer could not be reached; whether any material contained in petitioner’s probation file was used does not appear.</p>
</footnote>
<footnote label="7">
<p id="b929-8"> The dissenters speculate that the information might not have come from the police at all, “but from someone impersonating an officer.” <em>Post, </em><page-number citation-index="1" label="880">*880</page-number>at 888. The trial court, however, found as a matter of fact that Lew received the tip on which he relied from a police officer. See <span class="citation" data-id="9585432"><a href="/opinion/1254526/state-v-griffin/#62" aria-description="Citation for case: State v. Griffin">131 Wis. 2d, at 62</a></span>, <span class="citation" data-id="9585432"><a href="/opinion/1254526/state-v-griffin/#543" aria-description="Citation for case: State v. Griffin">388 N. W. 2d, at 543</a></span>. The Wisconsin Supreme Court affirmed that finding, <em>ibid., </em>and neither the petitioner nor the dissenters assert that it is clearly erroneous.</p>
</footnote>
<footnote label="8">
<p id="b930-12"> The dissenters assert that the search did not comport with all the governing Wisconsin regulations. There are reasonable grounds on which the Wisconsin court could find that it did. But we need not belabor those here, since the only regulation upon which we rely for our constitutional decision is that which permits a warrantless search on “reasonable grounds.” The Wisconsin Supreme Court found the requirement of “reasonable grounds” to have been met on the facts of this case and, as discussed earlier, we hold that such a requirement, so interpreted, meets constitutional minimum standards as well. That the procedures followed, although establishing “reasonable grounds” under Wisconsin law, and adequate under federal constitutional standards, may have violated Wisconsin state regulations, is irrelevant to the ease before us.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Groh v. Ramirez.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Groh v. Ramirez"
type: case
citation: "540 U.S. 551 (2004)"
parallel_cite: "124 S. Ct. 1284; 157 L. Ed. 2d 1068"
neutral_cite: "2004 U.S. LEXIS 1624; 2004 WL 330057"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-02-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Groh v. Ramirez
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/131161/groh-v-ramirez/"
  cluster_id: 131161
  opinion_id: 131161
  identity_checked: true
homes:
  - page: "[[Particularity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Maryland v. Garrison]]", "[[United States v. Leon]]", "[[Massachusetts v. Sheppard]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "particularity", "qualified-immunity", "facial-invalidity"]
holding: "A warrant that utterly **fails to describe the persons or things to be seized** is facially invalid under the Particularity Clause —…"
lake:
  record_id: Groh v. Ramirez
  status: verified
  projected_at: 2026-07-06
---

# Groh v. Ramirez

*540 U.S. 551 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An ATF agent, Groh, prepared and obtained a warrant to search the Ramirezes' Montana ranch for specified firearms and explosives. But in the part of the warrant form describing the persons or things to be seized, Groh typed a description of the house itself ("a single dwelling residence . . . blue in color"), not the weapons. The supporting application listed the items, but the warrant did not, no document was incorporated by reference, and no copy describing the items was left with the family. Officers searched, found nothing, and the Ramirezes sued; Groh claimed [[Qualified Immunity|qualified immunity]].

## Issue
Whether a warrant that wholly fails to describe the persons or things to be seized is valid because the supporting application described them — and whether the officer who prepared and led the search under such a warrant is entitled to [[Qualified Immunity|qualified immunity]].

## Rule
No. [[Particularity]] is a requirement of the warrant itself, not of the supporting papers, so a warrant that omits the things to be seized is facially invalid. "The fact that the application adequately described the 'things to be seized' does not save the warrant from its facial invalidity. The Fourth Amendment by its terms requires particularity in the warrant, not in the supporting documents." — 540 U.S. at 557. ^pin-557

Because the warrant "did not describe the items to be seized at all," it "was so obviously deficient that we must regard the search as 'warrantless'." — *Id.* at 558. ^pin-558

## Application
Groh's warrant described only the house, not the firearms and explosives that were its object, and nothing cured the defect — no incorporation by reference, no affidavit accompanying the warrant, no copy of the items left with the family. Because the warrant failed the [[Particularity|particularity]] requirement on its face, and so plainly that any reasonable officer who prepared it would have recognized the defect, the search was effectively warrantless and Groh — who drafted and led it — was not entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
The facially deficient warrant rendered the search unconstitutional, and the officer who prepared and executed it was denied [[Qualified Immunity|qualified immunity]]; the judgment in his favor was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Groh* is a leading [[Particularity|particularity]]-clause decision and a marker for when a warrant is so facially deficient that good-faith reliance on it is unreasonable.

## Appears on
- [[Particularity]] — *Key — Progeny / Refinement*

## Sources
- *Groh v. Ramirez*, 540 U.S. 551 (2004) — https://www.courtlistener.com/opinion/131161/groh-v-ramirez/ — pinpoints: 557, 558.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b26aeb0afa43ed72", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Groh v. Ramirez"}, "payload": {"all": [{"cite": "540 U.S. 551", "page": "551", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "540"}, {"cite": "124 S. Ct. 1284", "page": "1284", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "157 L. Ed. 2d 1068", "page": "1068", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "157"}, {"cite": "2004 U.S. LEXIS 1624", "page": "1624", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}, {"cite": "2004 WL 330057", "page": "330057", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2004"}], "display": "540 U.S. 551", "official": {"cite": "540 U.S. 551", "page": "551", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "540"}, "official_selection_present": true, "record_id": "Groh v. Ramirez"}}
{"assertion_id": "38ee66f7f3f998f9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-557", "record_id": "Groh v. Ramirez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-557", "pinpoint_status": "slip-only", "quote": "), not the weapons. The supporting application listed the items, but the warrant did not, no document was incorporated by reference, and no copy describing the items was left with the family. Officers searched, found nothing, and the Ramirezes sued; Groh claimed qualified immunity. ## Issue Whether a warrant that wholly fails to describe the persons or things to be seized is valid because the supporting application described them — and whether the officer who prepared and led the search under such a warrant is entitled to qualified immunity. ## Rule No. Particularity is a requirement of the warrant itself, not of the supporting papers, so a warrant that omits the things to be seized is facially invalid.", "quote_fidelity": "mismatch", "record_id": "Groh v. Ramirez", "star_marker": null}}
{"assertion_id": "65765c5f88ae0f8c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-558", "record_id": "Groh v. Ramirez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-558", "pinpoint_status": "slip-only", "quote": "did not describe the items to be seized at all,", "quote_fidelity": "mismatch", "record_id": "Groh v. Ramirez", "star_marker": null}}
{"assertion_id": "d5b3499a280500dc", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Groh v. Ramirez"}, "payload": {"as_of_content": "2004-02-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Groh v. Ramirez", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Groh v. Ramirez

```json
{
  "schema_version": "s2.v1",
  "record_id": "Groh v. Ramirez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Groh v. Ramirez",
    "case_name_short": "Groh",
    "case_name_full": "GROH v. RAMIREZ Et Al.",
    "input_case_name": "Groh v. Ramirez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-02-24",
    "year": 2004,
    "docket": null,
    "cluster_id": 131161,
    "lead_opinion_id": 131161,
    "sibling_ids": [
      131161,
      9434540,
      9434541,
      9434542
    ],
    "absolute_url": "/opinion/131161/groh-v-ramirez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "540 U.S. 551",
      "volume": "540",
      "reporter": "U.S.",
      "page": "551",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 1284",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1284",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1068",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1068",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 1624",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "1624",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 WL 330057",
        "volume": "2004",
        "reporter": "WL",
        "page": "330057",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "540 U.S. 551",
        "volume": "540",
        "reporter": "U.S.",
        "page": "551",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1284",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1284",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1068",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1068",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 1624",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "1624",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 WL 330057",
        "volume": "2004",
        "reporter": "WL",
        "page": "330057",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "540 U.S. 551",
    "official_selection": {
      "court_class": "scotus",
      "selected": "540 U.S. 551",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-557",
      "page": null,
      "quote": "), not the weapons. The supporting application listed the items, but the warrant did not, no document was incorporated by reference, and no copy describing the items was left with the family. Officers searched, found nothing, and the Ramirezes sued; Groh claimed qualified immunity. ## Issue Whether a warrant that wholly fails to describe the persons or things to be seized is valid because the supporting application described them \u2014 and whether the officer who prepared and led the search under such a warrant is entitled to qualified immunity. ## Rule No. Particularity is a requirement of the warrant itself, not of the supporting papers, so a warrant that omits the things to be seized is facially invalid.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-558",
      "page": null,
      "quote": "did not describe the items to be seized at all,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Groh v. Ramirez",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532255,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532252,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended July 5, 2017 State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4471947,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4384931,
          "cite": [
            "893 N.W.2d 904",
            "2017 WL 1422692",
            "2017 Iowa Sup. LEXIS 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tosh Toussaint",
          "cluster_id": 4259133,
          "cite": [
            "838 F.3d 503",
            "2016 U.S. App. LEXIS 17357",
            "2016 WL 5314862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wheeler v. State",
          "cluster_id": 3182294,
          "cite": [
            "135 A.3d 282",
            "2016 Del. LEXIS 121",
            "2016 WL 825395"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chandler",
          "cluster_id": 7318545,
          "cite": [
            "164 F. Supp. 3d 368",
            "2016 U.S. Dist. LEXIS 17682",
            "2016 WL 614679"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yee",
          "cluster_id": 3062319,
          "cite": [
            "177 So. 3d 72",
            "2015 Fla. App. LEXIS 15198",
            "2015 WL 5965213"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Wright",
          "cluster_id": 2777610,
          "cite": [
            "777 F.3d 635",
            "2015 WL 507169",
            "2015 U.S. App. LEXIS 1939"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Christopher Covey v. Assessor of Ohio County",
          "cluster_id": 2773276,
          "cite": [
            "777 F.3d 186",
            "2015 WL 309598",
            "2015 U.S. App. LEXIS 1113"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pearson v. Callahan",
          "cluster_id": 145918,
          "cite": [
            "172 L. Ed. 2d 565",
            "129 S. Ct. 808",
            "555 U.S. 223",
            "2009 U.S. LEXIS 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
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
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sosa v. Alvarez-Machain",
          "cluster_id": 137006,
          "cite": [
            "159 L. Ed. 2d 718",
            "124 S. Ct. 2739",
            "542 U.S. 692",
            "2004 U.S. LEXIS 4763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Messerschmidt v. Millender",
          "cluster_id": 623242,
          "cite": [
            "182 L. Ed. 2d 47",
            "132 S. Ct. 1235",
            "565 U.S. 535",
            "2012 U.S. LEXIS 1687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mattos v. Agarano",
          "cluster_id": 615433,
          "cite": [
            "661 F.3d 433",
            "2011 WL 4908374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Grubbs",
          "cluster_id": 145670,
          "cite": [
            "164 L. Ed. 2d 195",
            "126 S. Ct. 1494",
            "547 U.S. 90",
            "2006 U.S. LEXIS 2496"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walczyk v. Rio",
          "cluster_id": 2704,
          "cite": [
            "496 F.3d 139",
            "2007 WL 2199005"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate of Tori Carter Brenda Chambers v. City of Detroit, Donald Hollins, Lieutenant",
          "cluster_id": 790266,
          "cite": [
            "408 F.3d 305",
            "2005 U.S. App. LEXIS 9717",
            "2005 WL 1280174"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Fisher",
          "cluster_id": 1755,
          "cite": [
            "175 L. Ed. 2d 410",
            "130 S. Ct. 546",
            "558 U.S. 45",
            "2009 U.S. LEXIS 8773"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arar v. Ashcroft",
          "cluster_id": 2451,
          "cite": [
            "585 F.3d 559",
            "2009 U.S. App. LEXIS 23988",
            "2009 WL 3522887"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elizabeth Harvey v. Plains Township Police Department Edward J. Walsh Ronald Dombroski Plains Township Board Joan A. Chukinas",
          "cluster_id": 791673,
          "cite": [
            "421 F.3d 185",
            "2005 U.S. App. LEXIS 18756",
            "2005 WL 2077254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nathaniel Brent v. Wayne Cty. Dep't of Human Servs.",
          "cluster_id": 4529474,
          "cite": [
            "901 F.3d 656"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fernandez v. California",
          "cluster_id": 2654534,
          "cite": [
            "188 L. Ed. 2d 25",
            "134 S. Ct. 1126",
            "2014 U.S. LEXIS 1636",
            "82 U.S.L.W. 4102",
            "571 U.S. 292",
            "24 Fla. L. Weekly Fed. S 553",
            "2014 WL 700100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chavez",
          "cluster_id": 2380403,
          "cite": [
            "240 P.3d 448",
            "2010 Colo. App. LEXIS 213",
            "2010 WL 547625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cox v. Maine State Police",
          "cluster_id": 201366,
          "cite": [
            "391 F.3d 25",
            "2004 WL 2731499"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Riccardi",
          "cluster_id": 165743,
          "cite": [
            "405 F.3d 852",
            "2005 U.S. App. LEXIS 6631",
            "2005 WL 896430"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
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
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeffrey Meek",
          "cluster_id": 786002,
          "cite": [
            "366 F.3d 705",
            "2004 U.S. App. LEXIS 7470",
            "2004 WL 829899"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cooper",
          "cluster_id": 223162,
          "cite": [
            "654 F.3d 1104",
            "108 A.F.T.R.2d (RIA) 5815",
            "2011 U.S. App. LEXIS 16825",
            "2011 WL 3559929"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Motley v. Parks",
          "cluster_id": 3035469,
          "cite": [
            "432 F.3d 1072",
            "2005 WL 3556971"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weigel v. Broad",
          "cluster_id": 171335,
          "cite": [
            "544 F.3d 1143",
            "2008 U.S. App. LEXIS 21877",
            "2008 WL 4631920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 1023785,
          "cite": [
            "501 F.3d 374",
            "2007 U.S. App. LEXIS 22436",
            "2007 WL 2729126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moss v. Kopp",
          "cluster_id": 171900,
          "cite": [
            "559 F.3d 1155",
            "2009 U.S. App. LEXIS 5752",
            "2009 WL 692832"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Gerald Gamboa",
          "cluster_id": 793501,
          "cite": [
            "439 F.3d 796",
            "69 Fed. R. Serv. 675",
            "2006 U.S. App. LEXIS 5393",
            "2006 WL 508321"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Groh v. Ramirez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(131161 OR 9434540 OR 9434541 OR 9434542) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDEzMzMxMjAwMDAwJnM9Mjc0MzYxMSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28131161+OR+9434540+OR+9434541+OR+9434542%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(131161 OR 9434540 OR 9434541 OR 9434542)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDcmcz04MTIzNTYmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28131161+OR+9434540+OR+9434541+OR+9434542%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(131161 OR 9434540 OR 9434541 OR 9434542)",
        "reviewed": 50,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 50,
        "triage_read": 0,
        "triage_snippet_classified": 50
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(131161 OR 9434540 OR 9434541 OR 9434542)",
    "indexed_citing_opinions": 679,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 131161,
        "count": 557,
        "count_source": "search"
      },
      {
        "opinion_id": 9434540,
        "count": 132,
        "count_source": "search"
      },
      {
        "opinion_id": 9434541,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434542,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1305,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/groh-v-ramirez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyMDk0NDEmcz0xMDMzMTE3NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28131161+OR+9434540+OR+9434541+OR+9434542%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 131161,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 109932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 111719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 112762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 288501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 336439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 350518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 373913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 402242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 405042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 546301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 552757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 567212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 627497,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 744863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 764737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131161,
        "cited_id": 778595,
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
    "date_created": "2026-07-05T05:58:54Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:59:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:59:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:03:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:59:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Groh v. Ramirez

```
<div>
<center><b><span class="citation" data-id="9434540"><a href="/opinion/131161/groh-v-ramirez/" aria-description="Citation for case: Groh v. Ramirez">540 U.S. 551</a></span> (2004)</b></center>
<center><h1>GROH<br>
v.<br>
RAMIREZ ET AL.</h1></center>
<center>No. 02-811.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 4, 2003.</center>
<center>Decided February 24, 2004.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*552</span> STEVENS, J., delivered the opinion of the Court, in which O'CONNOR, SOUTER, GINSBURG, and BREYER, JJ., joined. KENNEDY, J., filed a dissenting <span class="star-pagination">*553</span> opinion, in which REHNQUIST, C. J., joined, <i>post,</i> p. 566. THOMAS, J., filed a dissenting opinion, in which SCALIA, J., joined, and in which REHNQUIST, C. J., joined as to Part III, <i>post,</i> p. 571.</p>
<p><i>Richard A. Cordray</i> argued the cause for petitioner. With him on the briefs was <i>Harry Litman.</i></p>
<p><i>Austin C. Schlick</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Olson, Assistant Attorney General McCallum, Deputy Solicitor General Clement, Barbara L. Herwig,</i> and <i>Howard S. Scher.</i></p>
<p><i>Vincent J. Kozakiewicz</i> argued the cause for respondents. With him on the brief was <i>W. G. Gilbert III.</i><sup>[*]</sup></p>
<p>JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>Petitioner conducted a search of respondents' home pursuant to a warrant that failed to describe the "persons or things to be seized." U. S. Const., Amdt. 4. The questions presented are (1) whether the search violated the Fourth Amendment, and (2) if so, whether petitioner nevertheless is entitled to qualified immunity, given that a Magistrate Judge (Magistrate), relying on an affidavit that particularly described the items in question, found probable cause to conduct the search.</p>
<p></p>
<h2>
<span class="star-pagination">*554</span> I</h2>
<p>Respondents, Joseph Ramirez and members of his family, live on a large ranch in Butte-Silver Bow County, Montana. Petitioner, Jeff Groh, has been a Special Agent for the Bureau of Alcohol, Tobacco and Firearms (ATF) since 1989. In February 1997, a concerned citizen informed petitioner that on a number of visits to respondents' ranch the visitor had seen a large stock of weaponry, including an automatic rifle, grenades, a grenade launcher, and a rocket launcher.<sup>[1]</sup> Based on that information, petitioner prepared and signed an application for a warrant to search the ranch. The application stated that the search was for "any automatic firearms or parts to automatic weapons, destructive devices to include but not limited to grenades, grenade launchers, rocket launchers, and any and all receipts pertaining to the purchase or manufacture of automatic weapons or explosive devices or launchers." App. to Pet. for Cert. 28a. Petitioner supported the application with a detailed affidavit, which he also prepared and executed, that set forth the basis for his belief that the listed items were concealed on the ranch. Petitioner then presented these documents to a Magistrate, along with a warrant form that petitioner also had completed. The Magistrate signed the warrant form.</p>
<p>Although the application particularly described the place to be searched and the contraband petitioner expected to find, the warrant itself was less specific; it failed to identify any of the items that petitioner intended to seize. In the portion of the form that called for a description of the "person or property" to be seized, petitioner typed a description of respondents' two-story blue house rather than the alleged stockpile of firearms.<sup>[2]</sup> The warrant did not incorporate by <span class="star-pagination">*555</span> reference the itemized list contained in the application. It did, however, recite that the Magistrate was satisfied the affidavit established probable cause to believe that contraband was concealed on the premises, and that sufficient grounds existed for the warrant's issuance.<sup>[3]</sup></p>
<p>The day after the Magistrate issued the warrant, petitioner led a team of law enforcement officers, including both federal agents and members of the local sheriff's department, in the search of respondents' premises. Although respondent Joseph Ramirez was not home, his wife and children were. Petitioner states that he orally described the objects of the search to Mrs. Ramirez in person and to Mr. Ramirez by telephone. According to Mrs. Ramirez, however, petitioner explained only that he was searching for "`an explosive device in a box.'" <i>Ramirez</i> v. <i>Butte-Silver Bow County,</i> <span class="citation" data-id="778595"><a href="/opinion/778595/ramirez-v-butte-silver-bow-county/#1026" aria-description="Citation for case: Ramirez v. Butte-Silver Bow County">298 F. 3d 1022, 1026</a></span> (CA9 2002). At any rate, the officers' search uncovered no illegal weapons or explosives. When the officers left, petitioner gave Mrs. Ramirez a copy of the search warrant, but not a copy of the application, which had been sealed. The following day, in response to a request from respondents' attorney, petitioner faxed the attorney a copy of the page of the application that listed the items to be seized. No charges were filed against the Ramirezes.</p>
<p>Respondents sued petitioner and the other officers under <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971), and Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, raising eight claims, including violation of the Fourth Amendment. App. 17-27. The District Court entered summary judgment for all defendants. The court found no Fourth Amendment violation, because it considered the case comparable to one in which the warrant contained an inaccurate address, and in such a case, the court reasoned, the warrant is sufficiently <span class="star-pagination">*556</span> detailed if the executing officers can locate the correct house. App. to Pet. for Cert. 20a-22a. The court added that even if a constitutional violation occurred, the defendants were entitled to qualified immunity because the failure of the warrant to describe the objects of the search amounted to a mere "typographical error." <i><span class="citation no-link">Id.,</span></i> at 22a-24a.</p>
<p>The Court of Appeals affirmed the judgment with respect to all defendants and all claims, with the exception of respondents' Fourth Amendment claim against petitioner. <span class="citation" data-id="778595"><a href="/opinion/778595/ramirez-v-butte-silver-bow-county/#1029" aria-description="Citation for case: Ramirez v. Butte-Silver Bow County">298 F. 3d, at 1029-1030</a></span>. On that claim, the court held that the warrant was invalid because it did not "describe with particularity the place to be searched and the items to be seized," and that oral statements by petitioner during or after the search could not cure the omission. <span class="citation" data-id="778595"><a href="/opinion/778595/ramirez-v-butte-silver-bow-county/#1025" aria-description="Citation for case: Ramirez v. Butte-Silver Bow County"><i>Id.,</i> at 1025-1026</a></span>. The court observed that the warrant's facial defect "increased the likelihood and degree of confrontation between the Ramirezes and the police" and deprived respondents of the means "to challenge officers who might have exceeded the limits imposed by the magistrate." <span class="citation" data-id="778595"><a href="/opinion/778595/ramirez-v-butte-silver-bow-county/#1027" aria-description="Citation for case: Ramirez v. Butte-Silver Bow County"><i>Id.,</i> at 1027</a></span>. The court also expressed concern that "permitting officers to expand the scope of the warrant by oral statements would broaden the area of dispute between the parties in subsequent litigation." <i><span class="citation" data-id="778595"><a href="/opinion/778595/ramirez-v-butte-silver-bow-county/" aria-description="Citation for case: Ramirez v. Butte-Silver Bow County">Ibid.</a></span></i> The court nevertheless concluded that all of the officers except petitioner were protected by qualified immunity. With respect to petitioner, the court read our opinion in <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> (1984), as precluding qualified immunity for the leader of a search who fails to "read the warrant and satisfy [himself] that [he] understand[s] its scope and limitations, and that it is not defective in some obvious way." <span class="citation" data-id="778595"><a href="/opinion/778595/ramirez-v-butte-silver-bow-county/#1027" aria-description="Citation for case: Ramirez v. Butte-Silver Bow County">298 F. 3d, at 1027</a></span>. The court added that "[t]he leaders of the search team must also make sure that a copy of the warrant is available to give to the person whose property is being searched at the commencement of the search, and that such copy has no missing pages or other obvious defects." <i><span class="citation" data-id="778595"><a href="/opinion/778595/ramirez-v-butte-silver-bow-county/" aria-description="Citation for case: Ramirez v. Butte-Silver Bow County">Ibid.</a></span></i> (footnote omitted). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./537/1231/">537 U. S. 1231</a></span> (2003).</p>
<p></p>
<h2>
<span class="star-pagination">*557</span> II</h2>
<p>The warrant was plainly invalid. The Fourth Amendment states unambiguously that "no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and <i>particularly describing</i> the place to be searched, and <i>the persons or things to be seized.</i>" (Emphasis added.) The warrant in this case complied with the first three of these requirements: It was based on probable cause and supported by a sworn affidavit, and it described particularly the place of the search. On the fourth requirement, however, the warrant failed altogether. Indeed, petitioner concedes that "the warrant . . . was deficient in particularity because it provided no description of the type of evidence sought." Brief for Petitioner 10.</p>
<p>The fact that the <i>application</i> adequately described the "things to be seized" does not save the <i>warrant</i> from its facial invalidity. The Fourth Amendment by its terms requires particularity in the warrant, not in the supporting documents. See <i>Massachusetts</i> v. <i>Sheppard,</i> <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#988" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S. 981, 988, n. 5</a></span> (1984) ("[A] warrant that fails to conform to the particularity requirement of the Fourth Amendment is unconstitutional"); see also <i>United States</i> v. <i>Stefonek,</i> <span class="citation" data-id="764737"><a href="/opinion/764737/united-states-v-barbara-e-stefonek-cross-appellee/#1033" aria-description="Citation for case: United States v. Barbara E. Stefonek, Cross-Appellee">179 F. 3d 1030, 1033</a></span> (CA7 1999) ("The Fourth Amendment requires that the <i>warrant</i> particularly describe the things to be seized, not the papers presented to the judicial officer . . . asked to issue the warrant" (emphasis in original)). And for good reason: "The presence of a search warrant serves a high function," <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455</a></span> (1948), and that high function is not necessarily vindicated when some other document, somewhere, says something about the objects of the search, but the contents of that document are neither known to the person whose home is being searched nor available for her inspection. We do not say that the Fourth Amendment forbids a warrant from cross-referencing other documents. Indeed, most Courts of Appeals have held that a court may construe a warrant with reference to a supporting application or affidavit if the warrant <span class="star-pagination">*558</span> uses appropriate words of incorporation, and if the supporting document accompanies the warrant. See, <i>e.g., </i><i>United States</i> v. <i>McGrew,</i> <span class="citation" data-id="744863"><a href="/opinion/744863/united-states-of-america-plaintiff-appellee-v-chong-hyon-mcgrew-aka/#849" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellee, v. Chong...">122 F. 3d 847, 849-850</a></span> (CA9 1997); <i>United States</i> v. <i>Williamson,</i> <span class="citation" data-id="627497"><a href="/opinion/627497/united-states-v-john-s-williamson/#1136" aria-description="Citation for case: United States v. John S. Williamson">1 F. 3d 1134, 1136, n. 1</a></span> (CA10 1993); <i>United States</i> v. <i>Blakeney,</i> <span class="citation" data-id="567212"><a href="/opinion/567212/united-states-v-roy-c-blakeney-90-5664-kenneth-a-kutnyak-90-5665/#1025" aria-description="Citation for case: United States v. Roy C. Blakeney (90-5664), Kenneth A....">942 F. 2d 1001, 1025-1026</a></span> (CA6 1991); <i>United States</i> v. <i>Maxwell,</i> <span class="citation" data-id="552757"><a href="/opinion/552757/united-states-v-carrye-e-maxwell/#1031" aria-description="Citation for case: United States v. Carrye E. Maxwell">920 F. 2d 1028, 1031</a></span> (CADC 1990); <i>United States</i> v. <i>Curry,</i> <span class="citation" data-id="546301"><a href="/opinion/546301/united-states-v-tanell-rashaad-curry-tn-tanell-r-curry/#76" aria-description="Citation for case: United States v. Tanell Rashaad Curry, T/n Tanell R. Curry">911 F. 2d 72, 76-77</a></span> (CA8 1990); <i>United States</i> v. <i>Roche,</i> <span class="citation" data-id="373913"><a href="/opinion/373913/united-states-v-john-c-roche/#8" aria-description="Citation for case: United States v. John C. Roche">614 F. 2d 6, 8</a></span> (CA1 1980). But in this case the warrant did not incorporate other documents by reference, nor did either the affidavit or the application (which had been placed under seal) accompany the warrant. Hence, we need not further explore the matter of incorporation.</p>
<p>Petitioner argues that even though the warrant was invalid, the search nevertheless was "reasonable" within the meaning of the Fourth Amendment. He notes that a Magistrate authorized the search on the basis of adequate evidence of probable cause, that petitioner orally described to respondents the items to be seized, and that the search did not exceed the limits intended by the Magistrate and described by petitioner. Thus, petitioner maintains, his search of respondents' ranch was functionally equivalent to a search authorized by a valid warrant.</p>
<p>We disagree. This warrant did not simply omit a few items from a list of many to be seized, or misdescribe a few of several items. Nor did it make what fairly could be characterized as a mere technical mistake or typographical error. Rather, in the space set aside for a description of the items to be seized, the warrant stated that the items consisted of a "single dwelling residence . . . blue in color." In other words, the warrant did not describe the items to be seized <i>at all.</i> In this respect the warrant was so obviously deficient that we must regard the search as "warrantless" within the meaning of our case law. See <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U. S., at 923</a></span>; cf. <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#85" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 85</a></span> (1987); <i>Steele</i> v. <i>United States,</i> <span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/#503" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498, 503-504</a></span> (1925). "We are not <span class="star-pagination">*559</span> dealing with formalities." <i>McDonald,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U.S., at 455</a></span>. Because "`the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion'" stands "'[a]t the very core' of the Fourth Amendment," <i>Kyllo</i> v. <i>United States,</i> <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#31" aria-description="Citation for case: Kyllo v. United States">533 U. S. 27, 31</a></span> (2001) (quoting <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span> (1961)), our cases have firmly established the "`basic principle of Fourth Amendment law' that searches and seizures inside a home without a warrant are presumptively unreasonable," <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980) (footnote omitted). Thus, "absent exigent circumstances, a warrantless entry to search for weapons or contraband is unconstitutional even when a felony has been committed and there is probable cause to believe that incriminating evidence will be found within." <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York"><i>Id.,</i> at 587-588</a></span> (footnote omitted). See <i>Kyllo,</i> <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#29" aria-description="Citation for case: Kyllo v. United States">533 U. S., at 29</a></span>; <i>Illinois</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/#181" aria-description="Citation for case: Illinois v. Rodriguez">497 U. S. 177, 181</a></span> (1990); <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#761" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 761-763</a></span> (1969); <i>McDonald,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#454" aria-description="Citation for case: McDonald v. United States">335 U. S., at 454</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948).</p>
<p>We have clearly stated that the presumptive rule against warrantless searches applies with equal force to searches whose only defect is a lack of particularity in the warrant. In <i><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span>,</i> for instance, the petitioner argued that even though the warrant was invalid for lack of particularity, "the search was constitutional because it was reasonable within the meaning of the Fourth Amendment." 468 U. S., at 988, n. 5. In squarely rejecting that position, we explained:</p>
<blockquote>"The uniformly applied rule is that a search conducted pursuant to a warrant that fails to conform to the particularity requirement of the Fourth Amendment is unconstitutional. <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476</a></span> (1965); <i>United States</i> v. <i>Cardwell,</i> <span class="citation" data-id="405042"><a href="/opinion/405042/united-states-v-james-b-cardwell-united-states-of-america-v-marvin/#77" aria-description="Citation for case: United States v. James B. Cardwell, United States of...">680 F. 2d 75, 77-78</a></span> (CA9 1982); <i>United States</i> v. <i>Crozier,</i> <span class="citation" data-id="402242"><a href="/opinion/402242/united-states-v-clarence-jay-crozier-manuel-isadore-pine-alan-terry/#1299" aria-description="Citation for case: United States v. Clarence Jay Crozier, Manuel Isadore...">674 F. 2d 1293, 1299</a></span> (CA9 1982); <i>United States</i> v. <i>Klein,</i> <span class="citation" data-id="9464268"><a href="/opinion/350518/united-states-v-allan-michael-klein/#185" aria-description="Citation for case: United States v. Allan Michael Klein">565 F. 2d 183, 185</a></span> (CA1 1977); <i>United States</i> v. <i>Gardner,</i> <span class="citation" data-id="336439"><a href="/opinion/336439/united-states-v-norman-eugene-gardner/#862" aria-description="Citation for case: United States v. Norman Eugene Gardner">537 F. 2d 861, 862</a></span> (CA6 1976); <i>United States</i> v. <i>Marti,</i> <span class="citation" data-id="288501"><a href="/opinion/288501/united-states-v-luis-marti-and-lou-saks/" aria-description="Citation for case: United States v. Luis Marti and Lou Saks">421 F. 2d 1263</a></span>, 1268-1269 <span class="star-pagination">*560</span> (CA2 1970). That rule is in keeping with the well-established principle that `except in certain carefully defined classes of cases, a search of private property without proper consent is "unreasonable" unless it has been authorized by a valid search warrant.' <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span> (1967). See <i>Steagald</i> v. <i>United States,</i> <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#211" aria-description="Citation for case: Steagald v. United States">451 U. S. 204, 211-212</a></span> (1981); <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958)." <i><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Ibid.</a></span></i>
</blockquote>
<p>Petitioner asks us to hold that a search conducted pursuant to a warrant lacking particularity should be exempt from the presumption of unreasonableness if the goals served by the particularity requirement are otherwise satisfied. He maintains that the search in this case satisfied those goals  which he says are "to prevent general searches, to prevent the seizure of one thing under a warrant describing another, and to prevent warrants from being issued on vague or dubious information," Brief for Petitioner 16  because the scope of the search did not exceed the limits set forth in the application. But unless the particular items described in the affidavit are also set forth in the warrant itself (or at least incorporated by reference, and the affidavit present at the search), there can be no written assurance that the Magistrate actually found probable cause to search for, and to seize, every item mentioned in the affidavit. See <i>McDonald,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S., at 455</a></span> ("Absent some grave emergency, the Fourth Amendment has interposed a magistrate between the citizen and the police. This was done . . . so that an objective mind might weigh the need to invade [the citizen's] privacy in order to enforce the law"). In this case, for example, it is at least theoretically possible that the Magistrate was satisfied that the search for weapons and explosives was justified by the showing in the affidavit, but not convinced that any evidentiary basis existed for rummaging through respondents' files and papers for receipts pertaining to the purchase or manufacture of such items. Cf. <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U.S. 476, 485-486</a></span> (1965). Or, conceivably, the Magistrate might <span class="star-pagination">*561</span> have believed that some of the weapons mentioned in the affidavit could have been lawfully possessed and therefore should not be seized. See <span class="citation no-link">26 U. S. C. § 5861</span> (requiring registration, but not banning possession of, certain firearms). The mere fact that the Magistrate issued a warrant does not necessarily establish that he agreed that the scope of the search should be as broad as the affiant's request. Even though petitioner acted with restraint in conducting the search, "the inescapable fact is that this restraint was imposed by the agents themselves, not by a judicial officer." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 356</a></span> (1967).<sup>[4]</sup></p>
<p>We have long held, moreover, that the purpose of the particularity requirement is not limited to the prevention of general searches. See <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#84" aria-description="Citation for case: Maryland v. Garrison">480 U. S., at 84</a></span>. A particular warrant also "assures the individual whose property is searched or seized of the lawful authority of the executing officer, his need to search, and the limits of his power to search." <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977) (citing <i>Camara</i> v. <i>Municipal Court of City and County of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 532</a></span> (1967)), abrogated on other grounds, <i>California</i> v. <i>Acevedo,</i> <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">500 U. S. 565</a></span> (1991). See also <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#236" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 236</a></span> (1983) ("[P]ossession <span class="star-pagination">*562</span> of a warrant by officers conducting an arrest or search greatly reduces the perception of unlawful or intrusive police conduct").<sup>[5]</sup></p>
<p>Petitioner argues that even if the goals of the particularity requirement are broader than he acknowledges, those goals nevertheless were served because he orally described to respondents the items for which he was searching. Thus, he submits, respondents had all of the notice that a proper warrant would have accorded. But this case presents no occasion even to reach this argument, since respondents, as noted above, dispute petitioner's account. According to Mrs. Ramirez, petitioner stated only that he was looking for an "`explosive device in a box.'" <span class="citation" data-id="778595"><a href="/opinion/778595/ramirez-v-butte-silver-bow-county/#1026" aria-description="Citation for case: Ramirez v. Butte-Silver Bow County">298 F. 3d, at 1026</a></span>. Because this dispute is before us on petitioner's motion for summary judgment, App. to Pet. for Cert. 13a, "[t]he evidence of the nonmovant is to be believed, and all justifiable inferences are to be drawn in [her] favor," <i>Anderson</i> v. <i>Liberty Lobby, Inc.,</i> <span class="citation" data-id="9430599"><a href="/opinion/111719/anderson-v-liberty-lobby-inc/#255" aria-description="Citation for case: Anderson v. Liberty Lobby, Inc.">477 U. S. 242, 255</a></span> (1986) (citation omitted). The posture of the case therefore obliges us to credit Mrs. Ramirez's account, and we find that petitioner's description of "`an explosive <span class="star-pagination">*563</span> device in a box'" was little better than no guidance at all. See <i>Stefonek,</i> <span class="citation" data-id="764737"><a href="/opinion/764737/united-states-v-barbara-e-stefonek-cross-appellee/#1032" aria-description="Citation for case: United States v. Barbara E. Stefonek, Cross-Appellee">179 F. 3d, at 1032-1033</a></span> (holding that a search warrant for "`evidence of crime'" was "[s]o open-ended" in its description that it could "only be described as a general warrant").</p>
<p>It is incumbent on the officer executing a search warrant to ensure the search is lawfully authorized and lawfully conducted.<sup>[6]</sup> Because petitioner did not have in his possession a warrant particularly describing the things he intended to seize, proceeding with the search was clearly "unreasonable" under the Fourth Amendment. The Court of Appeals correctly held that the search was unconstitutional.</p>
<p></p>
<h2>III</h2>
<p>Having concluded that a constitutional violation occurred, we turn to the question whether petitioner is entitled to qualified immunity despite that violation. See <i>Wilson</i> v. <i>Layne,</i> <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#609" aria-description="Citation for case: Wilson v. Layne">526 U. S. 603, 609</a></span> (1999). The answer depends on whether the right that was transgressed was "`clearly established'"  that is, "whether it would be clear to a reasonable officer that his conduct was unlawful in the situation he confronted." <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 202 (2001).</p>
<p>Given that the particularity requirement is set forth in the text of the Constitution, no reasonable officer could believe that a warrant that plainly did not comply with that requirement was valid. See <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818-819</a></span> (1982) ("If the law was clearly established, the immunity <span class="star-pagination">*564</span> defense ordinarily should fail, since a reasonably competent public official should know the law governing his conduct"). Moreover, because petitioner himself prepared the invalid warrant, he may not argue that he reasonably relied on the Magistrate's assurance that the warrant contained an adequate description of the things to be seized and was therefore valid. Cf. <i>Sheppard,</i> <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#989" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S., at 989-990</a></span>. In fact, the guidelines of petitioner's own department placed him on notice that he might be liable for executing a manifestly invalid warrant. An ATF directive in force at the time of this search warned: "Special agents are liable if they exceed their authority while executing a search warrant and must be sure that a search warrant is sufficient on its face even when issued by a magistrate." Searches and Examinations, ATF Order O 3220.1(7)(d) (Feb. 13, 1997). See also <i>id.,</i> at 3220.1(23)(b) ("If any error or deficiency is discovered and there is a reasonable probability that it will invalidate the warrant, such warrant shall not be executed. The search shall be postponed until a satisfactory warrant has been obtained").<sup>[7]</sup> And even a cursory reading of the warrant in this caseperhaps just a simple glance  would have revealed a glaring deficiency that any reasonable police officer would have known was constitutionally fatal.</p>
<p>No reasonable officer could claim to be unaware of the basic rule, well established by our cases, that, absent consent or exigency, a warrantless search of the home is presumptively unconstitutional. See <i>Payton,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S., at 586-588</a></span>. Indeed, as we noted nearly 20 years ago in <i><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span>:</i> "The uniformly applied rule is that a search conducted pursuant to a warrant that fails to conform to the particularity requirement of the Fourth Amendment is unconstitutional." <span class="star-pagination">*565</span> 468 U. S., at 988, n. 5.<sup>[8]</sup> Because not a word in any of our cases would suggest to a reasonable officer that this case fits within any exception to that fundamental tenet, petitioner is asking us, in effect, to craft a new exception. Absent any support for such an exception in our cases, he cannot reasonably have relied on an expectation that we would do so.</p>
<p>Petitioner contends that the search in this case was the product, at worst, of a lack of due care, and that our case law requires more than negligent behavior before depriving an official of qualified immunity. See <i>Malley</i> v. <i>Briggs,</i> <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 341</a></span> (1986). But as we observed in the companion case to <i><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span>,</i> "a warrant may be so facially deficient  <i>i. e.,</i> in failing to particularize the place to be searched or the things to be seized  that the executing officers cannot reasonably presume it to be valid." <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U. S., at 923</a></span>. This is such a case.<sup>[9]</sup></p>
<p><span class="star-pagination">*566</span> Accordingly, the judgment of the Court of Appeals is affirmed.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE KENNEDY, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>I agree with the Court that the Fourth Amendment was violated in this case. The Fourth Amendment states that "no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." The warrant issued in this case did not particularly describe the things to be seized, and so did not comply with the Fourth Amendment. I disagree with the Court on whether the officer who obtained the warrant and led the search team is entitled to qualified immunity for his role in the search. In my view, the officer should receive qualified immunity.</p>
<p>An officer conducting a search is entitled to qualified immunity if "a reasonable officer could have believed" that the search was lawful "in light of clearly established law and the information the searching officers possessed." <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 641</a></span> (1987). As the Court notes, this is the same objective reasonableness standard applied under the "`good faith'" exception to the exclusionary rule. See <i>ante,</i> at 565, n. 8 (citing <i>Malley</i> v. <i>Briggs,</i> <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#344" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 344</a></span> (1986)). The central question is whether someone in the officer's position could reasonably but mistakenly conclude that his conduct complied with the Fourth Amendment. <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton"><i>Creighton, supra,</i> at 641</a></span>. See also <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 206 (2001); <i>Hunter</i> v. <i>Bryant,</i> <span class="citation" data-id="9432435"><a href="/opinion/112671/hunter-v-bryant/#227" aria-description="Citation for case: Hunter v. Bryant">502 U. S. 224, 227</a></span> (1991) <i>(per curiam)</i><i>.</i></p>
<p>An officer might reach such a mistaken conclusion for several reasons. He may be unaware of existing law and how it should be applied. See, <i>e. g., </i><i>Saucier, supra</i><i>.</i> Alternatively, <span class="star-pagination">*567</span> he may misunderstand important facts about the search and assess the legality of his conduct based on that misunderstanding. See, <i>e. g., </i><i>Arizona</i> v. <i>Evans,</i> <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans">514 U. S. 1</a></span> (1995). Finally, an officer may misunderstand elements of both the facts and the law. See, <i>e. g., </i><i><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Creighton, supra</a></span></i><i>.</i> Our qualified immunity doctrine applies regardless of whether the officer's error is a mistake of law, a mistake of fact, or a mistake based on mixed questions of law and fact. <i>Butz</i> v. <i>Economou,</i> <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou">438 U. S. 478, 507</a></span> (1978) (noting that qualified immunity covers "mere mistakes in judgment, whether the mistake is one of fact or one of law").</p>
<p>The present case involves a straightforward mistake of fact. Although the Court does not acknowledge it directly, it is obvious from the record below that the officer simply made a clerical error when he filled out the proposed warrant and offered it to the Magistrate Judge. The officer used the proper description of the property to be seized when he completed the affidavit. He also used the proper description in the accompanying application. When he typed up the description a third time for the proposed warrant, however, the officer accidentally entered a description of the place to be searched in the part of the warrant form that called for a description of the property to be seized. No one noticed the error before the search was executed. Although the record is not entirely clear on this point, the mistake apparently remained undiscovered until the day after the search when respondents' attorney reviewed the warrant for defects. The officer, being unaware of his mistake, did not rely on it in any way. It is uncontested that the officer trained the search team and executed the warrant based on his mistaken belief that the warrant contained the proper description of the items to be seized.</p>
<p>The question is whether the officer's mistaken belief that the warrant contained the proper language was a reasonable belief. In my view, it was. A law enforcement officer charged with leading a team to execute a search warrant for <span class="star-pagination">*568</span> illegal weapons must fulfill a number of serious responsibilities. The officer must establish probable cause to believe the crime has been committed and that evidence is likely to be found at the place to be searched; must articulate specific items that can be seized, and a specific place to be searched; must obtain the warrant from a magistrate judge; and must instruct a search team to execute the warrant within the time allowed by the warrant. The officer must also oversee the execution of the warrant in a way that protects officer safety, directs a thorough and professional search for the evidence, and avoids unnecessary destruction of property. These difficult and important tasks demand the officer's full attention in the heat of an ongoing and often dangerous criminal investigation.</p>
<p>An officer who complies fully with all of these duties can be excused for not being aware that he had made a clerical error in the course of filling out the proposed warrant. See <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#87" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 87</a></span> (1987) (recognizing "the need to allow some latitude for honest mistakes that are made by officers in the dangerous and difficult process of making arrests and executing search warrants"). An officer who drafts an affidavit, types up an application and proposed warrant, and then obtains a judge's approval naturally assumes that he has filled out the warrant form correctly. Even if the officer checks over the warrant, he may very well miss a mistake. We all tend toward myopia when looking for our own errors. Every lawyer and every judge can recite examples of documents that they wrote, checked, and doublechecked, but that still contained glaring errors. Law enforcement officers are no different. It would be better if the officer recognizes the error, of course. It would be better still if he does not make the mistake in the first place. In the context of an otherwise proper search, however, an officer's failure to recognize his clerical error on a warrant form can be a reasonable mistake.</p>
<p><span class="star-pagination">*569</span> The Court reaches a different result by construing the officer's error as a mistake of law rather than a mistake of fact. According to the Court, the officer should not receive qualified immunity because "no reasonable officer could believe that a warrant that plainly did not comply with [the particularity] requirement was valid." <i>Ante,</i> at 563. The majority is surely right that a reasonable officer must know that a defective warrant is invalid. This much is obvious, if not tautological. It is also irrelevant, for the essential question here is whether a reasonable officer in petitioner's position would necessarily know that the warrant had a clerical error in the first place. The issue in this case is whether an officer can reasonably fail to recognize a clerical error, not whether an officer who recognizes a clerical error can reasonably conclude that a defective warrant is legally valid.</p>
<p>The Court gives little attention to this important and difficult question. It receives only two sentences at the very end of the Court's opinion. In the first sentence, the Court quotes dictum from <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 923</a></span> (1984), to the effect that "`a warrant may be so facially deficient  <i>i.e.,</i> in failing to particularize the place to be searched or the things to be seizedthat the executing officers cannot reasonably presume it to be valid.'" <i>Ante,</i> at 565. In the second sentence, the Court informs us without explanation that "[t]his is such a case." <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Ibid.</a></span></i> This reasoning is not convincing.</p>
<p>To understand the passage from <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> that the Court relies upon, it helps to recognize that most challenges to defective search warrants arise when officers rely on the defect and conduct a search that should not have occurred. The target of the improper search then brings a civil action challenging the improper search, or, if charges have been filed, moves to suppress the fruits of the search. The inquiry in both instances is whether the officers' reliance on the defect was reasonable. See, <i>e. g., </i><i><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">Garrison, supra</a></span></i> (apartment wrongly searched because the searching officers did not realize that <span class="star-pagination">*570</span> there were two apartments on the third floor and obtained a warrant to search the entire floor); <i>Arizona</i> v. <i>Evans,</i> <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans">514 U. S. 1</a></span> (1995) (person wrongly arrested and searched because a court employee's clerical error led officer to believe a warrant existed for person's arrest); <i>McCleary</i> v. <i>Navarro,</i> <span class="citation" data-id="9432605"><a href="/opinion/112762/mccleary-v-navarro-et-ux/" aria-description="Citation for case: McCleary v. Navarro Et Ux.">504 U. S. 966</a></span> (1992) (White, J., dissenting from denial of certiorari) (house wrongly searched because informant told officers the suspect lived in the second house on the right, but the suspect lived in the third house on the right).</p>
<p>The language the Court quotes from <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> comes from a discussion of when "an officer [who] has obtained a [defective] warrant and abided by its terms" has acted reasonably. 468 U. S., at 922. The discussion notes that there are some cases in which "no reasonably well trained officer should rely on the warrant." <i>Id.,</i> at 923. The passage also includes several examples, among them the one that the Court relies on in this case: "[D]epending on the circumstances of the particular case, a warrant may be so facially deficient  <i>i.e.,</i> in failing to particularize the place to be searched or the things to be seized  that the executing officers cannot reasonably presume it to be valid." <i>Ibid.</i></p>
<p>The Court interprets this language to mean that a clerical mistake can be so obvious that an officer who fails to recognize the mistake should not receive qualified immunity. Read in context, however, the quoted language is addressed to a quite different issue. The most natural interpretation of the language is that a clerical mistake can be so obvious that the officer cannot reasonably rely on the mistake in the course of executing the warrant. In other words, a defect can be so clear that an officer cannot reasonably "abid[e] by its terms" and execute the warrant as written. <i>Id.,</i> at 922.</p>
<p>We confront no such issue here, of course. No one suggests that the officer reasonably could have relied on the defective language in the warrant. This is a case about an officer being unaware of a clerical error, not a case about an officer relying on one. The respondents do not make the <span class="star-pagination">*571</span> usual claim that they were injured by a defect that led to an improper search. Rather, they make an unusual claim that they were injured simply because the warrant form did not contain the correct description of the property to be seized, even though no property was seized. The language from <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> is not on point.</p>
<p>Our Court has stressed that "the purpose of encouraging recourse to the warrant procedure" can be served best by rejecting overly technical standards when courts review warrants. <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#237" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 237</a></span> (1983). We have also stressed that qualified immunity "provides ample protection to all but the plainly incompetent or those who knowingly violate the law." <i>Malley,</i> <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs">475 U.S., at 341</a></span>. The Court's opinion is inconsistent with these principles. Its analysis requires our Nation's police officers to concentrate more on the correctness of paper forms than substantive rights. The Court's new "duty to ensure that the warrant conforms to constitutional requirements" sounds laudable, <i>ante,</i> at 563, n. 6, but would be more at home in a regime of strict liability than within the "ample room for mistaken judgments" that our qualified immunity jurisprudence traditionally provides. <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#343" aria-description="Citation for case: Malley v. Briggs"><i>Malley, supra,</i> at 343</a></span>.</p>
<p>For these reasons, I dissent.</p>
<p>JUSTICE THOMAS, with whom JUSTICE SCALIA joins, and with whom THE CHIEF JUSTICE joins as to Part III, dissenting.</p>
<p>The Fourth Amendment provides: "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." The precise relationship between the Amendment's Warrant Clause and Unreasonableness Clause is unclear. But neither Clause explicitly requires a warrant. <span class="star-pagination">*572</span> While "it is of course textually possible to consider [a warrant requirement] implicit within the requirement of reasonableness," <i>California</i> v. <i>Acevedo,</i> <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/#582" aria-description="Citation for case: California v. Acevedo">500 U. S. 565, 582</a></span> (1991) (SCALIA, J., concurring in judgment), the text of the Fourth Amendment certainly does not mandate this result. Nor does the Amendment's history, which is clear as to the Amendment's principal target (general warrants), but not as clear with respect to when warrants were required, if ever. Indeed, because of the very different nature and scope of federal authority and ability to conduct searches and arrests at the founding, it is possible that neither the history of the Fourth Amendment nor the common law provides much guidance.</p>
<p>As a result, the Court has vacillated between imposing a categorical warrant requirement and applying a general reasonableness standard. Compare <i>Thompson</i> v. <i>Louisiana,</i> <span class="citation" data-id="111282"><a href="/opinion/111282/thompson-v-louisiana/#20" aria-description="Citation for case: Thompson v. Louisiana">469 U. S. 17, 20</a></span> (1984) <i>(per curiam)</i><i>,</i> with <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#65" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 65</a></span> (1950). The Court has most frequently held that warrantless searches are presumptively unreasonable, see, <i>e. g., </i><i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967); <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 583</a></span> (1980), but has also found a plethora of exceptions to presumptive unreasonableness, see, <i>e. g., </i><i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 762-763</a></span> (1969) (searches incident to arrest); <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#800" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 800</a></span> (1982) (automobile searches); <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 315-317</a></span> (1972) (searches of "pervasively regulated" businesses); <i>Camara</i> v. <i>Municipal Court of City and County of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-539</a></span> (1967) (administrative searches); <i>Warden, Md. Penitentiary</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298</a></span> (1967) (exigent circumstances); <i>California</i> v. <i>Carney,</i> <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#390" aria-description="Citation for case: California v. Carney">471 U. S. 386, 390-394</a></span> (1985) (mobile home searches); <i>Illinois</i> v. <i>Lafayette,</i> <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#648" aria-description="Citation for case: Illinois v. Lafayette">462 U. S. 640, 648</a></span> (1983) (inventory searches); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#272" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 272</a></span> (1973) (border searches). That is, our cases stand for <span class="star-pagination">*573</span> the illuminating proposition that warrantless searches are <i>per se</i> unreasonable, except, of course, when they are not.</p>
<p>Today the Court holds that the warrant in this case was "so obviously deficient" that the ensuing search must be regarded as a warrantless search and thus presumptively unreasonable. <i>Ante,</i> at 558-559. However, the text of the Fourth Amendment, its history, and the sheer number of exceptions to the Court's categorical warrant requirement seriously undermine the bases upon which the Court today rests its holding. Instead of adding to this confusing jurisprudence, as the Court has done, I would turn to first principles in order to determine the relationship between the Warrant Clause and the Unreasonableness Clause. But even within the Court's current framework, a search conducted pursuant to a defective warrant is constitutionally different from a "warrantless search." Consequently, despite the defective warrant, I would still ask whether this search was unreasonable and would conclude that it was not. Furthermore, even if the Court were correct that this search violated the Constitution (and in particular, respondents' Fourth Amendment rights), given the confused state of our Fourth Amendment jurisprudence and the reasonableness of petitioner's actions, I cannot agree with the Court's conclusion that petitioner is not entitled to qualified immunity. For these reasons, I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>"[A]ny Fourth Amendment case may present two separate questions: whether the search was conducted pursuant to a warrant issued in accordance with the second Clause, and, if not, whether it was nevertheless `reasonable' within the meaning of the first." <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#961" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 961</a></span> (1984) (STEVENS, J., dissenting). By categorizing the search here to be a "warrantless" one, the Court declines to perform a reasonableness inquiry and ignores the fact that this search is quite different from searches that the Court has considered to be "warrantless" in the past. Our cases <span class="star-pagination">*574</span> involving "warrantless" searches do not generally involve situations in which an officer has obtained a warrant that is later determined to be facially defective, but rather involve situations in which the officers neither sought nor obtained a warrant. See, <i>e. g., </i><i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635</a></span> (1987) (officer entitled to qualified immunity despite conducting a warrantless search of respondents' home in the mistaken belief that a robbery suspect was hiding there); <i>Payton</i> v. <i>New <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">York, supra</a></span></i> (striking down a New York statute authorizing the warrantless entry into a private residence to make a routine felony arrest). By simply treating this case as if no warrant had even been sought or issued, the Court glosses over what should be the key inquiry: whether it is always appropriate to treat a search made pursuant to a warrant that fails to describe particularly the things to be seized as presumptively unreasonable.</p>
<p>The Court bases its holding that a defect in the particularity of the warrant by itself renders a search "warrantless" on a citation of a single footnote in <i>Massachusetts</i> v. <i>Sheppard,</i> <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S. 981</a></span> (1984). In <i><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span>,</i> the Court, after noting that "the sole issue . . . in th[e] case is whether the officers reasonably believed that the search they conducted was authorized by a valid warrant," <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#988" aria-description="Citation for case: Massachusetts v. Sheppard"><i>id.,</i> at 988</a></span>, rejected the petitioner's argument that despite the invalid warrant, the otherwise reasonable search was constitutional, <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#988" aria-description="Citation for case: Massachusetts v. Sheppard"><i>id.,</i> at 988, n. 5</a></span>. The Court recognized that under its case law a reasonableness inquiry would be appropriate if one of the exceptions to the warrant requirement applied. But the Court declined to consider whether such an exception applied and whether the search actually violated the Fourth Amendment because that question presented merely a "fact-bound issue of little importance." <i><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Ibid.</a></span></i> Because the Court in <i><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span></i> did not conduct any sort of inquiry into whether a Fourth Amendment violation actually occurred, it is clear that the Court assumed a violation for the purposes of its analysis. Rather than rely on dicta buried in a footnote in <span class="star-pagination">*575</span> <i><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span>,</i> the Court should actually analyze the arguably dispositive issue in this case.</p>
<p>The Court also rejects the argument that the details of the warrant application and affidavit save the warrant, because "`[t]he presence of a search warrant serves a high function.'" <i>Ante,</i> at 557 (quoting <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455</a></span> (1948)). But it is not only the physical existence of the warrant and its typewritten contents that serve this high function. The Warrant Clause's principal protection lies in the fact that the "Fourth Amendment has interposed a magistrate between the citizen and the police . . . so that an objective mind might weigh the need to invade [the searchee's] privacy in order to enforce the law." <i>Ante,</i> at 560. The Court has further explained:</p>
<blockquote>"The point of the Fourth Amendment . . . is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers. . . . When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948) (footnotes omitted).</blockquote>
<p>But the actual contents of the warrant are simply manifestations of this protection. Hence, in contrast to the case of a truly warrantless search, where a warrant (due to a mistake) does not specify on its face the particular items to be seized <span class="star-pagination">*576</span> but the warrant application passed on by the magistrate judge contains such details, a searchee still has the benefit of a determination by a neutral magistrate that there is probable cause to search a particular place and to seize particular items. In such a circumstance, the principal justification for applying a rule of presumptive unreasonableness falls away.</p>
<p>In the instant case, the items to be seized were clearly specified in the warrant application and set forth in the affidavit, both of which were given to the Judge (Magistrate). The Magistrate reviewed all of the documents and signed the warrant application and made no adjustment or correction to this application. It is clear that respondents here received the protection of the Warrant Clause, as described in <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span></i> and <i><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">McDonald</a></span>.</i> Under these circumstances, I would not hold that any ensuing search constitutes a presumptively unreasonable warrantless search. Instead, I would determine whether, despite the invalid warrant, the resulting search was reasonable and hence constitutional.</p>
<p></p>
<h2>II</h2>
<p>Because the search was not unreasonable, I would conclude that it was constitutional. Prior to execution of the warrant, petitioner briefed the search team and provided a copy of the search warrant application, the supporting affidavit, and the warrant for the officers to review. Petitioner orally reviewed the terms of the warrant with the officers, including the specific items for which the officers were authorized to search. Petitioner and his search team then conducted the search entirely within the scope of the warrant application and warrant; that is, within the scope of what the Magistrate had authorized. Finding no illegal weapons or explosives, the search team seized nothing. <span class="citation multiple-matches"><a href="/c/F.%203d/298/1022/">298 F. 3d 1022</a></span>, 1025 (CA9 2002). When petitioner left, he gave respondents a copy of the search warrant. Upon request the next day, petitioner faxed respondents a copy of the more detailed <span class="star-pagination">*577</span> warrant application. Indeed, putting aside the technical defect in the warrant, it is hard to imagine how the actual search could have been carried out any more reasonably.</p>
<p>The Court argues that this eminently reasonable search is nonetheless unreasonable because "there can be no written assurance that the Magistrate actually found probable cause to search for, and to seize, every item mentioned in the affidavit" "unless the particular items described in the affidavit are also set forth in the warrant itself." <i>Ante,</i> at 560. The Court argues that it was at least possible that the Magistrate intended to authorize a much more limited search than the one petitioner requested. <i>Ante,</i> at 560-561. As a theoretical matter, this may be true. But the more reasonable inference is that the Magistrate intended to authorize everything in the warrant application, as he signed the application and did not make any written adjustments to the application or the warrant itself.</p>
<p>The Court also attempts to bolster its focus on the faulty warrant by arguing that the purpose of the particularity requirement is not only to prevent general searches, but also to assure the searchee of the lawful authority for the search. <i>Ante,</i> at 561. But as the Court recognizes, neither the Fourth Amendment nor Federal Rule of Criminal Procedure 41 requires an officer to serve the warrant on the searchee before the search. <i>Ante,</i> at 562, n. 5. Thus, a search should not be considered <i>per se</i> unreasonable for failing to apprise the searchee of the lawful authority prior to the search, especially where, as here, the officer promptly provides the requisite information when the defect in the papers is detected. Additionally, unless the Court adopts the Court of Appeals' view that the Constitution protects a searchee's ability to "be on the lookout and to challenge officers," while the officers are actually carrying out the search, <span class="citation" data-id="778595"><a href="/opinion/778595/ramirez-v-butte-silver-bow-county/#1027" aria-description="Citation for case: Ramirez v. Butte-Silver Bow County">298 F. 3d, at 1027</a></span>, petitioner's provision of the requisite information the following day is sufficient to satisfy this interest.</p>
<p></p>
<h2>
<span class="star-pagination">*578</span> III</h2>
<p>Even assuming a constitutional violation, I would find that petitioner is entitled to qualified immunity. The qualified immunity inquiry rests on "the `objective legal reasonableness' of the action, <i>Harlow</i> [v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#819" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 819</a></span> (1982)], assessed in light of the legal rules that were `clearly established' at the time it was taken." <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#639" aria-description="Citation for case: Anderson v. Creighton">483 U. S., at 639</a></span>. The outcome of this inquiry "depends substantially upon the level of generality at which the relevant `legal rule' is . . . identified. For example, the right to due process of law is quite clearly established by the Due Process Clause, and thus there is a sense in which any action that violates that Clause . . . violates a clearly established right." <i><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Ibid.</a></span></i> To apply the standard at such a high level of generality would allow plaintiffs "to convert the rule of qualified immunity . . . into a rule of virtually unqualified liability simply by alleging violation of extremely abstract rights." <i><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Ibid.</a></span></i> The Court in <i>Anderson</i> criticized the Court of Appeals for considering the qualified immunity question only in terms of the petitioner's "right to be free from warrantless searches of one's home unless the searching officers have probable cause and there are exigent circumstances." <i>Id.,</i> at 640. The Court of Appeals should have instead considered "the objective (albeit fact-specific) question whether a reasonable officer could have believed Anderson's warrantless search to be lawful, in light of clearly established law and the information the searching officers possessed." <i>Id.,</i> at 641.</p>
<p>The Court errs not only by defining the question at too high a level of generality but also by assessing the question without regard to the relevant circumstances. Even if it were true that no reasonable officer could believe that a search of a home pursuant to a warrant that fails the particularity requirement is lawful absent exigent circumstances  a proposition apparently established by dicta buried in a footnote in <i><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span></i>  petitioner did not know when he carried <span class="star-pagination">*579</span> out the search that the search warrant was invalidlet alone legally nonexistent. Petitioner's entitlement to qualified immunity, then, turns on whether his belief that the search warrant was valid was objectively reasonable. Petitioner's belief surely was reasonable.</p>
<p>The Court has stated that "depending on the circumstances of the particular case, a warrant may be so facially deficient . . . that the executing officers cannot reasonably presume it to be valid." <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U. S., at 923</a></span>. This language makes clear that this exception to <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i>'s good-faith exception does not apply in every circumstance. And the Court does not explain why it should apply here. As an initial matter, the Court does not even argue that the fact that petitioner made a mistake in preparing the warrant was objectively unreasonable, nor could it. Given the sheer number of warrants prepared and executed by officers each year, combined with the fact that these same officers also prepare detailed and sometimes somewhat comprehensive documents supporting the warrant applications, it is inevitable that officers acting reasonably and entirely in good faith will occasionally make such errors.</p>
<p>The only remaining question is whether petitioner's failure to notice the defect was objectively unreasonable. The Court today points to no cases directing an officer to proofread a warrant after it has been passed on by a neutral magistrate, where the officer is already fully aware of the scope of the intended search and the magistrate gives no reason to believe that he has authorized anything other than the requested search. Nor does the Court point to any case suggesting that where the same officer both prepares and executes the invalid warrant, he can never rely on the magistrate's assurance that the warrant is proper. Indeed, in <i>Massachusetts</i> v. <i>Sheppard,</i> <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S. 981</a></span> (1984), the Court suggested that although an officer who is not involved in the warrant application process would normally read the issued warrant to determine the object of the search, an executing <span class="star-pagination">*580</span> officer who is also the affiant might not need to do so. <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#989" aria-description="Citation for case: Massachusetts v. Sheppard"><i>Id.,</i> at 989, n. 6</a></span>.</p>
<p>Although the Court contends that it does not impose a proofreading requirement upon officers executing warrants, <i>ante,</i> at 563, n. 6, I see no other way to read its decision, particularly where, as here, petitioner could have done nothing more to ensure the reasonableness of his actions than to proofread the warrant. After receiving several allegations that respondents possessed illegal firearms and explosives, petitioner prepared an application for a warrant to search respondents' ranch, along with a supporting affidavit detailing the history of allegations against respondents, petitioner's investigation into these allegations, and petitioner's verification of the sources of the allegations. Petitioner properly filled out the warrant application, which described both the place to be searched and the things to be seized, and obtained the Magistrate's signature on both the warrant application and the warrant itself. Prior to execution of the warrant, petitioner briefed the search team to ensure that each officer understood the limits of the search. Petitioner and his search team then executed the warrant within those limits. And when the error in the search warrant was discovered, petitioner promptly faxed the missing information to respondents. In my view, petitioner's actions were objectively reasonable, and thus he should be entitled to qualified immunity.</p>
<p>For the foregoing reasons, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   A brief of <i>amici curiae</i> urging reversal was filed for the State of Texas et al. by <i>Greg Abbott,</i> Attorney General of Texas, <i>R. Ted Cruz,</i> Solicitor General, <i>Barry R. McBee,</i> First Assistant Attorney General, <i>Jay Kimbrough,</i> Deputy Attorney General, and <i>Ryan D. Clinton,</i> Assistant Solicitor General, and by the Attorneys General for their respective States as follows: <i>Gregg D. Renkes</i> of Alaska, <i>M. Jane Brady</i> of Delaware, <i>Charles J. Crist, Jr.,</i> of Florida, <i>Mark J. Bennett</i> of Hawaii, <i>Steve Carter</i> of Indiana, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Mike Hatch</i> of Minnesota, <i>Mike Moore</i> of Mississippi, <i>Brian Sandoval</i> of Nevada, W. A. <i>Drew Edmondson</i> of Oklahoma, <i>D. Michael Fisher</i> of Pennsylvania, <i>Lawrence E. Long</i> of South Dakota, <i>William H. Sorrell</i> of Vermont, <i>Jerry W. Kilgore</i> of Virginia, <i>Christine O. Gregoire</i> of Washington, and <i>Peggy A. Lautenschlager</i> of Wisconsin.</p>
<p>[1]  Possession of these items, if unregistered, would violate <span class="citation no-link">18 U. S. C. § 922</span>(<i>o</i>)(1) and <span class="citation no-link">26 U. S. C. § 5861</span>.</p>
<p>[2]  The warrant stated: "[T]here is now concealed [on the specified premises] a certain person or property, namely [a] single dwelling residence two story in height which is blue in color and has two additions attached to the east. The front entrance to the residence faces in a southerly direction." App. to Pet. for Cert. 26a.</p>
<p>[3]  The affidavit was sealed. Its sufficiency is not disputed.</p>
<p>[4]  For this reason petitioner's argument that any constitutional error was committed by the Magistrate, not petitioner, is misplaced. In <i>Massachusetts</i> v. <i>Sheppard,</i> <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S. 981</a></span> (1984), we suggested that "the judge, not the police officers," may have committed "[a]n error of constitutional dimension," <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#990" aria-description="Citation for case: Massachusetts v. Sheppard"><i>id.,</i> at 990</a></span>, because the judge had assured the officers requesting the warrant that he would take the steps necessary to conform the warrant to constitutional requirements, <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#986" aria-description="Citation for case: Massachusetts v. Sheppard"><i>id.,</i> at 986</a></span>. Thus, "it was not unreasonable for the police in [that] case to rely on the judge's assurances that the warrant authorized the search they had requested." <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#989" aria-description="Citation for case: Massachusetts v. Sheppard"><i>Id.,</i> at 989, n. 6</a></span>. In this case, by contrast, petitioner did not alert the Magistrate to the defect in the warrant that petitioner had drafted, and we therefore cannot know whether the Magistrate was aware of the scope of the search he was authorizing. Nor would it have been reasonable for petitioner to rely on a warrant that was so patently defective, even if the Magistrate was aware of the deficiency. See <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#915" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 915, 922, n. 23</a></span> (1984).</p>
<p>[5]  It is true, as petitioner points out, that neither the Fourth Amendment nor Rule 41 of the Federal Rules of Criminal Procedure requires the executing officer to serve the warrant on the owner before commencing the search. Rule 41(f)(3) provides that "[t]he officer executing the warrant must: (A) give a copy of the warrant and a receipt for the property taken to the person from whom, or from whose premises, the property was taken; or (B) leave a copy of the warrant and receipt at the place where the officer took the property." Quite obviously, in some circumstancesa surreptitious search by means of a wiretap, for example, or the search of empty or abandoned premises  it will be impracticable or imprudent for the officers to show the warrant in advance. See <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#355" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 355, n. 16</a></span> (1967); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#37" aria-description="Citation for case: Ker v. California">374 U. S. 23, 37-41</a></span> (1963). Whether it would be unreasonable to refuse a request to furnish the warrant at the outset of the search when, as in this case, an occupant of the premises is present and poses no threat to the officers' safe and effective performance of their mission, is a question that this case does not present.</p>
<p>[6]  The Court of Appeals' decision is consistent with this principle. Petitioner mischaracterizes the court's decision when he contends that it imposed a novel proofreading requirement on officers executing warrants. The court held that officers leading a search team must "mak[e] sure that they have a proper warrant that in fact authorizes the search and seizure they are about to conduct." <span class="citation multiple-matches"><a href="/c/F.%203d/298/1022/">298 F. 3d 1022</a></span>, 1027 (CA9 2002). That is not a duty to proofread; it is, rather, a duty to ensure that the warrant conforms to constitutional requirements.</p>
<p>[7]  We do not suggest that an official is deprived of qualified immunity whenever he violates an internal guideline. We refer to the ATF Order only to underscore that petitioner should have known that he should not execute a patently defective warrant.</p>
<p>[8]  Although both <i><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span></i> and <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> involved the application of the "good faith" exception to the Fourth Amendment's general exclusionary rule, we have explained that "the same standard of objective reasonableness that we applied in the context of a suppression hearing in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> defines the qualified immunity accorded an officer." <i>Malley</i> v. <i>Briggs,</i> <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#344" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 344</a></span> (1986) (citation omitted).</p>
<p>[9]  JUSTICE KENNEDY argues in dissent that we have not allowed "`ample room for mistaken judgments,'" <i>post,</i> at 571 (quoting <i>Malley,</i> <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#343" aria-description="Citation for case: Malley v. Briggs">475 U. S., at 343</a></span>), because "difficult and important tasks demand the officer's full attention in the heat of an ongoing and often dangerous criminal investigation," <i>post,</i> at 568. In this case, however, petitioner does not contend that any sort of exigency existed when he drafted the affidavit, the warrant application, and the warrant, or when he conducted the search. This is not the situation, therefore, in which we have recognized that "officers in the dangerous and difficult process of making arrests and executing search warrants" require "some latitude." <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#87" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 87</a></span> (1987).
</p>
<p>Nor are we according "the correctness of paper forms" a higher status than "substantive rights." <i>Post,</i> at 571. As we have explained, the Fourth Amendment's particularity requirement assures the subject of the search that a magistrate has duly authorized the officer to conduct a search of limited scope. This substantive right is not protected when the officer fails to take the time to glance at the authorizing document and detect a glaring defect that JUSTICE KENNEDY agrees is of constitutional magnitude, <i>post</i> this page.</p>

</div>
```

---
