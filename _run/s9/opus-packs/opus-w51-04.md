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

## GROUP: content/cases/United States v. Basher.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Basher"
type: case
citation: "629 F.3d 1161 (2011)"
parallel_cite: ""
neutral_cite: "2011 U.S. App. LEXIS 1064; 2011 WL 167045"
court: "U.S. Court of Appeals, 9th Circuit"
court_level: coa
circuit: 9th
year: 2011
date_decided: 2011-01-20
docket: ""
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Basher
  varies_by_point: false
  scope_note: "Good law in-circuit; reaffirms tent privacy while holding the area outside a dispersed-campsite tent is not curtilage."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/183144/united-states-v-basher/"
  cluster_id: 183144
  opinion_id: 183144
  identity_checked: true
homes:
  - page: "[[Tents]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Curtilage]]"
    role: "Related (cross-doctrine)"
related: ["[[Oliver v. United States]]", "[[California v. Ciraolo]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "curtilage", "tents"]
holding: "(Persuasive (outside circuit) — 9th Cir.) Reaffirms privacy inside a tent ('comparable to a house, apartment, or hotel room'), but the area outside the tent in a dispersed public-land campsite is not curtilage."
lake:
  record_id: United States v. Basher
  status: verified
  projected_at: 2026-07-06
---

# United States v. Basher

*629 F.3d 1161 (9th Cir. 2011)* · U.S. Court of Appeals, 9th Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Basher was camping in a dispersed, undeveloped area of public (National Forest) land when officers, responding to reports of illegal gunfire and an illegal campfire during a burn ban, approached his campsite and tent. His camp was visible from the developed area where officers had stayed. After questioning and observing shotgun shells in plain view, officers searched the area outside the tent and the tent. Basher moved to suppress, claiming a protected privacy interest in his campsite.

## Issue
Whether a camper has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the area outside his tent at a dispersed public-land campsite — i.e., whether that surrounding area is [[Curtilage|curtilage]].

## Rule
A tent itself is a private space: "A tent is comparable to a house, apartment, or hotel room because it is a private area where people sleep and change clothing." — 629 F.3d at 1169. ^pin-1169

But the open area around a tent on dispersed public land is not [[Curtilage|curtilage]]. The court held that, on these facts, "there was no expectation of privacy in the campsite, and that the area outside of the tent in these circumstances is not curtilage." — *Id.* at 1169. ^pin-1169a

## Application
Because Basher's camp sat on undeveloped public land, in an area open to the public and visible from the developed campground, the space outside his tent carried no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] and was not [[Curtilage|curtilage]] to be treated like the grounds of a home. The interior of the tent remained a protected private area, but the officers' observations and search of the exposed surrounding campsite did not invade a constitutionally protected privacy interest.

## Conclusion
The area outside Basher's tent at the dispersed public-land campsite was not [[Curtilage|curtilage]] and carried no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]]; suppression was denied and the conviction affirmed. Tent interiors are private like a home, but the exposed ground around a public-land campsite is not.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.**
- *Basher* applies the open-and-exposed-land logic of [[Oliver v. United States]] and [[California v. Ciraolo]] to camping, while preserving the [[Katz v. United States]] expectation-of-privacy interest in the tent's interior.

## Appears on
- [[Tents]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Basher*, 629 F.3d 1161 (9th Cir. 2011) — https://www.courtlistener.com/opinion/183144/united-states-v-basher/ — pinpoint: 1169.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "818663b1eca338a6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "629 F.3d 1161 (2011)", "court": "U.S. Court of Appeals, 9th Circuit", "neutral_cite": "2011 U.S. App. LEXIS 1064; 2011 WL 167045", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Basher", "year": "2011"}}
{"assertion_id": "6df6f83eeed8d8cf", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Related (cross-doctrine)", "title": "United States v. Basher"}}
{"assertion_id": "c7c1bf78325a6b52", "dimension": "support", "kind": "home_role", "locator": {"home": "Tents"}, "payload": {"home": "Tents", "role": "Key — Progeny / Refinement", "title": "United States v. Basher"}}
{"assertion_id": "f45b11ee0d9cbb21", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "(Persuasive (outside circuit) — 9th Cir.) Reaffirms privacy inside a tent ('comparable to a house, apartment, or hotel room'), but the area outside the tent in a dispersed public-land campsite is not curtilage.", "title": "United States v. Basher"}}
{"assertion_id": "87218c1e6c7ea707", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Basher"}}
{"assertion_id": "97333510732e8e73", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Basher", "field_i_validity": "good_law", "scope_note": "Good law in-circuit; reaffirms tent privacy while holding the area outside a dispersed-campsite tent is not curtilage.", "title": "United States v. Basher", "varies_by_point": "false"}}
```

### lake record — United States v. Basher

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Basher",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Basher",
    "case_name_short": "Basher",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Michael Emery BASHER, Defendant-Appellant",
    "input_case_name": "United States v. Basher",
    "court": "U.S. Court of Appeals, 9th Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2011-01-20",
    "year": 2011,
    "docket": null,
    "cluster_id": 183144,
    "lead_opinion_id": 183144,
    "sibling_ids": [
      183144
    ],
    "absolute_url": "/opinion/183144/united-states-v-basher/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "629 F.3d 1161",
      "volume": "629",
      "reporter": "F.3d",
      "page": "1161",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. App. LEXIS 1064",
        "volume": "2011",
        "reporter": "U.S. App. LEXIS",
        "page": "1064",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 WL 167045",
        "volume": "2011",
        "reporter": "WL",
        "page": "167045",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "629 F.3d 1161",
        "volume": "629",
        "reporter": "F.3d",
        "page": "1161",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. App. LEXIS 1064",
        "volume": "2011",
        "reporter": "U.S. App. LEXIS",
        "page": "1064",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 WL 167045",
        "volume": "2011",
        "reporter": "WL",
        "page": "167045",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "629 F.3d 1161",
    "official_selection": {
      "court_class": "coa",
      "selected": "629 F.3d 1161",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1169",
      "page": null,
      "quote": "--- # United States v. Basher *629 F.3d 1161 (9th Cir. 2011)* \u00b7 U.S. Court of Appeals, 9th Circuit \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Basher was camping in a dispersed, undeveloped area of public (National Forest) land when officers, responding to reports of illegal gunfire and an illegal campfire during a burn ban, approached his campsite and tent. His camp was visible from the developed area where officers had stayed. After questioning and observing shotgun shells in plain view, officers searched the area outside the tent and the tent. Basher moved to suppress, claiming a protected privacy interest in his campsite. ## Issue Whether a camper has a reasonable expectation of privacy in the area outside his tent at a dispersed public-land campsite \u2014 i.e., whether that surrounding area is curtilage. ## Rule A tent itself is a private space:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1169a",
      "page": null,
      "quote": "there was no expectation of privacy in the campsite, and that the area outside of the tent in these circumstances is not curtilage.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": null,
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Basher",
    "varies_by_point": false,
    "scope_note": "Good law in-circuit; reaffirms tent privacy while holding the area outside a dispersed-campsite tent is not curtilage.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Johnson v. Bay Area Rapid Transit District",
          "cluster_id": 1035754,
          "cite": [
            "724 F.3d 1159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Xzavione Taylor",
          "cluster_id": 9380817,
          "cite": [
            "60 F.4th 1233"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Nishi",
          "cluster_id": 5811207,
          "cite": [
            "207 Cal. App. 4th 954",
            "143 Cal. Rptr. 3d 882",
            "2012 WL 2870591",
            "2012 Cal. App. LEXIS 806"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joshua Lucas",
          "cluster_id": 4319190,
          "cite": [
            "841 F.3d 796",
            "2016 U.S. App. LEXIS 20141",
            "2016 WL 6595972"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daino",
          "cluster_id": 4832810,
          "cite": [
            "475 P.3d 354"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Markanthony Sapalasan",
          "cluster_id": 9489620,
          "cite": [
            "97 F.4th 657"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Escobar",
          "cluster_id": 7330094,
          "cite": [
            "309 F. Supp. 3d 778"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mitchell",
          "cluster_id": 10308415,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Xzavione Taylor",
          "cluster_id": 9380540,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tekoh v. County of Los Angeles",
          "cluster_id": 7327016,
          "cite": [
            "270 F. Supp. 3d 1163"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Brian Anthony Wiley",
          "cluster_id": 4714059,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Richard L. Beck",
          "cluster_id": 3149271,
          "cite": [
            "157 Idaho 402",
            "336 P.3d 809",
            "2014 Ida. App. LEXIS 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Basher:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(183144) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(183144)",
        "reviewed": 13,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 12,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(183144)",
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
    "complete_query": "cites:(183144)",
    "indexed_citing_opinions": 13,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 183144,
        "count": 13,
        "count_source": "search"
      }
    ],
    "citation_count": 154,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-basher.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 13,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 183144,
        "cited_id": 91,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 137742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 142878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 145496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 171585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 654273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 746804,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 765204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 770197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 770456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 779346,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 785454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 796411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 796826,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 1354603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 1382743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 1390224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 1464333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 1863711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 183144,
        "cited_id": 2517633,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LCU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T22:35:58Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:36:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:36:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:39:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:36:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Basher

```
                     FOR PUBLICATION
  UNITED STATES COURT OF APPEALS
       FOR THE NINTH CIRCUIT

UNITED STATES OF AMERICA,                        No. 09-30311
                Plaintiff-Appellee,
               v.                                  D.C. No.
                                                CR-08-2127-RWH
MICHAEL EMERY BASHER,
                                                   OPINION
             Defendant-Appellant.
                                           
         Appeal from the United States District Court
           for the Eastern District of Washington
         Robert H. Whaley, District Judge, Presiding

                    Argued and Submitted
               May 6, 2010—Seattle, Washington

                      Filed January 20, 2011

   Before: Kim McLane Wardlaw and Ronald M. Gould,
 Circuit Judges, and Richard Mills,* Senior District Judge.

                     Opinion by Judge Mills




   *The Honorable Richard Mills, Senior United States District Judge for
the Central District of Illinois, sitting by designation.

                                 1149
1152                UNITED STATES v. BASHER




                          COUNSEL

James A. McDevitt, United States Attorney, Alexander C.
Ekstrom (argued), Assistant United States Attorney, Yakima,
Washington, for the plaintiff-appellee.

Diane E. Hehir, Assistant Federal Public Defender, Federal
Defenders of Eastern Washington & Idaho, Yakima, Wash-
ington, for the defendant-appellant.


                          OPINION

MILLS, Senior District Judge:

  Michael E. Basher (“Basher”) appeals the denial of his
motion to suppress a firearm and statements made to police
who arrested him after responding to reports of an illegal fire
and discharge of a firearm on National Forest Service land.
Basher entered a conditional guilty plea after the district court
                     UNITED STATES v. BASHER                     1153
denied his motion to suppress. Basher was convicted of being
a prohibited person in possession of a firearm, in violation of
18 U.S.C. § 922(g)(1), and for possession of an unregistered
firearm, in violation of 26 U.S.C. § 5861(d).

   We have jurisdiction pursuant to 28 U.S.C. § 1291, and we
affirm.

                                  I.

   On the night of September 1, 2007, campers on National
Forest Service land in Yakima County, Washington heard
intermittent gunfire over the course of two hours coming from
a “dispersed” or undeveloped campsite on the bank of the
South Fork River. Campers also observed a campfire at the
same location, although a burn ban was in effect. Among the
campers who heard the gunfire were two off-duty law
enforcement officers.

   The topography surrounding the dispersed campsite,
including a rock wall, caused an echo phenomenon that dis-
torted the report of the firearm, so the officers could not tell
what kind of weapon was being discharged. While the echo
phenomenon distorted the report of the firearm, it did not
seem to affect the campers’ ability to locate the source of the
firing. Campers and one of the officers identified the dis-
persed campsite as the source of the firing.

   The two off-duty officers—Yakima County Sheriff’s Dep-
uty Dan Cypher1 and Forest Service Officer Blair Bickel—
checked into duty the following morning and each traveled
toward the dispersed campsite to investigate. Officer Bickel
arrived first and contacted Deputy Cypher by radio, informing
him that he wished to investigate the occurrences at the camp-
  1
   The Yakima County Sheriff’s Department has a contract to provide law
enforcement services to the United States Forest Service.
1154               UNITED STATES v. BASHER
site. Deputy Cypher was en route, and arrived immediately
after the radio communication.

   Upon arriving, Deputy Cypher parked his vehicle nose to
nose with Basher’s truck. While Deputy Cypher later testified
that this would block the vehicle’s exit, Officer Bickel testi-
fied that there was sufficient room to drive around the police
vehicle. Deputy Cypher emitted a few short bursts from his
vehicle’s siren.

  Deputy Cypher noticed that the driver’s side window of
Basher’s truck was rolled down, and that a box of shotgun
shells was lying in plain view on the driver’s seat. He also
noted that the box was open and half-empty. Deputy Cypher
pointed out the box of shotgun shells to Officer Bickel.

   The officers also observed the fire ring as they approached
the tent. Officer Cypher testified that in addition to the rocks
typically placed around the edge of a fire ring, this fire ring
had additional rocks stacked on top, creating a cone of rocks
that could inhibit observation of the fire. Deputy Cypher testi-
fied that he saw smoke rising from the fire ring, and that the
contents appeared to be smoldering. Officer Bickel remem-
bered seeing ashes that were consistent with a recent fire, but
could not recall seeing smoke.

   From their position, the officers were facing the rear of the
tent. Upon drawing closer to the tent, Deputy Cypher
announced “Sheriff’s Office” after noticing that the occupants
were moving within the tent. The occupants were asked to
exit the tent, and they came out of their own volition.

   As the individuals exited the tent, Deputy Cypher told them
to keep their hands in view. Deputy Cypher could not recall
his exact words, and Officer Bickel could only recall that the
word “hands” was used. The officers did not have their weap-
ons drawn or yell at Basher or his son. There was no testi-
mony that Basher and his son were ordered out of the tent.
                   UNITED STATES v. BASHER               1155
The officers guided Basher away from the tent, slightly sepa-
rating him from his son. The officers engaged in small talk
with them, and Basher lit a cigarette. No one was placed in
handcuffs or frisked.

   Deputy Cypher then asked Basher where the gun was.
Basher responded “What gun?” Deputy Cypher told Basher
that he had seen the shotgun shells and explained there were
reports of gunfire coming from the campsite. Basher
responded that the gun was in the tent.

   Deputy Cypher asked if Basher’s son could retrieve the
weapon from the tent. Basher looked at his son and nodded
affirmatively for him to retrieve the gun. Deputy Cypher gave
the son instructions on how to safely retrieve the weapon. The
officers did not enter the tent at any point.

   The son went into the tent, and came out with a sawed-off
shotgun. Deputy Cypher testified that he immediately recog-
nized that the shotgun was of an illegal length, and arrested
Basher. Deputy Cypher read Basher his Miranda rights, and
Basher waived his rights. Basher subsequently made inculpa-
tory statements. Upon running Basher’s name through a data-
base, Deputy Cypher discovered that Basher had an
outstanding warrant from Lewis County. Basher was subse-
quently transported to jail. Ultimately, Basher was not for-
mally charged with violating provisions in the Code of
Federal Regulations (“C.F.R.”) regarding the illegal campfire
or the firing of the weapon, nor was he charged for analogous
state crimes.

   On November 13, 2008, Basher was indicted and charged
with being a prohibited person in possession of a firearm, in
violation of 18 U.S.C. § 922(g)(1), and possession of an
unregistered firearm, in violation of 26 U.S.C. § 5861(d).
Basher filed his motion to suppress on February 27, 2009, and
a hearing was held on March 11, 2009. Neither Basher nor his
son testified at the suppression hearing.
1156                  UNITED STATES v. BASHER
   The district court denied the motion to suppress, following
testimony and argument by counsel. The district court made
the following factual findings: (1) both officers were aware
that gunshots had been fired; (2) Deputy Cypher believed the
firing came from the dispersed campsite and Officer Bickel
did not know where the firing originated; and (3) Officer
Bickel was able to determine from witness statements that the
firing came from the dispersed campsite, and that there was
an illegal fire at that location.

   The district court ruled that the officers’ conduct was law-
ful under Terry v. Ohio, 392 U.S. 1 (1968). The district court
held alternatively that there was probable cause to arrest
Basher for illegal discharge of a weapon and for violating the
burn ban, and that in any event, the questioning regarding the
gun falls under the public safety exception.

  Basher entered a conditional guilty plea on April 24, 2009,
and he was sentenced to a term of 15 months on August 4,
2009. Basher filed his Notice of Appeal on August 20, 2009.
According to the Bureau of Prisons (“BOP”) Inmate Locator
Service, Basher was released from custody on February 12,
2010.2

                                   II.

                                   A.

   “ ‘We review de novo motions to suppress, and any factual
findings made at the suppression hearing for clear error.’ ”
United States v. Ruckes, 586 F.3d 713, 716 (9th Cir. 2009)
(quoting United States v. Negrete-Gonzales, 966 F.2d 1277,
1282 (9th Cir. 1992)).
   2
     See Inmate Locator, http://www.bop.gov/iloc2/LocateInmate.jsp (last
visited Dec. 4, 2010). We take judicial notice of this information that is
available to the public. See Demis v. Sniezek, 558 F.3d 508, 513 n.2 (6th
Cir. 2009); see also United States v. Montgomery, 550 F.3d 1229, 1231
n.1 (10th Cir. 2008).
                   UNITED STATES v. BASHER                1157
                              B.

   [1] The officers’ interaction with Basher was a valid Terry
encounter. An investigatory stop or encounter does not violate
the Fourth Amendment if the officers have “reasonable suspi-
cion supported by articulable facts that criminal activity ‘may
be afoot.’ ” United States v. Sokolow, 490 U.S. 1, 7 (1989)
(quoting Terry v. Ohio, 392 U.S. 1, 30 (1968)).

   In deciding whether a stop was supported by reasonable
suspicion, the court must consider whether “in light of the
totality of the circumstances, the officer had a particularized
and objective basis for suspecting the particular person
stopped of criminal activity.” United States v. Berber-Tinoco,
510 F.3d 1083, 1087 (9th Cir. 2007) (internal quotation marks
and citation omitted).

   [2] Deputy Cypher and Officer Bickel had well-founded
suspicions of criminal activity originating in Basher’s camp.
The record indicates, and the district court found, that Deputy
Cypher determined that the firing originated from Basher’s
dispersed campsite. Although Officer Bickel did not know
initially where the firing came from, he was able to interview
witnesses and determine that the firing came from the
Basher’s dispersed campsite. The witness reports received in
person by the officers appear to have been credible, and pro-
vided a legitimate basis for investigating, although the offi-
cers did not write down the witnesses’ names. See United
States v. Palos-Marquez, 591 F.3d 1272, 1275-77 (9th Cir.
2010) (holding that an in-person tip can be sufficiently reli-
able to justify an investigatory stop).

   Basher has attempted to portray the officers as merely act-
ing upon a hunch. However, it appears from the record that
there were specific and articulable facts that led each officer
to believe that the shooting and campfire should be investi-
gated. It is noteworthy that it appears from the record that
each officer decided independently to pursue this matter.
1158                   UNITED STATES v. BASHER
   Basher has argued that by the time the officers arrived at
the dispersed campsite there was no longer a reason to investi-
gate under Terry because the illegal acts had ceased. How-
ever, it was reasonable to believe that the activities would
recur. When dealing with illegal sporadic gunfire, there is no
guarantee that the culprits will refrain from firing again in the
future. The same can be said for the use of an illegal campfire
during a burn ban. Therefore, the officers could have reason-
ably assumed that the firing could resume sometime in the
near term.

   Basher states that Deputy Cypher had no reason under
Terry to ask about a firearm after Basher and his son exited
the tent, because they were unarmed and the weapon was in
the tent. Although Terry often comes up in the context of offi-
cer safety, the whole purpose of a Terry encounter is to inves-
tigate suspected criminal activity. See Terry, 392 U.S. at 22.
The officers were justified asking about the gun because it
was within the scope of the investigation and to ensure officer
safety.

   [3] Here, the officers were investigating a gun crime and
an illegal campfire. When police officers investigate gun
crimes, it is routine to ask questions about guns. It is reason-
able for officers investigating a gun crime to determine
whether a firearm is present, and what kind of firearm it is.
Therefore, the questions regarding the gun were within the
scope of the Terry encounter.3
  3
    If the officers had asked questions about something other than a gun,
it would not have necessarily created a seizure under the Fourth Amend-
ment. In the context of a Terry stop, a person’s Fourth Amendment rights
are not violated by the asking of questions, as long as the seizure itself is
lawful under Terry and the encounter is not prolonged by the questioning.
See United States v. Mendez, 476 F.3d 1077, 1080 (9th Cir. 2007)
(“ ‘[M]ere police questioning does not constitute a seizure’ unless it pro-
longs the detention of the individual, and, thus, no reasonable suspicion is
required to justify questioning that does not prolong the stop.” (quoting
Muehler v. Mena, 544 U.S. 93, 101 (2005))); cf. Illinois v. Caballes, 543
                       UNITED STATES v. BASHER                        1159
                                    C.

   [4] The parties dispute whether Miranda applies. Officers
are required to inform suspects of their Fifth Amendment
rights before custodial interrogations. Miranda v. Arizona,
384 U.S. 436, 444-45 (1966). The standard for determining
whether police questioning rises to the level of a custodial
interrogation is detailed below:

     Miranda warnings are required only where there has
     been such a restriction on a person’s freedom as to
     render him “in custody.” The “ultimate inquiry”
     underlying the question of custody is simply whether
     there was a formal arrest or restraint on freedom of
     movement of the degree associated with a formal
     arrest. To answer this question, the reviewing court
     looks to the totality of the circumstances that might
     affect how a reasonable person in that position
     would perceive his or her freedom to leave.

Stanley v. Schriro, 598 F.3d 612, 618 (9th Cir. 2010) (internal
quotation marks, alterations, and citations omitted).

   [5] In this case, there was no display of weapons by the
officers, no use of physical force, and it does not appear there
was threatening language. Immediately before the questions
about the firearm, Deputy Cypher and Basher were making
small talk and Basher lit a cigarette. It does not appear that
Basher’s movements were significantly curtailed.

   [6] Basher argues that he and his son were seized while
inside the tent because of the officers’ show of force. Basher’s

U.S. 405, 407-08 (2005) (holding that a dog sniff carried out during a traf-
fic stop, when there is no reasonable suspicion of drug activity, does not
violate the Fourth Amendment as long as the duration of the stop was not
extended by the dog sniff).
1160                    UNITED STATES v. BASHER
assertion that the officers presented an overwhelming show of
force is unpersuasive. Deputy Cypher merely alerted Basher
and his son to the officers’ presence by briefly sounding the
siren and announcing “Sheriff’s Department.” Furthermore,
Basher’s emphasis on the “hands” comment is unfounded.
Police officers routinely ask individuals to keep their hands in
sight for officer protection, and in this case the request does
not appear to have been made in a threatening manner.
Although Basher argues that his truck was blocked in, the tes-
timony on that issue was contradictory, with Officer Bickel
testifying that there was room to drive away.

   Basher further argues that he was under duress because
under Forest Service regulations, campers and hikers are pro-
hibited from interfering with the law enforcement activities of
the officers, and that campers must respond to law enforce-
ment contact. See 36 C.F.R. § 261.3.

   This argument is without merit. First, it is unclear that this
issue was properly presented to the district court.4 Second,
Basher adduces no evidence that his cooperation was moti-
vated by a desire to comply with an obscure regulation. Third,
the regulation does not trump a person’s Fifth Amendment
right against self-incrimination. Thus, cooperation out of fear
of violating the regulation would be unreasonable.

   [7] In any event, it appears that the public safety exception
applies to the questioning. An officer’s questioning of a sus-
pect without a Miranda warning is proper if the questioning
is related to “an objectively reasonable need to protect the
police or the public from any immediate danger associated
  4
    When Basher mentioned the regulation in general terms at the hearing,
the district court requested the citation or the text of the regulation. Basher
initially provided the district court the citation of a nonexistent regulation
and later apologized being unable to provide a citation. The district court
noted, “if it has some relevance that I have to rule on it, I’d like to see it.
But other than that I don’t know—I mean you haven’t argued it.”
                   UNITED STATES v. BASHER                 1161
with the weapon.” New York v. Quarles, 467 U.S. 649, 659
n.8 (1984) (holding that similar facts established only a Terry
stop). An officer’s subjective motivation is not relevant in
analyzing whether questioning falls within the public safety
exception. Id. at 656.

   [8] In this case, Basher had not been searched or hand-
cuffed, and he could have retrieved a weapon. See United
States v. Reilly, 224 F.3d 986, 993 (9th Cir. 2000). The offi-
cers had reliable information that there was at least one gun
in the camp, and there was an objectively reasonable need to
find out where it was located. Basher has argued that there
was no reason to ask about the gun because Basher and his
son were unarmed at the time the question was asked. How-
ever, it is not clear that the officers knew that Basher was
unarmed when they asked him where the gun was located. See
Allen v. Roe, 305 F.3d 1046, 1050-51 (9th Cir. 2002) (“[T]he
gun’s actual location is irrelevant because the ‘objectively
reasonable need’ for protection is based on what the officers
knew at the time of the questioning.”).

                              D.

   [9] The district court found that the retrieval of the weapon
was voluntary, but it did not make a specific finding of fact
on Basher’s consent to the retrieval. The Fourth Amendment
provides that people are protected from warrantless searches
and seizures. Consent can be inferred from nonverbal actions,
but it must be “unequivocal and specific” and “freely and
intelligently given.” United States v. Chan-Jimenez, 125 F.3d
1324, 1328 (9th Cir. 1997) (quoting United States v. Shaibu,
920 F.2d 1423, 1426 (9th Cir. 1990)). We have held that peo-
ple can have a reasonable expectation of privacy in a tent
pitched on public land. See United States v. Gooch, 6 F.3d
673, 677 (9th Cir. 1993).

  The testimony indicates that Deputy Cypher asked for
Basher’s consent. It is undisputed that Basher affirmatively
1162                   UNITED STATES v. BASHER
nodded his head regarding the retrieval of the shotgun.
Basher’s attorney did not cross-examine Deputy Cypher on
this point.5

  [10] From the record, the head nod did not seem to be
ambiguous, and head nods have been found to express con-
sent. See, e.g., United States v. Yockey, 654 F. Supp. 2d 945,
954 (N. D. Iowa 2009). The consent in this case seems to be
specific—clearly defining who would enter the tent (his son)
and the scope of the activity (bringing the gun outside).6

   The totality of the circumstances determine whether con-
sent was “freely and intelligently given.” United States v.
Reid, 226 F.3d 1020, 1026 (9th Cir. 2000). We look to five
factors in determining voluntariness: “(1) whether defendant
was in custody; (2) whether the arresting officers had their
guns drawn; (3) whether Miranda warnings were given; (4)
whether the defendant was notified that [he] had a right not
to consent; and (5) whether the defendant had been told a
search warrant could be obtained.” United States v. Patayan
Soriano, 361 F.3d 494, 502 (9th Cir. 2004). We noted that
“[i]t is not necessary to check off all five factors, but many
of this court’s decisions upholding consent as voluntary are
supported by at least several factors.” Id. (internal quotation
marks and citation omitted).

   [11] In this case, the defendant was not in custody and the
officers did not have their guns drawn. In addition, the offi-
cers did not tell Basher that a search warrant could be
obtained if he refused to consent. On the other hand, Basher
  5
     Counsel did ask about the instructions relating to the son, but did not
elicit testimony clarifying the interaction regarding consent to search.
Instead, counsel only elicited testimony from Deputy Cypher about his
instructions to the son on how to unload the weapon.
   6
     Basher argues that one cannot give consent during a Terry encounter,
claiming that police-citizen interactions are either wholly consensual or
completely involuntary. This argument is without merit. See United States
v. Meza-Corrales, 183 F.3d 1116, 1125 (9th Cir. 1999).
                   UNITED STATES v. BASHER                1163
had not been told he could refuse consent. As indicated above,
we hold that Basher was not in custody, so the fact that no
Miranda warnings were given is inapposite. Considering the
totality of the circumstances, it appears that no Fourth
Amendment violation occurred in connection to the retrieval
of the weapon.

                              E.

   Basher has made several arguments regarding the warrant
requirement, and has drawn our attention to United States v.
Struckman, 603 F.3d 731 (9th Cir. 2010). In that case, a
neighbor saw Struckman toss a backpack over the fence of an
unoccupied home, and then saw him climb over the fence into
the backyard. Id. at 736. After a 911 call, police arrived and
confronted Struckman, who was acting erratically because he
was high on methamphetamine. Id. at 736-37. During a pat-
down search, police officers found a handgun magazine in
Struckman’s pocket and later located the handgun in the back-
pack. Id. at 737. After questioning Struckman, the police
learned that he resided at the home. Id.

   We reversed Struckman’s conviction of being a felon in
possession of a firearm, in part, because we held that the
backyard of a home is curtilage, subject to Fourth Amend-
ment protections. Id. at 739. We also held that the Terry
exception to the warrant requirement does not apply in homes.
Id. at 738.

   As mentioned above, Basher claims that he and his son
were seized while in their tent, because of the officers’ dis-
play of authority. As we have detailed, the officers merely
announced their presence, and the district court held that
Basher and his son exited the tent of their own volition. The
district court’s finding does not appear to be clearly errone-
ous, and therefore we will not disturb it. See Ruckes, 586 F.3d
at 716.
1164                UNITED STATES v. BASHER
   [12] Basher’s seizure claim is distinguishable from Struck-
man because police officers entered Struckman’s backyard,
while here the Bashers left voluntarily. Because the Bashers
left the tent voluntarily, the seizure argument necessarily fails.
See United States v. Crapser, 472 F.3d 1141, 1145-46 (9th
Cir. 2007).

   [13] In addition, Basher has referred to the warrantless
entry or search of the camp by the officers. Under Gooch,
officers cannot enter a tent without a warrant, but that case did
not address whether a campsite is also protected by the war-
rant requirement. See Gooch, 6 F.3d at 677; see also Float-
Rite Park, Inc. v. Vill. of Somerset, 629 N.W.2d 818, 824 n.2
(Wis. Ct. App. 2001) (examining Gooch and rejecting argu-
ment that expectation of privacy extends to campground).

   [14] Classifying the area outside of a tent in a National
Park or National Forest lands campsite as curtilage would be
very problematic. A tent is comparable to a house, apartment,
or hotel room because it is a private area where people sleep
and change clothing. See Gooch, 6 F.3d at 677. However,
campsites, such as the dispersed, ill-defined site here, are
open to the public and exposed.

   In United States v. Dunn, 480 U.S. 294 (1987), the
Supreme Court found that curtilage is defined by reference to
four factors: proximity of the area to the home, the nature of
the uses to which the area is put, whether the area is included
in an enclosure around the home, and the steps taken by the
resident to protect the area from observation. Id. at 301. While
these factors can be employed with reasonable certainty in the
urban residential environment, the analysis does not necessar-
ily carry over to most camping contexts. Parkland campsites
often have layouts that are vague or dispersed, and individuals
often camp in areas that are not predetermined campsites.

  [15] In the case at bar, Basher was staying in a dispersed,
or undeveloped camping area. It appears that Basher’s camp
                    UNITED STATES v. BASHER                 1165
was visible from the developed camping area where the offi-
cers had stayed the previous night. Therefore, we hold that
there was no expectation of privacy in the campsite, and that
the area outside of the tent in these circumstances is not curti-
lage. Accordingly, Struckman does not control the outcome of
this case.

                              III.

  In summary, we hold that the officers’ interaction with
Basher constituted a valid Terry encounter, and that Basher’s
Fifth Amendment rights were not violated.

  We further hold that Basher’s Fourth Amendment rights
were not violated, and that he consented to the retrieval of the
shotgun from the tent.

   [16] Finally, we hold that the area of a campsite outside of
a tent in these circumstances is not curtilage.

 Accordingly, the district court properly denied Basher’s
Motion to Suppress.

  AFFIRMED.

```

---

## GROUP: content/cases/United States v. Berkowitz.md  (`case`, 6 assertions)

### content_page

```
---
title: United States v. Berkowitz
type: case
citation: "927 F.2d 1376 (1991)"
parallel_cite: ""
neutral_cite: "1991 U.S. App. LEXIS 4135; 1991 WL 33079"
court: 7th Cir.
court_level: coa
circuit: ca7
year: 1991
date_decided: ""
docket: ""
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
  opinion_url: "https://www.courtlistener.com/opinion/557342/united-states-v-marvin-berkowitz/"
  cluster_id: 557342
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Berkowitz
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — constructive-entry (7th Cir. narrow side: voice-from-outside arrest OK, warrantless entry before arrest not, 927 F.2d at 1386)"
  - page: "[[Arrest in the Home]]"
    role: "Related — constructive-entry cross-ref"
related:
  - "[[Entry to Arrest]]"
  - "[[Arrest in the Home]]"
  - "[[Payton v. New York]]"
  - "[[United States v. Watson]]"
  - "[[Knight v. Jacobson]]"
tags:
  - case
  - fourth-amendment
  - arrest
  - warrantless-arrest
  - payton
  - home
holding: "Payton's warrant requirement for in-home arrests bars only a warrantless, nonexigent physical entry into the home, not an officer's announcement of an arrest from outside the threshold; a warrantless arrest is therefore valid where police announce it from outside and the suspect surrenders at the doorway, but unlawful where police enter the home before effecting the arrest — so a suppression claim turning on which occurred requires an evidentiary hearing."
---

# United States v. Berkowitz

*927 F.2d 1376 (7th Cir. 1991)* (No. 89-2125) · U.S. Court of Appeals for the Seventh Circuit · **Binding in-circuit — 7th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 557342 → opinion 557342 (927 F.2d 1376, decided 1991-03-15, No. 89-2125); Rule quote string-matched to the CL opinion text 2026-07-07. Note: lake stub omits date_decided + docket — flagged for S2 repair (cluster carries 1991-03-15 / No. 89-2125). S9 promotes. -->

## Background
Marvin Berkowitz was convicted of obstruction of justice and stealing government property. He moved to suppress evidence obtained after IRS agents came to his home and arrested him without a warrant. The accounts of the arrest conflicted: on the government's version, the agents knocked, and when Berkowitz opened the door they announced from outside that he was under arrest, and he acquiesced before they stepped in; on Berkowitz's version, the agents entered his home before announcing the arrest. The district court denied the motion to suppress, and Berkowitz appealed.

## Issue
Whether a warrantless arrest at the home violates *[[Payton v. New York]]* — and in particular whether it matters that officers announce the arrest from outside the threshold and the suspect surrenders at the doorway, versus entering the home before effecting the arrest.

## Rule
*[[Payton v. New York|Payton]]* draws "a firm line at the entrance to the house," which absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] may not be crossed without a warrant. But that line guards physical entry, not communication: "Payton prohibits only a warrantless entry into the home, not a policeman's use of his voice to convey a message of arrest from outside the home." — 927 F.2d at 1386. Conversely, "entering a person's home without a warrant to arrest him, where no exigent circumstances exist, violates this clear command," even if the suspect is standing at his open doorway.

## Application
The legality of Berkowitz's arrest turned on a fact the record did not resolve. If the agents announced the arrest from outside and Berkowitz surrendered at his doorway before they entered, the arrest was valid — a doorway surrender is consistent with *[[Payton v. New York|Payton]]* and with *[[United States v. Santana]]*, which treats an open doorway as a public place. But if the agents made a warrantless, nonexigent entry before announcing or effecting the arrest, that entry violated *[[Payton v. New York|Payton]]*, and *[[United States v. Santana|Santana]]* — which rested on [[Exigent Circumstances and Hot Pursuit|hot pursuit]] of a suspect who fled from a public doorway — would not save it. Because the affidavits disagreed about when the agents crossed the threshold relative to the arrest, the court [[Reading and Citing Cases#on-remand|remanded]] for an evidentiary hearing.

## Conclusion
Berkowitz's assistance-of-counsel and sentencing challenges were rejected, but the case was **[[Reading and Citing Cases#on-remand|remanded]]** for an evidentiary hearing on the motion to suppress. Manion, J., wrote for the court (Coffey, Ripple, Manion, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Berkowitz* is the Seventh Circuit's framework for the "knock and arrest" at the doorway: *[[Payton v. New York|Payton]]* is not offended when officers announce an arrest from outside and the suspect surrenders at the threshold, but it is violated by a warrantless, nonexigent entry made before the arrest is effected — the same line later drawn in *[[Knight v. Jacobson]]* between the officer's body and his voice.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Related*

## Sources
- [*United States v. Berkowitz*, 927 F.2d 1376 (7th Cir. 1991)](https://www.courtlistener.com/opinion/557342/united-states-v-marvin-berkowitz/) — pinpoint: 1386 (threshold / voice-vs-entry holding). The primary CL opinion object is paragraph-numbered; the reporter-paginated sibling opinion (CL 9481419) star-paginates 927 F.2d and places the quoted holding at 1386. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fda4ff40003920fc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "927 F.2d 1376 (1991)", "court": "7th Cir.", "neutral_cite": "1991 U.S. App. LEXIS 4135; 1991 WL 33079", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Berkowitz", "year": "1991"}}
{"assertion_id": "0a484d5270863e45", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Payton's warrant requirement for in-home arrests bars only a warrantless, nonexigent physical entry into the home, not an officer's announcement of an arrest from outside the threshold; a warrantless arrest is therefore valid where police announce it from outside and the suspect surrenders at the doorway, but unlawful where police enter the home before effecting the arrest — so a suppression claim turning on which occurred requires an evidentiary hearing.", "title": "United States v. Berkowitz"}}
{"assertion_id": "4bddefc09a398df0", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related — constructive-entry cross-ref", "title": "United States v. Berkowitz"}}
{"assertion_id": "d9c86f8bf0b060f4", "dimension": "support", "kind": "home_role", "locator": {"home": "Entry to Arrest"}, "payload": {"home": "Entry to Arrest", "role": "Key — constructive-entry (7th Cir. narrow side: voice-from-outside arrest OK, warrantless entry before arrest not, 927 F.2d at 1386)", "title": "United States v. Berkowitz"}}
{"assertion_id": "23cb182ac3a77f55", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Berkowitz", "varies_by_point": "false"}}
{"assertion_id": "92955d24a9158de9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 7th Cir.", "title": "United States v. Berkowitz"}}
```

### lake record — United States v. Berkowitz

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Berkowitz",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Marvin Berkowitz",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Marvin BERKOWITZ, Defendant-Appellant",
    "input_case_name": "United States v. Berkowitz",
    "court": "7th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca7",
    "state": null,
    "date_decided": null,
    "year": 1991,
    "docket": null,
    "cluster_id": 557342,
    "lead_opinion_id": 9481419,
    "sibling_ids": [],
    "absolute_url": "/opinion/557342/united-states-v-marvin-berkowitz/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "927 F.2d 1376",
      "volume": "927",
      "reporter": "F.2d",
      "page": "1376",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. App. LEXIS 4135",
        "volume": "1991",
        "reporter": "U.S. App. LEXIS",
        "page": "4135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 WL 33079",
        "volume": "1991",
        "reporter": "WL",
        "page": "33079",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "927 F.2d 1376",
        "volume": "927",
        "reporter": "F.2d",
        "page": "1376",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. App. LEXIS 4135",
        "volume": "1991",
        "reporter": "U.S. App. LEXIS",
        "page": "4135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 WL 33079",
        "volume": "1991",
        "reporter": "WL",
        "page": "33079",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "927 F.2d 1376",
    "official_selection": {
      "court_class": "coa",
      "selected": "927 F.2d 1376",
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
    "date_created": "2026-07-07T01:39:05Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:39:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:39:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-berkowitz--557342",
      "to_record_id": "United States v. Berkowitz",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Berkowitz

```
<opinion type="majority">
<author id="b1464-18">MANTON, Circuit Judge.</author>
<p id="b1464-19">A jury convicted Marvin Berkowitz of two counts of obstruction of justice, <span class="citation no-link">18 U.S.C. § 1503</span>, and one count of stealing government property, <span class="citation no-link">18 U.S.C. § 641</span>. Berkowitz appeals, contending that the district court erred by denying his motion to suppress evidence, that certain actions by the district court deprived him of the assistance of counsel, that when he did have counsel he provided ineffective assistance, and that the district court improperly sentenced him. <span class="citation" data-id="1475767"><a href="/opinion/1475767/united-states-v-berkowitz/" aria-description="Citation for case: United States v. Berkowitz">712 F.Supp. 707</a></span>. We reject Berkowitz’s assistance of counsel and sentencing claims, but remand for an eviden-tiary hearing on his motion to suppress.</p>
<p id="b1464-20">I.</p>
<p id="b1464-21">A grand jury indicted Berkowitz (along with others) in April 1988, alleging numerous counts of tax fraud, mail fraud, and obstruction of justice centering around the sales of allegedly fraudulent tax shelters (the “tax fraud case”). During its investigation of Berkowitz's activities, an investigation that began in 1983, the government accumulated almost 18,000 documents, plus other exhibits, all of which filled more than 50 boxes.</p>
<p id="b1464-22">The government stored this evidence in a file room in a secured area of the United States Attorney’s (USA) office in Chicago, and in June 1988 established a procedure to allow the defendants in the tax fraud case to inspect, examine, and photocopy those <page-number citation-index="1" label="1379">*1379</page-number>documents that were discoverable to prepare for trial. Boxes that were available for immediate inspection were marked with a “Y” or the word “Yes.” However, some documents such as witness statements, internal memoranda, and work product were either not discoverable or, under Fed.R. Crim.P. 16, Northern District of Illinois Local Rule 2.04, or the Jencks Act, <span class="citation no-link">18 U.S.C. § 3500</span>, were not discoverable until a later date. The government kept these documents in boxes marked with an “N” or the word “No.” To gain access to the documents, a defendant or his attorney had to make an appointment with IRS Special Agent Merle Shearer. On the appointed date, either Shearer or IRS Special Agent Frank Calabrese would escort the defendant or his attorney to the file room containing the documents.</p>
<p id="b1465-4">Of the defendants in the tax fraud case, Berkowitz showed the keenest interest in examining the government’s documents and exhibits; in fact, he was the only defendant to review documents personally at the USA’s office. Between July and October 1988, Berkowitz arranged to examine the documents and exhibits 17 times. According to Shearer, the first time he met with Berkowitz and his attorney he escorted them to the file room, explained the procedures to them, showed them which documents were and were not available to inspect, and showed them a photocopier they could use.</p>
<p id="b1465-5">Berkowitz, however, turned out to be not particularly scrupulous about following the procedure established for inspecting the documents. On August 17, Calabrese escorted Berkowitz from the file room to the elevators in the reception area of the USA’s office after a reviewing session. Calabrese returned to the file room to retrieve his briefcase, went back to the elevators, and found Berkowitz gone. When Calabrese returned to the secured area of the USA’s offices (the elevators being in an unsecured area) he found Berkowitz standing in a stall in the men’s washroom, apparently hiding. Berkowitz had no permission to return to the secured area.</p>
<p id="b1465-6">On October 5, after a reviewing session, Calabrese escorted Berkowitz and his attorney to the first floor of the Dirksen Federal Building, in which the USA’s office is located. A little later that day, Assistant United States Attorney William Cook, who was prosecuting the tax fraud case, saw Berkowitz leave the men’s bathroom in the secured area of the USA’s office and walk to the file room unescorted. After trying to find Calabrese, Cook confronted Ber-kowitz and asked where Calabrese was. Berkowitz said he was in the men’s room; he was not. Cook then went back to the file room, and asked Berkowitz what he was doing. Berkowitz told Cook that he had left something in the file room, and started moving “No” boxes around. Cook told Berkowitz those boxes were off-limits, and Berkowitz left.</p>
<p id="b1465-7">Judge Marshall, who was presiding over the tax fraud case, ordered the government to produce by November 15, 1988, a list of the evidence it intended to present at trial and the names of and any background material concerning witnesses it intended to call. To comply with this deadline, Shearer began to review the documents on October 26. At that time, Shearer discovered that about twelve of the fifty boxes of evidence were missing. An investigation revealed that none of the missing documents had been misplaced in the USA’s office. One box was found on the Dirksen Building’s seventh floor, near a freight elevator accessible both from a public area on the seventh floor and from the secured area of the USA’s office.</p>
<p id="b1465-8">Cook advised Berkowitz’s co-defendants’ attorneys that documents were missing, and gave them an inventory of the missing documents. Cook learned on November 4 that documents had been delivered to two attorneys’ offices. That same day, receptionists for each of the attorneys identified Berkowitz’s picture from a photographic array as the man who had delivered the documents.</p>
<p id="b1465-9">The IRS agents and Cook put two and two together and concluded Berkowitz had stolen the missing documents. On November 7, Shearer, Calabrese, and other IRS <page-number citation-index="1" label="1380">*1380</page-number>agents set out to Berkowitz’s home to arrest him. But despite the knowledge they had (knowledge that indisputably amounted to probable cause to arrest Berkowitz), and for reasons not apparent to us, the agents did not bother to obtain an arrest warrant.</p>
<p id="b1466-4">The parties agree that when the agents arrived at the house, Shearer knocked on the door and Berkowitz opened the door to answer. At this point, their stories diverge. According to Shearer, after Ber-kowitz opened the front door Shearer immediately told him he was under arrest. Berkowitz did not resist or attempt to close the door; he simply asked if he could have his sports coat. An agent retrieved the coat, which was draped over a chair inside Berkowitz’s house. According to Berkow-itz, however, immediately after the door was opened, Shearer stepped into the house and then told Berkowitz he was under arrest. As the government presents things, the arrest preceded the agents’ entry; as Berkowitz tells it, the entry preceded the arrest.</p>
<p id="b1466-5">After arresting Berkowitz, Shearer asked him if there was anything he wanted. Berkowitz responded that his keys were in his office. Berkowitz started walking toward his office, and Shearer and Calabrese followed him. According to Shearer, he noticed on top of a desk in Berkowitz’s office and in an alcove area under the desk numerous files and other documents (including original tax returns) that he recognized as some of the files and documents missing from the USA's office. Shearer said he was able to recognize those files and documents, in part, because his own handwriting was on some of the files. Shearer seized some of the records, and took Berkowitz away.</p>
<p id="b1466-6">That day, the government obtained a warrant to search Berkowitz’s home; the next day, the government obtained a warrant to search a safe in Berkowitz’s house. Those searches turned up numerous documents and evidence that had been missing, including checks that had been torn up and thrown in a wastebasket. But despite those searches, the government never recovered the vast majority of missing documents.</p>
<p id="b1466-8">A grand jury indicted Berkowitz, charging him with two counts of obstruction of justice, <span class="citation no-link">18 U.S.C. § 1503</span>, and one count of stealing government property, <span class="citation no-link">18 U.S.C. § 641</span>. Before trial, Berkowitz’s appointed attorney, William Huyck, filed a motion to suppress the evidence found in Berkowitz’s home during his arrest and the subsequent searches. Judge Bua, who presided over this case, denied the motion without holding an evidentiary hearing.</p>
<p id="b1466-9">About two weeks before trial, Huyck asked the district court to continue the trial because he had had insufficient time before trial to review documents in the government’s possession. Judge Bua denied the motion but urged the government to accommodate Huyck’s request to review the documents. The next day, Huyck moved to withdraw so that Berkowitz could retain a new attorney. However, since the new attorney could not be ready to try the case on the date set for trial, the judge denied this motion also.</p>
<p id="b1466-10">On the first day of trial, after the jury was selected and immediately before the opening statements, Berkowitz told the court that he wanted to represent himself. Judge Bua asked Berkowitz whether he was insisting on his constitutional right to represent himself. Berkowitz responded that he wanted to “waive the right to counsel, but ... not waive the right to have counsel”; in other words, he wanted to try the case himself but have standby counsel. Without inquiring any further into Berkow-itz’s understanding of what trying a case entailed or the disadvantages he might face by trying the case himself, the judge granted Berkowitz’s requests, declaring that “based on the little I know about your background [exactly what the judge knew does not appear in the record] ... if any defendant is competent to represent himself, it is you.... ”</p>
<p id="b1466-11">At trial, Berkowitz testified on his own behalf (with Huyck asking the questions), and admitted taking government documents out of the USA’s office. However, this admission was necessary within the <page-number citation-index="1" label="1381">*1381</page-number>context of Berkowitz’s defense, which was to deny (or at least create doubt about) his intent to deprive the government of the documents or to obstruct justice. Thus, Berkowitz testified that he did not intend to obstruct the government’s prosecution of his case. He took documents only because he believed that the government was withholding evidence and treating him unfairly in the tax fraud case. He testified that he intended only to copy and return the documents, and that he did in fact return many of the documents he took after copying them. He also testified that a number of the documents found at the time of his arrest were his own, not the government’s, thus casting (or attempting to cast) doubt on the government’s contention about how many documents he took. Ber-kowitz’s cross-examinations of the government’s witnesses (Shearer and Cook) followed this same theme.</p>
<p id="b1467-4">In the end, though, the jury did not accept Berkowitz’s defense, and convicted him of all three counts charged. The district court sentenced Berkowitz under the sentencing guidelines to sixty-three months imprisonment, which represented an upward departure from the sentencing guideline range that would have applied based on the severity of Berkowitz’s offenses and his criminal history score.</p>
<p id="b1467-5">II. Assistance of Counsel</p>
<p id="b1467-6">Berkowitz contends that we must reverse his convictions because he received ineffective assistance of counsel. According to Berkowitz, Huyck was ineffective because he failed to examine documents. Moreover, Berkowitz says that the district court effectively deprived him of counsel by denying his motion to continue the trial date and by failing to admonish him properly about the pitfalls of proceeding <em>pro se.</em></p>
<p id="b1467-7">
<em>A. Denial of Continuance.</em>
</p>
<p id="b1467-8">We first consider Berkowitz’s contention that the district judge denied him effective assistance of counsel by denying Huyck’s motion to continue the trial date. According to Berkowitz, denying the continuance left Huyck without adequate time to examine the government’s documents before trial. This lack of preparation, Ber-kowitz says, led to his decision to proceed <em>pro se.</em></p>
<p id="b1467-10">The Sixth Amendment provides that “[i]n all criminal prosecutions, the accused shall enjoy the right ... to have the Assistance of Counsel for his defense.” Normally, to show that his Sixth Amendment right to counsel has been violated, a defendant must show that deficiencies in counsel’s conduct (such as poor preparation) actually prejudiced him by casting doubt on the reliability of the trial’s outcome. See <em>United States v. Cronic, </em><span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#655" aria-description="Citation for case: United States v. Cronic">466 U.S. 648, 655-59</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#2044" aria-description="Citation for case: United States v. Cronic">104 S.Ct. 2039, 2044-47</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">80 L.Ed.2d 657</a></span> (1984); <em>Strickland v. Washington, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#691" aria-description="Citation for case: Strickland v. Washington">466 U.S. 668, 691-96</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#2066" aria-description="Citation for case: Strickland v. Washington">104 S.Ct. 2052, 2066-69</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">80 L.Ed.2d 674</a></span> (1984). However, in some cases where the defendant has no counsel at all, or an action by the prosecution or the trial court so hamstrings counsel as to effectively prevent counsel from actually assisting the defendant, prejudice is presumed and constitutional error is present without the defendant having to show actual prejudice. See, e.g., the cases cited in <em>Cronic, </em><span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">466 U.S. at 659</a></span> n. 25, 104 S.Ct. at 2047 n. 25. Berkowitz seems to be arguing that the trial judge’s denial of a continuance hampered Huyck so much (by denying him adequate time to prepare) that the denial of the continuance prevented Huyck from actually assisting Berkowitz. We disagree with this characterization.</p>
<p id="b1467-11">Trial judges have broad discretion in scheduling trials. Consequently, “only an unreasoning and arbitrary ‘insistence upon expeditiousness in the face of a justifiable request for delay’ violates the right to assistance of counsel.” <em>Morris v. Slappy, </em><span class="citation" data-id="9429156"><a href="/opinion/110914/morris-v-slappy/#11" aria-description="Citation for case: Morris v. Slappy">461 U.S. 1, 11-12</a></span>, <span class="citation" data-id="9429156"><a href="/opinion/110914/morris-v-slappy/#1616" aria-description="Citation for case: Morris v. Slappy">103 S.Ct. 1610, 1616-17</a></span>, <span class="citation" data-id="9429156"><a href="/opinion/110914/morris-v-slappy/" aria-description="Citation for case: Morris v. Slappy">75 L.Ed.2d 610</a></span> (1983). The district judge in this case did not abuse his discretion in denying the continuance motion, so that denial did not deprive Berkowitz of counsel’s assistance. Huyck had almost two months (from November 14, 1988, the date of his appointment as counsel, to January 3, 1989, the trial date) to prepare for trial. He had almost two weeks from the time the trial judge denied the continuance to <page-number citation-index="1" label="1382">*1382</page-number>the trial date. The government provided Huyck and Berkowitz with a detailed inventory of the documents it claimed were missing, and made the remaining documents available for inspection at any time. The issues in the case — essentially, whether Berkowitz stole and destroyed documents, and whether Berkowitz intended to obstruct justice — were not complex. In short, the trial judge acted well within his discretion in denying a continuance, and that denial, by itself, did not deprive Ber-kowitz of Huyck’s effective assistance. Cf. <em>United States v. Blandina, </em><span class="citation" data-id="536077"><a href="/opinion/536077/united-states-v-charles-a-blandina/#297" aria-description="Citation for case: United States v. Charles A. Blandina">895 F.2d 293, 297</a></span> (7th Cir.1989); <em>United States v. Studley, </em><span class="citation" data-id="534239"><a href="/opinion/534239/united-states-v-leland-l-studley/#521" aria-description="Citation for case: United States v. Leland L. Studley">892 F.2d 518, 521-23</a></span> (7th Cir.1989).</p>
<p id="b1468-4">
<em>B. Failure to Examine Documents.</em>
</p>
<p id="b1468-5">This brings us to Berkowitz’s second contention concerning effective assistance of counsel: that Huyck failed to provide him effective assistance because he failed to examine documents. Adequate pretrial preparation, including the examination of documents, is essential to properly represent a criminal defendant. But how much preparation is enough (like the numerous other decisions an attorney must make in the course of representation) is a matter of professional judgment. The attorney’s judgment is entitled to deference; thus, for Berkowitz to show Huyck’s performance was deficient, he must overcome a “strong presumption that [Huyck’s] conduct [fell] within the wide range of reasonable professional assistance” and show that Huyck’s pretrial preparation fell below “an objective standard of reasonableness” based on “prevailing professional norms.” <em>Strickland, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#687" aria-description="Citation for case: Strickland v. Washington">466 U.S. at 687-91</a></span>,<span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#2064" aria-description="Citation for case: Strickland v. Washington">104 S.Ct. at 2064-66</a></span>; see also <em>United States v. Weaver, </em><span class="citation" data-id="527854"><a href="/opinion/527854/united-states-v-larry-weaver-and-mark-schmanke-united-states-of-america/#1138" aria-description="Citation for case: United States v. Larry Weaver and Mark Schmanke, United...">882 F.2d 1128, 1138</a></span> (7th Cir.1989). Moreover, even if Huyck’s pretrial preparation was objectively deficient, Berkowitz must show that lack of preparation prejudiced him in the sense that a reasonable probability exists that “but for counsel’s unprofessional errors, the result of the proceeding would have been different.” <em>Strickland, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#694" aria-description="Citation for case: Strickland v. Washington">466 U.S. at 694</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#2068" aria-description="Citation for case: Strickland v. Washington">104 S.Ct. at 2068</a></span>.</p>
<p id="b1468-6">Since we presume that Huyck’s performance fell within the range of reasonable professional assistance, it is Berkowitz’s task to show otherwise. The only evidence Berkowitz cites concerning Huyck’s preparation is a statement in a new trial motion, prepared by Huyck, that he did not seek copies of the records the government had seized. But the motion states only that Huyck did not ask for copies; it does not state that Huyck did not inspect the government exhibits. Furthermore, there are indications in the record that Huyck spent considerable time reviewing records and preparing for trial. The evidence in the record is insufficient for Berkowitz to overcome the presumption that Huyck’s preparation was reasonable.</p>
<p id="b1468-8">Even if Huyck’s preparation was deficient, Berkowitz has failed to show prejudice from this deficiency. Berkowitz says that because Huyck did not review all the government’s documents, he could not show that the government never possessed many of the documents that Berkowitz allegedly stole. Berkowitz also argues that without knowing what documents the government had left after Berkowitz’s theft, Huyck could not challenge the government’s assertion that the loss of the stolen documents adversely affected the government’s ability to try the tax fraud case. Neither of these complaints are sufficient to establish prejudice. First, the evidence that Berkowitz did steal and destroy at least some documents was overwhelming: Berkowitz himself admitted taking documents, and the government recovered torn checks that had been stolen from a wastebasket in Berkowitz’s home. Second, obstruction of justice requires the government to show only that a defendant “endeavor[ed] to impede a prosecution, not that he actually impeded the prosecution. See <span class="citation no-link">18 U.S.C. § 1503</span>. The key question at trial was Berkowitz’s intent, not whether he actually impeded the tax fraud prosecution. The fact that Berkowitz actually did destroy documents and the fact that he had government documents in his house several weeks after his last visit to the USA’s office raise a strong inference that Ber-kowitz intended to impede the tax fraud case. Why else would he keep or destroy government documents? During trial, Ber-<page-number citation-index="1" label="1383">*1383</page-number>kowitz was able to identify numerous documents that the government claimed were stolen that had already been in his possession. But given the overwhelming evidence that Berkowitz did steal and destroy some documents, it is not reasonably probable that showing that some other documents the government claimed were stolen were not would have changed the jury’s verdict.</p>
<p id="b1469-4">C. <em>Waiver of Counsel.</em></p>
<p id="b1469-5">Berkowitz’s third, and potentially most substantial claim concerning assistance of counsel is his claim that the district court failed to properly admonish him about the pitfalls of representing himself. In <em>Faretta v. California, </em><span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/" aria-description="Citation for case: Faretta v. California">422 U.S. 806</a></span>, <span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/" aria-description="Citation for case: Faretta v. California">95 S.Ct. 2525</a></span>, <span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/" aria-description="Citation for case: Faretta v. California">45 L.Ed.2d 562</a></span> (1975), the Supreme Court held that criminal defendants have a constitutional right to self-representation. But before permitting a defendant to exercise this right, the trial judge must ensure that the defendant has knowingly and voluntarily waived his Sixth Amendment right to counsel. To do this, the judge should advise the defendant about and try to ensure he understands the benefits associated with the right to counsel, the pitfalls of self-representation, and the fact that it is unwise for one not trained in the law to try to represent himself. See <em>United, States v. Moya-Gomez, </em><span class="citation" data-id="513458"><a href="/opinion/513458/united-states-v-rigoberto-moya-gomez-celestino-orlando-estevez-amado/#731" aria-description="Citation for case: United States v. Rigoberto Moya-Gomez Celestino Orlando...">860 F.2d 706, 731-32</a></span> (7th Cir.1988). In <em>United States v. Mitchell, </em><span class="citation" data-id="468796"><a href="/opinion/468796/united-states-v-ronald-mitchell/" aria-description="Citation for case: United States v. Ronald Mitchell">788 F.2d 1232</a></span>, 1236 n. 3 (7th Cir.1986), we stated that the district judge should engage in</p>
<blockquote id="Ausx">a thorough and extensive inquiry of [defendant] by asking [him] his age and degree of education; informing him of the crimes with which he was charged and the maximum possible sentences; determining that [he] understands] the nature of the charges; ascertaining that he ha[s] copies of the Federal Rules of Evidence and the Federal Rules of Civil Procedure and instructing him to read them and to abide by them, whether read or not; and telling [him] that he would be expected to conduct himself in accordance with those rules.</blockquote>
<p id="b1469-6">See also <em>Moya-Gomez, </em><span class="citation" data-id="513458"><a href="/opinion/513458/united-states-v-rigoberto-moya-gomez-celestino-orlando-estevez-amado/#732" aria-description="Citation for case: United States v. Rigoberto Moya-Gomez Celestino Orlando...">860 F.2d at 732</a></span>. An excellent guideline for the appropriate inquiry a district judge should conduct when a defendant announces he wants to represent himself, and a guideline consistent with our pronouncements in <em><span class="citation" data-id="468796"><a href="/opinion/468796/united-states-v-ronald-mitchell/" aria-description="Citation for case: United States v. Ronald Mitchell">Mitchell</a></span> </em>and <em><span class="citation" data-id="513458"><a href="/opinion/513458/united-states-v-rigoberto-moya-gomez-celestino-orlando-estevez-amado/" aria-description="Citation for case: United States v. Rigoberto Moya-Gomez Celestino Orlando...">Moya-Gomez</a></span>, </em>is contained in 1 <em>Bench Book for United States District Judges </em>§ 1.02 (3d ed.1986), which is reproduced as an appendix to the opinion in <em>United States v. McDowell, </em><span class="citation" data-id="484975"><a href="/opinion/484975/united-states-v-william-stewart-mcdowell/#251" aria-description="Citation for case: United States v. William Stewart McDowell">814 F.2d 245, 251-52</a></span> (6th Cir.1987).</p>
<p id="b1469-8">It is important that district judges conduct a proper inquiry of and convey the necessary information to a defendant who wishes to represent himself. When the Supreme Court in <em><span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/" aria-description="Citation for case: Faretta v. California">Faretta</a></span> </em>announced the right to self-representation it placed trial judges between a rock and hard place. Whether the district court honors or denies the defendant’s request to represent himself, the defendant is likely to appeal if he loses at trial. The appeal will almost inevitably revolve around whether or not the defendant was fully aware of his right to counsel, the benefits he receives because of that right, and the pitfalls of going alone. By conducting a formal inquiry such as the one set out in the District Judge’s Bench Book, the judge will insulate the judgment from this type of attack. The trial judge is in the best position to assess whether a defendant has knowingly and voluntarily waived counsel. This court will most likely uphold the trial judge’s decision to honor or deny the defendant’s request to represent himself where the judge has made the proper inquiries and conveyed the proper information, and reaches a reasoned conclusion about the defendant’s understanding of his rights and the voluntariness of his decision. We realize that such inquiries take time. But the few minutes a proper <em><span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/" aria-description="Citation for case: Faretta v. California">Faretta</a></span> </em>inquiry normally would take is a worthwhile alternative to a new trial.</p>
<p id="b1469-9">It is clear the district judge in this case did not conduct a proper inquiry concerning Berkowitz’s waiver of counsel. The judge did not inform Berkowitz of the benefits of having counsel or the pitfalls of representing himself. While the judge did recite to Berkowitz the old saw that “a lawyer [who] represents himself ... has a fool for a client,” this hardly constitutes the kind of <page-number citation-index="1" label="1384">*1384</page-number>searching inquiry we spoke of in <em><span class="citation" data-id="468796"><a href="/opinion/468796/united-states-v-ronald-mitchell/" aria-description="Citation for case: United States v. Ronald Mitchell">Mitchell</a></span> </em>and <em><span class="citation" data-id="513458"><a href="/opinion/513458/united-states-v-rigoberto-moya-gomez-celestino-orlando-estevez-amado/" aria-description="Citation for case: United States v. Rigoberto Moya-Gomez Celestino Orlando...">Moya-Gomez</a></span>. </em>But on appeal Berkow-itz makes little of this shortcoming. He raised the <em><span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/" aria-description="Citation for case: Faretta v. California">Faretta</a></span> </em>issue as almost an afterthought, devoting only one sentence in his brief to this issue, not even attempting to explain what a proper inquiry should entail, and citing no pertinent authority to support his “argument.” His nonchalant treatment of the omission on appeal leads us to conclude he considers the inquiry of little consequence. We repeatedly have made clear that perfunctory and undeveloped arguments, and arguments that are unsupported by pertinent authority, are waived (even where those arguments raise constitutional issues). See, e.g., <em>United States v. Brown, </em><span class="citation" data-id="538873"><a href="/opinion/538873/united-states-v-winford-earl-brown/" aria-description="Citation for case: United States v. Winford Earl Brown">899 F.2d 677</a></span>, 679 n. 1 (7th Cir.1990); <em>United States v. Petitjean, </em><span class="citation no-link">888 F.2d 1341</span>, 1349 (7th Cir.1989); <em>United States v. Williams, </em><span class="citation" data-id="525016"><a href="/opinion/525016/united-states-v-frank-james-williams-and-tedric-beverly/#518" aria-description="Citation for case: United States v. Frank James Williams and Tedric Beverly">877 F.2d 516, 518-19</a></span> (7th Cir.1989); Fed.R.App.P. 28(a)(4).</p>
<p id="b1470-4">Given the complete lack of inquiry by the district judge, we might be willing to forgive Berkowitz’s waiver but for one point: a failure to make a proper inquiry of a defendant who asks to represent himself, by itself, is not necessarily reversible error. The real question when a criminal defendant waives counsel is not the quality of the trial judge’s inquiry; rather, it is whether the defendant knowingly and voluntarily waived his right to counsel. Thus, if a formal inquiry is deficient, or even lacking, we will not reverse the defendant’s conviction if the record as a whole demonstrates the defendant knowingly and voluntarily waived his right to counsel. See <em>Moya-Gomez, </em><span class="citation" data-id="513458"><a href="/opinion/513458/united-states-v-rigoberto-moya-gomez-celestino-orlando-estevez-amado/" aria-description="Citation for case: United States v. Rigoberto Moya-Gomez Celestino Orlando...">860 F.2d at 733</a></span> (citing cases).</p>
<p id="b1470-5">Berkowitz did not argue in his opening brief how the record as a whole does not show that his waiver of counsel was not knowing and voluntary. In fact, he did not mention this necessary analysis of the record or even assert that his waiver was <em>not </em>knowing and voluntary. He cited no pertinent authority on the point. The government in its response brief thoroughly analyzed the record to attempt to demonstrate that Berkowitz’s waiver of counsel was knowing and voluntary, and cited authority to support its legal analysis. Despite the government’s argument, Berkow-itz ignored the waiver of counsel issue in his reply brief and at oral argument, making no attempt to refute the government’s analysis either legally or factually.</p>
<p id="b1470-7">A party urging us to reverse a district court’s judgment has an obligation to argue why we should reverse that judgment, and to cite appropriate authority to support that argument. See <em>Brown, </em><span class="citation" data-id="538873"><a href="/opinion/538873/united-states-v-winford-earl-brown/" aria-description="Citation for case: United States v. Winford Earl Brown">899 F.2d at 679</a></span> n. 1; see also <em>Beard v. Whitley County REMC, </em><span class="citation" data-id="8958168"><a href="/opinion/8966810/beard-v-whitley-county-remc/#408" aria-description="Citation for case: Beard v. Whitley County REMC">840 F.2d 405, 408-09</a></span> (7th Cir.1988). “The premise of our adversarial system is that appellate courts do not sit as self-directed boards of legal inquiry and research, but essentially as arbiters of legal questions presented and argued by the parties before them.” <em>Carducci v. Regan, </em><span class="citation" data-id="423490"><a href="/opinion/423490/louis-a-carducci-v-donald-t-regan-secretary-us-treasury-department/#177" aria-description="Citation for case: Louis A. Carducci v. Donald T. Regan, Secretary, U.S....">714 F.2d 171, 177</a></span> (D.C.Cir.1983) (Scalia, J.). It is not this court’s responsibility to research and construct the parties’ arguments. <em>Williams, </em><span class="citation" data-id="525016"><a href="/opinion/525016/united-states-v-frank-james-williams-and-tedric-beverly/#518" aria-description="Citation for case: United States v. Frank James Williams and Tedric Beverly">877 F.2d at 518</a></span>; <em>Beard, </em><span class="citation" data-id="8958168"><a href="/opinion/8966810/beard-v-whitley-county-remc/#408" aria-description="Citation for case: Beard v. Whitley County REMC">840 F.2d at 408-09</a></span>. Since Berkowitz has chosen not to argue that his waiver of counsel was not knowing and voluntary, even despite the government’s argument that it was, he has waived the issue.</p>
<p id="b1470-8">In any event, there are several indications in the record that Berkowitz knowingly and voluntarily waived his right to counsel. Berkowitz is a college graduate. He knew he had the right to be represented by counsel, and affirmatively asked to represent himself. He understood the distinction between having counsel and being represented by counsel; while he asked to conduct the trial himself, he insisted that Huyck stay in the case as standby counsel. Not only did Berkowitz actively participate in the discovery process of the tax fraud case, but he also had represented himself in a prior civil action, so he had prior experience with judicial procedures. Moreover, Berkowitz’s trial conduct demonstrated a fairly sophisticated understanding of the judicial process. Berkowitz made several evidentiary objections that the district court sustained. He also was able to cross-examine the government’s witnesses on the subtleties of the best evidence rule, Northern District of Illinois Local Rule 2.04, Fed. R.Crim.P. 16, and the Jencks Act. While <page-number citation-index="1" label="1385">*1385</page-number>the district judge should have conducted a much more searching inquiry concerning Berkowitz’s waiver of counsel, the facts we have noted are enough to demonstrate that Berkowitz’s waiver was knowing and voluntary, at least absent any assertion by Berkowitz otherwise.</p>
<p id="b1471-4">III. Arrest and Search</p>
<p id="b1471-5">Berkowitz next asserts that the district court should have suppressed the evidence found in his home during his warrantless arrest and during the searches of his home the following day. (According to Berkow-itz, information derived from the documents seized at the time of arrest was used in the affidavit Shearer submitted to obtain a search warrant; the government does not — at least now — contest this assertion.). Berkowitz posits three reasons why the district judge should have suppressed this evidence. First, Berkowitz argues that Shearer and other IRS agents illegally arrested him in his home without a warrant. Second, Berkowitz argues that even if the arrest was lawful, IRS agents had no right to follow him into his office, where they found the documents. Finally, Ber-kowitz argues that even if the agents had a right to be in his office, the documents Shearer seized were not seizable under the plain view exception to the warrant requirement because it was not readily apparent that those documents were among the ones Berkowitz stole.</p>
<p id="b1471-6">
<em>A. Arrest at Berkowitz’s Home.</em>
</p>
<p id="b1471-7">The district judge denied the suppression motion without holding an evidentiary hearing because he found that Berkowitz had “failed to identify any factual dispute relevant to the disposition of the motion.” But there was, as we have seen, a factual dispute concerning Berkowitz's arrest. The government claimed (supported by an affidavit by Shearer) that the IRS agents asserted their authority to arrest before entering Berkowitz’s home, and that Berkowitz did not resist their authority; only after this did the agents enter the home to complete the arrest. On the other hand, Berkowitz claimed (supported by his own affidavit) that Shearer and the other IRS agents entered his home before informing him he was under arrest.</p>
<p id="b1471-9">Despite this factual conflict, the district court was obliged to hold a hearing only if the difference in facts is material, that is, only if the disputed fact makes a difference in the outcome. See <em>United States v. Rollins, </em><span class="citation" data-id="515491"><a href="/opinion/515491/united-states-v-kelly-rollins-and-dan-slaughter/#1291" aria-description="Citation for case: United States v. Kelly Rollins and Dan Slaughter">862 F.2d 1282, 1291</a></span> (7th Cir.1988); <em>Nechy v. United States, </em><span class="citation" data-id="8914356"><a href="/opinion/8924920/nechy-v-united-states/#776" aria-description="Citation for case: Nechy v. United States">665 F.2d 775, 776</a></span> (7th Cir.1981); see also <em>United States v. Sophie, </em><span class="citation" data-id="539884"><a href="/opinion/539884/united-states-v-scott-sophie/#1071" aria-description="Citation for case: United States v. Scott Sophie">900 F.2d 1064, 1071-72</a></span> (7th Cir.1990). Whether the factual conflict here is material depends on whether the arrest’s legality differs under the different versions of facts. If the arrest was legal under either version of the facts, we must affirm the district court; if the arrest was illegal under either version of the facts, we must reverse. Only if the arrest was legal under the government’s facts but illegal under Berkowitz’s must we remand for an eviden-tiary hearing.</p>
<p id="b1471-10">Generally, police may not enter a person’s home to arrest that person without an arrest warrant, unless exigent circumstances exist. <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980); see also <em>Minnesota v. Olson, </em>— U.S. -, <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/#1687" aria-description="Citation for case: Minnesota v. Olson">110 S.Ct. 1684, 1687</a></span>, <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">109 L.Ed.2d 85</a></span> (1990); <em>Welsh v. Wisconsin, </em><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U.S. 740</a></span>, <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">104 S.Ct. 2091</a></span>, <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">80 L.Ed.2d 732</a></span> (1984). The Fourth Amendment protects a person’s reasonable expectation of privacy in a variety of settings, but the chief evil against which the amendment is directed is the physical entry of the home. See <em>Payton, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U.S. at 585, 589</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1379" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1379, 1381</a></span>. “In [no setting] is the zone of privacy more clearly defined than when bounded by the unambiguous physical dimensions of an individual’s home.... ” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York"><em>Id. </em>at 589</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1381" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1381</a></span>. Thus, the Court held in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>the Fourth Amendment draws “a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York"><em>Id. </em>at 590</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1382" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1382</a></span>.</p>
<p id="b1471-13">A few years before deciding <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>however, the Supreme Court had held in <em>United States v. Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U.S. 38</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">96 S.Ct. 2406</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">49 L.Ed.2d 300</a></span> (1976), that po<page-number citation-index="1" label="1386">*1386</page-number>lice could arrest without a warrant a person standing in the open doorway to her home because the open doorway was a public place. In <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span>, </em>police saw “Mom” Santana standing in the open doorway to her home shortly after a heroin transaction they had probable cause to believe she participated in. The police pulled their van up near her home, exited the van, identified themselves, and approached Santana to arrest her. Santana fled into her home; the police followed and arrested her. <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#40" aria-description="Citation for case: United States v. Santana"><em>Id. </em>at 40-41</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#2408" aria-description="Citation for case: United States v. Santana">96 S.Ct. at 2408-09</a></span>.</p>
<p id="b1472-4">The Supreme Court upheld Santana’s arrest. First, the Court held Santana had no reasonable expectation of privacy standing in her open doorway: “She was not merely visible to the public but was as exposed to public view, speech, hearing, and touch as if she had been standing completely outside her house.” <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana"><em>Id. </em>at 42</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#2409" aria-description="Citation for case: United States v. Santana">96 S.Ct. at 2409</a></span>. Thus, the police could arrest Santana in her doorway under the Court’s decision in <em>United States v. Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U.S. 411</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">96 S.Ct. 820</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">46 L.Ed.2d 598</a></span> (1976), that police with probable cause to arrest may arrest a person in a public place without a warrant.</p>
<p id="b1472-5">The police, however, were not actually able to complete Santana’s arrest in her doorway; they had to enter her home to bring her under their control. The Court upheld the arrest in the home, not because the home was a public place, but because Santana could not thwart an arrest begun in a public place (her open doorway) by retreating into her house. <em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Id.</a></span> </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U.S. at 42-43</a></span>, 96 S.Ct. at 2409-10. The entry into Santana’s home was justified by an exigent circumstance: the police’s “hot pursuit” of a fleeing felon. See <em>id.</em></p>
<p id="b1472-6">If Berkowitz’s arrest occurred as the government says it did, the arrest was legal. Courts have generally upheld arrests such as that described by Shearer in this case, where the police go to a person’s home without a warrant, knock on the door, announce from outside the home the person is under arrest when he opens the door to answer, and the person acquiesces to the arrest. See, e.g., <em>McKinney v. George, </em><span class="citation" data-id="430916"><a href="/opinion/430916/raymond-lee-mckinney-v-velma-george/#1188" aria-description="Citation for case: Raymond Lee McKinney v. Velma George">726 F.2d 1183, 1188</a></span> (7th Cir.1984); <em>United States v. Carrion, </em><span class="citation" data-id="482020"><a href="/opinion/482020/united-states-v-anthony-nicholas-carrion-and-fred-solmor/#1128" aria-description="Citation for case: United States v. Anthony Nicholas Carrion and Fred Solmor">809 F.2d 1120, 1128</a></span> (5th Cir.1987); <em>United States v. Whitten, </em><span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/#1015" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">706 F.2d 1000, 1015</a></span> (9th Cir.1983); <em>United States v. Botero, </em><span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/" aria-description="Citation for case: United States v. Diego Botero, United States of America...">589 F.2d 430</a></span> (9th Cir.1978); see generally 2 Wayne R. La Fave, <em>Search and Seizure </em>§ 6.1(e), at 589-61 (2d ed. 1987). While most of these cases have justified their holdings as applications of <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span>, </em>the arrests in these cases, and the arrest here as Shearer presents it, are consistent with <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>It is true that Berkowitz was still standing inside his home when Shearer told him he was under arrest. But <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>prohibits only a war-rantless <em>entry </em>into the home, not a policeman’s use of his voice to convey a message of arrest from outside the home. See La Fave, <em>supra, </em>§ 6.1(e) at 590. Moreover, there is nothing in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>that prohibits a person from surrendering to police at his doorway. <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Id.</a></span> </em>The agents in this case (even as Shearer tells it) did enter Berkow-itz’s house (remaining immediately adjacent to his doorway) after Shearer told Berkow-itz he was under arrest. But from Shearer’s affidavit, it appears Berkowitz submitted to the agents’ authority to arrest him before they entered. For reasons we will explain shortly, we do not think the agents’ entry (if the facts are as Shearer states) violated any reasonable privacy expectation of Berkowitz’s, and therefore did not violate <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>.</em></p>
<p id="b1472-8">As Berkowitz presents the arrest, however, Shearer and the other IRS agents entered his home <em>before </em>announcing he was under arrest. One might argue that this should not make a difference; Berkowitz was standing at or near his doorway, and <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span> </em>says the doorway is a public place. Moreover, one might argue that a search’s legality should not turn on such subtle distinctions as whether the police announce an arrest before entering a home, or wait until after entry to announce the arrest (so long as the police stay near the doorway). We find these arguments unpersuasive for several reasons.</p>
<p id="b1472-9"><em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>holds the Fourth Amendment draws a clear line at the entrance of a person’s house: “Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U.S. at 590</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1382" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1382</a></span>. Entering a person’s <page-number citation-index="1" label="1387">*1387</page-number>home without a warrant to arrest him, where no exigent circumstances exist, violates this clear command. The government has not cited any “knock and arrest” cases upholding arrests where the police entered the arrestee’s home before telling the person he was under arrest. The Fourth Circuit has recently held that a warrantless nonconsenual entry into a hotel room to arrest a subject who answered a knock at his door and was standing near the door when the police entered violates <em>Payton. United States v. McCraw, </em><span class="citation" data-id="9481089"><a href="/opinion/552357/united-states-v-david-mccraw-united-states-of-america-v-james-mathis/#228" aria-description="Citation for case: United States v. David McCraw United States of America v....">920 F.2d 224, 228-30</a></span> (4th Cir.1990). A case from this circuit also indicates that such an arrest would be illegal. In <em>United States v. Diaz, </em><span class="citation" data-id="485008"><a href="/opinion/485008/united-states-v-manuel-nicholas-diaz/" aria-description="Citation for case: United States v. Manuel Nicholas Diaz">814 F.2d 454</a></span> (7th Cir.1987), an undercover officer was in Diaz’s hotel room testing cocaine he was supposed to buy from Diaz. The officer told Diaz the cocaine was acceptable, and left the room purportedly to call his “money man.” After leaving the room, the officer gave a signal to other officers stationed near the room. The first officer then went back to the room, and knocked on the door. When Diaz answered, the other officers entered the room and arrested him. See <span class="citation" data-id="485008"><a href="/opinion/485008/united-states-v-manuel-nicholas-diaz/#456" aria-description="Citation for case: United States v. Manuel Nicholas Diaz"><em>id. </em>at 456</a></span>. This court upheld the search on the basis of Diaz’s original consent to the first officer to be in the hotel room. But although Diaz was at the doorway to his hotel room when the other officers entered and arrested, we held there were no exigent circumstances to justify the entry, thus indicating that absent Diaz’s consent to the first officer the warrantless entry to arrest Diaz would have violated the Fourth Amendment as interpreted in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>See <em>id. </em>at 458-59.</p>
<p id="b1473-4">That warrantless entry before arrest is not legal (and, conversely, that a slight entry after the defendant has submitted to the police is legal) can be seen from analyzing the privacy interests involved in the situation. The Fourth Amendment protects people’s legitimate expectations of privacy. A person’s subjective privacy expectation in any situation is legitimate, and therefore worthy of Fourth Amendment protection, if it is “one that society is prepared to recognize as reasonable.” <em>Minnesota v. Olson, </em><span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/#1687" aria-description="Citation for case: Minnesota v. Olson">110 S.Ct. at 1687</a></span> (citation omitted).</p>
<p id="b1473-5">As the Court noted in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>there is no place where a person’s expectation of privacy is greater than in his own home. See <em>Payton, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U.S. at 589</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1381" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1381</a></span>. A person does not abandon this privacy interest in his home by opening his door from within to answer a knock. Answering a knock at the door is not an invitation to come in the house. We think society would recognize a person’s right to choose to close his door on and exclude people he does not want within his home. This right to exclude is one of the most — if not the most — important components of a person’s privacy expectation in his home.</p>
<p id="b1473-6">When the police assert from outside the home their authority to arrest a person, they have not breached the person's privacy interest in the home. If the person recognizes and submits to that authority, the arrestee, in effect, has forfeited the privacy of his home to a certain extent. At that point, it is not unreasonable for the police to enter the home to the extent necessary to complete the arrest. A person who has submitted to the police’s authority and stands waiting for the police to take him away can hardly complain when the police enter his home briefly to complete the arrest. This is why, if Shearer’s version of the arrest is true, it would not have violated the Fourth Amendment for Shearer and the other agents to enter Berkow-itz’s house after announcing the arrest, and remain near his door, to take Berkowitz under their control.</p>
<p id="b1473-7">It is a different matter, however, for the police to enter a person’s home, without his consent, before announcing their authority to arrest. In that case, the arrestee has not forfeited his privacy interest in the home; he has not relinquished his right to close the door on the unwanted visitors. See <em>McCraw, </em><span class="citation" data-id="9481089"><a href="/opinion/552357/united-states-v-david-mccraw-united-states-of-america-v-james-mathis/#229" aria-description="Citation for case: United States v. David McCraw United States of America v....">920 F.2d at 229</a></span>; see also <em>McKinney v. George, </em><span class="citation" data-id="430916"><a href="/opinion/430916/raymond-lee-mckinney-v-velma-george/#1188" aria-description="Citation for case: Raymond Lee McKinney v. Velma George">726 F.2d at 1188</a></span> (suggesting that a person answering the police’s knock may retreat into his home, and that police may not then enter without a warrant to arrest him); <em>La Fave, supra, </em>§ 6.1(e) at 591. Indeed, the police have not even given him a chance to exercise that right. <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>holds that police may not <page-number citation-index="1" label="1388">*1388</page-number>enter a person’s home without a warrant to arrest him; to hold it was proper for Shearer and his cohorts to enter Berkowitz’s home in this case before announcing his arrest would be to sanction the very conduct that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>holds the Fourth Amendment forbids.</p>
<p id="b1474-3"><em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span> </em>does not require a different result. As far as reasonable privacy expectations go, there is a significant difference between a person who for no reason voluntarily decides to stand in his open doorway, and a person who merely answers a knock on his door. The person who answers the knock and stays within the house is not voluntarily exposing himself "to public view, speech, hearing, and touch as if [he is] standing completely outside [his] house.” <em>Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U.S. at 42</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#2409" aria-description="Citation for case: United States v. Santana">96 S.Ct. at 2409</a></span>. Moreover, the entry in <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span> </em>was justified by hot pursuit; Santana had just completed a heroin transaction, she voluntarily relinquished her privacy expectation in her home by exposing herself to the public in her open doorway, the police began the arrest while Santana had no reasonable privacy expectation, and there was a real possibility that delaying her arrest would result in her destroying evidence. See <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana"><em>id. </em>at 42-43</a></span>, 96 S.Ct. at 2409-10. In this case, there was no justification for Shearer and the other agents to enter Berkowitz’s home to arrest him without a warrant.</p>
<p id="b1474-4">One might argue that to disallow the minimal entry into the home to arrest in this case could hamstring police. But <em>Pay-ton </em>forbids any non-consensual warrantless entry into the home absent exigent circumstances. <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>did not draw the line one or two feet into the home; it drew the line at the home’s entrance. Also, if police go to a person’s home to arrest him, and have reason to believe they may have to enter the home to make the arrest, they should obtain a warrant. There was no reason in this case for Shearer and his cohorts not to get a warrant, and plenty of reason to obtain a warrant. What would have happened if Berkowitz had refused to open his door to the police? Or if another member of Berkowitz’s family had answered the door, but Berkowitz refused to come to the door? The agents would have had to go back and get a warrant (after having effectively warned Berkowitz that they suspected him of stealing documents, something that would have created a real danger that Berkowitz would destroy evidence or try to flee). Obtaining a warrant in the first place would have prevented these potential problems, to say nothing of the time it would have saved at trial and on appeal litigating the legality of Berkowitz’s arrest.</p>
<p id="b1474-6">Because there is a factual dispute in this case, and because resolving that dispute is necessary to determine whether Berkow-itz’s arrest was legal, the district judge should have held an evidentiary hearing. Therefore, we must reverse and remand so that the judge may hold that hearing.</p>
<p id="b1474-7">
<em>B. Plain View Seizure of Documents.</em>
</p>
<p id="b1474-8">There are two other questions we must answer concerning Berkowitz’s motion to suppress, assuming that if on remand the court determines Berkowitz’s arrest was legal. Both center around whether Shearer legally seized documents from Berkowitz’s home office at the time of his arrest. Since Shearer did not have a warrant to seize those documents, the seizure was proper only under the plain view exception to the warrant requirement. A warrantless seizure is justified under the plain view doctrine if the officer has a legal right to be in the place from where he sees the object subject to seizure and “a lawful right of access to the object itself,” and if “ ‘the object’s incriminating nature is immediately apparent.’ ” <em>Horton v. California, </em>— U.S. -, <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#2308" aria-description="Citation for case: Horton v. California">110 S.Ct. 2301, 2308</a></span>, <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/" aria-description="Citation for case: Horton v. California">110 L.Ed.2d 112</a></span> (1990). The two questions we must answer (assuming the arrest to be legal) are whether Shearer had a right to be in Berkowitz’s office when he discovered the documents, and whether it was “immediately apparent” to Shearer that those were government documents. (There is no dispute, assuming Shearer’s presence in the office was legal, about whether Shearer had a lawful right of access to the documents he seized, since they were lying in the open in a place he had a right to be.)</p>
<p id="b1475-3"><page-number citation-index="1" label="1389">*1389</page-number>There is no material factual dispute about Shearer’s presence in Berkowitz’s office. Both parties agree that Berkowitz told the agents that he wanted to get his keys, and that Shearer followed Berkowitz into his office where his keys were. While the government asserts that Berkowitz consented to being followed and Berkowitz asserts he did not consent, this factual dispute is unimportant. In <em>Washington v. Chrisman, </em><span class="citation" data-id="9428641"><a href="/opinion/110636/washington-v-chrisman/" aria-description="Citation for case: Washington v. Chrisman">455 U.S. 1</a></span>, <span class="citation" data-id="9428641"><a href="/opinion/110636/washington-v-chrisman/" aria-description="Citation for case: Washington v. Chrisman">102 S.Ct. 812</a></span>, <span class="citation" data-id="9428641"><a href="/opinion/110636/washington-v-chrisman/" aria-description="Citation for case: Washington v. Chrisman">70 L.Ed.2d 778</a></span> (1982), the Supreme Court held that when police lawfully arrest a person, they may follow that person into his home to monitor him, and seize any contraband they find in plain view. That is exactly what occurred here. The officer’s authority to monitor a suspect does not depend on the suspect’s consent; a suspect under arrest has no right to wander off on his own. Thus, the district court correctly held that Shearer could legally follow Berkowitz into his office.</p>
<p id="b1475-4">The second requirement, that an object’s incriminating nature be “immediately apparent,” is met where a police officer, upon seeing the object, has probable cause to believe the object is contraband or evidence of a crime. <em>Arizona v. Hicks, </em><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#327" aria-description="Citation for case: Arizona v. Hicks">480 U.S. 321, 327</a></span>, <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#1153" aria-description="Citation for case: Arizona v. Hicks">107 S.Ct. 1149, 1153</a></span>, <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/" aria-description="Citation for case: Arizona v. Hicks">94 L.Ed.2d 347</a></span> (1987). In this case, Shearer stated in his affidavit he observed “numerous files” on top of the desk in Berkowitz’s office and under the desk’s alcove area. Shearer stated that he “immediately recognized” the files as those that had been stored in the USA’s office. He knew the files were from the USA’s office because, among other things, he recognized his own handwriting on some of the files. Shearer also stated that he saw some original income tax returns.</p>
<p id="b1475-5">Shearer’s affidavit is sufficient to show that it was “immediately apparent” to him the files he saw in and seized from Berkow-itz’s office were taken from the USA’s office. Berkowitz, however, disputes several of the facts in Shearer’s affidavit. The question, therefore, is whether these disputed facts are material, so that the district court should have taken evidence concerning the seizure.</p>
<p id="b1475-11">None of the factual disputes concerning the documents’ seizure is material. Ber-kowitz states that it would not have been immediately apparent from looking at any files on his desk that they were government files. However, Berkowitz cannot contest what would have been apparent to Shearer (who was the agent responsible for investigating the tax fraud case) just by baldly asserting what he thinks would have been apparent.</p>
<p id="b1475-12">Berkowitz also stated that there were no papers in the alcove area under his desk. But Shearer stated he saw files in the alcove area, not papers. In any event, even if Shearer was mistaken about seeing files in the alcove area, the fact remains that Shearer did seize files from Berkow-itz’s office that were in plain view. Any dispute about precisely where Shearer actually found the files is not relevant to the question of whether it was immediately apparent to Shearer that the files he did find were government files.</p>
<p id="b1475-13">Finally, Berkowitz stated that there were no original tax returns on top of his desk. However, Berkowitz does not contest that Shearer actually seized original tax returns. Even if those tax returns were in the files, they were seizable because the files themselves were seizable. Berkowitz does not dispute that Shearer’s handwriting was on the files, or that there were other reasons for him to recognize the files. Thus, the fact that there may have been no original tax returns on top of the desk is not material to whether Shearer legally seized the documents he found in plain view in Berkowitz’s office. Since there is no material factual dispute concerning Shearer’s seizure of documents at the time of the arrest, if Berkowitz’s arrest was legal, the seizure of the documents was legal.<footnotemark>1</footnotemark></p>
<p id="b1476-2"><page-number citation-index="1" label="1390">*1390</page-number>IV. Sentencing</p>
<p id="b1476-3">
<em>A. Offense Level Increase for Destroying Documents.</em>
</p>
<p id="b1476-4">Since Berkowitz’s conviction may still stand after the district court holds an evidentiary hearing concerning his arrest, we consider Berkowitz’s challenges to his sentence. Berkowitz first argues that the district court erred by increasing his offense level for the obstruction of justice counts eight levels because he destroyed documents. Sentencing Guideline § 2J1.2(b)(l) provides for an eight-level increase for obstruction of justice offenses “[i]f the defendant obstructed or attempted to obstruct justice by causing or threatening to cause physical injury to a person or property....” Berkowitz argues that § 2J1.2(b)(l)’s eight-level increase applies only when property damage is used to intimidate a witness or inflict emotional distress. That is not, however, what the guideline says, and there is nothing in the commentary to § 2J1.2 to support Berkow-itz's argument. Section 2J1.2(b)(l) provides for an eight-level increase where the offense involves property damage; since Berkowitz destroyed government documents, that increase applies here.</p>
<p id="b1476-7">
<em>B. Amount of Loss.</em>
</p>
<p id="b1476-8">Berkowitz next argues that the district court erred by increasing the offense level for his theft conviction by eight levels. Guideline § 2B1.1 provides a base offense level of four for theft, and then increases the offense level as the amount of loss from the theft rises. For losses between $100,001 and $200,000, § 2Bl.l(b)(l)(I) provides for an eight-level increase. Berkowitz argues that the government did not introduce sufficient evidence to support the district judge’s finding that the government’s loss from his theft amounted to more than $100,000.</p>
<p id="b1476-11">Section 2B1.1, Application Note 2, provides that “loss” ordinarily means the market value of the property stolen. However, “[wjhere the market value is difficult to ascertain or inadequate to measure harm to the victim, the court may measure loss in some other way, such as reasonable replacement cost to the victim.” <em>Id. </em>The government estimated that the replacement cost of the documents Berkowitz stole would be more than $100,000. The government based its estimate on the effort it would take to duplicate the missing documents, including the time at least a dozen banks would have to spend duplicating documents, and the time the government would have to spend reorganizing the documents, reinterviewing witnesses, obtaining new copies of documents the witnesses had previously supplied, and recopying stolen undercover tape recordings. Time is money, and the value of the labor involved in replacing the stolen documents is part of the cost of replacing them. Moreover, time a person spends doing one thing is time that person cannot spend doing something else; therefore, opportunity costs must also be factored into the cost of replacing the documents. “[LJoss need not be determined with precision, and may be inferred from any reasonably reliable information available_” Guideline § 2B1.1, Application Note 3. Given that Berkowitz produced no evidence to challenge the government’s assertions about replacing the documents, those assertions were sufficient to support the trial judge’s finding that the loss exceeded $100,000.</p>
<p id="b1476-15">Berkowitz also argues that the district court in determining the amount of loss should have considered the government’s failure to mitigate. This argument is mer-itless. Berkowitz’s crime is the same whether or not the government mitigated its loss, and the government’s lack of mitigation is irrelevant to Berkowitz’s culpability. Besides, Application Note 2 indicates that mitigation is not required. For example, the note provides that if a defendant steals a car, the loss refers to the value of the car even if the vehicle is recovered immediately. In that case, the victim’s true loss is the value of not having his car <page-number citation-index="1" label="1391">*1391</page-number>for a certain amount of time, and any other losses flowing from not having the car. In the case where the car is returned immediately, that loss is likely to be very small. Yet, loss is still measured by the car’s market value. Similarly, even though the government might have been able to mitigate its loss, the loss should still be measured by the value of the documents stolen — in this case, the documents’ replacement cost.</p>
<p id="b1477-4">
<em>C. Upward, Departure.</em>
</p>
<p id="b1477-5">Berkowitz next argues that the district court erred by departing upward from criminal history category I (the category based on Berkowitz’s prior criminal record) to category III. Guideline § 4A1.3 provides that “if the criminal history category does not adequately reflect the seriousness of the defendant’s past criminal conduct or the likelihood that the defendant will commit other crimes” the court may depart upward. As an example of the kind of information the judge may consider in deciding to depart upward, § 4A1.3(d) provides that the judge may consider “whether the defendant was pending trial ... on another charge at the time of the instant offense.” Section 4A1.3 then gives as an example of when a departure is warranted “the case of a defendant who ... committed the instant offense while on bail or pretrial release for another serious offense.”</p>
<p id="b1477-6">The district judge quite logically applied the straightforward language in § 4A1.3 and departed upward because “Berkowitz committed the instant offenses while serious tax fraud and mail fraud charges were pending against him, and after he had been released on bond.” But despite § 4A1.3’s straightforward language, Berkowitz argues that the departure was unwarranted because the tax fraud case and this case were so closely related that the fact he stole the documents while out on bond for the tax fraud case indicates nothing about his likelihood of committing future crimes. We disagree. Most criminal defendants do not try to impede their prosecutions by stealing and destroying government evidence. Perhaps they realize stealing and destroying evidence would be wrong. More likely they realize that attempts to impede the prosecution will only land them in bigger trouble than they are already in. But neither the fact that such action was wrong nor the fact that his attempt to impede the prosecution could have serious adverse consequences deterred Berkowitz from stealing and destroying government documents. Given this, it is reasonable to conclude that Berkowitz might be more likely than the average offender to resort to crime in the future if he thought it to be to his advantage.</p>
<p id="b1477-8">Berkowitz attempts to make two other arguments concerning the upward departure. First, he states that since <span class="citation no-link">18 U.S.C. § 3147</span> and Guideline § 2J1.7 “cover” the commission of offenses while on bond, the court may not properly depart under § 4A1.3. Second, he states that the district judge did not follow a proper procedure in deciding to depart to criminal history category III. Since his argument concerning <span class="citation no-link">18 U.S.C. § 3147</span> and Guideline § 2J1.7 is a perfunctory two-sentence argument that does not explain how those provisions “cover” this situation, and that cites no applicable authority, he has waived it. See <em>United States v. Petitjean, </em>883 F.2d at 1349. He has also waived his procedural argument because he raised it for the first time in his reply brief. See Fed.R.App.P. 28; Seventh Circuit Rule 28(f); <em>Reynolds v. East Dyer Development Co., </em><span class="citation" data-id="8972260"><a href="/opinion/8980399/reynolds-v-east-dyer-development-co/" aria-description="Citation for case: Reynolds v. East Dyer Development Co.">882 F.2d 1249</a></span>, 1253 n. 2 (7th Cir.1989).</p>
<p id="b1477-9">
<em>D. Failure to Depart Downward.</em>
</p>
<p id="b1477-10">Berkowitz finally argues that the district court should have departed downward from the otherwise applicable guideline range because of a psychiatrist’s testimony about Berkowitz’s mental state at the time of his offense. However, we have no jurisdiction to review a district court’s decision not to depart, <em>United States v. Franz, </em><span class="citation" data-id="529999"><a href="/opinion/529999/united-states-v-scott-franz/" aria-description="Citation for case: United States v. Scott Franz">886 F.2d 973</a></span> (7th Cir.1989), and thus may not consider this argument.</p>
<p id="b1477-11">V.</p>
<p id="b1477-12">To sum up: We reject Berkowitz’s claims that he received ineffective assistance of <page-number citation-index="1" label="1392">*1392</page-number>counsel at trial and that the trial judge deprived him of assistance of counsel. We also hold that Berkowitz’s sentence was proper. However, we reverse and remand this case to the district court to hold an evidentiary hearing concerning Berkowitz’s arrest. Circuit Rule 36 shall not apply on remand.</p>
<footnote label="1">
<p id="b1475-6">. If Berkowitz’s arrest was not legal, it follows that Shearer had no right to follow Berkowitz into his office, and we could not uphold the seizure of the documents on the basis that <em>Chris-man </em>allowed Shearer to be in the office where he saw the documents in plain view. However, nothing in this opinion prevents the government from arguing any other theory to uphold the <page-number citation-index="1" label="1390">*1390</page-number>seizure (e.g., inevitable discovery) if the district court finds Berkowitz’s arrest illegal. We express no view about whether any other theory the government might argue would be successful.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Biswell.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Biswell"
type: case
citation: "406 U.S. 311 (1972)"
parallel_cite: "92 S. Ct. 1593; 32 L. Ed. 2d 87"
neutral_cite: 1972 U.S. LEXIS 60
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-05-15
docket: 71-81
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1972-05-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Biswell
  varies_by_point: false
  scope_note: "Good law; foundational pervasively-regulated-industry case (with Colonnade), applied in Donovan v. Dewey and organized into the three-part test of New York v. Burger (1987)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108533/united-states-v-biswell/"
  cluster_id: 108533
  opinion_id: 108533
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Progeny (pervasively-regulated industry)"
related: ["[[Donovan v. Dewey]]", "[[Marshall v. Barlow's Inc.]]", "[[See v. City of Seattle]]"]
aliases: []
tags: ["case", "fourth-amendment", "administrative-search", "inspections", "pervasively-regulated", "firearms", "gun-control-act"]
holding: "A warrantless inspection of a federally licensed firearms dealer under the Gun Control Act is reasonable: dealing in firearms is a pervasively regulated business whose licensee accepts inspection as a condition, and unannounced warrantless inspection is essential to effective enforcement."
lake:
  record_id: United States v. Biswell
  status: verified
  projected_at: 2026-07-09
---

# United States v. Biswell

*406 U.S. 311 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A city policeman and a federal Treasury agent entered the gun shop of Biswell, a federally licensed firearms dealer, and — under § 923(g) of the Gun Control Act — inspected a locked storeroom, finding two sawed-off rifles he was not licensed to possess. Biswell was convicted of dealing in firearms without paying the special occupational tax. He moved to suppress, arguing the warrantless inspection violated the Fourth Amendment.

## Issue
Whether a warrantless inspection of a licensed firearms dealer's premises, as authorized by the Gun Control Act, is reasonable under the Fourth Amendment.

## Rule
Yes. Effective enforcement requires unannounced inspection: "if inspection is to be effective and serve as a credible deterrent, unannounced, even frequent, inspections are essential. In this context, the prerequisite of a warrant could easily frustrate inspection." — 406 U.S. at 316. ^pin-316a

The licensee's privacy expectation is reduced by his choice to enter the business: "When a dealer chooses to engage in this pervasively regulated business and to accept a federal license, he does so with the knowledge that his business records, firearms, and ammunition will be subject to effective inspection. … The dealer is not left to wonder about the purposes of the inspector or the limits of his task." — *Id.* at 316. ^pin-316b

"We have little difficulty in concluding that where, as here, regulatory inspections further urgent federal interest, and the possibilities of abuse and the threat to privacy are not of impressive dimensions, the inspection may proceed without a warrant where specifically authorized by statute." — [*Id.* at 317](https://www.courtlistener.com/opinion/108533/united-states-v-biswell/#:~:text=We%20have%20little%20difficulty%20in). ^pin-317

## Application
Federal firearms regulation is of "central importance to federal efforts to prevent violent crime," and inspection is "a crucial part of the regulatory scheme." Biswell, as a licensed dealer, was annually furnished with the rules defining his obligations and the inspector's authority, so the warrantless inspection threatened only limited, anticipated privacy intrusion while serving an urgent interest. The seizure of the sawed-off rifles was therefore reasonable.

## Conclusion
The warrantless inspection and seizure were reasonable under the Fourth Amendment; the Court of Appeals' contrary judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Biswell*, with *[[Colonnade Catering Corp. v. United States]]* (liquor), is a foundational pervasively-regulated-industry case; its reasoning was preserved in [[Marshall v. Barlow's Inc.]], applied to mines in [[Donovan v. Dewey]], and organized into the three-part test of *[[New York v. Burger]]* (1987). It remains good law.

## Appears on
- [[Special Needs and Administrative Searches]] — *Progeny (pervasively-regulated industry)*

## Sources
- *United States v. Biswell*, 406 U.S. 311 (1972) — https://www.courtlistener.com/opinion/108533/united-states-v-biswell/ — pinpoints: 316, 317.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1ce531034c6c6784", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "406 U.S. 311 (1972)", "court": "U.S. Supreme Court", "neutral_cite": "1972 U.S. LEXIS 60", "official_citation_present": true, "parallel_cite": "92 S. Ct. 1593; 32 L. Ed. 2d 87", "title": "United States v. Biswell", "year": "1972"}}
{"assertion_id": "09233654f30c9f13", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Progeny (pervasively-regulated industry)", "title": "United States v. Biswell"}}
{"assertion_id": "a337f8e42fa39111", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless inspection of a federally licensed firearms dealer under the Gun Control Act is reasonable: dealing in firearms is a pervasively regulated business whose licensee accepts inspection as a condition, and unannounced warrantless inspection is essential to effective enforcement.", "title": "United States v. Biswell"}}
{"assertion_id": "72081c1a63eb3fab", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1972-05-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Biswell", "field_i_validity": "good_law", "scope_note": "Good law; foundational pervasively-regulated-industry case (with Colonnade), applied in Donovan v. Dewey and organized into the three-part test of New York v. Burger (1987).", "title": "United States v. Biswell", "varies_by_point": "false"}}
{"assertion_id": "f2c1a29d9b5c9488", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Biswell"}}
```

### lake record — United States v. Biswell

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Biswell",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Biswell",
    "case_name_short": "Biswell",
    "case_name_full": "United States v. Biswell",
    "input_case_name": "United States v. Biswell",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-05-15",
    "year": 1972,
    "docket": "71-81",
    "cluster_id": 108533,
    "lead_opinion_id": 108533,
    "sibling_ids": [
      108533,
      9424870,
      9424871,
      9424872
    ],
    "absolute_url": "/opinion/108533/united-states-v-biswell/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "406 U.S. 311",
      "volume": "406",
      "reporter": "U.S.",
      "page": "311",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "92 S. Ct. 1593",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "1593",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 87",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "87",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 60",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "60",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "406 U.S. 311",
        "volume": "406",
        "reporter": "U.S.",
        "page": "311",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 1593",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "1593",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 87",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "87",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 60",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "60",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "406 U.S. 311",
    "official_selection": {
      "court_class": "scotus",
      "selected": "406 U.S. 311",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-316a",
      "page": null,
      "quote": "--- # United States v. Biswell *406 U.S. 311 (1972)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A city policeman and a federal Treasury agent entered the gun shop of Biswell, a federally licensed firearms dealer, and \u2014 under \u00a7 923(g) of the Gun Control Act \u2014 inspected a locked storeroom, finding two sawed-off rifles he was not licensed to possess. Biswell was convicted of dealing in firearms without paying the special occupational tax. He moved to suppress, arguing the warrantless inspection violated the Fourth Amendment. ## Issue Whether a warrantless inspection of a licensed firearms dealer's premises, as authorized by the Gun Control Act, is reasonable under the Fourth Amendment. ## Rule Yes. Effective enforcement requires unannounced inspection:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-316b",
      "page": null,
      "quote": "When a dealer chooses to engage in this pervasively regulated business and to accept a federal license, he does so with the knowledge that his business records, firearms, and ammunition will be subject to effective inspection. \u2026 The dealer is not left to wonder about the purposes of the inspector or the limits of his task.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-317",
      "page": null,
      "quote": "We have little difficulty in concluding that where, as here, regulatory inspections further urgent federal interest, and the possibilities of abuse and the threat to privacy are not of impressive dimensions, the inspection may proceed without a warrant where specifically authorized by statute.",
      "star_marker": "317",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10283,
      "fragment": "#:~:text=We%20have%20little%20difficulty%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1972-05-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Biswell",
    "varies_by_point": false,
    "scope_note": "Good law; foundational pervasively-regulated-industry case (with Colonnade), applied in Donovan v. Dewey and organized into the three-part test of New York v. Burger (1987).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Najar",
          "cluster_id": 167674,
          "cite": [
            "451 F.3d 710",
            "2006 U.S. App. LEXIS 15171",
            "2006 WL 1689231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 165906,
          "cite": [
            "408 F.3d 1313",
            "2005 U.S. App. LEXIS 9988",
            "2005 WL 1283833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Opinion No.",
          "cluster_id": 3262306,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Knox County Education Association v. Knox County Board of Education",
          "cluster_id": 758562,
          "cite": [
            "158 F.3d 361"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Norwood v. Bain",
          "cluster_id": 2966869,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Argent Chemical Laboratories, Inc.",
          "cluster_id": 7038653,
          "cite": [
            "93 F.3d 572",
            "96 Cal. Daily Op. Serv. 6117",
            "96 Daily Journal DAR 10005",
            "1996 U.S. App. LEXIS 20462",
            "1996 WL 465363"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Keta",
          "cluster_id": 6064779,
          "cite": [
            "165 A.D.2d 172",
            "567 N.Y.S.2d 738",
            "1991 N.Y. App. Div. LEXIS 2305"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Caruso v. Ward",
          "cluster_id": 6033327,
          "cite": [
            "131 A.D.2d 214",
            "520 N.Y.S.2d 551",
            "2 I.E.R. Cas. (BNA) 1057",
            "1987 N.Y. App. Div. LEXIS 49496",
            "44 Empl. Prac. Dec. (CCH) 37,504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ingersoll v. Palmer",
          "cluster_id": 2604190,
          "cite": [
            "743 P.2d 1299",
            "43 Cal. 3d 1321",
            "241 Cal. Rptr. 42",
            "1987 Cal. LEXIS 451"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brignoni-Ponce",
          "cluster_id": 109311,
          "cite": [
            "45 L. Ed. 2d 607",
            "95 S. Ct. 2574",
            "422 U.S. 873",
            "1975 U.S. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
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
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New Jersey v. T. L. O.",
          "cluster_id": 111301,
          "cite": [
            "83 L. Ed. 2d 720",
            "105 S. Ct. 733",
            "469 U.S. 325",
            "1985 U.S. LEXIS 41",
            "53 U.S.L.W. 4083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
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
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Wisconsin",
          "cluster_id": 111959,
          "cite": [
            "97 L. Ed. 2d 709",
            "107 S. Ct. 3164",
            "483 U.S. 868",
            "1987 U.S. LEXIS 2897",
            "55 U.S.L.W. 5156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ybarra v. Illinois",
          "cluster_id": 110158,
          "cite": [
            "62 L. Ed. 2d 238",
            "100 S. Ct. 338",
            "444 U.S. 85",
            "1979 U.S. LEXIS 151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
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
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Barlow's, Inc.",
          "cluster_id": 109866,
          "cite": [
            "56 L. Ed. 2d 305",
            "98 S. Ct. 1816",
            "436 U.S. 307",
            "1978 U.S. LEXIS 26",
            "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
            "6 OSHC (BNA) 1571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Almeida-Sanchez v. United States",
          "cluster_id": 108845,
          "cite": [
            "37 L. Ed. 2d 596",
            "93 S. Ct. 2535",
            "413 U.S. 266",
            "1973 U.S. LEXIS 44"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Krull",
          "cluster_id": 111835,
          "cite": [
            "94 L. Ed. 2d 364",
            "107 S. Ct. 1160",
            "480 U.S. 340",
            "1987 U.S. LEXIS 1061",
            "55 U.S.L.W. 4291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Burger",
          "cluster_id": 111927,
          "cite": [
            "96 L. Ed. 2d 601",
            "107 S. Ct. 2636",
            "482 U.S. 691",
            "1987 U.S. LEXIS 2725",
            "55 U.S.L.W. 4890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zurcher v. Stanford Daily",
          "cluster_id": 109876,
          "cite": [
            "56 L. Ed. 2d 525",
            "98 S. Ct. 1970",
            "436 U.S. 547",
            "1978 U.S. LEXIS 98"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donovan v. Dewey",
          "cluster_id": 110530,
          "cite": [
            "69 L. Ed. 2d 262",
            "101 S. Ct. 2534",
            "452 U.S. 594",
            "1980 U.S. LEXIS 58"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G. M. Leasing Corp. v. United States",
          "cluster_id": 109579,
          "cite": [
            "50 L. Ed. 2d 530",
            "97 S. Ct. 619",
            "429 U.S. 338",
            "1977 U.S. LEXIS 33",
            "39 A.F.T.R.2d (RIA) 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramsey",
          "cluster_id": 109675,
          "cite": [
            "52 L. Ed. 2d 617",
            "97 S. Ct. 1972",
            "431 U.S. 606",
            "1977 U.S. LEXIS 101"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
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
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California Bankers Assn. v. Shultz",
          "cluster_id": 109005,
          "cite": [
            "39 L. Ed. 2d 812",
            "94 S. Ct. 1494",
            "416 U.S. 21",
            "1974 U.S. LEXIS 34",
            "33 A.F.T.R.2d (RIA) 1041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ortiz",
          "cluster_id": 109312,
          "cite": [
            "45 L. Ed. 2d 623",
            "95 S. Ct. 2585",
            "422 U.S. 891",
            "1975 U.S. LEXIS 146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
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
        "journal_ref": "United States v. Biswell:lane2_top_cited"
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
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Clifford",
          "cluster_id": 111057,
          "cite": [
            "78 L. Ed. 2d 477",
            "104 S. Ct. 641",
            "464 U.S. 287",
            "1984 U.S. LEXIS 14",
            "52 U.S.L.W. 4056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Biswell:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108533 OR 9424870 OR 9424871 OR 9424872) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MzcwNjI0MDAwMDAmcz00ODEzNjQmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108533+OR+9424870+OR+9424871+OR+9424872%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108533 OR 9424870 OR 9424871 OR 9424872)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDkmcz0xOTc1NTMxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108533+OR+9424870+OR+9424871+OR+9424872%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108533 OR 9424870 OR 9424871 OR 9424872)",
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
    "complete_query": "cites:(108533 OR 9424870 OR 9424871 OR 9424872)",
    "indexed_citing_opinions": 639,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108533,
        "count": 582,
        "count_source": "search"
      },
      {
        "opinion_id": 9424870,
        "count": 75,
        "count_source": "search"
      },
      {
        "opinion_id": 9424871,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424872,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 945,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-biswell.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU5MDgyNjQmcz00NTEzNjkxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108533+OR+9424870+OR+9424871+OR+9424872%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108533,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108533,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108533,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108533,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108533,
        "cited_id": 296736,
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
    "date_created": "2026-07-05T22:39:04Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:39:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:39:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:45:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:39:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Biswell

```
<div>
<center><b><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U.S. 311</a></span> (1972)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
BISWELL.</h1></center>
<center>No. 71-81.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 28, 1972.</center>
<center>Decided May 15, 1972.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE TENTH CIRCUIT.
<p><i>R. Kent Greenawalt</i> argued the cause for the United States. On the brief were <i>Solicitor General Griswold, Assistant Attorney General Petersen, Jerome M. Feit, Beatrice Rosenberg,</i> and <i>Kirby W. Patterson.</i></p>
<p><i>Warren F. Reynolds</i> argued the cause and filed a brief for respondent.</p>
<p><i>John S. Edmunds</i> and <i>Melvin L. Wulf</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging affirmance.</p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>The Gun Control Act of 1968, <span class="citation no-link">82 Stat. 1213</span>, <span class="citation no-link">18 U. S. C. § 921</span> <i>et seq.,</i> authorizes official entry during business hours into "the premises (including places of storage) of any firearms or ammunition . . . dealer . . . for the purpose of inspecting or examining (1) any records or documents required to be kept . . . and (2) any firearms or ammunition kept or stored by such . . . dealer . . . at <span class="star-pagination">*312</span> such premises."<sup>[1]</sup> <span class="citation no-link">18 U. S. C. § 923</span> (g). Respondent, a pawn shop operator who was federally licensed to deal in sporting weapons, was visited one afternoon by a city policeman and a Federal Treasury agent who identified himself, inspected respondent's books, and requested entry into a locked gun storeroom. Respondent asked whether the agent had a search warrant, and the investigator told him that he did not, but that § 923 (g) authorized such inspections. Respondent was given a copy of the section to read and he replied, "Well, that's what it says so I guess it's okay." Respondent unlocked the storeroom, and the agent found and seized two sawed-off rifles which respondent was not licensed to possess. He was indicted and convicted for dealing in firearms without <span class="star-pagination">*313</span> having paid the required special occupational tax.<sup>[2]</sup> The Court of Appeals reversed, however, holding that § 923 (g) was unconstitutional under the Fourth Amendment because it authorized warrantless searches of business premises and that respondent's ostensible consent to the search was invalid under <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543</a></span> (1968). The Court of Appeals concluded that the sawed-off rifles, having been illegally seized, were inadmissible in evidence. <span class="citation" data-id="296736"><a href="/opinion/296736/united-states-v-loarn-anthony-biswell/" aria-description="Citation for case: United States v. Loarn Anthony Biswell">442 F. 2d 1189</a></span> (CA10 1971). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./404/983/">404 U. S. 983</a></span> (1971), and now reverse the judgment of the Court of Appeals.</p>
<p>As the Court of Appeals correctly recognized, we had no occasion in <i>See</i> v. <i>City of Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967), to consider the reach of the Fourth Amendment with respect to various federal regulatory statutes. In <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970), we dealt with the statutory authorization for warrantless inspections of federally licensed dealers in alcoholic beverages. There, federal inspectors, without a warrant <span class="star-pagination">*314</span> and without the owner's permission, had forcibly entered a locked storeroom and seized illegal liquor. Emphasizing the historically broad authority of the Government to regulate the liquor industry and the approval of similar inspection laws of this kind in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886),<sup>[3]</sup> we concluded that Congress had ample power "to design such powers of inspection under the liquor laws as it deems necessary to meet the evils at hand." <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#76" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 76</a></span>. We found, however, that Congress had not expressly provided for forcible entry in the absence of a warrant and had instead given Government agents a remedy by making it a criminal offense to refuse admission to the inspectors under <span class="citation no-link">26 U. S. C. § 7342</span>.</p>
<p>Here, the search was not accompanied by any unauthorized force, and if the target of the inspection had been a federally licensed liquor dealer, it is clear under <i>Colonnade</i> that the Fourth Amendment would not bar a seizure of illicit liquor. When the officers asked to inspect respondent's locked storeroom, they were merely asserting their statutory right, and respondent was on <span class="star-pagination">*315</span> notice as to their identity and the legal basis for their action. Respondent's submission to <i>lawful</i> authority and his decision to step aside and permit the inspection rather than face a criminal prosecution<sup>[4]</sup> is analogous to a house-holder's acquiescence in a search pursuant to a warrant when the alternative is a possible criminal prosecution for refusing entry or a forcible entry. In neither case does the lawfulness of the search depend on consent; in both, there is lawful authority independent of the will of the householder who might, other things being equal, prefer no search at all. In this context, <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543</a></span> (1968), is inapposite, since there the police relied on a warrant that was never shown to be valid; because their demand for entry was not pursuant to lawful authority, the acquiescence of the householder was held an involuntary consent. In the context of a regulatory inspection system of business premises that is carefully limited in time, place, and scope, the legality of the search depends not on consent but on the authority of a valid statute.</p>
<p>We think a like result is required in the present case, which involves a similar inspection system aimed at federally licensed dealers in firearms. Federal regulation of the interstate traffic in firearms is not as deeply rooted in history as is governmental control of the liquor industry, but close scrutiny of this traffic is undeniably of central importance to federal efforts to prevent violent crime and to assist the States in regulating the firearms traffic within their borders. See Congressional Findings and Declaration, Note preceding <span class="citation no-link">18 U. S. C. § 922</span>. Large interests are at stake, and inspection is a crucial part of the regulatory scheme, since it assures that weapons are distributed through regular channels and in <span class="star-pagination">*316</span> a traceable manner and makes possible the prevention of sales to undesirable customers and the detection of the origin of particular firearms.</p>
<p>It is also apparent that if the law is to be properly enforced and inspection made effective, inspections without warrant must be deemed reasonable official conduct under the Fourth Amendment. In <i>See</i> v. <i>City of Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967), the mission of the inspection system was to discover and correct violations of the building code, conditions that were relatively difficult to conceal or to correct in a short time. Periodic inspection sufficed, and inspection warrants could be required and privacy given a measure of protection with little if any threat to the effectiveness of the inspection system there at issue. We expressly refrained in that case from questioning a warrantless regulatory search such as that authorized by § 923 of the Gun Control Act. Here, if inspection is to be effective and serve as a credible deterrent, unannounced, even frequent, inspections are essential. In this context, the prerequisite of a warrant could easily frustrate inspection; and if the necessary flexibility as to time, scope, and frequency is to be preserved, the protections afforded by a warrant would be negligible.</p>
<p>It is also plain that inspections for compliance with the Gun Control Act pose only limited threats to the dealer's justifiable expectations of privacy. When a dealer chooses to engage in this pervasively regulated business and to accept a federal license, he does so with the knowledge that his business records, firearms, and ammunition will be subject to effective inspection. Each licensee is annually furnished with a revised compilation of ordinances that describe his obligations and define the inspector's authority. <span class="citation no-link">18 U. S. C. § 921</span> (a) (19). The dealer is not left to wonder about the purposes of the inspector or the limits of his task.</p>
<p><span class="star-pagination">*317</span> We have little difficulty in concluding that where, as here, regulatory inspections further urgent federal interest, and the possibilities of abuse and the threat to privacy are not of impressive dimensions, the inspection may proceed without a warrant where specifically authorized by statute. The seizure of respondent's sawed-off rifles was not unreasonable under the Fourth Amendment, and the judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring in the result.</p>
<p>Had I been a member of the Court when <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970), was decided, I would have joined the respective dissenting opinions of Mr. Justice Black and of THE CHIEF JUSTICE, <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 79</a></span> and 77. I therefore concur in the result here.</p>
<p>MR. JUSTICE DOUGLAS, dissenting.</p>
<p>As Mr. Justice Clark, writing for the three-judge panel in the Court of Appeals for the Tenth Circuit said, the Federal Gun Control Act, <span class="citation no-link">18 U. S. C. § 923</span> (g), has a provision for inspection that is "almost identical" with the one in <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span>.</p>
<p>The present one provides:</p>
<blockquote>"The Secretary may enter during business hours the premises (including places of storage) of any firearms or ammunition . . . dealer . . . for the purpose of inspecting or examining (1) any records or documents required to be kept . . . and (2) any firearms or ammunition kept or stored by such . . . dealer . . . ." <span class="citation no-link">18 U. S. C. § 923</span> (g).</blockquote>
<p><span class="star-pagination">*318</span> The one in <i>Colonnade</i> provided:</p>
<blockquote>"The Secretary or his delegate may enter during business hours the premises . . . of any dealer for the purpose of inspecting or examining any records or other documents required to be kept . . . under this chapter . . . ." <span class="citation no-link">26 U. S. C. § 5146</span> (b).</blockquote>
<p>The Court legitimates this inspection scheme because of its belief that, had respondent been a dealer in liquor instead of firearms, such a search as was here undertaken would have been valid under the principles of <i>Colonnade.</i> I respectfully disagree. <i>Colonnade,</i> of course, rested heavily on the unique historical origins of governmental regulation of liquor. And the Court admits that similar regulation of the firearms traffic "is not as deeply rooted in history as is governmental control of the liquor industry." Yet, assuming, <i>arguendo,</i> that the firearms industry is as appropriate a subject of pervasive governmental inspection as is the liquor industry, the Court errs.</p>
<p>In <i>Colonnade,</i> we agreed that "Congress has broad power to design such powers of inspection under the liquor laws as it deems necessary to meet the evils at hand." <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#76" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 76</a></span>. But we also said:</p>
<blockquote>"Where Congress has authorized inspection but made no rules governing the procedure that inspectors must follow, the Fourth Amendment and its various restrictive rules apply." <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#77" aria-description="Citation for case: Colonnade Catering Corp. v. United States"><i>Id.,</i> at 77</a></span>.</blockquote>
<p>Here, the statute authorizing inspection is virtually identical to the one we considered in <i>Colonnade.</i> The conclusion necessarily follows that Congress, as in <i>Colonnade,</i> has here "selected a standard that does not include forcible entries without a warrant." <i><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">Ibid.</a></span></i></p>
<p>In my view, a search conducted over the objection of the owner of the premises sought to be searched is "forcible," whether or not violent means are used to effect <span class="star-pagination">*319</span> the search. In this case, the owner withdrew his objection upon being shown a copy of the statute authorizing inspection, saying: "If that is the law, I guess it is all right." If we apply the test of "consent" that we used in <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543</a></span>, we would affirm this judgment,<sup>[*]</sup> for as MR. JUSTICE STEWART, speaking for the Court in <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span>,</i> said:</p>
<blockquote>"When a prosecutor seeks to rely upon consent to justify the lawfulness of a search, he has the burden of proving that the consent was, in fact, freely and voluntarily given. This burden cannot be discharged by showing no more than acquiescence to a claim of lawful authority. A search conducted in reliance upon a warrant cannot later be justified on the basis of consent if it turns out that the warrant was invalid. The result can be no different when it turns out that the State does not even attempt to rely upon the validity of the warrant, or fails to show that there was, in fact, any warrant at all.</blockquote>
<blockquote>"When a law enforcement officer claims authority to search a home under a warrant, he announces in effect that the occupant has no right to resist the search. The situation is instinct with coercion albeit colorably lawful coercion. Where there is coercion there cannot be consent." <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina"><i>Id.,</i> at 548-550</a></span>.</blockquote>
<p>I would affirm the judgment below.</p>
<h2>NOTES</h2>
<p>[1]  "Each licensed importer, licensed manufacturer, licensed dealer, and licensed collector shall maintain such records of importation, production, shipment, receipt, sale, or other disposition, of firearms and ammunition at such place, for such period, and in such form as the Secretary [of the Treasury] may by regulations prescribe. Such importers, manufacturers, dealers, and collectors shall make such records available for inspection at all reasonable times, and shall submit to the Secretary such reports and information with respect to such records and the contents thereof as he shall by regulations prescribe. The Secretary may enter during business hours the premises (including places of storage) of any firearms or ammunition importer, manufacturer, dealer, or collector for the purpose of inspecting or examining (1) any records or documents required to be kept by such importer, manufacturer, dealer, or collector under the provisions of this chapter or regulations issued under this chapter, and (2) any firearms or ammunition kept or stored by such importer, manufacturer, dealer, or collector at such premises. Upon the request of any State or any political subdivision thereof, the Secretary may make available to such State or any political subdivision thereof, any information which he may obtain by reason of the provisions of this chapter with respect to the identification of persons within such State or political subdivision thereof, who have purchased or received firearms or ammunition, together with a description of such firearms or ammunition." <span class="citation no-link">18 U. S. C. § 923</span> (g).</p>
<p>[2]  Respondent was licensed under <span class="citation no-link">18 U. S. C. § 923</span> to sell certain sporting weapons as defined in <span class="citation no-link">18 U. S. C. § 921</span>. The sawed-off rifles, however, fell under <span class="citation no-link">26 U. S. C. § 5845</span>'s technical definition of "firearms," and every dealer in such firearms was required by <span class="citation no-link">26 U. S. C. § 5801</span> to pay a special occupational tax of $200 a year. Such firearms are also required to be registered to a dealer in the National Firearms Registration and Transfer Record. <span class="citation no-link">26 U. S. C. § 5841</span>. Respondent was indicted on six counts. Count I, on which he was convicted, charged that he had "wilfully and knowingly engaged in business as a dealer in firearms, as defined by 26 U. S. C. 5845 . . . without having paid the special (occupational) tax required by 26 U. S. C. 5801 for his business." Counts II-V, on which he was acquitted, charged that he had possessed certain firearms that were not identified by serial number, as required by <span class="citation no-link">26 U. S. C. § 5842</span>, and that were not registered in the National Firearms Registration and Transfer Record, as required by <span class="citation no-link">26 U. S. C. § 5841</span>. Count VI, which charged respondent with failing to maintain properly the records required under <span class="citation no-link">18 U. S. C. § 923</span>, was severed and is awaiting trial.</p>
<p>[3]  "The seizure of stolen goods is authorized by the common law; and the seizure of goods forfeited for a breach of the revenue laws, or concealed to avoid the duties payable on them, has been authorized by English statutes for at least two centuries past; and the like seizures have been authorized by our own revenue acts from the commencement of the government. The first statute passed by Congress to regulate the collection of duties, the act of July 31, 1789, <span class="citation no-link">1 Stat. 29</span>, 43, contains provisions to this effect. As this act was passed by the same Congress which proposed for adoption the original amendments to the Constitution, it is clear that the members of that body did not regard searches and seizures of this kind as `unreasonable,' and they are not embraced within the prohibition of the amendment. . . . [I]n the case of excisable or dutiable articles, the government has an interest in them for the payment of the duties thereon, and until such duties are paid has a right to keep them under observation, or to pursue and drag them from concealment." <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S., at 623-624</a></span> (footnote omitted).</p>
<p>[4]  Congress has made it a crime to violate any provision of the Gun Control Act. <span class="citation no-link">18 U. S. C. § 924</span>.</p>
<p>[*]  The majority concludes that <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span></i> is "inapposite" to this case. <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span></i> holds that an <i>otherwise invalid</i> search is not legitimated because of the occupant's consent to a law enforcement officer's assertion of authority. <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span></i> is only "inapposite" if one has already concluded that consent is irrelevant to the validity of the search at issue.</p>

</div>
```

---

## GROUP: content/cases/United States v. Black.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Black
type: case
citation: "707 F.3d 531 (2013)"
parallel_cite: ""
neutral_cite: "2013 WL 657789; 2013 U.S. App. LEXIS 4251"
court: "U.S. Court of Appeals, 4th Cir."
court_level: coa
circuit: ca4
year: 2013
date_decided: 2013-02-25
docket: 11-5084
authority_weight: "Binding in-circuit — 4th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/821235/united-states-v-nathaniel-black/"
  cluster_id: 821235
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Black
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: Key
related:
  - "[[Terry Stops and Reasonable Suspicion]]"
  - "[[Terry v. Ohio]]"
  - "[[California v. Hodari D.]]"
  - "[[Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - terry-stop
  - reasonable-suspicion
  - high-crime-area
holding: "Reasonable suspicion for a Terry stop cannot be built by patching together a set of innocent, suspicion-free facts; a companion's lawful open carry of a firearm, another person's arrest history, presence in a high-crime area at night, and cooperative behavior — none particularized to the defendant — do not add up to reasonable suspicion, and there is no reasonable suspicion merely by association."
---

# United States v. Black

*707 F.3d 531 (4th Cir. 2013)* (No. 11-5084) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 821235 → opinion 821235 (707 F.3d 531, decided 2013-02-25); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Late one night, Charlotte-Mecklenburg officers patrolling a high-crime division watched a car idle at a gas pump without the driver pumping gas — behavior Officer Zastrow deemed "unusual" and indicative of drug activity. They followed the car to a parking lot between apartment complexes, where the driver, Dior Troupe, joined a group of men that included Nathaniel Black. The officers recognized one man, Charles Gates, as having a prior record, and saw that Troupe was openly carrying a firearm. Several officers converged and began frisking members of the group. Black handed over his identification, which showed an out-of-district address, then walked away; an officer grabbed him, and a search revealed that Black — a convicted felon — was carrying a firearm. The district court denied his motion to suppress, and Black entered a conditional guilty plea.

## Issue
Whether the totality of the factors the government identified — a companion's lawful open carry of a firearm, another man's arrest history, presence in a high-crime area at night, and Black's cooperation — amounted to reasonable suspicion justifying Black's seizure under *[[Terry v. Ohio]]*.

## Rule
*[[Terry v. Ohio|Terry]]* requires specific and articulable facts, particular to the person seized, that reasonably warrant the intrusion; innocent facts can combine into reasonable suspicion, but not here: "we encounter yet another situation where the Government attempts to meet its Terry burden by patching together a set of innocent, suspicion-free facts, which cannot rationally be relied on to establish reasonable suspicion." — slip op. at 11. The court added two limits central to the stop's illegality: where a state permits open carry, "the exercise of this right, without more, cannot justify an investigatory detention," and "there is no reasonable suspicion merely by association."

## Application
The court dismantled each proffered factor. Troupe's idling at a gas pump was not suspicious; Gates's arrest history was not particularized to Black; Troupe's openly carried firearm was legal under North Carolina law and could not, without more, justify detaining anyone — least of all Black, who was merely present in the group; and Black's cooperation in producing his ID was innocent, not incriminating. That left only the men's presence in a high-crime area at night, which cannot by itself establish reasonable suspicion. Aggregating these innocent facts, and invoking suspicion by association, could not carry the government's *[[Terry v. Ohio|Terry]]* burden.

## Conclusion
The judgment was **reversed and [[Reading and Citing Cases#vacated|vacated]]**: the district court erred in denying suppression, and Black's conviction and sentence were [[Reading and Citing Cases#vacated|vacated]]. Gregory, J., wrote for the court (Gregory, Davis, JJ.); Traxler, C.J., concurred in the result.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Black* is a leading Fourth Circuit statement that *[[Terry v. Ohio|Terry]]*'s reasonable-suspicion standard cannot be satisfied by stacking innocent facts or by association, and that lawfully carrying a firearm where state law permits open carry is not itself a basis to detain — a rationale the court tied to its 2011 line of cases including *[[United States v. Massenburg]]*.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Key*

## Sources
- [*United States v. Black*, 707 F.3d 531 (4th Cir. 2013)](https://www.courtlistener.com/opinion/821235/united-states-v-nathaniel-black/) — pinpoint: slip op. at 11 (patchwork-of-innocent-facts holding); the CL opinion text carries the slip-opinion page numbers rather than 707 F.3d star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "13e916d4736bcdd6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "707 F.3d 531 (2013)", "court": "U.S. Court of Appeals, 4th Cir.", "neutral_cite": "2013 WL 657789; 2013 U.S. App. LEXIS 4251", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Black", "year": "2013"}}
{"assertion_id": "21fce6dde88b8f0f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Reasonable suspicion for a Terry stop cannot be built by patching together a set of innocent, suspicion-free facts; a companion's lawful open carry of a firearm, another person's arrest history, presence in a high-crime area at night, and cooperative behavior — none particularized to the defendant — do not add up to reasonable suspicion, and there is no reasonable suspicion merely by association.", "title": "United States v. Black"}}
{"assertion_id": "c7f5b48799aff3ac", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Key", "title": "United States v. Black"}}
{"assertion_id": "44b594fad76ebbf2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "United States v. Black"}}
{"assertion_id": "6bfc35db883e008d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Black", "varies_by_point": "false"}}
```

### lake record — United States v. Black

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Black",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Nathaniel Black",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Nathaniel BLACK, Defendant-Appellant",
    "input_case_name": "United States v. Black",
    "court": "U.S. Court of Appeals, 4th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2013-02-25",
    "year": 2013,
    "docket": "11-5084",
    "cluster_id": 821235,
    "lead_opinion_id": 9502817,
    "sibling_ids": [],
    "absolute_url": "/opinion/821235/united-states-v-nathaniel-black/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "707 F.3d 531",
      "volume": "707",
      "reporter": "F.3d",
      "page": "531",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2013 WL 657789",
        "volume": "2013",
        "reporter": "WL",
        "page": "657789",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. App. LEXIS 4251",
        "volume": "2013",
        "reporter": "U.S. App. LEXIS",
        "page": "4251",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "707 F.3d 531",
        "volume": "707",
        "reporter": "F.3d",
        "page": "531",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 657789",
        "volume": "2013",
        "reporter": "WL",
        "page": "657789",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. App. LEXIS 4251",
        "volume": "2013",
        "reporter": "U.S. App. LEXIS",
        "page": "4251",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "707 F.3d 531",
    "official_selection": {
      "court_class": "coa",
      "selected": "707 F.3d 531",
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
    "date_created": "2026-07-07T13:48:26Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-black--821235",
      "to_record_id": "United States v. Black",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Black

```
<opinion type="majority">
<p id="b558-7">Reversed and vacated by published opinion. Judge GREGORY wrote the opinion, in which Judge DAVIS joined. Chief Judge TRAXLER wrote a separate opinion concurring in the result.</p>
<p id="b558-8">OPINION</p>
<author id="b558-9">GREGORY, Circuit Judge:</author>
<p id="b558-10">In <em>Terry v. Ohio, </em>Chief Justice Earl Warren recognized that police officers need discretion to perform their investigative duties. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968). Since <em>Terry, </em>this discretion has been judicially broadened, giving police wide latitude to fulfill their functions. In some circumstances, however, police abuse this discretion, and we must remind law enforcement that the Fourth Amendment protects against unreasonable searches and seizures. Because in this case, we find the police disregarded the basic tenets of the Fourth Amendment, we reverse.</p>
<p id="b558-12">I.</p>
<p id="ALY">In reviewing the denial of a motion to suppress, we view the facts in the light most favorable to the Government, as the party prevailing below. <em>United States v. Jamison, </em><span class="citation" data-id="1024429"><a href="/opinion/1024429/united-states-v-jamison/#628" aria-description="Citation for case: United States v. Jamison">509 F.3d 623, 628</a></span> (4th Cir.2007). At approximately 10:00 p.m. on June 15, 2010, uniformed Officers Matthew Zastrow and Shane Strayer of the Charlotte-Meck-lenburg Police Department were in a marked police vehicle, patrolling the East-way Division of Charlotte, North Carolina. Certain apartment complexes in the East-way Division are known for armed robberies and other violent crimes.</p>
<p id="b558-14">As the officers patrolled, they observed a vehicle parked at the pump of a gas station. Though neither officer saw the vehicle pull into the gas station, during the approximately three-minute observation, the officers observed that the driver and sole occupant of the vehicle did not leave the car, pump gas, or go into the convenience store. Officer Zastrow believed this type of behavior was “unusual” and indicative of drug transactions. On this basis, the officers ran the license tag of the vehicle, which retrieved no outstanding traffic violations, and followed the vehicle as it traveled to a nearby parking lot located in between two apartment complexes.</p>
<p id="b558-15">At the parking lot, the officers observed the driver of the vehicle, later identified as Dior Troupe, park his vehicle and walk toward a group of five men in a semi-circle who were speaking and laughing with each other. Four of the men were standing, and an African-American male, later identified as Appellant Nathaniel Black, was <page-number citation-index="1" label="535">*535</page-number>sitting at the left-end of the semi-circle. The six men saw the police vehicle but did not react. Neither officer observed the men engaging in any criminal activity.</p>
<p id="b559-5">Officer Zastrow drove out of view and contacted other police units for assistance because he and Officer Strayer wanted to make “voluntary contact” with the men, and the officers believed it was unwise to do so if they were outnumbered. Officers Butler and Lang were in the immediate area and joined Officers Zastrow and Strayer in an adjacent parking lot. The four officers returned in their marked police vehicles to the same parking lot where they saw the men in the semi-circle. Three other officers, Fusco, Conner, and Harris, were also nearby in another apartment complex responding to a different call and later joined the first four officers.</p>
<p id="b559-6">At about 10:15 p.m., the four uniformed officers exited their marked patrol vehicles and started walking towards the men. Officers Zastrow and Strayer recognized one of the men in the group as Charles Gates. They had spoken with Gates two weeks prior to this incident about his residence in one of the nearby apartments. Officer Zastrow was aware of Gates’ prior felony drug arrests. Officer Strayer had previously arrested Gates for driving while intoxicated and drug offenses, and also knew Gates had been tased once by another officer. Neither officer knew whether Gates’ prior arrests resulted in convictions.</p>
<p id="b559-7">As the officers approached the men, Troupe, who was closer to the officers, motioned to the officers with his hands indicating that he had a firearm in a holster on his hip, in plain view. Officer Strayer seized Troupe’s firearm, obtained Troupe’s driver’s license, and secured the firearm in a patrol vehicle. Officer Stray-er stated that although it is legal in North Carolina for a person to openly carry a firearm, in his years in the Eastway Division, he had never seen anyone do it.</p>
<p id="b559-10">Officer Zastrow testified he had been trained to operate on what he called the “Rule of Two,” that is, if the police find one firearm, there will “most likely” be another firearm in the immediate area. Officer Strayer testified he had also been trained on what he referred to as the “one-plus” rule, that where there is one gun, there usually is another gun. Officer Strayer acknowledged that this “rule” was not always accurate as there are instances where a second gun is not always recovered.</p>
<p id="b559-11">After securing Troupe’s gun in the police vehicle, Officer Strayer frisked Troupe, and proceeded to frisk the other men in the group. By this time, Officers Fusco and Conner had arrived at the scene, and a total of six officers were present.<footnotemark>1</footnotemark> Officers Fusco and Conner stood at a distance of about 10 to 15 feet from the men to ensure no other individuals walked up to the locale of the police encounter with the men.</p>
<p id="b559-12">While Officer Strayer was securing Troupe’s gun, Officer Zastrow introduced himself to the men. He asked if any of the men lived in the apartments or if they were visiting. At that point, Appellant Black, who was still sitting, offered Officer Zastrow his North Carolina identification card. To Officer Zastrow, it was “unusual for someone to volunteer an ID” and the “remaining individuals in the group were argumentative and did not give any information, so it stood out that one volunteered an ID immediately.” From his ID, Officer Zastrow believed that Black lived outside the Eastway Division. Black confirmed this belief by informing Officer Zas-<page-number citation-index="1" label="536">*536</page-number>trow that he was visiting some friends in the area.</p>
<p id="b560-4">Officer Zastrow did not return Black’s ID, instead, he pinned it to his uniform, and continued to obtain identification information from the other individuals. Officer Zastrow testified that the other individuals did not have physical identification so he wrote their names, addresses, and birth-dates in a notebook.<footnotemark>2</footnotemark> Officer Zastrow described Black’s behavior during this encounter as “extremely cooperative.”</p>
<p id="b560-5">By this time, Officer Strayer had frisked Troupe and proceeded to frisk Nicolas Moses, who was standing at the right-end of the semi-circle. While Officer Strayer was frisking Moses, Officer Zastrow noticed that Black became “fidgety,” sat forward in his chair, and “began looking left and right.” In Officer Zastrow’s training and experience, looking left and right is a “cue” that the individual is looking to flee. To Officer Fusco, who also observed this behavior, it indicates that the individual seeks a path to escape.</p>
<p id="b560-6">Black stood up, said he was going home, and began walking towards the apartments. Officer Zastrow, who was approximately five feet from Black, walked in front of Black and told him that he was not free to leave and he should sit down. In response, Black said “I can’t go home?” or “I can’t leave?” and continued walking away.</p>
<p id="b560-7">Officer Zastrow then grabbed Black’s left bicep with his left hand. According to Officer Zastrow, he could feel Black’s “extremely fast” pulse through Black’s t-shirt, which he believed was a sign of nervousness. Black pulled away from Officer Zastrow and began running towards an apartment building. Officers Zastrow and Fusco told Black to stop, and when he refused, they chased him. Officer Fusco grabbed Black from behind and tackled him to the ground. Officer Zastrow grabbed Black’s wrist to try to handcuff him. As he did so, Officer Zastrow felt a metal object underneath Black’s hand and clothing, which Officer Zastrow immediately recognized as a firearm. Officer Zastrow yelled “gun,” and held on to Black’s hand until the firearm fell to the ground. Officer Zastrow placed Black in handcuffs and arrested him.</p>
<p id="b560-10">Black was charged in a one-count indictment for possession of a firearm by a convicted felon, in violation of <span class="citation no-link">18 U.S.C. § 922</span>(g)(1). Black moved to suppress the firearm on the basis that it was the fruit of the unlawful seizure of his person. At a hearing on the motion to suppress, Black argued that he was unlawfully seized when he was told he could not leave, and the seizure was not supported by reasonable articulable suspicion. The Government relied on <em>California v. Hodari D., </em><span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/" aria-description="Citation for case: California v. Hodari D.">499 U.S. 621</a></span>, <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/" aria-description="Citation for case: California v. Hodari D.">111 S.Ct. 1547</a></span>, <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/" aria-description="Citation for case: California v. Hodari D.">113 L.Ed.2d 690</a></span> (1991), to argue that until Black’s bicep was grabbed, he was not seized for Fourth Amendment purposes, and his seizure was supported by reasonable suspicion. The district court agreed with the Government and denied the motion.</p>
<p id="b560-11">Subsequently, Black entered a conditional plea of guilty and reserved his right to appeal the denial of his suppression motion. <em>See </em>Fed.R.Crim.P. 11(a)(2). At sentencing, the district court found that with a total offense level of 31, and a criminal history category of TV, Black’s advisory guideline range was 151 to 188 months. However, because Black was subject to a statutory minimum sentence of 180 months, see <span class="citation no-link">18 U.S.C. § 924</span>(e), the court <page-number citation-index="1" label="537">*537</page-number>sentenced Black to 180 months’ imprisonment and three years of supervised release. ,</p>
<p id="b561-5">Black now appeals the denial of his motion to suppress, and we have jurisdiction pursuant to <span class="citation no-link">28 U.S.C. § 1291</span>.</p>
<p id="b561-6">II.</p>
<p id="b561-7">We review a district court’s factual findings in a motion to suppress for clear error, and the legal determinations <em>de novo. United States v. Cain, </em><span class="citation" data-id="1025667"><a href="/opinion/1025667/united-states-v-cain/#481" aria-description="Citation for case: United States v. Cain">524 F.3d 477, 481</a></span> (4th Cir.2008).</p>
<p id="b561-8">III.</p>
<p id="b561-9">The Fourth Amendment protects “[t]he right of the people to be secure in their persons ... against unreasonable searches and seizures.” U.S. Const, amend. TV. “The Fourth Amendment does not proscribe all contact between the police and citizens, but is designed ‘to prevent arbitrary and oppressive interference by enforcement officials with the privacy and personal security of individuals.’ ” <em>I.N.S. v. Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U.S. 210, 215</a></span>, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">104 S.Ct. 1758</a></span>, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">80 L.Ed.2d 247</a></span> (1984) (quoting <em>United States v. Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U.S. 543, 554</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">96 S.Ct. 3074</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">49 L.Ed.2d 1116</a></span> (1976)).</p>
<p id="b561-11">Although brief encounters between police and citizens require no objective justification, <em>United States v. Weaver, </em><span class="citation" data-id="776764"><a href="/opinion/776764/united-states-v-otis-lee-weaver-jr/#309" aria-description="Citation for case: United States v. Otis Lee Weaver, Jr.">282 F.3d 302, 309</a></span> (4th Cir.2002), it is clearly established that an investigatory detention of a citizen by an officer must be supported by reasonable articulable suspicion that the- individual is engaged in criminal activity. <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 21</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. In the case before us, we first consider when Black was “seized” for purposes of the Fourth Amendment, and then consider whether the seizure comports with the reasonable suspicion standard set forth in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</em></p>
<p id="b561-14">A.</p>
<p id="b561-15">A person is “seized” within the meaning of the Fourth Amendment if, “ ‘in view of all [of] the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave.’ ” <em>United States v. Gray, </em><span class="citation" data-id="528214"><a href="/opinion/528214/united-states-v-arthur-gray/#322" aria-description="Citation for case: United States v. Arthur Gray">883 F.2d 320, 322</a></span> (4th Cir.1989) (quoting <em>United States v. Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U.S. 544, 554</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. 1870</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">64 L.Ed.2d 497</a></span> (1980)).<footnotemark>3</footnotemark> Specific factors to consider in determining whether a reasonable person would feel free to leave include: (i) the number of police officers present at the scene; (ii) whether the police officers were in uniform; (iii) whether the police officers displayed their weapons; (iv) whether they “touched the defendant or made any attempt to physically block his departure or <page-number citation-index="1" label="538">*538</page-number>restrain his movement”; (v) “the use of language or tone of voice indicating that compliance with the officer’s request might be compelled”; (vi) whether the officers informed the defendant that they suspected him of “illegal activity rather than treating the encounter as ‘routine’ in nature”; and (vii) “whether, if the officer requested from the defendant ... some form of official identification, the officer promptly returned it.” <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U.S. at 554</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. 1870</a></span>; <em>Gray, </em><span class="citation" data-id="528214"><a href="/opinion/528214/united-states-v-arthur-gray/#322" aria-description="Citation for case: United States v. Arthur Gray">883 F.2d at 322-23</a></span>. We have noted that though not dispositive, “the retention of a citizen’s identification or other personal property or effects is highly <em>material </em>under the totality of the circumstances analysis.” <em>Weaver, </em><span class="citation" data-id="776764"><a href="/opinion/776764/united-states-v-otis-lee-weaver-jr/#310" aria-description="Citation for case: United States v. Otis Lee Weaver, Jr.">282 F.3d at 310</a></span> (emphasis added).</p>
<p id="b562-4">Considering the totality of the following circumstances of this case, it is clear that when Officer Zastrow expressly told Black he could not leave, Black was <em>already </em>seized for purposes of the Fourth Amendment. First is the collective show of authority by the uniformed police officers and their marked police vehicles. The citizens observed a marked police vehicle drive to the parking lot, and then drive out of view. The police vehicle returned along with another marked police vehicle. Four uniformed officers approached the men, a number that quickly increased to six uniformed officers, and then seven. At least two of the officers were performing perimeter duties, ensuring that no other individuals interrupted the police interaction, and preventing the men from leaving the vicinity. Second, Officer Strayer had obtained Troupe’s gun and secured it in his police vehicle, indicating that at the very least, Troupe was not free to leave. <em>See Weaver, </em><span class="citation" data-id="776764"><a href="/opinion/776764/united-states-v-otis-lee-weaver-jr/#310" aria-description="Citation for case: United States v. Otis Lee Weaver, Jr.">282 F.3d at 310</a></span> (retention of personal property is highly material). Third, Officer Strayer had frisked Troupe and was frisking Moses; a reliable indicator that Officer Strayer would proceed to frisk the other men, and that the men were not free to leave until such action was completed. Fourth, and highly material, is the retention of Black’s ID by Officer Zastrow, while Officer Stray-er frisked other men in the group. <em>See <span class="citation" data-id="776764"><a href="/opinion/776764/united-states-v-otis-lee-weaver-jr/" aria-description="Citation for case: United States v. Otis Lee Weaver, Jr.">id.</a></span></em></p>
<p id="b562-6">These factors persuade us that long before he was told not to leave, Black was seized for purposes of the Fourth Amendment. Specifically, we hold that in view of all these circumstances, Black was seized at the point when Officer Zastrow pinned Black’s ID to his uniform, while Officer Strayer frisked the men in the group. The verbal directive from the officers not to leave was not the initiation of the seizure, but rather an affirmation that Black was not free to leave. Black’s subsequent decision to leave does not negate the finding that a reasonable person in Black’s circumstances would not feel free to leave. Instead, Black’s decision to leave was an effort to terminate an illegal seizure.</p>
<p id="b562-7">We disagree with the Government’s argument that all of Black’s interactions with the police before his bicep was grabbed were consensual and do not implicate the Fourth Amendment. Though we do not reach this issue, we are doubtful that this encounter was consensual at its inception as the facts of this case are similar to our recent decision in <em>United States v. Jones, </em><span class="citation" data-id="799658"><a href="/opinion/799658/united-states-v-jones/#299" aria-description="Citation for case: United States v. Jones">678 F.3d 293, 299, 301-04</a></span> (4th Cir.2012), where we held that the defendant was seized prior to the beginning of the verbal interaction. Even assuming the encounter here was consensual at its inception, the increasing show of authority, immediate seizure of Troupe’s gun, and frisk of the men in the group quickly changed the encounter to an investigatory detention. Because we hold that Black was seized for purposes of the Fourth Amendment when his ID was retained while his companions were frisked, we need not determine <page-number citation-index="1" label="539">*539</page-number>whether he was seized at any point prior to this.</p>
<p id="b563-5">B.</p>
<p id="b563-6">We next consider whether Black’s seizure was reasonable. To be lawful, a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop “must be supported at least by a reasonable and articulable suspicion that the person seized is engaged in criminal activity.” <em>Reid v. Georgia, </em><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#440" aria-description="Citation for case: Reid v. Georgia">448 U.S. 438, 440</a></span>, <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">100 S.Ct. 2752</a></span>, <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">65 L.Ed.2d 890</a></span> (1980). The level of suspicion must be a “particularized and objective basis for suspecting the particular person stopped of criminal activity.” <em>United States v. Griffin, </em><span class="citation" data-id="9519150"><a href="/opinion/1030983/united-states-v-griffin/#152" aria-description="Citation for case: United States v. Griffin">589 F.3d 148, 152</a></span> (4th Cir.2009). As such, “the officer must be able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant that intrusion.” <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 21</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>.<footnotemark>4</footnotemark> There is no reasonable suspicion merely by association.</p>
<p id="b563-7">Here, the totality of the factors outlined by the district court — an individual’s presence at a gas station; prior arrest history of another individual; lawful possession and display of a firearm by another; Black’s submission of his ID showing an out-of-district address to Officer Zas-trow, all of which occurred in a high crime area at night — fails to support the conclusion that Officer Zastrow had reasonable suspicion to detain Black.<footnotemark>5</footnotemark></p>
<p id="b563-8">At least four times in 2011, we admonished against the Government’s misuse of innocent facts as indicia of suspicious activity. <em>See United States v. Powell, </em><span class="citation" data-id="9484981"><a href="/opinion/617111/united-states-v-powell/" aria-description="Citation for case: United States v. Powell">666 F.3d 180</a></span> (4th Cir.2011); <em>Massenburg, </em><span class="citation" data-id="223188"><a href="/opinion/223188/united-states-v-massenburg/" aria-description="Citation for case: United States v. Massenburg">654 F.3d 480</a></span>; <em>United States v. Digiovanni, </em><span class="citation" data-id="221744"><a href="/opinion/221744/united-states-v-stephen-digiovanni/" aria-description="Citation for case: United States v. Stephen Digiovanni">650 F.3d 498</a></span> (4th Cir.2011); and <em>United States v. Foster, </em><span class="citation" data-id="205824"><a href="/opinion/205824/united-states-v-foster/" aria-description="Citation for case: United States v. Foster">634 F.3d 243</a></span> (4th Cir.2011). Although factors “susceptible of innocent explanation,” when taken together, may “form a particularized and objective basis” for reasonable suspicion for a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop, <em>United States v. Arvizu, </em><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/#277" aria-description="Citation for case: United States v. Arvizu">534 U.S. 266, 277-78</a></span>, <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">122 S.Ct. 744</a></span>, <span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">151 L.Ed.2d 740</a></span> (2002), this is not such a case. Instead, we encounter yet another situation where the Government attempts to meet its <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>burden by patching together a set of innocent, suspicion-free facts, which cannot rationally be relied on to establish reasonable suspicion.</p>
<p id="b563-12">First, Officer Zastrow’s suspicion that a lone driver at a gas pump who he did not observe drive into the gas station is engaged in drug trafficking borders on absurd.<footnotemark>6</footnotemark> Other than Troupe, there was no one else in the vehicle, and it defies reason to believe that Troupe was engaged in drug trafficking — an act that by definition involves transmitting drugs to another person. Moreover, by Officer Zastrow’s own admission, he failed to include this gas station observation in his incident report on Black’s arrest because he viewed them as separate incidents. In short, concluding that Troupe’s presence in his vehicle at a gas station is suspicious is unreasonable.</p>
<p id="b564-3"><page-number citation-index="1" label="540">*540</page-number>Second, Gates’ prior arrest history cannot be a logical basis for a reasonable, particularized suspicion as to Black. Without more, Gates’ prior arrest history in itself is insufficient to support reasonable suspicion as to Gates, much less Black. <em>See Powell, </em><span class="citation" data-id="9484981"><a href="/opinion/617111/united-states-v-powell/#188" aria-description="Citation for case: United States v. Powell">666 F.3d at 188</a></span> (“[A] prior criminal record is not, standing alone, sufficient to create reasonable suspicion.” (citation omitted)). Moreover, we “ha[ve] repeatedly emphasized that to be reasonable under the Fourth Amendment, a search ordinarily must be based on <em>individualized </em>suspicion of wrongdoing.” <em>Des-Roches v. Caprio, </em><span class="citation" data-id="758051"><a href="/opinion/758051/james-desroches-ii-a-minor-by-his-father-and-next-friend-james/#574" aria-description="Citation for case: James Desroches, Ii, a Minor, by His Father and Next...">156 F.3d 571, 574</a></span> (4th Cir.1998) (quotation marks and alterations omitted) (emphasis added). In other words, the suspicious facts must be specific and particular to the individual seized. Exceptions to the individualized suspicion requirement “have been upheld only in ‘certain limited circumstances,’ where the search is justified by ‘special needs’ ”— that is, concerns other than crime detection—and must be justified by balancing the individual’s privacy expectations against the government interests. <em><span class="citation" data-id="758051"><a href="/opinion/758051/james-desroches-ii-a-minor-by-his-father-and-next-friend-james/" aria-description="Citation for case: James Desroches, Ii, a Minor, by His Father and Next...">Id.</a></span> </em>(quoting <em>Chandler v. Miller, </em><span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#308" aria-description="Citation for case: Chandler v. Miller">520 U.S. 305, 308, 313</a></span>, <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">117 S.Ct. 1295</a></span>, <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">137 L.Ed.2d 513</a></span> (1997)); <em>see Treasury Employees v. Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U.S. 656, 665-66</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">109 S.Ct. 1384</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">103 L.Ed.2d 685</a></span> (1989). Here, the Government has not identified any substantial interests that override Black’s interest in privacy or that suppress the normal requirement of individualized suspicion.</p>
<p id="b564-4">Third, it is undisputed that under the laws of North Carolina, which permit its residents to openly carry firearms, <em>see generally </em>N.C. Gen.Stat. §§ 14-415.10 to 14-415.23, Troupe’s gun was legally possessed and displayed. The Government contends that because other laws prevent convicted felons from possessing guns, the officers could not know whether Troupe was lawfully in possession of the gun until they performed a records check. Additionally, the Government avers it would be “foolhardy” for the officers to “go about their business while allowing a stranger in their midst to possess a firearm.” We are not persuaded.</p>
<p id="b564-6">Being a felon in possession of a firearm is not the default status. More importantly, where a state permits individuals to openly carry firearms, the exercise of this right, without more, cannot justify an investigatory detention. Permitting such a justification would eviscerate Fourth Amendment protections for lawfully armed individuals in those states. <em>United States v. King, </em><span class="citation" data-id="604813"><a href="/opinion/604813/united-states-v-terry-king-and-valerie-jean-burdex/#1559" aria-description="Citation for case: United States v. Terry King and Valerie Jean Burdex">990 F.2d 1552, 1559</a></span> (10th Cir.1993). Here, Troupe’s lawful display of his lawfully possessed firearm cannot be the justification for Troupe’s detention. <em>See St. John v. McColley, </em><span class="citation" data-id="2417423"><a href="/opinion/2417423/st-john-v-mccolley/#1161" aria-description="Citation for case: St. John v. McColley">653 F.Supp.2d 1155, 1161</a></span> (D.N.M.2009) (finding no reasonable suspicion where the plaintiff arrived at a movie theater openly carrying a holstered handgun, an act which is legal in the State of New Mexico.) That the officer had never seen anyone in this particular division openly carry a weapon also fails to justify reasonable suspicion. From our understanding of the laws of North Carolina, its laws apply uniformly and without exception in every single division, and every part of the state. Thus, the officer’s observation is irrational and fails to give rise to reasonable suspicion. To hold otherwise would be to give the judicial imprimatur to the dichotomy in the intrusion of constitutional protections.</p>
<p id="b564-7">Additionally, even if the officers were justified in detaining Troupe for exercising his constitutional right to bear arms, reasonable suspicion as to Troupe does not amount to, and is not particularized as to Black, and we refuse to find reasonable suspicion merely by association.</p>
<p id="b564-8">Fourth, with respect to the officers’ “Rule of Two” or “one-plus rule,” we <page-number citation-index="1" label="541">*541</page-number>would abdicate our judicial role if we took law enforcement-created rules as sufficient to establish reasonable suspicion. “The essential purpose of the proscriptions in the Fourth Amendment is to impose a standard of ‘reasonableness’ upon the exercise of discretion by government officials, including law enforcement agents, in order to safeguard the privacy and security of individuals against arbitrary invasions.” <em>Delaware v. Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U.S. 648, 653-54</a></span>, <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S.Ct. 1391</a></span>, <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">59 L.Ed.2d 660</a></span> (1979) (citation and quotation marks omitted). As such, we must consider whether, in applying law enforcement rules, there are safeguards “to assure that the individual’s reasonable expectation of privacy is not subject to the discretion of the official in the field.” <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#655" aria-description="Citation for case: Delaware v. Prouse"><em>Id. </em>at 655</a></span>, <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S.Ct. 1391</a></span> (citation and quotation marks omitted).</p>
<p id="b565-5">Here, the practical implication of applying the so-called “Rule of Two” is that anyone in proximity to an individual with a gun is involved in criminal activity. Such a rule subjects to seizure or search anyone who actively or passively associates with a gun carrier. The seizure has no connection with the individual seized, the activity they are involved in, their mannerisms, or their suspiciousness; rather, the seizure is a mere happenstance of geography. The absurdity of this rule may be gleaned from scenarios where an individual carrying a firearm walks into a monastery subjecting to seizure all of the nuns and priests, or an ice-cream shop subjecting all of the patrons to a seizure. Or could police officers apply this rule to seize all individuals at a shooting range or on a hunting trip? The scenarios abound. As there are no safeguards against the unlawful use of discretion by the officer applying such an arbitrary and boundless rule, it cannot be a basis for reasonable suspicion of criminal activity.</p>
<p id="b565-6">Fifth, it is counterintuitive that Black provided a justification for reasonable suspicion by volunteering his ID to the officer. The Government characterizes Black’s behavior as “overly” cooperative and cites cases outside this Circuit for the proposition that “a surprisingly high level of cooperation” though not dispositive, is a factor to consider for individualized suspicion. <em>See United States v. Bravo, </em><span class="citation" data-id="9495158"><a href="/opinion/778266/united-states-v-ricardo-a-bravo/#1007" aria-description="Citation for case: United States v. Ricardo A. Bravo">295 F.3d 1002, 1007</a></span> (9th Cir.2002); <em>United States v. Ozbirn, </em><span class="citation" data-id="158521"><a href="/opinion/158521/united-states-v-ozbirn/" aria-description="Citation for case: United States v. Ozbirn">189 F.3d 1194</a></span>, 1200 n. 4 (10th Cir.1999). The record indicates that three of the six men provided identification to the officers, thus, Black’s action could hardly be characterized as overly cooperative. Additionally, we have noted that this type of argument — that cooperation is a justification for reasonable suspicion — actually places a defendant in a worse position than if he had simply refused to cooperate altogether because the Supreme Court has “ ‘consistently held that a refusal to cooperate, without more, does not furnish the minimal level of objective justification needed for a detention or seizure.’ ” <em>Powell, </em><span class="citation" data-id="9484981"><a href="/opinion/617111/united-states-v-powell/" aria-description="Citation for case: United States v. Powell">666 F.3d at 189</a></span> n. 10 (quoting <em>Florida v. Bostick, </em><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick">501 U.S. 429, 437</a></span>, <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">111 S.Ct. 2382</a></span>, <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">115 L.Ed.2d 389</a></span> (1991)). In certain communities that have been subject to overbearing or harassing police conduct, cautious parents may counsel their children to be respective, compliant, and accommodating to police officers, to do everything officers instruct them to do. If police officers can justify unreasonable seizures on a citizen’s acquiescence, individuals would have no Fourth Amendment protections unless they interact with officers with the perfect amount of graceful disdain.</p>
<p id="b565-7">Likewise, there is nothing suspicious about the fact that Black’s ID revealed he lived outside the district. Black correctly informed the officers that he was visiting friends. If Black was untruthful or provided a false identification, then the offi<page-number citation-index="1" label="542">*542</page-number>cers may have had some minimal, but not dispositive, basis for reasonable suspicion.</p>
<p id="b566-4">The pertinent facts remaining in the reasonable suspicion analysis are that the men were in a high crime area at night. These facts, even when coupled with the officers’ irrational assumptions based on innocent facts, fail to support the conclusion that Officer Zastrow had reasonable suspicion that Black was engaging in criminal activity. <em>See Illinois v. Wardlow, </em><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/#124" aria-description="Citation for case: Illinois v. Wardlow">528 U.S. 119, 124</a></span>, <span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">120 S.Ct. 673</a></span>, <span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">145 L.Ed.2d 570</a></span> (2000) (though a relevant consideration, “presence in an area of expected criminal activity, standing alone, is not enough to support a reasonable, particularized suspicion that the person is committing a crime”). In our present society, the demographics of those who reside in high crime neighborhoods often consist of racial minorities and individuals disadvantaged by their social and economic circumstances. To conclude that mere presence in a high crime area at night is sufficient justification for detention by law enforcement is to accept <em>carte blanche </em>the implicit assertion that Fourth Amendment protections are reserved only for a certain race or class of people. We denounce such an assertion.</p>
<p id="b566-5">IV.</p>
<p id="b566-6">The facts of this case give us cause to pause and ponder the slow systematic erosion of Fourth Amendment protections for a certain demographic. In the words of Dr. Martin Luther King, Jr., we are reminded that “we are tied together in a single garment of destiny, caught in an inescapable network of mutuality,” that our individual freedom is inextricably bound to the freedom of others. Thus, we must ensure that the Fourth Amendment rights of <em>all </em>individuals are protected.</p>
<p id="b566-7">Viewed in their totality, all the factors recited by the Government fail to amount to a reasonable suspicion justifying Black’s seizure, and the district court erred in denying the motion to suppress. Therefore, we reverse the district court’s ruling, and vacate Black’s conviction and sentence.</p>
<p id="b566-9">
<em>REVERSED AND VACATED</em>
</p>
<footnote label="1">
<p id="b559-8">. It is unclear when the seventh officer, Officer Harris, arrived at the scene.</p>
</footnote>
<footnote label="2">
<p id="b560-8">. We note that Officer Zastrow's testimony that the other men had no physical identification is contrary to Officer Strayer’s testimony that he obtained physical ID from Troupe and Moses.</p>
</footnote>
<footnote label="3">
<p id="b561-12">. The Government argues that in determining whether a seizure occurred, we should apply the "force or submission” standard set forth in <em>Hodari D., </em>where the Supreme Court stated, “[a]n arrest requires either physical force ... or, where that is absent, submission to the assertion of authority.” <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#626" aria-description="Citation for case: California v. Hodari D.">499 U.S. at 626</a></span>, <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/" aria-description="Citation for case: California v. Hodari D.">111 S.Ct. 1547</a></span> (emphasis omitted). The Government intends that in applying <em>Hodari D., </em>we would reach the conclusion that Black was seized only when Officer Zastrow exerted physical force by grabbing Black's bicep. In <em>Brendlin v. California, </em>the Supreme Court clarified <em>Hodari D., </em>stating that "[w]hen the actions of the police do not show an unambiguous intent to restrain or when an individual’s submission to a show of governmental authority takes the form of passive acquiescence,” <em>Hodari D.’s </em>force or submission test yields to <em>Mendenhall’s </em>free to leave, totality of the circumstances test. <span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/#255" aria-description="Citation for case: Brendlin v. California">551 U.S. 249, 255</a></span>, <span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">127 S.Ct. 2400</a></span>, <span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">168 L.Ed.2d 132</a></span> (2007). Here, we find that at the time the officers arrived and seized Troupe’s gun, their actions did not convey an unambiguous intent to restrain Black, and Black’s submission to the officers' authority was in essence passive acquiescence, and thus, <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>, </em>as opposed to <em>Hodari D. </em>applies.</p>
</footnote>
<footnote label="4">
<p id="b563-9">. We believe the collective-knowledge doctrine issue raised in this case is fully addressed by our decision in <em>United States v. Massenburg, </em><span class="citation" data-id="223188"><a href="/opinion/223188/united-states-v-massenburg/#492" aria-description="Citation for case: United States v. Massenburg">654 F.3d 480, 492</a></span> (4th Cir.2011), and see no need to further address it.</p>
</footnote>
<footnote label="5">
<p id="b563-10">. The other factors the district court recited as establishing reasonable suspicion — that Black looked nervous as his companions were frisked; walked away from the scene after he was told not to; left his ID behind; and said he was going home but walked towards the apartment complexes he did not live in — are irrelevant because they occurred after Black was seized.</p>
</footnote>
<footnote label="6">
<p id="b563-14">.Both parties are in accord, and we agree, that the district court erred in finding that the officers saw the vehicle pull into the gas station. This finding is unsupported by the officers’ own testimonies.</p>
</footnote>
</opinion>
```

---
