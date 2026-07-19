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

## GROUP: content/cases/United States v. Cano.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Cano"
type: case
citation: "934 F.3d 1002 (2019)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 9th Circuit"
court_level: coa
circuit: 9th
year: 2019
date_decided: 2019-08-16
docket: ""
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2019-08-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Cano
  varies_by_point: false
  scope_note: "Good law in-circuit; clarifies Cotterman and illustrates a circuit split with the 11th Cir. (Touset) on suspicion for border device searches."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4649091/united-states-v-miguel-cano/"
  cluster_id: 4649091
  opinion_id: 4426344
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Illustrates a circuit split"
related: ["[[United States v. Cotterman]]", "[[Riley v. California]]", "[[Carpenter v. United States]]"]
aliases: ["United States v. Miguel Cano"]
tags: ["case", "fourth-amendment", "border-search", "digital-privacy"]
holding: "Manual border searches of a cell phone need no suspicion, but a *forensic* (Cellebrite-type) device search requires reasonable suspicion…"
lake:
  record_id: United States v. Cano
  status: verified
  projected_at: 2026-07-09
---

# United States v. Cano

*934 F.3d 1002 (9th Cir. 2019)* · U.S. Court of Appeals, 9th Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At the U.S.-Mexico border, agents searched Cano's cell phone after finding cocaine in his car. They conducted a brief manual look and then a more thorough forensic-type search, recording phone numbers from the call log and photographing text messages for further investigation of the drug offense. Cano moved to suppress the phone evidence, arguing the searches exceeded the scope of the border-search exception.

## Issue
What level of suspicion the border-search exception requires for manual versus forensic cell-phone searches, and whether such searches may look for evidence of crime generally or only for digital contraband.

## Rule
The court clarified the standard and capped the scope of border phone searches: "We clarify *Cotterman* by holding that 'reasonable suspicion' in this context means that officials must reasonably suspect that the cell phone contains digital contraband. We further conclude that cell phone searches at the border, whether manual or forensic, must be limited in scope to a search for digital contraband." — slip op., at 5. ^pin-op5

Manual searches need no suspicion; forensic searches require reasonable suspicion of digital contraband; and neither may be used to hunt for evidence of crime generally. A search that goes beyond verifying the phone lacks digital contraband "exceeded the proper scope of a border search and was unreasonable as a border search under the Fourth Amendment." — [*Id.* at 29](https://www.courtlistener.com/opinion/4649091/united-states-v-miguel-cano/#:~:text=exceeded%20the%20proper%20scope%20of%20a%20border%20search%20and%20was%20unreasonable%20as%20a%20border%20search%20under%20the). ^pin-op29

## Application
Recording Cano's phone numbers and photographing his text messages sought evidence of the drug offense rather than verifying the phone was free of digital contraband such as child pornography. Because the agents' search exceeded the permissible contraband-focused scope of a border search, most of the phone evidence should have been suppressed — even though a suspicionless manual check, and a forensic check supported by reasonable suspicion of contraband, would have been permissible.

## Conclusion
Manual border phone searches need no suspicion and forensic ones require reasonable suspicion, but both are confined to searching for digital contraband; because the agents searched for evidence of crime, most of the phone evidence was suppressed and the denial of suppression was reversed in part. The border-search exception cannot justify mining a phone for case evidence.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.**
- *Cano* clarifies [[United States v. Cotterman]] (reasonable suspicion means suspicion of digital contraband) and reflects the digital-privacy concerns of [[Riley v. California]] and [[Carpenter v. United States]]. It deepens a circuit split — the Eleventh Circuit (*[[United States v. Touset]]*) requires no suspicion even for forensic border device searches.

## Appears on
- [[Border Searches]] — *Illustrates a circuit split*

## Sources
- *United States v. Cano*, 934 F.3d 1002 (9th Cir. 2019) — https://www.courtlistener.com/opinion/4649091/united-states-v-miguel-cano/ — pinpoints: slip op., at 5, 29 (CL carries the slip opinion; cluster 4649091 → opinion 4426344).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c155fecc60945c62", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "934 F.3d 1002 (2019)", "court": "U.S. Court of Appeals, 9th Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Cano", "year": "2019"}}
{"assertion_id": "40ed8ce8fa347882", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Illustrates a circuit split", "title": "United States v. Cano"}}
{"assertion_id": "47c42ba6680c064d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Manual border searches of a cell phone need no suspicion, but a *forensic* (Cellebrite-type) device search requires reasonable suspicion…", "title": "United States v. Cano"}}
{"assertion_id": "050a681c7cfa3aae", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Cano"}}
{"assertion_id": "fdb04fdb1d111d86", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2019-08-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Cano", "field_i_validity": "good_law", "scope_note": "Good law in-circuit; clarifies Cotterman and illustrates a circuit split with the 11th Cir. (Touset) on suspicion for border device searches.", "title": "United States v. Cano", "varies_by_point": "false"}}
```

### lake record — United States v. Cano

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Cano",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Miguel Cano",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Cano",
    "court": "U.S. Court of Appeals, 9th Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2019-08-16",
    "year": 2019,
    "docket": null,
    "cluster_id": 4649091,
    "lead_opinion_id": 4426344,
    "sibling_ids": [
      4426344
    ],
    "absolute_url": "/opinion/4649091/united-states-v-miguel-cano/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "934 F.3d 1002",
      "volume": "934",
      "reporter": "F.3d",
      "page": "1002",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "934 F.3d 1002",
        "volume": "934",
        "reporter": "F.3d",
        "page": "1002",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "934 F.3d 1002",
    "official_selection": {
      "court_class": "coa",
      "selected": "934 F.3d 1002",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op5",
      "page": null,
      "quote": "--- # United States v. Cano *934 F.3d 1002 (9th Cir. 2019)* \u00b7 U.S. Court of Appeals, 9th Circuit \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the U.S.-Mexico border, agents searched Cano's cell phone after finding cocaine in his car. They conducted a brief manual look and then a more thorough forensic-type search, recording phone numbers from the call log and photographing text messages for further investigation of the drug offense. Cano moved to suppress the phone evidence, arguing the searches exceeded the scope of the border-search exception. ## Issue What level of suspicion the border-search exception requires for manual versus forensic cell-phone searches, and whether such searches may look for evidence of crime generally or only for digital contraband. ## Rule The court clarified the standard and capped the scope of border phone searches:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op29",
      "page": null,
      "quote": "exceeded the proper scope of a border search and was unreasonable as a border search under the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 49689,
      "fragment": "#:~:text=exceeded%20the%20proper%20scope%20of%20a%20border%20search%20and%20was%20unreasonable%20as%20a%20border%20search%20under%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2019-08-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Cano",
    "varies_by_point": false,
    "scope_note": "Good law in-circuit; clarifies Cotterman and illustrates a circuit split with the 11th Cir. (Touset) on suspicion for border device searches.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Ahmed Alahmedalabdaloklah",
          "cluster_id": 9419050,
          "cite": [
            "94 F.4th 782"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
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
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Malik Ngumezi",
          "cluster_id": 4808091,
          "cite": [
            "980 F.3d 1285"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Aaron Holmes, Jr.",
          "cluster_id": 10273168,
          "cite": [
            "121 F.4th 727"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Haitao Xiang",
          "cluster_id": 9397097,
          "cite": [
            "67 F.4th 895"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eunice Nkongho",
          "cluster_id": 9999950,
          "cite": [
            "107 F.4th 373"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524074,
          "cite": [
            "103 F.4th 1303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Perkins",
          "cluster_id": 4761795,
          "cite": [
            "126 N.Y.S.3d 745",
            "184 A.D.3d 776",
            "2020 NY Slip Op 3425"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pendleton",
          "cluster_id": 9427220,
          "cite": [
            "537 P.3d 66"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Cano",
          "cluster_id": 4781994,
          "cite": [
            "973 F.3d 966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Carter, D.",
          "cluster_id": 10663183,
          "cite": [
            "2025 Pa. Super. 190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524075,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ahmed Alahmedalabdaloklah",
          "cluster_id": 9479199,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Graham v. District Attorney for the Hampden District",
          "cluster_id": 9468079,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cameron v. District of Columbia",
          "cluster_id": 7860641,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alasaad v. Wolf",
          "cluster_id": 4855246,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cano:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4426344) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
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
        "query": "cites:(4426344)",
        "reviewed": 17,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 16,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4426344)",
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
    "complete_query": "cites:(4426344)",
    "indexed_citing_opinions": 17,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4426344,
        "count": 17,
        "count_source": "search"
      }
    ],
    "citation_count": 42,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-cano.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 17,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4426344,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 145497,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 145639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 175207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 186862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 218926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 219828,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 273246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 307684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 365940,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 366062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 456285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 518930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 558564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 558592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 580904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 687686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 692307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 749834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 782323,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 788746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 789362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 858288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 1225723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 1468715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4426344,
        "cited_id": 2500363,
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
    "date_created": "2026-07-05T22:55:54Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:56:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:56:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:59:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:56:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Cano

```
                      FOR PUBLICATION

    UNITED STATES COURT OF APPEALS
         FOR THE NINTH CIRCUIT


 UNITED STATES OF AMERICA,                    No. 17-50151
           Plaintiff-Appellee,
                                               D.C. No.
                 v.                      3:16-cr-01770-BTM-1

 MIGUEL ANGEL CANO,
        Defendant-Appellant.                    OPINION


       Appeal from the United States District Court
          for the Southern District of California
      Barry Ted Moskowitz, District Judge, Presiding

            Argued and Submitted April 10, 2019
                   Pasadena, California

                       Filed August 16, 2019

Before: Susan P. Graber and Jay S. Bybee, Circuit Judges,
        and M. Douglas Harpool,* District Judge.

                      Opinion by Judge Bybee




     *
       The Honorable M. Douglas Harpool, United States District Judge
for the Western District of Missouri, sitting by designation
2                    UNITED STATES V. CANO

                            SUMMARY**


                            Criminal Law

    The panel reversed the district court’s order denying the
defendant’s motion to suppress evidence obtained from
warrantless searches of his cell phone by Customs and Border
Protection officials, and vacated his conviction for importing
cocaine.

    Applying United States v. Cotterman, 709 F.3d 952 (9th
Cir. 2013) (en banc), the panel held that manual cell phone
searches may be conducted by border officials without
reasonable suspicion but that forensic cell phone searches
require reasonable suspicion. The panel clarified Cotterman
by holding that “reasonable suspicion” in this context means
that officials must reasonably suspect that the cell phone
contains digital contraband. The panel further concluded that
cell phone searches at the border, whether manual or forensic,
must be limited in scope to whether the phone contains digital
contraband; and that a broader search for evidence of a crime
cannot be justified by the purposes of the border search
exception to the Fourth Amendment warrant requirement.

    The panel held that to the extent that a Border Patrol
agent’s search of the defendant’s phone – which included the
recording of phone numbers and text messages for further
processing – went beyond a verification that the phone lacked
digital contraband, the search exceeded the proper scope of a
border search and was unreasonable as a border search under

    **
       This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                  UNITED STATES V. CANO                       3

the Fourth Amendment. The panel held that although the
agents had reason to suspect the defendant’s phone would
contain evidence leading to additional drugs, the record does
not give rise to an objectively reasonable suspicion that the
digital data in the phone contained contraband, and the border
search exception therefore did not authorize the agents to
conduct a warrantless forensic search of the defendant’s
phone. The panel held that the good faith exception to the
exclusionary rule does not apply because the border officials
did not rely on binding appellate precedent specifically
authorizing the cell phone searches at issue here.

    Rejecting the defendant’s contention that the government
violated his rights under Brady v, Maryland, 373 U.S. 83
(1963), and Fed. R. Crim. P. 16, by failing to turn over certain
information he requested from the FBI and DEA in pursuit of
this third-party defense, the panel found no evidence that the
prosecution had knowledge or possession of evidence
showing that the defendant’s cousin or his cousin’s gang were
involved in drug trafficking at the Mexico-California border,
and held that the prosecutor should not be held to have
“access” to any information that an agency not involved in
the investigation or prosecution of the case refuses to turn
over.
4                 UNITED STATES V. CANO

                        COUNSEL

Harini P. Raghupathi (argued), Federal Defenders of San
Diego, Inc., San Diego, California, for Defendant-Appellant.

Mark R. Rehe (argued), Assistant United States Attorney;
Helen H. Hong, Assistant United States Attorney, Chief,
Appellate Section, Criminal Division; Adam L. Braverman,
United States Attorney; United States Attorney’s Office, San
Diego, California; for Plaintiff-Appellee.

Sophia Cope and Adam Schwartz, Electronic Frontier
Foundation, San Francisco, California, for Amicus Curiae
Electronic Frontier Foundation.


                         OPINION

BYBEE, Circuit Judge:

    Defendant-Appellant Miguel Cano was arrested for
carrying cocaine as he attempted to cross into the United
States from Mexico at the San Ysidro Port of Entry.
Following his arrest, a Customs and Border Protection
official seized Cano’s cell phone and searched it, first
manually and then using software that accesses all text
messages, contacts, call logs, media, and application data.
When Cano moved to suppress the evidence obtained from
the warrantless searches of his cell phone, the district court
held that the searches were valid under the border search
exception to the Fourth Amendment’s warrant requirement.

    Applying United States v. Cotterman, 709 F.3d 952 (9th
Cir. 2013) (en banc), we conclude that manual cell phone
                  UNITED STATES V. CANO                     5

searches may be conducted by border officials without
reasonable suspicion but that forensic cell phone searches
require reasonable suspicion. We clarify Cotterman by
holding that “reasonable suspicion” in this context means that
officials must reasonably suspect that the cell phone contains
digital contraband. We further conclude that cell phone
searches at the border, whether manual or forensic, must be
limited in scope to a search for digital contraband. In this
case, the officials violated the Fourth Amendment when their
warrantless searches exceeded the permissible scope of a
border search. Accordingly, we hold that most of the
evidence from the searches of Cano’s cell phone should have
been suppressed. We also conclude that Cano’s Brady claims
are unpersuasive. Because we vacate Cano’s conviction, we
do not reach his claim of prosecutorial misconduct.

   We reverse the district court’s order denying Cano’s
motion to suppress and vacate Cano’s conviction.

                 I. THE BACKGROUND

A. The Facts

    Defendant-Appellant Miguel Cano worked in the flooring
and carpet installation trade and lived with his wife and
children in the Mission Hills community north of Los
Angeles. In the summer of 2016, however, Cano moved from
Los Angeles to Tijuana, Mexico, where he stayed with his
cousin Jose Medina. While staying with Medina, Cano
crossed the border into the United States six times, sometimes
remaining in the United States for less than thirty minutes.
On two of those trips, Cano was referred to secondary
inspection, but no contraband was found.
6                 UNITED STATES V. CANO

    On July 25, 2016, Cano arrived at the San Ysidro Port of
Entry from Tijuana. In primary inspection, Cano stated that
“he was living in Mexico, working in San Diego, but going to
LA on that day.” Pursuant to a random Customs and Border
Protection (CBP) computer referral, Cano was referred to
secondary inspection, where a narcotic-detecting dog alerted
to the vehicle’s spare tire. A CBP official removed the spare
tire from the undercarriage of the truck and discovered 14
vacuum-sealed packages inside, containing 14.03 kilograms
(30.93 pounds) of cocaine.

    Cano was arrested, and a CBP official administratively
seized his cell phone. The CBP officials called Homeland
Security Investigations (HSI), which dispatched Agents
Petonak and Medrano to investigate. After arriving, Agent
Petonak “briefly” and manually reviewed Cano’s cell phone,
noticing a “lengthy call log” but no text messages. Agent
Petonak later stated that the purpose of this manual search
was “two-pronged”: “to find some brief investigative leads in
the current case,” and “to see if there’s evidence of other
things coming across the border.”

    Agent Petonak proceeded to question Cano, who waived
his Miranda rights and agreed to talk. During that interview,
Cano denied any knowledge of the cocaine. Cano stated that
he had moved to Tijuana to look for work in nearby San
Diego, because work was slow in Los Angeles. He also said
he had crossed the border every day for the previous three
weeks looking for work. He told Agent Petonak that he was
headed to a carpet store in Chula Vista that day to seek work.
When pressed, Cano was not able to provide the name or
address of the store, claiming that he intended to look it up on
Google after crossing the border. Cano also explained that he
did not have his flooring tools with him in his pickup truck so
                  UNITED STATES V. CANO                      7

as to avoid problems with border crossings; Cano intended to
drive to Los Angeles to retrieve his tools if he located work
in San Diego.

    During the interrogation, Agent Petonak specifically
asked Cano about the lack of text messages on his cell phone.
Cano responded that his cousin had advised him to delete his
text messages “just in case” he got pulled over in Mexico and
police were to check his cell phone. Cano stated that he
erased his messages to avoid “any problems” with the
Mexican police.

    While Agent Petonak questioned Cano, Agent Medrano
conducted a second manual search of the cell phone. Agent
Medrano browsed the call log and wrote down some of the
phone numbers on a piece of paper. He also noticed two
messages that arrived after Cano had reached the border, and
he took a photograph of the messages. The first message
stated, “Good morning,” and the second message stated,
“Primo, are you coming to the house?” Agent Medrano gave
all of this information—the recorded list of calls and the
photograph—to Agent Petonak.

    Finally, Agent Medrano conducted a “logical download”
of the phone using Cellebrite software. A Cellebrite search
enables the user to access text messages, contacts, call logs,
media, and application data on a cell phone and to select
which types of data to download. It does not, however, allow
the user to access data stored within third-party applications.
Agent Medrano typically does not select the option to
download photographs.

    After Agent Petonak interviewed Cano, he reviewed the
results of the Cellebrite download of Cano’s phone by Agent
8                    UNITED STATES V. CANO

Medrano. The Cellebrite results revealed that Cano had sent
no text messages, and it listed all the calls made by Cano.
Agent Petonak later concluded that none of the phone
numbers in the call log corresponded to carpeting stores in
San Diego.

B. The Proceedings

     Cano was indicted for importing cocaine. Before trial,
Cano moved to suppress any evidence obtained from Agents
Petonak and Medrano’s warrantless searches of his cell phone
at the border. The district court denied Cano’s motion, ruling
that the manual searches and the Cellebrite search of Cano’s
phone were valid border searches. During trial, the
government introduced evidence that resulted from the
manual searches of the phone and from Agent Medrano’s
Cellebrite download of the phone.1

    In preparation for trial, Cano indicated his intent to
present a third-party culpability defense claiming that his
cousin, Jose Medina, was responsible for placing the drugs in
Cano’s spare tire without Cano’s knowledge. Cano proffered
evidence that Medina had a key to Cano’s car and had driven
it shortly before Cano’s attempted border crossing, that


    1
         Some—but not all—of the evidence was available through
alternative channels. For example, the government introduced a call log,
unchallenged by Cano, that the government received from Cano’s phone
company. Similarly, the government later obtained a warrant to search the
phone, and an agent conducted further searches. Because the government
introduced at trial much evidence pre-dating those events, and because the
government has not argued that any Fourth Amendment error was
harmless, those later events do not affect our Fourth Amendment analysis
of the warrantless searches. United States v. Rodriguez, 880 F.3d 1151,
1163 (9th Cir. 2018)
                  UNITED STATES V. CANO                      9

Medina had a criminal record including a conviction for
cocaine possession, that Medina was a member of a Chicago-
based gang called the Latin Kings, and that the Latin Kings
sold cocaine within the United States and were involved with
a cartel that trafficked drugs across the border.

     Following Cano’s implication of Medina, the government
contacted Medina and promised him immunity and
immigration papers in exchange for his cooperation. Medina
initially denied being involved with drugs, but later contacted
the government on his own and offered to help them with the
“biggest RICO case” and “drug seizures of 20 to 25
kilograms at a time.” All of this information was made
available to Cano.

    As part of his defense, Cano sought additional discovery
from HSI, the Federal Bureau of Investigation (FBI), and the
Drug Enforcement Agency (DEA) regarding: (1) records
linking Medina to drug sales, distribution, or trafficking; and
(2) records linking the Latin Kings to drug trafficking from
Mexico to Southern California. The government opposed
Cano’s discovery motion, arguing that the evidence was not
material under Federal Rule of Criminal Procedure
16(a)(1)(E)(i) and that discovery should be limited to HSI, as
neither the DEA nor the FBI had participated in the
investigation of Cano. The district court originally overruled
both objections, finding the evidence material under Rule 16
and exculpatory under Brady v. Maryland, 373 U.S. 83
(1963). The court also reasoned that, because HSI could
inquire of the DEA and FBI if it sought inculpatory evidence,
HSI had access to the files and was required to provide any
exculpatory evidence held by the DEA or FBI.
10                   UNITED STATES V. CANO

    In response to the court’s discovery order, HSI produced
Medina’s immigration file and his Bureau of Prisons record.
Agent Petonak also searched for Medina’s name in two
different police clearinghouses, but neither returned any hits.2
Both Agent Petonak and the United States Attorney’s Office
(USAO) subsequently requested information showing a link
between the Latin Kings and drug trafficking from Mexico
from the legal counsel of both the FBI and DEA. Both
agencies denied the requests without providing any
explanation or any indication as to whether the requested
information existed.

    Following these attempts, the government moved for the
district court to reconsider its discovery order and excuse it
from discovery relating to files held by the FBI and DEA.
The district court granted the motion to reconsider, finding
that the prosecutor did not have access to the evidence when
he was “rebuffed” by agencies over which he had no control.

    The case proceeded to trial and Cano presented his third-
party culpability defense. The first trial resulted in a hung
jury and a mistrial. On retrial, Cano again relied on his third-
party culpability defense. The second trial resulted in Cano’s
conviction. This appeal followed, in which Cano raises three
issues: (1) whether the warrantless searches of his cell phone
violated the Fourth Amendment and whether the resulting
evidence should be suppressed; (2) whether the government’s
non-disclosure of materials that may have been held by the
DEA and FBI violated his right to due process under Brady


     2
       A police clearinghouse works for the purpose of “deconfliction” by
notifying an agency if another agency has an investigation pending against
the same person or item. The DEA and FBI participate in the two
clearinghouses searched by Agent Petonak.
                    UNITED STATES V. CANO                         11

and Federal Rule of Criminal Procedure 16; and (3) whether
the government raised an improper propensity inference in its
closing argument. We address Cano’s first two arguments in
turn. Because we conclude that the district court erred in
denying Cano’s motion to suppress, we vacate Cano’s
conviction and do not reach his claim of prosecutorial
misconduct.

    II. THE WARRANTLESS SEARCH OF CANO’S
                 CELL PHONE

    The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures.” U.S. Const.
amend. IV.3 Ordinarily, before conducting a search, police
must obtain a warrant issued by a judicial officer based “upon
probable cause, supported by Oath or affirmation, and
particularly describing the place to be searched, and the
persons or things to be seized.” Id. Warrants are generally
required “unless ‘the exigencies of the situation’ make the
needs of law enforcement so compelling that the warrantless
search is objectively reasonable under the Fourth
Amendment.” Mincey v. Arizona, 437 U.S. 385, 393–94
(1978) (citation omitted). Consequently, “searches conducted
outside the judicial process, without prior approval by judge
or magistrate, are per se unreasonable under the Fourth
Amendment—subject only to a few specifically established
and well-delineated exceptions.” Katz v. United States, 389
U.S. 347, 357 (1967) (footnote omitted). Such “specifically
established and well-delineated exceptions” include exigent


    3
       We review de novo “the district court’s determination that [a]
warrantless search . . . was a valid border search.” United States v.
Cardona, 769 F.2d 625, 628 (9th Cir. 1985).
12                UNITED STATES V. CANO

circumstances, searches incident to arrest, vehicle searches,
and border searches. See Arizona v. Gant, 556 U.S. 332, 343
(2009) (vehicle searches); Brigham City v. Stuart, 547 U.S.
398, 403 (2006) (exigent circumstances; listing other
exceptions, including warrantless entry to fight a fire, to
prevent the imminent destruction of evidence, or in “hot
pursuit” of a fleeing suspect); United States v. Ramsey, 431
U.S. 606, 616 (1977) (border searches); Weeks v. United
States, 232 U.S. 383, 392 (1914) (searches incident to arrest),
overruled in part on other grounds by Mapp v. Ohio, 367
U.S. 643 (1961).

    Exceptions to the warrant requirement are subject to two
important constraints. First, any search conducted under an
exception must be within the scope of the exception. Second,
some searches, even when conducted within the scope of the
exception, are so intrusive that they require additional
justification, up to and including probable cause and a
warrant.

    The first constraint is illustrated by the Supreme Court’s
decision in Riley v. California, 573 U.S. 373 (2014), a case
involving the search incident to arrest exception. In Riley, the
Court addressed “whether the police may, without a warrant,
search digital information on a cell phone seized from an
individual who has been arrested”; in other words, whether
cell phones fell within the scope of the search incident to
arrest exception. Id. at 378. The Court began by recognizing
the increasing role in our lives of “minicomputers that also
happen to have the capacity to be used as a telephone”;
“[m]odern cell phones, as a category, implicate privacy
concerns far beyond those implicated by the search of a
cigarette pack, a wallet, or a purse.”            Id. at 393.
Acknowledging that “it has been well accepted that [a search
                  UNITED STATES V. CANO                      13

incident to lawful arrest] constitutes an exception to the
warrant requirement,” id. at 382, the Court pointed out that
such searches serve two purposes: (1) to secure “the officer’s
safety” and (2) to “prevent . . . concealment or destruction [of
evidence],” id. at 383 (citation omitted). The Court then
considered whether a cell phone search qualified as a search
incident to arrest by considering “whether application of the
search incident to arrest doctrine to [cell phones] would
‘untether the rule from the justifications underlying the . . .
exception.’” Id. at 386 (quoting Gant, 556 U.S. at 343).

     The Court concluded that neither purpose for the search
incident to arrest exception justified the search of a cell
phone. The Court rejected the government’s argument that
searching a cell phone incident to arrest would “help ensure
officer safety in . . . indirect ways, for example by alerting
officers that confederates of the arrestee are headed to the
scene.” Id. at 387. The Court reasoned that the government’s
position “would . . . represent a broadening” of the
exception’s foundational concern that “an arrestee himself
might grab a weapon and use it against an officer.” Id. at
387–88. The Court observed that “once law enforcement
officers have secured a cell phone, there is no longer any risk
that the arrestee himself will be able to delete incriminating
data from the phone,” id. at 388, and police have means to
ensure that data cannot be wiped from the phone remotely,
id. at 390. The Court concluded “not that the information on
a cell phone is immune from search; [but rather] that a
warrant is generally required before such a search, even when
a cell phone is seized incident to arrest.” Id. at 401.

    The second constraint on warrantless searches is
illustrated by the Court’s decision in United States v.
Montoya de Hernandez, 473 U.S. 531 (1985). Montoya was
14                UNITED STATES V. CANO

stopped at Los Angeles International Airport and referred to
secondary inspection. Id. at 533. She had arrived from
Bogota and was carrying $5,000 in cash. Id. She had no
credit cards and no hotel reservations. Id. at 533–34.
Because border officials suspected that Montoya may have
swallowed cocaine-filled balloons, Montoya was held in the
customs office and, after a magistrate judge issued an order,
taken to a hospital for a rectal examination. Id. at 534–35.
Over the next four days, she passed 88 balloons containing
cocaine. Id. at 536. Montoya argued that the search she was
subjected to, though a border search, was so intrusive that it
could not be conducted without a high level of particularized
suspicion. Id. at 536–37, 540. The Court balanced her
privacy interests against the interests of the government at the
border and concluded that, while routine searches may be
conducted at the border without any showing of suspicion, a
more intrusive, nonroutine search must be supported by
“reasonable suspicion.” Id. at 537–41; see also United States
v. Flores-Montano, 541 U.S. 149, 152 (2004) (suggesting that
nonroutine searches are limited to “highly intrusive searches
of the person” involving “dignity and privacy interests”).

    Cano recognizes that he was subject to search at the
border, but Cano and amicus Electronic Frontier Foundation
(“EFF”) raise two categorical challenges and one as-applied
challenge to the searches conducted here. First, EFF argues
that any warrantless search of a cell phone falls outside the
scope of the border search exception. Second, EFF argues
that even if the search is within the scope of the border search
exception, a warrantless cell phone search is so intrusive that
it requires probable cause. We address these categorical
challenges in Part II.A. Third, Cano asserts that, even if cell
phones are generally subject to search at the border, the
manual and forensic searches of his cell phone exceeded the
                  UNITED STATES V. CANO                    15

“well delineated” scope of the border search. We address this
as-applied question in Part II.B. Finally, the government
argues that even if the border search exceeded the limits of
the Fourth Amendment, the search was conducted in good
faith, and the evidence is admissible. We consider the good
faith exception in Part II.C.

A. Border Searches and Cell Phones

    “[B]order searches constitute a ‘historically recognized
exception to the Fourth Amendment’s general principle that
a warrant be obtained.’” Cotterman, 709 F.3d at 957 (quoting
Ramsey, 431 U.S. at 621). Indeed, border searches typically
do not require any particularized suspicion, so long as they
are “routine inspections and searches of individuals or
conveyances seeking to cross our borders.” Almeida-Sanchez
v. United States, 413 U.S. 266, 272 (1973); see United States
v. Seljan, 547 F.3d 993, 999 (9th Cir. 2008) (en banc). Such
searches are “reasonable simply by virtue of the fact they
occur at the border.” Ramsey, 431 U.S. at 616. The
exception is “rooted in ‘the long-standing right of the
sovereign to protect itself by stopping and examining persons
and property crossing into this country,’” Cotterman, 709
F.3d at 960 (quoting Ramsey, 431 U.S. at 616), to “prevent[]
the entry of unwanted persons and effects,” id. (quoting
Flores-Montano, 541 U.S. at 152).

    The sovereign’s right to conduct suspicionless searches at
the border “does not mean, however, that at the border
‘anything goes.’” Id. (quoting Seljan, 547 F.3d at 1000).
Rather, the border search exception is a “narrow exception”
that is limited in two important ways. Id. (citation omitted).
First, “[t]he authorizing statute limits the persons who may
legally conduct a ‘border search’ to ‘persons authorized to
16                    UNITED STATES V. CANO

board or search vessels.’” United States v. Soto-Soto, 598
F.2d 545, 549 (9th Cir. 1979) (citing 19 U.S.C. § 482).4 This
includes customs and immigration officials, but not general
law enforcement officers such as FBI agents. Id.; see United
States v. Diamond, 471 F.2d 771, 773 (9th Cir. 1973) (stating
that “customs agents are not general guardians of the public
peace”). Second, a border search must be conducted “in
enforcement of customs laws.” Soto-Soto, 598 F.2d at 549.
A border search must be conducted to “enforce importation
laws,” and not for “general law enforcement purposes.” Id.


     4
         Section 482 now reads in relevant part:

               Any of the officers or persons authorized to board
          or search vessels may stop, search, and examine . . . any
          vehicle, beast, or person, on which or whom he or they
          shall suspect there is merchandise which is subject to
          duty, or shall have been introduced into the United
          States in any manner contrary to law . . . . [and may]
          seize and secure the same for trial.

19 U.S.C. § 482(a); see id. § 1467 (“[T]he appropriate customs officer for
[a] port or place of arrival may . . . enforce, cause inspection, examination,
and search to be made of the persons, baggage, and merchandise
discharged or unladen from [an arriving] vessel . . . .”); id. § 1496 (“The
appropriate customs officer may cause an examination to be made of the
baggage of any persons arriving in the United States in order to ascertain
what articles are contained therein and whether subject to duty, free of
duty, or prohibited . . . .”); id. § 1582 (“[A]ll persons coming into the
United States from foreign countries shall be liable to detention and search
by authorized officers or agents . . . .”).

     The Court has described § 482 as granting the executive “plenary
authority to conduct routine searches and seizures at the border, without
probable cause or a warrant.” Montoya de Hernandez, 473 U.S. at 537.
We have held that the “outer limits of authority delegated by [§ 482 are]
available only in border searches.” Corngold v. United States, 367 F.2d
1, 3 (9th Cir. 1966) (en banc).
                  UNITED STATES V. CANO                       17

A general search cannot be “justif[ied] . . . on the mere basis
that it occurred at the border.” Id. (affirming the suppression
of evidence where an FBI agent stopped and searched the
vehicle of an alien to determine whether the car had been
stolen).

    1. Cell Phone Data as Contraband

    As we discussed briefly above, the Supreme Court has
identified two principal purposes behind warrantless border
searches: First, to identify “[t]ravellers . . . entitled to come
in” and, second, to verify their “belongings as effects which
may be lawfully brought in.” Carroll v. United States, 267
U.S. 132, 154 (1925); see Ramsey, 431 U.S. at 620 (“The
border-search exception is grounded in the recognized right
of the sovereign to control . . . who and what may enter the
country.”).

    EFF argues that applying the border search exception to
a cell phone’s data would “untether” the exception from the
purposes underlying it. EFF contends that a border search
encompasses only a search for illegal persons and physical
contraband located on the body of the applicant for
admission or among his effects. Because digital data on a cell
phone cannot conceal objects such as drugs, guns, or
smuggled persons, EFF asserts that digital cell phone
searches are always beyond the scope of the border search
exception.

    We agree with EFF that the purpose of the border search
is to interdict contraband, but we disagree with its premise
that cell phones cannot contain contraband. Although cell
18                   UNITED STATES V. CANO

phone data cannot hide physical objects,5 the data can contain
digital contraband. The best example is child pornography.
See United States v. Molina-Isidoro, 884 F.3d 287, 295 n.3
(5th Cir. 2018) (Costa, J., specially concurring) (“One type of
contraband that can be stored within the data of a cell
phone . . . is child pornography.”). And because cell phones
may ultimately be released into the interior, even if the owner
has been detained, the United States has a strong interest in
preventing the entry of such material. See, e.g., United States
v. Vergara, 884 F.3d 1309, 1311 (11th Cir.) (describing how
agents returned one of the defendant’s phones to a family
member after defendant had been arrested for possessing
child pornography on his other two phones), cert. denied, 139
S. Ct. 70 (2018). We find no basis for the proposition that the
border search exception is limited to searching for physical
contraband. At the very least, a cell phone that has photos
stored on it is the equivalent of photographs, magazines, and
books.6 See Riley, 573 U.S. at 394; Cotterman, 709 F.3d at
964. The contents may be digital when they are on the phone,
but the physicality of the phone itself and the possibility that


     5
        No one contests that a border official could, consistent with the
Fourth Amendment, examine the physical body of a cell phone to see if
the phone itself is contraband—because, for example, it is a pirated copy
of a patented U.S. phone—or if the phone itself presents a physical threat
to officers. See Riley, 573 U.S. at 387 (“Law enforcement officers remain
free to examine the physical aspects of a phone to ensure that it will not
be used as a weapon—say, to determine whether there is a razor blade
hidden between the phone and its case.”). The dispute here concerns only
whether border officials may search the digital data contained within the
phone.
     6
     We need not address here questions surrounding the use of “cloud
computing,” where the phone gives access to, but does not contain in its
own memory, digital data stored in the cloud. See Riley, 573 U.S. at
397–98; Cotterman, 709 F.3d at 965 & n.12.
                    UNITED STATES V. CANO                            19

the phone’s contents can be printed or shared electronically
gives border officials sufficient reason to inspect it at the
border. We conclude that cell phones—including the phones’
data—are subject to search at the border.

    2. Forensic Cell Phone Searches as an Intrusive Search

    The second question we must address in response to
amicus EFF is whether forensic searches of a cell phone are
so intrusive that they require reasonable suspicion or even
probable cause. We answered this question in our en banc
decision in Cotterman, but with respect to laptop computers.7
Cotterman, 709 F.3d at 962–68. Cotterman was a United
States citizen returning to the United States from Mexico. Id.
at 957. When he reached the port of entry, border officials
noted that Cotterman had various convictions for sexual
conduct with children. Id. Concerned that Cotterman might
be involved in child sex tourism, officials conducted a brief
search of his laptop computers and digital cameras and noted
that the laptops had password-protected files. Id. at 958. The
officials detained the computers for several days in order to
run a comprehensive forensic search of the hard drive, which
revealed hundreds of images of child pornography. Id. at
958–59. For us, “the legitimacy of the initial search of
Cotterman’s electronic devices at the border [was] not in
doubt,” id. at 960, “[t]he difficult question . . . [was] the
reasonableness, without a warrant, of the forensic



    7
      Although Cotterman referred to “electronic devices” generally, see
709 F.3d at 962–68, our holding was limited to the “examination of
Cotterman’s computer,” id. at 968, and did not address cell phones. We
mentioned cell phones only once—in the first paragraph of the
introduction describing the modern “digital world.” Id. at 956.
20                UNITED STATES V. CANO

examination that comprehensively analyzed the hard drive of
the computer,” id. at 961.

    We acknowledged the “substantial personal privacy
interests” in “[e]lectronic devices . . . capable of storing
warehouses full of information.” Id. at 964. At the same
time, we recognized “the important security concerns that
prevail at the border” and the legitimacy of “[t]he effort to
interdict child pornography.” Id. at 966. We held that a
routine, manual search of files on a laptop computer—“a
quick look and unintrusive search”—is reasonable “even
without particularized suspicion,” but that officials must
“possess a particularized and objective basis for suspecting
the person stopped of criminal activity” to engage in a
forensic examination, which is “essentially a computer strip
search.” Id. at 960–61, 966, 967 (citation omitted). We
concluded that reasonable suspicion was “a modest, workable
standard that is already applied in the extended border search,
Terry stop, and other contexts.” Id. at 966; see id. at 968
(defining reasonable suspicion as “a particularized and
objective basis for suspecting the particular person stopped of
criminal activity” (quoting United States v. Cortez, 449 U.S.
411, 417–18 (1981))).

    We think that Cotterman’s reasoning applies equally to
cell phones. In large measure, we anticipated the Supreme
Court’s reasoning in Riley, 573 U.S. at 393–97, when we
recognized in Cotterman that digital devices “contain the
most intimate details of our lives” and “the uniquely sensitive
nature of data on electronic devices carries with it a
significant expectation of privacy,” Cotterman, 709 F.3d at
965–66; see Riley, 573 U.S. at 385, 393 (describing cell
phones as “a pervasive and insistent part of daily life” that,
“as a category, implicate privacy concerns far beyond those
                      UNITED STATES V. CANO                               21

implicated by the search of a cigarette pack, a wallet, or a
purse”). The Court’s view of cell phones in Riley so closely
resembles our own analysis of laptop computers in Cotterman
that we find no basis to distinguish a forensic cell phone
search from a forensic laptop search.8

    Nor do we believe that Riley renders the Cotterman
standard insufficiently protective. Riley, of course, held that
“a warrant is generally required” before searching a cell
phone, “even when a cell phone is seized incident to arrest.”
573 U.S. at 401. But here we deal with the border search
exception—not the search incident to arrest exception—and
the difference in context is critical. In light of the
government’s enhanced interest in protecting the “integrity of
the border” and the individual’s decreased expectation of
privacy, the Court has emphasized that “the Fourth
Amendment’s balance of reasonableness is qualitatively
different at the international border than in the interior” and
is “struck much more favorably to the Government.”
Montoya de Hernandez, 473 U.S. at 538–40. As a result,
post-Riley, no court has required more than reasonable
suspicion to justify even an intrusive border search. See
United States v. Wanjiku, 919 F.3d 472, 485 (7th Cir. 2019)
(“[N]o circuit court, before or after Riley, has required more
than reasonable suspicion for a border search of cell phones
or electronically-stored data.”); Touset, 890 F.3d at 1234

    8
        We note that the Eleventh Circuit disagreed with Cotterman in
United States v. Touset, 890 F.3d 1227, 1234 (11th Cir. 2018). The court
held that no level of suspicion was required to conduct a forensic search
of a cell phone. Id. at 1234–35. Nevertheless, the Touset court held, in
the alternative, that the forensic search of various electronic devices seized
at the border were supported by reasonable suspicion. Id. at 1237. As
with most cell phone search cases, in Touset border agents were looking
for child pornography.
22                UNITED STATES V. CANO

(“Riley, which involved the search-incident-to-arrest
exception, does not apply to searches at the border.”);
Molina-Isidoro, 884 F.3d at 291 (“For border searches both
routine and not, no case has required a warrant.”); id. at 293
(“The bottom line is that only two of the many federal cases
addressing border searches of electronic devices have ever
required any level of suspicion. They both required only
reasonable suspicion and that was for the more intrusive
forensic search.”); see also Kolsuz, 890 F.3d 133, 137 (4th
Cir. 2018) (concluding that a “forensic examination of
Kolsuz’s phone must be considered a nonroutine border
search, requiring some measure of individualized suspicion”
but declining to decide whether the standard should be
reasonable suspicion or probable cause).

     Accordingly, we hold that manual searches of cell phones
at the border are reasonable without individualized suspicion,
whereas the forensic examination of a cell phone requires a
showing of reasonable suspicion. See Cotterman, 709 F.3d
at 968.

B. The Searches of Cano’s Cell Phone and the Scope of the
   Border Search Exception

    Having concluded that border officials may conduct
suspicionless manual searches of cell phones, but must have
reasonable suspicion before they conduct a forensic search,
we still must address the core of Cano’s argument: whether
the manual and forensic searches of his cell phone were not
searches for digital contraband, but searches for evidence of
a crime, and thus exceeded the proper scope of a border
search.
                     UNITED STATES V. CANO                             23

    1. The Border Exception and the Search for Contraband

    As a threshold matter, Cano argues that border searches
are limited in both purpose and scope to searches for
contraband.9 In response, the government argues that
searches for evidence that would aid in prosecuting past and
preventing future border-related crimes are tethered to the
purpose of the border search exception—namely, interdicting
foreign contraband—and thus fall within its scope.




    9
       Cano emphasizes that the officials who arrested him were looking
for evidence of a crime, not contraband that could be seized at the border,
and this renders the search unconstitutional. He points to Officers Petonak
and Medrano, who searched Cano’s cell phone, and who testified that their
searches had a dual purpose: “to find some brief investigative leads in the
current case” and “to see if there[] [was] evidence of other things coming
across the border.” Because the agents acknowledged that they sought
evidence to use against Cano in building a criminal case, Cano argues that
the court should treat the search as one conducted for “general law
enforcement purposes” rather than a border search.

     Cano’s focus on the officials’ subjective motivations is misplaced,
however. As the district court recognized, “courts have repeatedly held
that the Fourth Amendment’s reasonableness analysis is ‘predominantly
an objective inquiry.’” See Whren v. United States, 517 U.S. 806, 813
(1996) (upholding a “pretextual” stop because “[s]ubjective intentions
play no role in ordinary . . . Fourth Amendment analysis”). We have
upheld border searches of persons seeking entry even when those searches
were conducted “at the behest” of DEA agents seeking criminal evidence.
See United States v. Schoor, 597 F.2d 1303, 1305–06 (9th Cir. 1979)
(holding a border search reasonable where it was conducted “at the
behest” of DEA agents and included a search for certain items of evidence
in addition to a search for contraband). Thus, the mere fact that Officers
Petonak and Medrano subjectively hoped to find “investigative leads”
pertaining to the seized shipment of cocaine does not render their searches
of Cano’s phone beyond the border search exception.
24                UNITED STATES V. CANO

    This is a close question, but we think Cano has the better
of the argument. There is a difference between a search for
contraband and a search for evidence of border-related
crimes, although the distinction may not be apparent.
Cotterman helps us focus on the difference. There, border
officials had been alerted that Cotterman had a criminal
record of sex abuse of minors and might be involved in “child
sex tourism.” Cotterman, 709 F.3d at 957. The officials
seized his laptop and subjected it to searches for child
pornography, which they found. In Cotterman, the child
pornography was contraband subject to seizure at the border.
As contraband, the child pornography is also evidence of
various crimes, including possession of child pornography,
18 U.S.C. § 2252A(a)(5)(B), and importation of obscene
material, 18 U.S.C. § 1462(a). But nothing in Cotterman
authorized border officials to conduct a search for evidence
that Cotterman was involved in sex-related crimes generally.

    Border officials are authorized to seize “merchandise
which . . . shall have been introduced into the United States
in any manner contrary to law.” 19 U.S.C. § 482(a)
(emphasis added). The photos on Cotterman’s laptop
computer were such merchandise. 18 U.S.C. § 2252(a). But
border officials have no general authority to search for crime.
This is true even if there is a possibility that such crimes may
be perpetrated at the border in the future. So, for example, if
U.S. officials reasonably suspect that a person who has
presented himself at the border may be engaged in price
fixing, see 15 U.S.C. § 1, they may not conduct a forensic
search of his phone or laptop. Evidence of price fixing—
texts or emails, for example—is not itself contraband whose
importation is prohibited by law. Such emails may be
evidence of a crime, but they are not contraband, and there is
no law prohibiting the importation of mere evidence of crime.
                      UNITED STATES V. CANO                               25

    We recognize that our analysis is in tension with the
Fourth Circuit’s decision in Kolsuz. Kolsuz was detained at
Washington Dulles International Airport when customs
agents discovered firearm parts in his luggage. Kolsuz, 890
F.3d at 138–39. Kolsuz was arrested and his cell phone
seized. Id. at 139. The agents subjected the phone to a
month-long forensic search, producing a 896-page report. Id.
Kolsuz challenged the search, which the district court upheld
and the Fourth Circuit affirmed. Id. at 139–42. The court
approved the forensic search because the agents had “reason
to believe . . . that Kolsuz was attempting to export firearms
illegally” and that “their search would reveal not only
evidence of the export violation they already had detected,
but also ‘information related to other ongoing attempts to
export illegally various firearm parts.’” Id. at 143 (quoting
the district court; citation omitted). According to the Fourth
Circuit, “[t]he justification behind the border search
exception is broad enough to accommodate not only the
direct interception of contraband as it crosses the border, but
also the prevention and disruption of ongoing efforts to
export contraband illegally.” Id. (emphasis added).10

    We agree with much of the Fourth Circuit’s discussion of
foundational principles, but we respectfully disagree with the
final step approving the search for further evidence that


     10
        As support for this proposition, the Fourth Circuit cited two district
court cases originating within our circuit. Both of those cases addressed
fact-patterns almost identical to Cano’s, and in each case the district court
held that the border-search exception was not limited to searching for
contraband directly. See United States v. Mendez, 240 F. Supp. 3d 1005,
1007–08 (D. Ariz. 2017); United States v. Ramos, 190 F. Supp. 3d 992,
999 (S.D. Cal. 2016). In neither case was the issue appealed to our circuit.
Thus, Cano’s case presents the first opportunity for us to consider the
matter.
26                UNITED STATES V. CANO

Kolsuz was smuggling weapons. Our disagreement focuses
precisely on the critical question that we previously
identified: Does the proper scope of a border search include
the power to search for evidence of contraband that is not
present at the border? Or, put differently, can border agents
conduct a warrantless search for evidence of past or future
border-related crimes? We think that the answer must be
“no.” The “[d]etection of . . . contraband is the strongest
historic rationale for the border-search exception.” Molina-
Isidoro, 884 F.3d at 295 (Costa, J., specially concurring).
Indeed, “every border-search case the Supreme Court has
decided involved searches to locate items being smuggled”
rather than evidence. Id. (emphasis added); see Montoya de
Hernandez, 473 U.S. at 537 (the border search is “to prevent
the introduction of contraband into this country”); United
States v. 12 200-Foot Reels of Super 8mm. Film, 413 U.S.
123, 125 (1973) (border searches are “necessary to prevent
smuggling and to prevent prohibited articles from entry”);
United States v. Thirty-Seven Photographs, 402 U.S. 363, 376
(1971) (“Customs officers characteristically inspect luggage
and their power to do so is not questioned in this case; it is an
old practice and is intimately associated with excluding
illegal articles from the country”). In fact, the Court has long
“draw[n] a sharp distinction between searches for contraband
and those for evidence that may reveal the importation of
contraband.” Molina-Isidoro, 884 F.3d at 296 (Costa, J.,
specially concurring).       The classic statement on the
distinction between seizing goods at the border because their
importation is prohibited and seizing goods at the border
because they may be useful in prosecuting crimes is found in
Boyd v. United States:

        Is a search and seizure, or, what is equivalent
        thereto, a compulsory production of a man’s
                  UNITED STATES V. CANO                       27

        private papers, to be used in evidence against
        him in a proceeding to forfeit his property for
        alleged fraud against the revenue laws—is
        such a proceeding for such a purpose an
        “unreasonable search and seizure” within the
        meaning of the fourth amendment of the
        constitution? . . . . The search for and seizure
        of stolen or forfeited goods, or goods liable to
        duties and concealed to avoid the payment
        thereof, are totally different things from a
        search for and seizure of a man’s private
        books and papers for the purpose of obtaining
        information therein contained, or of using
        them as evidence against him. The two things
        differ toto coelo.

116 U.S. 616, 622–23 (1886), overruled in part on other
grounds by Warden, Md. Penitentiary v. Hayden, 387 U.S.
294 (1967); see also id. at 633 (stating that compelling a man
to produce the evidence against himself not only violates the
Fifth Amendment, but makes the seizure of his “books and
papers” unreasonable under the Fourth Amendment).

     Although we continue to acknowledge that “[t]he
Government’s interest in preventing the entry of unwanted
persons and effects is at its zenith at the international border”
and that “the expectation of privacy is less at the border than
it is in the interior,” Flores-Montano, 541 U.S. at 152, 154,
we hold that the border search exception authorizes
warrantless searches of a cell phone only to determine
whether the phone contains contraband. A broader search
cannot be “justified by the particular purposes served by the
exception.” Florida v. Royer, 460 U.S. 491, 500 (1983).
28                UNITED STATES V. CANO

     2. The Impact of a Limited Scope for Border Searches

    Our conclusion that the border search exception is
restricted in scope to searches for contraband implicates two
practical limitations on warrantless border searches. First,
border officials are limited to searching for contraband only;
they may not search in a manner untethered to the search for
contraband. The Supreme Court has repeatedly emphasized
that “[t]he scope of the search must be ‘strictly tied to and
justified by’ the circumstances which rendered its initiation
permissible.” Terry v. Ohio, 392 U.S. 1, 19 (1968).

    The validity of the manual searches conducted by Agents
Petonak and Medrano at their inception is beyond dispute.
Manual searches of a cell phone at the border can be
conducted without any suspicion whatsoever, see Cotterman,
709 F.3d at 960, and both agents were officers of HSI and
thus had authority to conduct border searches, Soto-Soto, 598
F.2d at 548–49. As the Supreme Court explained in Terry,
however, “a search which is reasonable at its inception may
violate the Fourth Amendment by virtue of its intolerable
intensity and scope.” 392 U.S. at 18.

    Once Cano was arrested, Agent Petonak briefly searched
Cano’s phone and observed that there were no text messages.
The observation that the phone contained no text messages
falls comfortably within the scope of a search for digital
contraband. Child pornography may be sent via text
message, so the officers acted within the scope of a
permissible border search in accessing the phone’s text
messages.

   Agent Medrano conducted a second manual search of the
phone log and text messages on Cano’s phone. Medrano,
                     UNITED STATES V. CANO                            29

however, did more than thumb through the phone consistent
with a search for contraband. He also recorded phone
numbers found in the call log, and he photographed two
messages received after Cano had reached the border. Those
actions have no connection whatsoever to digital contraband.
Criminals may hide contraband in unexpected places, so it
was reasonable for the two HSI officers to open the phone’s
call log to verify that the log contained a list of phone
numbers and not surreptitious images or videos. But the
border search exception does not justify Agent Medrano’s
recording of the phone numbers and text messages for further
processing, because that action has no connection to ensuring
that the phone lacks digital contraband. Accordingly, to the
extent that Agent Medrano’s search of Cano’s phone went
beyond a verification that the phone lacked digital
contraband, the search exceeded the proper scope of a border
search and was unreasonable as a border search under the
Fourth Amendment.11


     11
        The fact of Cano’s arrest does not affect our analysis. The border
search does not lose its identity as such once Cano was arrested. The
United States retains a strong interest in preventing contraband from
entering the United States, whether it is brought in inadvertently,
smuggled, or admitted into the United States once its owner is arrested.
See United States v. Ickes, 393 F.3d 501, 503–05 (4th Cir. 2005)
(upholding the post-arrest search of a laptop computer at the border where
the officials had reason to suspect the computer carried child
pornography); see also United States v. Bates, 526 F.2d 966, 967–68 (5th
Cir. 1976) (per curiam) (upholding a search of the defendant’s vehicle
after he had been arrested at the border for violating his bond in
connection with a previous drug crime under both the search incident to
arrest and the border search exception).

    The government has not argued that the forensic search of Cano’s
phone can be justified as a search incident to lawful arrest. Such an
argument is foreclosed by Riley. See Riley, 573 U.S. at 388–91. Nor has
30                  UNITED STATES V. CANO

    Second, because the border search exception is limited in
scope to searches for contraband, border officials may
conduct a forensic cell phone search only when they
reasonably suspect that the cell phone contains contraband.
We have held that a “highly intrusive” search—such as a
forensic cell phone search—requires some level of
particularized suspicion. Cotterman, 709 F.3d at 963, 968;
see Flores-Montano, 541 U.S. at 152. But that just begs the
question: Particularized suspicion of what? Contraband? Or
evidence of future border-related crimes? Having concluded
above that border searches are limited in scope to searches for
contraband and do not encompass searches for evidence of
past or future border-related crimes, we think the answer here
is clear: to conduct a more intrusive, forensic cell phone
search border officials must reasonably suspect that the cell
phone to be searched itself contains contraband.

    Were we to rule otherwise, the government could conduct
a full forensic search of every electronic device of anyone
arrested at the border, for the probable cause required to
justify an arrest at the border will always satisfy the lesser
reasonable suspicion standard needed to justify a forensic
search. As the Court pointed out in Riley, modern cell phones
are “minicomputers” with “immense storage capacity.” 573
U.S. at 393. Such phones “carry a cache of sensitive personal
information”—“[t]he sum of an individual’s private life”—
such that a search of a cell phone may give the government


the government argued that once Medrano saw the phone numbers in the
call log and the text messages that he could record them consistent with
the plain view exception. See United States v. Comprehensive Drug
Testing, 621 F.3d 1162, 1175–77 (9th Cir. 2010) (en banc) (per curiam),
overruled in part on other grounds as recognized by Demaree v.
Pederson, 887 F.3d 870, 876 (9th Cir. 2018) (per curiam).
                  UNITED STATES V. CANO                     31

not only “sensitive records previously found in the home,”
but a “broad array of private information never found in a
home in any form—unless the phone is.” Id. at 393–97.
Were we to give the government unfettered access to cell
phones, we would enable the government to evade the
protections laid out in Riley “on the mere basis that [the
searches] occurred at the border.” Soto-Soto, 598 F.2d at 549.

     Moreover, in cases such as this, where the individual
suspected of committing the border-related crime has already
been arrested, there is no reason why border officials cannot
obtain a warrant before conducting their forensic search. This
“is particularly true in light of ‘advances’ in technology that
now permit ‘the more expeditious processing of warrant
applications.’” Birchfield v. North Dakota, 136 S. Ct. 2160,
2192 (2016) (quoting Missouri v. McNeely, 569 U.S. 141, 154
(2013)); see Riley, 573 U.S. at 401. Indeed, in most cases the
time required to obtain a warrant would seem trivial
compared to the hours, days, and weeks needed to complete
a forensic electronic search. See, e.g., Wanjiku, 919 F.3d at
477 (noting that a forensic “preview” takes one to three
hours; the full examination “could take months”); Kolsuz, 890
F.3d at 139 (describing how the forensic search “lasted for a
full month, and yielded an 896-page report”); Cotterman, 709
F.3d at 959 (describing how the first forensic search was
conducted over five days; additional evidence was found
“[o]ver the next few months”). We therefore conclude that
border officials may conduct a forensic cell phone search
only when they reasonably suspect that the cell phone to be
searched itself contains contraband.

   Applied here, if the Cellebrite search of Cano’s cell phone
qualifies as a forensic search, the entire search was
32                    UNITED STATES V. CANO

unreasonable under the Fourth Amendment.12 Although
Agents Petonak and Medrano had reason to suspect that
Cano’s phone would contain evidence leading to additional
drugs, the record does not give rise to any objectively
reasonable suspicion that the digital data in the phone
contained contraband.13 Absent reasonable suspicion, the
border search exception did not authorize the agents to
conduct a warrantless forensic search of Cano’s phone, and
evidence obtained through a forensic search should be
suppressed.

     C. Good Faith Exception

    We next consider whether the evidence uncovered by the
searches is nevertheless allowed by the good faith exception.
Having held that the manual searches partially violated the
Fourth Amendment and having held that, if the Cellebrite

     12
         Whether the Cellebrite search constitutes a forensic search is
disputed. Because the district court passed on the issue without deciding
it, because neither party has briefed the question to us, and because we are
vacating Defendant’s conviction, we decline to reach the merits of the
parties’ dispute. See ASSE Int’l, Inc. v. Kerry, 803 F.3d 1059, 1079 (9th
Cir. 2015).
     13
       Indeed, the detection-of-contraband justification would rarely seem
to apply to an electronic search of a cell phone outside the context of child
pornography. The courts of appeals have just begun to confront the
difficult questions attending cell phone searches at the border. Most of the
cases have involved child pornography. See, e.g., Wanjiku, 919 F.3d 472;
Touset, 890 F.3d 1227; Molina-Isidoro, 884 F.3d 287; Vergara, 884 F.3d
1309; Cotterman, 709 F.3d 952. Among the courts of appeals, only the
Fourth Circuit has addressed the question outside the context of
pornography. Kolsuz, 890 F.3d 133 (exportation of firearms parts); see
also United States v. Kim, 103 F. Supp. 3d 32 (D.D.C. 2015) (exports in
violation of Iranian trade embargo); United States v. Saboonchi, 990 F.
Supp. 2d 536 (D. Md. 2014) (same).
                   UNITED STATES V. CANO                       33

search of Cano’s phone was a forensic search, it violated the
Fourth Amendment, we must determine whether the
appropriate remedy is suppression of the evidence. The
exclusionary rule is “a ‘prudential’ doctrine”; it is “‘not a
personal constitutional right,’ nor is it designed to ‘redress the
injury’ occasioned by an unconstitutional search.” Davis v.
United States, 564 U.S. 229, 236 (2011) (quoting Stone v.
Powell, 428 U.S. 465, 486 (1976)). Because “[e]xclusion
exacts a heavy toll on both the judicial system and society at
large,” we invoke the rule when we are confident that it will
“deter future Fourth Amendment violations.” Id. at 236–37.
The exclusionary rule does not deter such violations “when
the police conduct a search in objectively reasonable reliance
on binding judicial precedent.” Id. at 239. We have said that
the good faith exception applies only to searches where
“binding appellate precedent . . . ‘specifically authorizes’ the
police’s search.” United States v. Lara, 815 F.3d 605, 613
(9th Cir. 2016) (quoting Davis, 564 U.S. at 232). It is not
sufficient for the question to be “unclear” or for the
government’s position to be “plausibly . . . permissible.” Id.
at 613–14. At the same time, the “precedent [does not have]
to constitute a factual match with the circumstances of the
search in question for the good-faith exception to apply” so
as not to “make the good-faith exception a nullity.” United
States v. Lustig, 830 F.3d 1075, 1082 (9th Cir. 2016).

    The government points to Cotterman as support for the
good faith of the officials. We fail to see how border officials
could believe that Cotterman was “binding appellate
precedent” authorizing their search. Although we have
concluded that Cotterman is still good law after Riley, the
officials could not rely on Cotterman to justify a search for
evidence; Cotterman was a search for contraband that the
government has a right to seize at the border. Here, the
34                UNITED STATES V. CANO

officials’ search was objectively tied only to proving their
case against Cano and finding evidence of future crimes.
Searching for evidence and searching for contraband are not
the same thing.

    We understand that border officials might have thought
that their actions were reasonable, and we recognize that
border officials have to make in-the-moment decisions about
how to conduct their business—whether or not they have
written guidance from the courts. But as we understand the
Davis rule, the good faith exception to the exclusionary rule
applies only when the officials have relied on “binding
appellate precedent.” See Lara, 815 F.3d at 613; see also
Wanjiku, 919 F.3d at 485–86 (finding that agents had
reasonable suspicion to search the defendant’s cell phone,
laptop, and portable hard drive for child pornography;
holding that, if probable cause was required, the officials
acted in good faith). This is a rapidly developing area, not an
area of settled law. Even if our decision in Cotterman
rendered the searches “plausibly . . . permissible,” it did not
“specifically authorize” the cell phone searches at issue here.
Lara, 815 F.3d at 613–14.

                            ***

    In sum, the manual searches and the Cellebrite search of
Cano’s cell phone exceeded the scope of a valid border
search. Because the good faith exception does not apply,
most of the evidence obtained from the searches of Cano’s
cell phone should have been suppressed. We thus reverse the
district court’s order denying Cano’s motion to suppress, and
we vacate Cano’s conviction. On any retrial, the district court
should determine whether any additional evidence from the
warrantless searches of Cano’s cell phone should be
                  UNITED STATES V. CANO                       35

suppressed, either because the Cellebrite search qualifies as
a forensic search, which the government lacked reasonable
suspicion to conduct, or because the evidence exceeds the
proper scope of a border search.

                 III. DISCOVERY ISSUES

    Cano has also alleged that the government violated his
rights under both Brady and Federal Rule of Criminal
Procedure 16 when it failed to turn over certain information
that Cano requested from the FBI and DEA. We address
Cano’s discovery claims, as the issues may be relevant on any
retrial.

    Under Brady, the prosecution has an obligation, imposed
by the Due Process Clause, to produce “evidence favorable to
an accused upon request . . . where the evidence is material
either to guilt or to punishment.” 373 U.S. at 87.
“[E]vidence is material only if there is a reasonable
probability that, had the evidence been disclosed to the
defense, the result of the proceeding would have been
different.” United States v. Bagley, 473 U.S. 667, 682
(1985).14

    Under Rule 16, the government must, upon request, turn
over any documents “within the government’s possession,
custody, or control” that are “material to preparing the
defense.” Fed. R. Crim. P. 16(a)(1)(E)(i). The defendant
“must make a threshold showing of materiality, which
requires a presentation of facts which would tend to show that
the Government is in possession of information helpful to the

    14
        We review de novo whether a Brady violation has occurred.
United States v. Stever, 603 F.3d 747, 752 (9th Cir. 2010).
36                  UNITED STATES V. CANO

defense.” United States v. Muniz-Jaquez, 718 F.3d 1180,
1183–84 (9th Cir. 2013) (quoting United States v. Stever, 603
F.3d 747, 752 (9th Cir. 2010)). Because “[i]nformation that
is not exculpatory or impeaching may still be relevant to
developing a possible defense,” Rule 16 is “broader than
Brady.” Id. at 1183.15

    Under both Brady and Rule 16, the government “has no
obligation to produce information which it does not possess
or of which it is unaware.” Sanchez v. United States, 50 F.3d
1448, 1453 (9th Cir. 1995). It has an obligation to turn over
only material, exculpatory or otherwise helpful to the defense,
that it has in its possession.16 “Possession” is not limited to
what the prosecutor personally knows. Browning v. Baker,
875 F.3d 444, 460 (9th Cir. 2017), cert. denied, 138 S. Ct.
2608 (2018); United States v. Bryan, 868 F.2d 1032, 1036
(9th Cir. 1989). Because prosecutors are in a “unique
position to obtain information known to other agents of the
government,” they have an obligation to “disclos[e] what
[they] do[] not know but could have learned.” Carriger v.
Stewart, 132 F.3d 463, 480 (9th Cir. 1997) (en banc); see also
Kyles v. Whitley, 514 U.S. 419, 437 (1995) (describing how


     15
        Although discovery rulings are generally reviewed for abuse of
discretion, Stever, 603 F.3d at 752, we review a district court’s
interpretation of the discovery rules de novo, United States v. Cedano-
Arellano, 332 F.3d 568, 570–71 (9th Cir. 2003).
     16
        The “possession” element of Brady is treated as coextensive with
that of Rule 16. See, e.g., United States v. Bryan, 868 F.2d 1032, 1037
(9th Cir. 1989) (using the same “knowledge and access” test to determine
“possession” for both Rule 16 and Brady); United States v. Grace, 401 F.
Supp. 2d 1069, 1076 (D. Mont. 2005) (“Whether exculpatory information
is in the government’s possession for Brady purposes is measured by the
same . . . test used under Rule 16(a)(1)(E) for discovery.”).
                  UNITED STATES V. CANO                       37

the “individual prosecutor has a duty to learn of any favorable
evidence known to [those] acting on the government’s
behalf”); Youngblood v. West Virginia, 547 U.S. 867, 869–70
(2006) (per curiam). This includes information held by
subordinates such as investigating police officers, see Kyles,
514 U.S. at 438; United States v. Price, 566 F.3d 900, 908–09
(9th Cir. 2009), and sometimes extends to information held
by other executive branch agencies, see United States v.
Santiago, 46 F.3d 885, 893 (9th Cir. 1995); United States v.
Jennings, 960 F.2d 1488, 1490–91 (9th Cir. 1992).

    Documents held by another executive branch agency are
deemed to be “in the possession of the government” if the
prosecutor has “knowledge of and access to” the documents.
Bryan, 868 F.2d at 1036. Knowledge and access are
presumed if the agency participates in the investigation of the
defendant. Id. (“The prosecutor will be deemed to have
knowledge of and access to anything in the possession,
custody or control of any federal agency participating in the
same investigation of the defendant.”). However, “a federal
prosecutor need not comb the files of every federal agency
which might have documents regarding the defendant in order
to fulfill his or her obligations under [Rule 16].” Id.; see also
Kyles, 514 U.S. at 437 (“We have never held that the
Constitution demands an open file policy . . . .”).

    Here, Cano asserted a third-party defense theory: he was
staying in Tijuana with his cousin, Jose Medina; Medina was
a member of the Latin Kings gang which was involved in the
drug trade; and Medina had access to Cano’s car before Cano
was stopped at the border. Cano requested that the U.S.
Attorney’s Office turn over any material held by HSI, the
FBI, and the DEA relating to: (1) records linking his cousin
Jose Medina to drug sales, distribution, and trafficking; and
38                UNITED STATES V. CANO

(2) documentation showing a link between the Latin Kings
and drug trafficking through the United States-Mexico
border. The district court found that both requests might
produce evidence that was exculpatory under Brady and
material under Rule 16, but limited Cano’s discovery to only
material held by HSI. The court concluded that the
prosecutor did not have access to evidence held by the FBI
and DEA, and thus had no obligation to provide such
evidence, because both agencies had “rebuffed” the
prosecutor’s attempts to obtain information. Thus, the only
issue raised on appeal is whether any material held by the
DEA and FBI should be deemed “within the government’s
possession.”

    We find no evidence that the prosecution had knowledge
or possession of evidence showing that Medina or the Latin
Kings were involved in drug trafficking at the Mexico-
California border. Medina had one drug-related conviction,
and it was for simple possession of cocaine, not trafficking.
Before trial, however, the prosecution team reached out to
Medina and promised him immunity and immigration
documents in exchange for cooperation and information
concerning drug importation. Although Medina originally
rebuffed the government, he eventually offered to work with
the government and “stated that he would be able to assist the
Government with the . . . biggest RICO . . . case and drug
seizures of 20 to 25 kilograms at a time.” The district court
found that Medina’s statements “spawn[ed] an inference that
[he] is closely connected to the drug-traffickers in Tijuana.”
Based on this inference, Cano argues that the government had
sufficient knowledge of a possible connection between
Medina and drug trafficking to trigger the government’s
discovery obligations.
                     UNITED STATES V. CANO                            39

    Cano’s argument, however, misstates the test we first set
out in Bryan. Cano has argued only that the prosecutor had
knowledge that certain facts might exist. However, we have
said that the prosecutor’s disclosure obligations turn on “the
extent to which the prosecutor has knowledge of and access
to the documents sought by the defendant.” Bryan, 868 F.2d
at 1036 (emphasis added); see also Santiago, 46 F.3d at 894
(analyzing whether the prosecutor had knowledge of and
access to certain inmate files). We have required disclosure
only of documents that the prosecutor knew existed. Bryan,
868 F.2d at 1034–37.

    Here, although Cano has presented evidence alleging a
plausible connection between Medina and drug trafficking,
Cano has failed to adduce any evidence showing that
prosecutors or investigators knew that the FBI or the DEA
possessed documents showing that connection. In fact, the
record established the opposite. One of the HSI agents ran
Medina’s name through two different law enforcement
clearinghouses—in which the FBI and DEA both
participate—and neither search returned any hits.

    Moreover, the prosecutor did not have access to FBI or
DEA files and thus was under no obligation to “comb the
files” of the FBI and DEA for documents relating to
Medina.17 We have occasionally presumed that a prosecutor

    17
        Cano sought to introduce a 2015 report from the FBI’s National
Gang Intelligence Center listing the Latin Kings as one of the top gangs
involved in cross border crime, and including drug importation in its list
of cross-border crimes. (The evidence was not ultimately presented at
trial.) Cano also proffered information concerning two government
informants working within the Latin Kings. Although these reports may
suggest that the FBI may have had further information regarding a
connection between the Latin Kings and drug importation, Cano has not
40                   UNITED STATES V. CANO

has access to an agency’s files where the prosecutor actually
obtained inculpatory information from the agency, even if the
agency was not involved in the investigation or prosecution.
See Santiago, 46 F.3d at 894 (concluding that the prosecutor
had access to other inmates’ prison files where the prosecutor
was able to obtain the defendant’s prison file from the Bureau
of Prisons). Here, however, the U.S. Attorney’s Office
advised the district court that it did not obtain any evidence—
inculpatory or exculpatory—from the FBI or the DEA.
Following the district court’s initial discovery order, HSI’s
agent—Agent Petonak—made a formal request to the legal
counsel for the FBI and the DEA for any “materials related to
the Latin Kings importing cocaine from Mexico to the United
States,” but both agencies “declined to provide [him] with
any such information.” Neither agency revealed whether any
such information existed or provided a reason for its refusal.
The U.S. Attorney’s Office also reached out to the FBI and
the DEA for Latin Kings-related discovery. That request was
also denied.

    Cano argues that the FBI and DEA’s refusal to turn over
information in this particular case should not be
determinative and that the test for access under Bryan and
Santiago requires only that the U.S. Attorney’s Office or
investigating agency generally have access to this type of
information. Cano points to evidence from both prosecution
and defense witnesses that HSI regularly works with the FBI
and the DEA; that “interagency cooperation has been
emphasized” after September 11, 2001; that agents from the
different agencies regularly access information for one
another; that a DEA representative worked in Agent
Petonak’s office; and that agents are often cross-listed


established that the prosecutor had access to the FBI’s or the DEA’s files.
                  UNITED STATES V. CANO                      41

between agencies. From this, Cano argues that HSI generally
has access to FBI and DEA files for inculpatory purposes,
and thus asserts that the refusal of the FBI and DEA to
provide information in this particular case should not relieve
HSI of its discovery obligations. To rule otherwise, Cano
contends, would allow these withholding agencies “to
effectively wall off exculpatory information from the
government in a particular defendant’s case, all the while
providing the government free-flowing access to information
in its overall investigations.”

    Although we are sympathetic to Cano’s concerns
regarding strategic withholding, the rule Cano urges us to
adopt is much too broad. Brady and Rule 16 obligations are
case specific. In Bryan we stated that the test for
“possession” turns on the prosecutor’s “knowledge of and
access to the documents sought by the defendant in each
case” and that “[t]he prosecutor will be deemed to have
knowledge of and access to anything in the possession,
custody or control of any federal agency participating in the
same investigation of the defendant.” 868 F.2d at 1036
(emphases added). Such a case-by-case approach makes
sense, as the FBI and DEA may have valid concerns over
revealing sensitive information in cases wholly unrelated to
the agencies’ own workload; the agencies may be reluctant to
cooperate in a particular investigation if it means opening
their files in other investigations. If Cano thinks that the FBI
or the DEA have other information, not known to the U.S.
Attorney’s Office or the investigating officers, he may file a
request under the Freedom of Information Act, subject to that
Act’s own restrictions on releasing “records or information
compiled for law enforcement purposes.” 5 U.S.C.
§ 552(b)(7). Brady and Rule 16 are not a means for a
defendant to require the prosecutor to do this work for him.
42                UNITED STATES V. CANO

See generally Roth v. U.S. Dep’t of Justice, 642 F.3d 1161,
1175–76 (D.C. Cir. 2011); Boyd v. Crim. Div. of U.S. Dep’t
of Justice, 475 F.3d 381, 386–89 (D.C. Cir. 2007).

    Cano is unable to identify any case in which the
prosecutor was required to obtain discovery from an agency
wholly unrelated to the investigation of the defendant in spite
of that agency’s refusal to comply; all of the cases cited by
Cano imposing a “duty to learn” on the prosecutor involve
independent federal agencies that had participated in the
investigation of the defendant. See Price, 566 F.3d at
908–09; Carriger, 132 F.3d at 479–80; United States v.
Perdomo, 929 F.2d 967, 971 (3d Cir. 1991); United States v.
Osorio, 929 F.2d 753, 762 (1st Cir. 1991). Indeed, the Third
Circuit has held that a Brady obligation is not triggered where
the agency did not participate in the investigation in any way,
did not share any information with the prosecuting team, and
where the prosecutor had no authority or control over the
agency’s members. United States v. Pelullo, 399 F.3d 197,
218 (3d Cir. 2005); see also United States v. Salyer, 271
F.R.D. 148, 156 (E.D. Cal. 2010) (concluding that “[t]he need
for formal process in the acquisition of documents [from
another agency] is the antithesis of ‘access’”). We similarly
now hold that the prosecutor should not be held to have
“access” to any information that an agency not involved in
the investigation or prosecution of the case refuses to turn
over.

    Because the HSI agents and prosecutors in Cano’s case
neither knew of nor had access to any additional files relating
to Medina and the Latin Kings, we conclude that the
government has satisfied its discovery obligations under
Brady and Rule 16.
                UNITED STATES V. CANO               43

                  IV. CONCLUSION

   We REVERSE the district court’s order denying Cano’s
motion to suppress and VACATE Cano’s conviction.

```

---

## GROUP: content/cases/United States v. Capers.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Capers
type: case
citation: "627 F.3d 470 (2010)"
parallel_cite: ""
neutral_cite: "2010 U.S. App. LEXIS 24516; 2010 WL 4869768"
court: 2d Cir.
court_level: coa
circuit: ca2
year: 2010
date_decided: 2010-12-01
docket: 09-2101
authority_weight: "Binding in-circuit — 2d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/180156/united-states-v-capers/"
  cluster_id: 180156
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Capers
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: Key
related:
  - "[[Miranda Waiver and Invocation]]"
tags:
  - case
  - fifth-amendment
  - miranda
  - question-first
  - seibert
  - two-step-interrogation
  - second-circuit
holding: "Under Justice Kennedy's controlling concurrence in Missouri v. Seibert, a confession obtained through a deliberate, two-step 'question-first, warn-later' interrogation must be suppressed absent curative measures; where a postal inspector aware of the obvious need for a Miranda warning interrogated Capers without one, then re-interrogated him on the same subject about 90 minutes later with no curative language, the technique was a deliberate two-step designed to undermine Miranda, and the postwarning statements were properly suppressed."
aliases:
  - United States v. Capers
  - "United States v. Capers (2d Cir. 2010)"
---

# United States v. Capers

*627 F.3d 470 (2d Cir. 2010)* (No. 07-1830-cr) · U.S. Court of Appeals for the Second Circuit · **Binding in-circuit — 2d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 180156 → majority opinion 180156 (Hall, J.; 627 F.3d 470, decided Dec. 1, 2010). Re-keyed in the pre-W5 identity audit from a wrong-case namesake (RICO/crime-of-violence Capers) to the intended Seibert question-first Capers; identity re-verified on read 2026-07-07. Rule quote string-matched to the CL opinion text; the holding is stated at the opinion's opening (627 F.3d 470-471) — S9 verifies the exact star page. -->

## Background
Postal Inspectors suspected William Capers, a mail handler, of stealing money orders and ran a sting, planting an alarmed Express Mail envelope. When the alarm sounded, inspectors handcuffed Capers, sat him in a supervisor's office, and — without any [[Miranda and Custodial Interrogation|Miranda warning]] — Inspector Hoti told him he had been watching all day and questioned him; Capers admitted taking the money orders and produced them. About 90 minutes later, at a second facility, the same inspector gave [[Miranda and Custodial Interrogation|Miranda warnings]] and re-interrogated Capers on the same subject, making no reference to the earlier statements. The district court suppressed the postwarning statements; the government appealed.

## Issue
Whether the postwarning statements must be suppressed as the product of a deliberate, two-step "question-first" interrogation under *[[Missouri v. Seibert]]*.

## Rule
Under Justice Kennedy's controlling *[[Missouri v. Seibert|Seibert]]* [[Common Legal Terms#concurring-opinion|concurrence]], a court first asks whether officers used a "deliberate two-step strategy" to undermine *[[Miranda v. Arizona|Miranda]]*, and if so whether curative measures were taken; without them, the postwarning statements are inadmissible. Applying that standard, the court held: the initial unwarned interrogation, "followed 90 minutes later by a second, post-*Miranda* interrogation by the same investigator, on the same subject matter, under similar circumstances and with no explicit curative language[,] amounted to a deliberate, two-step interrogation technique designed to undermine the defendant's *Miranda* rights." — 627 F.3d at 471. ^pin-471

## Application
The same inspector conducted both rounds, on the same theft, under materially similar custodial conditions; the 90-minute gap and transport did not break the continuity, and the second warning said nothing about the already-elicited admissions. On those facts the interrogation bore the hallmarks of the calculated question-first technique *[[Missouri v. Seibert|Seibert]]* condemns, and no curative step — a substantial break made meaningful to the suspect, or a warning explaining the likely inadmissibility of the earlier statement — was taken. Suppression followed.

## Conclusion
**Affirmed.** Judge Hall wrote for the panel; Judge Trager dissented. The suppression order was upheld.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Capers* is a leading circuit application of the *[[Miranda Waiver and Invocation|Miranda]]* two-step doctrine, adopting Justice Kennedy's *[[Missouri v. Seibert|Seibert]]* [[Common Legal Terms#concurring-opinion|concurrence]]: a deliberate question-first strategy voids a later warned confession unless curative measures restore the warning's meaning.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key*

## Sources
- [*United States v. Capers*, 627 F.3d 470 (2d Cir. 2010)](https://www.courtlistener.com/opinion/180156/united-states-v-capers/) — pinpoint: 627 F.3d at 471 (deliberate two-step "question-first" interrogation; postwarning statements suppressed under Kennedy's *Seibert* test). Rule quote string-matched to the CL opinion text 2026-07-07 (opening holding).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f0a382372357b047", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "627 F.3d 470 (2010)", "court": "2d Cir.", "neutral_cite": "2010 U.S. App. LEXIS 24516; 2010 WL 4869768", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Capers", "year": "2010"}}
{"assertion_id": "5b47e56423fed39d", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key", "title": "United States v. Capers"}}
{"assertion_id": "760836d23e669497", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under Justice Kennedy's controlling concurrence in Missouri v. Seibert, a confession obtained through a deliberate, two-step 'question-first, warn-later' interrogation must be suppressed absent curative measures; where a postal inspector aware of the obvious need for a Miranda warning interrogated Capers without one, then re-interrogated him on the same subject about 90 minutes later with no curative language, the technique was a deliberate two-step designed to undermine Miranda, and the postwarning statements were properly suppressed.", "title": "United States v. Capers"}}
{"assertion_id": "2074904685a2c862", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Capers", "varies_by_point": "false"}}
{"assertion_id": "4361fcfa4f09e505", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 2d Cir.", "title": "United States v. Capers"}}
```

### lake record — United States v. Capers

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Capers",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Capers",
    "case_name_short": "Capers",
    "case_name_full": "UNITED STATES of America, Appellant, v. William CAPERS, Defendant-Appellee",
    "input_case_name": "United States v. Capers",
    "court": "2d Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca2",
    "state": null,
    "date_decided": "2010-12-01",
    "year": 2010,
    "docket": "09-2101",
    "cluster_id": 180156,
    "lead_opinion_id": 9438686,
    "sibling_ids": [],
    "absolute_url": "/opinion/180156/united-states-v-capers/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "627 F.3d 470",
      "volume": "627",
      "reporter": "F.3d",
      "page": "470",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. App. LEXIS 24516",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "24516",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 4869768",
        "volume": "2010",
        "reporter": "WL",
        "page": "4869768",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "627 F.3d 470",
        "volume": "627",
        "reporter": "F.3d",
        "page": "470",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. App. LEXIS 24516",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "24516",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 4869768",
        "volume": "2010",
        "reporter": "WL",
        "page": "4869768",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "627 F.3d 470",
    "official_selection": {
      "court_class": "coa",
      "selected": "627 F.3d 470",
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
    "date_created": "2026-07-07T18:15:24Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:15:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:15:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:15:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:15:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-capers--180156",
      "to_record_id": "United States v. Capers",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Capers

```
<opinion type="majority">
<p id="b502-6">Judge TRAGER dissents in a separate opinion.</p>
<author id="b502-7">HALL, Circuit Judge:</author>
<p id="b502-8">The government appeals from an order entered in the United States District Court for the Southern District of New York (McKenna, <em>J.) </em>to suppress inculpatory statements made by defendant-appellee while in custody. We AFFIRM the order of the district court on the ground that the initial interrogation conducted by an investigator aware of the obvious need for a <em>Miranda </em>warning, followed 90 minutes later by a second, <em>post-Miranda </em>interrogation by the same investigator, on the same subject matter, under similar circumstances and with no explicit curative language amounted to a deliberate, two-step interrogation technique designed to undermine the defendant’s <em>Miranda </em>rights.</p>
<p id="b502-9">BACKGROUND</p>
<p id="b502-10">In March 2005, the United States Postal Service suspected defendant-appellee William Capers, employed as a mail handler, of stealing money orders from Express Mail envelopes. Postal Inspectors decided to conduct a sting operation targeting Capers. In December 2005, Inspectors planted two Express Mail envelopes in the mail-sorting facility where Capers worked. One envelope contained $30 cash, and the other contained two $80 money orders and was equipped with an alarm device. The alarm was set to trigger automatically in the event the envelope with the money orders was opened and its contents removed.</p>
<p id="b502-14">Haring planted the envelopes in a mail container, Postal Inspectors Hoti, Del Giudice, Moon, and Chow conducted surveillance of Capers throughout the day. At approximately 5 p.m., Capers noticed the envelopes for the first time. Approximately two hours later, Capers and Juan Lopez, a fellow employee, entered a trailer holding mail containers and briefly disappeared from the inspectors’ view. Less than one minute later, the alarm in the envelope sounded, and the postal inspectors rushed into the trailer to apprehend both Capers and Lopez. The inspectors handcuffed both suspects. Inspector Hoti instructed Capers to follow him into a supervisor’s office. Inspectors Del Giudice and Moon also entered the office. They instructed Capers to sit in a chair, still handcuffed, while the three inspectors stood around him. None of the inspectors gave Capers a <em>Miranda </em>warning.</p>
<p id="b502-15">According to the testimony of Del Giudice, Hoti said to Capers: <page-number citation-index="1" label="473">*473</page-number>(Hr’g Tr. 95, Sept. 5, 2006.) Hoti then asked Capers where the contents of the Express Mail envelope were located. Capers gestured toward his right side pants pocket, and Hoti asked Capers what was in his pocket. Capers replied the money orders. (Hr’g Tr. 34.) Hoti asked for Capers’ permission to “grab” them, and when Capers said “yes,” Hoti removed the money orders from Capers’ pocket. (Hr’g Tr. 34.) Hoti asked Capers if the money orders belonged to him, and Capers said no. (Hr’g Tr. 34.) Capers told Hoti that he got the money orders from the Express Mail envelope. (Hr’g Tr. 64.) Hoti also questioned Capers about the $30 cash that had been planted in the other Express Mail envelope, but Capers stated that he did not know anything about it. The entire questioning took less than five minutes. Regarding the lack of a <em>Miranda </em>warning, Hoti testified that he did not read Capers his rights because he was in a hurry to track down the missing money orders so that they did not get lost in the large mail-sorting facility and because he needed to question Lopez, who was held handcuffed outside the supervisor’s office, to determine his level of involvement in the crime.</p>
<blockquote id="b502-16"><page-number citation-index="1" label="472">*472</page-number>something like, look, you know, talk to me or don’t talk to me, I don’t care but I’m telling you right now or I’ll tell you that I’m going to do my best to make you go away, and I just want you to know. And I’ve been watching you all day. I know everything that you did tonight.</blockquote>
<p id="b503-5"><page-number citation-index="1" label="473">*473</page-number>Del Giudice and Moon then escorted Capers to a van to transport him to another Postal Service facility (the “Bronx Domicile”) for further questioning. They waited in the van for approximately 15 to 20 minutes while the other inspectors located the alarm device from the opened envelope. In the van, Del Giudice engaged Capers in conversation primarily about Capers’ automobile. Capers remained handcuffed throughout this time, which included 15 to 20 minutes of waiting and 20 minutes of driving to the Bronx Domicile.</p>
<p id="b503-6">When they arrived at the Bronx Domicile, the inspectors placed Capers in an interview room and handcuffed him to the chair in which he sat. Del Giudice and Moon remained with him, engaging him in further conversation, and gathering relevant personal information from Capers for their paperwork. At one point, Capers asked Del Giudice about the possibility of being fired, and Del Giudice told him that “it’s in your best interest to tell the truth when Inspector Hoti comes down. Be honest. It’s always better if you’re honest.” (Hr’g Tr. 117.)</p>
<p id="b503-8">Capers and the two postal inspectors waited for approximately 30 to 40 minutes until Hoti entered the room. Hoti then advised Capers of his <em>Miranda </em>rights. Hoti made no reference, however, to the statements Capers had already made during the initial interrogation. Hoti explained in his testimony, “I don’t remember the specific question and its sequence, and I don’t see a need to say what did you do with the contents of this Express Mail when I already have the answer to that. So I would not have asked that same question.” (Hr’g Tr. 72.) Capers signed a Postal Service Warning and Waiver of Rights form, and Hoti proceeded to question Capers about the events of the evening, specifically asking about what he did with the Express Mail envelopes earlier that night. Capers verbally confessed to taking the money orders. When Hoti asked him to provide a written statement, Capers replied by asking, ‘What’s in it for me?” (Hr’g Tr. 51.) Hoti told Capers “there’s nothing I can promise you,” and then ended the questioning. (Hr’g Tr. 51.)</p>
<p id="b503-9">Capers was indicted in March 2006, charged with one count of theft of mail matter by a postal employee, in violation of <span class="citation no-link">18 U.S.C. § 1709</span>. He moved to suppress the inculpatory statements he made both before and after receiving the <em>Miranda </em>warning, and on March 30, 2007, the district court entered an order suppressing the statements. The district court found <page-number citation-index="1" label="474">*474</page-number>that “[t]he government has not shown that ... defendant relinquished his right to remain silent voluntarily with a full awareness of the rights being waived and the consequences of doing so.” <em>United States v. Capers, </em>No. 06 Cr. 266, <span class="citation no-link">2007 WL 959300</span>, at * 15 (S.D.N.Y. Mar.29, 2007) (internal quotation marks omitted). Although the district court found that the postal inspectors did not have the “specific intent” to circumvent Capers’ <em>Miranda </em>rights, <em><span class="citation no-link">id.,</span> </em>it did find their interrogation tactics deprived Capers of a “genuine right to remain silent,” <span class="citation no-link"><em>id. </em>at * 14</span>. The United States filed a timely notice of appeal.</p>
<p id="b504-4">DISCUSSION</p>
<p id="b504-5">I. Standard of Review</p>
<p id="b504-6">“We review a district court’s determination regarding the constitutionality of a <em>Miranda </em>waiver <em>de novo.” United States v. Carter, </em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/#534" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">489 F.3d 528, 534</a></span> (2d Cir.2007). In doing so, we review “a district court’s underlying factual findings for clear error.” <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Id.</a></span></em></p>
<p id="b504-7">II. <em>Miranda </em>and the Two-Step Interrogation Technique</p>
<p id="b504-8">The issue before us is whether Hoti and the other postal inspectors deliberately deprived Capers of the rights to which he is entitled under <em>Miranda v. Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L.Ed.2d 694</a></span> (1966). The government argues that the defendant was given an effective <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning prior to making voluntary inculpatory statements, and therefore the statements he made following the warning should not have been suppressed by the district court. Capers argues that the rule that the Supreme Court announced in <em>Missouri v. Seibert, </em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">542 U.S. 600</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">159 L.Ed.2d 643</a></span> (2004), and that this Court further clarified in <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span>, </em>requires us to conclude that the postal inspectors’ two-step interrogation in this case constituted a deliberate violation of Capers’ <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights.</p>
<p id="b504-10">“The purpose of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning is to ensure that the person in custody has sufficient knowledge of his or her constitutional rights relating to the interrogation and that any waiver of such rights is knowing, intelligent, and voluntary.” <em>Carter, </em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/#534" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">489 F.3d at 534</a></span>. The Supreme Court, in <em>Oregon v. Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U.S. 298</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">84 L.Ed.2d 222</a></span> (1985), and <em>Seibert, </em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">542 U.S. 600</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>, has twice addressed situations like this one in which a suspect in custody confessed without having received a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning, subsequently received a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning, and then confessed again.</p>
<p id="b504-11"><em>Elstad </em>involved a situation in which a suspect made a self-incriminating statement while two police officers were at his home investigating a robbery. At the time he had not received a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#300" aria-description="Citation for case: Oregon v. Elstad">470 U.S. at 300-01</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. The officers transported the suspect to a police station where they gave him a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning prior to obtaining both an oral and written confession. <em>Id. </em>at 301, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. At trial, the defendant moved to suppress the postwarning confessions on the ground that the statements made at the police station only came about as a result of the first inadmissable statement made at his house. <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#302" aria-description="Citation for case: Oregon v. Elstad"><em>Id. </em>at 302</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. The Supreme Court ultimately rejected the “fruit of the poisonous tree” argument, <em>see Wong Sun v. United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471, 487-88</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span> (1963), and held that “[tjhough <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires that the unwarned admission must be suppressed, the admissibility of any subsequent statement should turn in these circumstances solely on whether it is knowingly and voluntarily made,” <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#309" aria-description="Citation for case: Oregon v. Elstad">470 U.S. at 309</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. The Court reasoned that the police did not employ any coercive tactics to elicit <page-number citation-index="1" label="475">*475</page-number>either confession and that the defendant made his postwarning confession voluntarily. <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad"><em>Id. </em>at 316</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. The Court concluded that “the dictates of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and the goals of the Fifth Amendment proscription against use of compelled testimony are fully satisfied in the circumstances of this case.” <em>Id. </em>at 318, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>.</p>
<p id="b505-5">Whereas <em>Elstad </em>involved a good-faith effort by the police to administer a proper <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning, <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>addressed the use of a two-step interrogation strategy designed to elicit a <em>post-Miranda </em>waiver and confession after the defendant had already confessed before he was given <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. In <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>, </em>the police department had a policy of withholding <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings until an arrestee confessed and then reading the arrestee <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and asking for a waiver prior to eliciting a second confession. <em>Seibert, </em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#609" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 609-10</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (plurality opinion).<footnotemark>1</footnotemark> The police in <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>employed this strategy when they arrested the defendant for setting a fire that killed a teenager. <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#604" aria-description="Citation for case: Missouri v. Seibert"><em>Id. </em>at 604</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. After taking the defendant into custody and deliberately withholding <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, the police elicited a confession. <em>Id. </em>at 604-05, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. The police then gave the defendant a 20-minute break after which they provided her <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, obtained a signed waiver of rights, and tape-recorded a second confession. <em>Id. </em>at 605, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. A majority of the Court admonished against the use of this “question-first” technique and held that this strategy violated <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#617" aria-description="Citation for case: Missouri v. Seibert"><em>Miranda. Id. </em>at 617</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>; <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#620" aria-description="Citation for case: Missouri v. Seibert"><em>id. </em>at 620-21</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring).</p>
<p id="b505-7">The <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>plurality concluded that “[u]pon hearing warnings only in the aftermath of interrogation and just after making a confession, a suspect would hardly think he had a genuine right to remain silent, let alone persist in so believing once the police began to lead him over the same ground again.” <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#613" aria-description="Citation for case: Missouri v. Seibert"><em>Id. </em>at 613</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (plurality opinion). The plurality focused on whether the midstream <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning was effective, and questioned whether “it would be reasonable to find that in these circumstances the warnings could function ‘effectively’ as <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires .... [and] advise the suspect that he had a real choice about giving an admissible statement at that juncture.” <em>Id. </em>at 611-12, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. Writing for the plurality, Justice Souter laid out five factors to be weighed when analyzing the effectiveness of the warning: (1) “the completeness and detail of the questions and answers in the first round of interrogation,” (2) “the overlapping content of the two statements,” (3) “the timing and setting of the first and second” interrogation, (4) “the continuity of police personnel,” and (5) “the degree to which the interrogator’s questions treated the second round as continuous with the first.” <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#615" aria-description="Citation for case: Missouri v. Seibert"><em>Id. </em>at 615</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.</p>
<p id="b505-8">The plurality voted to suppress the second confession because, unlike in <em>Elstad, </em>the unwarned interrogation was “systematic, ejdiaustive, and managed with psychological skill.” <em>Id. </em>at 616, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. Applying the five factors, the plurality focused on the facts that: both phases of questioning occurred while the suspect was clearly in custody; there was no advice given to the suspect that her first statement was inadmissible; the same police <page-number citation-index="1" label="476">*476</page-number>officer conducted both interrogations in the same location with only a 15 to 20 minute break between the two; and references to the earlier confession fostered an “impression that the further questioning was a mere continuation” of the first interrogation. <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Id.</a></span> </em>The plurality ultimately concluded that “[t]hese circumstances must be seen as challenging the comprehensibility and efficacy of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to the point that a reasonable person in the suspect’s shoes would not have understood them to convey a message that she retained a choice about continuing to talk.” <em>Id. </em>at 617, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.</p>
<p id="b506-4">Justice Kennedy agreed with the plurality’s conclusion that the postwarning statements should be suppressed, but he believed the plurality’s test “cut too broadly,” <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert"><em>id. </em>at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, /., concurring), because it applied in instances of “both intentional and unintentional two-stage interrogations,” <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#621" aria-description="Citation for case: Missouri v. Seibert"><em>id. </em>at 621</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. Under Justice Kennedy’s approach, the first question would be whether law enforcement officers used a “deliberate two-step strategy” in “a calculated way to undermine the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning,” <em>id. </em>at 622, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>, and “to obscure both the practical and legal significance of the admonition when finally given,” <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#620" aria-description="Citation for case: Missouri v. Seibert"><em>id. </em>at 620</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. If the answer to that question were “no,” then the suppression analysis would be governed by the voluntariness standard set forth in <em>Elstad. <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Id.</a></span> </em>If the answer were “yes,” however, the next question would be whether any curative measures were taken “to ensure that a reasonable person in the suspect’s situation would understand the import and effect of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning and of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span> </em>Justice Kennedy provided two examples of such curative measures: (1) “a substantial break in time and circumstances between the prewarning statement and the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning ... [because] it allows the accused to distinguish the two contexts and appreciate that the interrogation has taken a new turn”; and (2) “an additional warning that explains the likely inadmissibility of the prewarning custodial statement.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span> </em>Reasoning that the police had used a deliberate two-step interrogation technique and that no curative steps had been taken, Justice Kennedy concluded that the post-warning statements were inadmissible. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></em></p>
<p id="b506-6">In <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span>, </em>this Court joined the Eleventh, Fifth, Ninth, Third, and Eighth Circuits in applying Justice Kennedy’s approach in <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>, </em>holding that <em>“Seibert </em>lays out an exception to <em>Elstad </em>for cases in which a deliberate, two-step strategy was used by law enforcement to obtain the postwarning confession.” <em>Carter, </em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/#535" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">489 F.3d at 535</a></span>. <em>Cf. United States v. Street, </em><span class="citation" data-id="77537"><a href="/opinion/77537/united-states-v-stanley-street/#1312" aria-description="Citation for case: United States v. Stanley Street">472 F.3d 1298, 1312</a></span> (11th Cir.2006); <em>United States v. Courtney, </em><span class="citation" data-id="45540"><a href="/opinion/45540/united-states-v-courtney/#338" aria-description="Citation for case: United States v. Courtney">463 F.3d 333, 338</a></span> (5th Cir.2006); <em>United States v. Williams, </em><span class="citation" data-id="793121"><a href="/opinion/793121/united-states-v-tashiri-wayne-williams/#1157" aria-description="Citation for case: United States v. Tashiri Wayne Williams">435 F.3d 1148, 1157</a></span> (9th Cir.2006); <em>United States v. Kiam, </em><span class="citation" data-id="792714"><a href="/opinion/792714/united-states-v-long-tong-kiam/#532" aria-description="Citation for case: United States v. Long Tong Kiam">432 F.3d 524, 532</a></span> (3d Cir.2006); <em>United States v. Hernandez-Hernandez, </em><span class="citation" data-id="787857"><a href="/opinion/787857/united-states-v-ervey-hernandez-hernandez/#566" aria-description="Citation for case: United States v. Ervey Hernandez-Hernandez">384 F.3d 562, 566</a></span> (8th Cir.2004). <em>But see United States v. Heron, </em><span class="citation" data-id="1192547"><a href="/opinion/1192547/united-states-v-heron/#884" aria-description="Citation for case: United States v. Heron">564 F.3d 879, 884-85</a></span> (7th Cir.2009) (Justice Kennedy’s concurrence is not controlling). In <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span>, </em>law enforcement agents recovered a large bag of drugs after searching a restaurant owned and operated by the suspect. <span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/#531" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam"><em>Id. </em>at 531</a></span>. Approximately 30 minutes after the search concluded, an agent noticed the suspect sitting outside the restaurant and, in a casual fashion, asked him about a brown substance found in the bag of drugs. The agent asked if the substance was heroin, and the suspect replied, “No, it’s bad.” <span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/#532" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam"><em>Id. </em>at 532</a></span>. The agent then asked, “Bad what?,” to which the suspect replied, “Bad coke.” <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Id.</a></span> </em>The agent later testified that he asked the suspect about the drugs solely “out of curiosity.” <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Id.</a></span> </em>Approximately 30 <page-number citation-index="1" label="477">*477</page-number>minutes later, after the defendant was given a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning and after he signed a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver form, a different agent conducted a formal interrogation and elicited a full confession. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#533" aria-description="Citation for case: Miranda v. Arizona"><em>Id. </em>at 533</a></span>. The latter agent had no knowledge of the suspect’s previous statement about the brown substance and did not learn about it until shortly before the trial commenced. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span> </em>The defendant moved to suppress the second confession on the grounds that he did not knowingly and voluntarily waive his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#534" aria-description="Citation for case: Miranda v. Arizona"><em>Id. </em>at 534</a></span>.</p>
<p id="b507-5">Analyzing “[t]he factual differences between [Carter’s] case and <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#536" aria-description="Citation for case: Miranda v. Arizona"><em>Seibert,” id. </em>at 536</a></span>, we determined that the agents in <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span> </em>did not deliberately use a two-step interrogation strategy designed to circumvent <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>for three reasons: (1) there was almost no overlap between the suspect’s first statement and his subsequent confession; (2) different officers questioned the suspect at different locations (the first outside the store that was being searched and the second in an interrogation room), and the second officer was not aware of the suspect’s previous inculpatory statement; and (3) “the postwarning questioning was not a continuation of the prewarning question.”<footnotemark>2</footnotemark> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#536" aria-description="Citation for case: Miranda v. Arizona"><em>Id. </em>at 536</a></span>. Accordingly, applying <em>Elstad, </em>we determined that <em>Carter’s </em>postwarning statement was made knowingly and voluntarily, and it was properly admissible at trial. <em>Id. </em>at 536-37.</p>
<p id="b507-6">Here, in a decision that predated <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span>, </em>the district court found that Capers did not give his <em>post-Miranda </em>warning statement “voluntarily with a full awareness of the rights being waived and the consequences of doing so.” <em>Capers, </em><span class="citation no-link">2007 WL 959300</span>, at * 15 (internal quotation marks omitted). For that reason, it suppressed Capers’ statement. In so doing, the district court rejected Justice Kennedy’s approach in <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>, </em>explaining that Justice Kennedy’s concurring opinion “cannot reasonably be taken to be the law of the land,” because it did not represent the majority opinion of the Supreme Court. <em>Id. </em>at *11 (internal quotation marks omitted).</p>
<p id="b507-10">In a footnote to its decision, the district court remarked that “if Justice Kennedy’s <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>concurrence represented the law, suppression would be denied.” <em>Capers, </em><span class="citation no-link">2007 WL 959300</span>, at *15 n.17. The district court based this statement, which under the circumstances constituted dictum, on its understanding that Justice Kennedy’s test turned on “the subjective intent of the police,” <span class="citation no-link"><em>id. </em>at *10</span>, coupled with the district court’s own determination that the inspectors in this case did not have the “specific intent” to evade <span class="citation no-link"><em>Miranda, id. </em>at *12</span>.</p>
<p id="b507-11">Our intervening decision in <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span>, </em>however, requires a different analysis. Under <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span>, </em>we must address whether the officers employed a “deliberate, two-step strategy, predicated upon violating <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>during an extended interview,” <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#621" aria-description="Citation for case: Missouri v. Seibert"><em>Seibert, 542 </em>U.S. at 621</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>, and if so, whether “specific, curative steps,” <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">id.,</a></span> </em>were taken to obviate the violation that occurred.</p>
<p id="b507-12">III. Deliberateness</p>
<p id="b507-13">In <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>, </em>because the record was clear that the interrogating officers intentionally and purposefully employed a technique in which they had been instructed, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#609" aria-description="Citation for case: Missouri v. Seibert"><em>id. </em>at 609-10</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>, Justice Kennedy had no reason to explore how a court should determine when a two-step interrogation strategy had been executed deliberately. <page-number citation-index="1" label="478">*478</page-number>Wrestling with the problem we now address, the Ninth Circuit has stated:</p>
<blockquote id="b508-4">As an initial matter, we note that Justice Kennedy did not articulate how a court should determine whether an interrogator used a deliberate two-step strategy- • • •</blockquote>
<blockquote id="b508-5">For example, Justice Kennedy’s opinion is silent as to what, if any presumptions apply or which party bears the burden of proving or disproving deliberateness.</blockquote>
<p id="b508-6"><em>United States v. Williams, </em><span class="citation" data-id="793121"><a href="/opinion/793121/united-states-v-tashiri-wayne-williams/" aria-description="Citation for case: United States v. Tashiri Wayne Williams">435 F.3d 1148</a></span>, 1158 &amp; n. 11 (9th Cir.2006).</p>
<p id="b508-7">In constructing a method to determine deliberateness, the Ninth Circuit in <em><span class="citation" data-id="793121"><a href="/opinion/793121/united-states-v-tashiri-wayne-williams/" aria-description="Citation for case: United States v. Tashiri Wayne Williams">Williams</a></span> </em>looked to whether “objective evidence and any available subjective evidence, such as an officer’s testimony, support an inference that the two-step interrogation procedure was used to undermine the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning.” <em>Id. </em>at 1158. Following on the Ninth Circuit’s guidance, the test articulated by the Eleventh Circuit to determine deliberateness relies upon “the totality of the circumstances including ‘the timing, setting and completeness of the prewarning interrogation, the continuity of police personnel and the overlapping content of the pre- and post-warning statements.’ ” <em>United States v. Street, </em><span class="citation" data-id="77537"><a href="/opinion/77537/united-states-v-stanley-street/#1314" aria-description="Citation for case: United States v. Stanley Street">472 F.3d 1298, 1314</a></span> (11th Cir.2006) (quoting <em>Williams, </em><span class="citation" data-id="793121"><a href="/opinion/793121/united-states-v-tashiri-wayne-williams/#1159" aria-description="Citation for case: United States v. Tashiri Wayne Williams">435 F.3d at 1159</a></span>). The Fifth Circuit’s articulation of when deliberateness may be inferred also relies upon the totality of the circumstances surrounding the interrogations:</p>
<blockquote id="b508-9">[Tjhere was nothing in the circumstances or the nature of the questioning to indicate that coercion or other improper tactics were used. All evidence suggests that Nunez was calm and cooperative, and the agents did not act with aggressiveness or hostility. The district court stated that “the defendant initially had done nothing more than voluntarily respond to questions as to his name, place of birth, and immigration status.”</blockquote>
<p id="A0M"><em>United States v. Nunez-Sanchez, </em><span class="citation" data-id="47927"><a href="/opinion/47927/united-states-v-nunez-sanchez/#668" aria-description="Citation for case: United States v. Nunez-Sanchez">478 F.3d 663, 668-669</a></span> (5th Cir.2007).<footnotemark>3</footnotemark></p>
<p id="b508-10">In our Court’s opinion in <em>Carter, </em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/#528" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">489 F.3d at 528</a></span>, without expressly stating that we were doing so, we similarly analyzed objective factors. In the context of the interrogation that took place there, we needed only to consider three factors to conclude that the interrogating officers did not deliberately employ a two-step interrogation procedure: (1) there was no overlap between the suspect’s first and second statements; (2) different officers questioned the suspect at different locations, and the second officer was not aware of the suspect’s previous inculpatory statement; and (3) “the postwarning questioning was not a continuation of the prewarning question[ing].” <em>Carter, </em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/#536" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">489 F.3d at 536</a></span>.</p>
<p id="b508-11">These considerations, while determinative of the analysis of deliberateness on the facts presented in <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span>, </em>are by no means the only factors to be considered when seeking to divine whether the officers’ actions are sufficiently indicative of a deliberate circumvention of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to <page-number citation-index="1" label="479">*479</page-number>require that a defendant’s statements must be suppressed. We recognize the wisdom of Justice Souter’s observation that “the intent of the officer will rarely be as candidly admitted as it was” in <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>, </em>where the interrogating officer testified not only that he was trained to execute a two-step interrogation procedure but also implied that the tactic is taught nationwide. <em>Seibert, </em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 616</a></span> n. 6, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. In light of the above, we join our sister circuits in concluding that a court should review the totality of the objective and subjective evidence surrounding the interrogations in order to determine deliberateness, with a recognition that in most instances the inquiry will rely heavily, if not entirely, upon objective evidence. <em>Cf. Seibert, </em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, concurring) (“[A] multifactor test that applies to every two-stage interrogation may serve to undermine th[e] clarity [of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>].”).</p>
<p id="b509-5">Recognizing the inherent difficulty in proving deliberateness, and also conceding that “determining the officer’s state of mind at the time of the interrogation can be difficult,” we turn to the unsettled question of which party bears the burden of proving deliberateness or absence thereof. <em>United States v. Ollie, </em><span class="citation" data-id="793845"><a href="/opinion/793845/united-states-v-johnny-lee-ollie-jr/#1142" aria-description="Citation for case: United States v. Johnny Lee Ollie, Jr.">442 F.3d 1135, 1142</a></span> (8th Cir.2006). For the following reasons, we hold that the burden rests on the prosecution to disprove deliberateness.</p>
<p id="b509-6">“[Wjhen a confession challenged as involuntary is sought to be used against a criminal defendant at his trial, he is entitled to a reliable and clear-cut determination that the confession was in fact voluntarily rendered.” <em>Lego v. Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey">404 U.S. 477, 489</a></span>, <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">92 S.Ct. 619</a></span>, <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">30 L.Ed.2d 618</a></span> (1972). Accordingly, courts place upon the government the burden to prove that a defendant’s confession was voluntary. <em>See, e.g., Colorado v. Connelly, </em><span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#168" aria-description="Citation for case: Colorado v. Connelly">479 U.S. 157, 168</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">107 S.Ct. 515</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">93 L.Ed.2d 473</a></span> (1986). The question of deliberateness, while distinct from voluntariness, will nonetheless be dispositive of a defendant’s challenge to the voluntariness of a confession garnered from a two-step interrogation procedure. <em>See United States v. Stewart, </em><span class="citation" data-id="1401670"><a href="/opinion/1401670/united-states-v-stewart/#719" aria-description="Citation for case: United States v. Stewart">536 F.3d 714, 719</a></span> (7th Cir.2008). The Eighth Circuit, which also places the burden on the government to disprove deliberateness, cautioned that while “the law generally frowns on requiring a party to prove a negative,” the Supreme Court has consistently required the government to prove the admissibility of a confession against a criminal defendant, <em>Ollie, </em><span class="citation" data-id="793845"><a href="/opinion/793845/united-states-v-johnny-lee-ollie-jr/#1143" aria-description="Citation for case: United States v. Johnny Lee Ollie, Jr.">442 F.3d at 1143</a></span>. <em>See also Brown v. Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590, 603-04</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span> (1975) (requiring the government to show that a confession was not the fruit of an earlier illegal arrest); <em>Connelly, </em><span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#168" aria-description="Citation for case: Colorado v. Connelly">479 U.S. at 168</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">107 S.Ct. 515</a></span> (requiring the government to show that defendant’s <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver given during an alleged psychotic episode, was knowing and voluntary).</p>
<p id="b509-8">Indeed, the Supreme Court has “always set high standards of proof for the waiver of constitutional rights.... ” <em>Tague v. Louisiana, </em><span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/#470" aria-description="Citation for case: Tague v. Louisiana">444 U.S. 469, 470</a></span>, <span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/" aria-description="Citation for case: Tague v. Louisiana">100 S.Ct. 652</a></span>, <span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/" aria-description="Citation for case: Tague v. Louisiana">62 L.Ed.2d 622</a></span> (1980). In <em><span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/" aria-description="Citation for case: Tague v. Louisiana">Tague</a></span>, </em>the Court held: “Since the State is responsible for establishing the isolated circumstances under which the interrogation takes place and has the only means of making available corroborated evidence of warnings given during incommunicado interrogation, the burden is rightly on its shoulders.” <em><span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/" aria-description="Citation for case: Tague v. Louisiana">Id.</a></span> </em>Guided by <em><span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/" aria-description="Citation for case: Tague v. Louisiana">Tague</a></span>, </em>we are mindful that evidence of deliberateness or lack thereof is similarly in the hands of the government, and we are further persuaded that the party seeking to introduce the confession should remain responsible for showing that it was not obtained through a subterfuge.</p>
<p id="b510-3"><page-number citation-index="1" label="480">*480</page-number> With respect to the quantum of proof necessary, we are mindful that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>may impose a “heavy burden [upon] the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination,” and that in order to satisfy that burden a “high standarfd] of proof’ is applicable. <em>Berghuis v. Thompkins, </em>— U.S. -, <span class="citation" data-id="6680916"><a href="/opinion/6796082/berghuis-v-thompkins/#2272" aria-description="Citation for case: Berghuis v. Thompkins">130 S.Ct. 2250, 2272</a></span>, <span class="citation" data-id="6680916"><a href="/opinion/6796082/berghuis-v-thompkins/" aria-description="Citation for case: Berghuis v. Thompkins">176 L.Ed.2d 1098</a></span> (2010) (Sotomayor, dissenting). Nonetheless, “[w]henever the State bears the burden of proof in a motion to suppress a statement that the defendant claims was obtained in violation of our <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>doctrine, the State need prove waiver only by a preponderance of the evidence.” <em>Connelly, </em><span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#168" aria-description="Citation for case: Colorado v. Connelly">479 U.S. at 168</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">107 S.Ct. 515</a></span>. We apply the preponderance standard to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>challenges in recognition that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is an exclusionary rule “aimed at deterring lawless conduct by police and prosecution,” and that imposing a higher burden of proof would do little to mitigaté prosecutorial overreaching while at the same time concealing troves of probative evidence from the eyes of the jury. <em>Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey">404 U.S. at 489</a></span>, <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">92 S.Ct. 619</a></span>. For similar reasons, we hold that the government must meet its burden of disproving the deliberate use of a two-step interrogation technique by a preponderance of the evidence.</p>
<p id="b510-6">Looking to the totality of the circumstances in the case before us, the evidence proffered by the government to show that Capers was not the subject of a deliberate, two-step interrogation is outweighed by subjective and objective evidence to the contrary. Hoti testified that he delayed issuing a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning because his “mindset was on, one ... recovering evidence, ... [a]s well as determining if the two of them or if — either both of them or only one of them had any role to play in committing the crime.” (Hr’g Tr. 65.) Hoti testified that he was concerned about losing the money orders in the “very, very large” facility because the money orders were about the size of a U.S. dollar and the defendants could “toss them, hide them ... [and] [y]ou’d have a real, real tough time finding [them] in this large facility like that with all the packages and other types of mail.” (Hr’g Tr. 31-31.) As to making a determination about defendant Lopez, Hoti testified that “[i]f I could determine fairly quickly that, in fact, he had no role to play in that crime, I need to take those cuffs off and basically cut him loose.” (Hr’g. Tr. 35.) When asked whether he was in a position to read Capers his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings before asking him about the money orders, Hoti replied “absolutely.” (Hr’g. Tr. 65.)</p>
<p id="b510-8">The district court concluded from this testimony that Hoti’s purpose in delaying a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning was not to undermine Capers’ Fifth Amendment rights, but rather “to prevent the loss or concealment of the currency and money orders that the Express Mail envelopes contained, and to ascertain whether Lopez was involved in the crime, so that he could be freed or not.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span> </em>at *12 n. 13 (citation omitted). Neither of these reasons, however, justifies delaying a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning once it is obvious that a suspect is in custody. There is no exception to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that allows a delay in giving <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings in order to preserve evanescent evidence. Neither is there an exception to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that permits delaying the warnings in order to ascertain whether a suspected co-conspirator may be entitled to release. Indeed, we agree with the <em><span class="citation" data-id="793121"><a href="/opinion/793121/united-states-v-tashiri-wayne-williams/" aria-description="Citation for case: United States v. Tashiri Wayne Williams">Williams</a></span> </em>Court in its observation that</p>
<blockquote id="b510-9">[o]nce a law enforcement officer has detained a suspect <em>and subjects him to interrogation ... </em>there is rarely, if ever, a legitimate reason to delay giving a <page-number citation-index="1" label="481">*481</page-number><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning until after the suspect has confessed. Instead, the most plausible reason ... is an <em>illegitimate </em>one, which is the interrogator’s desire to weaken the warning’s effectiveness.</blockquote>
<p id="b511-5"><span class="citation" data-id="793121"><a href="/opinion/793121/united-states-v-tashiri-wayne-williams/#1159" aria-description="Citation for case: United States v. Tashiri Wayne Williams">435 F.3d at 1159</a></span>. The only legitimate reason to delay intentionally a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning until after a custodial interrogation has begun is to protect the safety of the arresting officers or the public — neither of which was an issue here. <em>See, e.g., United States v. Newton, </em><span class="citation" data-id="786350"><a href="/opinion/786350/united-states-v-sewn-newton/#677" aria-description="Citation for case: United States v. Sewn Newton">369 F.3d 659, 677</a></span> (2d Cir.2004) (recognizing this “narrow exception” to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule).</p>
<p id="b511-6">Inexperience, while not a legitimate excuse for postponing a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning, nevertheless may save a confession from exclusion under <em>Seibert. See United States v. Naranjo, </em><span class="citation" data-id="792184"><a href="/opinion/792184/united-states-v-adolfo-naranjo/#232" aria-description="Citation for case: United States v. Adolfo Naranjo">426 F.3d 221, 232</a></span> (3d Cir.2005) (implying that an “inadvertent” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>omission, or a “rookie mistake,” should not warrant <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>scrutiny). In the case before us, however, sufficient subjective evidence was adduced to rule out the officers’ inexperience as well as raise significant doubts as to whether a mistake had been made. The district court found it clear from Hoti’s testimony and from his experience in law enforcement that his failure to Mirandize Capers was not an accident. The district court explained: “Inspector Hoti did not merely forget to give defendant <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. Inspector Hoti had served as a New York City police officer for some three years, and as Inspector Del Giudice testified, postal inspectors are ‘trained to provide <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>when there is a custodial interrogation.’ ” <em>Capers, </em><span class="citation no-link">2007 WL 959300</span> at *12 (quoting Hr’g Tr. 165). Indeed, Hoti explicitly testified that he “absolutely” was in a position to inform Capers of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights once Capers was confined to the supervisor’s office. (Hr’g Tr. 65.) The arrest of Capers did not occur “out of the blue,” as it might were Hoti driving to work and witnessed a crime in progress, or were he responding to a radio call reporting a crime in progress. Capers’ arrest was the culmination of a nine-month investigation into Capers’ suspected criminal activity. In surveiling Capers and determining when to give the order to his team to descend on Capers and Lopez, therefore, Hoti had time to think through what procedural steps he would need to take following arrest in order to build his case for prosecution. Because, as the district court found, Hoti had sufficient experience to know that a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning was unquestionably necessary in connection with Capers’ post-arrest interrogation, the corollary to that finding must also obtain. Hoti was experienced enough to know that in this case there was no valid reason to delay a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning until after questioning a suspect in custody.</p>
<p id="b511-8">The district court found that there was “no evidence ... that Inspector Hoti had the specific intent to use the two-stage questioning technique” to undermine Capers’ <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. <em>Capers, </em><span class="citation no-link">2007 WL 959300</span> at *12. The dissent endorses this finding, arguing that “there is nothing suspicious about the reasons put forth by Inspector Hoti.” Dissent at 492. Considering the totality of the circumstances, however, we find Inspector Hoti’s proffered reasons for delaying the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning to lack not only legitimacy, but also credibility. Inspector Hoti explained that he delayed informing Capers of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights because Hoti had to determine if Lopez was involved in the scheme, and if he was not, release him. If Capers had told Inspector Hoti during the initial interrogation that Lopez had nothing to do with the scheme, would Inspector Hoti, who had just witnessed the two men enter a storage container and the envelope alarms subsequently sound, then have released Lopez on his own recognizance? We consider such a conclusion dubious. With respect to Hoti’s claim that he did not want to lose <page-number citation-index="1" label="482">*482</page-number>the money orders and cash in the large postal facility, this assertion is belied by the testimony of the arresting officers that Capers and Lopez were detained almost directly after the envelope alarm sounded and were found either still in the storage container, or in that immediate vicinity. In light of the above, as well as objective evidence discussed below, the district court’s finding that there was “no evidence” of a deliberate, two-step interrogation tactic at work was clear error. <em>Capers, </em><span class="citation no-link">2007 WL 959300</span> at *12.</p>
<p id="b512-4">The dissent asserts that the “test used by the majority to determine whether Inspector Hoti deliberately utilized a two-step interrogation technique effectively undermines the subjective test established by Justice Kennedy ... because it ignores subjective evidence showing that the inspector did not deliberately utilize a two-step technique, and instead relies exclusively on the objective factors listed in the non-controlling <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>plurality opinion.” Dissent at 491. This conclusion misreads our analysis and conflates Justice Kennedy’s test with that articulated by Justice Breyer in his concurring opinion in <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#617" aria-description="Citation for case: Missouri v. Seibert"><em>Seibert. 542 </em>U.S. at 617</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Breyer, J., concurring) (“Courts should exclude the ‘fruits’ of the initial unwarned questioning unless the failure to warn was in good faith.”) (citations omitted). By contrast, our analysis considers the subjective evidence adduced at the suppression hearing in the context set forth by Justice Kennedy — as instructive but not automatically dispositive. Justice Kennedy’s concurrence in <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>does not advocate a test whereby a deliberate two-step interrogation will be found only when a law enforcement officer admits to executing such a strategy. Nor does this test envision blind, unquestioning reliance on the testimony of arresting and interrogating officers. To the contrary, because Justice Kennedy’s test seeks to exclude only those statements that are the result of <em>deliberate </em>and <em>calculated </em>police strategies to undermine <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>a searching and penetrating inquiry of the officer’s testimony and proffered reasons for delaying <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning is therefore necessary to determine when these strategies are being employed.</p>
<p id="b512-6">The dissent asserts that the above consideration “gives absolutely no weight to the inspector’s testimony that his reasons for not immediately advising Capers of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights were to prevent the loss or concealment of the currency and money orders that the Express Mail envelope contained and to ascertain whether Lopez was involved in the crime.” Dissent at 492. The dissent argues that Judge McKenna “witnessed Inspector Hoti’s testimony and was therefore better able to assess his credibility.” Dissent at 492. Although appellate courts do not have the opportunity to observe witness testimony and are, therefore, precluded from making credibility determinations, in light of the clear inconsistency between Inspector Hoti’s stated reasons for delaying <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and the objective and subjective evidence constituting the remainder of the record bearing on this point, it is clear the district court’s determination “that there is no evidence ... Inspector Hoti had the specific intent to use the two-stage questioning technique with the purpose of first obtaining unwarned incriminating statements in order, in a subsequent warned interrogation, to obtain similar incriminating statements,” <em>Capers, </em><span class="citation no-link">2007 WL 959300</span> at *12, afforded blind and absolute weight to the testimony of the arresting officers and ignored all the other relevant evidence which we here announce must <page-number citation-index="1" label="483">*483</page-number>also be considered.<footnotemark>4</footnotemark> If Justice Kennedy’s test is to have any meaning outside of the unique and never-again-to-be-repeated circumstances of <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>, </em>the district court’s unidimensional analysis cannot be determinative of the outcome in this case.</p>
<p id="b513-5">Objective evidence also leads us to conclude that the Government has failed to meet its burden of demonstrating that Capers was not subjected to a two-step interrogation. First, there is considerable overlap between the statements elicited from the defendant during the first and second interrogation. Hoti’s initial interrogation of Capers resulted in a confession and “there remained ‘little, if anything, of incriminating potential left unsaid.’ ” <em>Capers, </em><span class="citation no-link">2007 WL 959300</span>, at *13 (quoting <em>Seibert, </em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#616" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 616</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (plurality opinion)). The circumstances surrounding the two sessions of the interrogation, including the nature of the respective environs in which the interrogation took place and the continuity of the cast of interrogating officers, was indicative of a deliberate two-step interrogation. While the location of the interrogation sessions changed, the first taking place in a room at the post office and the second in the Domicile, the inquisitorial environment of the questioning was consistent.</p>
<p id="b513-6">Unlike in <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span>, </em>the initial conversation between Capers and Hoti was in no way casual. <em>See Nunez-Sanchez, </em><span class="citation" data-id="47927"><a href="/opinion/47927/united-states-v-nunez-sanchez/#663" aria-description="Citation for case: United States v. Nunez-Sanchez">478 F.3d at 663-69</a></span>. It began with Hoti’s opening statement to Capers that “I’m going to do my best to make you go away, and I just want you to know.” (Hr’g Tr. 95.) Capers was handcuffed throughout the process. On the facts presented, the district court correctly concluded, and we agree, that Hoti’s initial questioning was indeed a formal interrogation. <em>See Capers, </em><span class="citation no-link">2007 WL 959300</span>, at *4 (concluding that Capers was in custody from the moment he was handcuffed).</p>
<p id="b513-9">Between the two phases of the interrogation, Hoti’s fellow inspectors engaged Capers in “small talk,” and advised him that it was in his interest to tell the truth when Hoti arrived. Capers continued to be handcuffed throughout the process. The second phase of the interrogation also opened with a hostile remark, namely Hoti’s observation that Capers was “one of the most laziest employees I’ve ever seen.” <em>Cf. Nunez-Sanchez, </em><span class="citation" data-id="47927"><a href="/opinion/47927/united-states-v-nunez-sanchez/#668" aria-description="Citation for case: United States v. Nunez-Sanchez">478 F.3d at 668-69</a></span> (finding that there was “no evidence of a deliberate attempt to employ a two-step strategy” because, <em>inter alia, </em>“the agents did not act with aggressiveness or hostility”). In combination with the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning, the inspectors clearly established that this second encounter was not a casual conversation. For the most part there was also continuity in the officers present at both interrogations. During the first interrogation Hoti asked the questions, while Del Giudice and Moon were present in the room. The second interrogation, at the outset, involved the same three inspectors with Hoti again asking the questions and Del Giudice and Moon remaining silent.</p>
<p id="b514-3"><page-number citation-index="1" label="484">*484</page-number>Finally, the temporal proximity of the pre- and post-warning interrogations, along with the continuity of Caper’s custody, reasonably leads to the conclusion that the latter was a continuation of the former. Only 90 minutes separated the two interrogation sessions. And while not carried out to the degree it was in <em>Seibert, </em>at least to some extent the latter session was “essentially a cross-examination using information gained during the first round of interrogation.” <em>See Carter, </em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/#536" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">489 F.3d at 536</a></span>. Accordingly, the government has not produced sufficient objective evidence to meet its burden to dispel a conclusion that Hoti’s conduct amounted to a deliberate “question first” interrogation tactic designed to undermine Capers’ exercise of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights.<footnotemark>5</footnotemark></p>
<p id="b514-4">IV. Curative Measures</p>
<p id="b514-5">Deliberateness having been established, we must next consider whether any curative measures intervened to restore the defendant’s opportunity voluntarily to exercise his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. <em>See Seibert, </em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, <em>J., </em>concurring) (“[P]ostwarning statements that are related to the substance of prewarning statements must be excluded unless curative measures are taken before the postwarning statement is made.”). As noted, Justice Kennedy provided two examples of potential curative measures: (1) “a substantial break in time and circumstances between the prewarning statement and the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning,” and (2) “an additional warning that explains the likely inadmissibility of the prewarning custodial statement.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span> </em>Based on the facts before us, we cannot say that any such curative measure occurred such that it rendered effective the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings given to Capers before the second interrogation.</p>
<p id="b514-8">As discussed, although approximately 90 minutes passed between the first and second interrogations, the two rounds of questioning bracketed one continual process. Del Giudice and Moon were with Capers throughout the 90 minutes, engaging in “small talk” and advising Capers to tell the truth. Despite the different locations of the interrogation sessions, both occurred while Capers remained in handcuffs and in settings that clearly established the authoritative nature of the questioning. There is little meaningful difference between the circumstances surrounding Capers’ two interrogation sessions, and there was certainly no “substantial break” that would have restored his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights.</p>
<p id="b514-9">Moreover, despite Hoti’s knowledge that Capers’ first statement would be inadmissable in court, he never alerted Capers to that fact. <em>Capers, </em><span class="citation no-link">2007 WL 959300</span>, at *14. Hoti continued his line of questioning without dispelling Capers’ probable assumption that he had already incriminated himself based on his first confession. Hoti revealed as much in his testimony. When <page-number citation-index="1" label="485">*485</page-number>asked whether he posed some of the same questions at the Bronx Domicile as he had asked earlier in the supervisor’s office, Hoti replied that he did not see the need to ask the same questions for which he already had answers. (Hr’g Tr. 72.) By the same token, Hoti did build on Capers’ admission of theft in the original session by structuring the second interrogation session to elicit a play-by-play description of how Capers went about stealing the money orders. Capers thus had no reason to know that his first broad confession could not be used against him when, only 90 minutes later while still in close custody, he actually “waived” his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights.<footnotemark>6</footnotemark> On these facts, there were no measures taken to cure the inspectors’ use of the deliberate, two-step interrogation strategy. Because on the objective and subjective evidence we are left to conclude that the inspectors employed a strategy to circumvent the defendant’s <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights and because there were no curative measures to ensure that the defendant was not misled with regard to his rights prior to his second confession, Capers’ waiver of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights was invalid. The district court, therefore, properly suppressed his post-warning confession.</p>
<p id="b515-5">CONCLUSION</p>
<p id="b515-6">For the foregoing reasons, we AFFIRM the district court’s decision to suppress the defendant’s post <em>-Miranda </em>statements.</p>
<footnote label="1">
<p id="b505-6">. The Supreme Court noted a police officer’s testimony at trial that the two-step strategy was promoted by his department, as well as by a national police training organization and was corroborated by a manual from the Police Law Institute, which provided instruction on the technique. <em>Seibert, </em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#609" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 609-10</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (plurality opinion).</p>
</footnote>
<footnote label="2">
<p id="b507-7">. Because we concluded that the <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>approach was inapplicable in <em><span class="citation" data-id="9499740"><a href="/opinion/798020/united-states-v-johnny-carter-micheal-bearam/" aria-description="Citation for case: United States v. Johnny Carter, Micheal Bearam">Carter</a></span>, </em>we did not reach the issue of whether the police undertook any curative measures such that the suspect “would understand the import and effect of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning and of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver.” <em>Seibert, </em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, <em>J., </em>concurring).</p>
</footnote>
<footnote label="3">
<p id="b508-8">. In an unpublished Order and Judgment the Tenth Circuit, while declining to endorse either Kennedy’s concurrence or the <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>plurality opinion as the holding of <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>, </em>explained in <em>United States v. Crisp, </em><span class="citation" data-id="1243"><a href="/opinion/1243/united-states-v-crisp/#932" aria-description="Citation for case: United States v. Crisp">371 Fed.Appx. 925, 932</a></span> (10th Cir.2010), that the defendant's argument that his pre-warning statement was the product of a deliberate two-step interrogation was unavailing because no coercion was evident in either the surrounding circumstances or the content of the questioning, the pre-arrest statement "occurred after the parties had bantered about the pursuit and in response to a question about the marijuana use” of the defendant's female companion, and "the <em>pre-Miranda </em>statements also were unrelated to the <em>post-Miranda </em>statements regarding cocaine base.”</p>
</footnote>
<footnote label="4">
<p id="b513-7">. We note that in light of the district court's conclusion that “Justice Kennedy’s concurrence ... cannot reasonably be taken to be the 'law of the land,’ ” it likely did not avail itself of a number of opinions by our sister circuits, which have been instructive in our analysis, advising trial courts how to gauge deliberateness under Justice Kennedy's <em><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span> </em>concurrence. <em>See Street, </em><span class="citation" data-id="77537"><a href="/opinion/77537/united-states-v-stanley-street/#1312" aria-description="Citation for case: United States v. Stanley Street">472 F.3d at 1312</a></span> (11th Cir.2006); <em>Courtney, </em><span class="citation" data-id="45540"><a href="/opinion/45540/united-states-v-courtney/#338" aria-description="Citation for case: United States v. Courtney">463 F.3d at 338</a></span> (5th Cir.2006); <em>Williams, </em><span class="citation" data-id="793121"><a href="/opinion/793121/united-states-v-tashiri-wayne-williams/#1157" aria-description="Citation for case: United States v. Tashiri Wayne Williams">435 F.3d at 1157</a></span> (9th Cir.2006); <em>Kiam, </em><span class="citation" data-id="792714"><a href="/opinion/792714/united-states-v-long-tong-kiam/#532" aria-description="Citation for case: United States v. Long Tong Kiam">432 F.3d at 532</a></span> (3d Cir.2006); <em>Hernandez-Hernandez, </em><span class="citation" data-id="787857"><a href="/opinion/787857/united-states-v-ervey-hernandez-hernandez/#566" aria-description="Citation for case: United States v. Ervey Hernandez-Hernandez">384 F.3d at 566</a></span> (8th Cir.2004). Indeed it appears as though the district court thought that the Kennedy test required it to analyze only the statements of the offending officer, without reference to any other facts, possibly contradictory to the statements of the officer, that appeared on the record.</p>
</footnote>
<footnote label="5">
<p id="b514-6">. The dissent argues that under the test outlined above “in almost all cases where a prewarning confession is suppressed due to a violation of the suspect’s <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, a subsequent post-warning confession will also be suppressed because the interrogating officer will be unable to articulate a 'legitimate' reason for not advising the suspect of his or her <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights prior to the initial interrogation.” Dissent at 493. This conclusion also misreads our reasoning. To the contrary, there be will many occasions where the totality of the circumstances surrounding the two interrogations leads to the conclusion that a two-step interrogation was the product of a "rookie mistake,” resulted from poor communication among investigating officers, or occurred when an experienced officer suffered a momentary lapse in judgment. What will require higher scrutiny are situations where, as here, an experienced officer conducts both interrogations, and the reasons proffered for not initially <em>Mirandizing </em>a suspect are not only questionable but also inherently lack credibility in light of the totality of the circumstances.</p>
</footnote>
<footnote label="6">
<p id="b515-9">. Consideration of whether or not curative measures were taken is an inquiry separate and apart from determining deliberateness. When analyzing deliberateness, however, courts may consider an experienced officer’s failure to warn a suspect that an earlier admission, known to the interrogating officer, is inadmissible. Indeed such an omission on the part of the interrogating officer is probative of a "calculated” plan to subvert <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Carloss.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Carloss"
type: case
citation: "818 F.3d 988 (2016)"
parallel_cite: ""
neutral_cite: "2016 WL 929663; 2016 U.S. App. LEXIS 4547"
court: "U.S. Court of Appeals, 10th Circuit"
court_level: coa
circuit: 10th
year: 2016
date_decided: 2016-03-11
docket: 13-7082
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2016-03-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Carloss
  varies_by_point: false
  scope_note: "Good law. Then-Judge Gorsuch dissented, illustrating the divide over whether 'No Trespassing' signage revokes the implied knock-and-talk license."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/3184928/united-states-v-carloss/"
  cluster_id: 3184928
  opinion_id: 9822082
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Illustrates a circuit split"
related: ["[[Florida v. Jardines]]", "[[Oliver v. United States]]", "[[United States v. Walker]]", "[[United States v. Lundin]]", "[[French v. Merrill]]"]
aliases: ["United States v. Ralph Carloss", "United States v. Carloss (10th Cir. 2016)"]
tags: ["case", "fourth-amendment", "knock-and-talk", "implied-license", "no-trespassing", "curtilage", "tenth-circuit"]
holding: "On these facts, 'No Trespassing' signs posted around a home and on its front door did not revoke the implied license that lets an officer, like any citizen, approach the front door and knock to seek a consensual conversation; whether signage revokes the license is judged by what an objective officer would perceive, and a 'No Trespassing' sign by itself is not enough."
lake:
  record_id: United States v. Carloss
  status: verified
  projected_at: 2026-07-06
---

# United States v. Carloss

*818 F.3d 988 (10th Cir. 2016)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on information that Ralph Carloss possessed a machine gun, two officers went to the house where he was staying and knocked on the front door, seeking to speak with him. The home had "No Trespassing" signs posted in the unenclosed front and side yards and along the driveway, plus a sign on the front door reading "Posted Private Property — Hunting, Fishing, Trapping or Trespassing for Any Purpose Is Strictly Forbidden." A man (Wilson) answered the front door; Carloss came out the back and joined the officers in the side yard; neither pointed out the signs or asked the officers to leave. Carloss ultimately consented to the officers entering, and the district court — finding his consent voluntary — denied his motion to suppress the evidence supporting the charges against him. He appealed.

## Issue
Whether "No Trespassing" signs posted around a home and on its front door revoke the implied license that allows an officer, like any private citizen, to approach the front door and knock to seek a consensual conversation with the occupants.

## Rule
"Ordinarily a police officer, like any citizen, has an implied license to approach a home, knock on the front door, and ask to speak with the occupants." The court held that, "under the circumstances presented here, those 'No Trespassing' signs would not have conveyed to an objective officer that he could not approach the house and knock on the front door seeking to have a consensual conversation with the occupants." — *United States v. Carloss*, 818 F.3d 988 (10th Cir. 2016) (slip op., at 1-2). ^pin-op1

Whether signage revokes the license turns on objective perception, not the resident's subjective intent: "the relevant inquiry here . . . has to be measured, not by what the resident subjectively intended, but instead by what an objective officer would have perceived." — *Id.* (slip op., at 10). ^pin-op10

And a sign alone is not enough: "just the presence of a 'No Trespassing' sign is not alone sufficient to convey to an objective officer, or member of the public, that he cannot go to the front door and knock. Such signs, by themselves, do not have the talismanic quality Carloss attributes to them." — *Id.* (slip op., at 11). ^pin-op11

The court found "[no] post-*Jardines* authority holding that a resident can revoke the implied license to approach his home and knock on the front door simply by posting a 'No Trespassing' sign." — *Id.* (slip op., at 11). ^pin-op11a

## Application
On these facts the signs did not revoke the implied license. Most of the "No Trespassing" signs were in the unenclosed front and side yards and along the driveway — areas Carloss did not establish were [[Curtilage|curtilage]] — and the front-door sign was framed around hunting, fishing, and trapping, recreational activities not ordinarily conducted at a home, so it did not read as barring a visitor who wished to speak with the occupants. An objective officer therefore would not have understood the signs to forbid approaching and knocking. Because the officers stayed within the implied license, and Carloss then voluntarily consented to entry, the search did not violate the Fourth Amendment.

## Conclusion
The "No Trespassing" signs did not revoke the implied [[Knock and Talk|knock-and-talk]] license, the officers' approach was lawful, and Carloss's consent to entry was valid; the Tenth Circuit affirmed the denial of suppression.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- *Carloss* illustrates the **divide** over whether signage revokes the implied license: then-Judge **Gorsuch dissented**, arguing that the posted "No Trespassing" signs (and the officers' purpose) withdrew the implicit license so that the entry was a search of a constitutionally protected space. The majority's objective-officer rule aligns with the Fourth and Eleventh Circuits' post-*[[Florida v. Jardines|Jardines]]* [[Knock and Talk|knock-and-talk]] decisions (see [[United States v. Walker]]) and applies the implied-license framework of [[Florida v. Jardines]]; contrast the time-plus-purpose limit in [[United States v. Lundin]] (9th Cir.).

## Appears on
- [[Knock and Talk]] — *Illustrates a circuit split*

## Sources
- *United States v. Carloss*, 818 F.3d 988 (10th Cir. 2016) — https://www.courtlistener.com/opinion/3184928/united-states-v-carloss/ — pinpoints given as slip-opinion pages (slip op., at 1-2, 10-11); CourtListener carries the slip opinion (cluster 3184928 → opinion 3184893). The pinpoints above are to the majority opinion; Gorsuch, J., dissented separately.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1fe754fb6af23287", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "818 F.3d 988 (2016)", "court": "U.S. Court of Appeals, 10th Circuit", "neutral_cite": "2016 WL 929663; 2016 U.S. App. LEXIS 4547", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Carloss", "year": "2016"}}
{"assertion_id": "93412be6289dfe22", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "On these facts, 'No Trespassing' signs posted around a home and on its front door did not revoke the implied license that lets an officer, like any citizen, approach the front door and knock to seek a consensual conversation; whether signage revokes the license is judged by what an objective officer would perceive, and a 'No Trespassing' sign by itself is not enough.", "title": "United States v. Carloss"}}
{"assertion_id": "a76155947e6378c3", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Illustrates a circuit split", "title": "United States v. Carloss"}}
{"assertion_id": "27a72ce1f6902a71", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2016-03-11", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Carloss", "field_i_validity": "good_law", "scope_note": "Good law. Then-Judge Gorsuch dissented, illustrating the divide over whether 'No Trespassing' signage revokes the implied knock-and-talk license.", "title": "United States v. Carloss", "varies_by_point": "false"}}
{"assertion_id": "a212f8c7e2532f98", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Carloss"}}
```

### lake record — United States v. Carloss

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Carloss",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Carloss",
    "case_name_short": "Carloss",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Ralph Gene CARLOSS, Defendant-Appellant",
    "input_case_name": "United States v. Carloss",
    "court": "U.S. Court of Appeals, 10th Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "2016-03-11",
    "year": 2016,
    "docket": "13-7082",
    "cluster_id": 3184928,
    "lead_opinion_id": 9822082,
    "sibling_ids": [
      3184893,
      9822082,
      9822083,
      9822084
    ],
    "absolute_url": "/opinion/3184928/united-states-v-carloss/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "818 F.3d 988",
      "volume": "818",
      "reporter": "F.3d",
      "page": "988",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2016 WL 929663",
        "volume": "2016",
        "reporter": "WL",
        "page": "929663",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 4547",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "4547",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "818 F.3d 988",
        "volume": "818",
        "reporter": "F.3d",
        "page": "988",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 929663",
        "volume": "2016",
        "reporter": "WL",
        "page": "929663",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 4547",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "4547",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "818 F.3d 988",
    "official_selection": {
      "court_class": "coa",
      "selected": "818 F.3d 988",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op1",
      "page": null,
      "quote": "signs posted around a home and on its front door revoke the implied license that allows an officer, like any private citizen, to approach the front door and knock to seek a consensual conversation with the occupants. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op10",
      "page": null,
      "quote": "the relevant inquiry here . . . has to be measured, not by what the resident subjectively intended, but instead by what an objective officer would have perceived.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op11",
      "page": null,
      "quote": "just the presence of a 'No Trespassing' sign is not alone sufficient to convey to an objective officer, or member of the public, that he cannot go to the front door and knock. Such signs, by themselves, do not have the talismanic quality Carloss attributes to them.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op11a",
      "page": null,
      "quote": "[no] post-*Jardines* authority holding that a resident can revoke the implied license to approach his home and knock on the front door simply by posting a 'No Trespassing' sign.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2016-03-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Carloss",
    "varies_by_point": false,
    "scope_note": "Good law. Then-Judge Gorsuch dissented, illustrating the divide over whether 'No Trespassing' signage revokes the implied knock-and-talk license.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "French v. Merrill",
          "cluster_id": 5273192,
          "cite": [
            "15 F.4th 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Smith",
          "cluster_id": 4600520,
          "cite": [
            "919 F.3d 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guillen",
          "cluster_id": 4877545,
          "cite": [
            "995 F.3d 1095"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
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
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronell Moses, Jr.",
          "cluster_id": 10623354,
          "cite": [
            "142 F.4th 126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Tilden Fellmy",
          "cluster_id": 10778901,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Albertson",
          "cluster_id": 10733103,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
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
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hannah Marie Kilby",
          "cluster_id": 5290146,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Nicholas Dean Wright",
          "cluster_id": 4894883,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hannah Marie Kilby",
          "cluster_id": 4893115,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Nicholas Dean Wright",
          "cluster_id": 4893114,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Brian De Arrie McGee",
          "cluster_id": 4883113,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Carloss:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(3184893 OR 9822082 OR 9822083 OR 9822084) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
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
        "query": "cites:(3184893 OR 9822082 OR 9822083 OR 9822084)",
        "reviewed": 14,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 13,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(3184893 OR 9822082 OR 9822083 OR 9822084)",
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
    "complete_query": "cites:(3184893 OR 9822082 OR 9822083 OR 9822084)",
    "indexed_citing_opinions": 14,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 3184893,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9822082,
        "count": 14,
        "count_source": "search"
      },
      {
        "opinion_id": 9822083,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9822084,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 53,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-carloss.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 14,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 3184893,
        "cited_id": 103832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 104917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 145669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 145814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 145922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 163041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 163607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 169130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 170672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 216522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 220092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 222695,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 785402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 795153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 801018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 1378909,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 1390153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 2568893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3184893,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T22:59:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:59:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:59:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:02:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:59:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Carloss

```
<opinion type="majority">
<author id="b1034-5">EBEL, Circuit Judge.</author>
<p id="b1034-6">In this direct criminal appeal, Defendant-Appellant Ralph Carloss contends that two police officers violated the Fourth Amendment by knocking on his front door, seeking to speak with him. Ordinarily a police officer, like any citizen, has an implied license to approach a home, knock on the front door, and ask to speak with the occupants. Carloss, however, claims that “No Trespassing” signs posted around the house and on the front door of his home revoked that implied license. We conclude, to the contrary, that under the circumstances presented here, those “No Trespassing” signs would hot have conveyed to an objective officer that he could not approach the house and knock on the front door seeking to have a consensual conversation with the occupants. Nor did the officers exceed the implied license to knock on the front door by knocking too long. We also uphold the district court’s factual finding that Carloss voluntarily consénted to the officers entering the house. Therefore, having jurisdiction under <span class="citation no-link">28 U.S.C. § 1291</span>, we AFFIRM the district court’s decision to deny Carloss’s motion to suppress evidence that the officers discovered as a result of their consensual interaction with Carloss, after he responded to their knocking.</p>
<p id="b1034-7">BACKGROUND</p>
<p id="b1034-8">Ashley Stephens, an agent with the federal Bureau of Alcohol, Tobacco and Firearms, received several tips that Carloss, a previously convicted felon, was unlawfully in possession of a firearm, possibly a machine gun, and was selling methamphetamine. In order to investigate these tips, Agent Stephens, along with Tahlequah, Oklahoma police investigator Elden Graves, went one afternoon to the home where Carloss was staying to talk with him. The home was a single-family dwelling located in a “pretty old area” in the “middle” of Tahlequah. (R. v.2 at 71-72.) There was no evidence of any fence or other enclosure around the house or yard, but there were several “No Trespassing” signs placed in the yard and on the front door. Specifically there was a “No Trespassing” sign on an approximately three-foot-high wooden post located beside the driveway, on the side farthest from the house, and another sign tacked to a tree in the side yard, both stating “Private Property No <em>Trespassing.” </em>(Aplt. Add. Def. Ex. 2-5, 7.) There was a sign, on a wooden pole in the front yard along the side of the driveway closest to the house, and a sign on the front door- of the house, both stating “Posted Private Property Hunting, Fishing, Trapping or Trespassing for Any Purpose Is Strictly Forbidden Violators Will Be Prosecuted.” <em>(Id </em>Ex. 1, 6.) These signs were professionally printed, with yellow or orange lettering against a black background. Although the officers testified that they did not recall seeing any of these signs, on the day they went to talk to Carloss, the district court found that the signs were there on that day, and that is not contested on appeal.</p>
<p id="b1034-10">When the two officers went to the house to speak with Carloss, they drove into the driveway, parked, walked to the front door, and knocked “for several minutes.” (R. v.2 at 74.) In response to their knocks, the officers could hear movement, inside the house, but no one answered the <em>front </em>door. Instead, “a short time later,” Heather Wilson exited the back door of the house and met the officers in the side <page-number citation-index="1" label="991">*991</page-number>yard. <em>(Id. </em>at 17.) The officers explained why they were there and asked who else was in the home. Wilson responded that Carloss, Earnest Dry, and Katy Homber-ger were inside.</p>
<p id="b1035-5">At about that time, Carloss exited the back door of the house and joined the officers and Wilson in the side yard. At no time did either Wilson or 'Carloss point out the “No Trespassing” signs to the officers or ask the officers to leave. The officers told Carloss that they suspected he had a machine gun. Carloss responded that he could not be around “ammunition” because of his prior criminal conviction. <em>(Id. </em>at 18.) The officers then asked who lived in the house; Carloss responded that he had a room there, but Earnest Dry owned the house. (Earnest Dry’s mother, Diana Fishinghawk, was the actual owner.) When the officers asked Carloss if they could search the home, Carloss told them he would have to get “the man of the house,” referring to Dry. <em>(Id.) </em>As Carloss started to go inside, apparently to get Dry, the officers asked if they could go in with Carloss; he said, “sure.”<footnotemark>1</footnotemark> <em>(Id. </em>at 19.)</p>
<p id="b1035-6">Carloss and the officers entered the back door, went through a storage or “mud” room into a room that Carloss identified as' his. <em>(Id. </em>at 34.) In Carloss’s room, the officers saw drug paraphernalia and a white powder residue that appeared to be methamphetamine.</p>
<p id="b1035-7">The officers waited with Carloss in his room; Dry and Homberger soon entered. The officers identified themselves, explained to Dry why they were there and asked if they could search the house. Dry asked if they had a warrant; they did not. After calling his attorney, Dry declined to let the officers search the house and instead asked them to leave. They did so but, based on the drug paraphernalia the officers saw in Carloss’s room, they obtained a warrant to return and search, the house. During the search, pursuant to that warrant, officers found “multiple methamphetamine labs” and lab components, a loaded shotgun, two blasting caps, ammunition, and other drug paraphernalia. (R. v.3 (sealed) Doc. 80 ¶¶ 15-19.)</p>
<p id="b1035-11">Based on this evidence, the United States prosecuted both Carloss and Dry for drug and weapons offenses. After unsuccessfully moving to suppress the evidence found in the house, Carloss pled guilty to conspiring to possess pseu-doephedrine; the district court sentenced him to forty-nine months in prison and three years’ supervised release. - His conditional guilty plea permitted this appeal to challenge the denial of his suppression motion.</p>
<p id="b1035-12">. STANDARD OF REVIEW</p>
<p id="b1035-13">In reviewing, the district court’s decision to deny Carloss’s suppression motion, “we view the evidence , in the light most favorable to the government, accept the district court’s findings of fact unless they are clearly erroneous, and review de novo the ultimate question of [the] reasonableness [of the officers’ actions] under the Fourth Amendment.” <em>United States v. Pettit, 785. </em>F.3d 1374, 1378-79 (10th Cir.2015), ce<em>rt. denied, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./136/282/">136 S.Ct. 282</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/193/205/">193 L.Ed.2d 205</a></span> (2015).</p>
<p id="b1035-16">DISCUSSION</p>
<p id="b1035-17">I. The officers did not violate the Fourth Amendment by going to the front door and knocking, seeking to speak with Carloss</p>
<p id="b1035-18">The Fourth ’ Amendment provides that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches <page-number citation-index="1" label="992">*992</page-number>and seizures, shall not be violated.” U.S. Const., amend. IV. “[H]ouses,” for Fourth Amendment purposes, include a home’s curtilage, and a home’s “front porch is the classic exemplar” of curtilage. <em>Florida v. Jardines, </em>— U.S. -, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1415" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. 1409, 1415</a></span>, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">185 L.Ed.2d 495</a></span> (2013). Carloss contends that the search of his home pursuant to the warrant was illegal because the officers got the^warrant based on information that they obtained in violation of the Fourth Amendment when they trespassed onto the curtilage of his home — the front porch — to knock on the front door, seeking to speak with him.<footnotemark>2</footnotemark></p>
<p id="b1036-6">A. The Tenth Circuit has upheld an officer’s knocking on. the front door seeking to speak with a home’s occupants</p>
<p id="b1036-7">This court has held, prior to <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span>, </em>that police officers do not violate the Fourth Amendment by going to the front door of a home and knocking, seeking to speak with the occupants. Specifically addressing an investigative knock-and-talk— during which police officers knock on the door'of a home seeking to speak with the occupants, <em>see United States v. Carter, </em><span class="citation" data-id="785402"><a href="/opinion/785402/united-states-v-bryan-keith-carter/#1238" aria-description="Citation for case: United States v. Bryan Keith Carter">360 F.3d 1235, 1238</a></span> (10th Cir.2004) — this court has held that, “[a]s commonly understood, a ‘knock and talk’- is a consensual encounter and therefore does not contravene the Fourth Amendment, even absent reasonable suspicion.” <em>United States v. Cruz-Mendez, </em><span class="citation" data-id="8410300"><a href="/opinion/8439529/united-states-v-cruz-mendez/#1264" aria-description="Citation for case: United States v. Cruz-Mendez">467 F.3d 1260, 1264</a></span> (10th Cir.2006); <em>see also, e.g., United States v. Harrison, </em><span class="citation" data-id="216522"><a href="/opinion/216522/united-states-v-harrison/" aria-description="Citation for case: United States v. Harrison">639 F.3d 1273</a></span>, 1276 n. 1 (10th Cir.2011); <em>United States v. Parker, </em><span class="citation" data-id="173207"><a href="/opinion/173207/united-states-v-parker/" aria-description="Citation for case: United States v. Parker">594 F.3d 1243</a></span>, 1244 n. 1 (10th Cir.2010); <em>cf. Florida v. Royer, </em>460, U.S. 491, 497, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">75 L.Ed.2d 229</a></span> (1983) (plurality) (“[L]aw enforcement officers do not violate the Fourth Amendment by merely approaching an individual on the street or in another public place, by asking him if he is willing to answer some questions, by putting questions to him if the person is willing to listen, or by offering in evidence in a criminal prosecution his voluntary answers to such questions.”). <em>See generally Kentucky v. King, </em><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">563 U.S. 452</a></span>, <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/#1862" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849, 1862</a></span>, <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span> (2011) (“[Wjhen law enforcement officers who are not armed with a warrant knock on a door, they do no more than any citizen might do.”).</p>
<p id="b1036-10">The home’s occupant remains free to terminate the conversation or even to avoid it altogether by not opening the door. <em>See King, </em><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/#1862" aria-description="Citation for case: Kentucky v. King">131 S.Ct. at 1862</a></span> (“[W]hether the person who knocks on the door and requests the- opportunity to speak is a police officer or a private citizen, the occupant has no obligation to open the door or to speak.”).</p>
<p id="b1036-11">B. <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>did not change our prior law upholding knock-and-talks</p>
<p id="b1036-12">The Supreme Court recently reaffirmed the validity of police knock-and-talk encounters in <em>Jardines, </em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. 1409</a></span>. <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>expressly recognizes that a police officer, like any member of the public, has an implied license to enter a home’s curti-lage to knock on the front door, seeking to speak with the home’s occupants. <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1416" aria-description="Citation for case: Florida v. Jardines"><em>See id. </em>at 1416</a></span>.</p>
<p id="b1036-13">1. <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>did not involve a knock-and-talk</p>
<p id="b1036-14">In <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span>, </em>officers ■ approached the front door of a home, not seeking a consen<page-number citation-index="1" label="993">*993</page-number>sual knock-and-talk, but instead specifically to conduct a search from the porch. The officers took a drug-sniffing dog onto Jardines’s front porch in order to gather information about what was occurring inside the home. <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1413" aria-description="Citation for case: Florida v. Jardines"><em>Id. </em>at 1413, 1416-18</a></span>; <em>cf. Kyllo v. United </em>States, <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#29" aria-description="Citation for case: Kyllo v. United States">533 U.S. 27, 29</a></span>, 35 n. 2, 40, <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">121 S.Ct. 2038</a></span>, <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">150 L.Ed.2d 94</a></span> (2001) (holding that an officer’s use of a thermal-imaging device from a public street to detect relative amounts of heat inside the home was a search). The <em>Jar-dines </em>Court .held that the license to approach a home and knock on the front door does not extend to permitting an officer to perform a search of. the interior of the house from the porch with the enhanced sensory ability of a trained dog. <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1416" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1416</a></span> (stating that, for a home’s occupant “[t]o find a visitor knocking on., the dooi; is routine (even if sometimes unwelcome); to spot that same visitor exploring the front path with a metal detector, or marching his bloodhound into the garden before saying hello and asking permission, would inspire most of us to — well, call the police”); <em>see also <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">id.</a></span> </em>at 1416-17 &amp; 1416 n. 4. In reaching that conclusion, however, <em>Jar-dines </em>reiterated that a knock-and-talk i1&gt; self is not a search for Fourth Amendment purposes: “[I]t is not a Fourth Amendment search to approach the home in order to speak with the occupant, <em>because all are invited to do that. </em>The mere purpose of discovering information in the course of engaging in that permitted conduct does not cause it to violate the Fourth Amend-ttient.” <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Id.</a></span> </em>at 1416 n. 4 (citation, internal quotation marks omitted). The <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>dissenters agreed with this part of the analysis.. <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1423" aria-description="Citation for case: Florida v. Jardines"><em>Id. </em>at 1423</a></span> (Alito, J., dissenting) (“[P]olice officers do not engage in a search when they approach the front door of a residence and seek to engage in what is termed, a ‘knock and talk,’ <em>i.e., </em>knocking on the door and seeking to speak to an occupant for the purpose of gathering evidence.”) (internal quotation marks omitted).. Thus, <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>left our preexisting knock-and-talk precedent undisturbed.</p>
<p id="b1037-7">2. In this case, the officers did not conduct a search when they went onto the front porch to knock on Car-loss’s front door</p>
<p id="b1037-8">This case is distinguishable from <em>Jar-dines </em>because there is nothing in this record to suggest that the officers conducted, or intended to conduct, a search from the front porch when they went onto the front porch to knock on Carloss’s front door. <em>See </em>Jardines, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1414" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1414-16</a></span>; <em>see also United States v. Walker, </em><span class="citation" data-id="2844024"><a href="/opinion/2844024/united-states-v-wayne-walker/#1363" aria-description="Citation for case: United States v. Wayne Walker">799 F.3d 1361, 1363-64</a></span> (11th Cir.2015). The officers did not.attempt to gather data about what, was occurring ins,ide the house from the. front porch, nor did they take with them anything that would enhance their ability to .do that, like the, drug-sniffing dog in <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>or the thermal imaging device at issue in <em><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span>. </em>Here, the officers simply went to the front door and knocked, seeking to speak consensually with Car-loss. Nor did the officers discover any incriminating evidence while they were on the front porch knocking.<footnotemark>3</footnotemark>.</p>
<p id="b1038-3"><page-number citation-index="1" label="994">*994</page-number>C. <em>Post-Jardines </em>cases make clear that <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>. did not restrict knock-and-talks</p>
<p id="b1038-4">Since <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span>, </em>the Tenth Circuit'has continued to uphold the constitutionality of knock-and-talks, based on the implied’license recognized in <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>that allows police officers, like members of the public, to approach the front door of a home and knock. <em>See United States v. Shuck, </em><span class="citation" data-id="857898"><a href="/opinion/857898/united-states-v-shuck/#567" aria-description="Citation for case: United States v. Shuck">713 F.3d 563, 567</a></span> (10th Cir.2013) (“A ‘knock- and-talk’ is a consensual encounter” that “does not contravene the Fourth Amendment.”) (internal quotation marks omitted); <em>see also McDowell, </em><span class="citation" data-id="857898"><a href="/opinion/857898/united-states-v-shuck/#574" aria-description="Citation for case: United States v. Shuck">713 F.3d at 574</a></span>.<footnotemark>4</footnotemark></p>
<p id="b1038-5">D. There was an implied license here for members of the public to go onto the curtilage of Carloss’s home in order to knock on the front door</p>
<p id="b1038-6">1. <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>recognizes such an implied license</p>
<p id="b1038-7"><em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>recognizes an implied license that “typically permits [a] visitor to approach [a] home by the front path, knock promptly, wait briefly to be received, and then (absent invitation to linger longer), leave.” <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1416" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1416</a></span>. On this basis, “a police officer not armed with a warrant may approach a home and knock, precisely because that is ‘no more than any private citizen might do.’ ” <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Id.</a></span> </em>(quoting <em>King, </em><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/#1862" aria-description="Citation for case: Kentucky v. King">131 S.Ct. at 1862</a></span>).</p>
<p id="b1038-12">Carloss contends that neither he nor Dry <em>gave </em>officers a license to approach the house and knock. But, because such “[a] license may be implied from the habits of the country,” <em>id.- </em>at 1415 (internal quotation marks omitted), a resident need not affirmatively grant the license. <em>See generally </em>James W. Ely, Jr. and Jon W. Bruce, <em>The Law of Easements and Licenses in Land, </em>§ 11.2 (updated Sept. 2015) (“Licenses may ... be implied from the conduct of a landowner or from local custom.” (footnote omitted)).</p>
<p id="b1038-13">2. The implied license at Carloss’s home had not been revoked</p>
<p id="b1038-14">Carloss contends that the “No Trespassing” signs placed on and about the house where he lived revoked the implied license that the public has to approach the house and knock on the front door. Whether that is so depends on the context in which a member of the public, or an officer seeking to conduct a knock-ahd-talk, encountered the signs and the message that those signs would have conveyed to an objective officer, or member of the public, under the circumstances.<footnotemark>5</footnotemark> <em>See State v. Christensen, </em>No. W2014-00931-CCA-R3-CD, <span class="citation no-link">2015 WL 2330185</span>, at *8 (Tenn.Crim.App. May 14, 2015) (unpub<page-number citation-index="1" label="995">*995</page-number>lished) (holding that “the. emerging rule appears to be that the implied invitation of the front door can be revoked but that the revocation must be obvious to the casual visitor who wishes only to contact the residents of a property”), <em>appeal granted, </em>(Tenn. Sept. 22, 2015); <em>cf. State v. Hiebert, </em><span class="citation" data-id="3149298"><a href="/opinion/3149298/state-v-dennis-earl-hiebert/" aria-description="Citation for case: State v. Dennis Earl Hiebert">156 Idaho, 637</a></span>, <span class="citation" data-id="3149298"><a href="/opinion/3149298/state-v-dennis-earl-hiebert/#1090" aria-description="Citation for case: State v. Dennis Earl Hiebert">329 P.3d 1085, 1090</a></span> (App. 2014) (holding, in case involving police entering a combined business (junk yard) and residence, that, although the defendant’s father, who resided there, “testified that the back of the junk yard is closed to the public and that people are supposed to stop at the shop, the [relevant] question is what an ordinary visitor to the business property, not knowing the subjective intent of the owner, would have objectively perceived as reasonable conduct”). We conclude1 that, under the circumstances presented here, the “No Trespassing” signs placed about Carloss’s home would not have conveyed to an objective officer that he could not go to the front door and knock, seeking to speak consensually with Carloss.</p>
<p id="b1039-5">As an initial matter, just the presence of a “No Trespassing” sign is not alone sufficient to convey to an objective officer, or member of the public, that he cannot go to the front door and knock. Such signs, by themselves, do not have the talismanic quality Carloss attributes to them. <em>See Davis v. City of Milwaukee, </em>No. 13-CV-982-JPS, <span class="citation no-link">2015 WL 5010459</span>, at *13 (E.D.Wis. Aug. 21, 2015) (indicating, post-<em>Jardines, </em>that “signs stating , ‘Private Property’ or ‘No Trespassing’ do not, by themselves, create an impenetrable privacy zone”); <em>United States v. Jones, </em>No. 4:13CR00011-003, <span class="citation no-link">2013 WL 4678229</span>, at *5 (W.D.Va. Aug. 30, 2013) (stating, <em>gosl-Jar-dines, </em>that “No Trespassing” “signs do not, in and of themselves, create a right to privacy or automatically place an area under the Fourth Amendment’s protections”); <em>see also City of Beatrice v. Meints, </em><span class="citation no-link">289 Neb. 558</span>, <span class="citation no-link">856 N.W.2d 410</span>, 421 (2014) (holding, <em>post-Jardines, </em>that a resident “could not reasonably expect that tacking a ‘no trespassing’ sign to a tree would prevent others from viewing or walking on his land”), <em>cert. denied, </em>— <em>U.S. -, </em><span class="citation multiple-matches"><a href="/c/S.Ct./135/2388/">135 S.Ct. 2388</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/192/166/">192 L.Ed.2d 166</a></span> (2015); <em>Christensen, </em><span class="citation no-link">2015 WL 2330185</span>, at *6-*8 (Tenn.Crim.App.). (rejecting, post-<span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines"><em>Jardines, </em></a></span>a bright-line rule that a “No Trespassing” sign revokes the implied license to approach a front door to conduct knock-and-talk). Carloss has not cited, nor can we find, any <em>post-Jardines </em>authority holding that a resident can revoke the implied license to approach his home and knock on the front door simply by posting a “No Trespassing” sign.</p>
<p id="b1039-9">Here, with the exception of the sign on the front door, the “No Trespassing” signs were placed in the unenclosed front and side yards and along the driveway of the house where Carloss lived. Because Carloss does not expressly claim that these areas were part of the home’s curtilage — and it was Carloss’s burden to establish what was included in the home’s curtilage, <em>see United States v. Cavely, </em><span class="citation" data-id="163041"><a href="/opinion/163041/united-states-v-cavely/#994" aria-description="Citation for case: United States v. Cavely">318 F.3d 987, 994</a></span> (10th Cir.2003)—these areas were instead “open fields.” <em>See Reeves v. Churchich, </em><span class="citation" data-id="169130"><a href="/opinion/169130/reeves-v-churchich/#1255" aria-description="Citation for case: Reeves v. Churchich">484 F.3d 1244, 1255</a></span> (10th Cir.2007) (holding, where there was no evidence that a front yard was enclosed, used for intimate activities of the home, or in any way protected from observation, that front yard was not part of the home’s curtilage but was instead an open field); <em>see also United States v. Cousins, </em><span class="citation" data-id="795153"><a href="/opinion/795153/united-states-v-kurt-donald-cousins-and-bukola-tolase-cousins/#1122" aria-description="Citation for case: United States v. Kurt Donald Cousins, and Bukola...">455 F.3d 1116, 1122-24</a></span> (10th Cir.2006) (holding side yard was not curtilage).</p>
<p id="b1039-10">Those signs would not have conveyed to an objectivé officer, or member of the public, that he could not walk up to the porch and knock on the front door and attempt to contact the occupants. It is well-established that “No Trespassing” signs will not prevent an officer from entering privately owned “open fields.” <em>See </em><page-number citation-index="1" label="996">*996</page-number><em>Jardines, </em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1414" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1414</a></span>; <em>Oliver v. United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States">466 U.S. 170, 182-83</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">104 S.Ct. 1735</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">80 L.Ed.2d 214</a></span> (1984); <em>see also Rieck v. Jensen, </em><span class="citation" data-id="220092"><a href="/opinion/220092/rieck-v-jensen/#1189" aria-description="Citation for case: Rieck v. Jensen">651 F.3d 1188, 1189, 1191-94</a></span> (10th Cir.2011) (holding that a deputy sheriffs entry onto private property that was not curtilage, by opening a closed gate with a “No Trespassing” sign and despite homeowner telling deputy he had no right to enter, did'not violate the Fourth Amendment). That is true even though the officers’ entry into the yard might be considered a trespass at common law, <em>see Oliver, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#183" aria-description="Citation for case: Oliver v. United States">466 U.S. at 183-84</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">104 S.Ct. 1735</a></span> (“[I]n the case of open fields, the general rights of property protected by the common law of trespass have little or no relevance to the applicability of the Fourth Amendment.”); <em>Rieck, </em><span class="citation" data-id="220092"><a href="/opinion/220092/rieck-v-jensen/#1191" aria-description="Citation for case: Rieck v. Jensen">651 F.3d at 1191</a></span> (10th Cir.) (stating that “the Supreme Court has made it clear that the Fourth Amendment does not track property law,” citing <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span> </em>and <em>United States v. Dunn, </em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">480 U.S. 294</a></span>, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">107 S.Ct. 1134</a></span>, <span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/" aria-description="Citation for case: United States v. Dunn">94 L.Ed.2d 326</a></span> (1987)); or might have violated Oklahoma statutory law, <em>see United States v. Hatfield, </em><span class="citation" data-id="163607"><a href="/opinion/163607/united-states-v-hatfield/#1198" aria-description="Citation for case: United States v. Hatfield">333 F.3d 1189, 1198-99</a></span> (10th Cir.2003) (holding officers did not violate the Fourth Amendment when they made observations from a defendant’s open field, even though the officers, in entering the open field, violated Okla, Stat. tit. 21, § 1835).<footnotemark>6</footnotemark></p>
<p id="b1040-7">There was also a sign on the front door itself stating: “Posted 'Private Property Hunting, Fishing, Trapping or Trespassing for Any Purpose Is Strictly Forbidden Violators Will Be Prosecuted.” (Aplt. Add. Def. Ex. 1.) But that sign was ambiguous and did not clearly; revoke the implied license extended to members of the public, including police officers, to enter the home’s curtilage and knock on the front, door, seeking to speak consensually with the occupants. The sign on the front door of Carloss’s home referenced activities that ordinarily do not take place within a home or its curtilage — hunting, fishing, and trapping. Thus, on its face, this sign does not appear to be directed to people who desire .to approach and speak directly with the occupants of the home in the ordinary course of societally accepted discourse. When considered in light of the other, similar “No Trespassing” signs in Carloss’s yard, this front door sign could have simply been reiterating that such recreational activities would not be <page-number citation-index="1" label="997">*997</page-number>allowed on the property generally. <em>See Christensen, </em><span class="citation no-link">2015 WL 2330185</span>, at *8 (Tenn.Crim.App.) (stating that a “sign reading ‘no trespassingt,] hunting[,] oh fishing,’ posted in a field next to appellant’s driveway ... would not have prevented the casual visitor or the reasonably respectful citizen from approaching appellant’s residence”; citing cases indicating that “such a sign, especially on a rural property, is generally intended to prevent people from unauthorized use of the property, not to prevent á casual visitor from approaching the residence”).' The message here does not clearly and unambiguously tell the mail carrier, pizza deliverer, or police officer that they cannot knock on the front’ door seeking a consensual conversation with those who live there. <em>See Jones, </em><span class="citation no-link">2013 WL 4678229</span>, at *1-*2, *5-*6 (W.D.Va.) (holding, <em>post-Jardines, </em>that officers did not violate, the Fourth Amendment by entering rural property, driving past “No Trespassing” signs on either side of the driveway, passing another sign , on then- way to the house and another affixed to the house, and walking past a “No Trespassing” sign hanging to the right of the front door in order to conduct a knock-and-talk). We conclude that, under the' circumstances presented here, an objective officer would not have understood that the implied license he would ordinarily have to approach the porch and knock on the front door of a home had been revoked at this house. Therefore, the officers did not violate the Fourth Amendment when they went onto the porch and knocked on the front door of the house in which Carloss lived. <em>See United States v. Bearden, </em>780 F.3d-887, 890-91, 893-94 (8th Cir.2015) (holding that officers did not violate the Fourth Amendment by driving through an open gate with a “No Trespassing” sign on their way to entering a home’s curtilage in order, to conduct a knock-and-talk); <em>United States v. Lubrin, </em>No. CR-2014-0056, <span class="citation no-link">2015 WL 361796</span>, at *2, *5-*6 &amp; *5 n. 6, *6 n. 7 (D.Vi. Jan. 28, 2015) (holding that officers did not-violate the ■ Fourth Amendment by entering a home’s: curtilage through'a gate in a fence, to conduct knock-and-talk, despite a “No Trespassing” sign on the fence, but not near gate); <em>Hiebert, </em><span class="citation" data-id="3149298"><a href="/opinion/3149298/state-v-dennis-earl-hiebert/" aria-description="Citation for case: State v. Dennis Earl Hiebert">329 P.3d at 1089</a></span> n. 2, 1090 (Idaho Ct.App.) (holding that “No Trespassing” signs located in curtilage “cannot reasonably be interpreted to exclude normal, legitimate' inquiries or visits by ordinary individuals, including police officers, who restrict their movements' to the areas normally used by a reasonable visitor”); <em>Pache v. State, </em><span class="citation" data-id="3074937"><a href="/opinion/3074937/michael-wade-pache-v-state/#511" aria-description="Citation for case: Michael Wade Pache v. State">413 S.W.3d 509, 511-12</a></span> (Tex.App.2013) (holding the officers could enter curtilage and go to front door and knock, notwithstanding testimony'that there wds a “No.Trespassing” sign at the gate through which the officers entered front-yard); <em>see also Covey v. Assessor of Ohio Comity, </em><span class="citation" data-id="2773276"><a href="/opinion/2773276/christopher-covey-v-assessor-of-ohio-county/#190" aria-description="Citation for case: Christopher Covey v. Assessor of Ohio County">777 F.3d 186, 190, 192-94</a></span> (4th Cir.2015) (suggesting that police officers'conducting knock-and-talk at a “privately' set home in [a] rural village” did not violate the Fourth Amendment by driving past two “No Trespassing” signs posted along driveway); <em>Hollaran v. Duncan, </em><span class="citation" data-id="7230400"><a href="/opinion/7312496/holloran-v-duncan/#783" aria-description="Citation for case: Holloran v. Duncan">92 F.Supp.3d 774, 783-84, 787-88</a></span> (W.D.Tenn.2015) (holding that officers did not violate the Fourth Amendment by entering onto “farm property” by removing locked gate and driving past “No Trespassing” signs); <em>United States v. Denim, </em>No. 2:13-CR-63, <span class="citation no-link">2013 WL 4591469</span>, at *1-*6 (E.D.Tenn. Aug. 28, 2013) (holding, without discussing what areas of the home were curtilage, that placing six' “No Trespassing” signs along a driveway leading to a home did not revoke the implied license to approach home and knock, seeking to talk with occupants);</p>
<p id="b1041-6">E. The officers did not exceed the scope of the implied license by knocking too long</p>
<p id="b1041-7">.■ Carloss further argues that the officers exceeded the scope of their implied <page-number citation-index="1" label="998">*998</page-number>license because they knocked at his front door too long. We cannot agree. The implied license <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span> </em>recognized “typically permits the visitor to approach the home by the front path, knock promptly, wait briefly to be received, and then (absent invitation to linger longer) leave.” <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1415" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1415</a></span>. We decline to place a specific time limit on how long a person can knock before exceeding the scope of this implied license. Here, the officers testified that they knocked “for several” minutes or “a minute or two.” (R. v. 2 at 26, 74.) The officers were no doubt encouraged to remain a bit longer, ■ hoping someone would respond to their knock, because they heard movement inside the house and received no request from inside the house to depart. In fact, Heather Wilson emerged from the back door of the house only “a short while later,” or “a minute or so later,” and met the officers in the side yard. <em>(Id. </em>at 17, 63.) There is no suggestion that the officers knocked aggressively or demanded entry. Under these circumstances, we cannot say that the officers exceeded the implied license they had to approach the house and knock, seeking to speak with the occupants.</p>
<p id="b1042-4">II. The district court did not clearly err in finding that Carloss voluntarily consented to the officers accompanying him into the home</p>
<p id="b1042-5">Finally, the district court did not clearly err in finding that Carloss voluntarily consented to the officers following him into the house. <em>See United States v. Thompson, </em><span class="citation" data-id="170672"><a href="/opinion/170672/united-states-v-thompson/#1133" aria-description="Citation for case: United States v. Thompson">524 F.3d 1126, 1133</a></span> (10th Cir.2008) (holding “[v]oluntariness is a factual finding” reviewed for clear error); <em>see also Jones, </em>701 F.3d at 1318 (10th Cir.) (setting forth factors to consider in deciding whether consent was voluntary); <em>United States v. Benard, </em><span class="citation" data-id="9500555"><a href="/opinion/801018/united-states-v-benard/#1211" aria-description="Citation for case: United States v. Benard">680 F.3d 1206, 1211</a></span> (10th Cir.2012) (same).</p>
<p id="b1042-6">Carloss first argues that his consent was the product of a Fourth Amendment violation — the officers’ unlicensed knocking on the front door. But we have concluded there was no such Fourth Amendment violation.</p>
<p id="b1042-8">Carloss further asserts that his consent that the officers enter the house was involuntary because there was testimony suggesting that the officers conveyed to him, before he consented, that they would not let him enter the home without them; and that, because Carloss told the officers he could not consent to the search of the house, the officers should ■ not have believed that Carloss could consent to their accompanying them into the home. However, the district court found that Carloss voluntarily consented to the officers accompanying him into the house, and that finding was not clearly erroneous.</p>
<p id="b1042-9">There were only two officers, dressed in plainclothes: They never ’drew their weapons. There was no evidence that the officers physically touched or mistreated Car-loss, nor that they got Carloss to let them enter the house using threats or promises. The officers spoke in a casual, rather than an aggressive, manner, never demanding entry into the house or otherwise claiming any lawful authority to be admitted. They did not retain any of Carloss’s personal effects and there is no suggestion that Carloss had any physical or mental deficits that the officers exploited. Carloss’s conversation with the officers occurred in the side yard, in public view during daylight hours. <em>See Benard, </em><span class="citation" data-id="9500555"><a href="/opinion/801018/united-states-v-benard/#1211" aria-description="Citation for case: United States v. Benard">680 F.3d at 1211</a></span> (considering, in determining whether consent was voluntary, fact that interaction between officer and individual occurred in public place during daylight). Furthermore, although the officers did not inform Carloss that he could refuse their request to accompany him into the house (which is not a prerequisite for voluntary consent, <em>see Schneckloth v. Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#231" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 231-33</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> <page-number citation-index="1" label="999">*999</page-number>(1973)), Carloss was aware he could refuse the officers’ request because he had just declined to give them broader general consent to search the house, indicating instead that the officers would have to ask Dry for permission to do that. For these reasons, the district court’s finding-that Carloss voluntarily consented to the officers accompanying him into the house was not clearly erroneous.</p>
<p id="b1043-5">CONCLUSION</p>
<p id="b1043-6">For the foregoing reasons, we AFFIRM the district court’s decision to deny Car-loss’s suppression motion.</p>
<footnote label="1">
<p id="b1035-8">. At the suppression hearing, Carloss gave a different version of these events, but the district court found that the officers’ testimony was more credible, than Carloss’s.- On appeal, Carloss does not challenge that credibility determination.</p>
</footnote>
<footnote label="2">
<p id="b1036-8">. The Fourth Amendment protects against the government’s ' 1) unprivileged trespass on property expressly protected by the Fourth Amendment — "persons, houses, papers, and effects” — for the purpose of conducting a search or seizure; and 2) infringement of an individual’s reasonable expectation of privacy. <em>See Jardines, </em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1414" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1414, 1417</a></span>; <em>see also United States v. Jones, </em>— U.S. -, <span class="citation" data-id="7268856"><a href="/opinion/7350871/united-states-v-jones/#949" aria-description="Citation for case: United States v. Jones">132 S.Ct. 945, 949-53</a></span>, <span class="citation" data-id="7268856"><a href="/opinion/7350871/united-states-v-jones/" aria-description="Citation for case: United States v. Jones">181 L.Ed.2d 911</a></span> (2012). Carloss expressly bases his argument solely on the trespass theory of Fourth Amendment protections and we, therefore, confine our analysis to that theory.</p>
</footnote>
<footnote label="3">
<p id="b1037-5">. Had the officers discovered incriminating evidence while lawfully on the front porch knocking, however, that would not violate the Fourth Amendment. <em>See United States v. McDowell, </em><span class="citation" data-id="857912"><a href="/opinion/857912/united-states-v-mcdowell-theodore/#574" aria-description="Citation for case: United States v. McDowell (Theodore)">713 F.3d 571, 574</a></span> (10th Cir.2013). In <em><span class="citation" data-id="857912"><a href="/opinion/857912/united-states-v-mcdowell-theodore/" aria-description="Citation for case: United States v. McDowell (Theodore)">McDowell</a></span>, </em>a <em>post-Jardines </em>case, an officer, at 11:00 p.m., walked on the driveway and front walk of a home, on his way to the front door to conduct a knock-arid-talk. <span class="citation" data-id="857912"><a href="/opinion/857912/united-states-v-mcdowell-theodore/#572" aria-description="Citation for case: United States v. McDowell (Theodore)"><em>Id. </em>at 572</a></span>. On his way to the front door, the officer smelled a strong odor of marijuana coming from the garage. <em><span class="citation" data-id="857912"><a href="/opinion/857912/united-states-v-mcdowell-theodore/" aria-description="Citation for case: United States v. McDowell (Theodore)">Id.</a></span> </em>This court held that, "whether or not the driveway and front sidewalk were curtilage, [the officer] did not violate the Fourth Amendment by traversing them on his way to the front door. Thus, the smell of marijuana that reached him while he <page-number citation-index="1" label="994">*994</page-number>was in the driveway was not fruit of an unlawful search,”</p>
</footnote>
<footnote label="4">
<p id="b1038-9">. The Fourth and Eleventh Circuits have also upheld knock-and-talks after <em>Jardines. See Walker, </em><span class="citation" data-id="2844024"><a href="/opinion/2844024/united-states-v-wayne-walker/#1363" aria-description="Citation for case: United States v. Wayne Walker">799 F.3d at 1363</a></span> (11th Cir.); <em>Covey v. Assessor of Ohio Cnty., 777 </em>F.3d 186, 192-93 (4th Cir.2015). There does not appear to be any circuit that has concluded, after <em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span>, </em>that a knock-and-talk is invalid.</p>
</footnote>
<footnote label="5">
<p id="b1038-10">. In this case, the property owner, Diana Fishinghawk, testified that her daughter put up the "No Trespassing” signs at the home in which Carloss lived seven years earlier, when the daughter lived in the house, because she was having trouble with “drunks” from a nearby bar wandering onto the property (R. v.2 at 103); Fishinghawk advised her daughter that the "No Trespassing” signs would assist the police in removing the drunks from the property. According to Fishinghawk, the "No Trespassing” signs were not intended to keep police officers from investigating crimes or providing assistance. Nevertheless, the relevant inquiry here, in determining whether the signs revoked the officers' implied license to approach the house and knock, has to be measured, not by what the resident subjectively intended, but instead by what an objective officer would have perceived.</p>
</footnote>
<footnote label="6">
<p id="b1040-5">. <em>See generally Virginia v. Moore, </em><span class="citation" data-id="9435233"><a href="/opinion/145814/virginia-v-moore/#166" aria-description="Citation for case: Virginia v. Moore">553 U.S. 164, 166, 176, 178</a></span>, <span class="citation" data-id="9435233"><a href="/opinion/145814/virginia-v-moore/" aria-description="Citation for case: Virginia v. Moore">128 S.Ct. 1598</a></span>, <span class="citation" data-id="9435233"><a href="/opinion/145814/virginia-v-moore/" aria-description="Citation for case: Virginia v. Moore">170 L.Ed.2d 559</a></span> (2008) (holding that an arrest was reasonable under the Fourth Amendment even though it violated state law, and stating that "linking Fourth Amendment protections to state law would cause them to vary from place to place and from time to time” (internal quotation marks omitted)); <em>California v. Greenwood, </em><span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/#43" aria-description="Citation for case: California v. Greenwood">486 U.S. 35, 43</a></span>, <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/" aria-description="Citation for case: California v. Greenwood">108 S.Ct. 1625</a></span>, <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/" aria-description="Citation for case: California v. Greenwood">100 L.Ed.2d 30</a></span> (1988) ("We have never intimated ... that whether or not a search is reasonable within the meaning of the Fourth Amendihent depends on the law of the particular State in which the search occurs. Wfe have -emphasized instead that the Fourth Amendment analysis must turn on factors such as our <em>societal </em>understanding that certain areas deserve the most scrupulous protection from government invasion,” (internal quotation-marks omitted)); <em>United States v. Jones, </em><span class="citation" data-id="813790"><a href="/opinion/813790/united-states-v-jones/#1309" aria-description="Citation for case: United States v. Jones">701 F.3d 1300, 1309-10</a></span> (10th Cir.2012) (stating that, under facts presented there, the question of whether Missouri' officers were acting without authority under Kansas state law was "irrelevant” to the question of whether they violated the Fourth Amendment, that "officers’ violation of state law is not, without more, necessarily a federal constitutional violation,” and that, “[w]hile compliance with state law may be relevant to our Fourth Amendment reasonableness analysis in some circumstances, we have never held it to be determinative of the constitutionality of police conduct” (internal quotation marks omitted)); <em>United States v. Madden, </em><span class="citation" data-id="802514"><a href="/opinion/802514/united-states-v-madden/#927" aria-description="Citation for case: United States v. Madden">682 F.3d 920, 927</a></span> (10th Cir.2012) ("Whether an arrest, search, or seizure may have violated state law is irrelevant as long as the standards developed under the Federal Constitution were not offended.” (internal quotation marks omitted)).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Carlton Williams.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Carlton Williams
type: case
citation: "898 F.3d 323 (2018)"
parallel_cite: ""
neutral_cite: ""
court: 3d Cir. 2018
court_level: coa
circuit: ca3
year: 2018
date_decided: 2018-08-01
docket: 16-3547
authority_weight: "Binding in-circuit — 3d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4522771/united-states-v-carlton-williams/"
  cluster_id: 4522771
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Carlton Williams
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Consent Searches]]"
    role: Key
related:
  - "[[Consent Searches]]"
  - "[[Schneckloth v. Bustamonte]]"
  - "[[Florida v. Jimeno]]"
tags:
  - case
  - fourth-amendment
  - search
  - consent
  - scope-of-consent
holding: "A suspect who has voluntarily consented to a search may withdraw that consent, but only by an unambiguous act or unequivocal statement that an objective viewer would understand as a desire to stop the search; ambiguous complaints or impatience do not withdraw consent, so evidence found before any clear withdrawal remains admissible."
---

# United States v. Carlton Williams

*898 F.3d 323 (3d Cir. 2018)* (No. 16-3547) · U.S. Court of Appeals for the Third Circuit · **Binding in-circuit — 3d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4522771 → opinion 4300024 (898 F.3d 323, decided 2018-08-01); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
A DEA task force learned that Carlton Williams was trafficking heroin from Detroit to Pittsburgh and, after tracking his car by GPS for about a month, arranged a traffic stop when the car returned from Detroit. Pennsylvania Trooper Volk stopped Williams for speeding, issued a citation, told him he was free to go, and then asked for consent to search; Williams signed a written consent-to-search form titled a Waiver of Rights and Consent to Search, and the parties agreed his consent was knowing, intelligent, and voluntary. The ensuing search lasted about seventy-one minutes. As it dragged on, Williams grew impatient and grumbled that the troopers were holding him up, and he specifically objected when officers examined his phones and began disassembling his speakers — objections the troopers honored. Drugs were ultimately found. Williams pleaded guilty, reserving his challenge to the denial of suppression.

## Issue
Whether the Fourth Amendment permits the subject of a consensual search to withdraw his consent, and if so, what a suspect must do to withdraw it — and whether Williams's impatient statements withdrew the consent he had voluntarily given.

## Rule
A search conducted with voluntary consent is a recognized exception to the warrant requirement, and the subject of the search "may delimit as he chooses the scope of the search to which he consents." Joining every sister circuit to consider the question, the Third Circuit held that a suspect may withdraw consent — but only unequivocally: "Once it has been established that a suspect has voluntarily consented to a search, it is his burden to demonstrate that he has withdrawn that consent by pointing to an act or statement that an objective viewer would understand as an expression of his desire to no longer be searched." — slip op. at 11. Ambiguous or equivocal acts and statements do not withdraw consent; the measure is objective reasonableness — what a typical reasonable person would have understood from the exchange.

## Application
Williams's consent was concededly voluntary, so it was his burden to show an unequivocal withdrawal. His impatient grumbling that the troopers had already searched his car several times and were holding him up was equivocal, made in a normal tone the trooper may not even have heard, and did not objectively signal a desire to end the search. Where Williams did clearly delimit his consent — objecting to the search of his phones and speakers — the troopers honored those limits and stopped. Measured objectively, nothing he said withdrew his general consent to search the car, so the drugs later discovered fell within a continuing, valid consent.

## Conclusion
The denial of suppression was **affirmed**. Roth, J., wrote for the court (Hardiman, Roth, Fisher, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Carlton Williams* is the Third Circuit's adoption of the withdrawal-of-consent rule: consent voluntarily given under *[[Schneckloth v. Bustamonte|Schneckloth]]* remains valid until the suspect withdraws it by an unambiguous act or unequivocal statement, judged by the *[[Florida v. Jimeno|Jimeno]]* standard of objective reasonableness — mere impatience or ambiguous protest is not enough.

## Appears on
- [[Consent Searches]] — *Key*

## Sources
- [*United States v. Carlton Williams*, 898 F.3d 323 (3d Cir. 2018)](https://www.courtlistener.com/opinion/4522771/united-states-v-carlton-williams/) — pinpoint: slip op. at 11 (withdrawal-of-consent standard); the CL opinion text carries the slip-opinion page numbers rather than 898 F.3d star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "70821aa48ad8c363", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "898 F.3d 323 (2018)", "court": "3d Cir. 2018", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Carlton Williams", "year": "2018"}}
{"assertion_id": "42fba29ececa92f9", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Key", "title": "United States v. Carlton Williams"}}
{"assertion_id": "4ad98d3173ab3921", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A suspect who has voluntarily consented to a search may withdraw that consent, but only by an unambiguous act or unequivocal statement that an objective viewer would understand as a desire to stop the search; ambiguous complaints or impatience do not withdraw consent, so evidence found before any clear withdrawal remains admissible.", "title": "United States v. Carlton Williams"}}
{"assertion_id": "83f02604b7f0584b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 3d Cir.", "title": "United States v. Carlton Williams"}}
{"assertion_id": "d405fc8cbca9f18c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Carlton Williams", "varies_by_point": "false"}}
```

### lake record — United States v. Carlton Williams

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Carlton Williams",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Carlton Williams",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America v. Carlton WILLIAMS, Appellant",
    "input_case_name": "United States v. Carlton Williams",
    "court": "3d Cir. 2018",
    "court_id": "ca3",
    "court_level": "coa",
    "circuit": "ca3",
    "state": null,
    "date_decided": "2018-08-01",
    "year": 2018,
    "docket": "16-3547",
    "cluster_id": 4522771,
    "lead_opinion_id": 9886943,
    "sibling_ids": [],
    "absolute_url": "/opinion/4522771/united-states-v-carlton-williams/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "898 F.3d 323",
      "volume": "898",
      "reporter": "F.3d",
      "page": "323",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "898 F.3d 323",
        "volume": "898",
        "reporter": "F.3d",
        "page": "323",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "898 F.3d 323",
    "official_selection": {
      "court_class": "state",
      "selected": "898 F.3d 323",
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
    "date_created": "2026-07-06T05:50:59Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:51:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:51:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:51:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:51:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-carlton-williams--4522771",
      "to_record_id": "United States v. Carlton Williams",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Carlton Williams

```
<opinion type="majority">
<author id="p-8">ROTH, Circuit Judge</author>
<p id="p-9">During an investigation, federal law enforcement officials learned that Carlton Williams was involved in the distribution of heroin. The investigation involved surveillance of Williams's activity, which eventually led to a stop of his car. During the traffic stop, law enforcement officials conducted a search of Williams's car and its <a class="page-label" data-citation-index="1" data-label="327" href="#p327" id="p327">*327</a>contents. As they expected, the officials discovered drugs during the search. Williams subsequently pleaded guilty to possession of heroin with intent to distribute in violation of federal drug laws. Williams now appeals the denial of his suppression motion and application of the United States Sentencing Guidelines' career offender enhancement. Finding no merit in either claim, we will affirm Williams's conviction and sentence.</p>
<p id="p-10"><strong>I.</strong></p>
<p id="p-11"><strong>A. Factual Background</strong></p>
<p id="p-12">The underlying facts are uncontested. During an investigation that began as early as November 2012, a Drug Enforcement Administration task force officer learned that Williams bought heroin in Detroit, Michigan, which he packaged and sold in Pittsburgh, Pennsylvania. The officer subsequently placed a GPS tracker on Williams's car and monitored his movements for approximately one month. On January 11, 2013, data from the GPS tracker indicated that Williams's car was driven to Detroit. Suspecting that Williams drove his car to Detroit to retrieve heroin, the task force officer organized a plan to have Williams's car stopped upon its return to Pennsylvania. Pennsylvania State Police trooper Michael Volk effectuated the traffic stop.</p>
<p id="p-13">Later that same evening, Trooper Volk observed Williams's car speeding and stopped it. The trooper issued a citation for the traffic violation and told Williams that he was free to go. Before Williams left, however, Trooper Volk asked Williams for consent to search his car. Williams agreed and signed a consent to search form labeled "Waiver of Rights and Consent to Search." The parties do not dispute that Williams knowingly, intelligently, and voluntarily consented to the search of his car, its contents, and his person.</p>
<p id="p-14">Trooper Volk, with the help of other troopers, commenced a search of Williams's car that lasted for approximately seventy-one minutes. The troopers searched every part of the car, including its passenger compartment, trunk, and undercarriage. Unable to locate any narcotics, Trooper Volk requested the assistance of a narcotics-detection dog. Shortly thereafter, Trooper Volk updated another trooper on the progress of the search and indicated that "[the search] was going to take awhile [because] he hadn't found [the heroin], but the K-9 was on its way coming from a distance."<footnotemark>1</footnotemark></p>
<p id="p-15">Williams eventually became less patient and told Trooper Volk "you searched my car three times, now you hold me up and I have to go."<footnotemark>2</footnotemark> According to Williams, he made this statement in only "a regular tone of voice that he expected Trooper Volk to hear but [the trooper] was at a distance and there was a lot of noise from the turnpike traffic and the wind."<footnotemark>3</footnotemark> Other than Williams's own testimony, there was no evidence that Trooper Volk heard his alleged protest. The District Court, as a result, found Williams's testimony "only credible to a degree."<footnotemark>4</footnotemark></p>
<p id="p-16">The troopers continued their search despite Williams's irritation. As the search continued, Williams requested five items from his car, including his two cellular phones. One of the troopers retrieved Williams's cellular phones and attempted to search them before handing them over <a class="page-label" data-citation-index="1" data-label="328" href="#p328" id="p328">*328</a>to Williams. The trooper was able to read the text messages contained on only one of the devices because the other device was password-protected. The trooper who read Williams's text messages told Trooper Volk that the messages suggested that Williams had "something."<footnotemark>5</footnotemark> When Williams was confronted about the text messages, he warned the officers that they could not search his phone without a warrant.</p>
<p id="p-17">The search of the car continued. After fifty-one minutes, the troopers had not discovered any drugs. They began to disassemble Williams's sound system speakers. Williams objected that the troopers were not permitted to search his speakers without a warrant. Trooper Volk told Williams to "relax," to which Williams replied, "I've been out here half an hour, man."<footnotemark>6</footnotemark> Upon Williams's protest, Trooper Volk reassembled the car's speakers but otherwise continued searching the vehicle. Soon after, and seventy-one minutes into the search, Trooper Volk discovered thirty-nine grams of heroin in a sleeve covering the car's parking brake lever. Williams was immediately arrested.</p>
<p id="p-18"><strong>B. Procedural History</strong></p>
<p id="p-19">Williams was charged with possession of heroin with intent to distribute, in violation of <extracted-citation index="0" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">21 U.S.C. §§ 841</span></extracted-citation>(a)(1) and 841(b)(1)(C). He filed a number of pretrial motions, including a motion to suppress the evidence seized from his car. Following a two-day hearing and the submission of post-hearing briefing, the District Court denied Williams's suppression motion, because it concluded that Williams had voluntarily consented to the search and had not unequivocally withdrawn his consent during the search.</p>
<p id="p-20">Prior to Williams's sentencing, the United States Probation Office prepared a Presentence Investigation Report (PSR), which the District Court adopted without change. The sentencing range calculation included U.S.S.G. § 4B1.1 's career offender enhancement because the District Court concluded that Williams had two prior convictions for controlled substance offenses: a 2007 conviction for possession with intent to distribute heroin and a 1998 conviction under <extracted-citation index="1" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%201962"><span class="citation no-link">18 U.S.C. § 1962</span></extracted-citation>(c) and (d) of the Racketeer Influenced and Corrupt Organizations Act (RICO). Williams admitted to various predicate acts forming the basis for his § 1962 RICO conviction, all of which were for possession with intent to distribute either crack cocaine or heroin in violation of <extracted-citation index="2" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">21 U.S.C. §§ 841</span></extracted-citation>(a)(1), 841(b)(1)(C), 841(b)(1)(B)(iii), and 846.<footnotemark>7</footnotemark> As a result of the career offender enhancement, Williams faced a Guidelines sentencing range of 210-262 months. On May 11, 2016, Williams entered a conditional guilty plea, preserving his right to appeal the denial of his suppression motion and the application of the Guidelines' career offender designation. Williams was sentenced to, <em>inter alia</em> , a term of 160 months' imprisonment. This appeal followed.</p>
<p id="p-21">Williams appeals both the denial of his suppression motion and the District Court's application of the Guidelines' career offender designation. The District Court had jurisdiction pursuant to <extracted-citation index="3" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%203231"><span class="citation no-link">18 U.S.C. § 3231</span></extracted-citation>. We exercise appellate jurisdiction under <extracted-citation index="4" url="https://cite.case.law/citations/?q=28%20U.S.C.%20%C2%A7%201291"><span class="citation no-link">28 U.S.C. § 1291</span></extracted-citation> and <extracted-citation index="5" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%203742"><span class="citation no-link">18 U.S.C. § 3742</span></extracted-citation>(a).<footnotemark>8</footnotemark></p>
<p id="p-22"><strong>II.</strong></p>
<p id="p-23">"We review the District Court's denial of a motion to suppress for clear <a class="page-label" data-citation-index="1" data-label="329" href="#p329" id="p329">*329</a>error as to the underlying factual findings, and we exercise plenary review of its application of the law to those facts."<footnotemark>9</footnotemark> " 'A finding is clearly erroneous when although there is evidence to support it, the reviewing court on the entire evidence is left with the definite and firm conviction that a mistake has been committed.' "<footnotemark>10</footnotemark> Therefore, " '[i]f the [D]istrict [C]ourt's account of the evidence is plausible in light of the record viewed in its entirety,' we will not reverse it even if, as the trier of fact, we would have weighed the evidence differently."<footnotemark>11</footnotemark></p>
<p id="p-24"><strong>A. The District Court Properly Denied Williams's Motion to Suppress</strong></p>
<p id="p-25">With respect to his suppression motion, Williams claims that the District Court erred in denying his suppression motion because he properly withdrew his consent to the search or was improperly prevented from doing so.</p>
<p id="p-26">It is well settled that the Fourth Amendment protects suspects from unreasonable searches.<footnotemark>12</footnotemark> "[A] search conducted without a warrant issued upon probable cause is [presumptively] unreasonable ... subject only to a few specifically established and well-delineated exceptions."<footnotemark>13</footnotemark> A search conducted with consent is one such "established exception."<footnotemark>14</footnotemark> The appellant concedes that the search here began as a consensual one. He contends, however, that the search ceased to be so when he withdrew his consent or was prevented from doing so. Before reaching the issue of whether Williams withdrew his consent in this case, we must first determine whether the Fourth Amendment allows the subject of a consensual search to terminate the search by withdrawing his consent. Neither this Court nor the Supreme Court has expressly established that the subject of a consensual search may withdraw consent that he has voluntarily given. The Supreme Court, however, has recognized that a person may "delimit as he chooses the scope of the search to which he consents."<footnotemark>15</footnotemark> In so holding, the Court has instructed that the standard for measuring the limitations placed on a consensual search "is that of objective reasonableness."<footnotemark>16</footnotemark> Thus, in determining the legal bounds of a consensual search, we must determine "what would the typical reasonable person have understood by the exchange between the officer and the suspect."<footnotemark>17</footnotemark> Relying on <em>Florida v. Jimeno</em> 's recognition that a consensual search may be restricted by individuals, our sister circuits that have considered whether individuals may withdraw consent to search have unanimously answered in the affirmative.<footnotemark>18</footnotemark> Today, we join them.</p>
<p id="p-27"><a class="page-label" data-citation-index="1" data-label="330" href="#p330" id="p330">*330</a>Although the Supreme Court has not itself expressly held that the subject of a consensual search may terminate the search by withdrawing his consent, considerable support for such a proposition is easily found in its Fourth Amendment jurisprudence. The Court recognized in <em>Walter v. United States</em> ,<footnotemark>19</footnotemark> and later in <em>Jimeno</em> ,<footnotemark>20</footnotemark> that a consensual search satisfies the mandates of the Constitution only if conducted within the boundaries of the consent given. This recognition establishes that it is the subject of a consensual search who decides the terms of the search. Although <em>Walter</em> and <em>Jimeno</em> expressly consider only a party's right to limit the particular things officials may search, nothing in those opinions suggests that consent, which waives Fourth Amendment rights, cannot otherwise be narrowed, qualified, or withdrawn. That a party may terminate a search by withdrawing his consent is a corollary of the recognition that the subject of a consensual search determines the parameters of that search.</p>
<p id="p-28">Moreover, recognition of a party's right to take away the consent that he or she has conferred advances society's interest in promoting consensual searches. The Supreme Court has acknowledged that consensual searches are important because they promote the effective enforcement of criminal laws.<footnotemark>21</footnotemark> This is particularly true where there is lack of probable cause to arrest or search because, in such situations, "a search authorized by a valid consent may be the only means of obtaining important and reliable evidence."<footnotemark>22</footnotemark> Moreover, a rule restricting the ability to withdraw consent would likely discourage people from consenting to searches when they otherwise might have done so. In the present case, for example, Williams voluntarily authorized the troopers to conduct a search. He then admonished the troopers that the search of his speakers and electronic devices was not within the bounds of his authorization. As a result, the troopers reassembled the speakers and ceased examining the phone that was not password-protected. However, "where a suspect does not withdraw his valid consent to a search for illegal substances before they are discovered, the consent remains valid and the substances are admissible as evidence."<footnotemark>23</footnotemark></p>
<p id="p-29">Turning to the merits of this case, we must decide whether Williams actually withdrew his consent. As the parties note, <a class="page-label" data-citation-index="1" data-label="331" href="#p331" id="p331">*331</a>"the ultimate touchstone of the Fourth Amendment is 'reasonableness.' "<footnotemark>24</footnotemark> Thus, in determining whether suspects have withdrawn their consent to a search, courts have been guided by how a reasonable person would have understood the exchange between law enforcement officers and suspects.<footnotemark>25</footnotemark> Courts agree that a reasonable person would not understand certain equivocal acts or statements to convey a suspect's desire to withdraw consent that he has voluntarily conferred.<footnotemark>26</footnotemark> Ambiguous acts and statements do not ordinarily lend themselves to a conclusive determination of whether consent has been withdrawn. Once it has been established that a suspect has voluntarily consented to a search, it is his burden to demonstrate that he has withdrawn that consent by pointing to an act or statement that an objective viewer would understand as an expression of his desire to no longer be searched.</p>
<p id="p-30">With these principles in mind, we hold that the circumstances here do not demonstrate that Williams withdrew his consent to the troopers' search of his car. Williams knew how to express the absence of consent to search. As the record demonstrates, Williams told the troopers that they did not have consent to search his speakers or his cellular phones. The search of those areas then stopped.</p>
<p id="p-31">Williams also argues that he conveyed withdrawal of his consent to search the car when he complained that he had been standing "out [there] half an hour" and after he told officer Volk "you searched my car three times [and] y'all got me on the side of this road in the middle of the winter holding me up and I got to go."<footnotemark>27</footnotemark> The District Court held that Williams's comments only "constituted manifestations of irritation" and not statements indicating that he was withdrawing the consent he had conferred.<footnotemark>28</footnotemark> We agree. Although defendants need not use a special set of words to withdraw consent, they must do more than express unhappiness about the search to which they consented.</p>
<p id="p-32">Other courts have reached the same conclusion when presented with similar facts. For example, the Eighth Circuit Court of Appeals in <em>United States v. Gray</em> held that a suspect had not withdrawn consent simply by objecting that the search was "ridiculous" and that he was "ready to go."<footnotemark>29</footnotemark> The court held that such statements amounted only to "expressions of impatience."<footnotemark>30</footnotemark> The court warned that "protests about the length of time the search was taking without any specific request to leave did not under the circumstances"</p>
<p id="p-33"><a class="page-label" data-citation-index="1" data-label="332" href="#p332" id="p332">*332</a>amount to a withdrawal of consent.<footnotemark>31</footnotemark> Similarly, Williams's statements here were expressions of frustration. Williams falls short of meeting his burden of proof to establish that his consent was withdrawn.</p>
<p id="p-34">Williams alternatively contends that, even if he did not withdraw his consent to the search, the evidence should be suppressed because the "coercive" nature of the search prevented him from revoking consent.</p>
<p id="p-35">The Fourth Amendment requires that consent not be coerced.<footnotemark>32</footnotemark> The question of whether Williams's consent was at any point the product of coercion is "a question of fact determined from the totality of the circumstances."<footnotemark>33</footnotemark> In assessing the voluntariness of a suspect's consent, we consider "the age, education, and intelligence of the subject; whether the subject was advised of his or her constitutional rights; the length of the encounter; the repetition or duration of the questioning; and the use of physical punishment."<footnotemark>34</footnotemark> Our analysis "must accord the district court's conclusion that [Williams]'s consent was [voluntary] great deference, unless our examination of the record shows that the district court committed clear error."<footnotemark>35</footnotemark> Thus, the District Court's finding that Williams's consent was voluntary will not be overturned unless it is "(1) completely devoid of minimum evidentiary support displaying some hue of credibility, or (2) bears no rational relationship to the supportive evidentiary data."<footnotemark>36</footnotemark></p>
<p id="p-36">Our assessment of the totality of the circumstances precludes us from concluding that the District Court committed clear error. As the District Court noted, Williams's interaction with the troopers was not hostile. The troopers neither made threats nor showed force. No restraints were employed at the time of the search. The District Court's finding that Williams exhibited his ability to intelligently delimit the scope of the search is supported by the record. Accordingly, the District Court did not err in finding that, throughout the entire encounter, Williams's grant of consent was not the product of coercion.</p>
<p id="p-37"><strong>B. The District Court Properly Applied the Guidelines' Career Offender Enhancement</strong></p>
<p id="p-38">Williams next appeals his career offender designation, arguing that his 1998 RICO conviction-predicated on his distribution of heroin and crack cocaine-was not a requisite "controlled substance offense" under the Sentencing Guidelines. We disagree.</p>
<p id="p-39">Under the Sentencing Guidelines, a defendant must be sentenced as a "career offender" if: (1) he was at least eighteen years old when he committed the instant offense of conviction; (2) the instant offense is a felony crime of violence or controlled substance offense; and (3) he has at least two prior felony convictions for a crime of violence or controlled substance offense.<footnotemark>37</footnotemark></p>
<p id="p-40"><a class="page-label" data-citation-index="1" data-label="333" href="#p333" id="p333">*333</a>In this case, there is no dispute that the instant offense-possession with intent to distribute heroin in violation of §§ 841(a)(1) and 841(b)(1)(C) -is a controlled substance offense. Nor is there any doubt that Williams was at least eighteen at the time. The parties agree that Williams's 2007 conviction for possession with intent to distribute heroin supplies one of the two required prior felony convictions. The 1998 RICO conviction, we now hold, supplies the second.</p>
<p id="p-41">Ordinarily, to determine whether a prior conviction qualifies as a crime of violence or controlled substance offense, we apply a categorical approach.<footnotemark>38</footnotemark> We consider only the elements of the crime of conviction and assess whether they fall within the bounds of a crime of violence or controlled substance offense, as defined under the Guidelines.<footnotemark>39</footnotemark> To avoid the "practical difficulties and potential unfairness" inherent in "determining the precise facts underlying a defendant's [prior] conviction," which may have occurred years or decades ago, we do not excavate or dissect the underlying factual record.<footnotemark>40</footnotemark></p>
<p id="p-42">There is an exception, however. When a crime is defined with alternative elements, we may review a limited set of documents-including the indictment and plea colloquy, among others-but only to determine which version of the statute formed the basis of the prior conviction.<footnotemark>41</footnotemark> Such a statute is termed "divisible" and this approach-a more record-invasive variant of the categorical approach-is called the "modified categorical approach."</p>
<p id="p-43">RICO, in particular Section 1962(c), is one such divisible statute. That statutory subsection, the basis for Williams's 1998 RICO conviction, proscribes "conduct[ing] ... [an] enterprise's affairs through a pattern of racketeering activity or collection of unlawful debt." It proscribes two alternative forms of conduct: <em>either</em> racketeering activity <em>or</em> the collection of unlawful debt. That fork in the statute has even more branches. "Racketeering activity," a statutory phrase without independent meaning, has "constituent parts" or alternative "elements" that need to be proven beyond a reasonable doubt to sustain a conviction.<footnotemark>42</footnotemark> Under RICO, those elements are known as "predicate acts" and include certain violations of federal law, including "fraud connected with a case under title 11," or "fraud in the sale of securities," or "the felonious manufacture, importation, receiving, concealment, buying, selling, or otherwise dealing in a controlled substance or listed chemical."<footnotemark>43</footnotemark> Without consulting the record, we would not know which of these multiple alternatives yielded Williams's prior RICO conviction.</p>
<p id="p-44">Fortunately, because Section 1962(c) is divisible, we may consult select portions of the record under the modified categorical approach to make that determination.</p>
<p id="p-45"><a class="page-label" data-citation-index="1" data-label="334" href="#p334" id="p334">*334</a>The superseding indictment and Williams's 1998 plea colloquy are illuminating. They reveal that Williams pleaded guilty to a RICO violation under Section 1962(c) and five underlying RICO predicate acts.<footnotemark>44</footnotemark> All five of those predicate acts of racketeering were violations of <extracted-citation index="6" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">21 U.S.C. § 841</span></extracted-citation>(a)(1) -or conspiracy to commit such a violation under <extracted-citation index="7" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%20846"><span class="citation no-link">21 U.S.C. § 846</span></extracted-citation>.<footnotemark>45</footnotemark> Specifically, he admitted to "manufactur[ing], distribut[ing], or dispens[ing], or possess[ing] with intent to manufacture, distribute, or dispense" heroin or crack cocaine.<footnotemark>46</footnotemark> Without probing the record further or examining Williams's prior conduct, we now know that Williams's prior RICO conviction necessarily implicated only a limited portion of <extracted-citation index="8" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%201961"><span class="citation no-link">18 U.S.C. § 1961</span></extracted-citation>(1)(D), namely, only the "felonious manufacture," or "recei[pt]," or "buying, selling, or otherwise dealing in a controlled substance."<footnotemark>47</footnotemark> This limited and non-fact-intensive review of the record unmasks the specific version of the RICO statute under which Williams was convicted: "conduct[ing] ... [an] enterprise's affairs" through "a pattern of racketeering activity" by "felonious[ly] manufactur[ing]," or "receiving," or "buying, selling, or otherwise dealing in a controlled substance or listed chemical."<footnotemark>48</footnotemark></p>
<p id="p-46">The final step in this analysis is to assess whether the offense of conviction-as decoded by this selective review of the record-sweeps any more broadly than the relevant generic offense,<footnotemark>49</footnotemark> in this case a "controlled substance offense" as defined in the Guidelines. Section 4B1.2 of the Guidelines defines a "controlled substance offense" as "the manufacture, import, export, distribution, or dispensing of a controlled substance (or a counterfeit substance) or the possession of a controlled substance (or a counterfeit substance) with intent to manufacture, import, export, distribute, or dispense."<footnotemark>50</footnotemark> The specific version of RICO implicated by Williams's prior conviction encompasses only the "felonious manufacture," or "recei[pt]," or "buying, selling, or otherwise dealing in a controlled substance": It is categorically a subset of the Guidelines' definition of a "controlled substance offense." For that reason, Williams's prior RICO conviction was a "controlled substance offense" under the Guidelines.</p>
<p id="p-47">Because both his 2007 heroin distribution conviction and his 1998 RICO conviction were prior felony convictions for controlled substance offenses, the District Court correctly applied the career offender enhancement to Williams.</p>
<p id="p-48"><strong>III.</strong></p>
<p id="p-49">For the foregoing reasons, we will affirm the judgment of the District Court.</p>
<p id="p-50">HARDIMAN, Circuit Judge, concurring in part and concurring in the judgment.</p>
<p id="p-51">I agree with my colleagues that the District Court did not err when it denied Williams's motion to suppress evidence. I also agree that Williams is-as the District Court found-a career offender under § 4B1.1 of the United States Sentencing Guidelines (2015) (USSG). As to that second issue, I concur in the judgment only because I cannot subscribe to the Majority's modified categorical approach, which I <a class="page-label" data-citation-index="1" data-label="335" href="#p335" id="p335">*335</a>believe misapplies the Supreme Court's decisions in <em>Taylor v. United States</em> , <extracted-citation case-ids="634101" index="9" url="https://cite.case.law/us/495/575/"><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">495 U.S. 575</a></span></extracted-citation>, <extracted-citation case-ids="634101" index="10" url="https://cite.case.law/us/495/575/"><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">110 S.Ct. 2143</a></span></extracted-citation>, <extracted-citation case-ids="634101" index="11" url="https://cite.case.law/us/495/575/"><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">109 L.Ed.2d 607</a></span></extracted-citation> (1990), and <em>Mathis v. United States</em> , --- U.S. ----, <extracted-citation case-ids="12598042" index="12" url="https://cite.case.law/s-ct/136/2243/"><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">136 S.Ct. 2243</a></span></extracted-citation>, <extracted-citation case-ids="12598042" index="13" url="https://cite.case.law/s-ct/136/2243/"><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">195 L.Ed.2d 604</a></span></extracted-citation> (2016). But because a proper application of the modified categorical approach would yield absurd results in cases involving RICO predicate offenses, I am convinced that the Supreme Court would not apply it here. Accordingly, I agree with my colleagues that Williams is a career offender.</p>
<p id="p-52">At the outset, it's important to note that the Supreme Court has not yet applied <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> (or <em><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span></em> ) in a case involving a RICO predicate offense. And although some of our sister courts have adjudicated cases involving the interplay between RICO and the § 4B1.1 career offender guideline, they have not settled on a consistent mode of analysis. For example, the Ninth Circuit placed "the focus of the inquiry ... on the <em>conduct</em> for which [the defendant] was convicted" without mentioning the categorical approach or citing <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> . <em>United States v. Scott</em> , <extracted-citation case-ids="3383320" index="14" url="https://cite.case.law/f3d/642/791/#p801"><span class="citation" data-id="218363"><a href="/opinion/218363/united-states-v-scott/" aria-description="Citation for case: United States v. Scott">642 F.3d 791</a></span></extracted-citation>, 801 (9th Cir. 2011) (per curiam). The First Circuit has taken a different tack, explaining that in determining whether a RICO conviction counts toward the career offender enhancement, courts should "in fidelity to <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> principles ... merely assess the nature and object of the racketeering activity as described in the indictment and fleshed out in the jury instructions." <em>United States v. Winter</em> , <extracted-citation case-ids="10501902" index="15" url="https://cite.case.law/f3d/22/15/#p19"><span class="citation" data-id="195327"><a href="/opinion/195327/united-states-v-winter/" aria-description="Citation for case: United States v. Winter">22 F.3d 15</a></span></extracted-citation>, 19-21 (1st Cir. 1994). Like the First Circuit, a panel of the Eleventh Circuit professed fealty to <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> , but it looked to "the facts to which [the defendant] stipulated" in comparing the conduct underlying the defendant's prior racketeering conviction with the definition of a "controlled substance offense" under USSG § 4B1.2(b). <em>United States v. Rosquete</em> , <extracted-citation case-ids="3893600" index="16" url="https://cite.case.law/f-appx/208/737/#p739"><span class="citation" data-id="44812"><a href="/opinion/44812/united-states-v-leonardo-rosquete/" aria-description="Citation for case: United States v. Leonardo Rosquete">208 F. App'x 737</a></span></extracted-citation>, 739-41 (11th Cir. 2006) (per curiam).</p>
<p id="p-53">Here, my colleagues have chosen to follow the path marked by the Supreme Court in <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> and <em><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span></em> . And if the <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> <em>/</em> <em><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span></em> framework applies to this case, the Majority is quite right that the relevant statute ( <extracted-citation index="17" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%201962"><span class="citation no-link">18 U.S.C. § 1962</span></extracted-citation>(c) ) is divisible, which requires application of the modified categorical approach.</p>
<p id="p-54">But the modified categorical approach yields a result contrary to the one the Majority reaches. Section 1961(1)(D), which specifies the type of racketeering activity Williams was engaged in, is <em>not</em> "categorically a subset of the Guidelines' definition of a 'controlled substance offense.' " Maj. Op. 334. Under Guidelines § 4B1.2(b), a "controlled substance offense" encompasses "the manufacture, import, export, distribution, or dispensing of a controlled substance (or a counterfeit substance) or the possession of a controlled substance (or a counterfeit substance) with intent to manufacture, import, export, distribute, or dispense." That definition differs from Williams's RICO conviction, which involved "the felonious manufacture, importation, receiving, concealment, buying, selling, or otherwise dealing in a controlled substance or listed chemical (as defined in section 102 of the Controlled Substances Act), punishable under any law of the United States." <extracted-citation index="18" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%201961"><span class="citation no-link">18 U.S.C. § 1961</span></extracted-citation>(1)(D). A comparison of the two provisions makes clear that Williams's RICO offense encompasses conduct that § 4B1.2(b) does not cover, such as "receiving, concealment, buying ... or otherwise dealing in a controlled substance." <em>See <extracted-citation index="19" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%201961">id.</extracted-citation></em> Because it "sweeps more broadly than the generic crime," Williams's RICO conviction is not a qualifying offense under the modified categorical approach. <em>See</em> <em>Descamps v. United States</em> , <extracted-citation case-ids="12698469" index="20" url="https://cite.case.law/us/570/254/#p261"><span class="citation" data-id="9515838"><a href="/opinion/903971/descamps-v-united-states/" aria-description="Citation for case: Descamps v. United States">570 U.S. 254</a></span></extracted-citation>, 261, <extracted-citation case-ids="12698469" index="21" url="https://cite.case.law/us/570/254/#p261"><span class="citation" data-id="9515838"><a href="/opinion/903971/descamps-v-united-states/" aria-description="Citation for case: Descamps v. United States">133 S.Ct. 2276</a></span></extracted-citation>, <extracted-citation case-ids="12698469" index="22" url="https://cite.case.law/us/570/254/#p261"><span class="citation" data-id="9515838"><a href="/opinion/903971/descamps-v-united-states/" aria-description="Citation for case: Descamps v. United States">186 L.Ed.2d 438</a></span></extracted-citation> (2013).</p>
<p id="p-55">Would the Supreme Court really conclude that Williams's RICO conviction did <a class="page-label" data-citation-index="1" data-label="336" href="#p336" id="p336">*336</a>not constitute a "controlled substance offense"? I think not. The predicate acts underlying Williams's conviction included the distribution of and possession with intent to distribute: (1) in excess of a kilogram of heroin; (2) in excess of 50 grams of cocaine base; (3) in excess of 5 grams of cocaine base; (4) less than 5 grams of cocaine base; and (5) less than 100 grams of heroin. The enumeration of these predicate acts plainly establishes that Williams's RICO conviction is for a controlled substance offense.</p>
<p id="p-56">To hold that it is not defies common sense not only in this case, but in <em>any</em> RICO case predicated on federal drug crimes. This is so because in every such case the "element" that <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> and <em><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span></em> require us to compare to USSG § 4B1.2(b) will be the same: <extracted-citation index="23" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%201961"><span class="citation no-link">18 U.S.C. § 1961</span></extracted-citation>(1)(D). <em>See</em> Maj. Op. 333-34. An application of the modified categorical approach will thus generate the same nonsensical answer-that a RICO conviction based on controlled substance offenses is not a "controlled substance offense"-every time.</p>
<p id="p-57">I cannot accept that Congress, the United States Sentencing Commission, or the Supreme Court would endorse such an absurd result. Accordingly, I would hold that the approach the Court has articulated in cases like <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> , <em><span class="citation" data-id="9515838"><a href="/opinion/903971/descamps-v-united-states/" aria-description="Citation for case: Descamps v. United States">Descamps</a></span></em> , and <em><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span></em> does not apply here. The categorical approach was developed to ensure that federal defendants who have committed essentially the same crimes in the past don't receive disparate sentences merely because they committed those prior offenses in different states. <em>See</em> <em>Taylor</em> , <extracted-citation case-ids="634101" index="24" url="https://cite.case.law/us/495/575/"><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">495 U.S. at 591</a></span>-92</extracted-citation>, <extracted-citation case-ids="634101" index="25" url="https://cite.case.law/us/495/575/"><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">110 S.Ct. 2143</a></span></extracted-citation>. That policy justification has no relevance here, where the nature of the prior federal conviction is clear on the face of the docket.</p>
<p id="p-58">Were the Supreme Court confronted with the question before us, I think it would not attempt to pound the square peg of RICO into the round hole of the categorical/modified categorical approach. It would be especially surprising for the Court to do so not only because the predicate offense at issue here is markedly different from the state burglary crimes at issue in <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> and <em><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span></em> , but also because several Justices have expressed dissatisfaction with the categorical approach generally.<footnotemark>1</footnotemark> For these reasons, I would not apply the categorical approach of <em><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></em> and <em><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span></em> to the RICO offense at issue here. Instead, I would hold that Williams's RICO conviction was, on its face, a controlled substance offense that counted toward the USSG § 4B1.1 career offender enhancement.</p>
<p id="p-59">* * *</p>
<p id="p-60">For the reasons stated, I join the Court's opinion regarding the denial of Williams's motion to suppress, and I concur in the Court's judgment that Williams is a career offender.</p>
<footnote label="1">
<p id="p-88"><em>United States v. Williams</em> , <extracted-citation index="26" url="https://cite.case.law/citations/?q=2015%20WL%205602617"><span class="citation no-link">2015 WL 5602617</span></extracted-citation>, at *6 n.5 (W.D. Pa. 2015).</p>
</footnote>
<footnote label="2">
<p id="p-89"><span class="citation no-link"><em>Id.</em> at *6</span>.</p>
</footnote>
<footnote label="3">
<p id="p-90"><em><extracted-citation case-ids="9248250" index="27" url="https://cite.case.law/f3d/369/1024/#p1026"><span class="citation no-link">Id.</span></extracted-citation></em></p>
</footnote>
<footnote label="4">
<p id="p-91"><em><extracted-citation case-ids="9248250" index="28" url="https://cite.case.law/f3d/369/1024/#p1026"><span class="citation no-link">Id.</span></extracted-citation></em></p>
</footnote>
<footnote label="5">
<p id="p-92">App. 222.</p>
</footnote>
<footnote label="6">
<p id="p-93"><em><span class="citation no-link">Williams</span></em> , <extracted-citation index="29" url="https://cite.case.law/citations/?q=2015%20WL%205602617"><span class="citation no-link">2015 WL 5602617</span></extracted-citation>, at *6.</p>
</footnote>
<footnote label="7">
<p id="p-94">Supp. App. 19-25.</p>
</footnote>
<footnote label="8">
<p id="p-95"><em>United States v. Johnson</em> , <extracted-citation case-ids="5680687" index="30" url="https://cite.case.law/f3d/587/203/#p207"><span class="citation" data-id="1345057"><a href="/opinion/1345057/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">587 F.3d 203</a></span></extracted-citation>, 207 (3d Cir. 2009).</p>
</footnote>
<footnote label="9">
<p id="p-96"><em>United States v. Bansal</em> , <extracted-citation case-ids="5879577" index="31" url="https://cite.case.law/f3d/663/634/#p651"><span class="citation" data-id="618840"><a href="/opinion/618840/united-states-v-bansal/" aria-description="Citation for case: United States v. Bansal">663 F.3d 634</a></span></extracted-citation>, 651-52 (3d Cir. 2011) (citing <em>United States v. Perez</em> , <extracted-citation case-ids="9393346" index="32" url="https://cite.case.law/f3d/280/318/#p336"><span class="citation" data-id="776532"><a href="/opinion/776532/united-states-v-linette-perez-united-states-of-america-v-juancho/" aria-description="Citation for case: United States v. Linette Perez, United States of America...">280 F.3d 318</a></span></extracted-citation>, 336 (3d Cir. 2002) ).</p>
</footnote>
<footnote label="10">
<p id="p-97"><em>United States v. Price</em> , <extracted-citation case-ids="3359359" index="33" url="https://cite.case.law/f3d/558/270/#p276"><span class="citation" data-id="1354805"><a href="/opinion/1354805/united-states-v-price/" aria-description="Citation for case: United States v. Price">558 F.3d 270</a></span></extracted-citation>, 276-77 (3d Cir. 2009) (quoting <em>United States v. Pelullo</em> , <extracted-citation case-ids="11618440" index="34" url="https://cite.case.law/f3d/173/131/#p135"><span class="citation" data-id="763105"><a href="/opinion/763105/united-states-v-leonard-a-pelullo/" aria-description="Citation for case: United States v. Leonard A. Pelullo">173 F.3d 131</a></span></extracted-citation>, 135 (3d Cir. 1999) ).</p>
</footnote>
<footnote label="11">
<p id="p-98"><em>Price</em> , <extracted-citation case-ids="3359359" index="35" url="https://cite.case.law/f3d/558/270/#p276"><span class="citation" data-id="1354805"><a href="/opinion/1354805/united-states-v-price/" aria-description="Citation for case: United States v. Price">558 F.3d at 277</a></span></extracted-citation> (quoting <em>Anderson v. City of Bessemer City</em> , <extracted-citation case-ids="11299693" index="36" url="https://cite.case.law/us/470/564/#p573"><span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/" aria-description="Citation for case: Anderson v. City of Bessemer City">470 U.S. 564</a></span></extracted-citation>, 573-74, <extracted-citation case-ids="11299693" index="37" url="https://cite.case.law/us/470/564/#p573"><span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/" aria-description="Citation for case: Anderson v. City of Bessemer City">105 S.Ct. 1504</a></span></extracted-citation>, <extracted-citation case-ids="11299693" index="38" url="https://cite.case.law/us/470/564/#p573"><span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/" aria-description="Citation for case: Anderson v. City of Bessemer City">84 L.Ed.2d 518</a></span></extracted-citation> (1985) ).</p>
</footnote>
<footnote label="12">
<p id="p-99">U.S. Const. Amend. IV.</p>
</footnote>
<footnote label="13">
<p id="p-100"><em>Schneckloth v. Bustamonte</em> , <extracted-citation case-ids="6172008" index="39" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218</a></span></extracted-citation>, 219, <extracted-citation case-ids="6172008" index="40" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation>, <extracted-citation case-ids="6172008" index="41" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span></extracted-citation> (1973) (internal quotation marks omitted) (citing <em>Katz v. United States</em> , <extracted-citation case-ids="11339173" index="42" url="https://cite.case.law/us/389/347/#p357"><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U.S. 347</a></span></extracted-citation>, 357, <extracted-citation case-ids="11339173" index="43" url="https://cite.case.law/us/389/347/#p357"><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span></extracted-citation>, <extracted-citation case-ids="11339173" index="44" url="https://cite.case.law/us/389/347/#p357"><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span></extracted-citation> (1967) ).</p>
</footnote>
<footnote label="14">
<p id="p-101"><em>Id</em> . at 219, <extracted-citation case-ids="6172008" index="45" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation> (citations omitted).</p>
</footnote>
<footnote label="15">
<p id="p-102"><em>Florida v. Jimeno</em> , <extracted-citation case-ids="6221328" index="46" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">500 U.S. 248</a></span></extracted-citation>, 252, <extracted-citation case-ids="6221328" index="47" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span></extracted-citation>, <extracted-citation case-ids="6221328" index="48" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">114 L.Ed.2d 297</a></span></extracted-citation> (1991).</p>
</footnote>
<footnote label="16">
<p id="p-103"><em>Id</em> . at 251, <extracted-citation case-ids="6221328" index="49" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span></extracted-citation> (internal quotation marks omitted).</p>
</footnote>
<footnote label="17">
<p id="p-104">See <em>Jimeno</em> , <extracted-citation case-ids="6221328" index="50" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">500 U.S. at 251</a></span></extracted-citation>, <extracted-citation case-ids="6221328" index="51" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span></extracted-citation> (applying a reasonable person standard for determining the scope of consent).</p>
</footnote>
<footnote label="18">
<p id="p-105"><em>See</em> <em>United States v. Dyer</em> , <extracted-citation case-ids="1548216" index="52" url="https://cite.case.law/f2d/784/812/#p816"><span class="citation" data-id="465233"><a href="/opinion/465233/united-states-v-gary-g-dyer/" aria-description="Citation for case: United States v. Gary G. Dyer">784 F.2d 812</a></span></extracted-citation>, 816 (7th Cir. 1986) ("Clearly a person may limit or withdraw his consent to a search, and the police must honor such limitations."); <em>Painter v. Robertson</em> , <extracted-citation case-ids="11585138" index="53" url="https://cite.case.law/f3d/185/557/#p567"><span class="citation" data-id="9492333"><a href="/opinion/765393/robert-painter-v-bill-robertson-robert-tush/" aria-description="Citation for case: Robert Painter v. Bill Robertson Robert Tush">185 F.3d 557</a></span></extracted-citation>, 567 (6th Cir. 1999) ("[T]he consenting party may limit the scope of that search, and hence at any moment may retract his consent"); <em>United States v. Sanders</em> , <extracted-citation case-ids="8925205" index="54" url="https://cite.case.law/f3d/424/768/#p774"><span class="citation" data-id="9498397"><a href="/opinion/792033/united-states-v-craig-sanders-aka-sparks/" aria-description="Citation for case: United States v. Craig Sanders, A/K/A Sparks">424 F.3d 768</a></span></extracted-citation>, 774 (8th Cir. 2005) ("Once given, consent to search may be withdrawn[.]"); <em>United States v. McWeeney</em> , <extracted-citation case-ids="5560301" index="55" url="https://cite.case.law/f3d/454/1030/#p1034"><span class="citation" data-id="9499048"><a href="/opinion/795052/united-states-v-nicholas-j-mcweeney/" aria-description="Citation for case: United States v. Nicholas J. McWeeney">454 F.3d 1030</a></span></extracted-citation>, 1034 (9th Cir. 2006) ("A suspect is free, however, after initially giving consent, to delimit or withdraw his or her consent at anytime."); <em>see also</em> <em>United States v. Pelle</em> , No. 05-407, <extracted-citation index="56" url="https://cite.case.law/citations/?q=2006%20WL%20436920"><span class="citation no-link">2006 WL 436920</span></extracted-citation>, at *4 (D.N.J. Feb. 17, 2006) ("The courts which have decided the issue, however, have unanimously answered that question in the affirmative, generally holding that any such withdrawal must be supported by unambiguous acts or unequivocal statements.") (collecting cases).</p>
</footnote>
<footnote label="19">
<p id="p-106"><extracted-citation case-ids="6187551" index="57" url="https://cite.case.law/us/447/649/#p656"><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">447 U.S. 649</a></span></extracted-citation>, 656, <extracted-citation case-ids="6187551" index="58" url="https://cite.case.law/us/447/649/#p656"><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">100 S.Ct. 2395</a></span></extracted-citation>, <extracted-citation case-ids="6187551" index="59" url="https://cite.case.law/us/447/649/#p656"><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">65 L.Ed.2d 410</a></span></extracted-citation> (1980) ("When an official search is properly authorized-whether by consent or by the issuance of a valid warrant-the scope of the search is limited by the terms of its authorization.").</p>
</footnote>
<footnote label="20">
<p id="p-107"><extracted-citation case-ids="6221328" index="60" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">500 U.S. at 252</a></span></extracted-citation>, <extracted-citation case-ids="6221328" index="61" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span></extracted-citation>.</p>
</footnote>
<footnote label="21">
<p id="p-108"><em>Schneckloth</em> , <extracted-citation case-ids="6172008" index="62" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. at 228</a></span></extracted-citation>, <extracted-citation case-ids="6172008" index="63" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation> ("[A] search pursuant to consent may result in considerably less inconvenience for the subject of the search, and, properly conducted, is a constitutionally permissible and wholly legitimate aspect of effective police activity.").</p>
</footnote>
<footnote label="22">
<p id="p-109"><em>Id</em> . at 227, <extracted-citation case-ids="6172008" index="64" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation> (citation omitted).</p>
</footnote>
<footnote label="23">
<p id="p-110"><em>Dyer</em> , <extracted-citation case-ids="1548216" index="65" url="https://cite.case.law/f2d/784/812/#p816"><span class="citation" data-id="465233"><a href="/opinion/465233/united-states-v-gary-g-dyer/" aria-description="Citation for case: United States v. Gary G. Dyer">784 F.2d at 816</a></span></extracted-citation>.</p>
</footnote>
<footnote label="24">
<p id="p-111"><em>Brigham City v. Stuart</em> , <extracted-citation case-ids="3275413" index="66" url="https://cite.case.law/us/547/398/#p403"><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">547 U.S. 398</a></span></extracted-citation>, 403, <extracted-citation case-ids="3275413" index="67" url="https://cite.case.law/us/547/398/#p403"><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">126 S.Ct. 1943</a></span></extracted-citation>, <extracted-citation case-ids="3275413" index="68" url="https://cite.case.law/us/547/398/#p403"><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">164 L.Ed.2d 650</a></span></extracted-citation> (2006) (citations omitted).</p>
</footnote>
<footnote label="25">
<p id="p-112"><em>See e.g.,</em> <em>United States v. Martel-Martines</em> , <extracted-citation case-ids="10515235" index="69" url="https://cite.case.law/f2d/988/855/#p858"><span class="citation" data-id="602422"><a href="/opinion/602422/united-states-v-miguel-martel-martines/" aria-description="Citation for case: United States v. Miguel Martel-Martines">988 F.2d 855</a></span></extracted-citation>, 858 (8th Cir. 1993) ; <em>see also</em> <em>Jimeno,</em> <extracted-citation case-ids="6221328" index="70" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">500 U.S. at 251</a></span></extracted-citation>, <extracted-citation case-ids="6221328" index="71" url="https://cite.case.law/us/500/248/#p252"><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span></extracted-citation> ("The standard for measuring the scope of a suspect's consent under the Fourth Amendment is that of 'objective' reasonableness-what would the typical reasonable person have understood by the exchange between the officer and the suspect?" (citations omitted) ).</p>
</footnote>
<footnote label="26">
<p id="p-113"><em>See, e.g.,</em> <em>United States v. $304,980.00 in U.S. Currency</em> , <extracted-citation case-ids="3710672" index="72" url="https://cite.case.law/f3d/732/812/#p820"><span class="citation" data-id="2709255"><a href="/opinion/2709255/united-states-v-30498000-in-united-states-currency/" aria-description="Citation for case: United States v. $304,980.00 in United States Currency">732 F.3d 812</a></span></extracted-citation>, 820 (7th Cir. 2013) ("[P]olice officers do not act unreasonably by failing to halt their search every time a consenting suspect equivocates."); <em>Martel-Martines</em> , <extracted-citation case-ids="10515235" index="73" url="https://cite.case.law/f2d/988/855/#p858"><span class="citation" data-id="602422"><a href="/opinion/602422/united-states-v-miguel-martel-martines/#858" aria-description="Citation for case: United States v. Miguel Martel-Martines">988 F.2d at 858</a></span></extracted-citation> (requiring " 'unequivocal act or statement of withdrawal' " (quoting <em>United States v. Alfaro</em> , <extracted-citation case-ids="10533570" index="74" url="https://cite.case.law/f2d/935/64/#p67"><span class="citation" data-id="562331"><a href="/opinion/562331/united-states-v-daniel-alfaro/" aria-description="Citation for case: United States v. Daniel Alfaro">935 F.2d 64</a></span></extracted-citation>, 67 (5th Cir. 1991) ).)</p>
</footnote>
<footnote label="27">
<p id="p-114"><em>Williams</em> , <extracted-citation index="75" url="https://cite.case.law/citations/?q=2015%20WL%205602617"><span class="citation no-link">2015 WL 5602617</span></extracted-citation>, at *6 ; App. 196, 198-99.</p>
</footnote>
<footnote label="28">
<p id="p-115"><em>Williams</em> , <extracted-citation index="76" url="https://cite.case.law/citations/?q=2015%20WL%205602617"><span class="citation no-link">2015 WL 5602617</span></extracted-citation> at *9.</p>
</footnote>
<footnote label="29">
<p id="p-116"><extracted-citation case-ids="9248250" index="77" url="https://cite.case.law/f3d/369/1024/#p1026"><span class="citation" data-id="786374"><a href="/opinion/786374/united-states-v-darnell-a-gray/" aria-description="Citation for case: United States v. Darnell A. Gray">369 F.3d 1024</a></span></extracted-citation>, 1026 (8th Cir. 2004).</p>
</footnote>
<footnote label="30">
<p id="p-117"><em><extracted-citation case-ids="9248250" index="78" url="https://cite.case.law/f3d/369/1024/#p1026"><span class="citation" data-id="786374"><a href="/opinion/786374/united-states-v-darnell-a-gray/" aria-description="Citation for case: United States v. Darnell A. Gray">Id.</a></span></extracted-citation></em></p>
</footnote>
<footnote label="31">
<p id="p-118"><em>U.S. v. Sanders</em> , <extracted-citation case-ids="8925205" index="79" url="https://cite.case.law/f3d/424/768/#p774"><span class="citation" data-id="9498397"><a href="/opinion/792033/united-states-v-craig-sanders-aka-sparks/" aria-description="Citation for case: United States v. Craig Sanders, A/K/A Sparks">424 F.3d 768</a></span></extracted-citation>, 774 (8th Cir. 2005) (citing <em>Gray</em> , <extracted-citation case-ids="9248250" index="80" url="https://cite.case.law/f3d/369/1024/#p1026">369 F.3d at </extracted-citation>1026 ).</p>
</footnote>
<footnote label="32">
<p id="p-119"><em>Schneckloth</em> , <extracted-citation case-ids="6172008" index="81" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. at 228</a></span></extracted-citation>, <extracted-citation case-ids="6172008" index="82" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation>.</p>
</footnote>
<footnote label="33">
<p id="p-120"><em>United States v. Antoon</em> , <extracted-citation case-ids="10541708" index="83" url="https://cite.case.law/f2d/933/200/#p203"><span class="citation" data-id="561269"><a href="/opinion/561269/united-states-v-michael-s-antoon-john-a-bettor-xavier-w-folino-dba/" aria-description="Citation for case: United States v. Michael S. Antoon John A. Bettor Xavier...">933 F.2d 200</a></span></extracted-citation>, 203 (3d Cir. 1991).</p>
</footnote>
<footnote label="34">
<p id="p-121"><em>Price</em> , <extracted-citation case-ids="3359359" index="84" url="https://cite.case.law/f3d/558/270/#p276">558 F.3d at </extracted-citation>278 (citing <em>Schneckloth</em> , <extracted-citation case-ids="6172008" index="85" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. at 226</a></span></extracted-citation>, <extracted-citation case-ids="6172008" index="86" url="https://cite.case.law/us/412/218/#p219"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation> ; <em>United States v. Kim</em> , <extracted-citation case-ids="10531471" index="87" url="https://cite.case.law/f3d/27/947/#p955"><span class="citation" data-id="9486933"><a href="/opinion/672873/united-states-v-yong-hyon-kim/" aria-description="Citation for case: United States v. Yong Hyon Kim">27 F.3d 947</a></span></extracted-citation>, 955 (3d Cir. 1994) ).</p>
</footnote>
<footnote label="35">
<p id="p-122"><em>Antoon,</em> <extracted-citation case-ids="10541708" index="88" url="https://cite.case.law/f2d/933/200/#p203"><span class="citation" data-id="561269"><a href="/opinion/561269/united-states-v-michael-s-antoon-john-a-bettor-xavier-w-folino-dba/#204" aria-description="Citation for case: United States v. Michael S. Antoon John A. Bettor Xavier...">933 F.2d at 204</a></span></extracted-citation> (citation omitted).</p>
</footnote>
<footnote label="36">
<p id="p-123"><em>Id</em> . (quoting <em>Krasnov v. Dinan</em> , <extracted-citation case-ids="714667" index="89" url="https://cite.case.law/f2d/465/1298/#p1302"><span class="citation" data-id="305328"><a href="/opinion/305328/george-s-krasnov-v-brendan-dinan/" aria-description="Citation for case: George S. Krasnov v. Brendan Dinan">465 F.2d 1298</a></span></extracted-citation>, 1302 (3d Cir.1972) ).</p>
</footnote>
<footnote label="37">
<p id="p-124">U.S.S.G. § 4B1.1(a).</p>
</footnote>
<footnote label="38">
<p id="p-125"><em>Taylor v. United States</em> , <extracted-citation case-ids="634101" index="90" url="https://cite.case.law/us/495/575/"><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">495 U.S. 575</a></span></extracted-citation>, 588, <extracted-citation case-ids="634101" index="91" url="https://cite.case.law/us/495/575/"><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">110 S.Ct. 2143</a></span></extracted-citation>, <extracted-citation case-ids="634101" index="92" url="https://cite.case.law/us/495/575/"><span class="citation" data-id="9432018"><a href="/opinion/112435/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">109 L.Ed.2d 607</a></span></extracted-citation> (1990).</p>
</footnote>
<footnote label="39">
<p id="p-126"><em>See, e.g.</em> , <em>United States v. Chapman</em> , <extracted-citation case-ids="12275357" index="93" url="https://cite.case.law/f3d/866/129/#p133"><span class="citation" data-id="9877744"><a href="/opinion/4416181/united-states-v-shaun-chapman/" aria-description="Citation for case: United States v. Shaun Chapman">866 F.3d 129</a></span></extracted-citation>, 133 (3d Cir. 2017).</p>
</footnote>
<footnote label="40">
<p id="p-127"><em>United States v. Robinson</em> , <extracted-citation case-ids="12175092" index="94" url="https://cite.case.law/f3d/844/137/#p142"><span class="citation" data-id="9870456"><a href="/opinion/4331288/united-states-v-anthony-robinson/" aria-description="Citation for case: United States v. Anthony Robinson">844 F.3d 137</a></span></extracted-citation>, 142 (3d Cir. 2016).</p>
</footnote>
<footnote label="41">
<p id="p-128"><em>Descamps v. United States</em> , <extracted-citation case-ids="12698469" index="95" url="https://cite.case.law/us/570/254/#p261"><span class="citation" data-id="9515838"><a href="/opinion/903971/descamps-v-united-states/" aria-description="Citation for case: Descamps v. United States">570 U.S. 254</a></span></extracted-citation>, 261-62, <extracted-citation case-ids="12698469" index="96" url="https://cite.case.law/us/570/254/#p261"><span class="citation" data-id="9515838"><a href="/opinion/903971/descamps-v-united-states/" aria-description="Citation for case: Descamps v. United States">133 S.Ct. 2276</a></span></extracted-citation>, <extracted-citation case-ids="12698469" index="97" url="https://cite.case.law/us/570/254/#p261"><span class="citation" data-id="9515838"><a href="/opinion/903971/descamps-v-united-states/" aria-description="Citation for case: Descamps v. United States">186 L.Ed.2d 438</a></span></extracted-citation> (2013) (reiterating that, for purposes of this inquiry, we may not examine a defendant's prior conduct).</p>
</footnote>
<footnote label="42">
<p id="p-129"><em>Mathis v. United States</em> , --- U.S. ----, <extracted-citation case-ids="12598042" index="98" url="https://cite.case.law/s-ct/136/2243/"><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">136 S.Ct. 2243</a></span></extracted-citation>, 2248, <extracted-citation case-ids="12598042" index="99" url="https://cite.case.law/s-ct/136/2243/"><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">195 L.Ed.2d 604</a></span></extracted-citation> (2016) ; <em>see also</em> 3d Cir. Model Crim. Jury Instr. 6.18.1962C-6 (2018) (establishing that the government must prove predicate acts beyond a reasonable doubt to sustain a conviction).</p>
</footnote>
<footnote label="43">
<p id="p-130"><extracted-citation index="100" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%201961"><span class="citation no-link">18 U.S.C. § 1961</span></extracted-citation>(1)(D).</p>
</footnote>
<footnote label="44">
<p id="p-131">App. 324.</p>
</footnote>
<footnote label="45">
<p id="p-132">Supp. App. 19-25.</p>
</footnote>
<footnote label="46">
<p id="p-133"><extracted-citation index="101" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">21 U.S.C. § 841</span></extracted-citation>(a)(1).</p>
</footnote>
<footnote label="47">
<p id="p-134"><extracted-citation index="102" url="https://cite.case.law/citations/?q=18%20U.S.C.%20%C2%A7%201961"><span class="citation no-link">18 U.S.C. § 1961</span></extracted-citation>(1)(D)</p>
</footnote>
<footnote label="48">
<p id="p-135"><em><extracted-citation case-ids="9248250" index="103" url="https://cite.case.law/f3d/369/1024/#p1026"><span class="citation no-link">Id.</span></extracted-citation></em> §§ 1961(1)(D), 1962(c).</p>
</footnote>
<footnote label="49">
<p id="p-136"><em>Mathis</em> , <extracted-citation case-ids="12598042" index="104" url="https://cite.case.law/s-ct/136/2243/"><span class="citation" data-id="9824286"><a href="/opinion/3216494/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">136 S.Ct. at 2249</a></span></extracted-citation>.</p>
</footnote>
<footnote label="50">
<p id="p-137">U.S.S.G. § 4B1.2(b).</p>
</footnote>
</opinion>
```

---
