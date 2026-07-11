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

## GROUP: _overhaul2/lake/cases/State v. Mitcham.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "State v. Mitcham"
type: case
citation: "559 P.3d 1099 (2024)"
parallel_cite: ""
neutral_cite: ""
court: Arizona Supreme Court
court_level: state
circuit: ""
year: 2024
date_decided: 2024-12-17
docket: CR-23-0238-PR
authority_weight: "Persuasive — state, illustrative"
treatment:
  field_i_validity: good_law
  as_of_content: 2024-12-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: State v. Mitcham
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10293607/state-of-arizona-v-ian-mitcham/"
  cluster_id: 10293607
  opinion_id: 10760195
  identity_checked: false
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Recent development (role-based)"
related: ["[[Nix v. Williams]]", "[[Murray v. United States]]", "[[Segura v. United States]]", "[[Herring v. United States]]", "[[Utah v. Strieff]]"]
aliases: ["State of Arizona v. Ian Mitcham"]
tags: ["case", "exclusionary-rule", "inevitable-discovery", "independent-source", "dna", "arizona"]
holding: "Arizona Supreme Court applies the independent-source exception: evidence discovered during/because of an unlawful search is admissible…"
lake:
  record_id: State v. Mitcham
  status: under_review
  projected_at: 2026-07-06
---

# State v. Mitcham

*258 Ariz. 435, 559 P.3d 1099 (2024)* · Arizona Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a 2015 cold-case murder (victim Allison Feldman), police obtained Mitcham's DNA through an unlawful warrantless search of a second vial of blood drawn after a 2015 DUI arrest; the DNA matched, and Mitcham moved to suppress. Separately, Mitcham had been convicted in 2022 of unrelated felonies (narcotics and aggravated DUI), which by statute required collection of his DNA upon imprisonment.

## Issue
Whether DNA evidence obtained through an unlawful search must be suppressed, or whether an exception to the exclusionary rule permits its use.

## Rule
The Court distinguished and applied the exclusionary-rule exceptions. "The 'independent source' exception permits the admission of evidence discovered during or because of an unlawful search if the evidence was also obtained independently from activities that were tainted by the illegality." — 258 Ariz. 435, ¶ 34 (2024). ^pin-34

The two exceptions differ in that the distinction "rests on whether the evidence was discovered through an independent, untainted source ..., or whether the evidence would have been discovered through an independent, untainted source despite the illegal search ...." — *Id.* ¶ 36. ^pin-36

Applying [[Inevitable Discovery and Independent Source|inevitable discovery]], the Court held the State "would have inevitably obtained Mitcham's DNA profile from an independent, untainted source despite the warrantless search of the second vial of blood ...." — *Id.* ¶ 37. ^pin-37

## Application
Mitcham's unrelated 2022 felony convictions and prison sentence triggered Arizona's statutory requirement (A.R.S. § 13-610) that the Department of Corrections collect his DNA for profiling. That lawful, untainted process would inevitably have produced the same DNA profile independent of the illegal 2018 search; the only reason it did not was that police already held a sample from the illegal search. Suppression would put the prosecution in a worse position than if the violation had never occurred, so the inevitable-discovery exception applied.

## Conclusion
The DNA evidence was admissible under the inevitable-discovery exception; suppression was denied.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Persuasive — state, illustrative**.
- Applies the inevitable-discovery exception of [[Nix v. Williams]] and its independent-source roots ([[Murray v. United States]], [[Segura v. United States]]) within the deterrence-focused exclusionary framework of [[Herring v. United States]] and [[Utah v. Strieff]].

## Appears on
- [[The Exclusionary Rule]] — *Recent development (role-based)*

## Sources
- *State v. Mitcham*, 258 Ariz. 435, 559 P.3d 1099 (Ariz. 2024) — https://www.courtlistener.com/opinion/10293607/state-of-arizona-v-ian-mitcham/ (lead opinion id 10760195) — pinpoints: ¶¶ 34, 36, 37.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "03a5081424775da2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "State v. Mitcham"}, "payload": {"all": [{"cite": "559 P.3d 1099", "page": "1099", "reporter": "P.3d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "559"}], "display": "559 P.3d 1099", "official": {"cite": "559 P.3d 1099", "page": "1099", "reporter": "P.3d", "selected_official": true, "source": "cluster.citations[]", "type": 3, "volume": "559"}, "official_selection_present": true, "record_id": "State v. Mitcham"}}
{"assertion_id": "35ee42d1f8e32577", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-36", "record_id": "State v. Mitcham"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-36", "pinpoint_status": "slip-only", "quote": "rests on whether the evidence was discovered through an independent, untainted source ..., or whether the evidence would have been discovered through an independent, untainted source despite the illegal search ....", "quote_fidelity": "mismatch", "record_id": "State v. Mitcham", "star_marker": null}}
{"assertion_id": "61cdf5efdd859394", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-37", "record_id": "State v. Mitcham"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-37", "pinpoint_status": "slip-only", "quote": "would have inevitably obtained Mitcham's DNA profile from an independent, untainted source despite the warrantless search of the second vial of blood ....", "quote_fidelity": "mismatch", "record_id": "State v. Mitcham", "star_marker": null}}
{"assertion_id": "d6bbdd8469334276", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-34", "record_id": "State v. Mitcham"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-34", "pinpoint_status": "slip-only", "quote": "--- # State v. Mitcham *258 Ariz. 435, 559 P.3d 1099 (2024)* · Arizona Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a 2015 cold-case murder (victim Allison Feldman), police obtained Mitcham's DNA through an unlawful warrantless search of a second vial of blood drawn after a 2015 DUI arrest; the DNA matched, and Mitcham moved to suppress. Separately, Mitcham had been convicted in 2022 of unrelated felonies (narcotics and aggravated DUI), which by statute required collection of his DNA upon imprisonment. ## Issue Whether DNA evidence obtained through an unlawful search must be suppressed, or whether an exception to the exclusionary rule permits its use. ## Rule The Court distinguished and applied the exclusionary-rule exceptions.", "quote_fidelity": "mismatch", "record_id": "State v. Mitcham", "star_marker": null}}
{"assertion_id": "38698018a982faf1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Mitcham"}, "payload": {"as_of_content": "2024-12-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "State v. Mitcham", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — State v. Mitcham

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Mitcham",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "State of Arizona v. Ian Mitcham",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "State v. Mitcham",
    "court": "Arizona Supreme Court",
    "court_id": "ariz",
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "2024-12-17",
    "year": 2024,
    "docket": "CR-23-0238-PR",
    "cluster_id": 10293607,
    "lead_opinion_id": 10760195,
    "sibling_ids": [
      10760195
    ],
    "absolute_url": "/opinion/10293607/state-of-arizona-v-ian-mitcham/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "559 P.3d 1099",
      "volume": "559",
      "reporter": "P.3d",
      "page": "1099",
      "type": 3,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "559 P.3d 1099",
        "volume": "559",
        "reporter": "P.3d",
        "page": "1099",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "559 P.3d 1099",
    "official_selection": {
      "court_class": "state",
      "selected": "559 P.3d 1099",
      "reason": "selected_rank_2"
    }
  },
  "pinpoints": [
    {
      "id": "pin-34",
      "page": null,
      "quote": "--- # State v. Mitcham *258 Ariz. 435, 559 P.3d 1099 (2024)* \u00b7 Arizona Supreme Court \u00b7 **Persuasive \u2014 state, illustrative** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a 2015 cold-case murder (victim Allison Feldman), police obtained Mitcham's DNA through an unlawful warrantless search of a second vial of blood drawn after a 2015 DUI arrest; the DNA matched, and Mitcham moved to suppress. Separately, Mitcham had been convicted in 2022 of unrelated felonies (narcotics and aggravated DUI), which by statute required collection of his DNA upon imprisonment. ## Issue Whether DNA evidence obtained through an unlawful search must be suppressed, or whether an exception to the exclusionary rule permits its use. ## Rule The Court distinguished and applied the exclusionary-rule exceptions.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-36",
      "page": null,
      "quote": "rests on whether the evidence was discovered through an independent, untainted source ..., or whether the evidence would have been discovered through an independent, untainted source despite the illegal search ....",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-37",
      "page": null,
      "quote": "would have inevitably obtained Mitcham's DNA profile from an independent, untainted source despite the warrantless search of the second vial of blood ....",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2024-12-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "State v. Mitcham",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(10760195) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ariz OR arizctapp)",
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
        "query": "cites:(10760195)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(10760195)",
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
    "complete_query": "cites:(10760195)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 10760195,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/state-v-mitcham.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 10760195,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 450747,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 700649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 755893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 867200,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 867501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 873669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1135969,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1179100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1206372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1297298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1393415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 2582173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 2813060,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 3214776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 3216391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 3418437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4028107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4171004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4206137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4583624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4650433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 5666093,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 6104581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 6105914,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 6110937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 6480131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 7263677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 7268856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9422064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9422515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9427563,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9427638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9428007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9429647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9429757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9431434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9431606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9432279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9433685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9434934,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9457073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9476246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9514985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9571325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9628491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9637378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9812443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9822918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9888052,
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
    "date_created": "2026-07-05T20:31:00Z",
    "date_modified": "2026-07-06T08:52:25Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:31:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:31:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:32:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:31:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — State v. Mitcham

```
                               IN THE

    SUPREME COURT OF THE STATE OF ARIZONA

                          STATE OF ARIZONA,
                              Appellant,

                                  v.

                            IAN MITCHAM,
                               Appellee.




                         No. CR-23-0236-PR
                       Filed December 17, 2024


          Appeal from the Superior Court in Maricopa County
              The Honorable Roy C. Whitehead, Judge
                       No. CR2018-118086-001

                   REVERSED AND REMANDED


                   Opinion of the Court of Appeals,
                            Division One
                      256 Ariz. 104 (App. 2023)

                             VACATED



COUNSEL:

Rachel H. Mitchell, Maricopa County Attorney, Nick Klingerman (argued),
Special Deputy County Attorney, Ryan Green, Deputy County Attorney,
Maricopa County Attorney’s Office, Phoenix, Attorneys for State of
Arizona

Gary Kula, Maricopa County Public Defender, Mikel Steinfeld (argued),
Martha Barco Penunuri, Jeffrey A. Kirchler, Richard D. Randall, Deputy
                            STATE V. MITCHAM
                           Opinion of the Court

Public Defenders, Phoenix, Attorneys for Ian Mitcham

David J. Euchner (argued), Pima County Public Defender’s Office, Grant D.
Wille, Ralls, Wille, & Coomer, P.C., Tucson, Attorneys for Amicus Curiae
Arizona Attorneys for Criminal Justice

Kristin K. Mayes, Arizona Attorney General, Alice M. Jones, Deputy
Solicitor General/Section Chief of Criminal Appeals, Michael O’Toole,
Assistant Attorney General, Phoenix, Attorneys for Amicus Curiae Arizona
Attorney General

Jared G. Keenan, Lauren K. Beall, American Civil Liberties Union
Foundation of Arizona; Vera Eidelman, American Civil Liberties Union
Foundation, New York, NY, Attorneys for Amici Curiae American Civil
Liberties Union of Arizona and American Civil Liberties Union



CHIEF JUSTICE TIMMER authored the Opinion of the Court, in which
VICE CHIEF JUSTICE LOPEZ, JUSTICES BOLICK, BEENE, KING,
BRUTINEL (RETIRED), and JUDGE SKLAR joined. *




CHIEF JUSTICE TIMMER, Opinion of the Court:

¶1           After police arrested Ian Mitcham for driving under the
influence of alcohol (“DUI”), he consented to a blood test to determine
alcohol concentration or drug content. Years later, police suspected
Mitcham of committing a murder, and they still had Mitcham’s blood from
the DUI arrest. Without obtaining a warrant, they extracted a DNA profile
from that blood, which linked Mitcham to the murder.




*  Justice Brutinel retired after oral argument in this case but nevertheless
participated in deciding this opinion. Justice Montgomery is recused from
this matter. Pursuant to article 6, section 3 of the Arizona Constitution,
Judge Jeffrey Sklar of the Arizona Court of Appeals, Division Two, was
designated to sit in this matter.

                                     2
                             STATE V. MITCHAM
                            Opinion of the Court

¶2            We decide that the police violated Mitcham’s Fourth
Amendment rights by conducting the warrantless search. Because the
inevitable discovery exception to the exclusionary rule applies, however,
we hold that the trial court erred by suppressing the DNA evidence.

                             BACKGROUND

¶3            In January 2015, Scottsdale Police arrested Mitcham for DUI.
A police officer advised Mitcham that Arizona law required him to submit
to a blood test to determine alcohol concentration or drug content. The
officer explained that if Mitcham refused to consent to testing, the state
would suspend his driver’s license for twelve months.            Mitcham
consented.

¶4             The police drew two vials of blood from Mitcham and used
one vial for their test. They made the second vial available to Mitcham to
allow him to independently test his blood.             Mitcham signed a
“Destruction Notice,” acknowledging that police would destroy the second
vial if he did not ask for it within ninety days. Mitcham never asked for
the second vial, but the police did not destroy it. Mitcham was ultimately
convicted of a misdemeanor DUI.

¶5            Tragically, one month after Mitcham’s DUI arrest, Allison
Feldman was found murdered in her Scottsdale home. The police
collected biological swabs from the scene, developed a male DNA profile,
and uploaded it into the National DNA Index System (“NDIS”) using the
Combined DNA Index System (“CODIS”).                See A.R.S. § 41-2418(A)
(establishing Arizona’s DNA identification system). CODIS is a software
program maintained by the Federal Bureau of Investigation that “link[s]
DNA profiles culled from federal, state, and territorial DNA collection
programs,” United States v. Kriesel, 508 F.3d 941, 944 (9th Cir. 2007), and
searches the NDIS database of DNA profiles taken from convicted
offenders, among others.        See 34 U.S.C. § 12592(a) (authorizing the
establishment of a national DNA index); see also Lockett v. Wray, 271 F. Supp.
3d 205, 209 (D.D.C. 2017) (relating expert descriptions of NDIS and CODIS).
CODIS did not return a match, and Feldman’s murder remained unsolved
for several years.

¶6           In 2017, police initiated a “familial DNA” investigation on the
unknown-male DNA profile by asking the Arizona Department of Public
Safety (“DPS”) to search Arizona’s DNA identification system to determine

                                      3
                            STATE V. MITCHAM
                           Opinion of the Court

whether anyone incarcerated by the state is related to that unknown male.
See § 41-2418(A). Through this investigation, DPS identified Mitcham’s
incarcerated brother as closely related—most likely through a parent-child
or sibling relationship—to the man whose DNA was collected at the
murder scene. The police then discovered that the inmate had two sons
and three brothers, including Mitcham. Only Mitcham and one other
brother lived in the Phoenix area.

¶7           The police focused their investigation on Mitcham. An
investigating officer reviewed Mitcham’s 2015 DUI arrest records and
learned that both vials of blood taken from Mitcham were still in police
possession. Without obtaining a warrant, the police analyzed the blood in
the second vial and created Mitcham’s DNA profile. On April 5, 2018, the
police crime lab determined that Mitcham’s profile matched the
unknown-male DNA profile taken from Feldman’s house.

¶8             Days later, the trial court issued search warrants permitting
officers to search Mitcham’s home and seize certain items; place a GPS
tracking device on his car; and obtain buccal samples from Mitcham for
purposes of DNA profiling.          The affidavits supporting the warrant
applications described the circumstances leading the police to Mitcham and
stated that officers had used the blood sample taken in the 2015 DUI arrest
to match Mitcham’s DNA with the unknown-male DNA profile from the
murder scene.

¶9             On April 10, police collected buccal swabs from Mitcham
pursuant to the search warrant. The police created another DNA profile
from this sample, which again matched the unknown-male DNA profile
taken from the murder scene. On April 18, a grand jury indicted Mitcham
for first degree murder, second degree burglary, and sexual assault.

¶10           On July 7, 2022, Mitcham moved the trial court to suppress
both (1) the DNA evidence gathered from the second vial taken during his
2015 DUI arrest; and (2) the DNA evidence extracted from the buccal swabs
collected pursuant to the 2018 search warrant. After an evidentiary
hearing, the court granted the motion, reasoning that the warrantless search
of the second vial of blood violated the Fourth Amendment, and no
exceptions to exclusion applied. It also suppressed the DNA evidence
gathered from the buccal swabs pursuant to the warrant, reasoning that the
evidence was “the direct result of the improper DNA extraction [in 2018].”
The court subsequently stayed proceedings to permit the State to appeal its
                                     4
                             STATE V. MITCHAM
                            Opinion of the Court

ruling. See A.R.S. § 13-4032(6) (permitting the state to appeal “[a]n order
granting a motion to suppress the use of evidence”).

¶11             The court of appeals unanimously reversed, but the judges
had different reasons for doing so. See State v. Mitcham, 256 Ariz. 104
(App. 2023). The majority concluded that although the police had violated
Mitcham’s Fourth Amendment rights, excluding the DNA evidence was
not warranted because the evidence would inevitably have been
discovered, and it had an independent source. See id. at 115 ¶¶ 46–47, 51.
The concurring judge found no Fourth Amendment violation, explaining
that Mitcham did not have a reasonable expectation of privacy in the second
vial of blood because it was lawfully in police possession. See id. ¶ 53
(Catlett, J., concurring).

¶12           We granted Mitcham’s subsequently filed petition for review
to determine (1) whether the sequencing of Mitcham’s DNA profile from
the second vial of blood taken during the 2015 DUI arrest constituted a
search and violated Mitcham’s rights under the Fourth Amendment; and
(2) if so, whether the DNA evidence should be suppressed. These are
potentially recurring issues of statewide importance and therefore merit
our review. We have jurisdiction under article 6, section 5(3) of the
Arizona Constitution.

                               DISCUSSION

¶13           We review a trial court’s factual findings on a motion to
suppress for an abuse of discretion. State v. Smith, 250 Ariz. 69, 80 ¶ 16
(2020). In doing so, we consider “only the evidence presented at the
suppression hearing and [view such evidence] in the light most favorable
to sustaining the trial court’s ruling.” State v. Thompson, 252 Ariz. 279, 290
¶ 26 (2022) (quoting State v. Primous, 242 Ariz. 221, 223 ¶ 10 (2017)). But
we review de novo the trial court’s legal determination about whether a
search complied with the Fourth Amendment. State v. Jean, 243 Ariz. 331,
334 ¶ 9 (2018).

A. The Police Violated Mitcham’s Fourth Amendment Rights By
Sequencing A DNA Profile From The Second Vial Of Blood Taken
During The 2015 DUI Arrest.

¶14          The Fourth Amendment to the United States Constitution
“safeguard[s] the privacy and security of individuals against arbitrary

                                      5
                             STATE V. MITCHAM
                            Opinion of the Court

invasions by governmental officials.” Carpenter v. United States, 585 U.S.
296, 303 (2018) (quoting Camara v. Municipal Court, 387 U.S. 523, 528 (1967)).
Although Fourth Amendment violations were formerly “tied to
common-law trespass,” United States v. Jones, 565 U.S. 400, 405 (2012), the
Supreme Court has recognized that “the Fourth Amendment protects
people, not places,” Carpenter, 585 U.S. at 304 (quoting Katz v. United States,
389 U.S. 347, 351 (1967)). Thus, when an individual “seeks to preserve
[something] as private,” and that expectation of privacy is “one that society
is prepared to recognize as ‘reasonable,’” Fourth Amendment protections
will apply. Smith v. Maryland, 442 U.S. 735, 740 (1979) (alteration in
original) (quoting Katz, 389 U.S. at 351, 361); see also Florida v. Jimeno, 500
U.S. 248, 250 (1991) (“The touchstone of the Fourth Amendment is
reasonableness.”).

¶15           A search occurs when the government infringes a privacy
interest that society considers to be reasonable. See State v. Mixton, 250
Ariz. 282, 286 ¶ 13 (2021). Such an intrusion “generally . . . requires a
warrant supported by probable cause.”         Carpenter, 585 U.S. at 304.
Warrantless searches are “per se unreasonable under the Fourth
Amendment—subject only to a few specifically established and
well-delineated exceptions.” Katz, 389 U.S. at 357 (footnote omitted).

       1.   A search occurred here.

¶16           The State argues that sequencing Mitcham’s DNA from the
second vial of blood collected during his 2015 DUI arrest was not a “search”
for Fourth Amendment purposes because it already lawfully possessed the
blood. To resolve this argument, we begin with this Court’s opinion in
Mario W. v. Kaipio, 230 Ariz. 122 (2012). There, we considered the
constitutionality of an Arizona law requiring juveniles accused of
committing enumerated offenses to provide law enforcement with a buccal
swab for DNA profiling. Id. at 123–24 ¶ 1. After sequencing, the DNA
profiles were entered into CODIS and Arizona’s DNA identification
database. See id. at 124 ¶ 5. If not ultimately adjudicated delinquent, the
juvenile could petition the court for expungement of the profile from the
databases. Id.

¶17            The Court recognized that the challenged law intruded on a
juvenile’s privacy by authorizing law enforcement to both physically collect
the buccal sample and then process it to extract a DNA profile. Id.
at 126–27 ¶ 18. We therefore addressed each intrusion separately. See id.

                                      6
                             STATE V. MITCHAM
                            Opinion of the Court

at 127 ¶ 20 (noting that a two-tiered analysis was particularly appropriate
because DNA profiling is much more intrusive than collecting buccal cells).

¶18           We first concluded that collecting the buccal sample was
constitutionally permissible. Id. at 128 ¶ 25. We reasoned that the buccal
swab was minimally intrusive, and the state was justified in collecting the
sample for identification purposes before the juvenile was adjudicated
delinquent because it would lose its chance at collection if the juvenile
absconded. See id. at 127–28 ¶¶ 22–25.

¶19            We then reached a different conclusion about the
constitutionality of extracting a DNA profile from the buccal sample before
the juvenile was adjudicated delinquent.           See id. at 129 ¶ 32.    We
recognized that “[t]his second search presents a greater privacy concern
than the buccal swab because it involves the extraction (and subsequent
publication to law enforcement nationwide) of thirteen genetic markers
from the arrestee’s DNA sample that create a DNA profile effectively
unique to that individual.” Id. at 128 ¶ 27. Further, we could not
perceive any governmental interest in processing the sample and creating
the DNA profile before adjudication. Id. at 129 ¶ 28. Thus, we concluded
that the state’s interest in processing the sample before adjudication did not
justify the serious intrusion on a juvenile’s privacy interest in the DNA
profile. Id. ¶ 32. Notably, we remarked that:

       [O]ne accused of a crime, although having diminished
       expectations of privacy in some respects, does not forfeit
       Fourth Amendment protections with respect to other offenses
       not charged absent either probable cause or reasonable
       suspicion. An arrest for vehicular homicide, for example,
       cannot alone justify a warrantless search of an arrestee’s
       financial records to see if he is also an embezzler.

Id. ¶ 31. We therefore disallowed processing the buccal cells to extract a
DNA profile before a delinquency adjudication as an unreasonable search
under the Fourth Amendment. See id. ¶ 32.

¶20           Although Mario W. seemingly resolves that the police in this
case conducted a “search” by extracting Mitcham’s DNA profile from the
second vial of blood taken during his 2015 DUI arrest, the State argues that
the Supreme Court in Maryland v. King, 569 U.S. 435 (2013), overruled Mario
W. The State describes King as concluding that “sequencing a DNA profile
                                      7
                            STATE V. MITCHAM
                           Opinion of the Court

from lawfully obtained evidence is not a second ‘search’ within the
meaning of the Fourth Amendment.” With that characterization, the State
argues that King overruled Mario W. to the extent the latter case concluded
that creating a DNA profile from a buccal swab is a “search” under the
Fourth Amendment. We disagree.

¶21           In King, the Supreme Court held that a Maryland law
authorizing law enforcement officials to “collect DNA samples” from
persons arrested for specific felony offenses—committing or attempting to
commit violent crimes or burglaries—did not violate the Fourth
Amendment. 569 U.S. at 443, 465. The Court found that “using a buccal
swab on the inner tissues of a person’s cheek in order to obtain DNA
samples is a search.” Id. at 446. But it noted that “[t]he expectations of
privacy of an individual taken into police custody ‘necessarily [are] of a
diminished scope.’” Id. at 462 (second alteration in original) (quoting Bell
v. Wolfish, 441 U.S. 520, 557 (1979)). It characterized that search as
minimally intrusive and outweighed by substantial government interests
in identifying arrestees and determining whether they had committed other
crimes. Id. at 461, 463–64. And the DNA analysis did not reveal any
information about the arrestee other than mere identification.           Id.
at 464–65.

¶22           Importantly, the Court never addressed whether creating a
DNA profile from the buccal sample was a separate “search.” Instead, the
Court examined as a set whether collecting and analyzing a DNA sample
taken from felony arrestees violates the Fourth Amendment. See id. at 442.
Because the collection and analysis occurred in short order as part of “a
routine booking procedure” after a suspect’s arrest, the Court had no need
to address whether the analysis itself was a “search.” See id. at 465.

¶23            The conclusion we take from King is that “taking and
analyzing a cheek swab of the arrestee’s DNA is, like fingerprinting and
photographing, a legitimate police booking procedure that is reasonable
under the Fourth Amendment.” Id. at 465–66 (“Upon these considerations
the Court concludes that DNA identification of arrestees is a reasonable
search that can be considered part of a routine booking procedure.”
(emphasis added)). Thus, King overruled Mario W. to the extent the latter
case held that processing buccal swabs before adjudication violated the
juveniles’ Fourth Amendment rights. See Mario W., 230 Ariz. at 129 ¶ 32.
But King did not address whether creating a DNA profile from an arrestee’s
cell sample itself constitutes a separate search. Thus, we do not view King
                                     8
                             STATE V. MITCHAM
                            Opinion of the Court

as overruling Mario W.’s conclusion that processing a sample to extract a
DNA profile is a search. Cf. Birchfield v. N.D. Dep’t of Transp., 579 U.S. 438,
464 (2016) (recognizing that blood can reveal information beyond alcohol
and drug content); Skinner v. Ry. Lab. Execs.’ Ass’n, 489 U.S. 602, 617–18
(1989) (referring to “the collection and subsequent analysis [of urine
samples]” as separate searches under the Fourth Amendment).

¶24            Mario W. remains controlling. We therefore conclude that
extracting Mitcham’s DNA profile in 2018 from the second vial of blood
taken during his 2015 DUI arrest was a “search” under the Fourth
Amendment. See also Skinner, 489 U.S. at 616 (recognizing that the
chemical analysis of a blood sample to obtain physiological data is an
invasion of privacy interests apart from the blood draw itself); State v.
Martinez, 570 S.W.3d 278, 292 (Tex. Crim. App. 2019) (concluding that
subsequent testing of blood drawn for medical purposes constituted “a
Fourth Amendment search separate and apart from the seizure of the blood
by the State”); People v. Thomas, 132 Cal. Rptr. 3d 714, 716 (Cal. Ct. App.
2011) (“When an individual is compelled to provide a biological sample for
analysis, the collection and subsequent analysis of the sample are treated as
separate searches because they intrude on separate privacy interests.”).

       2.   The search was unreasonable.

¶25             Unlike the situation in King, the police here did not extract
Mitcham’s DNA profile pursuant to statutory authority governing routine
booking procedures intended to identify perpetrators. See 569 U.S. at 443;
see also In re Leopoldo L., 209 Ariz. 249, 252 ¶ 14 (App. 2004) (explaining that
“compelled DNA testing of juveniles adjudicated delinquent for
committing sexual offenses is not an unreasonable search” because
statutory procedural safeguards “are more stringent than those required for
issuance of a search warrant based on a probable cause finding”). And the
police did not obtain a warrant to create Mitcham’s DNA profile from the
second vial of blood. Under these circumstances, the warrantless search
was unreasonable under the Fourth Amendment absent an exception. See
Katz, 389 U.S. at 357.

¶26           One such exception occurred here if Mitcham freely and
voluntarily consented to the search. See State v. Valenzuela, 239 Ariz. 299,
301 ¶ 1 (2016); see also Jimeno, 500 U.S. at 250–51 (“[W]e have long approved
consensual searches because it is no doubt reasonable for the police to
conduct a search once they have been permitted to do so.”). The State

                                       9
                             STATE V. MITCHAM
                            Opinion of the Court

bears the burden of proving by a preponderance of the evidence that
Mitcham voluntarily consented to the search and that the search fell within
the scope of that consent. See Valenzuela, 239 Ariz. at 302–03 ¶ 11; State v.
Ontiveros-Loya, 237 Ariz. 472, 479 ¶ 24 (App. 2015); Ariz. R. Crim. P. 16.2(b);
see also Walter v. United States, 447 U.S. 649, 656 (1980) (“When an official
search is properly authorized—whether by consent or by the issuance of a
valid warrant—the scope of the search is limited by the terms of its
authorization.”).

¶27            The State argues that Mitcham consented to the 2018
warrantless search by consenting to the 2015 DUI blood draw, giving the
State lawful possession of the sample and the freedom to later use it to
create a DNA profile. Mitcham acknowledges he consented to the blood
draw in 2015 to allow the State to determine his alcohol concentration or
drug content. But he argues the State exceeded the scope of that consent
by later creating the DNA profile to determine his culpability for Feldman’s
murder, making the warrantless search unreasonable under the Fourth
Amendment.

¶28          Courts measure the scope of a consent to search using an
objective standard: “what would the typical reasonable person have
understood by the exchange between the officer and the suspect?” Jimeno,
500 U.S. at 251. The question before us then is whether a reasonable
person would have understood that consenting to a blood draw to
determine alcohol concentration or drug content would include consent to
create a DNA profile from that sample. See id. We do not think so.

¶29           Here, the search authorization terms were simple and
unambiguous. Mitcham consented to the blood draw after an officer
advised him that Arizona’s implied consent law required him to submit to
the blood draw “for the purpose of determining alcohol concentration or
drug content.” 1 See A.R.S. § 28-1321(A). The officer did not tell Mitcham
that his blood could be used to create a DNA profile, and Mitcham did not
consent to the search of his blood for that purpose. Further, it was not

1  The year after Mitcham’s blood draw, we held that “showing only that
consent was given in response to this admonition fails to prove that an
arrestee’s consent was freely and voluntarily given.” Valenzuela, 239 Ariz.
at 301 ¶ 2. Mitcham does not challenge the voluntariness of his consent to
draw his blood for purposes of determining his alcohol concentration or
drug content.
                                      10
                             STATE V. MITCHAM
                            Opinion of the Court

necessary to create a DNA profile to determine alcohol concentration or
drug content. And Mitcham agreed that his second vial of blood would
be destroyed in ninety days if he did not first retrieve it, further supporting
a reasonable belief that Mitcham’s consent was limited to searching for
evidence pertinent only to the pending DUI charge, not other, future
crimes.

¶30            A typical reasonable person in Mitcham’s circumstances
would not have understood that consenting to the blood draw for the
limited purpose of determining alcohol concentration or drug content also
included consenting to the creation of a DNA profile, especially years later.
See Jimeno, 500 U.S. at 251. The search of the blood to create the DNA
profile therefore exceeded the scope of Mitcham’s consent and cannot serve
as an exception to the warrant requirement. See State v. Billups, 118 Ariz.
124, 126 (1978) (finding that police exceeded the scope of the defendant’s
consent to search his house by searching an unattached shed); United States
v. Dichiarinte, 445 F.2d 126, 128, 130 (7th Cir. 1971) (finding that federal
narcotics agents exceeded the scope of the defendant’s consent to search his
home for narcotics by searching for documents); see also People v. Schmoll, 48
N.E.2d 933, 934 (Ill. 1943) (“An arresting officer has no more right to make
a search beyond the limit prescribed in a consent to search, than he has to
exceed the limit prescribed in a search warrant.”). Other courts have
reached similar conclusions in analogous situations. See People v. Pickard,
222 Cal. Rptr. 3d 686, 687, 689 (Cal. App. Dep’t Super. Ct. 2017) (recognizing
that when a driver consents to a blood test under a state’s implied consent
law, further testing of the sample for other substances or DNA may be
beyond the scope of the consent); State v. Binner, 886 P.2d 1056, 1059 (Or.
Ct. App. 1994) (concluding that the defendant who consented to a blood
draw for purposes of determining alcohol concentration did not consent to
having his blood tested for drugs); State v. Gerace, 437 S.E.2d 862, 863 (Ga.
Ct. App. 1993) (concluding that consent given to test blood for alcohol
concentration did not include consent to extract a DNA profile).

¶31            In sum, the 2018 creation of Mitcham’s DNA profile from the
second vial of blood taken during the 2015 DUI arrest was a search. That
search was unreasonable and violated the Fourth Amendment because it
was not authorized by a warrant, and the search exceeded the scope of
Mitcham’s consent to analyze his blood to determine alcohol concentration
or drug content. In reaching this conclusion, we emphatically reject the
State’s position that it was free to analyze Mitcham’s blood in any way it
pleased simply because the State lawfully possessed the blood vials. See
                                      11
                              STATE V. MITCHAM
                             Opinion of the Court

Walter, 447 U.S. at 654 (“The fact that FBI agents were lawfully in possession
of the boxes of film did not give them authority to search their contents.”);
Gerace, 437 S.E.2d at 863 (“The State’s argument that because the blood
sample was obtained with consent it is free to use it for any purpose, paints
the notion of consent with far too broad a brush.”). Although Mitcham
lost his possessory rights to the second vial of blood, he did not lose all of
his privacy rights in that blood. See Mario W., 230 Ariz. at 128 ¶ 27, 129
¶ 31; see also State v. Granville, 423 S.W.3d 399, 426 (Tex. Crim. App. 2014)
(Keller, P.J., concurring) (recognizing that people can have expectations of
privacy in the informational dimension of property separate and apart from
the expectation of privacy in the physical dimension of that property). The
police violated Mitcham’s Fourth Amendment rights by conducting a
search beyond the scope of his consent.

B. The Exclusionary Rule Does Not Require Suppression Of Mitcham’s
DNA Profile.

       1.   There are exceptions to the exclusionary rule.

¶32             The Fourth Amendment itself does not require courts to
suppress evidence gathered in violation of that amendment. See Davis v.
United States, 564 U.S. 229, 236–38 (2011). Instead, courts invoke the
judicially created “exclusionary rule” to suppress evidence obtained in
violation of the Fourth Amendment. See Utah v. Strieff, 579 U.S. 232, 237
(2016); Wong Sun v. United States, 371 U.S. 471, 484–85 (1963); Valenzuela, 239
Ariz. at 308–09 ¶ 31. The exclusionary rule is a prudential doctrine created
to “compel respect for the constitutional guaranty” by deterring future
violations. See Davis, 564 U.S. at 236 (quoting Elkins v. United States, 364
U.S. 206, 217 (1960)); Valenzuela, 239 Ariz. at 308–09 ¶ 31. The rule applies
to evidence obtained directly from an illegal search and to evidence later
discovered because of the illegal search, which is commonly called the
“fruit of the poisonous tree.” Strieff, 579 U.S. at 237 (quoting Segura v.
United States, 468 U.S. 796, 804 (1984)). The rationale for the exclusionary
rule is that the prosecution should not be placed in a better position because
of the illegal conduct. Nix v. Williams, 467 U.S. 431, 443 (1984).

¶33            Importantly, “[s]uppression of evidence . . . has always been
our last resort, not our first impulse.” Hudson v. Michigan, 547 U.S. 586,
591 (2006); State v. Weakland, 246 Ariz. 67, 73 ¶ 20 (2019). We only apply
the exclusionary rule “where its deterrence benefits outweigh its
‘substantial social costs.’” Hudson, 547 U.S. at 591 (quoting Pa. Bd. of Prob.
& Parole v. Scott, 524 U.S. 357, 363 (1998)); Nix, 467 U.S. at 443 (accepting that
                                        12
                              STATE V. MITCHAM
                             Opinion of the Court

the way to ensure Fourth Amendment protections “is to exclude evidence
seized as a result of such violations notwithstanding the high social cost of
letting persons obviously guilty go unpunished for their crimes”).
Consequently, we have recognized several exceptions to the exclusionary
rule, including the “independent source” and “inevitable discovery”
exceptions. See Strieff, 579 U.S. at 238.

¶34             The “independent source” exception permits the admission
of evidence discovered during or because of an unlawful search if the
evidence was also obtained independently from activities that were tainted
by the illegality. See Murray v. United States, 487 U.S. 533, 537–38 (1988);
State v. Bolt, 142 Ariz. 260, 263 (1984). For instance, in Segura, the Supreme
Court held that although the police illegally entered private premises, the
exclusionary rule did not apply because police seized property at those
premises pursuant to a search warrant that was based on information
unconnected to the illegal entry. 468 U.S. at 814. The independent
source exception, which applies to violations of the Fourth, Fifth, and Sixth
Amendments, rests on the premise that “while the government should not
profit from its illegal activity, neither should it be placed in a worse position
than it would otherwise have occupied” without the illegal conduct. See
Murray, 487 U.S. at 537, 542.

¶35            The “inevitable discovery” exception applies “[i]f the
prosecution can establish by a preponderance of the evidence that the
information ultimately or inevitably would have been discovered by lawful
means,” making the reason for applying the exclusionary rule meaningless.
Nix, 467 U.S. at 444.      Courts extrapolated this exception from the
independent source exception, reasoning that because “tainted evidence
would be admissible if in fact discovered through an independent source,
it should be admissible if it inevitably would have been discovered” from
such a source. Murray, 487 U.S. at 539. Importantly, “[t]he exception
does not turn on whether the evidence would have been discovered had
[officers] acted lawfully in the first place,” but instead “applies if the
evidence would have been lawfully discovered despite the unlawful
behavior and independent of it.” Brown v. McClennen, 239 Ariz. 521,
524–25 ¶ 14 (2016) (emphasis added). For example, in State v. Jones, 185
Ariz. 471, 481 (1996), we held that despite an improper warrantless search
of the arrested defendant’s belongings while stowed in a police car, because
police inevitably would have conducted a proper inventory search of those
belongings upon return to the station, the exclusionary rule did not apply
to suppress evidence of the defendant’s bloody clothing.
                                       13
                            STATE V. MITCHAM
                           Opinion of the Court


¶36           In sum, the distinction between the independent source
exception and the inevitable discovery exception rests on whether the
evidence was discovered through an independent, untainted source
(independent source exception), or whether the evidence would have been
discovered through an independent, untainted source despite the illegal
search (inevitable discovery exception). See State v. Boll, 651 N.W.2d 710,
716–17 ¶¶ 20–26 (S.D. 2002) (similarly distinguishing these exceptions).

      2.   The inevitable discovery exception applies here.

¶37            Turning to this case, we agree with the State that the police
would have inevitably obtained Mitcham’s DNA profile from an
independent, untainted source despite the warrantless search of the second
vial of blood taken after the 2015 DUI arrest. To prove the inevitable
discovery exception, the State cannot speculate but must instead “focus[]
on demonstrated historical facts capable of ready verification or
impeachment.” Nix, 467 U.S. at 444 n.5. The court “view[s] affairs as
they existed at the instant before the unlawful search” and then determines
“what would have happened had the unlawful search never occurred.”
United States v. Kennedy, 61 F.3d 494, 498 (6th Cir. 1995) (quoting United
States v. Eng, 971 F.2d 854, 861 (2d Cir. 1992)).

¶38            Here, the verifiable facts demonstrate inevitable discovery of
Mitcham’s DNA profile. At the time of the illegal search in 2018, Mitcham
was facing charges unrelated to Feldman’s murder. In 2016, the state
charged him with committing a narcotic drug violation, a class four felony.
The next year, the state charged him with two counts of aggravated DUI,
class six felonies. In June 2022, about six months before the suppression
hearing in this case, Mitcham pled guilty to all charges in the narcotics/DUI
cases, and the court sentenced him to a term of imprisonment in the Arizona
Department of Corrections, Rehabilitation and Reentry (“ADCRR”).

¶39           Arizona law requires ADCRR to take a sample of blood or
other bodily substance for purposes of DNA profiling from every person
convicted of a felony and sentenced to prison. See A.R.S. § 13-610(A), (O). 2


2 Section 13-610(A) refers to the “state department of corrections.” That
agency has changed its name to the “Arizona Department of Corrections,
Rehabilitation   and    Reentry.”         See   ADCRR      Home      Page,

                                     14
                             STATE V. MITCHAM
                            Opinion of the Court

Thereafter, ADCRR is required to transmit the sample to DPS, which must
extract a DNA profile and enter the results into Arizona’s DNA
identification system and CODIS. See Mario W., 230 Ariz. at 124 ¶ 5;
§ 13-610(H); § 41-2418(A).     The profile can then be used for “law
enforcement identification purposes” and in any criminal prosecution.
See § 13-610(I)(1)–(2). ADCRR must extract the sample for DNA profiling
within thirty days of sentencing but is prohibited from doing so if DPS “has
previously received and is maintaining a sample sufficient for [DNA]
testing.” See § 13-610(A), (G).

¶40           Pursuant to § 13-610, the State would have inevitably
discovered Mitcham’s DNA profile despite the illegal search of the second
vial of blood taken in 2015. The narcotics/DUI convictions and resulting
sentences were unrelated to and thus untainted by the illegal searches.
Had those searches not occurred, § 13-610(A) would have required ADCRR
to collect samples of Mitcham’s blood or bodily substances, and DPS would
have obtained the same DNA profile that was extracted from the second
vial of blood. As Mitcham acknowledged at oral argument, the only
reason this did not occur was because DPS already had Mitcham’s genetic
sample and DNA profile from the searches conducted in 2018, 3 and was
therefore prohibited from taking new samples.               See § 13-610(G).
Suppressing the DNA evidence in these circumstances would not fulfill the
exclusionary rule’s purpose of preventing the prosecution from being in a
better position due to the illegal search. See Nix, 467 U.S. at 443. Instead,
suppression would put the prosecution in a worse position than it would
have been in without the illegal search. See Murray, 487 U.S. at 537, 542.

¶41           We are not persuaded by Mitcham’s arguments against
application of the inevitable discovery exception. First, he argues that the


https://corrections.az.gov (last visited Dec. 9, 2024). We therefore refer to
the agency using its current name.
3  We could not determine from the record whether the Scottsdale Police
transferred Mitcham’s blood sample to DPS and uploaded the DNA profile
into Arizona’s DNA identification system. But the police were required to
transmit a sample of buccal cells or other bodily substances for DNA testing
to DPS when Mitcham was arrested for Feldman’s murder in 2018. See
§ 13-610(K) (requiring transmittal of a sample for persons arrested for listed
offenses, including first degree murder). Mitcham acknowledges that in
2018 DPS had a sample of his genetic material and his DNA profile.
                                     15
                            STATE V. MITCHAM
                           Opinion of the Court

DNA profile would not have been inevitably discovered from his 2022
felony convictions because DPS never received a blood or bodily substance
sample from which to create a DNA profile. See § 13-610(A). This
argument places form over substance, and we reject it. As explained,
§ 13-610(G) prohibited ADCRR from extracting a new sample because DPS
already had a sample and a DNA profile. The point here is that had the
illegal search not occurred, ADCRR would have provided a sample to DPS,
which would have extracted Mitcham’s DNA profile. And no purpose
would be served by suppressing Mitcham’s DNA profile only to have
ADCRR provide DPS with a new sample so the same profile could again be
extracted.

¶42            Second, Mitcham asserts that the inevitable discovery
exception applies only when “regular police work already in progress” at
the time of the illegal search demonstrates that the evidence would have
been inevitably discovered. Mitcham contends that because “the possible
‘future’ acquisition of [his] DNA from his 2022 convictions is not evidence
that ‘inevitably’ emerged during the homicide investigation,” and the
police “had no way of knowing that [he] would plead guilty over four years
later” to the narcotics/DUI charges, the police investigating at the time of
the illegal searches would not have inevitably discovered his DNA profile.
Applying the inevitable discovery exception in these circumstances, he
argues, would “rel[y] solely on speculation, and such speculation alone
cannot sustain the State’s burden” under Nix. We disagree.

¶43            Relying exclusively on investigative facts and procedures
available to police at the time of the illegal search to assess inevitable
discovery is unnecessarily restrictive. Nix did not confine the examination
of “historical facts capable of ready verification or impeachment” to facts
existing before an illegal search. See Nix, 467 U.S. at 444 n.5. Notably,
“Arizona has adopted the broad view of the inevitable discovery rule,” and
so “the State is not required to demonstrate that police initiated lawful
means to acquire evidence prior to its seizure.” State v. Davolt, 207 Ariz.
191, 204 ¶ 37 (2004). Similarly, we see no reason to require the State to
prove the exception by projecting investigative outcomes using only facts
available to the police before the illegal search. The key inquiry is whether
verifiable facts exist from which the court can find, at the time of the
suppression hearing, that the evidence would have been lawfully
discovered despite the illegal search and independent of it. See Brown, 239
Ariz. at 525 ¶ 14.


                                     16
                             STATE V. MITCHAM
                            Opinion of the Court

¶44            We find the Seventh Circuit’s decision in Sutton v. Pfister, 834
F.3d 816 (7th Cir. 2016), persuasive. There, the State of Illinois unlawfully
collected a sample of defendant Sutton’s blood during his prosecution for a
1991 attempted sexual assault and extracted his DNA profile. Id. at 818.
The state did not introduce DNA evidence at trial, but Sutton was
nevertheless convicted and sentenced to prison. See id. Meanwhile, law
enforcement matched Sutton’s illegally obtained DNA profile to physical
evidence collected from a 1990 sexual assault. See id. The Seventh Circuit
held that the inevitable discovery exception permitted the trial court to
admit the DNA evidence in Sutton’s 1990 sexual assault trial. See id. at 822.
It found that the state would have lawfully obtained Sutton’s blood sample
upon his conviction for the 1991 attempted sexual assault pursuant to an
Illinois law that required blood and saliva samples from convicted sex
offenders. See id. Conspicuously, the decision did not turn on whether
police in the 1991 case had any way of knowing at the time of the illegal
search that Sutton would be convicted without the DNA evidence and then
lawfully required to submit blood and saliva samples.

¶45           The cases cited by Mitcham do not persuade us to view the
inevitable discovery exception more restrictively. In State v. Lamb, 116
Ariz. 134, 138 (1977), this Court agreed with other courts that “evidence
obtained as a result of an unlawful search need not be suppressed where,
in the normal course of the police investigation and absent the illicit
conduct, the evidence would have been discovered anyway.” Although
the events demonstrating inevitable discovery there had occurred at the
time of the illegal search, nothing in Lamb precluded application of the
inevitable discovery exception if new events had occurred after the illegal
search. The key consideration was whether the means of discovery was
untainted by the illegal search. See id.

¶46           The cases Mitcham cites from other jurisdictions admittedly
use language suggesting that the inevitable discovery exception applies
only when investigative facts existing before an illegal search demonstrate
inevitable discovery. See United States v. Lang, 149 F.3d 1044, 1047 (9th Cir.
1998) (stating that application of the exception requires a court “to
determine whether a reasonable probability of discovery existed prior to
the unlawful conduct, based on the information possessed and
investigations being pursued at such time” (quoting United States v. Drosten,
819 F.2d 1067, 1070 (11th Cir. 1987))); Eng, 971 F.2d at 861 (“[T]he alternate
means of obtaining the evidence must at least be in existence and, at least
to some degree, imminent, if yet unrealized.” (alteration in original)
                                      17
                             STATE V. MITCHAM
                            Opinion of the Court

(quoting United States v. Cherry, 759 F.2d 1196, 1205 n.10 (5th Cir. 1985))).
Neither case, however, dealt with identification evidence like the DNA
evidence here, which can be extracted from different sources and at
different times. Rather, they concerned physical evidence that was the
subject of the illegal search. See Lang, 149 F.3d at 1046 (concerning “crack
cocaine found in a cereal box hidden inside the engine compartment” of a
vehicle); Eng, 971 F.2d at 857 (regarding the contents of defendant’s safe).
Thus, it is unsurprising that these courts required the government to show
that an active investigation, independent from and untainted by the illegal
search, would have uncovered the evidence. Regardless, to the extent
these cases categorically preclude assessment of events occurring after the
illegal search to decide whether to apply the inevitable discovery exception,
we disagree for the reasons previously explained. See Part B(2), ¶¶ 38–40,
43–44.

¶47            In sum, the inevitable discovery exception applies here, and
the trial court therefore erred by suppressing Mitcham’s DNA profile. If
the police had not created a DNA profile from the second vial of blood in
2018, DPS would have done so after his 2022 felony convictions. This is
certain, not speculative, so it easily satisfies the preponderance standard
adopted in Nix. See Nix, 467 U.S. at 444 n.5. In light of this conclusion,
we do not address whether other exceptions to the exclusionary rule apply
here. And we do not address Mitcham’s arguments based on the Arizona
Constitution’s Private Affairs Clause, as they were neither raised at the trial
court nor sufficiently developed here. See Ariz. Const. art. 2, § 8.

                              CONCLUSION

¶48           For the foregoing reasons, although we agree with the court
of appeals’ holding, we vacate its opinion to replace its reasoning with our
own. We also reverse the trial court’s suppression order and remand for
further proceedings.




                                      18

```

---

## GROUP: _overhaul2/lake/cases/State v. Tarantino.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "State v. Tarantino"
type: case
citation: ""
parallel_cite: "368 S.E.2d 588; 322 N.C. 386; 1988 N.C. LEXIS 373"
neutral_cite: ""
court: North Carolina Supreme Court
court_level: state
circuit: ""
year: 1988
date_decided: 1988-06-02
docket: 678PA87
authority_weight: "Persuasive — state, illustrative"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-06-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: State v. Tarantino
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/1294594/state-v-tarantino/"
  cluster_id: 1294594
  opinion_id: 9854442
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Progeny / Refinement"
related: ["[[California v. Ciraolo]]", "[[Arizona v. Hicks]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "plain-view", "open-view", "expectation-of-privacy", "north-carolina"]
holding: "A reasonable expectation of privacy in a building's interior is NOT eliminated by small (quarter-inch) cracks; an officer who must 'bend…"
lake:
  record_id: State v. Tarantino
  status: verified
  projected_at: 2026-07-06
---

# State v. Tarantino

*322 N.C. 386, 368 S.E.2d 588 (1988)* · North Carolina Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a tip, Detective Baker went at night to a closed, sealed building on Tarantino's property; by maneuvering his body and shining a flashlight through quarter-inch cracks near the floor in the back wall, he saw marijuana plants inside, then obtained a warrant and seized them. Tarantino moved to suppress the initial observation as a warrantless search.

## Issue
Whether a person retains a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a sealed building's interior despite small cracks in its wall, such that an officer's probing observation through them is a search.

## Rule
Small gaps do not by themselves defeat a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]]. "This expectation was not unreasonable even though there were small cracks between the boards in the building's back wall. The presence of tiny cracks near the floor on the interior wall of a second-floor porch is not the kind of exposure which serves to eliminate a reasonable expectation of privacy." — 368 S.E.2d at 591. ^pin-591

"Nothing in the Supreme Court's *Dunn* decision suggests that an expectation of privacy is eliminated by quarter-inch cracks in the back wall of an otherwise sealed building." — *Id.* at 591–592. ^pin-591a

And because "the cracks near the porch floor required him to make a probing examination in order to see inside[,] ... defendant's reasonable expectation of privacy remained intact." — *Id.* at 592. ^pin-592

## Application
Tarantino had sealed the building—padlocked front door, nailed back doors, boarded windows—so he retained a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in its interior. Because Detective Baker had to bend down and make a probing examination through tiny floor-level cracks, rather than view the interior from an ordinary vantage point, his observation was a warrantless search, and the trial court properly suppressed it.

## Conclusion
The defendant's expectation of privacy survived the small cracks; the warrantless observation was an unlawful search, and the suppression order was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Persuasive — state, illustrative**.
- Marks the open-view boundary of the [[Plain View Doctrine|plain-view doctrine]]—an officer's lawful vantage point ([[California v. Ciraolo]]) versus a probing intrusion to see inside—and complements the rule that even a minimal manipulation to observe can itself be a search ([[Arizona v. Hicks]]); applies the expectation-of-privacy test of [[Katz v. United States]].

## Appears on
- [[Plain View Doctrine]] — *Key — Progeny / Refinement*

## Sources
- *State v. Tarantino*, 322 N.C. 386, 368 S.E.2d 588 (1988) — https://www.courtlistener.com/opinion/1294594/state-v-tarantino/ — pinpoints: 591, 592 (S.E.2d).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "08bc03f591384b4f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "State v. Tarantino"}, "payload": {"all": [{"cite": "368 S.E.2d 588", "page": "588", "reporter": "S.E.2d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "368"}, {"cite": "322 N.C. 386", "page": "386", "reporter": "N.C.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "322"}, {"cite": "1988 N.C. LEXIS 373", "page": "373", "reporter": "N.C. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "1988"}], "display": null, "official": null, "official_selection_present": false, "record_id": "State v. Tarantino"}}
{"assertion_id": "23d2485cfc0ce8e8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-592", "record_id": "State v. Tarantino"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-592", "pinpoint_status": "slip-only", "quote": "the cracks near the porch floor required him to make a probing examination in order to see inside[,] ... defendant's reasonable expectation of privacy remained intact.", "quote_fidelity": "mismatch", "record_id": "State v. Tarantino", "star_marker": null}}
{"assertion_id": "59ecba9ad35b6f03", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-591a", "record_id": "State v. Tarantino"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-591a", "pinpoint_status": "slip-only", "quote": "Nothing in the Supreme Court's *Dunn* decision suggests that an expectation of privacy is eliminated by quarter-inch cracks in the back wall of an otherwise sealed building.", "quote_fidelity": "mismatch", "record_id": "State v. Tarantino", "star_marker": null}}
{"assertion_id": "cf7056138e6b2692", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-591", "record_id": "State v. Tarantino"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-591", "pinpoint_status": "slip-only", "quote": "--- # State v. Tarantino *322 N.C. 386, 368 S.E.2d 588 (1988)* · North Carolina Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a tip, Detective Baker went at night to a closed, sealed building on Tarantino's property; by maneuvering his body and shining a flashlight through quarter-inch cracks near the floor in the back wall, he saw marijuana plants inside, then obtained a warrant and seized them. Tarantino moved to suppress the initial observation as a warrantless search. ## Issue Whether a person retains a reasonable expectation of privacy in a sealed building's interior despite small cracks in its wall, such that an officer's probing observation through them is a search. ## Rule Small gaps do not by themselves defeat a reasonable expectation of privacy.", "quote_fidelity": "mismatch", "record_id": "State v. Tarantino", "star_marker": null}}
{"assertion_id": "eb34802a610f7f9b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Tarantino"}, "payload": {"as_of_content": "1988-06-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "State v. Tarantino", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — State v. Tarantino

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Tarantino",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "State v. Tarantino",
    "case_name_short": "Tarantino",
    "case_name_full": "State of North Carolina v. Joseph Mario Tarantino",
    "input_case_name": "State v. Tarantino",
    "court": "North Carolina Supreme Court",
    "court_id": "nc",
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "1988-06-02",
    "year": 1988,
    "docket": "678PA87",
    "cluster_id": 1294594,
    "lead_opinion_id": 9854442,
    "sibling_ids": [
      1294594,
      9854442,
      9854443
    ],
    "absolute_url": "/opinion/1294594/state-v-tarantino/",
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
        "cite": "368 S.E.2d 588",
        "volume": "368",
        "reporter": "S.E.2d",
        "page": "588",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "322 N.C. 386",
        "volume": "322",
        "reporter": "N.C.",
        "page": "386",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 N.C. LEXIS 373",
        "volume": "1988",
        "reporter": "N.C. LEXIS",
        "page": "373",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "368 S.E.2d 588",
        "volume": "368",
        "reporter": "S.E.2d",
        "page": "588",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "322 N.C. 386",
        "volume": "322",
        "reporter": "N.C.",
        "page": "386",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 N.C. LEXIS 373",
        "volume": "1988",
        "reporter": "N.C. LEXIS",
        "page": "373",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "state",
      "selected": null,
      "reason": "same_rank_tie"
    }
  },
  "pinpoints": [
    {
      "id": "pin-591",
      "page": null,
      "quote": "--- # State v. Tarantino *322 N.C. 386, 368 S.E.2d 588 (1988)* \u00b7 North Carolina Supreme Court \u00b7 **Persuasive \u2014 state, illustrative** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a tip, Detective Baker went at night to a closed, sealed building on Tarantino's property; by maneuvering his body and shining a flashlight through quarter-inch cracks near the floor in the back wall, he saw marijuana plants inside, then obtained a warrant and seized them. Tarantino moved to suppress the initial observation as a warrantless search. ## Issue Whether a person retains a reasonable expectation of privacy in a sealed building's interior despite small cracks in its wall, such that an officer's probing observation through them is a search. ## Rule Small gaps do not by themselves defeat a reasonable expectation of privacy.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-591a",
      "page": null,
      "quote": "Nothing in the Supreme Court's *Dunn* decision suggests that an expectation of privacy is eliminated by quarter-inch cracks in the back wall of an otherwise sealed building.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-592",
      "page": null,
      "quote": "the cracks near the porch floor required him to make a probing examination in order to see inside[,] ... defendant's reasonable expectation of privacy remained intact.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-06-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "State v. Tarantino",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rose",
          "cluster_id": 1251000,
          "cite": [
            "909 P.2d 280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Tarantino:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Glick",
          "cluster_id": 2453691,
          "cite": [
            "250 P.3d 578",
            "2011 WL 1566710"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Tarantino:lane2_top_cited"
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
        "journal_ref": "State v. Tarantino:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nance",
          "cluster_id": 1296688,
          "cite": [
            "562 S.E.2d 557",
            "149 N.C. App. 734",
            "2002 N.C. App. LEXIS 315"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Tarantino:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rose",
          "cluster_id": 1258968,
          "cite": [
            "876 P.2d 925",
            "75 Wash. App. 28",
            "1994 Wash. App. LEXIS 312"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Tarantino:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Barnes",
          "cluster_id": 1284972,
          "cite": [
            "582 S.E.2d 313",
            "158 N.C. App. 606",
            "2003 N.C. App. LEXIS 1232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Tarantino:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Herlth, J.",
          "cluster_id": 10870804,
          "cite": [
            "2026 Pa. Super. 114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Tarantino:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(1294594 OR 9854442 OR 9854443) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR nc OR ncctapp)",
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
        "query": "cites:(1294594 OR 9854442 OR 9854443)",
        "reviewed": 9,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 7,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(1294594 OR 9854442 OR 9854443)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 0,
        "triage_snippet_classified": 2
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(1294594 OR 9854442 OR 9854443)",
    "indexed_citing_opinions": 9,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 1294594,
        "count": 7,
        "count_source": "search"
      },
      {
        "opinion_id": 9854442,
        "count": 2,
        "count_source": "search"
      },
      {
        "opinion_id": 9854443,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 17,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/state-v-tarantino.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 9,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 1294594,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 454693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 1169275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 1183387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 1200960,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 1206533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 1287214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 1340838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 1354211,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1294594,
        "cited_id": 2149587,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T20:32:22Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: same_rank_tie",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:32:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:32:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:34:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:32:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — State v. Tarantino

```
<opinion type="majority">
<author id="b431-5">EXUM, Chief Justice.</author>
<p id="b431-6">The sole issue this case presents is whether, in light of the United States Supreme Court’s decision in <em>Dunn v. United States, </em>480 U.S. —, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d 326</a></span> (1987), the Court of Appeals correctly upheld the trial court’s decision to grant defendant’s motion to suppress evidence seized from his building because the information furnishing probable cause for the search warrant was obtained in violation of the Fourth Amendment of the United States Constitution. We answer yes, and affirm the Court of Appeals.</p>
<p id="b431-7">I.</p>
<p id="b431-8">On 10 April 1986 Judge Gray conducted a hearing on defendant’s motion to suppress evidence seized from a building he owned. After the hearing, he made findings of fact to which neither the state nor defendant except. He found that on 30 August 1985 B. R. Baker, Jr., a detective in the Avery County Sheriffs Department, received a telephone call from a confidential informant who said he had seen marijuana plants growing on the second floor of the old “Aldridge Store Building.” The caller informed Detective Baker that the plants could be observed by looking through cracks in the building’s back wall. Detective Baker concluded he lacked probable cause to obtain a search warrant because he knew the caller to be unreliable. At approximately 11 p.m. he went to the building, without a warrant, to investigate the caller’s claims.</p>
<p id="b431-9">The building which Detective Baker investigated was a two-story frame structure built into a hillside. It was in poor repair when he made his inspection. The windows were boarded from the inside, the solid-wood front door was padlocked, and the back doors — one solid and the other with a paneless window covered by wood — were nailed shut. The back doors opened directly to the building’s second floor from a porch which had a large open entrance. At the bottom of the wall between the porch doors were several cracks where the wooden boards did not join com<page-number citation-index="1" label="388">*388</page-number>pletely. These cracks were no more than one-quarter of an inch wide.</p>
<p id="b432-6">Detective Baker began his investigation by knocking on the front door. He then climbed the hill to the second-story porch, using a flashlight to guide his way along a little-used path. He entered the porch and knocked on one of the doors inside. Receiving no answer, he searched the back wall until he found cracks in the wall between the doors. By maneuvering his body and shining his flashlight through the cracks, Detective Baker illuminated a small part of the building’s interior and saw marijuana plants. He returned to the Avery County Sheriffs Department, executed an affidavit, obtained a search warrant from a magistrate, returned to the premises and seized the marijuana.</p>
<p id="b432-7">After making these findings, Judge Gray concluded, as a matter of law, that Detective Baker’s first inspection of the building constituted a warrantless search in violation of the Fourth Amendment. He determined defendant had a reasonable expectation of privacy in the premises searched. He further adjudged that the search fell within no exception to the Fourth Amendment’s requirement of a valid warrant. On the basis of his factual findings and legal conclusions, Judge Gray granted defendant’s motion to suppress.</p>
<p id="b432-8">The Court of Appeals affirmed Judge Gray’s decision. <em>State v. Tarantino, </em><span class="citation" data-id="1340838"><a href="/opinion/1340838/state-v-tarantino/" aria-description="Citation for case: State v. Tarantino">83 N.C. App. 473</a></span>, <span class="citation" data-id="1340838"><a href="/opinion/1340838/state-v-tarantino/" aria-description="Citation for case: State v. Tarantino">350 S.E. 2d 864</a></span> (1986). Subsequently, the United States Supreme Court decided <em>United States v. Dunn, </em>480 U.S. —, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d 326</a></span>. The state petitioned for discretionary review in light of the <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span> </em>decision. We granted the state’s petition and remanded the case to the Court of Appeals for further consideration in light of <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span>. </em>The Court of Appeals reaffirmed its previous decision, holding that the facts in the present case and those in <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span> </em>are sufficiently distinguishable such that <em>Dunn's </em>holding does not require a different result. <em>State v. Tarantino, </em>86 N.C. App. at 442, 358 S.E. 2d at 132.</p>
<p id="b432-9">II.</p>
<p id="b432-10">In <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span> </em>the United States Supreme Court held that Drug Administration Enforcement agents did not violate the Fourth Amendment when they peered into the “essentially open front” of the defendant’s barn and saw what they thought to be a drug lab<page-number citation-index="1" label="389">*389</page-number>oratory. <em>United States v. Dunn, </em>480 U.S. at —, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/#334" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d at 334</a></span>. The agents made their observations at night after crossing several fences encircling the barn, which was located about 60 yards from the defendant’s ranch house residence. A locked wooden fence with a waist-high gate barred the agents from entering the barn. The barn’s front section was open, covered only by netting material stretching from the barn’s ceiling to the gate’s top. By standing next to the netting and shining flashlights inside the barn, the agents acquired sufficient information to obtain a search warrant. Pursuant to the warrant, the agents seized chemicals and equipment and arrested the defendant. <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Id.</a></span> </em>at —, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/#332" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d at 332-34</a></span>.</p>
<p id="b433-4">The primary issue confronting the Court in <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span>, </em>as the Court of Appeals noted in its opinion below, was whether the agents’ search violated the defendant’s Fourth Amendment rights because the barn lay within the curtilage of his home. The Court held the barn did not lie within the house’s curtilage, applying a four-part test drawn from prior cases. <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Id.</a></span> </em>at —, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/#334" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d at 334</a></span>. However one might view the Court’s determination of the curtilage question in <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span>, </em>it has no bearing in the instant case, for no curtilage question is here presented.</p>
<p id="b433-5">The second issue addressed in <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span> </em>was whether the defendant possessed a reasonable expectation of privacy, independent from his home’s curtilage, in the barn and its contents. The Court assumed, for argument’s sake, that the barn itself could not be entered or its contents seized without a warrant, but went on to hold that the officers properly peered into its interior over the front gate. It reasoned, on the basis of its resolution of the curtilage question, that the officers lawfully approached and stood next to the barn because the land surrounding it was a constitutionally unprotected “open field.” From this vantage point the officers rightfully used flashlights to peer through the netting material covering the barn’s opening. The Court held “the officers’ use of the beam of a flashlight, directed through the essentially open front of [the defendant’s] barn, did not transform their observations into an unreasonable search within the meaning of the Fourth Amendment.” <em>United States v. Dunn, </em>480 U.S. at —, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/#337" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d at 337</a></span>. In so holding the Court drew support from its recent decision in <em>California v. Ciraolo </em>in which it stated “the Fourth Amendment ‘has never been extended to require law en<page-number citation-index="1" label="390">*390</page-number>forcement officers to shield their eyes when passing by a home on a public thoroughfare’.” <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Id.</a></span> </em>at —, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d at 337</a></span> (quoting <em>California v. Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo">476 U.S. 207, 213</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#216" aria-description="Citation for case: California v. Ciraolo">90 L.Ed. 2d 210, 216</a></span> (1986)).</p>
<p id="b434-6">The <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span> </em>decision, as the Court of Appeals correctly noted, does not alter the rule that the Fourth Amendment applies if a person exhibits a subjective expectation of privacy in the object of the challenged search, and that expectation is one which society is prepared to recognize as reasonable. <em>O'Conner v. Ortega, </em>480 U.S. —, —, <span class="citation multiple-matches"><a href="/c/L.Ed.%202d/90/714/">90 L.Ed. 2d 714</a></span>, 722 (1987); <em>California v. Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#211" aria-description="Citation for case: California v. Ciraolo">476 U.S. at 211</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#215" aria-description="Citation for case: California v. Ciraolo">90 L.Ed. 2d at 215</a></span>; <em>Smith v. Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U.S. 735, 740</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#226" aria-description="Citation for case: Smith v. Maryland">61 L.Ed. 2d 220, 226-27</a></span> (1979). The Fourth Amendment applies to non-residential buildings to the extent they are not exposed to the public. <em>Marshall v. Barlow’s Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#311" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U.S. 307, 311</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#310" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">56 L.Ed. 2d 305, 310</a></span> (1978); <em>United States v. Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 351-52</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#582" aria-description="Citation for case: Katz v. United States">19 L.Ed. 2d 576, 582</a></span> (1967).</p>
<p id="b434-7">Consistent with this traditional approach, the Court in <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span> </em>did not end its analysis by concluding the officers were in an open field when they made their observations; rather, it proceeded to examine the nature of the opening through which they made their observations to determine if this negated any reasonable expectation of privacy in the building’s interior. Because the barn’s interior was exposed to the public from an unprotected vantage point, the Court held that the officers’ inspection was not a Fourth Amendment violation. <em>United States v. Dunn, </em>480 U.S. at ---,<span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/#337" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d at 337</a></span>.</p>
<p id="b434-8">Applying traditional Fourth Amendment analysis to the instant case, we agree with the Court of Appeals that the trial court correctly concluded defendant had a reasonable expectation of privacy in the building which Detective Baker inspected. The building’s padlocked front door, nailed back doors, and boarded windows indicate that defendant had a subjective expectation of privacy in his building’s interior. This expectation was not unreasonable even though there were small cracks between the boards in the building’s back wall. The presence of tiny cracks near the floor on the interior wall of a second-floor porch is not the kind of exposure which serves to eliminate a reasonable expectation of privacy. To hold otherwise would result in an unfairly exacting standard. It would require owners of non-residential <page-number citation-index="1" label="391">*391</page-number>buildings who want to enjoy their Fourth Amendment rights to maintain their structures almost as airtight containers. The Supreme Court has never imposed such a standard, and we decline to do so in this case.</p>
<p id="b435-4">Nothing in the Supreme Court’s <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span> </em>decision suggests that an expectation of privacy is eliminated by quarter-inch cracks in the back wall of an otherwise sealed building. The inquiry in <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span> </em>centered on the Fourth Amendment’s requirements when law enforcement officials are faced with an open barn front obstructed only with see-through netting. The barn’s interior was fully exposed to anyone standing next to the netting. <em>United States v. Dunn, </em>480 U.S. at —, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/#338" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d at 338</a></span> (Brennan, J., dissenting). Under these circumstances the Court declared it would not require the officers to “shield their eyes” from that which was exposed to public view. <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Id.</a></span> </em>at —, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/#337" aria-description="Citation for case: United States v. Dunn">94 L.Ed. 2d at 337</a></span>.</p>
<p id="b435-5">By contrast, in the instant case, Detective Baker confronted a nearly solid wall when he entered defendant’s porch. Boarded windows and nailed doors prohibited observation of the inside from all but the most rigorous scrutiny. To make his observations, Detective Baker had to bend and peer with a flashlight through quarter-inch cracks near the floor. Nothing indicates, as in <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span>, </em>that had Detective Baker conducted his investigation during the day he could have viewed the building’s interior without making the same searching inquiry. These facts distinguish this case from <em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">Dunn</a></span> </em>in a constitutionally significant way. Far from demanding Detective Baker to avert his eyes to avoid viewing the building’s interior, the cracks near the porch floor required him to make a probing examination in order to see inside. Under these circumstances defendant’s reasonable expectation of privacy remained intact.<footnotemark>*</footnotemark></p>
<p id="b435-6">The reasonableness of defendant’s expectation of privacy was not eliminated because the building’s exterior evidenced a degree of neglect when Detective Baker made his observations. The Fourth Amendment’s application to a non-residential building’s interior is not diminished because its exterior reflects poor main<page-number citation-index="1" label="392">*392</page-number>tenance. <em>See United States v. Burnette, </em><span class="citation" data-id="390330"><a href="/opinion/390330/gilbert-mccullough-v-the-ss-coppename/#1047" aria-description="Citation for case: Gilbert McCullough v. The S/s Coppename">648 F. 2d 1038, 1047</a></span> (9th Cir. 1983). On the contrary, the Fourth Amendment applies fully so long as the interior is not exposed to the public. <em>Marshall v. Barlow’s Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#311" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U.S. at 311</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#310" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">56 L.Ed. 2d at 310</a></span>; <em>United States v. Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U.S. at 351-52</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#582" aria-description="Citation for case: Katz v. United States">19 L.Ed. 2d at 582</a></span>. Because defendant did not expose the interior of his building to the public, the Fourth Amendment applied with full force.</p>
<p id="b436-6">Our decision is consistent with those of other jurisdictions. In <em>Bradshaw v. United States, </em>the Fourth Circuit held that the defendant’s reasonable expectation of privacy in his truck’s interior was not eliminated by the presence of a crack where the back doors did not fit snugly. <span class="citation" data-id="9460223"><a href="/opinion/316481/united-states-v-william-garland-bradshaw/#1101" aria-description="Citation for case: United States v. William Garland Bradshaw">490 F. 2d 1097, 1101</a></span> (4th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./419/895/">419 U.S. 895</a></span>, <span class="citation" data-id="8992691"><a href="/opinion/9000177/zane-v-united-states/" aria-description="Citation for case: Zane v. United States">42 L.Ed. 2d 139</a></span> (1974). The court concluded that police officers violated the Fourth Amendment when they looked through the crack without a warrant, saw moonshine whiskey jugs, and seized them. The court acknowledged that the officers had a right to approach and stand next to the truck, but it concluded they went beyond lawful investigation when peering through the small space. <em><span class="citation" data-id="8992691"><a href="/opinion/9000177/zane-v-united-states/" aria-description="Citation for case: Zane v. United States">Id.</a></span> </em>In <em>State v. Kaaheena, </em>the Hawaii Supreme Court concluded the defendant’s Fourth Amendment rights were violated when the police stood on a crate and looked through a one-inch hole in the drapes and blinds of a building which housed a “commercial establishment and some rental apartments.” <span class="citation" data-id="1206533"><a href="/opinion/1206533/state-v-kaaheena/#466" aria-description="Citation for case: State v. Kaaheena">575 P. 2d 462, 466</a></span> (1978). Although the police made their observations from a public vantage point, the court held that the search was impermissible because the defendant maintained his reasonable expectation of privacy in the building’s interior. <span class="citation" data-id="1206533"><a href="/opinion/1206533/state-v-kaaheena/#467" aria-description="Citation for case: State v. Kaaheena"><em>Id. </em>at 467</a></span>; <em>see also Kroehler v. Scott, </em><span class="citation" data-id="1494964"><a href="/opinion/1494964/kroehler-v-scott/" aria-description="Citation for case: Kroehler v. Scott">391 F. Supp. 1114</a></span> (E.D. Pa. 1975) (violation of Fourth Amendment for officers to peer through small ceiling vents); <em>Lorenzana v. Superior Court of Los Angeles County, </em><span class="citation" data-id="1183387"><a href="/opinion/1183387/lorenzana-v-superior-court/" aria-description="Citation for case: Lorenzana v. Superior Court">9 Cal. 3d 626</a></span>, <span class="citation" data-id="1183387"><a href="/opinion/1183387/lorenzana-v-superior-court/" aria-description="Citation for case: Lorenzana v. Superior Court">511 P. 2d 33</a></span>, <span class="citation" data-id="1183387"><a href="/opinion/1183387/lorenzana-v-superior-court/" aria-description="Citation for case: Lorenzana v. Superior Court">108 Cal. Rptr. 585</a></span> (1973) (officers violated Fourth Amendment by peering through drawn curtains); <em>People v. Triggs, </em><span class="citation" data-id="1354211"><a href="/opinion/1354211/people-v-triggs/" aria-description="Citation for case: People v. Triggs">8 Cal. 3d 884</a></span>, <span class="citation" data-id="1354211"><a href="/opinion/1354211/people-v-triggs/" aria-description="Citation for case: People v. Triggs">506 P. 2d 232</a></span>, <span class="citation" data-id="1354211"><a href="/opinion/1354211/people-v-triggs/" aria-description="Citation for case: People v. Triggs">106 Cal. Rptr. 408</a></span> (1973) (illegal search where officers in maintenance access area peered through vents); <em>People v. Lovelace, </em><span class="citation" data-id="2149587"><a href="/opinion/2149587/people-v-lovelace/" aria-description="Citation for case: People v. Lovelace">172 Cal. Rptr. 65</a></span>, <span class="citation" data-id="2149587"><a href="/opinion/2149587/people-v-lovelace/" aria-description="Citation for case: People v. Lovelace">116 Cal. App. 3d 541</a></span> (1981) (reasonable expectation of privacy not eliminated by knotholes and cracks in six foot high wooden fence); <em>State v. Biggar, </em><span class="citation" data-id="1169275"><a href="/opinion/1169275/state-v-biggar/" aria-description="Citation for case: State v. Biggar">716 P. 2d 493</a></span> (1986) (reasonable expectation of privacy not eliminated by crack one-half to one inch wide where toilet stall door did not close properly).</p>
<p id="b437-5"><page-number citation-index="1" label="393">*393</page-number>In conclusion, we agree with the Court of Appeals that the decision by the Supreme Court in <em>United States v. Dunn </em>does not require a reversal of the trial court’s decision to grant defendant’s motion to suppress evidence taken from his building. Both the trial court and the Court of Appeals reached the right result on the search issue for the right reasons. The decision below, therefore, is</p>
<p id="b437-6">Affirmed.</p>
<footnote label="*">
<p id="b435-7"> Defendant argues that it was unlawful for Detective Baker to enter the porch without a warrant. We decline to assess this contention’s merit. Assuming, <em>arguendo, </em>that Detective Baker rightfully entered the porch, his subsequent action of peering into the building’s interior was an impermissible warrantless search.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/State v. Volle.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "State v. Volle"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: Kansas Supreme Court
court_level: state
circuit: ""
year: 2025
date_decided: 2025-12-12
docket: ""
authority_weight: "Persuasive — state, illustrative"
treatment:
  field_i_validity: good_law
  as_of_content: 2025-12-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: State v. Volle
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10811858/state-v-volle/"
  cluster_id: 10811858
  opinion_id: 11278610
  identity_checked: false
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Recent development (role-based)"
related: ["[[Riley v. California]]", "[[Carpenter v. United States]]", "[[State v. Mansor]]"]
aliases: []
tags: ["case", "fourth-amendment", "digital-search", "computer-warrant", "particularity", "kansas"]
holding: "Because relevant information may be stored anywhere on a digital device, a warrant ordinarily cannot prescribe in advance exactly how…"
lake:
  record_id: State v. Volle
  status: under_review
  projected_at: 2026-07-06
---

# State v. Volle

*580 P.3d 1223 (Kan. 2025)* · Kansas Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In a first-degree murder investigation, police obtained a warrant to search Volle's cell phone. The warrant authorized creating a complete forensic image of the phone but limited the seizure to data related to the murder or identifying the phone's owner. Volle argued the warrant was unconstitutionally overbroad as to digital evidence.

## Issue
How the Fourth Amendment's [[Particularity|particularity]] requirement applies to a warrant to search a digital device—specifically, whether the warrant must prescribe the search method and how it must limit what may be seized.

## Rule
A digital warrant need not dictate the search method, but must limit the seizure. "Because relevant information may be stored anywhere on such a device, it is ordinarily impractical—and sometimes impossible—for a warrant to prescribe in advance how officers must locate that data." — 580 P.3d 1223 (Kan. 2025) (slip op., at 13). ^pin-13

As to what may be seized, "even though investigators may need to review broad portions of a device's contents to locate relevant material, the warrant must still include a meaningful limiting principle tying the authorized seizure to evidence of a specified offense." — *Id.* ^pin-13a

## Application
The warrant satisfied both aspects of [[Particularity|particularity]]: it authorized a full forensic image of the phone—a breadth recognized as practically necessary for digital searches—while expressly limiting the authorized seizure to data related to first-degree murder or identifying the phone's owner. That limiting principle kept the search anchored to the probable-cause showing and prevented the kind of exploratory rummaging the Fourth Amendment forbids, so Volle's overbreadth challenge failed.

## Conclusion
The digital warrant was sufficiently particular; the district court properly rejected Volle's overbreadth claim.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Persuasive — state, illustrative**.
- A recent state development on digital-warrant [[Particularity|particularity]], coherent with the digital-privacy concerns of [[Riley v. California]] and [[Carpenter v. United States]] and the search-scope analysis of [[State v. Mansor]].

## Appears on
- [[Plain View Doctrine]] — *Recent development (role-based)*

## Sources
- *State v. Volle*, 580 P.3d 1223 (Kan. 2025) — https://www.courtlistener.com/opinion/10811858/state-v-volle/ (lead opinion id 11278610) — pinpoint: slip op. 13.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2fb1494b255a5a3d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-13", "record_id": "State v. Volle"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-13", "pinpoint_status": "slip-only", "quote": "--- # State v. Volle *580 P.3d 1223 (Kan. 2025)* · Kansas Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In a first-degree murder investigation, police obtained a warrant to search Volle's cell phone. The warrant authorized creating a complete forensic image of the phone but limited the seizure to data related to the murder or identifying the phone's owner. Volle argued the warrant was unconstitutionally overbroad as to digital evidence. ## Issue How the Fourth Amendment's particularity requirement applies to a warrant to search a digital device—specifically, whether the warrant must prescribe the search method and how it must limit what may be seized. ## Rule A digital warrant need not dictate the search method, but must limit the seizure.", "quote_fidelity": "mismatch", "record_id": "State v. Volle", "star_marker": null}}
{"assertion_id": "cc967dcfc2f36e5e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-13a", "record_id": "State v. Volle"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-13a", "pinpoint_status": "slip-only", "quote": "even though investigators may need to review broad portions of a device's contents to locate relevant material, the warrant must still include a meaningful limiting principle tying the authorized seizure to evidence of a specified offense.", "quote_fidelity": "mismatch", "record_id": "State v. Volle", "star_marker": null}}
{"assertion_id": "b3b8293a3796dfd2", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Volle"}, "payload": {"as_of_content": "2025-12-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "State v. Volle", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — State v. Volle

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Volle",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "State v. Volle",
    "case_name_short": "Volle",
    "case_name_full": "",
    "input_case_name": "State v. Volle",
    "court": "Kansas Supreme Court",
    "court_id": "kan",
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "2025-12-12",
    "year": 2025,
    "docket": null,
    "cluster_id": 10811858,
    "lead_opinion_id": 11278610,
    "sibling_ids": [
      11278610
    ],
    "absolute_url": "/opinion/10811858/state-v-volle/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
    }
  },
  "pinpoints": [
    {
      "id": "pin-13",
      "page": null,
      "quote": "--- # State v. Volle *580 P.3d 1223 (Kan. 2025)* \u00b7 Kansas Supreme Court \u00b7 **Persuasive \u2014 state, illustrative** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In a first-degree murder investigation, police obtained a warrant to search Volle's cell phone. The warrant authorized creating a complete forensic image of the phone but limited the seizure to data related to the murder or identifying the phone's owner. Volle argued the warrant was unconstitutionally overbroad as to digital evidence. ## Issue How the Fourth Amendment's particularity requirement applies to a warrant to search a digital device\u2014specifically, whether the warrant must prescribe the search method and how it must limit what may be seized. ## Rule A digital warrant need not dictate the search method, but must limit the seizure.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-13a",
      "page": null,
      "quote": "even though investigators may need to review broad portions of a device's contents to locate relevant material, the warrant must still include a meaningful limiting principle tying the authorized seizure to evidence of a specified offense.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2025-12-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "State v. Volle",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11278610) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR kan OR kanctapp)",
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
        "query": "cites:(11278610)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11278610)",
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
    "complete_query": "cites:(11278610)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11278610,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/state-v-volle.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11278610,
        "cited_id": 157595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 165743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 172511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 505922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1163616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1199913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1284639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1288294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1369871,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1379565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 2331603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 2517832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 2542699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 2606277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 3196866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4022220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4266071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4348417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4471470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4526564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4680503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4680504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4680507,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4684947,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4707986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 5139220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 5288625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 6346777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 6348805,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 6350811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7619597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7923237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7923547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7924104,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7924656,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9427638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9429558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9434728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9435413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9762923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9795487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9796947,
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
    "date_created": "2026-07-05T20:34:10Z",
    "date_modified": "2026-07-06T13:38:39Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "official cite selection failed closed: no_official_class_citation",
      "legacy treatment migrated: good -> good_law",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:35:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:35:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T13:38:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:35:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — State v. Volle

```
              IN THE SUPREME COURT OF THE STATE OF KANSAS

                                       No. 127,745

                                    STATE OF KANSAS,
                                        Appellee,

                                             v.

                                      JEREMY VOLLE,
                                         Appellant.


                              SYLLABUS BY THE COURT

1.
       The Fourth Amendment to the United States Constitution requires that "no
Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and
particularly describing the place to be searched, and the persons or things to be seized."
The scope of section 15 of the Kansas Constitution Bill of Rights is identical to that of
the Fourth Amendment to the United States Constitution.


2.
       A warrant satisfies the constitutional standard when it describes the evidence to be
searched with sufficient particularity to permit the executing officer to locate the same
from the face of the warrant. The standard, however, does not demand absolute precision;
it requires only that the warrant describe the property with as much specificity as the
government's knowledge and circumstances allow. The degree of specificity required
depends on the nature of the property and the facts known to officers at the time the
warrant issued.




                                             1
3.
          Separate from the method of search, the Fourth Amendment requires that a
warrant specify with particularity the type of evidence to be seized, and a valid warrant
must include a limiting principle that confines the authorized seizure to evidence of the
offense under investigation.


4.
          Courts evaluate electronic-device warrants under the same practical standard
applied to physical searches, asking only whether the description of items to be seized is
as particular as the circumstances reasonably allow. So long as the warrant contains a
clear limiting principle it is sufficiently particular.


5.
          Neither the Fourth Amendment nor section 15 of the Kansas Constitution Bill of
Rights mandate exclusion of unlawfully obtained evidence; the exclusionary rule is a
judicial deterrent, applied only when suppression would meaningfully deter police
misconduct.


6.
          Evidence is admissible under the inevitable discovery doctrine if the State proves
by a preponderance of the evidence that it would have been lawfully discovered absent
the unconstitutional conduct.


7.
          An inmate has no reasonable expectation of privacy in nonlegal outgoing mail that
is subject to inspection based on legitimate security or investigative purposes under jail
policy.


                                                2
8.
        An aiding-and-abetting instruction is proper when the evidence permits a
reasonable conclusion that the defendant knowingly and intentionally participated in a
criminal venture; mere presence or association is insufficient to establish accomplice
liability.


9.
        Cumulative trial errors, when considered together, may require reversal of the
defendant's convictions when the totality of the circumstances establish that the defendant
was substantially prejudiced by the errors and denied a fair trial.


10.
        A felony-murder conviction predicated on criminal discharge of a firearm at an
occupied motor vehicle is supported when the evidence shows a reckless discharge at an
occupied vehicle, even if the shooter's intent was directed at a person rather than the
vehicle itself.


11.
        Felony murder and reckless second-degree murder are distinct offenses under
K.S.A. 21-5109(d), and when both are found in the alternative, the convictions merge and
sentencing on the greater offense—felony murder—is proper.


        Appeal from Shawnee District Court; CHERYL RIOS, judge. Oral argument held September 9,
2025. Opinion filed December 12, 2025. Affirmed.


        Peter T. Maharry, of Kansas Appellate Defender Office, argued the cause and was on the briefs
for appellant.




                                                   3
        Carolyn A. Smith, assistant deputy district attorney, argued the cause, and Mike Kagay, district
attorney, and Kris W. Kobach, attorney general, were with her on the brief for appellee.


The opinion of the court was delivered by


        STANDRIDGE, J.: This is Jeremy Francis Volle's direct appeal following his
convictions for first-degree felony murder and criminal possession of a weapon. Volle
raises multiple claims of trial and sentencing error, including two evidentiary issues and
challenges to a jury instruction, sufficiency of the evidence, and sentencing. He also
argues cumulative error.


        For the reasons below, we affirm Volle's convictions and sentence. The district
court did not err in denying either of Volle's motions to suppress evidence or in
instructing the jury. In the absence of any error, Volle's cumulative error argument also
fails. Finally, the State presented sufficient evidence to support Volle's felony-murder
conviction, and the district court properly sentenced him for this crime.


                                                 FACTS


        In the early morning hours of May 27, 2021, Aaron Shepherd and his wife,
Megan, were driving around Topeka collecting scrap metal from dumpsters. While
Shepherd drove down the 1100 block of 17th Street, Megan slept in the front passenger
seat of their Ford Taurus. She woke up when Shepherd braked suddenly and she saw an
SUV speeding past. Shepherd told Megan that someone was chasing and shooting at
them, and he asked her to call 911. While Megan looked for her phone, Shepherd grabbed
Megan's BB gun, exited the car, and crouched near the open driver's side door as the
SUV drove by again. After the SUV passed, Shepherd tossed the BB gun back into the
car but remained outside, raising his arms and yelling. The SUV turned off 17th Street

                                                    4
and stopped. At this point, Megan saw a red laser beam hit Shepherd, heard a single
gunshot, and watched Shepherd fall to the ground. Shepherd was critically wounded and
later died at the hospital.


       Based on witness accounts of the shooting and video evidence collected from the
surrounding area, law enforcement identified a Chevy Trailblazer owned by Brandon
Croskey as the vehicle from which the gunshot was fired. Topeka Police Detective Jared
Strathman interviewed Croskey, who ultimately admitted involvement and identified
Volle as the shooter.


       The State charged Volle with criminal possession of a weapon and alternative
counts of first-degree felony murder and first-degree premeditated murder. To support the
felony-murder charge, the State alleged Volle killed Shepherd while committing the
inherently dangerous felony of criminal discharge of a firearm at an occupied motor
vehicle.


       The case proceeded to trial, where the jury heard conflicting testimony from
Croskey and Volle, with each implicating the other in the shooting.


       Croskey testified at trial, having previously pled guilty to reckless second-degree
murder and criminal discharge of a firearm at an occupied motor vehicle. As part of his
plea agreement, he agreed to provide truthful testimony for the State. Croskey testified
that around 4:30 a.m. on May 27, 2021, he was at a car wash at 21st and Wanamaker in
his Chevy Trailblazer, where he encountered Shepherd—a man he did not know—and
the two exchanged words. Croskey said he became upset and wanted to fight after
Shepherd called him a racial slur. Croskey left the car wash and called Volle to be his
backup in case Shepherd had a knife or gun.


                                              5
       Croskey went to Volle's house near 17th and Buchanan, and Volle eventually
came outside and got into the front passenger seat of the Trailblazer. Croskey started
driving and turned onto 17th Street, where he saw Shepherd's car and tried to cut him off.
After Shepherd drove around him, Croskey did a U-turn and caught up to Shepherd,
following close behind and then passing him when Shepherd slammed on his brakes.
Croskey did another U-turn and drove toward Shepherd's car. Croskey watched Shepherd
crouch between the open driver's side door and the car, holding what appeared to be a
firearm out the window. Croskey ducked down and then noticed Volle pulling a gun out
of his shorts pocket. Croskey testified he was shocked because he told Volle not to bring
a gun. Volle told Croskey to turn off 17th Street and stop so that he could take aim at
Shepherd. After Croskey did so, Volle leaned out of the passenger window, aimed the
laser on his gun at Shepherd, and fired one shot. Croskey then drove back to Volle's
house, where both men went inside and Croskey stayed for a few hours. Volle told
Croskey that he fired the shot because he wanted to see if the beam on his gun was
accurate. Volle also told Croskey not to contact the police and said that he should get rid
of his truck. Croskey later spray painted his Trailblazer blue but continued to drive it after
the shooting. When Croskey was interviewed by Detective Strathman, he did not
immediately identify Volle as the shooter because he was scared of Volle and feared what
Volle might do.


       Volle testified in his defense. He said he did not know Shepherd and denied
shooting him. Volle said Croskey arrived at his house upset about something, but he did
not know why Croskey wanted to meet up. Volle claimed he did not take a gun with him
when he got into Croskey's Trailblazer. He testified Croskey drove to 17th Street, tried to
cut off Shepherd's car, and then began following Shepherd. As they passed Shepherd's
car, Volle saw Shepherd pointing a gun at them but did not know it was a BB gun. After
Volle saw the gun, he was scared and told Croskey to take him home. Instead, Croskey
turned around and drove back toward Shepherd's car. Volle noticed Croskey had a gun in
                                              6
his hand as he drove by Shepherd, so Volle lay back in his seat. After turning off 17th
Street and coming to a stop, Croskey leaned over Volle and fired a single shot through
the passenger window. As Croskey drove away, Volle took the gun from the cup holder
and put it in his pocket because he recognized the gun as belonging to him. Volle did not
know that Croskey had the gun or how he had come to possess it. Volle assumed that the
mother of his children, who was friends with Croskey, loaned Croskey the gun.


       Volle said that when they went back to his house, they listened to the police
scanner for information about the shooting and later saw a news article confirming
Shepherd's death. Volle believed that Croskey was defending himself, because Croskey
told him that Shepherd had used a racial slur at the car wash and that Shepherd chased
Croskey with a gun. Volle did not want to cooperate with law enforcement because he
did not want to snitch on Croskey. Volle denied ever threatening Croskey after the
shooting or discouraging him from talking to the police. Volle claimed he told Croskey to
leave him out of it if he did talk to the police because he had nothing to do with the
shooting. According to Volle, Croskey did not seem afraid of him. Volle admitted that
videos from his phone after the shooting showed him wiping the gun for fingerprints and
talking to Croskey about looking for the shell casing and selling the gun or taking it "out
of commission." And Volle admitted that the videos captured him telling Croskey not to
leave in the morning before they could talk. Volle also said, "I think we're good," "I don't
think nobody saw the car," and, "Don't tell nobody, bro."


       A jury convicted Volle of first-degree felony murder, the alternative lesser
included offense of reckless second-degree murder, and criminal possession of a firearm.


       Before sentencing, Volle moved the district court to impose a sentence for reckless
second-degree murder because it was a more specific crime and therefore should control
his sentence under K.S.A. 21-5109(d). At sentencing, the court denied the motion,
                                             7
merged the murder convictions into a single conviction for felony murder, and imposed a
controlling sentence of life without the possibility of parole for 620 months.


        Volle directly appealed his convictions to this court. Jurisdiction is proper. See
K.S.A. 60-2101(b) (Supreme Court jurisdiction over direct appeals governed by K.S.A.
22-3601); K.S.A. 22-3601(b)(3)-(4) (life sentence and off-grid crime cases permitted to
be directly taken to Supreme Court); K.S.A. 21-5402(b) (first-degree murder is off-grid
person felony).


                                          ANALYSIS

        On appeal, Volle argues: (1) the district court erred in denying his motions to
suppress evidence, (2) the district court erred in instructing the jury on aiding and
abetting, (3) the cumulative effect of these errors deprived him of his constitutional right
to a fair trial, (4) the evidence was insufficient to support his conviction for first-degree
felony murder, and (5) the district court erred in sentencing Volle for his felony-murder
conviction rather than for reckless second-degree murder. We address each of Volle's
arguments in turn.


I. Motions to suppress

        Volle argues the district court erred when ruling on two motions to suppress
evidence: one regarding evidence law enforcement obtained from a search of his cell
phone and one regarding letters he wrote while in pretrial custody at the Shawnee County
Jail.


        When, as here, the material facts supporting a district court's decision on a motion
to suppress evidence are undisputed, suppression is a question of law subject to unlimited
appellate review. State v. Hanke, 307 Kan. 823, 827, 415 P.3d 966 (2018).
                                               8
       The Fourth Amendment to the United States Constitution and section 15 of the
Kansas Constitution Bill of Rights protect all persons against unreasonable searches and
seizures. State v. Baker, 306 Kan. 585, 589-90, 395 P.3d 422 (2017) (The Fourth
Amendment applies to the states through the Fourteenth Amendment.); State v. Daniel,
291 Kan. 490, 498, 242 P.3d 1186 (2010) (interpreting section 15 to provide the same
protections as the Fourth Amendment). The State bears the burden of proving the
lawfulness of a search and seizure. State v. Hillard, 315 Kan. 732, 747, 511 P.3d 883
(2022).


   A. Motion to suppress cell phone evidence


       After Croskey identified Volle as the shooter, law enforcement obtained a search
warrant for Volle's residence. When officers executed the search warrant, they found
Volle at the home and arrested him. At the time of his arrest, Volle had a black Samsung
cellular phone in his pocket. Law enforcement seized the phone and sought a separate
search warrant for it.


       In the affidavit in support of the search warrant for the phone, Detective Strathman
recounted the general investigation into the case and stated: "I am asking for a search
warrant for the phones as during my interview with [Croskey], he stated [Volle] had been
contacting him since the homicide occurred. Furthermore I know cellular devices are
capable of tracking movements through GPS if the location data is turned on." A district
court judge granted the State's application for a search warrant authorizing the following
search of Volle's cell phone:


       "Any and all electronically stored information, including but not limited to Call Logs,
       Text Messages, Multimedia Messaging, Pictures/videos, Messages, Information from

                                                   9
       Third Party Apps, Contacts Lists, device locations and any other form of electronically
       stored information associated with either crimes listed herein or identifying information
       to determine ownership of the searched devices.

       "Which items are contraband or are fruits, instrumentalities or evidence of K.S.A. 21-
       5402 Murder in the 1st Degree, are located in or upon:

       "Black Samsung cell phone IMEI 353327111435079 seized from Jeremy Volle."


       Before trial, Volle moved to suppress the cell phone evidence alleging the
affidavit lacked probable cause and contained factual misrepresentations, and the search
warrant was overbroad. As a result, Volle claimed the exclusionary rule applied and
required suppression of the evidence.


       After considering written and oral argument by the parties, the district court
denied Volle's motion to suppress. Although the district court agreed with Volle that the
affidavit failed to establish probable cause, it ultimately denied Volle's motion to
suppress after finding that the good-faith exception and, alternatively, the inevitable
discovery doctrine rendered the cell phone evidence admissible. The court also
determined that the warrant was not overbroad, contained no factual misrepresentations,
and was executed reasonably. Over Volle's objection at trial, the State introduced
evidence obtained from the search of Volle's cell phone.


       On appeal, Volle argues (1) the search warrant was overbroad, (2) the good-faith
exception does not apply because the affidavit contained factual misrepresentations, and
(3) the inevitable discovery doctrine is inapplicable because the evidence would not have
been discovered by lawful means absent the unconstitutional conduct.


       The State defends the district court's findings that the warrant was not overbroad,
that the affidavit contained no factual misrepresentations, and that the good-faith and
                                                   10
inevitable-discovery exceptions rendered the evidence admissible. The State further
asserts—without having filed a cross-appeal—that this court may nonetheless affirm the
district court's ruling as right for the wrong reason because, in its view, the affidavit itself
established sufficient probable cause to support the search.


       Before reaching the merits of the suppression issues, we must first determine
whether the State's probable-cause argument is properly before us. Kansas law requires
an appellee to cross-appeal a district court's adverse decisions before those rulings may
be challenged on appeal. Cooke v. Gillespie, 285 Kan. 748, 755, 176 P.3d 144 (2008); see
K.S.A. 60-2103(h) (cross-appeal required when "appellee desires to have a review of
rulings and decisions of which such appellee complains"). The State acknowledges that it
did not file a cross-appeal but contends that a cross-appeal was unnecessary because the
district court's finding of no probable cause was not an adverse ruling.


       The State's argument fails for two reasons. First, the governing statute does not
limit the cross-appeal requirement to "adverse" rulings. K.S.A. 2024 Supp. 60-2103(h)
provides that an appellee who seeks review of "rulings and decisions of which such
appellee complains" must file a notice of cross-appeal within 21 days after the notice of
appeal is filed. The statute's plain language encompasses any ruling the appellee seeks to
challenge, regardless of whether it altered the outcome of the judgment.


       Second, even if an "adverse" component were required, the district court's
determination that the warrant affidavit lacked probable cause was plainly adverse to the
State's position, even though the court ultimately denied the motion to suppress on other
grounds. See Merriam-Webster Online Dictionary (defining "adverse" as "opposed to
one's interests" or "unfavorable").




                                               11
       The State's failure to pursue a cross-appeal prevents us from reviewing the district
court's probable cause determination. See State v. Novotny, 297 Kan. 1174, 1181, 307
P.3d 1278 (2013) (holding appellee abandoned alternative grounds for affirming district
court's ultimately favorable suppression ruling when it failed to cross-appeal court's
adverse ruling on the alternative grounds). Accordingly, we decline to consider the State's
probable-cause argument.


          1. Suppression based on overbreadth


       Volle contends the district court should have suppressed evidence obtained from
his cell phone because the search warrant lacked the particularity required by the Fourth
Amendment. He argues the warrant was so sweeping that it allowed officers to search
"everything and anything" on his phone, leaving no meaningful limits on its scope.


       The Fourth Amendment to the United States Constitution requires that "no
Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and
particularly describing the place to be searched, and the persons or things to be seized."
"'The scope of Section 15 of the Kansas Constitution Bill of Rights is identical to that of
the Fourth Amendment to the United States Constitution.'" State v. Patterson, 304 Kan.
272, 275, 371 P.3d 893 (2016) (citing State v. LeFort, 248 Kan. 332, 334, 806 P.2d 986
[1991]; K.S.A. 2015 Supp. 22-2502[a] [authorizing the issuance of search warrants
"'which particularly describes a person, place or means of conveyance to be searched and
things to be seized'"]). A warrant satisfies the constitutional standard when it describes
the evidence to be searched "'with sufficient particularity to permit the executing officer
to locate the same from the face of the warrant.'" Patterson, 304 Kan. at 275 (citing
LeFort, 248 Kan. at 334-35).




                                             12
       The Fourth Amendment, however, does not demand absolute precision; it requires
only that the warrant describe the property "'with as much specificity as the government's
knowledge and circumstances allow.'" United States v. Riccardi, 405 F.3d 852, 862-63
(10th Cir. 2005) (citing United States v. Leary, 846 F.2d 592, 600 [10th Cir. 1988]). The
degree of specificity required depends on the nature of the property and the facts known
to officers at the time the warrant issued. 405 F.3d at 862. Kansas courts apply a
comparable standard, holding that "the test to prevent general searches is one of practical
accuracy rather than one of technical sufficiency, and absolute precision in the search
warrant is not required in identifying the property to be seized." State v. LeFort, 248 Kan.
332, 334-37, 806 P.2d 986 (1991); see also State v. Ames, 222 Kan. 88, 92, 563 P.2d
1034 (1977). Thus, so long as the warrant describes the evidence to be seized with as
much particularity as the circumstances reasonably allow, it satisfies both the Fourth
Amendment and Kansas constitutional standards.


       Although courts recognize that electronic devices pose unique challenges under
the Fourth Amendment's particularity requirement, they treat those challenges as part of
the circumstances that determine how particular a warrant need reasonably be. See, e.g.,
United States v. Burgess, 576 F.3d 1078, 1094 (10th Cir. 2009). Burgess explains that the
particularity requirement does not demand a warrant to specify the precise folders, file
paths, or search techniques officers must use when examining a digital device. Because
relevant information may be stored anywhere on such a device, it is ordinarily
impractical—and sometimes impossible—for a warrant to prescribe in advance how
officers must locate that data. 576 F.3d at 1094.


       But Burgess addresses only the method of executing a digital search; it does not
resolve the separate question of what evidence officers may seize. The Fourth
Amendment imposes a distinct requirement that the warrant describe with particularity
the type of evidence it authorizes officers to seize. Thus, even though investigators may
                                             13
need to review broad portions of a device's contents to locate relevant material, the
warrant must still include a meaningful limiting principle tying the authorized seizure to
evidence of a specified offense. See United States v. Palms, 21 F.4th 689, 698-99 (10th
Cir. 2021).


       Here, the warrant satisfied both aspects of the particularity requirement. It
permitted investigators to create a complete forensic image of the phone—a breadth that
Burgess recognizes as practically necessary—and it expressly limited the authorized
seizure to electronic data related to first-degree murder or identifying the phone's owner.
This limiting principle kept the search anchored to the probable-cause showing and
prevented the kind of exploratory rummaging the Fourth Amendment forbids.
Accordingly, the district court properly rejected Volle's overbreadth claim.


           2. Suppression based on inapplicability of the good-faith exception and the
              inevitable discovery doctrine

       Volle also claims the absence of probable cause barred admission of the cell phone
evidence and that neither the good-faith exception nor the inevitable discovery doctrine
justified its use. Before turning to the specific exceptions at issue, it helps to review the
principles governing the exclusionary rule and its role in enforcing Fourth Amendment
protections.


       Notably, neither the Fourth Amendment nor section 15 of the Kansas Constitution
Bill of Rights expressly prohibits evidence obtained in violation of their respective
protections. Rather, a judicially created remedy—the exclusionary rule—exists "to
prevent the use of unconstitutionally obtained evidence in a criminal proceeding against
the victim of the illegal search." Daniel, 291 Kan. at 496. This exclusionary rule protects
Fourth Amendment rights through deterrence and only applies when the rule's deterrent
effect will be achieved. Herring v. United States, 555 U.S. 135, 137, 129 S. Ct. 695, 172
                                              14
L. Ed. 2d 496 (2009) ("[S]uppression is not an automatic consequence of a Fourth
Amendment violation. Instead, the question turns on the culpability of the police and the
potential of exclusion to deter wrongful police conduct."); Daniel, 291 Kan. at 496
("'[A]pplication of the exclusionary rule properly has been restricted to those situations in
which its remedial purpose is effectively advanced.'"). Therefore, when considering
whether suppression is proper under the specific circumstances of each case, courts must
balance the deterrent effect of suppressing evidence against societal harms. Herring, 555
U.S. at 141.


       There are exceptions to the exclusionary rule which allow for the admission of
evidence that was obtained in violation of the Fourth Amendment. Relevant here, the
district court held the cell phone evidence was admissible under the good-faith exception
and the inevitable discovery doctrine. See Daniel, 291 Kan. at 497-500 (good-faith
exception); Baker, 306 Kan. at 591 (inevitable discovery doctrine). Volle challenges the
district court's conclusion that these exceptions applied. The question of whether an
exception to the exclusionary rule applies is a question of law, reviewed by this court
independently and without any required deference to the district court. See State v.
Hoeck, 284 Kan. 441, 447, 163 P.3d 252 (2007).


               i. Good-faith exception


       The United States Supreme Court first recognized the good-faith exception in
United States v. Leon, 468 U.S. 897, 920-25, 104 S. Ct. 3405, 82 L. Ed. 2d 677 (1984).
Under this exception, the Fourth Amendment exclusionary rule should not be applied to
bar evidence obtained by officers acting in reasonable reliance on a search warrant issued
by a detached and neutral magistrate but ultimately found to be invalid except where:




                                             15
       "'(1) the magistrate issuing the warrant was deliberately misled by false information; (2)
       the magistrate wholly abandoned his or her detached or neutral role; (3) there was so little
       indicia of probable cause contained in the affidavit that it was entirely unreasonable for
       the officers to believe the warrant was valid; or (4) the warrant so lacked specificity that
       officers could not determine the place to be searched or the items to be seized.'" State v.
       Hubbard, 309 Kan. 22, 33, 430 P.3d 956 (2018).


These circumstances should not occur often; the threshold to avoid application of the
Leon good-faith exception is high. State v. Zwickl, 306 Kan. 286, 295, 393 P.3d 621
(2017). Good faith is measured by an objective standard—how a reasonable law
enforcement officer would view the circumstances. Leon, 468 U.S. at 919-20.


       Because the State bears the burden of proving that the challenged police conduct
was permissible, the State must prove facts warranting application of the good-faith
exception. See Leon, 468 U.S. at 924; State v. Cleverly, 305 Kan. 598, 605, 385 P.3d 512
(2016). To satisfy its burden here, the State asserts that the warrant was not obviously
deficient and contends that law enforcement exhibited good faith in their investigative
efforts and in no way deliberately misled the judge who issued the warrant.


       Volle takes issue with the State's position, arguing the good-faith exception does
not apply because Detective Strathman deliberately misled the issuing judge by omitting
material information from the search warrant affidavit. As this court has recognized, a
deliberate omission may be equivalent to an affirmative misstatement if it misleads the
magistrate. State v. Probst, 247 Kan. 196, 206, 795 P.2d 393 (1990). A person attacking
an affidavit on the basis that it omitted information must prove that the omission was
both deliberate and material. State v. Colbert, 257 Kan. 896, 905, 896 P.2d 1089 (1995).
Thus, Volle must establish that inclusion of these omitted facts would have had some
bearing on the issuing judge's probable cause determination. See State v. Adams, 294
Kan. 171, 179, 273 P.3d 718 (2012); State v. Lockett, 232 Kan. 317, 320, 654 P.2d 433
                                                    16
(1982) (materiality determined by inquiring whether issuing judge would have found
probable cause if omitted material had been included).


       In support of his argument, Volle focuses on Detective Strathman's statement in
the affidavit that he was seeking a search warrant for Volle's phone because Croskey
stated during his interview that Volle had been contacting him since the shooting. He
contends this statement, which suggested there would be communication such as texts
between Volle and Croskey on Volle's phone, was misleading because Detective
Strathman omitted the following material information from the affidavit:


   • Croskey only gradually revealed more information during the interview and gave
       it in "varying shades of honesty."


   • When asked directly whether he shared text messages with Volle about the
       shooting, Croskey said "'I don't know, I don't think so.'"


   • When asked whether he sent anybody any text messages about the shooting,
       Croskey said, "'Huh-uh,'" and shook his head no.


Volle asserts that Detective Strathman's failure to include this information in the affidavit
constitutes a deliberate and material omission because including it would have led the
issuing judge to realize that no communication between Volle and Croskey would be
found on Volle's cell phone and thus deny the application for the warrant.


       But the record fails to support Volle's claim that Detective Strathman deliberately
withheld material information from the search warrant affidavit that would have had
some bearing on the issuing judge's probable cause determination. In the affidavit,
Detective Strathman recounted Croskey's statement that Volle had been contacting
                                             17
Croskey since the shooting. Notably, the information provided by Detective Strathman in
the affidavit was true regardless of whether Croskey and Volle exchanged text
messages—during Croskey's interview, he told Detective Strathman that Volle had tried
to contact him on his cell phone after the shooting and that he had Volle's number saved
in his phone. And despite Volle's suggestion otherwise, Croskey did not definitively deny
that he and Volle had exchanged text messages about the shooting. While Croskey
appeared relatively certain that he had not sent anyone else text messages about the
shooting, he could not say for sure whether he and Volle had texted about it.


       Moreover, it is unclear how any information about Croskey's honesty would have
impacted the court's decision to issue the warrant. If anything, these details, coupled with
Croskey's equivocation, could have reinforced an inference that Volle's phone contained
relevant communications. Thus, Detective Strathman's declaration in the search warrant
affidavit recounting Croskey's statement that Volle had been contacting him since the
shooting was not inaccurate or misleading, and the omitted information does not make it
so.


       In sum, there is no evidence to support Volle's claim that Detective Strathman's
omission was either deliberate or material such that it undermines the affidavit's
reliability. The warrant was not obviously deficient, and law enforcement acted in
objectively reasonable reliance on it. Because there was no misconduct to deter, the
good-faith exception applies. See Herring, 555 U.S. at 137 (purpose of the exclusionary
rule is to deter police misconduct). The district court did not err in finding that the good-
faith exception rendered the cell-phone evidence admissible.




                                              18
              ii. Inevitable discovery doctrine


       The inevitable discovery doctrine allows for the admission of unconstitutionally
obtained evidence if the evidence would have been discovered by lawful means absent
the unconstitutional conduct. Baker, 306 Kan. at 591 (explaining that "'punishment for an
act that does no harm is not required in order to deter harmful acts'"). The State must
establish inevitability by a preponderance of the evidence. 306 Kan. at 591.


       The district court held that the evidence from Volle's cell phone should not be
suppressed because it would have been discovered from an independent source—
Croskey's phone. Volle disagrees, arguing that the search of his phone was not inevitable.
He alleges that Croskey's phone only contained innocuous text message exchanges
between them that do not establish any basis for a search of Volle's phone.


       But Volle's argument ignores the fact that Croskey, the initial suspect in the
murder investigation, named Volle as the shooter during his interview with law
enforcement and said that he had been in contact with Volle before and after the shooting.
Based on this information, law enforcement sought a search warrant for the data on both
Croskey's and Volle's cell phones. So even if law enforcement had only searched
Croskey's phone, call logs and text messages from Croskey's phone around the time of
the murder would have ultimately led law enforcement to Volle and his phone. Therefore,
the district court did not err in finding the inevitable discovery doctrine applied.


              iii. Conclusion


       The district court properly admitted the cell-phone evidence under both the good-
faith and inevitable-discovery exceptions to the exclusionary rule. Thus, the district court
did not err in denying Volle's motion to suppress the cell phone evidence.
                                              19
    B.     Motion to suppress jail letters


         Volle also argues that the district court erred in denying his motion to suppress
evidence obtained from the search of his mail while in custody at the Shawnee County
Jail.


         Following Volle's arrest, he was held at the Shawnee County Jail. When inmates
arrive at the jail, they are provided with a physical copy of an Inmate Handbook. The
handbook may also be available in a digital format that inmates can access. The
handbook sets forth the jail's rules and expectations as well as inmate rights and
responsibilities. Relevant here, the handbook provides:


    • "You have the right to communicate with family, friends, and others via written
         correspondence, telephone calls, and/or visits according to facility rules,
         regulations, and schedules."


    • "You shall be allowed to correspond in writing with persons or organizations
         outside of this facility, unless there is a specific reason(s) to prohibit the
         correspondence to protect the safety and security of the recipient, the public, or the
         staff and inmates of the facility. Mail shall be limited to your personal
         correspondence with individuals outside the facility. All incoming and outgoing
         mail shall be subject to search at any time." (Emphasis added.)


         After Volle's arrest, Detective Strathman requested that the jail monitor Volle's
outgoing mail. According to the detective, it is common practice to monitor mail in cases
involving co-defendants "[p]artly because people that are incarcerated and don't have


                                                 20
access to the other party typically will go through somebody else to either send them a
message or something of that affect, or communicate about the case."


        After receiving the request from Detective Strathman, Shawnee County Jail
Lieutenant Matt Biltoft collected, opened, and scanned Volle's nonlegal mail and sent
digital copies to Detective Strathman. Two of Volle's outgoing letters caught the
detective's attention. The first letter was addressed to Destiny Baker and reads, in relevant
part:


                  "So, I'm not technically allowed to try to influence [Croskey] myself or threaten
        him, but if u were ta guide him N the direction he should prolly go it's not against the
        rules. Essentially you'll have to make him understand some things u already know. First
        and foremost-bein a snitch . . . is extremely dangerous 4 him.


                  "What's done is done tho now. He already wrote a statement and made up a story
        bcuz his mind was fucked up. They're prolly gonna offer him 60-120 months to testify on
        me. What they aren't gonna tell him is that they're gonna put him on the front page of the
        newspaper and everybody N prison will be waiting 4 him 2 get there. He'll only have 2
        choices—they both involve death just who's gonna b the cause of it? I'm not saying this ta
        try to threaten him, but he's a Topeka Crip. His own people aren't going ta let him walk
        around.


                  "He does have legal options tho. We know he was highly intoxicated when he
        talked to the police. That's called 'voluntary intoxication' and is enough to withdraw his
        statement mixed wit the fact that he was suicidal at the time of giving the statement. He
        needs to make his lawyer have a Jackson v. Denno hearing to get his statement
        withdrawn. Without his statement, the worst they can get him 4 is involuntary
        manslaughter & he could possibly go home the day of trial. Worst case scenario he'll
        have to do 32 months & if he withdraws his statement, from the second he steps foot N
        prison . . . he'll be treated like a God.



                                                     21
               "He does NOT have to testify against me (5th Amendment to the U.S.
       Constitution), but if he were to get on stand at my preliminary hearing on 8-18 & just told
       them that he was upset at me at the time he gave his statement & lied & told them it was
       me to try ta get me N trouble, that would also allow me to help him N the long run.


               "The reason I'm telling this all ta u is because he loves u more than he loves
       himself. U know he would do whatever u told him ta do. If u were to simply tell him that
       if he did the right thing & tell them that he lied u would b his chick through his whole
       prison sentence & you'd have a house 4 him to come home to. And on the other hand, if
       he were to go down a snitch, you'd never talk ta him again. You know how to work that
       nigga. U got me?"


The second letter was addressed to Noah Broja. It reads, in relevant part: "Bro do me a
HUGE favor and schedule visits 4 Brandon Croskey 4 as many as u can, under the name
DeathB4dishonor. Clog em up so he can't get any. And do it every few days."


       Based on the content of these letters, Detective Strathman requested and obtained
a search warrant to collect the original letters from Volle's property bag at the jail. Volle
filed a pretrial motion to suppress the letters, raising several constitutional arguments—
primarily, a violation of his right to privacy under the Fourth Amendment. After
considering the parties' written and oral arguments, the district court denied the motion.
Over Volle's objection at trial, the district court allowed the State to admit the letters into
evidence.


       As discussed, the Fourth Amendment prohibits unreasonable searches and
seizures. U.S. Const. amend. IV. But the Fourth Amendment is not implicated unless the
person invoking its protection had a justifiable, reasonable, or legitimate expectation of
privacy that was invaded by government action. Smith v. Maryland, 442 U.S. 735, 740,
99 S. Ct. 2577, 61 L. Ed. 2d 220 (1979); see Illinois v. Caballes, 543 U.S. 405, 408, 125

                                                   22
S. Ct. 834, 160 L. Ed. 2d 842 (2005) ("Official conduct that does not 'compromise any
legitimate interest in privacy' is not a search subject to the Fourth Amendment.").


       Ordinarily, the public at large has a legitimate expectation of privacy in letters and
other sealed packages. United States v. Jacobsen, 466 U.S. 109, 114, 104 S. Ct. 1652, 80
L. Ed. 2d 85 (1984). But the Fourth Amendment does not prohibit the examination of
prisoners' mail when it is prompted by reasonable justification. State v. Burnett, 300 Kan.
419, 442, 329 P.3d 1169 (2014) ("'[B]ecause of their reasonable concern for prison
security and inmates' diminished expectations of privacy, prison officials do not violate
the constitution when they read inmates' outgoing letters.'"); see United States v. Gordon,
168 F.3d 1222, 1228 (10th Cir. 1999) (The regulation of unprivileged incoming and
outgoing prison mail by prison officials is typically "an administrative matter in which
the courts will not intervene.").


       Volle argues the State failed to identify any reasonable justification for monitoring
his mail. Specifically, he contends Detective Strathman's request to monitor his mail as a
matter of "common practice" in multi-defendant cases was not connected to any
legitimate governmental interest. Without a reason for monitoring specific to him, Volle
contends the broad and sweeping request to seize all his mail violated his constitutional
rights under the Fourth Amendment.


       Courts generally assess whether a detainee has a reasonable expectation of privacy
in nonprivileged mail by examining the institution's policies. Burnett, 300 Kan. at 443-44
(finding defendant had no reasonable expectation that his letters would remain private
where defendant knew the jail reserved "'the right to monitor incoming/outgoing mail for
threats, escape plots, and other security concerns'"); State v. Matthews, 217 Kan. 654,
657-58, 538 P.2d 637 (1975) ("Since the letter was delivered to the jailer unsealed and


                                             23
with knowledge that it would be read [pursuant to jail policy], defendant has no claim of
any invasion of privacy.").


       Inmates at the Shawnee County Jail place outgoing mail in a communal box in
their living unit. The mailroom staff collects the letters and then sends them out of the
building. The inmate handbook—which Volle does not deny he received—provides that
all incoming and outgoing mail is subject to search at any time "to protect the safety and
security of the recipient, the public, or the staff and inmates of the facility." This policy
serves as a reasonable governmental justification for limiting Volle's already diminished
privacy interest. Moreover, Detective Strathman articulated an additional public-safety
rationale: in cases involving co-defendants, law enforcement monitors inmate mail to
prevent improper communications about the case. See State v. Mason, 268 Kan. 37, 41,
986 P.2d 387 (1999) ("[P]risoners' outgoing mail may be screened for information on
future criminal activities.").


       Under these circumstances, Volle lacked any legitimate expectation of privacy in
his nonlegal outgoing mail, and the State had a reasonable and specific justification for
monitoring it. Accordingly, the district court did not err in denying Volle's motion to
suppress the jail-letter evidence.


II. Aiding and abetting jury instruction

       Volle argues the district court committed reversible error when it sua sponte issued
a jury instruction on aiding and abetting.


       When analyzing jury instruction issues, appellate courts follow a three-step
process: (1) determining whether the appellate court can or should review the issue, in
other words, whether there is a lack of jurisdiction or a failure to preserve the issue for

                                              24
appeal; (2) considering the merits of the claim to determine whether error occurred
below; and (3) assessing whether any error requires reversal, in other words, whether the
error can be considered harmless. State v. Holley, 313 Kan. 249, 253, 485 P.3d 614
(2021); see K.S.A. 22-3414(3) ("No party may assign as error the giving or failure to give
an instruction . . . unless the party objects thereto before the jury retires to consider its
verdict . . . unless the instruction or the failure to give an instruction is clearly
erroneous.").


       At the first step, Volle objected to the instruction, which preserves the issue for
review. At the second step, we consider whether the aiding and abetting instruction was
legally and factually appropriate, using an unlimited standard of review of the entire
record. See Holley, 313 Kan. at 254. Neither party suggests that the instruction was
legally deficient in any way, so we assume that the instruction provided an accurate
recitation of Kansas' aiding and abetting law. State v. Broxton, 311 Kan. 357, 361, 461
P.3d 54 (2020) (To be legally appropriate, the instruction must fairly and accurately state
the applicable law.).


       Thus, our review at the second step focuses solely on whether the aiding and
abetting instruction was factually appropriate. To determine whether an instruction was
factually appropriate, we must decide whether there was sufficient evidence, viewed in
the light most favorable to the requesting party, to support the instruction. Holley, 313
Kan. at 255. Circumstantial evidence is enough to support a conviction of even the
gravest offense. In analyzing this issue, appellate courts do not reweigh the evidence,
resolve conflicts in the evidence, or pass on the credibility of witnesses. State v. Aguirre,
313 Kan. 189, 209, 485 P.3d 576 (2021).


       Though not requested by either party, the district court issued the following jury
instruction No. 8 on aiding and abetting:
                                                25
              "A person is criminally responsible for a crime committed by another if the
      person, either before or during its commission, and with the mental culpability required
      to commit the crime, intentionally aids the other person to commit the crime.


              "The person who is responsible for a crime committed by another is also
      responsible for any other crime committed in carrying out or attempting to carry out the
      intended crime, if the person could reasonably foresee the other crime as a probable
      consequence of committing or attempting to commit the intended crime.


              "All participants in a crime are equally responsible without regard to the extent of
      their participation. However, mere association with another person who actually commits
      the crime or mere presence in the vicinity of the crime is insufficient to make a person
      criminally responsible for the crime.


              "It is not a defense that others who participated in the commission of the crime
      has or has not been convicted of the crime, any lesser degree of the crime, or some other
      crime based on the same act."


See K.S.A. 21-5210; PIK Crim. 4th 52.140; PIK Crim. 4th 52.150.


      This instruction sets out several related principles of accomplice liability:


      (1) A person can be guilty of a crime someone else commits if they
          knowingly and intentionally help that person commit the crime;


      (2) A person who helps commit a crime is also responsible for any other
          crimes that happen while carrying out or trying to carry out the plan, if
          those other crimes could reasonably be expected to happen;



                                                  26
       (3) Everyone who takes part in a crime is equally responsible, no matter
          how much they were involved. But just being with someone who
          commits a crime, or simply being nearby, is not enough to make you
          guilty; and


       (4) It is not a defense that the other people involved were convicted of a
          different crime, a lesser crime, or weren't convicted at all.


If the jury unanimously agreed that Volle should be held responsible for Croskey's
criminal acts under these principles of accomplice liability, Volle was criminally
responsible for the murder even if he did not fire the shot that killed Shepherd.


       K.S.A. 21-5210(a) codifies this theory of liability: "A person is criminally
responsible for a crime committed by another if such person, acting with the mental
culpability required for the commission thereof, advises, hires, counsels or procures the
other to commit the crime or intentionally aids the other in committing the conduct
constituting the crime." But mere association with a bad actor cannot establish guilt
through accomplice liability. State v. Llamas, 298 Kan. 246, 253, 311 P.3d 399 (2013).
"'[T]o be guilty of aiding and abetting a defendant must willfully and knowingly associate
himself with the unlawful venture and willfully participate in it as he would in something
he wishes to bring about or to make succeed.'" Llamas, 298 Kan. at 253; see State v.
Simmons, 282 Kan. 728, 737-39, 148 P.3d 525 (2006) (witnesses who did not participate
in robbery were not accomplices; their mere presence during the planning stages and
receipt of stolen goods as incentives for their silence did not make them liable).


       An aiding-and-abetting instruction is factually appropriate if, based on the totality
of the evidence, the jury could reasonably conclude that the defendant aided and abetted
another in the commission of the crime. State v. Shields, 315 Kan. 814, 835, 511 P.3d 931
                                             27
(2022). Volle argues that the aiding and abetting instruction was not factually appropriate
because there was no evidence that he and Croskey acted together to shoot Shepherd.
Volle notes that he and Croskey presented conflicting testimony, each blaming the other
for the shooting and claiming they were unaware that the other person had a firearm or
was planning to use it to shoot Shepherd.


       But Volle's argument seeks to narrow the scope of accomplice liability to the act
of the shooting itself and ignores evidence of his actions both before and after the
shooting. Viewed in a light most favorable to the State (as the appellate party arguing in
favor of the instruction), sufficient evidence could support a jury's finding that Volle
willfully and knowingly associated with and participated in a criminal venture beyond
mere association. The State presented evidence that Croskey wanted to fight Shepherd
and contacted Volle to be his backup. Volle willingly got into Croskey's Trailblazer and
accompanied him to follow Shepherd. During this pursuit, Volle's gun was used to fire a
gunshot from the Trailblazer, killing Shepherd. After the shooting, Volle and Croskey
went to Volle's house, where they talked about the shooting and Volle wiped fingerprints
from the gun and discussed how to sell or destroy it. Volle never contacted the police to
report the shooting and told Croskey to leave him out of it if he decided to report it.


       Thus, even if the jury could not agree on who fired the fatal shot, sufficient
evidence could support a jury's finding that Volle aided and abetted Croskey in the
killing. See State v. Blevins, 313 Kan. 413, 428, 485 P.3d 1175 (2021) (conflicting
evidence creating ambiguity as to which party pulled the trigger rendered aiding and
abetting instruction factually appropriate); Llamas, 298 Kan. at 254 ("The requisite intent
to aid and abet the inherently dangerous felony may be inferred from circumstantial
evidence."). As a result, the aiding and abetting instruction was factually appropriate.
Because the instruction was both legally and factually appropriate, the district court did
not err in giving it.
                                             28
III. Cumulative error

       Volle argues that the cumulative effect of the errors alleged above warrants
reversal of his convictions.


       Cumulative trial errors, when considered together, may require reversal of the
defendant's convictions when the totality of the circumstances establish that the defendant
was substantially prejudiced by the errors and denied a fair trial. State v. Alfaro-Valleda,
314 Kan. 526, 551, 502 P.3d 66 (2022). But the cumulative error rule does not apply
when, as here, there are no errors. See State v. Lowry, 317 Kan. 89, 100, 524 P.3d 416
(2023).


IV. Sufficiency of the evidence

       Next, Volle challenges the sufficiency of the evidence supporting his conviction
for first-degree felony murder.


               "'When the sufficiency of the evidence is challenged in a criminal case, we
       review the evidence in a light most favorable to the State to determine whether a rational
       factfinder could have found the defendant guilty beyond a reasonable doubt. An appellate
       court does not reweigh evidence, resolve conflicts in the evidence, or pass on the
       credibility of witnesses.'" Aguirre, 313 Kan. at 209.


       K.S.A. 21-5402(a)(2) defines felony murder as "the killing of a human being
committed . . . in the commission of, attempt to commit, or flight from any inherently
dangerous felony." Criminal discharge of a firearm at an occupied motor vehicle is
included in the statutory list of inherently dangerous felonies. See K.S.A. 21-
5402(c)(1)(O); K.S.A. 21-6308(a)(1)(B).

                                                   29
       Consistent with this statutory definition and the principles of accomplice liability
previously discussed, the district court instructed the jury that to find Volle guilty of
felony murder, the State had to prove that (1) Volle or another for whose conduct he is
criminally responsible killed Shepherd and (2) the killing occurred while Volle or another
for whose conduct he is criminally responsible was committing criminal discharge of a
firearm at an occupied vehicle. The court also instructed the jury that to establish the
crime of criminal discharge of a firearm at an occupied vehicle, the State was required to
prove, in relevant part:


       "1. Mr. Volle or another for whose conduct he is criminally responsible discharged
       a firearm at an occupied vehicle.


       "2. Mr. Volle or another for whose conduct he is criminally responsible did so recklessly
       and without authority.


       "3. The vehicle was occupied by a human being at the time, whether or not Mr. Volle or
       another for whose conduct he is criminally responsible knew or had reason to know it
       was occupied."


See K.S.A. 21-6308(a)(1)(B).


       Volle argues that the evidence is insufficient to support his conviction for first-
degree felony murder because the State failed to prove the predicate offense it alleged to
support his felony-murder conviction—criminal discharge of a firearm at an occupied
motor vehicle. Volle claims the evidence showed that he shot only at Shepherd, not at a
vehicle.




                                                  30
       This court rejected the same argument in State v. Farmer, 285 Kan. 541, 175 P.3d
221 (2008), and recently affirmed that decision in State v. Levy, 313 Kan. 232, 485 P.3d
605 (2021).


       In Farmer, the defendant walked up to a vehicle window and shot the driver
multiple times both at close range and while backing away from the vehicle. He was
convicted of criminal discharge of a firearm at an occupied vehicle and felony murder.
On appeal, the defendant argued the evidence was insufficient to prove criminal
discharge of a firearm at an occupied vehicle because the evidence showed he fired at the
person in the vehicle, and not at the vehicle. 285 Kan. at 544-45.


       A majority of this court rejected the argument, holding that the prior version of the
criminal discharge statute did not require the State to prove that the shooter intended to
shoot the vehicle or building:


       "The statute was designed to cover situations where there are difficulties in proving the
       shooter's intent. According to Farmer's, and the dissent's, interpretation of the criminal
       discharge statute, there cannot be any evidence of intent to shoot at anything other than
       the occupied vehicle or building itself. In other words, there must be a complete absence
       of intent to hit an occupant of an occupied vehicle or building for the statute to apply.
       Such a construction eviscerates the criminal discharge statute by putting the focus right
       back on the shooter's intent, thus making it unavailable in the very situations it was
       designed to cover—situations where proof of intent to injure or kill is problematic."
       Farmer, 285 Kan. at 546-47.


       In dissent, Justice Beier concluded that the phrase "'at [a] . . . motor vehicle'" was
not ambiguous and required proof of a specific intent to shoot at the vehicle rather than
some other target. 285 Kan. at 556 (Beier, J., concurring in part and dissenting in part)



                                                    31
("[T]here is zero evidence that Farmer shot at the vehicle in which DeAundrey Neal
happened to be sitting rather than at Neal himself.").


       In Levy, the defendant exchanged gunfire with a rival gang, which resulted in the
shooting death of an innocent victim in a nearby truck. 313 Kan. at 232-33. Relying on
Justice Beier's analysis in the Farmer dissent, the defendant challenged his felony-murder
conviction by claiming the evidence was insufficient to support the predicate crime of
criminal discharge of a firearm at an occupied vehicle because the evidence showed only
that he intended to fire at a rival gang member, not at an occupied vehicle. 313 Kan. at
234-35. This court declined the defendant's invitation to revisit its decision in Farmer:


       "In Kansas, the crime of criminal discharge does not require a specific intent to shoot 'at a
       motor vehicle' as opposed to at some other target—whether that target is inside the
       vehicle, hiding behind the vehicle, or only nearby the vehicle. This conclusion is further
       supported by the legislative amendments to the criminal discharge statute altering the
       necessary state of mind to 'reckless.' Compare K.S.A. 2006 Supp. 21-4219(b)
       (criminalizing 'the malicious, intentional and unauthorized discharge of a firearm') with
       K.S.A. 2020 Supp. 21-6308(a)(1)(b) (changing the mens rea to 'reckless'). Putting all this
       together, a person has committed the crime of criminal discharge under K.S.A. 2020
       Supp. 21-6308(a)(1)(B) if: (1) that person recklessly and without authorization discharges
       a firearm; (2) that discharge was 'at a motor vehicle' independent of the shooter's intended
       target; and (3) a person was inside the vehicle." Levy, 313 Kan. at 236.


       Volle acknowledges this court's precedent in Farmer and Levy but disagrees with
the analysis in those cases, claiming it is contrary to the plain language of K.S.A. 21-
6308(a)(1)(B)—which requires that the firearm be discharged at an occupied vehicle—
and renders the phrase "at a motor vehicle" meaningless. He argues these cases were
wrongly decided because they focus on the shooter's intent rather than the shooter's
actions. Citing evidence in the record that the gun was only fired when its laser was
positioned on Shepherd and that no bullets hit Shepherd's car, Volle claims he did not
                                                    32
violate the statute because he did not fire at an occupied vehicle. Given the ambiguity of
K.S.A. 21-6308(a)(1)(B), Volle suggests the rule of lenity requires the statute to be
construed in his favor.


       Volle offers no compelling reason to deviate from our prior rulings in Farmer and
Levy. These decisions are not in conflict with K.S.A. 21-6308(a)(1)(B)'s plain language,
they do not render the phrase "at a motor vehicle" meaningless, and they do not focus on
the shooter's intent. To the contrary, Farmer and Levy both discussed how the criminal
discharge statute removed the focus from the shooter's intent. See Farmer, 285 Kan. at
546 ("The statute was designed to cover situations where there are difficulties in proving
the shooter's intent."); Levy, 313 Kan. at 236 (discussing legislative amendments to the
criminal discharge statute altering the necessary state of mind to "reckless").


       As discussed, to prove the offense of criminal discharge of a firearm at an
occupied motor vehicle, the State was required to prove that Volle (or another whose
conduct he was criminally responsible for): (1) recklessly discharged a firearm (2) at a
motor vehicle (3) with a person inside. See K.S.A. 21-6308(a)(1)(B); Levy, 313 Kan. at
236. The evidence presented at trial established that Shepherd was standing inside the
open driver's side door of his car when he was shot and that Megan was inside the car.
Although the shot did not hit the car, it need not do so to meet the elements of the crime
and does not negate the fact that the shot was fired at a motor vehicle occupied by
Megan. Viewing the evidence in the light most favorable to the State, a rational factfinder
could find Volle guilty beyond a reasonable doubt of the crime of criminal discharge of a
firearm at an occupied motor vehicle. As a result, the evidence was sufficient to support
Volle's felony-murder conviction.




                                             33
V. Sentencing


       Finally, Volle contends the district court erred when it sentenced him for his
felony-murder conviction because his conviction for reckless second-degree murder was
more specific and therefore should control his sentence under K.S.A. 21-5109(d).


       Resolving this issue requires statutory interpretation, which presents a question of
law over which appellate courts have unlimited review. State v. Betts, 316 Kan. 191, 197,
514 P.3d 341 (2022). When interpreting a statute, an appellate court must first attempt to
give effect to the intent of the Legislature through the statutory language enacted, giving
common words their ordinary meanings. When a statute is plain and unambiguous, an
appellate court should not speculate about the legislative intent behind that clear
language, and it should refrain from reading something into the statute that is not readily
found in its words. State v. Keys, 315 Kan. 690, 698, 510 P.3d 706 (2022).


       K.S.A. 21-5109(a) provides that a defendant may be charged with multiple crimes
stemming from the same conduct in different counts within a single complaint. But when
the crimes alleged "differ only in that one is defined to prohibit a designated kind of
conduct generally and the other to prohibit a specific instance of such conduct," the
defendant can be convicted only of one of the crimes and must be sentenced "according
to the terms of the more specific crime." K.S.A. 21-5109(d).


       Here, the jury found Volle guilty of felony murder and the alternative lesser
included offense of reckless second-degree murder. Felony murder is "the killing of a
human being committed . . . in the commission of, attempt to commit, or flight from any
inherently dangerous felony." K.S.A. 21-5402(a)(2). Reckless second-degree murder is
"the killing of a human being committed . . . unintentionally but recklessly under


                                             34
circumstances manifesting extreme indifference to the value of human life." K.S.A. 21-
5403(a)(2).


       Volle suggests that because his convictions for the two crimes were based on the
same conduct, reckless second-degree murder criminalizes more specific conduct since it
requires a mental state of recklessness, while felony murder does not require a culpable
mental state.


       Volle's argument misinterprets K.S.A. 21-5109(d). Although the same conduct
may support both felony murder and reckless second-degree murder, as it did here, the
felony-murder and reckless second-degree murder statutes are aimed at preventing
different conduct and require different elements of proof and different levels of mental
culpability. While both involve an unintentional killing, felony murder "requires proof
the defendant engaged in dangerous, felonious conduct and that a death occurred as a
result of that conduct." State v. Patterson, 311 Kan. 59, 67, 455 P.3d 792 (2020); see
K.S.A. 21-5402(a)(2) (felony murder requires proof of inherently dangerous felony). By
contrast, reckless second-degree murder does not require a defendant to engage in
dangerous, felonious conduct. Rather, the unintentional killing is borne out of reckless
conduct. State v. Deal, 293 Kan. 872, 883-84, 269 P.3d 1282 (2012); see K.S.A. 21-
5202(j) ("A person acts 'recklessly' or is 'reckless,' when such person consciously
disregards a substantial and unjustifiable risk that circumstances exist or that a result will
follow, and such disregard constitutes a gross deviation from the standard of care which a
reasonable person would exercise in the situation."); State v. Johnson, 304 Kan. 924, Syl.
¶ 5, 376 P.3d 70 (2016) (Reckless second-degree murder is not purposeful, willful, or
knowing, but results from an act performed with knowledge that the victim is in
imminent danger, although death is not foreseen.). In sum, neither crime is more general
nor more specific than the other because each targets a different theory of liability.
Because the reckless second-degree murder statute does not punish a more specific
                                              35
instance of conduct generally prohibited by the felony-murder statute, K.S.A. 21-5109(d)
does not apply to Volle's convictions.


       Moreover, although not discussed by either party, we find the district court
correctly sentenced Volle for felony murder based on Kansas' rules governing
convictions and sentencing for alternative charges. A defendant charged in the alternative
may be convicted of only one of the alternative offenses. State v. Garza, 290 Kan. 1021,
Syl. ¶ 5, 236 P.3d 501 (2010). When a jury returns guilty verdicts on two alternatively
charged counts, the doctrine of merger applies, and the district court must accept only the
verdict as to the greater charge. State v. Vargas, 313 Kan. 866, 873, 492 P.3d 412 (2021).


       The jury returned a verdict finding Volle guilty of both first-degree felony murder
and reckless second-degree murder—a lesser included offense of first-degree
premeditated murder, which the State had charged in the alternative. At sentencing, the
district court merged the murder convictions into a single conviction for first-degree
felony murder and sentenced Volle for that crime. Reckless second-degree murder is a
severity level 2, person felony. K.S.A. 21-5403(b)(2). First-degree murder is an off-grid
felony. K.S.A. 21-5402(b). Accordingly, the district court correctly applied the doctrine
of merger and sentenced Volle on the greater charge of felony murder.


       Finally, we acknowledge Volle's submission under Supreme Court Rule 6.09(b)
(2025 Kan. S. Ct. R. at 41) directing our attention to State v. Johnson, 321 Kan. ___,
2025 WL 3289978 (2025). Contrary to Volle's claim, Johnson's interpretation of K.S.A.
21-5109(d) aligns with—and confirms—the analysis and outcome we reach in this case.


       The judgment of the district court is affirmed.




                                            36

```

---

## GROUP: _overhaul2/lake/cases/State v. Weaver.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: State v. Weaver
type: case
citation: "2011 Tex. Crim. App. LEXIS 1320 (2011)"
parallel_cite: 349 S.W.3d 521
neutral_cite: 2011 WL 4715178
court: Tex. Crim. App.
court_level: state
circuit: ""
year: 2011
date_decided: 2011-09-28
docket: PD-1635-10
authority_weight: "Persuasive — state, illustrative"
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
  opinion_url: "https://www.courtlistener.com/opinion/2546485/state-v-weaver/"
  cluster_id: 2546485
  opinion_id: null
  identity_checked: true
lake:
  record_id: State v. Weaver
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Curtilage]]"
    role: Key
related:
  - "[[Curtilage]]"
  - "[[Consent Searches]]"
  - "[[Illinois v. Caballes]]"
  - "[[Florida v. Jimeno]]"
tags:
  - case
  - fourth-amendment
  - search
  - curtilage
  - consent
  - dog-sniff
  - state-court
holding: "A canine sniff of a vehicle on private, non-public business premises exceeds the scope of a limited consent and is unlawful once the owner's consent to be there for a particular purpose has ended — the rule that a dog sniff is not itself a Fourth Amendment search presupposes that the officer, and therefore the dog, has a lawful right to be where the sniff occurs, so suppression was proper where officers lingered and deployed a drug dog after their consented-to search for a person came up empty."
---

# State v. Weaver

*349 S.W.3d 521 (Tex. Crim. App. 2011)* (No. PD-1635-10) · Court of Criminal Appeals of Texas · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 2546485 → opinion 2546485 (349 S.W.3d 521, decided 2011-09-28); Rule quote string-matched to the CL opinion text 2026-07-07. Note: lake selected the neutral cite 2011 Tex. Crim. App. LEXIS 1320 as official — flagged for S2 re-selection (S.W.3d reporter is the correct primary). S9 promotes. -->

## Background
Four Polk County narcotics officers came to Roy Weaver's welding shop looking for "Bear," a man wanted in another county, and Weaver gave them consent to "look for him." After about ten minutes the officers had not found Bear or anything suspicious, but — having heard that methamphetamine was distributed from the business — they lingered. Sergeant Smith questioned Weaver, then asked to search a van backed into the workshop bay; Weaver refused. Smith immediately had a drug dog run around the van; the dog alerted, the van was searched, and a tin box holding glass pipes and methamphetamine was found. Weaver was arrested and charged with possession. The trial court suppressed the evidence, finding the search exceeded the scope of Weaver's consent; the court of appeals affirmed over a [[Common Legal Terms#dissenting-opinion|dissent]].

## Issue
Whether a warrantless canine sniff and search of a vehicle on the owner's private, non-public business premises — conducted after his limited consent to search for a person had come up empty and after he refused consent to search the van — exceeded the scope of his consent in violation of the Fourth Amendment.

## Rule
The Court of Criminal Appeals affirmed, resolving the case on the scope of consent. It reasoned that the settled rule that a dog sniff is not itself a Fourth Amendment search presupposes that the officer, and therefore the dog, has a right to be standing where the sniff occurs — a premise absent here, on private premises where the owner's limited consent had ended. The court held: "Because we agree that the resolution of this case turns on the scope of Mr. Weaver's consent, we affirm the judgment of the trial court and that of the court of appeals." — 349 S.W.3d at 523. ^pin-523

## Application
Weaver's consent authorized only a search for "Bear"; once that search produced nothing, a reasonable person would understand the consent as exhausted. The officers then had no lawful basis — neither probable cause nor continuing consent — to remain and deploy a drug dog around the van in the private, non-public workshop bay, an area the majority found was not open to the general public. Because the dog and officers lacked any right to be where they were when the sniff occurred, the *Caballes/Place* rule that a canine sniff is not a search did not apply, and the resulting search fell outside Weaver's consent.

## Conclusion
The suppression order was **affirmed**. Cochran, J., wrote for the majority (Meyers, Price, Womack, Johnson, Alcala, JJ.). Keller, P.J., and Keasler, J., dissented, arguing the dog sniff was not a search and that under *State v. Elias* the case should be [[Reading and Citing Cases#on-remand|remanded]] for a finding on whether the parking area was public or private.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Weaver* marks the private-premises limit on suspicionless canine sniffs: because the dog-sniff-is-not-a-search rule of *[[Illinois v. Caballes|Caballes]]* and *[[United States v. Place|Place]]* presupposes the officer's lawful presence, it does not reach a sniff conducted on private, non-public business [[Curtilage|curtilage]] after the owner's limited consent has ended.

## Appears on
- [[Curtilage]] — *Key*

## Sources
- [*State v. Weaver*, 349 S.W.3d 521 (Tex. Crim. App. 2011)](https://www.courtlistener.com/opinion/2546485/state-v-weaver/) — pinpoint: 523 (scope-of-consent holding; the CL opinion text star-paginates the S.W.3d reporter). Parallel neutral cite 2011 Tex. Crim. App. LEXIS 1320. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "771b8f55c10a8942", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "State v. Weaver"}, "payload": {"all": [{"cite": "349 S.W.3d 521", "page": "521", "reporter": "S.W.3d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "349"}, {"cite": "2011 Tex. Crim. App. LEXIS 1320", "page": "1320", "reporter": "Tex. Crim. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2011"}, {"cite": "2011 WL 4715178", "page": "4715178", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2011"}], "display": "2011 Tex. Crim. App. LEXIS 1320", "official": {"cite": "2011 Tex. Crim. App. LEXIS 1320", "page": "1320", "reporter": "Tex. Crim. App. LEXIS", "selected_official": true, "source": "cluster.citations[]", "type": 2, "volume": "2011"}, "official_selection_present": true, "record_id": "State v. Weaver"}}
{"assertion_id": "14ebbd28c8f35346", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Weaver"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "State v. Weaver", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — State v. Weaver

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Weaver",
  "status": "under_review",
  "identity": {
    "case_name": "State v. Weaver",
    "case_name_short": "Weaver",
    "case_name_full": "The STATE of Texas v. Roy Andrew WEAVER, Appellee",
    "input_case_name": "State v. Weaver",
    "court": "Tex. Crim. App.",
    "court_id": null,
    "court_level": "state",
    "circuit": null,
    "state": "Texas",
    "date_decided": "2011-09-28",
    "year": 2011,
    "docket": "PD-1635-10",
    "cluster_id": 2546485,
    "lead_opinion_id": 9784480,
    "sibling_ids": [],
    "absolute_url": "/opinion/2546485/state-v-weaver/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "2011 Tex. Crim. App. LEXIS 1320",
      "volume": "2011",
      "reporter": "Tex. Crim. App. LEXIS",
      "page": "1320",
      "type": 2,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "349 S.W.3d 521",
        "volume": "349",
        "reporter": "S.W.3d",
        "page": "521",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 WL 4715178",
        "volume": "2011",
        "reporter": "WL",
        "page": "4715178",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "349 S.W.3d 521",
        "volume": "349",
        "reporter": "S.W.3d",
        "page": "521",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 Tex. Crim. App. LEXIS 1320",
        "volume": "2011",
        "reporter": "Tex. Crim. App. LEXIS",
        "page": "1320",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 WL 4715178",
        "volume": "2011",
        "reporter": "WL",
        "page": "4715178",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "2011 Tex. Crim. App. LEXIS 1320",
    "official_selection": {
      "court_class": "state",
      "selected": "2011 Tex. Crim. App. LEXIS 1320",
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
    "date_created": "2026-07-07T01:38:37Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:38:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:38:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "state-v-weaver--2546485",
      "to_record_id": "State v. Weaver",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — State v. Weaver

```
<opinion type="majority">
<p id="b543-15">
<em>OPINION</em>
</p>
<author id="b543-16">COCHRAN, J.,</author>
<p id="A3_">delivered the opinion of the Court</p>
<judges id="Av7a">in which MEYERS, PRICE, WOMACK, JOHNSON and ALCALA, JJ., joined.</judges>
<p id="b543-17">Four police officers came to Mr. Weaver’s welding shop looking for a person wanted in another county. Mr. Weaver gave the officers consent to search for that person. The officers, over Mr. Weaver’s objection, ended up searching a van on his property and finding drugs in it. The trial judge granted Mr. Weaver’s motion to suppress because he found that the search of the van exceeded the scope of Mr. Weaver’s consent. The court of appeals, over a dissent, affirmed. We granted review in light of the justices’ disagreement. Because we agree that the resolution of this case turns on the scope of Mr. Weaver’s consent, we affirm the judgment of the trial court and that of the court of appeals.</p>
<p id="b543-18">I.</p>
<p id="b543-19">Roy Andrew Weaver owned a welding shop in Polk County.<footnotemark>1</footnotemark> There was a front office and a workshop in the rear. At the back on one side of the workshop was an open bay door with a van backed into it. Also parked in the back yard were several “broken down” vehicles, a boat, and “some other items.” One day, while the shop was open, four Polk County narcotics officers came looking for Jerry Barksdale (“Bear”), who worked or “hung out” at the shop. Bear was wanted in another county for organized crime. When the officers arrived, they saw Bear’s car parked out in front of the shop. The officers asked Mr. Weaver if they “could look around for the <page-number citation-index="1" label="524">*524</page-number>guy,” and he gave them “consent to look for him.”</p>
<p id="b544-4">The officers looked around for about ten minutes, but Bear was not at the shop nor inside the van that was backed up in the workshop bay door. Nonetheless, because the narcotics officers had received information “that there was also methamphetamine being used and distributed from the business,” they lingered in the shop.</p>
<p id="b544-5">Sergeant Smith “just began talking to Mr. Weaver. We were standing just inside the shop. I asked him if he had any illegal guns, knives, narcotics, anything like that. He advised no. He — well, he did tell me he had some guns inside the office.” Mr. Weaver showed Sgt. Smith the licensed guns in his office. After they came out of the office, Sgt. Smith then asked “who the van belonged to.” Mr. Weaver said that it was his dad’s van but that he drove it. When Sgt. Smith asked if he could search the van, Mr. Weaver refused consent.</p>
<p id="b544-6">As soon as Mr. Weaver refused consent, Sgt. Smith told Lieutenant Lowrie to retrieve his drug-dog from the patrol car and run the dog around the van parked in the bay door of the workshop. The dog showed “odor response” to the passenger door. The van was searched, and a tin box that contained glass pipes and some methamphetamine was found on the floorboard between the door and the passenger’s seat. Mr. Weaver was arrested and charged with possession of methamphetamine. He filed a motion to suppress which the trial judge, after hearing testimony from Sgt. Smith and Lt. Lowrie, granted. The judge entered findings of fact, including the following:</p>
<blockquote id="b544-7">3. The defendant gave the officers permission to search his shop for Barks-dale ....</blockquote>
<blockquote id="b544-9">4. A van was located beside the defendant’s shop on property owned by the defendant. Officers looked through the van windows and did not see Barksdale or any contraband.</blockquote>
<blockquote id="pAai">[[Image here]]</blockquote>
<blockquote id="b544-10">6. The officers asked the defendant for permission to search the van. The defendant refused permission and the officers used a drug canine to walk outside of the van.</blockquote>
<p id="b544-11">Based upon his factual findings, the trial judge concluded,</p>
<blockquote id="b544-12">The officers exceeded the scope of their search after they did not find Barksdale and they did not have enough cause to conduct the canine search on the van which they did not see being operated.</blockquote>
<p id="AObk">The State appealed, arguing that the officers and Mr. Weaver had a consensual interaction that never became a detention until the canine alert provided probable cause to arrest Mr. Weaver. Mr. Weaver responded that the consensual encounter became an unlawful detention before the dog sniff. The court of appeals affirmed the trial court’s ruling and held,</p>
<blockquote id="b544-13">In this case, the evidence shows that when the officers’ search for “Bear” ended, they had not observed anything suspicious. Because the trial judge could have determined that Weaver’s consent to search for “Bear” had ended, the trial court could reasonably find that the officers, without establishing probable cause, were not entitled to search for other purposes unrelated to that of their initial search. Under the facts of this case, we conclude the trial court did not abuse its discretion in granting Weaver’s motion to suppress. The trial court’s ruling is affirmed.<footnotemark>2</footnotemark></blockquote>
<p id="b544-14">Justice Gaultney dissented. He framed the issue as “whether the canine sniff of <page-number citation-index="1" label="525">*525</page-number>the exterior of the van while the officers were talking with Weaver was an impermissible ‘search’ for Fourth Amendment purposes.”<footnotemark>3</footnotemark> He concluded, “In this case the officers were on the business premises legally with the consent of the owner. They had not been asked to leave. Although the owner refused consent to a search of the van, the canine sniff of the exterior of the van, made while officers were questioning Weaver, was not a ‘search’ for Fourth Amendment purposes.” <footnotemark>4</footnotemark></p>
<p id="b545-5">The State Prosecuting Attorney (SPA) filed a petition for discretionary review, asking: “May police conduct a dog sniff of the exterior of an unoccupied vehicle in the parking lot of a business without the permission of the owner of the business?” We granted review in light of the justices’ disagreement on a material question of law.<footnotemark>5</footnotemark></p>
<p id="b545-6">II.</p>
<p id="b545-7">
<em>A. Standard of Review.</em>
</p>
<p id="b545-8">When reviewing the ruling on a suppression motion, the trial judge’s determination of facts — if supported by the record — is afforded almost total deference.<footnotemark>6</footnotemark> Regardless of whether the judge granted or denied the motion, appellate courts view the evidence in the light most favorable to the trial judge’s ruling.<footnotemark>7</footnotemark> The prevailing party is afforded the strongest legitimate view of the evidence and all reasonable inferences that may be drawn from that evidence.<footnotemark>8</footnotemark> We review a trial court’s application of the law of search and seizure to the facts <em>de novo.</em><footnotemark><em>9</em></footnotemark><em> </em>“We will sustain the trial judge’s ruling if that ruling is ‘reasonably supported by the record and is correct on any theory of law applicable to the case.’ ”<footnotemark>10</footnotemark></p>
<p id="b545-16">
<em>B. The Scope of Consent Under the Fourth Amendment.</em>
</p>
<p id="b545-17">The Fourth Amendment protects individuals against unreasonable searches and seizures.<footnotemark>11</footnotemark> Reasonableness is the touchstone of the Fourth Amendment.<footnotemark>12</footnotemark> And, “except in certain carefully defined classes of cases, a search of private property without proper consent is ‘unreasonable’ unless it has been authorized by a valid search warrant.”<footnotemark>13</footnotemark> The Supreme Court has “long approved consensual searches because it is no doubt reasonable for the police to conduct a search once <page-number citation-index="1" label="526">*526</page-number>they have been permitted to do so.”<footnotemark>14</footnotemark> Although consent must be positive, it may be given orally or by action, or it may be shown by circumstantial evidence.<footnotemark>15</footnotemark> The validity of an alleged consent to search is a question of fact to be determined from the totality of the circumstances.<footnotemark>16</footnotemark> Under Texas law, the State must prove voluntary consent by clear and convincing evidence.<footnotemark>17</footnotemark></p>
<p id="b546-4">The scope of a search is usually defined by its expressed object.<footnotemark>18</footnotemark> A person is free to limit the scope of the consent that he gives.<footnotemark>19</footnotemark> If police rely on consent as the basis for a warrantless search, “they have no more authority than they have apparently been given by the consent.”<footnotemark>20</footnotemark> It is therefore “important to take account of any express or implied limitations or qualifications attending that consent which establish the permissible scope of the search in terms of such matters as time, duration, area, or intensity.”<footnotemark>21</footnotemark> On the other hand, a person’s silence in the face of an officer’s further actions may imply consent to that further action.<footnotemark>22</footnotemark> The “standard for measuring the scope of a suspect’s consent under the Fourth Amendment is that of ‘objective’ reasonableness — what would the typical reasonable person have understood by the exchange between the officer and the suspect?” <footnotemark>23</footnotemark> Therefore, a court reviewing the totality of the circumstances of a particular police-citizen interaction does so without regard for the subjective thoughts or intents of either the officer or the citizen.<footnotemark>24</footnotemark> Still, in Texas, the “clear and convincing” burden “requires the prosecution to show the consent given was positive and unequivocal and there must not be duress or coercion, actual or implied.”<footnotemark>25</footnotemark></p>
<p id="b546-14">
<em>C. Business and Commercial Premises are Protected Areas.</em>
</p>
<p id="b546-15">The occupant of a business establishment enjoys the same constitutional <page-number citation-index="1" label="527">*527</page-number>right to be free from unreasonable searches as does the occupant of a private residence.<footnotemark>26</footnotemark> But “business and commercial premises are not as private as residential premises,” and “consequently there are various police investigative procedures which may be directed at such premises without the police conduct constituting a Fourth Amendment search.”<footnotemark>27</footnotemark> Police, although motivated by an investigative purpose, are as free as the general public to enter premises “open to the public,” when they are open to the public.<footnotemark>28</footnotemark> Officers are then entitled to note objects in plain view,<footnotemark>29</footnotemark> or examine merchandise as a customer would.<footnotemark>30</footnotemark> For “actions not to constitute a Fourth Amendment search, the officer must remain in that portion of the premises which is open to the public.”<footnotemark>31</footnotemark></p>
<p id="AaB">III.</p>
<p id="b547-10">The SPA asserts that the motion to suppress was granted based on incorrect conclusions of law rather than any fact-findings that were unfavorable to the State. These conclusions were incorrect, argues the SPA, because 1) the officers did not need permission to be in “the parking lot” when they initiated the dog sniff; 2) neither Mr. Weaver nor the van were seized in order to conduct the dog sniff; 3) the dog sniff was not a search; and 4) the dog’s positive alert justified the search. The Supreme Court has made it clear that a dog sniff is not a search,<footnotemark>32</footnotemark> and it is generally accepted that a positive alert by a certified drug dog is usually enough, by itself, to give officers probable cause to <page-number citation-index="1" label="528">*528</page-number>search.<footnotemark>33</footnotemark> We agree with the SPA that neither Mr. Weaver nor the van were seized in order to conduct the dog sniff.</p>
<p id="b548-4">But, as discussed below, the SPA assumes a fact that is not in evidence: that the van was parked in a parking lot “open to the public.”<footnotemark>34</footnotemark> Viewing the evidence in the light most favorable to the trial judge’s ruling, this area was not part of the “public” area of his welding shop. Therefore, the officers needed permission to be where they were when they initiated the dog sniff, but they did not have it.<footnotemark>35</footnotemark></p>
<p id="b548-5"><em>A. Affording appellee the “strongest legitimate view of the evidence, </em>” <em>the van was not parked in a parking lot open to the public.</em></p>
<p id="b548-6">The SPA’s position is apparent in the way it framed the issue for review: “May police conduct a dog sniff of the exterior of an unoccupied vehicle in the parking lot of a business without the permission of the owner of the business?” Surely the answer to that question, on its face, is yes. A public parking lot is public regardless of whether a nearby business is open or not.</p>
<p id="b548-11">In <em>Illinois v. </em>Caballes,<footnotemark>36</footnotemark> the Supreme Court held that the use of a narcotics-detection dog to sniff around the exteri- or of a motorist’s vehicle during a lawful traffic stop did not violate the Fourth Amendment because it revealed no information other than the location of a substance that the individual had no right to possess.<footnotemark>37</footnotemark> In keeping with Justice Ginsburg’s prophecy that <em>Caballes </em>“clears the way for suspicionless, dog-accompanied drug sweeps of parked cars along sidewalks and in parking lots,”<footnotemark>38</footnotemark> it has done just that. Federal and state courts alike have used <em>Caballes </em>to uphold dog sniffs in the public parking lots of gas stations, hotels, restaurants, and high schools.<footnotemark>39</footnotemark> But in <em>Caballes, </em>Justice Stevens empha<page-number citation-index="1" label="529">*529</page-number>sized that the police cannot prolong a traffic stop beyond the time reasonably required to accomplish its purpose simply to give them time to bring in a drug dog.<footnotemark>40</footnotemark> As our courts of appeals have recognized, officers initiating a dog sniff must have the right to be where they are at the time they initiate a dog sniff.<footnotemark>41</footnotemark></p>
<p id="b549-5">It is the <em>Caballes </em>line of cases that the SPA relies on here. The problem in this case is that no one, except the prosecutor, characterized the place the van was parked as a “parking lot.” Lt. Lowrie said that the truck was parked in a “sall[y] port.”</p>
<blockquote id="AJe2">Q. Where was the van parked? '</blockquote>
<blockquote id="b549-6">A. It was the — I guess it would be the north side of the building back up to the big sall[y] port<footnotemark>42</footnotemark> on the building.</blockquote>
<blockquote id="AyVM">Q. Is it, like, a parking lot or a parking area?</blockquote>
<blockquote id="b549-11">A. It’s a big, bay door. I guess you would say it’s kind of like a loading/unloading for the business area.</blockquote>
<p id="b549-12">The State argued to the trial court that “The vehicle ... was located on a parking lot that was in — in a business that was open for public use or open to the public. So the fact that the officers decided to run the canine, even though maybe they didn’t see or smell something, they didn’t have to have any type of reasonable suspicion to do that.” The SPA argues similarly: “While on the premises of a business open to the public, police are permitted to conduct a dog sniff of vehicles parked in the <page-number citation-index="1" label="530">*530</page-number>parking area.... The unoccupied van was parked in the parking lot[.]”<footnotemark>43</footnotemark></p>
<p id="b550-4">But the trial court did not find that the van was parked in a public parking lot. Rather, it found the van “was located beside the defendant’s shop on property owned by the defendant.” The prevailing party is afforded the strongest legitimate view of the evidence and all reasonable inferences that may be drawn from that evidence. The facts here support the trial court’s implicit finding that the van was not parked on any part of the business premises open to the public or in a public “parking lot.”<footnotemark>44</footnotemark> From the evidence in this record, the trial judge could have found otherwise, but he did not do so. We are obliged to give almost total deference to his implied factual findings.<footnotemark>45</footnotemark> Therefore, unless the officers had Mr. Weaver’s consent to be standing beside the van at the loading dock, they were no longer entitled to be in the non-public portion of the welding workshop at the time they conducted the dog sniff.<footnotemark>46</footnotemark></p>
<p id="b550-11">
<em>B. Affording Mr. Weaver the “strongest legitimate view of the evidence," the officers did not have continued consent to be on the premises at the time they ran the dog sniff</em>
</p>
<p id="b550-12">The SPA asserts that the officers — who had lawfully entered the premises — were “under no obligation to leave unless asked” and that there “was no evidence or fact finding that the officers were ever asked to stop their investigation or leave the premises.”<footnotemark>47</footnotemark> But the relevant question here is as follows: What would the typical reasonable person have under<page-number citation-index="1" label="531">*531</page-number>stood by the exchange between the officers and Mr. Weaver?<footnotemark>48</footnotemark> Mr. Weaver gave oral consent to search his welding shop for “Bear,” voluntarily showed the officers his registered guns,<footnotemark>49</footnotemark> and then unequivocally refused to consent to a search of the van backed up in the loading dock of his shop.</p>
<p id="b551-5">We recently addressed the scope of a consent to search under the Fourth Amendment in <em>Valtierra v. State.</em><footnotemark><em>50</em></footnotemark><em> </em>There, the trial court and the court of appeals agreed that Heriberto Valtierra consented to have police officers enter his apartment to talk to Erica, a 13-year-old runaway. The question before us was whether Heriberto’s consent extended to the officer’s act of walking down the open hallway to knock on the bathroom door where Erica was said to be taking a shower. We held that it was objectively reasonable for the officer to conclude that Heriberto’s general consent to come inside the apartment to talk to Erica included consent to walk down the open hallway to knock on the bathroom door.<footnotemark>51</footnotemark> Thus, the officer was lawfully present in the hallway when he observed, through an open bedroom door, two men making furtive gestures and throwing items under the bed.<footnotemark>52</footnotemark></p>
<p id="b551-6">This case is like <em>Valtierra </em>in that the officers here obtained oral consent to enter the premises to look for a specific individual. This case is also unlike <em>Valtierra, </em>because here the officers had finished looking for the specific individual and had achieved the ostensible purpose of their entry. And here, unlike in <em>Valtierra, </em>Mr. Weaver unequivocally said “No,” to a further search of his van.</p>
<p id="b551-11">The legal question is, what would “the typical reasonable person have understood by the exchange between the officer and the suspect?” We think that it was objectively unreasonable for the officers to conclude that Mr. Weaver’s act of objecting to the van search indicated, by clear and convincing evidence, his consent for the officers to remain standing beside his van while one officer went back out to the patrol car and retrieved a drug dog to run around his van.<footnotemark>53</footnotemark> A typical reasonable person would have understood — from Mr. Weaver’s refusal of consent to search the van — that he had had enough. It would be unreasonable for that typical person, having heard an unequivocal “No,” to think that he had “positive and unequivocal” consent, not only to remain standing beside the van on the non-public premises, but also to retrieve yet another unwelcome intruder. There is certainly no indication in the record that Mr. Weaver consented for the officers to bring the drug dog from the patrol car to the van parked at his loading dock. From these facts, the trial <page-number citation-index="1" label="532">*532</page-number>judge could have concluded that the consent to search for “Bear” was lawful at its inception, but that it had been completed. The officers had completed their stated mission. Thus, when Mr. Weaver unequivocally said “No” to any further search of his van, the officers violated the Fourth Amendment by remaining on his private business premises and bringing in a drug dog without legal authorization. Therefore, the trial judge could have justifiably concluded that the “nonconsensual” use of the drug dog and the subsequent discovery of contraband were the product of an unconstitutional search on private premises.</p>
<p id="b552-4">The record, viewed in the light most favorable to the trial judge’s ruling, supports an implicit fact finding that the van was parked in a protected, non-public area of the business premises rather than in a parking lot open to the public. And the record also supports the trial judge’s legal conclusion that the officers had worn out their welcome and lingered beyond the scope of Mr. Weaver’s consent before the initiation of the dog sniff. We recognize that this ease is a close call — but it is in the “close call” cases that the need for giving discretion to the trial judge and deferring to his factual findings is greatest, especially when the State must prove positive consent by clear and convincing evidence. We therefore affirm the court of appeals’s judgment that upheld the trial judge’s ruling.</p>
<judges id="b552-5">KELLER, P.J., filed a dissenting opinion in which KEASLER and HERVEY, JJ., joined.</judges>
<p id="AjE">KEASLER, J., filed a dissenting opinion in which KELLER, P.J., and HERVEY, J., joined.</p>
<footnote label="1">
<p id="AA_">. The shop is located at 203 Gray Drive in Livingston.</p>
</footnote>
<footnote label="2">
<p id="b544-8">. <em>State v. Weaver, </em><span class="citation no-link">2010 WL 3518743</span>, *4, 2010 Tex.App. LEXIS 7425, *9 (Tex.App.-Beaumont Sept. 8, 2010) (not designated for publication)</p>
</footnote>
<footnote label="3">
<p id="b545-9">. <em>Id. </em>at *4, 2010 Tex.App. LEXIS 7425, at *10-11 (Gaultney, J., dissenting).</p>
</footnote>
<footnote label="4">
<p id="b545-10">. <em>Id. </em>at *5, 2010 Tex.App. LEXIS 7425, at *11-12 (citing <em>City of Indianapolis v. Edmond, </em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#40" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32, 40</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S.Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L.Ed.2d 333</a></span> (2000); <em>Illinois v. Caballes, </em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#410" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405, 410</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">160 L.Ed.2d 842</a></span> (2005); <em>United States v. Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U.S. 696, 707</a></span>, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">103 S.Ct. 2637</a></span>, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">77 L.Ed.2d 110</a></span> (1983)).</p>
</footnote>
<footnote label="5">
<p id="b545-12">. Tex.R.App. P. 66.3(e).</p>
</footnote>
<footnote label="6">
<p id="b545-13">. <em>State v. Woodard, </em><span class="citation" data-id="9783836"><a href="/opinion/2540788/state-v-woodard/#410" aria-description="Citation for case: State v. Woodard">341 S.W.3d 404, 410</a></span> (Tex.Crim.App.2011) (citing <em>Guzman v. State, </em><span class="citation" data-id="9863199"><a href="/opinion/2449770/guzman-v-state/#89" aria-description="Citation for case: Guzman v. State">955 S.W.2d 85, 89</a></span> (Tex.Crim.App.1997)).</p>
</footnote>
<footnote label="7">
<p id="b545-14">. <span class="citation" data-id="9863199"><a href="/opinion/2449770/guzman-v-state/" aria-description="Citation for case: Guzman v. State">Id.</a></span> (citing State <em>v. Garcia-Cantu, </em><span class="citation" data-id="9680128"><a href="/opinion/1769810/state-v-garcia-cantu/#241" aria-description="Citation for case: State v. Garcia-Cantu">253 S.W.3d 236, 241</a></span> (Tex.Crim.App.2008); <em>Gutierrez v. State, </em><span class="citation" data-id="9643603"><a href="/opinion/1508583/gutierrez-v-state/#687" aria-description="Citation for case: Gutierrez v. State">221 S.W.3d 680, 687</a></span> (Tex.Crim.App.2007)).</p>
</footnote>
<footnote label="8">
<p id="b545-18">. <em><span class="citation" data-id="9643603"><a href="/opinion/1508583/gutierrez-v-state/" aria-description="Citation for case: Gutierrez v. State">Id.</a></span> </em>(citing <em>Garcia-Cantu, </em><span class="citation" data-id="9680128"><a href="/opinion/1769810/state-v-garcia-cantu/#241" aria-description="Citation for case: State v. Garcia-Cantu">253 S.W.3d at 241</a></span>).</p>
</footnote>
<footnote label="9">
<p id="b545-19">. <em>Valtierra v. State, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#447" aria-description="Citation for case: Valtierra v. State">310 S.W.3d 442, 447</a></span> (Tex.Crim.App.2010); <em>Wiede v. State, </em><span class="citation" data-id="1404049"><a href="/opinion/1404049/wiede-v-state/#25" aria-description="Citation for case: Wiede v. State">214 S.W.3d 17, 25</a></span> (Tex.Crim.App.2007).</p>
</footnote>
<footnote label="10">
<p id="b545-20">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 447</a></span>-48 (quoting <em>State v. Dixon, </em><span class="citation" data-id="9620856"><a href="/opinion/1400629/state-v-dixon/#590" aria-description="Citation for case: State v. Dixon">206 S.W.3d 587, 590</a></span> (Tex.Crim.App.2006)).</p>
</footnote>
<footnote label="11">
<p id="b545-21">. U.S. Const, amend. IV.</p>
</footnote>
<footnote label="12">
<p id="b545-22">. <em>Florida v. Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#250" aria-description="Citation for case: Florida v. Jimeno">500 U.S. 248, 250</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">114 L.Ed.2d 297</a></span> (1991).</p>
</footnote>
<footnote label="13">
<p id="b545-23">. <em>Camara v. Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U.S. 523, 528-29</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">87 S.Ct. 1727</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">18 L.Ed.2d 930</a></span> (1967).</p>
</footnote>
<footnote label="14">
<p id="b546-5">. <em>Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#250" aria-description="Citation for case: Florida v. Jimeno">500 U.S. at 250-51</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>.</p>
</footnote>
<footnote label="15">
<p id="b546-6">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#448" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 448</a></span>; <em>Johnson v. State, </em><span class="citation" data-id="9729074"><a href="/opinion/2165895/johnson-v-state/" aria-description="Citation for case: Johnson v. State">226 S.W.3d 439</a></span>, 446 n. 27 (Tex.Crim.App.2007); <em>Gallups v. State, </em><span class="citation" data-id="9655220"><a href="/opinion/1577308/gallups-v-state/#201" aria-description="Citation for case: Gallups v. State">151 S.W.3d 196, 201</a></span> (Tex.Crim.App.2004).</p>
</footnote>
<footnote label="16">
<p id="b546-7">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#448" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 448</a></span>; <em>Ohio v. Robinette, </em><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U.S. 33, 39-40</a></span>, <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">117 S.Ct. 417</a></span>, <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">136 L.Ed.2d 347</a></span> (1996); <em>Gallups, </em><span class="citation" data-id="9655220"><a href="/opinion/1577308/gallups-v-state/#200" aria-description="Citation for case: Gallups v. State">151 S.W.3d at 200-01</a></span>; <em>Guevara v. State, </em><span class="citation" data-id="2188747"><a href="/opinion/2188747/guevara-v-state/#582" aria-description="Citation for case: Guevara v. State">97 S.W.3d 579, 582</a></span> (Tex.Crim.App.2003).</p>
</footnote>
<footnote label="17">
<p id="b546-8">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#448" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 448</a></span>; <em>Reasor v. State, </em><span class="citation" data-id="1580731"><a href="/opinion/1580731/reasor-v-state/#817" aria-description="Citation for case: Reasor v. State">12 S.W.3d 813, 817</a></span> (Tex.Crim.App.2000); <em>Meeks v. State, 692 </em>S.W.2d 504, 509 (Tex.Crim.App.1985).</p>
</footnote>
<footnote label="18">
<p id="b546-9">. <em>Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#251" aria-description="Citation for case: Florida v. Jimeno">500 U.S. at 251</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>.</p>
</footnote>
<footnote label="19">
<p id="b546-10">. <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#252" aria-description="Citation for case: Florida v. Jimeno"><em>Id. </em>at 252</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span> ("A suspect may of course delimit as he chooses the scope of the search to which he consents.”).</p>
</footnote>
<footnote label="20">
<p id="b546-11">. 4 Wayne R. LaFave, Search and Seizure § 8.1© at 19 (4th ed.2004).</p>
</footnote>
<footnote label="21">
<p id="b546-12">. <em>Id.</em></p>
</footnote>
<footnote label="22">
<p id="b546-16">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#449" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 449</a></span>. <em>Accord United States v. Starr, </em><span class="citation" data-id="1235169"><a href="/opinion/1235169/united-states-v-starr/#996" aria-description="Citation for case: United States v. Starr">533 F.3d 985, 996</a></span> (8th Cir.2008) ("Starr was present during the officers' full search of his home, but remained silent and made no attempt to impede their efforts or to express his concern that they were exceeding the scope of his consent. Given these facts, we conclude that a reasonable person would have believed that the officers had authority to conduct a full search of Starr’s home including his closet and a roll of film; therefore, this warrantless search did not violate the Fourth Amendment because it was authorized by Starr's consent.”).</p>
</footnote>
<footnote label="23">
<p id="b546-17">. <em>Florida v. Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#251" aria-description="Citation for case: Florida v. Jimeno">500 U.S. at 251</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>.</p>
</footnote>
<footnote label="24">
<p id="b546-18">. <em>Meekins v. State, </em><span class="citation" data-id="9784155"><a href="/opinion/2544137/meekins-v-state/#459" aria-description="Citation for case: Meekins v. State">340 S.W.3d 454, 459</a></span> (Tex.Crim.App.2011) (citing <em>Maryland </em>v. <em>Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#470" aria-description="Citation for case: Maryland v. MacOn">472 U.S. 463, 470-71</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">105 S.Ct. 2778</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">86 L.Ed.2d 370</a></span> (1985); <em>Scott v. United States, </em><span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#136" aria-description="Citation for case: Scott v. United States">436 U.S. 128, 136</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">98 S.Ct. 1717</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">56 L.Ed.2d <em>168 </em></a></span>(1978)).</p>
</footnote>
<footnote label="25">
<p id="b546-19">. <em>Meeks </em>v. <em>State, </em><span class="citation" data-id="1782139"><a href="/opinion/1782139/mccullough-v-state/#509" aria-description="Citation for case: McCullough v. State">692 S.W.2d 504, 509</a></span> (Tex.Crim.App.1985).</p>
</footnote>
<footnote label="26">
<p id="b547-4">. <em>See v. Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle">387 U.S. 541, 543</a></span>, <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">87 S.Ct. 1737</a></span>, <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">18 L.Ed.2d 943</a></span> (1967) ("The businessman, like the occupant of a residence, has a constitutional right to go about his business free from unreasonable official entries upon his private commercial property."); <em>Oliver v. United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U.S. 170</a></span>, 178 n. 8, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">104 S.Ct. 1735</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">80 L.Ed.2d 214</a></span> (1984) ("The Fourth Amendment’s protection of offices and commercial buildings, in which there may be legitimate expectations of privacy, is based upon societal expectations that have deep roots in the history of the Amendment.”).</p>
</footnote>
<footnote label="27">
<p id="b547-5">. 1 LaFave, <em>supra </em>note 20, § 2.4(b) at 627.</p>
</footnote>
<footnote label="28">
<p id="b547-6">. <em>Maryland v. Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#470" aria-description="Citation for case: Maryland v. MacOn">472 U.S. 463, 470</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">105 S.Ct. 2778</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">86 L.Ed.2d 370</a></span> (1985).</p>
</footnote>
<footnote label="29">
<p id="b547-7">. <em>United States v. Morton, </em><span class="citation" data-id="664091"><a href="/opinion/664091/united-states-v-phillip-daniel-morton/#913" aria-description="Citation for case: United States v. Phillip Daniel Morton">17 F.3d 911, 913</a></span> (6th Cir.1994) (discovery and seizure of the gun did not violate the Fourth Amendment; testimony fairly established that the auto shop was open to the public for business, so the officers lawfully entered the shop, and, when the defendant stood up, an officer saw, in plain view, a gun in defendant's back pocket).</p>
</footnote>
<footnote label="30">
<p id="b547-8">. <em>Lo-Ji Sales, Inc. v. New York, </em><span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/#329" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U.S. 319, 329</a></span>, <span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">99 S.Ct. 2319</a></span>, <span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">60 L.Ed.2d 920</a></span> (1979) (Fourth Amendment violated by sweeping search of "adult” bookstore; officers viewed films “without the payment a member of the public would be required to make,” and viewed magazines and books "not ... as a customer would ordinarily see them” by removing cellophane wrappers).</p>
</footnote>
<footnote label="31">
<p id="b547-12">. 1 LaFave, <em>supra </em>note 20 § 2.4(b) at 630. Courts have held that searches of private offices, airline baggage rooms, employee break rooms, employee locker rooms, private dressing rooms of entertainers, etc. are not sustainable on the theory of "store premises open to the public.” <em>Id. </em>(collecting cases).</p>
</footnote>
<footnote label="32">
<p id="b547-13">. <em>Illinois v. Caballes, </em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#409" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405, 409</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">160 L.Ed.2d 842</a></span> (2005) (holding that a canine sniff of an automobile need not be justified by reasonable articulable suspicion of drug activity); <em>City of Indianapolis v. Edmond, </em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#40" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32, 40</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S.Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L.Ed.2d 333</a></span> (2000) (recognizing that a canine sniff of an automobile is not a search); <em>United States v. Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place">462 U.S. 696, 706-07</a></span>, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">103 S.Ct. 2637</a></span>, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">77 L.Ed.2d 110</a></span> (1983) (holding that a canine sniff of luggage does not constitute a search). These holdings are based on the legal theory that a canine sniff by a well-trained narcotics-detection dog is not Fourth Amendment search because it reveals no information other than the location of a substance that no individual has a legitimate privacy interest in. They are all premised, however, upon a finding that the officer — and therefore the dog — have a right to be standing where they are at the time of the canine sniff.</p>
</footnote>
<footnote label="33">
<p id="b548-7">. <em>United States v. Parada, </em><span class="citation" data-id="172578"><a href="/opinion/172578/united-states-v-parada/#1282" aria-description="Citation for case: United States v. Parada">577 F.3d 1275, 1282</a></span> (10th Cir.2009).</p>
</footnote>
<footnote label="34">
<p id="b548-8">. It has been suggested that this Court should remand this case to the trial judge to enter a specific finding on a disputed fact that is dispositive to the appeal. <em>See State v. Elias, </em><span class="citation" data-id="9783708"><a href="/opinion/2539936/state-v-elias/#676" aria-description="Citation for case: State v. Elias">339 S.W.3d 667, 676</a></span> (Tex.Crim.App.2011). But here, unlike the situation in <em><span class="citation" data-id="9783708"><a href="/opinion/2539936/state-v-elias/" aria-description="Citation for case: State v. Elias">Elias</a></span>, </em>there is no disputed fact issue. There is no evidence in this record that the van backed into the workshop bay door was located in a "parking lot” or an area that was open to the general public. The State <em>argues </em>that the van was located in a public parking lot, but there is no evidence from any witness in the record that supports that argument. We need not remand this case for the trial judge to enter a finding on a fact that, based on the record, is not in dispute.</p>
</footnote>
<footnote label="35">
<p id="b548-9">. <em>Weaver, </em><span class="citation no-link">2010 WL 3518743</span>, at <em>*4, </em>2010 Tex.App. LEXIS 7425, at *9 ("Because the trial judge could have determined that Weaver's consent to search for ‘Bear’ had ended, the trial court could reasonably find that the officers, without establishing probable cause, were not entitled to search for other purposes unrelated to that of their initial search.”).</p>
</footnote>
<footnote label="36">
<p id="b548-12">. <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">160 L.Ed.2d 842</a></span> (2005).</p>
</footnote>
<footnote label="37">
<p id="b548-13">. <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#409" aria-description="Citation for case: Illinois v. Caballes"><em>Id. </em>at 409</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span>.</p>
</footnote>
<footnote label="38">
<p id="b548-14">. <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#422" aria-description="Citation for case: Illinois v. Caballes"><em>Id. </em>at 422</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span> (Ginsburg, J„ dissenting) ("Today’s decision ... clears the way for suspicionless, dog-accompanied drug sweeps of parked cars along sidewalks and in parking lots.”).</p>
</footnote>
<footnote label="39">
<p id="b548-15">. <em>United States v. Dyson, </em><span class="citation" data-id="215072"><a href="/opinion/215072/united-states-v-dyson/" aria-description="Citation for case: United States v. Dyson">639 F.3d 230</a></span>-33 (6th Cir.2011) (dog sniff of an unoccupied, parked Maxima at gas station “does not in itself require reasonable suspicion”); <em>United States v. Perez, </em><span class="citation" data-id="793575"><a href="/opinion/793575/united-states-v-jaime-perez-04-5440-walter-rhodes-05-5373/" aria-description="Citation for case: United States v. Jaime Perez (04-5440) Walter Rhodes...">440 F.3d 363</a></span> (6th Cir.2006) (dog sniff of unoccupied Tahoe, which sat in the parking lot of the hotel and was not stopped, detained or moved, was not a search or seizure; no reasonable suspicion is required when using a drug-sniffing dog); <em>United States v. Engles, </em><span class="citation" data-id="797344"><a href="/opinion/797344/united-states-v-michael-delevan-engles/#1245" aria-description="Citation for case: United States v. Michael Delevan Engles">481 F.3d 1243, 1245</a></span> (10th Cir.2007) (dog sniff of the exterior of a vehicle parked in a restaurant parking lot does not require reasonable suspicion because it is not a Fourth Amendment intrusion); <em>State v. Hobbs, </em><span class="citation" data-id="9504938"><a href="/opinion/852203/state-v-hobbs/#1286" aria-description="Citation for case: State v. Hobbs">933 N.E.2d 1281, 1286-87</a></span> (Ind.2010) (dog sniff of car in Pizza Hut lot, conducted <page-number citation-index="1" label="529">*529</page-number>under circumstances in which Hobbs was not unconstitutionally seized, not Fourth Amendment violation); <em>Dowty v. State, </em><span class="citation" data-id="9691174"><a href="/opinion/1877908/dowty-v-state/" aria-description="Citation for case: Dowty v. State">363 Ark. 1</a></span>, <span class="citation" data-id="9691174"><a href="/opinion/1877908/dowty-v-state/#854" aria-description="Citation for case: Dowty v. State">210 S.W.3d 850, 854-55</a></span> (2005) (dog sniff of Grand Am and Suburban at a Western Siz-zlin parking lot not Fourth Amendment search); <em>Myers </em>v. <em>State, </em><span class="citation" data-id="9505227"><a href="/opinion/852725/myers-v-state/#1159" aria-description="Citation for case: Myers v. State">839 N.E.2d 1154, 1159</a></span> (Ind.2005) (high-school-student defendant’s car was subject to the narcotics dog-sniff test absent reasonable particularized suspicion, as it was parked and unoccupied and the defendant was in school).</p>
</footnote>
<footnote label="40">
<p id="b549-8">. <em>Caballes, </em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#407" aria-description="Citation for case: Illinois v. Caballes">543 U.S. at 407-08</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span> ("A seizure that is justified solely by the interest in issuing a warning ticket to the driver can become unlawful if it is prolonged beyond the time reasonably required to complete that mission. In an earlier case involving a dog sniff that occurred during an unreasonably prolonged traffic stop, the Illinois Supreme Court held that use of the dog and the subsequent discovery of contraband were the product of an unconstitutional seizure. We may assume that a similar result would be warranted in this case if the dog sniff had been conducted while respondent was being unlawfully detained.”) (citation omitted).</p>
</footnote>
<footnote label="41">
<p id="b549-9">. <em>See Branch v. State, </em><span class="citation" data-id="2291162"><a href="/opinion/2291162/branch-v-state/#901" aria-description="Citation for case: Branch v. State">335 S.W.3d 893, 901</a></span> (Tex.App.-Austin 2011, no pet.) ("Given the evidence regarding the initial traffic stop and the arrival of the drug-detection dog, all of which shows that the dog arrived within eight minutes of the traffic stop and before Wing-field finished conducting normal procedures for a traffic stop, we conclude that the record supports an implied finding by the trial court that the time it took for the dog to arrive did not prolong the initial stop beyond the time reasonably required to complete the mission of the stop."); <em>Johnson v. State, </em><span class="citation" data-id="2271814"><a href="/opinion/2271814/johnson-v-state/#562" aria-description="Citation for case: Johnson v. State">323 S.W.3d 561, 562-63</a></span> (Tex.App.-Eastland 2010, pet. ref’d) (Fourth Amendment does not requires reasonable suspicion to justify using a drug-detection dog to sniff a vehicle during a legitimate traffic stop; while one officer was running a check on appellant’s driver’s license, another officer had his drug-detection dog conduct an open-air search around the vehicle, and the dog alerted on the driver’s door).</p>
</footnote>
<footnote label="42">
<p id="b549-14">. Sally port may have been an unfortunate choice of words. It literally means "1. in fortification, a postern gate, or a passage under ground from the inner to the outer works, to afford free egress to troops in making a sally, closed by massive gates when not in use. 2. a large port on each quarter of a fire ship, for the escape of the men into boats when the train is fired; also, a large port in an ironclad.” Webster’s New Twentieth Century Dictionary Unabridged 1599 (2nd ed.1983). What the officer undoubtedly meant to say was that the van was backed into a loading-dock bay at the rear of the welding workshop.</p>
</footnote>
<footnote label="43">
<p id="b550-5">. SPA's Brief at 4, 7.</p>
</footnote>
<footnote label="44">
<p id="b550-6">. The record indicates that the parking lot for the welding shop was at the front of the shop where "Bear’s” car was parked. Furthermore, it is unlikely that Mr. Weaver would be storing his "broke down” vehicles, boat, and other items in a public parking lot, and Lt. Lowrie testified that those items were out in "the back” area with the van. It is also unlikely that the general public would have access to the workshop area and loading dock of a welding shop as welding operations involve both significant fire hazards and risks due to the use and movement of heavy equipment.</p>
</footnote>
<footnote label="45">
<p id="b550-7">. <em>State </em>v. <em>Woodard, </em><span class="citation" data-id="9783836"><a href="/opinion/2540788/state-v-woodard/#410" aria-description="Citation for case: State v. Woodard">341 S.W.3d 404, 410</a></span> (Tex.Crim.App.2011).</p>
</footnote>
<footnote label="46">
<p id="b550-8">. <em>Cf. Buchanan v. State, </em><span class="citation" data-id="1466758"><a href="/opinion/1466758/buchanan-v-state/#774" aria-description="Citation for case: Buchanan v. State">129 S.W.3d 767, 774</a></span> (Tex.App.-Amarillo 2004, pet. ref'd). In that case, the trial court denied a motion to suppress, but made no findings. The court of appeals, viewing the facts in the light most favorable to the prevailing party as it was required to do, found that appellant had no legitimate expectation of privacy in the dirt driveway entrance to a business run behind his house:</p>
<blockquote id="b550-9">The time of day, the presence of no one outside the fence with whom the officers could speak, the large open gate, the presence of a well-defined dirt driveway leading through the gate to a building behind the empty house, appellant’s operation (behind the gate) of a business involving vehicles owned by third parties, the reasonable inference not only that third parties passed through the gates to obtain appellant's mechanical services but also that they were authorized to do so during normal business hours, the lack of any evidence illustrating that only appellant or certain designated individuals could drive their cars through the gate, the presence of a third party actually working on his vehicle inside the fenced lot, and the officers confining themselves to the well-defined dirt driveway are indicia upon which a trial court could reasonably find that appellant had no legitimate expectation of privacy in the dirt driveway behind the fence and that which could be perceived from it. Thus, no search occurred when the officers passed through the gate while utilizing that path and smelled the ether. Nor can we say that the trial court abused its discretion in refusing to find that the entry violated appellant’s constitutional rights.</blockquote>
<p id="b550-14"><span class="citation" data-id="1466758"><a href="/opinion/1466758/buchanan-v-state/#774" aria-description="Citation for case: Buchanan v. State"><em>Id. </em>at 774</a></span>.</p>
</footnote>
<footnote label="47">
<p id="b550-15">. SPA’s Brief at 7.</p>
</footnote>
<footnote label="48">
<p id="b551-7">. <em>Florida v. Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#251" aria-description="Citation for case: Florida v. Jimeno">500 U.S. 248, 251</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">114 L.Ed.2d 297</a></span> (1991).</p>
</footnote>
<footnote label="49">
<p id="b551-8">. <em>See State v. Bagby, </em><span class="citation" data-id="2170730"><a href="/opinion/2170730/state-v-bagby/#450" aria-description="Citation for case: State v. Bagby">119 S.W.3d 446, 450</a></span> (Tex.App.-Tyler 2003, no pet.) (officer's entry into appellee's shed was expressly limited in scope by appellee to officer’s inspection of the firearms to determine if they had been recently discharged; continuation of search of shed after inspection was finished — resulting in discovery of methamphetamine — violated scope of consent).</p>
</footnote>
<footnote label="50">
<p id="b551-9">. <span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#451" aria-description="Citation for case: Valtierra v. State">310 S.W.3d 442, 451-52</a></span> (Tex.Crim.App.2010).</p>
</footnote>
<footnote label="51">
<p id="b551-14">
<em>.Id.</em>
</p>
</footnote>
<footnote label="52">
<p id="b551-12">. <em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/" aria-description="Citation for case: Valtierra v. State">Id.</a></span></em></p>
</footnote>
<footnote label="53">
<p id="b551-13">. <em>Accord Baldwin v. State, </em><span class="citation" data-id="9627668"><a href="/opinion/1427878/baldwin-v-state/#372" aria-description="Citation for case: Baldwin v. State">278 S.W.3d 367, 372</a></span> (Tex.Crim.App.2009) ("Deputy Smith believed that appellant's answer to a question regarding the location of his identification constituted permission to retrieve that identification. We find this belief to be <em>objectively unreasonable. </em>Appellant’s response was simply an answer to the officer’s question (after being handcuffed) and not a consent for the officer to search his person.”) (emphasis added).</p>
</footnote>
</opinion>
```

---
