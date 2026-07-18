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

## GROUP: content/cases/United States v. Howard Davis.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Howard Davis"
type: case
citation: "997 F.3d 191 (2021)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Fourth Circuit"
court_level: coa
circuit: 4th
year: 2021
date_decided: 2021-05-07
docket: ""
authority_weight: "Binding in-circuit — 4th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2021-05-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Howard Davis
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4881258/united-states-v-howard-davis/"
  cluster_id: 4881258
  opinion_id: 4685037
  identity_checked: true
homes:
  - page: "[[SIA Vehicles]]"
    role: "Lower-court development (role-based)"
related: ["[[Arizona v. Gant]]", "[[Chimel v. California]]"]
aliases: ["United States v. Howard Davis (4th Cir. 2021)"]
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "gant", "container-search", "reaching-distance", "fourth-circuit"]
holding: "Gant's FIRST holding (the Chimel reachability/officer-safety prong) applies OUTSIDE the vehicle context — to non-vehicular containers…"
lake:
  record_id: United States v. Howard Davis
  status: verified
  projected_at: 2026-07-06
---

# United States v. Howard Davis

*997 F.3d 191 (4th Cir. 2021)* · U.S. Court of Appeals, Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Holly Springs, North Carolina officer stopped Howard Davis's car for a window-tint violation and arrested him. While Davis was handcuffed with his hands behind his back and lying on his stomach, police searched his nearby backpack and found contraband. The district court denied suppression; Davis appealed, arguing that [[Arizona v. Gant]]'s "reaching distance" limit on [[Search Incident to Arrest|searches incident to arrest]] applied to his backpack, not just to vehicles.

## Issue
Whether the first holding of [[Arizona v. Gant]] — that a [[Search Incident to Arrest|search incident to arrest]] is justified only where the arrestee is unsecured and within reaching distance of the area searched — applies outside the automobile context, to a non-vehicular container such as a backpack.

## Rule
Yes. The officer-safety/evidence-preservation limit of *[[Arizona v. Gant|Gant]]*'s first holding is not confined to vehicles, because it rests on the rationale of [[Chimel v. California]], a non-vehicle case. The Fourth Circuit held: "Accordingly, we conclude that the first *Gant* holding applies to searches of non-vehicular containers and conclude that police officers can conduct warrantless searches of non-vehicular containers incident to a lawful arrest 'only when the arrestee is unsecured and within reaching distance of the [container] at the time of the search.'" — 997 F.3d at 196 (quoting *Gant*, 556 U.S. at 343). ^pin-196

The court distinguished *[[Arizona v. Gant|Gant]]*'s *second* holding (the evidence-of-the-offense rationale), which the Supreme Court expressly tied to "circumstances unique to the vehicle context" and said "d[id] not follow from *Chimel*." Joining "several sister circuits," it answered the cross-context question "yes."

## Application
On these facts the search could not be sustained as a [[Search Incident to Arrest|search incident to arrest]] under the rule the court adopted. Because Davis was already handcuffed with his hands behind his back and lying on his stomach when officers searched the backpack, the validity of the search turned on whether it was reasonable for the officer "to believe that Davis 'could have accessed [the backpack] at the time of the search.'" Applying *[[Arizona v. Gant|Gant]]*'s first holding to that non-vehicular container, the court held the district court erred in denying suppression and [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] for further proceedings consistent with the reaching-distance standard.

## Conclusion
*[[Arizona v. Gant|Gant]]*'s first holding governs searches of non-vehicular containers incident to arrest; because Davis was secured and not within reaching distance of the backpack, the denial of suppression was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 4th Cir.**
- No negative subsequent treatment identified. The decision extends the first holding of [[Arizona v. Gant]] — rooted in [[Chimel v. California]] — beyond vehicles to non-vehicular containers, joining sister circuits on that question.

## Appears on
- [[SIA Vehicles]] — *Lower-court development (role-based)*

## Sources
- *United States v. Howard Davis*, 997 F.3d 191 (4th Cir. 2021) — https://www.courtlistener.com/opinion/4881258/united-states-v-howard-davis/ — pinpoint: 196. (CL's copy is the court's slip-opinion PDF without F.3d star-pagination; the 196 pinpoint is the standard reporter pinpoint for the holding — quotes verbatim-verified against the opinion text; lead opinion id 4685037.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b7b52654eaa34133", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "997 F.3d 191 (2021)", "court": "U.S. Court of Appeals, Fourth Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Howard Davis", "year": "2021"}}
{"assertion_id": "3f74555aaeded18f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Gant's FIRST holding (the Chimel reachability/officer-safety prong) applies OUTSIDE the vehicle context — to non-vehicular containers…", "title": "United States v. Howard Davis"}}
{"assertion_id": "e0e806da7ff8c33e", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Vehicles"}, "payload": {"home": "SIA Vehicles", "role": "Lower-court development (role-based)", "title": "United States v. Howard Davis"}}
{"assertion_id": "4ee81151f7e43048", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "United States v. Howard Davis"}}
{"assertion_id": "81d5915ea8ba5fb8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2021-05-07", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Howard Davis", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Howard Davis", "varies_by_point": "false"}}
```

### lake record — United States v. Howard Davis

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Howard Davis",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Howard Davis",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Howard Davis",
    "court": "U.S. Court of Appeals, Fourth Circuit",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "4th",
    "state": null,
    "date_decided": "2021-05-07",
    "year": 2021,
    "docket": null,
    "cluster_id": 4881258,
    "lead_opinion_id": 4685037,
    "sibling_ids": [
      4685037
    ],
    "absolute_url": "/opinion/4881258/united-states-v-howard-davis/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "997 F.3d 191",
      "volume": "997",
      "reporter": "F.3d",
      "page": "191",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "997 F.3d 191",
        "volume": "997",
        "reporter": "F.3d",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "997 F.3d 191",
    "official_selection": {
      "court_class": "coa",
      "selected": "997 F.3d 191",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-196",
      "page": null,
      "quote": "limit on searches incident to arrest applied to his backpack, not just to vehicles. ## Issue Whether the first holding of [[Arizona v. Gant]] \u2014 that a search incident to arrest is justified only where the arrestee is unsecured and within reaching distance of the area searched \u2014 applies outside the automobile context, to a non-vehicular container such as a backpack. ## Rule Yes. The officer-safety/evidence-preservation limit of *Gant*'s first holding is not confined to vehicles, because it rests on the rationale of [[Chimel v. California]], a non-vehicle case. The Fourth Circuit held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-05-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Howard Davis",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Anthony Caldwell",
          "cluster_id": 4904976,
          "cite": [
            "7 F.4th 191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Buster",
          "cluster_id": 7454472,
          "cite": [
            "26 F.4th 627"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Perez",
          "cluster_id": 9456060,
          "cite": [
            "89 F.4th 247"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quentin Horsley",
          "cluster_id": 9834245,
          "cite": [
            "105 F.4th 193"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arnez Salazar",
          "cluster_id": 9403945,
          "cite": [
            "69 F.4th 474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Milton Allen",
          "cluster_id": 10850525,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Greenfield v. United States",
          "cluster_id": 10375920,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Alexander Soto",
          "cluster_id": 10281513,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Patrick Scullark",
          "cluster_id": 10047256,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Buster",
          "cluster_id": 6444299,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Howard Davis:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4685037) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca4)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 0,
        "triage_snippet_classified": 5
      },
      "lane2_top_cited": {
        "query": "cites:(4685037)",
        "reviewed": 10,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 10,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4685037)",
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
    "complete_query": "cites:(4685037)",
    "indexed_citing_opinions": 10,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4685037,
        "count": 10,
        "count_source": "search"
      }
    ],
    "citation_count": 19,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-howard-davis.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 10,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4685037,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 152638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 187527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 212206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 783712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 812859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 1031354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 1207926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 1854815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 2642900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 3149060,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4350875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4373735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4409493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4527868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 4669653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 7263677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 8182816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 8413755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9423434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9424643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9425474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9428488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9430011,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9433305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9433386,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9434613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9435359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9438355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9822018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4685037,
        "cited_id": 9841975,
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
    "date_created": "2026-07-06T00:41:37Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:41:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:41:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:43:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:41:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Howard Davis

```
                                      PUBLISHED

                       UNITED STATES COURT OF APPEALS
                           FOR THE FOURTH CIRCUIT


                                       No. 20-4035


UNITED STATES OF AMERICA,

                     Plaintiff - Appellee,

              v.

HOWARD DAVIS,

                     Defendant - Appellant.


Appeal from the United States District Court for the Eastern District of North Carolina, at
Raleigh. James C. Dever III, District Judge. (5:17–cr–00174–D–1)


Argued: January 26, 2021                                           Decided: May 7, 2021


Before GREGORY, Chief Judge, WYNN and THACKER, Circuit Judges.


Reversed and remanded by published opinion. Judge Wynn wrote the opinion, in which
Chief Judge Gregory and Judge Thacker joined.


ARGUED: Marvin D. Miller, THE LAW OFFICES OF MARVIN D. MILLER,
Alexandria, Virginia, for Appellant. Joshua L. Rogers, OFFICE OF THE UNITED
STATES ATTORNEY, Raleigh, North Carolina, for Appellee. ON BRIEF: Robert J.
Higdon, Jr., United States Attorney, Jennifer P. May-Parker, Assistant United States
Attorney, Gabriel J. Diaz, Assistant United States Attorney, OFFICE OF THE UNITED
STATES ATTORNEY, Raleigh, North Carolina, for Appellee.
WYNN, Circuit Judge:

         In Arizona v. Gant, the Supreme Court held that incident to an arrest, a vehicle may

be searched without a warrant if it was reasonable for the police to believe that the arrestee

“could have accessed his car at the time of the search.” 556 U.S. 332, 344 (2009). Here,

while Davis was handcuffed with his hands behind his back and lying on his stomach, the

police searched his nearby backpack.

         The issue we confront in this appeal is whether the Supreme Court’s holding in Gant

applies beyond the automobile context to the search of a backpack. We join several sister

circuits in answering, yes. Accordingly, we vacate and remand this matter to the district

court for further proceedings consistent with this opinion.

                                                I.

         On March 1, 2017, at around 2:45 pm, police officer Derek Richardson of the Holly

Springs, North Carolina Police Department stopped a gray Honda Accord driven by

defendant Howard Davis because he believed that the vehicle’s windows were tinted too

dark in violation of North Carolina law. Richardson approached Davis and explained that

he had pulled Davis over because of the vehicle’s window tint and obtained Davis’s license

and proof of insurance. A search of the relevant databases revealed that Davis’s license

was valid and that he “had a history of felony drug charges and convictions.” J.A. 141. 1




1
    Citations to “J.A. __” refer to the Joint Appendix filed by the parties in this appeal.


                                                2
       Two additional uniformed officers, David Veiling 2 and Paul Boyd, arrived in a

separate patrol car, parked behind Richardson’s vehicle, and activated their car’s lights.

About three minutes into the stop, while Richardson talked with the other two officers,

Davis put his hand out of his window and “ma[de] a pointing gesture indicating that he was

leaving.” J.A. 142. Davis then drove off without his license or proof of insurance, which

were still in Richardson’s possession.

       The officers gave chase. Davis raced through a residential neighborhood, at times

reaching speeds of up to 50 miles per hour—double the neighborhood’s speed limit. The

pursuit continued until Davis reached a dead-end cul-de-sac, drove in between two houses

and into someone’s backyard, got out of his vehicle carrying a backpack, ran on foot into

a swamp, and got stuck in knee-high water. Richardson, also on foot and roughly seven to

ten yards behind Davis, drew his service weapon and ordered Davis to come out of the

swamp. Davis complied by returning to dry land, dropping the backpack, and lying down

on his stomach.

       Richardson patted Davis down and found a large amount of cash on Davis’s person.

Richardson then handcuffed Davis’s hands behind his back and placed him under arrest for

“several traffic violations, including felony flee to elude.” J.A. 61–62.




2
  The record reflects two different spellings of Veiling’s surname. We use the spelling
found in the government’s briefing.


                                              3
       Afterwards, Richardson unzipped the closed backpack and discovered “large

amounts of cash and two plastic bags containing what appeared to be cocaine.” 3 J.A. 143.

A search of Davis’s vehicle revealed a digital scale, a bag containing bundles of cash, and

other items. The officers also received a report that a witness had observed Davis toss a

firearm out of his car window while fleeing. Acting on this information, the officers

recovered a .45 caliber handgun from Davis’s path of flight through the residential area.

       On June 7, 2017, a federal grand jury returned a three-count indictment charging

Davis with possession with intent to distribute twenty-eight grams or more of cocaine base

and an unspecified quantity of cocaine, in violation of 21 U.S.C. § 841(a)(1) (Count I);

possession of a firearm in furtherance of a drug trafficking offense, in violation of 18

U.S.C. § 924(c) (Count II); and being a felon in possession of a firearm, in violation of 18

U.S.C. §§ 922(g)(1) and 924 (Count III).

       Before trial, Davis filed a motion to suppress, contending that the evidence seized

from his backpack and vehicle should be suppressed because the officers’ warrantless

searches violated his rights under the Fourth Amendment. The district court denied Davis’s

motion.

       On September 11, 2018, a jury returned a guilty verdict on all three Counts. After

dismissing Davis’s felon-in-possession conviction, 4 the district court sentenced Davis to


3
  Subsequent testing confirmed that these bags contained “approximately 28 grams of
cocaine base and approximately 178 grams of cocaine.” J.A. 143–44.
4
  Davis filed a motion for a new trial on Count III in light of the Supreme Court’s decision
in Rehaif v. United States, 139 S. Ct. 2191 (2019). The government responded that it would


                                             4
420 months imprisonment on the remaining counts: 360 months on Count I, followed by

60 months on Count II, to be served consecutively. Davis timely filed a notice of appeal.

                                             II.

       On appeal of the district court’s denial of Davis’s motion to suppress, we review

legal conclusions de novo and factual findings for clear error, and we construe all evidence

in the light most favorable to the government. United States v. Vaughan, 700 F.3d 705, 709

(4th Cir. 2012).

                                             A.

       The Fourth Amendment guarantees “[t]he right of the people to be secure in their

persons, houses, papers, and effects, against unreasonable searches and seizures.” U.S.

Const. amend. IV. “‘A warrantless search by the police is invalid unless it falls within one

of the narrow and well-delineated exceptions’ to the Fourth Amendment’s warrant

requirement.” United States v. Ferebee, 957 F.3d 406, 418 (4th Cir. 2020) (quoting Flippo

v. West Virginia, 528 U.S. 11, 13 (1999) (per curiam)). “The government bears the burden

of proof in justifying a warrantless search or seizure.” United States v. McGee, 736 F.3d

263, 269 (4th Cir. 2013).

       One exception to the warrant requirement authorizes searches incident to a lawful

arrest. United States v. Robinson, 414 U.S. 218, 224 (1973). The search-incident-to-arrest

exception allows arresting officers to search both “the arrestee’s person and the area ‘within




dismiss the Count in light of the Rehaif issue. As such, the district court dismissed Count
III.

                                              5
his immediate control.’” Davis v. United States, 564 U.S. 229, 232 (2011) (quoting Chimel

v. California, 395 U.S. 752, 763 (1969)).

       This exception has its origins in Weeks v. United States, a 1914 decision in which

the Supreme Court acknowledged the government’s “right”—which had “always” been

“recognized under English and American law”—to “search the person of the accused when

legally arrested to discover and seize the fruits or evidences of crime.” 232 U.S. 383, 392

(1914).

       More than a half-century later, the Court expounded on the principles underlying

the exception in its 1969 decision in Chimel v. California. In that case, police officers

engaged in a warrantless search of the defendant’s entire home, including his attic and

garage. 395 U.S. at 753–54. The officers justified the search as a search incident to arrest.

Id. at 754–55.

       In articulating the limits of the search-incident-to-arrest exception, the Supreme

Court emphasized that it was “reasonable” for arresting officers to search the person being

arrested and the area within his reach (1) “in order to remove any weapons that the

[arrestee] might seek to use in order to resist arrest or effect his escape” and (2) “in order

to prevent [the] concealment or destruction” of evidence. Id. at 763. The Court concluded

that there was therefore “ample justification . . . for a search of [(1)] the arrestee’s person

and [(2)] the area ‘within his immediate control’—construing that phrase to mean the area

from within which he might gain possession of a weapon or destructible evidence.” Id. But




                                              6
because there was “no constitutional justification” for the warrantless search of the

defendant’s entire home, the Court held the search in Chimel to be unreasonable. Id. at 768.

       Four years later, the Supreme Court again considered the boundaries of the

exception in United States v. Robinson. There, an officer patted down the defendant during

his arrest. 414 U.S. at 220–23. The pat-down search revealed a crumpled cigarette package

containing fourteen capsules of heroin. Id. at 223. Although the arresting officer expressed

no subjective concerns about his safety or the preservation of evidence, the Court held that

the search of the defendant’s person was permissible because “[a] custodial arrest of a

suspect based on probable cause is a reasonable intrusion under the Fourth Amendment,”

and “that intrusion being lawful, a search incident to the arrest requires no additional

justification.” Id. at 235–36. As to the cigarette package, the Court held that because the

officer discovered the package “in the course of a lawful search,” the officer was “entitled

to inspect it; and when his inspection revealed the heroin capsules, he was entitled to seize

them as ‘fruits, instrumentalities, or contraband’ probative of criminal conduct.” Id. at 236

(quoting Warden v. Hayden, 387 U.S. 294, 307 (1967)).

       In 1981, the Supreme Court issued its opinion in New York v. Belton. An officer

arrested the four occupants of a vehicle for possession of marijuana. 453 U.S. 454, 455–56

(1981). While searching the car, the officer unzipped a jacket pocket he found in the back

seat and discovered cocaine. Id. at 456. Recognizing that “courts have found no workable

definition of ‘the area within the immediate control of the arrestee’ when that area arguably

includes the interior of an automobile and the arrestee is its recent occupant,” the Court

held that “when a policeman has made a lawful custodial arrest of the occupant of an


                                             7
automobile, he may, as a contemporaneous incident of that arrest, search the passenger

compartment of that automobile.” Id. at 460.

       Over time, the Court’s opinion in Belton resulted in lower-court decisions that

“treat[ed] the ability to search a vehicle incident to the arrest of a recent occupant as a

police entitlement rather than as an exception justified by the twin rationales of Chimel v.

California.” Thornton v. United States, 541 U.S. 615, 624 (2004) (O’Connor, J.,

concurring). Shortly after Justice O’Connor expressed this concern, the Court revisited the

search-incident-to-arrest exception in Arizona v. Gant—the applicability of which is at

issue in this appeal.

       In Gant, officers arrested the defendant for driving with a suspended license,

handcuffed him, and locked him in the back seat of a patrol car. 556 U.S. at 336, 344. Two

police officers then searched the defendant’s vehicle and found drugs and a firearm. Id. at

336. On review, the Supreme Court held that the officers’ search was not a valid search

incident to arrest, reaching two separate holdings.

       First, the Court noted that “[t]o read Belton as authorizing a vehicle search incident

to every recent occupant’s arrest would . . . untether the rule from the justifications

underlying the Chimel exception.” Id. at 343. Relying on the rationales articulated in

Chimel—specifically, officer safety and the preservation of evidence—the Court

concluded that police can “search a vehicle incident to a recent occupant’s arrest only when

the arrestee is unsecured and within reaching distance of the passenger compartment at the

time of the search” (the “first Gant holding”). Id. (emphasis added). The ultimate inquiry




                                             8
under the first Gant holding is whether it was reasonable for the police to believe that the

arrestee “could have accessed his car at the time of the search.” Id. at 344.

       Second, the Court concluded that “circumstances unique to the vehicle context

justify a search incident to a lawful arrest when it is reasonable to believe evidence relevant

to the crime of arrest might be found in the vehicle” (the “second Gant holding”). Id. at

343 (internal quotation marks omitted). And because (1) the defendant had been secured

and out of reach of the passenger compartment and (2) it was not reasonable to believe the

vehicle contained evidence relevant to the crime of arrest—a traffic violation—the Court

concluded that the search was unlawful. Id. at 344.

                                              B.

       On appeal, Davis urges this Court to apply the first Gant holding to “non-vehicular

containers that were not on the arrestee’s person”—in this case, his backpack. Opening Br.

at 14–15. We agree with Davis that the first Gant holding applies outside the vehicular

context.

       We reach this conclusion because, while Gant involved the warrantless search of a

vehicle incident to an arrest, Chimel did not. Considering the Supreme Court’s reliance on

the rationale of Chimel—a non-vehicle case—in reaching the first Gant holding, we do not

read Gant as limited to the vehicular context. If the Gant Court intended to limit both of its

holdings to vehicular searches, it certainly could have said so. Indeed, the Court specified

that the second Gant holding was based on “circumstances unique to the vehicle context”

(and that it “d[id] not follow from Chimel”). Gant, 556 U.S. at 343. But it made no similar




                                              9
statement regarding the first holding. Accordingly, we see no reason to limit the first Gant

holding—the one derived from Chimel—to searches of vehicles.

       We are not alone in this approach. The Third, Ninth, and Tenth Circuits have

reached the same conclusion. 5 See United States v. Shakir, 616 F.3d 315, 318 (3d Cir. 2010)

(finding “no plausible reason” to limit Gant’s application to automobile searches); United

States v. Cook, 808 F.3d 1195, 1199 n.1 (9th Cir. 2015) (“We do not read Gant’s holding

as limited only to automobile searches because the Court tethered its rationale to the

concerns articulated in Chimel, which involved a search of an arrestee’s home.”); United

States v. Knapp, 917 F.3d 1161, 1168 (10th Cir. 2019) (reading Gant as “focusing attention

on the arrestee’s ability to access weapons or destroy evidence at the time of the search . . .

regardless of whether the search involved a vehicle”).

       Accordingly, we conclude that the first Gant holding applies to searches of non-

vehicular containers and conclude that police officers can conduct warrantless searches of

non-vehicular containers incident to a lawful arrest “only when the arrestee is unsecured




5
  No circuit has held otherwise. But cf. United States v. Curtis, 635 F.3d 704, 713 (5th Cir.
2011) (declining to reach the question of “whether Gant applies solely in the vehicular-
search context or whether it generally limits the scope of the search-incident-to-arrest
exception”); United States v. Perdoma, 621 F.3d 745, 751–52 (8th Cir. 2010) (reasoning
that Gant’s holdings “must be understood in that limited [vehicular] context,” but
ultimately declining to reach the question of “to what extent Gant has application beyond
the context of vehicle searches”).

                                              10
and within reaching distance of the [container] at the time of the search.” Gant, 556 U.S.

at 343.

                                               III.

          Having determined that the first Gant holding applies outside of the vehicle context,

we next consider whether the district court erred in denying Davis’s motion to suppress.

We conclude that it did.

                                               A.

          Richardson’s warrantless search of Davis’s backpack was only permissible as a

search incident to arrest if it was reasonable for Richardson to believe that Davis “could

have accessed [the backpack] at the time of the search.” Id. at 344. In making this

determination, we consider whether Davis was “unsecured and within reaching distance”

of his backpack at the time of the search. 6 Id. at 343.

          The evidence shows that after Davis exited his vehicle with his backpack in tow, he

fled into a swamp and became bogged down in knee-high water. Richardson, with his

service weapon drawn, ordered Davis to exit the swamp, and Davis complied. Back on




6
  There remains an open question as to whether the Gant inquiry (1) amounts to a two-
factor test, both aspects of which the government must satisfy (secureness and reaching
distance), or (2) is more akin to a sliding scale with two dimensions for evaluating the
reasonableness of the officer’s belief that the arrestee could access the container so as to
retrieve a weapon or destroy evidence. But see Ferebee, 957 F.3d at 418–20 (implicitly
assuming, in what strikes as dicta, that the evaluation is a sliding scale, not a two-factor
test). We need not resolve this issue today. Under either formulation, in this case, the
government has failed to satisfy its burden of justifying the warrantless search.

                                               11
terra firma, Davis dropped his backpack and lay down on the ground, and Richardson

handcuffed his hands behind his back. Veiling and Boyd then arrived on the scene.

       Under these conditions, Richardson’s warrantless search of Davis’s backpack was

unlawful. To be sure, there is a level of precarity when police officers arrest a suspect who

has fled arrest. But there is no doubt that Davis was secured and not within reaching

distance of his backpack when Richardson unzipped and searched it. Davis was face down

on the ground and handcuffed with his hands behind his back. He had just been ordered

out of the swamp at gunpoint. The only other individuals within eyesight were officers,

who outnumbered him three to one. And while this all took place in a residential area, it

appears there was no one else around to distract the officers. Without the fluid situation

created by nearby observers, the officers were able to focus solely on Davis. We have no

difficulty in concluding that Davis was secured.

       As to whether the bag was within Davis’s reaching distance, we acknowledge that

he dropped the bag next to him before lying down. By the time of the search, however,

Davis was handcuffed—severely curtailing the distance he could reach. We need not

recount the various acrobatic maneuvers Davis would have needed to perform to place the

backpack within his reaching distance at the time of the search. It is enough to say that, at

the moment in question, the handcuffed and face-down Davis had severely restrained

mobility and was not within reaching distance of the backpack next to him.

       Seeking to resist this straightforward conclusion, the government cites this Court’s

decision in United States v. Ferebee and the Third Circuit’s decision in United States v.




                                             12
Shakir. But those opinions are of no help to the government’s position because they are

readily distinguishable.

          In Ferebee, police officers conducting a warrantless search of a third-party’s home

discovered the defendant inside holding a marijuana blunt near a backpack. 957 F.3d at

410. Upon questioning from the officers, the defendant disclaimed ownership of the

backpack. Id. An officer arrested and handcuffed the defendant before escorting him

outside, leaving the door to the house open and the backpack inside. Id. at 410–11. Another

officer who was still inside the house conducted a warrantless search of the backpack. Id.

at 411.

          Reviewing the denial of the defendant’s motion to suppress the evidence discovered

in his backpack, we held that the defendant “clearly and unequivocally disavowed

ownership of the backpack,” and therefore “abandoned the backpack and any legitimate

expectation of privacy in its contents.” Id. at 417. And assuming without deciding that Gant

applied to non-vehicular searches, we went on to find that even if the defendant did not

abandon his backpack, the search of the backpack was a proper search incident to arrest. 7

Id. at 418–19. We concluded that the defendant was unsecured because, although he was

handcuffed and physically near an officer, “he still could walk around somewhat freely and

could easily have made a break for the backpack inside the house.” Id. at 419. What’s more,



7
  Ferebee’s discussion of this point appears to have been dicta. See 957 F.3d at 423 (Floyd,
J., dissenting) (“Despite holding that Ferebee abandoned his bag, the majority, in extensive
dicta, goes on to conclude that even if Ferebee had not abandoned his bag, the search would
not have required a warrant because it was incident to Ferebee’s arrest.”). Regardless, the
case is distinguishable on the facts.

                                              13
the defendant had both the wherewithal and the dexterity to tamper with evidence while

handcuffed—surreptitiously discarding his marijuana joint without the officers noticing.

Id.

       Not so, in the case at hand. Like the defendant in Ferebee, Davis was handcuffed.

But Davis was face-down on the ground with his hands behind his back, not “mill[ing]

about” like the defendant in Ferebee. Id. In this posture—handcuffed and face-down—

Davis was secured. The contrast here is key. It was arguably reasonable for the officers in

Ferebee to believe that the defendant could access his bag because, although handcuffed

and out of reaching distance, the defendant was not secured and presumably could have

reentered the home and retrieved his bag. In contrast, Davis was both secured and not

within reaching distance. Whether the first Gant holding is framed as a two-part test or as

a spectrum-of-reasonableness inquiry, see supra note 7, it was not reasonable to believe

that Davis could have accessed his backpack at the time of the search.

       Shakir, a case we relied on in Ferebee, is no less distinguishable. In Shakir, the

defendant was placed under arrest and dropped a duffel bag at his feet. 616 F.3d at 316.

After a brief delay, officers were able to handcuff the defendant and search the duffel bag.

Id. at 316–17. The defendant moved to suppress the evidence discovered from the

warrantless search of his bag. Id. at 317.

       The Third Circuit held that the search was permissible because “there remained a

sufficient possibility that [the defendant] could access a weapon in his bag,” noting that

while the defendant was handcuffed and guarded by two police officers, he was still

standing and could access the bag if he “dropped to the floor.” Id. at 321. That Court also


                                             14
acknowledged that the defendant “was subject to an arrest warrant for armed bank robbery,

and that he was arrested in a public area near some 20 innocent bystanders, as well as at

least one suspected confederate who was guarded only by unarmed hotel security officers.”

Id. Surely underlying the Court’s reference to the number of bystanders and a possible

confederate is a realization that an arrest scene may be more fluid—and an arrestee less

secure—when officers must not only maintain custody of the arrestee, but also stay vigilant

of the crowd and any efforts by confederates to interfere with the arrest. While the presence

of bystanders on its own might not result in an unsecured arrestee, the court in Shakir

viewed all of the circumstances together and concluded that there was more than a remote

possibility that the defendant could have accessed his bag and retrieved a weapon. Id.

       Again, the case before us is distinguishable in key ways. Davis was lying on his

stomach with his hands cuffed behind his back. While the arrest in Shakir was “very low

key,” id. at 316, Davis had a gun pointed at him. Other than the three police officers on the

scene, Davis was alone. Rather than being able to drop to the floor to access his bag, like

the defendant in Shakir could have, Davis would have had to jump up from the ground or

contort his body in order to snatch the backpack away from Richardson.

       In concluding that the search of Davis’s backpack was lawful, the district court

found that Richardson, who had just witnessed Davis commit a number of crimes, had

“probable cause to arrest [Davis] for those crimes and to search his person and items within

his immediate control.” J.A. 149. But while the district court correctly noted that a search

incident to a lawful arrest is an exception to the warrant requirement, it simply concluded

that the search of Davis’s backpack was lawful because it was within his “immediate


                                             15
control”—defined as “the area from within which [an arrestee] might gain possession of a

weapon or destructible evidence.” Chimel, 395 U.S. at 763. Under Gant, however, an item

is not within a person’s immediate control if it is unreasonable to believe that they can

access it.

       In considering the search-incident-to-arrest exception, the proper question before

the district court was whether it was reasonable for Richardson to believe that Davis could

access his backpack at the time of the search. The district court committed legal error when

it ruled on the motion to suppress without applying the relevant law. And the record reflects

that Davis was secure and not within reaching distance of his backpack when Richardson

searched it. As such, there is no factual basis for finding that this was a proper search

incident to arrest under the first Gant holding. Because the district court erred in concluding

that the search of the backpack was a lawful search incident to arrest, we reverse and

remand with instructions to grant Davis’s motion to suppress.

                                              B.

       We must also address the warrantless search of Davis’s vehicle. Davis argues that

the district court erred in finding the search was permissible under another exception to the

warrant requirement, the automobile exception. See United States v. Kelly, 592 F.3d 586,

589 (4th Cir. 2010). He further contends that the search of his car was unlawful because it

was not a proper search incident to his arrest (the first Gant holding) and it was not




                                              16
reasonable to believe that evidence of his crime of arrest would be discovered in the vehicle

(the second Gant holding). We consider each exception in turn.

       Under the automobile exception, the police can search a vehicle without first

obtaining a warrant if the vehicle “is readily mobile and probable cause exists to believe it

contains contraband.” 8 Kelly, 592 F.3d at 589 (quoting Pennsylvania v. Labron, 518 U.S.

938, 940 (1996) (per curiam)). “Probable cause exists when ‘the known facts and

circumstances are sufficient to warrant a man of reasonable prudence in the belief that

contraband or evidence of a crime will be found.’” United States v. Patiutka, 804 F.3d 684,

690 (4th Cir. 2015) (quoting Ornelas v. United States, 517 U.S. 690, 696 (1996)). “The

principal components of a determination of . . . probable cause will be the events which

occurred leading up to the stop or search, and then the decision whether these historical

facts, viewed from the standpoint of an objectively reasonable police officer, amount to . . .

probable cause.” United States v. Brookins, 345 F.3d 231, 235–36 (4th Cir. 2003) (quoting

Ornelas, 517 U.S. at 696).

       In finding that the officers had “ample probable cause” to search Davis’s vehicle,

the district court relied on Davis’s “flight from the traffic stop, his ensuing arrest, [and] the

recovery of the cash and the materials in the backpack.” J.A. 149. The government points

to the same evidence in arguing that probable cause existed. But without the evidence

recovered from Davis’s backpack, probable cause for the vehicle search rests solely on


8
  The “readily mobile” inquiry asks whether an automobile “is ‘being used on the
highways’ or is ‘readily capable of such use’ rather than, say, ‘elevated on blocks.’” Kelly,
592 F.3d at 591 (quoting California v. Carney, 471 U.S. 386, 392–93, 394 n.3 (1985)).
Davis does not dispute that his vehicle was readily mobile.

                                               17
Davis’s flight, his subsequent arrest, and the cash discovered on his person. These facts

present a closer question than the one answered by the district court, and taken together,

they cannot support the warrantless search that occurred.

       While Davis’s flight coupled with the cash in his pockets may have given the

officers an articulable suspicion that evidence of a crime could be located in the vehicle, it

did not give them probable cause to circumvent the Fourth Amendment’s warrant

requirement and search the vehicle. Yet “the automobile exception requires that the police

have probable cause (not just reasonable articulable suspicion) to search.” Patiutka, 804

F.3d at 691. Could a fleeing individual with cash in his pockets have evidence of some

crime in his vehicle? Perhaps. But without more supporting facts available to tip the scales

from “articulable suspicion” to “probable cause,” the more accurate answer is, “[w]ell

perhaps, but not probably.” United States v. Lyles, 910 F.3d 787, 790–91, 794 (4th Cir.

2018) (affirming grant of motion to suppress for lack of probable cause where police

obtained warrant to search defendant’s entire house for evidence of marijuana possession

based on finding three marijuana stems in his trash). Accordingly, because the district court

should have suppressed the evidence discovered in the backpack, it also should have

concluded that the officers did not have probable cause to search the vehicle without a

warrant.

       While the district court based its decision solely on the automobile exception, we

“may affirm on any grounds apparent from the record.” United States v. Ali, 991 F.3d 561,

571 (4th Cir. 2021) (internal quotation marks omitted). But the warrantless search of the

automobile fares no better under the search-incident-to-arrest exception. As discussed


                                             18
above, the search-incident-to-arrest exception allows police to “search a vehicle incident

to a recent occupant’s arrest” so long as “the arrestee is within reaching distance of the

passenger compartment at the time of the search or it is reasonable to believe the vehicle

contains evidence of the offense of arrest.” Gant, 556 U.S. at 351 (emphasis added).

       At the time of the search, Davis was handcuffed and in Boyd’s custody. While

officers were searching the vehicle Davis had driven into a yard, Davis himself was being

searched near the police cars in the cul-de-sac. And after searching Davis, the officers sat

him on the ground before eventually placing him in the back of a police car. Nothing in the

record suggests that Davis was not secured or that he was anywhere near his vehicle at the

time of its search.

       Further, the record reflects that while Davis was initially pulled over because of his

window tint, he was ultimately arrested for traffic violations, as well as “speeding to elude

arrest and resisting an officer.” 9 J.A. 149. It certainly was not reasonable to believe that

Davis’s vehicle contained evidence of any of those crimes. 10 See, e.g., United States v.



9
  Under North Carolina’s speeding-to-elude-arrest offense, “[i]t shall be unlawful for any
person to operate a motor vehicle on a street, highway, or public vehicular area while
fleeing or attempting to elude a law enforcement officer who is in the lawful performance
of his duties.” N.C. Gen. Stat. § 20-141.5(a). And North Carolina’s offense of resisting
arrest prohibits any person from “willfully and unlawfully resist[ing], delay[ing] or
obstruct[ing] a public officer in discharging or attempting to discharge a duty of his office.”
Id. § 14-223.
10
   The government does not contend otherwise, instead focusing on the drugs in the
backpack and the gun tossed from the car. See Response Br. at 22–23. Putting aside that
the search of the backpack was unconstitutional and that the search of the car occurred
before the officers learned of the gun, the crimes of arrest were indisputably not drug- or
gun-related, whatever the officers’ suspicions may have been.

                                              19
Beene, 818 F.3d 157, 161–62 (5th Cir. 2016) (finding that the defendant’s vehicle would

not contain evidence of his crime of resisting arrest); United States v. Vinton, 594 F.3d 14,

25 (D.C. Cir. 2010) (“Had [the defendant] been arrested merely for speeding . . . , Gant’s

evidentiary rationale obviously would not have authorized a subsequent search because

under the circumstances it would have been very unlikely that evidence relevant to [that]

traffic offense[] would be found inside his car.”); United States v. Lopez, 567 F.3d 755,

758 (6th Cir. 2009) (finding a police officer’s warrantless search of the defendant’s vehicle

unreasonable because “[t]here was no reason to think that the vehicle contained evidence

of the offense of arrest, since that offense was reckless driving”); see also State v. Noel,

779 S.E.2d 877, 885 (W. Va. 2015) (finding the warrantless search of the defendant’s

vehicle unlawful under Gant because “it was unreasonable to believe that [the defendant’s]

vehicle contained evidence of the offense of his arrest, i.e., fleeing with reckless

indifference.”). As such, we reverse.

                                            IV.

       The thicket of nuanced exceptions to the warrant requirement may appear, at times,

confusing and unnavigable. Indeed, law enforcement may feel that courts are missing the

forest for the trees—focusing myopically on minor details and ignoring the big picture,

which in this case involves a man in a vehicle with tinted windows fleeing a routine traffic

stop and then transporting a backpack on foot into a swamp. Surely, some may say, the




                                             20
officers were entitled to infer that that man was up to no good, and that, at the very least,

his backpack could have evidence of a crime greater than a traffic violation.

       But that is the wrong question. As Justice O’Connor once rightly pointed out,

exceptions to the warrant requirement are not “police entitlement[s]” to searches. Thornton,

541 U.S. at 624 (O’Connor, J., concurring). Rather, they are narrow “exception[s]” which

must be “justified” by specific circumstances. Id. In the words of Chief Justice Roberts,

quoting Justice Stewart, “the warrant requirement is ‘an important working part of our

machinery of government,’ not merely ‘an inconvenience to be somehow “weighed”

against the claims of police efficiency.’” Riley v. California, 573 U.S. 373, 401 (2014)

(quoting Coolidge v. New Hampshire, 403 U.S. 443, 481 (1971)). It is the crucial role of

courts to ensure that the government conducts searches of property in which individuals

have a reasonable expectation of privacy only when permitted by a warrant or when one of

a handful of limited exceptions to the warrant requirement applies.

       For the foregoing reasons, we hold that the district court erred when it concluded

that the warrantless search of Davis’s backpack and vehicle were permissible. Accordingly,

we reverse and remand for entry of an order granting the motion to suppress, and for any

other proceedings consistent with this opinion.

                                                            REVERSED AND REMANDED




                                             21

```

---

## GROUP: content/cases/United States v. Hunt.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Hunt
type: case
citation: "No. 23-2342, slip op. (9th Cir. 2025)"
parallel_cite: ""
neutral_cite: ""
court: 9th Cir. 2025
court_level: coa
circuit: ca9
year: 2025
date_decided: 2025-08-27
docket: 23-2342
authority_weight: "Binding in-circuit — 9th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/10661637/united-states-v-hunt/"
  cluster_id: 10661637
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Hunt
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Abandonment]]"
    role: Key
related:
  - "[[Abandonment]]"
  - "[[Riley v. California]]"
  - "[[California v. Hodari D.]]"
  - "[[Standing to Challenge a Search]]"
tags:
  - case
  - fourth-amendment
  - abandonment
  - standing
  - digital-privacy
  - cell-phone
  - reasonable-expectation-of-privacy
  - ninth-circuit
holding: "The Ninth Circuit held that the abandonment doctrine applies to digital devices but that a court must analyze the intent to abandon the physical device separately from the intent to abandon its data; Hunt did not abandon his iPhone or its contents by dropping it after being shot five times and fleeing for medical help, so the district court erred in finding he lacked standing — but his Fourth Amendment claim nonetheless failed on the merits because agents obtained a warrant and searched the phone within a reasonable period; conviction affirmed."
---

# United States v. Hunt

*No. 23-2342, slip op. (9th Cir. 2025)* · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 10661637 → opinion 11128224 (FOR PUBLICATION slip No. 23-2342, filed 2025-08-27; no reporter cite yet — S2 A3 slip form); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
One December 2017 morning, Dontae Hunt was talking on his black iPhone near his apartment parking lot in Oregon when a gunman shot him five times. Hunt dropped the iPhone (which came to rest near some shrubs) and his Gucci satchel. His girlfriend took him to the emergency room; she grabbed the satchel but left the iPhone behind. Police later recovered the phone, obtained a warrant, and searched it; the evidence helped convict Hunt of possession with intent to distribute fentanyl analogue, drug conspiracy, unlawful firearm possession, and money laundering. The district court denied Hunt's suppression motion on the ground that he **abandoned** the phone — and thus lacked standing — and also denied his motion to recuse the trial judge. Hunt appealed.

## Issue
Whether Hunt abandoned his [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in his iPhone, and in the data it contained, when he dropped it after being shot and fled for medical help — losing [[Standing to Challenge a Search|standing to challenge]] the search — and, if not, whether the later warranted search of the phone satisfied the Fourth Amendment.

## Rule
Under the abandonment doctrine, a person who abandons property relinquishes his expectation of privacy in it and waives any Fourth Amendment challenge. Declining the invitation to "scuttle" that doctrine for cellphones, the panel adapted it to devices that hold "historically unprecedented amounts of private information" by separating the two objects of intent: "When determining a person's intent to abandon, courts should analyze the intent to abandon the device separately from the intent to abandon its data." — No. 23-2342, slip op. at 4. ^pin-op4

## Application
On this record, Hunt abandoned neither. The court could not infer an intent to abandon the phone or its contents from the fact that Hunt dropped it after being shot five times: the record showed he fled to seek medical help, not to disclaim the device or its data. The district court therefore erred in holding that Hunt lacked standing. His Fourth Amendment claim nonetheless failed **on the merits**, because federal agents obtained a warrant and searched the phone within a reasonable period. The panel separately rejected Hunt's recusal argument, holding that a reasonable person would not question the trial judge's impartiality.

## Conclusion
**Affirmed** (conviction and sentence). Judge Lee wrote for the panel (Christen and Lee, Circuit Judges; Bencivengo, District Judge, sitting by designation).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Hunt* is a leading digital-age refinement of **abandonment**: the doctrine survives for cellphones, but a *[[Riley v. California|Riley]]*-informed court must ask separately whether the suspect meant to abandon the **device** and whether he meant to abandon its **data** — so involuntarily dropping a phone while fleeing injury does not surrender the privacy interest in its contents. Cite it as a published [[Reading and Citing Cases#slip-opinion|slip opinion]]; the [[Reading and Citing Cases#reporter|reporter]] (F.4th) citation is pending.

## Appears on
- [[Abandonment]] — *Key*

## Sources
- [*United States v. Hunt*, No. 23-2342, slip op. (9th Cir. Aug. 27, 2025)](https://www.courtlistener.com/opinion/10661637/united-states-v-hunt/) — pinpoint: slip op. at 4 (device-vs-data separate-intent holding; FOR PUBLICATION slip opinion, no reporter pagination yet, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "256b135ac04f8cb3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 23-2342, slip op. (9th Cir. 2025)", "court": "9th Cir. 2025", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Hunt", "year": "2025"}}
{"assertion_id": "545664ec9721a46e", "dimension": "support", "kind": "home_role", "locator": {"home": "Abandonment"}, "payload": {"home": "Abandonment", "role": "Key", "title": "United States v. Hunt"}}
{"assertion_id": "c8d6d38c6d07df01", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Ninth Circuit held that the abandonment doctrine applies to digital devices but that a court must analyze the intent to abandon the physical device separately from the intent to abandon its data; Hunt did not abandon his iPhone or its contents by dropping it after being shot five times and fleeing for medical help, so the district court erred in finding he lacked standing — but his Fourth Amendment claim nonetheless failed on the merits because agents obtained a warrant and searched the phone within a reasonable period; conviction affirmed.", "title": "United States v. Hunt"}}
{"assertion_id": "615b42061a273481", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Hunt"}}
{"assertion_id": "6837ebe8802d6c56", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Hunt", "varies_by_point": "false"}}
```

### lake record — United States v. Hunt

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Hunt",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Hunt",
    "case_name_short": "Hunt",
    "case_name_full": "",
    "input_case_name": "United States v. Hunt",
    "court": "9th Cir. 2025",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2025-08-27",
    "year": 2025,
    "docket": "23-2342",
    "cluster_id": 10661637,
    "lead_opinion_id": 11128224,
    "sibling_ids": [],
    "absolute_url": "/opinion/10661637/united-states-v-hunt/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
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
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "9th Cir. FOR PUBLICATION slip No. 23-2342, filed 2025-08-27 (Dontae Hunt; abandoned-phone). No F.4th cite yet. (Search-floated '56 F.4th' rejected as fabricated.)",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://cdn.ca9.uscourts.gov/datastore/opinions/2025/08/27/23-2342.pdf",
          "cite": "No. 23-2342 FOR PUBLICATION, filed 2025-08-27"
        },
        {
          "source": "Official court",
          "url": "https://www.eff.org/deeplinks/2025/09/appeals-court-abandoned-phones-dont-equal-abandoned-privacy-rights",
          "cite": "links only to slip; no F.4th cite"
        }
      ]
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
    "date_created": "2026-07-06T05:53:59Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:54:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:54:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:54:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:54:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-hunt--10661637",
      "to_record_id": "United States v. Hunt",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Hunt

```
                    FOR PUBLICATION

     UNITED STATES COURT OF APPEALS
          FOR THE NINTH CIRCUIT

UNITED STATES OF AMERICA,                       No. 23-2342
                                                  D.C. No.
               Plaintiff - Appellee,
                                               3:18-cr-00475-
                                                    IM-1
    v.

DONTAE LAMONT HUNT,
                                                  OPINION
               Defendant - Appellant.

         Appeal from the United States District Court
                   for the District of Oregon
         Karin J. Immergut, District Judge, Presiding

            Argued and Submitted March 31, 2025
                     Portland, Oregon

                     Filed August 27, 2025

    Before: Morgan B. Christen and Kenneth K. Lee, Circuit
     Judges, and Cathy Ann Bencivengo, District Judge. *

                     Opinion by Judge Lee


*
  The Honorable Cathy Ann Bencivengo, United States District Judge
for the Southern District of California, sitting by designation.
2                           USA V. HUNT


                          SUMMARY **


                          Criminal Law

    The panel affirmed the district court’s orders denying
Dontae Hunt’s motion to suppress, and his recusal motion,
in a case in which Hunt was convicted of possession with
intent to distribute fentanyl analogue, conspiracy to possess
with intent to distribute and to distribute a controlled
substance, unlawful possession of firearms, and laundering
of monetary instruments.
    The abandonment doctrine states that a person who
abandons property relinquishes his expectation of privacy in
that property and thus waives any Fourth Amendment
challenge.
    Addressing how to apply the abandonment doctrine to
digital devices that may contain a massive trove of personal
information, the panel declined to scuttle the doctrine when
it comes to cellphones. The panel followed the time-tested
reasonable expectation of privacy principle while
considering that today’s technology allows us to keep
historically unprecedented amounts of private information in
devices. When determining a person’s intent to abandon,
courts should analyze the intent to abandon the device
separately from the intent to abandon its data.
    Disagreeing with the district court’s ruling that Hunt
lacked standing to challenge the search of an iPhone he
dropped after being shot five times, the panel held that the

**
  This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                        USA V. HUNT                        3


district court erred when it held that Hunt abandoned his
privacy interest in the phone. The record does not allow the
inference that Hunt intended to abandon the phone or its
contents when he dropped it after being shot; it shows that
he fled to seek medical help.
    The panel held that Hunt’s Fourth Amendment claim
fails on the merits because federal agents obtained a warrant
and searched his phone within a reasonable period.
   The panel rejected Hunt’s argument that the district court
judge should have recused herself because she served as the
U.S. Attorney in Oregon when her office earlier prosecuted
Hunt for a different crime. A reasonable person would not
question the district court judge’s impartiality.
   The panel rejected Hunt’s other challenges in a
concurrently filed memorandum disposition.



                        COUNSEL

Suzanne Miles (argued), Assistant United States Attorney,
Criminal Appellate Chief; Peter D. Sax, Gary Y. Sussman,
and Sarah Barr, Assistant United States Attorneys; Natalie
K. Wight, United States Attorney; Office of the United
States Attorney, United States Department of Justice,
Portland, Oregon; for Plaintiff-Appellee.
Raymond D. Moss Jr. (argued) and Jonathan S. Sack,
Morvillo Abramowitz Grand Iason & Anello PC, New York,
New York, for Defendant-Appellant.
Jennifer S. Granick, American Civil Liberties Union
Foundation, San Francisco, California; Nathan F. Wessler
4                       USA V. HUNT


and Brett M. Kaufman, American Civil Liberties Union
Foundation, New York, New York; Kelly Simon, American
Civil Liberties Union Foundation of Oregon, Portland,
Oregon; Andrew Crocker and Hannah Zhao, Electronic
Frontier Foundation, San Francisco, California; Jake
Wiener, Electronic Privacy Information Center,
Washington, D.C.; for Amici Curiae American Civil
Liberties Union, ACLU of Oregon, Electronic Frontier
Foundation, Electronic Privacy Information Center, and
National Association of Criminal Defense Lawyers.



                        OPINION

LEE, Circuit Judge:

    The abandonment doctrine states that a person who
abandons property relinquishes his expectation of privacy in
that property and thus waives any Fourth Amendment
challenge. But how should we apply the abandonment
doctrine to digital devices that may contain a massive trove
of personal information? Appellant Dontae Hunt and amici
urge us to scuttle this doctrine when it comes to cellphones.
    We decline to do so. We follow the time-tested
reasonable expectation of privacy principle while
considering that today’s technology allows us to keep
historically unprecedented amounts of private information in
devices. When determining a person’s intent to abandon,
courts should analyze the intent to abandon the device
separately from the intent to abandon its data.
    We disagree with the district court’s ruling that Hunt
lacked standing to challenge the search of his black iPhone.
                           USA V. HUNT                             5


The record does not allow the inference that Hunt intended
to abandon the phone or its contents when he dropped it after
being shot five times; it shows that he fled to seek medical
help. Hunt’s Fourth Amendment claim fails on the merits
because federal agents obtained a warrant and searched his
phone within a reasonable period.
    We also reject Hunt’s argument that the district court
judge should have recused herself because she served as the
U.S. Attorney in Oregon when her office earlier prosecuted
Hunt for a different crime. A reasonable person would not
question the district court judge’s impartiality. We affirm
the conviction and the sentence. 1
                       BACKGROUND
    I. Dontae Hunt drops his black iPhone as he gets shot
       five times.
    One early morning in December 2017, Dontae Hunt was
talking on his black iPhone as he strolled by his apartment
parking lot. A gunman suddenly appeared, firing a fusillade
of bullets at Hunt. Shot five times, Hunt dropped his black
iPhone and his Gucci satchel. Hunt’s girlfriend had
accompanied him and immediately called a female friend to
help take Hunt to a nearby hospital. The girlfriend took
Hunt’s satchel (which had fallen on the parking lot) but left
his black iPhone (which was near some shrubs). The two
women dropped Hunt off at the emergency room and left.
    The two women, however, did not make it far. The
police pulled the pair over for a traffic violation. During the
traffic stop, an officer spotted a brown Gucci satchel bag,


1
 We reject Hunt’s other challenges in a concurrently filed memorandum
disposition.
6                        USA V. HUNT


covered in blood, laying on the passenger floorboard. Inside
the bag the officer found two handguns. Hunt’s girlfriend
admitted the Gucci bag belonged to Hunt but denied
knowing the bag contained the handguns.
    Eugene police next went to the hospital to speak with
Hunt about the shooting. The officer found Hunt at the
hospital in “substantial pain.” Hunt refused to speak to the
officer. When the officer asked Hunt “if he wanted the
police to find out who shot him,” Hunt replied “no” and said
that “he was alright.” Before leaving the hospital, the officer
seized Hunt’s clothing and another iPhone—a white one—
as evidence associated with the shooting. The officer gave
Hunt a receipt for both the clothing and the white iPhone.
    Police visited the crime scene, where they found a black
iPhone near some shrubs a short distance from the shooting
location. The police took it into evidence as part of their
investigation into the shooting. No one ever came looking
for the phone, so it remained in evidence for over two years
until an unrelated investigation into a Portland overdose
death triggered police interest in the device.
    II. The federal government starts a separate drug
        investigation.
    The overdose investigation, conducted by the Portland
Police Bureau and several federal agencies, identified a
woman who sold counterfeit oxycodone pills to the
deceased. She declined to identify her supplier by name but
gave the police the supplier’s cellphone number. Relying on
this informant, the police obtained a geolocation warrant for
the registered cellphone owner, a woman who (the police
later discovered) worked for Hunt. In its affidavit in support
of the geolocation warrant, the police, however, failed to
disclose that this informant had a criminal history of lying to
                        USA V. HUNT                         7


the police. Nonetheless, the geolocation warrant ultimately
yielded additional evidence, leading the police to focus on
Hunt and to conduct an in-person surveillance of him. The
police noted that Hunt engaged in peculiar behavior common
to drug dealers trying to evade detection from law
enforcement. For example, he made well over a dozen
Walmart cash transfers using different phone numbers. The
mother of his children rented seven cars over four months,
and Hunt drove a Chevy Silverado paid for in cash by a
person with no links to Hunt. The investigation also turned
up evidence of Hunt’s past drug dealing convictions. And a
second confidential informant, with no criminal record or
known relationship to the first informant, told police that
Hunt continued to sell drugs and “store[] cash at residences
belonging to female acquaintances.”
    Federal agents used this information to obtain a premises
search warrant for three residences associated with Hunt,
including a home on Portland’s Dekum Street. During the
raid on the Dekum residence, police found counterfeit
fentanyl pills, firearms, and Hunt—barricaded in a bathroom
and allegedly flushing pills down the toilet.
 III. The government uses data from Hunt’s black
      iPhone to help convict him on drug-trafficking
      and other charges.
    The story comes full circle when federal agents filed an
affidavit in January 2020 to search several electronic
devices, including the black iPhone found at the scene of
Hunt’s shooting and held by the local police. At the time,
federal agents still lacked confirmation that the black iPhone
belonged to Hunt, though they suspected so because police
“found [it] on the ground where [Hunt] was shot.” The
8                       USA V. HUNT


search of the black iPhone produced more evidence of
Hunt’s drug dealing activities.
    Based on evidence from the searches of the Dekum
residence and the black iPhone, prosecutors charged Hunt
with several crimes, including possession with intent to
distribute fentanyl analogue, conspiracy to possess with
intent to distribute a controlled substance, unlawful
possession of a firearm, and laundering of monetary
instruments.    The case eventually landed on Judge
Immergut’s docket.
    Before the trial, Hunt moved for Judge Immergut’s
recusal. Over fifteen years earlier, Judge Immergut had
served as the U.S. Attorney for the District of Oregon when
that office prosecuted Hunt for unrelated charges. In that
case, the district court had sentenced Hunt to twenty years,
but his sentence was commuted after thirteen years. Judge
Immergut declined to recuse herself. She explained, “I have
no personal bias or prejudice against Defendant Hunt. Nor
do I have any personal recollection of Defendant Hunt or the
facts underlying his prior 2005 conviction.”          Judge
Immergut presided over the trial, which ultimately led to
Hunt’s conviction.
               STANDARD OF REVIEW
    This court reviews de novo a district court’s denial of a
motion to suppress. United States v. Yang, 958 F.3d 851,
857 (9th Cir. 2020). We review the district court’s factual
findings, including those factual findings related to
abandonment, for clear error. See id. at 858; see also United
States v. Nordling, 804 F.2d 1466, 1469 (9th Cir. 1986). For
recusal orders, we review for abuse of discretion. United
States v. McTiernan, 695 F.3d 882, 891 (9th Cir. 2012).
                          USA V. HUNT                          9


                        DISCUSSION
 I.   Judge Immergut did not abuse discretion in
      denying the recusal motion.
    As a threshold matter, we must decide whether Judge
Immergut should have recused herself because she served as
the U.S. Attorney in Oregon when that office prosecuted
Hunt in his earlier 2005 criminal proceedings. We reject
Hunt’s argument that she should have done so.
     A federal judge must “disqualify [her]self in any
proceeding in which [her] impartiality might reasonably be
questioned.” 28 U.S.C. § 455(a); see also United States v.
Holland, 519 F.3d 909, 913 (9th Cir. 2008) (quoting from
id.). This provision requires judges “to avoid even the
appearance of partiality.” Liljeberg v. Health Servs.
Acquisition Corp., 486 U.S. 847, 860 (1988) (quoting Health
Servs. Acquisition Corp. v. Liljeberg, 796 F.2d 796, 802 (5th
Cir. 1986)). We thus require recusal when “a reasonable
person with knowledge of all the facts would conclude that
the judge’s impartiality might reasonably be questioned.”
Holland, 519 F.3d at 913 (quotation omitted).
    Our circuit precedent does not establish many bright-line
rules and requires judges to take a “fact-driven” approach
that “may turn on the subtleties” of each case when applying
the recusal standard. Id. For example, in United States v.
Silver, we applied this fact-driven approach to find that a
judge did not need to recuse himself without a “factual
connection or relationship between the [] case [before him]
and [a ten-year-old] mail fraud” investigation into the
defendant that began during the judge’s tenure as the United
States Attorney. 245 F.3d 1075, 1079 (9th Cir. 2001). In
reaching that holding, Silver did not establish a rigid rule that
a judge can avoid recusal simply because the prior case lacks
10                      USA V. HUNT


a factual relationship to the case before the judge. See id.
Rather, both the age of the earlier investigation and the fact
that the judge only needed to consider the prior case for
sentencing purposes contributed to our determination that a
reasonable person would not doubt that judge’s impartiality.
Id. at 1080.
    In contrast, we did impose a bright-line rule in United
States v. Arnpriester that a judge cannot decide the same
case in which the judge participated in or supervised as the
United States Attorney. 37 F.3d 466, 467 (9th Cir. 1994).
We found categorically that a reasonable person would
question a judge’s impartiality in any such situation. See id.
    The facts of Hunt’s case convince us that Judge
Immergut did not abuse her discretion in holding that a
reasonable person would not question her impartiality. First,
as in Silver, Hunt’s current case has “no factual connection
or relationship” with his prior prosecution. See 245 F.3d at
1079. Second, over fifteen years passed between Hunt’s first
prosecution and this second case. That stretches beyond the
ten-year gap in Silver. Id. at 1080. Third, Judge Immergut
served as the United States Attorney, and not as a line
prosecutor. Many similar drug and felon-in-possession
prosecutions likely passed through her office, and Judge
Immergut, as the U.S. Attorney, likely was not directly
involved in these commonplace criminal prosecutions.
Fourth, Judge Immergut stated she did not have “any
personal recollection” of Hunt’s 2005 case and has “no
personal bias or prejudice” against him. These facts would
not lead a reasonable person to think that Judge Immergut
had any bias against Hunt. We thus next address Hunt’s
Fourth Amendment claim.
                        USA V. HUNT                        11


 II. Hunt has standing to make a Fourth Amendment
     challenge because he did not abandon his privacy
     interest in the black iPhone.
    The district court erred when it held that Hunt abandoned
the black iPhone and thus lacked standing to challenge the
search of the iPhone’s data. We, however, reject Hunt and
amici’s invitation to jettison the abandonment doctrine for
digital data. Rather, we follow the reasonable expectation of
privacy framework set by the Supreme Court and adapt the
abandonment doctrine to account for the unique
characteristics of cellphone data. That approach leads us to
hold that the abandonment doctrine can apply to cellphone
data but courts should analyze the physical phone and its
data separately to determine whether the circumstances
allow the conclusion that there was an intent to abandon
either.
   A. We apply the expectation-of-privacy principle
      while considering the unique nature of digital
      devices in applying the abandonment doctrine.
    The Fourth Amendment guarantees to the people the
right “to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures . . . .”
U.S. CONST. amend. IV. The Framers adopted this
amendment to guard against the type of abuses they
experienced under British rule: It was a “response to the
reviled ‘general warrants’ and ‘writs of assistance’ of the
colonial era, which allowed British officers to rummage
through homes in an unrestrained search for evidence of
criminal activity.” Carpenter v. United States, 585 U.S. 296,
303 (2018) (quoting Riley v. California, 573 U.S. 373, 403
(2014)). The Fourth Amendment enshrines the founding
generation’s goals to protect “‘the privacies of life’ against
12                           USA V. HUNT


‘arbitrary power’” and “to place obstacles in the way of a too
permeating police surveillance.” Id. (citations omitted).
    But as digital “technology has enhanced the
Government’s capacity to encroach upon” traditionally
private areas of life, the judiciary has sought to preserve
“that degree of privacy against government that existed
when the Fourth Amendment was adopted.” Carpenter, 585
U.S. at 305 (citing Kyllo v. United States, 533 U.S. 27, 34
(2001)). To that end, the Supreme Court warns that “[w]hen
confronting new concerns wrought by digital technology,”
courts must be “careful not to uncritically extend existing
precedents.” Carpenter, 585 U.S. at 318.
    We follow the model set by the Supreme Court in Riley,
Carpenter, Jones, and Kyllo and apply reasonable
expectation-of-privacy principles to a world where new
technology makes possible previously unimaginable and
objectionable invasions of privacy. 2 As one leading Fourth
Amendment scholar has argued, the Supreme Court’s
framework for analyzing digital devices advances the
“original public meaning of the Fourth Amendment.” Orin
Kerr, The Digital Fourth Amendment 54–56 (2025). It does
so by preserving the same balance between the citizenry’s
right to privacy and the government’s power to investigate
that existed in the early republic. See id. at 57. The founding

2
  See Riley, 573 U.S. at 385–401 (applying the traditional warrant
exception test to cellphone data); Carpenter, 585 U.S. at 313 (applying
the traditional expectation of privacy in the “whole of [one’s] physical
movements” to cell-site data); United States v. Jones, 565 U.S. 400, 402,
411 (2012) (“What we apply is an 18th-century guarantee against
unreasonable searches” to find attaching a GPS tracking advice to a car
counts as a search); Kyllo, 533 U.S. at 34–35 (applying the traditional
expectation of privacy standard in holding that the use of thermal
imagining technology can count as a search of a home).
                              USA V. HUNT                               13


generation always understood the Fourth Amendment to
protect a certain degree of privacy and not merely a specific
set of rules. Id.; see Kyllo, 533 U.S. at 34–35.
    The Supreme Court in Riley highlighted the unique
nature of digital devices containing massive amounts of
personal data. 573 U.S. 373. The police officers there
searched cellphones right after arresting the suspects, and
justified these warrantless searches under the search
incident-to-arrest exception. The Court, however, refused to
extend this warrantless search exception to cellphones, in
large part because it recognized the “substantially greater
individual privacy interests” associated with the private and
detailed data contained in cellphones as opposed to “a brief
physical search.” Id. at 374. 3 That greater privacy interest
stems from the vast quantity and intimate quality of the data
collected throughout the day and over the years. Id. at 393.
As the Court wryly remarked, “the proverbial visitor from
Mars might conclude [cellphones] were an important feature
of human anatomy,” given that they “are now such a
pervasive and insistent part of daily life.” Id. at 385.
    Cellphones can easily contain over a decade’s worth of
private photographs, personal text messages to family and
friends, every email sent to business associates, voicemails
from years ago, and call logs documenting every call
received or dialed. The various apps on a phone can also
contain a trove of personal information. For example, a


3
  The Court also reasoned that rationales justifying a warrantless search
incident to arrest—the risk of a suspect hiding a weapon in, say, a satchel
or reaching out to destroy evidence in that satchel—do not apply to
digital data. See 573 U.S. at 386. The Court, however, recognized
exigent circumstances could still allow a warrantless search of digital
devices. Id. at 391.
14                       USA V. HUNT


search of web-browsing history may reveal intimate details
of “an individual’s private interests or concerns.” Id. at 395.
A medical-related app may disclose private health
information or prescription history. And a financial app can
divulge purchases made on a credit card, bank balances,
credit scores, and an individual’s net worth. Indeed, a
cellphone’s ability to store vast data likely allows the
government to learn more about the cellphone’s owner than
would a search of the person’s entire home or every piece of
mail received. Id. at 396–97.
    In our case, we must decide how to apply the
abandonment doctrine—a well-established exception to the
Fourth Amendment’s prohibition against a warrantless
search and seizure—to cellphones. The abandonment
doctrine holds that a person forfeits a reasonable expectation
of privacy by voluntarily abandoning property. United
States v. Fisher, 56 F.4th 673, 686 (9th Cir. 2022).
Abandonment goes to intent. Nordling, 804 F.2d at 1469. A
person shows an intent to abandon a privacy interest when,
given the totality of the circumstances, by “words, acts or
other objective indications, [the] person has relinquished a
reasonable expectation of privacy in the property at the time
of the search or seizure.” Id. (citation modified). We ask
what “words, acts or other objective indications” would
reveal a person’s intent to voluntarily abandon any
expectation of privacy in the property. See id.
    Following the Supreme Court’s framework, we apply the
abandonment doctrine to cellphones while accounting for
the unique aspects of cellphone data. Someone who loses
her cellphone through theft or negligence likely does not
intend to release to the public details of her personal life any
more than someone who loses a house key intends to invite
the public to rummage through her home. See Riley, 573
                        USA V. HUNT                        15


U.S. at 397. That house key analogy proves particularly
instructive when thinking about abandonment because the
house key and the house provide the closest pre-digital
functional analogue to the cell phone and its data. See Kerr,
supra at 65. The analogy confirms that just as courts
historically would apply the reasonable expectation of
privacy principle separately to a house key and the contents
of a house, courts today may need to distinguish a digital
device from the data it contains to preserve the degree of
privacy that existed at the time of the Fourth Amendment’s
adoption. Id. Based on the specific facts of each case, courts
should analyze the intent to abandon the device separately
from the intent to abandon its data—and not reflexively
conflate the two.
     In Fisher, the Ninth Circuit’s most analogous case, two
defendants hid a cellphone and two hard drives with
incriminating information between the insulation and wood
framing of an attic. 56 F.4th at 681. While in custody, the
defendants sold the house with the devices still hidden in the
attic. Id. The court held that the defendants had abandoned
the devices when they did not recover them “before the home
was sold.” Id. at 687 (emphasis in original). Having
intentionally left their devices in the home and then sold the
house knowing that the devices remained there, the
defendants abandoned the devices and their data. Id.
   B. Hunt did not abandon the black iPhone or its
      data.
    Hunt’s actions do not suggest an intent to abandon his
black iPhone or its data. The district court committed clear
error by finding otherwise. The serious injuries caused by
the shooting—and the traumatic and chaotic atmosphere
after—suggest that Hunt likely dropped the black iPhone and
16                       USA V. HUNT


did not intend to leave it behind. Considering the
circumstances, Hunt likely only intended to get medical
attention and flee from the shooter as soon as possible
without thinking or even knowing what happened to the
phone. This is distinguishable from the situation in Fisher,
where the Ninth Circuit found that the defendants—who sold
their house even though they knew that it contained a
cellphone and two hard drives in its attic—forfeited their
privacy interest in the devices and their content. See 56 F.4th
at 687.
    The district court acknowledged that Hunt “may have
dropped the phone in the course of being shot or fleeing,”
but reasoned that after the shooting, Hunt made no “apparent
effort to secure the black iPhone.” But the iPhone was later
found in the bushes and not plainly visible. Most people
would not scour the bushes after a shooting to find a phone
(assuming that Hunt even realized he had lost or dropped the
phone after being shot).
    The government also argues that Hunt abandoned the
black iPhone and its data by not trying to retrieve the phone
from the police. That is an important fact in assessing intent,
but there is no indication that Hunt realized that he left the
missing phone at the shooting scene for at least three
reasons. First, Hunt claims to not remember the shooting, so
he might not have known that he used the black iPhone at
the time and that the police had it. Second, the police
officers seized the white iPhone from Hunt’s person and
gave him a receipt for it, such that Hunt could have
reasonably expected the police to give him a receipt for the
black iPhone if they also had it. The police, however, did
not provide a receipt for the black iPhone. Third, Hunt
reasonably could have concluded that someone other than
the police picked up a valuable iPhone in a public parking
                         USA V. HUNT                        17


lot. We thus hold that the district court clearly erred in
finding that Hunt intended to abandon the black iPhone, and
it logically follows that he did not intend to abandon the data
in it.
    Even if we assume that Hunt had abandoned his black
iPhone by not trying to retrieve it from the police, we cannot
conclude that he also intended to abandon the data in his
phone without examining all the relevant facts. Unlike the
defendants in Fisher, Hunt did not willingly sell or give
away his black iPhone with all its personal data still intact.
See 56 F.4th at 687. Rather, he simply lost the phone during
a shooting. Though he did not follow up with the police, the
record does not establish that he had reason to suspect the
police collected the black iPhone from the crime scene. We
need not conduct a separate analysis of the stored data
because we hold that Hunt did not abandon his phone.
III. The government did not violate Hunt’s Fourth
     Amendment rights because it obtained a warrant to
     search the phone and did not hold it for an
     unreasonable period.
    While Hunt has standing to challenge the search of the
black iPhone’s data, his argument fails on the merits.
Federal agents obtained a warrant to search the iPhone’s
data. So Hunt can only complain that the government
violated the Fourth Amendment by seizing the data for an
unreasonably long period. This argument falls flat because
the Eugene police acted reasonably by collecting the iPhone
as evidence related to the shooting investigation and by
holding it until someone claimed it.
    The Fourth Amendment prohibits unreasonable searches
and seizures. Soldal v. Cook County, 506 U.S. 56, 61 (1992)
(citation modified). The Court, however, has recognized
18                      USA V. HUNT


that “special law enforcement needs, diminished
expectations of privacy, minimal intrusions, or the like” may
make a warrantless seizure reasonable. Illinois v. McArthur,
531 U.S. 326, 330 (2001). But “a seizure lawful at its
inception can nevertheless violate the Fourth Amendment
because its manner of execution unreasonably infringes
possessory interests.” United States v. Jacobsen, 466 U.S.
109, 124 (1984). To remain reasonable, a seizure must last
“no longer than reasonably necessary for the police, acting
with diligence, to obtain the warrant” to search the property.
McArthur, 531 U.S. at 332; see also United States v.
Sullivan, 797 F.3d 623, 633 (9th Cir. 2015).
    To decide whether a prolonged seizure remained
reasonable, we balance “the nature and quality of the
intrusion on the individual’s Fourth Amendment interests
against the importance of the governmental interests alleged
to justify the intrusion.” Sullivan, 797 F.3d at 633 (citation
omitted). The balance here favors the government.
    Given that Hunt lost his iPhone and never sought to
recover it, the Eugene police’s intrusion upon his possessory
interest was minimal at best. See id. (finding owner’s
inability to use a device reduced his possessory interest in
the device).
     On the other side of the ledger, the Eugene police had a
legitimate law enforcement reason to seize the black iPhone
as evidence for its investigation into the shooting. While the
iPhone might have belonged to a random passerby, its
proximity to the site of Hunt’s shooting gave police a basis
to suspect the iPhone could help identify the shooter, an
accomplice, or a witness. The police thus acted reasonably
by seizing the iPhone during the initial sweep of the parking
lot.
                         USA V. HUNT                        19


    Moreover, police had a legitimate law enforcement
reason to retain the iPhone after its initial collection simply
because it represented lost property with no identified owner
to whom the police could return it. Multiple state supreme
court cases note that the police often retain lost or mislaid
property in secure locations until the authorities can identify
the owner. See State v. Hamilton, 67 P.3d 871, 875 (Mont.
2003); State v. Ching, 678 P.2d 1088, 1093 (Haw. 1984); see
also State v. Kealey, 907 P.2d 319, 325 (Wash. Ct. App.
1995), as amended on denial of reconsideration (Feb. 26,
1996). Here, the record does not suggest that the Eugene
police did anything with the black iPhone other than hold it
in evidence.
                      CONCLUSION
   We AFFIRM the district court’s orders denying Hunt’s
motion to suppress and his recusal motion.

```

---

## GROUP: content/cases/United States v. Lewis.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Lewis
type: case
citation: "No. 22-5593, slip op. (6th Cir. 2023)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 6th Cir."
court_level: coa
circuit: ca6
year: 2023
date_decided: 2023-09-01
docket: 22-5593
authority_weight: "Binding in-circuit — 6th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9424185/united-states-v-edward-leonidas-lewis/"
  cluster_id: 9424185
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Lewis
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Consent Searches]]"
    role: Key
related:
  - "[[Consent Searches]]"
  - "[[United States v. Leon]]"
  - "[[Riley v. California]]"
tags:
  - case
  - fourth-amendment
  - consent-search
  - scope-of-consent
  - electronic-devices
  - bare-bones-affidavit
  - good-faith-exception
  - sixth-circuit
holding: "A homeowner's consent to an on-site 'preview' of his laptop and cell phone authorized only that limited search; the later seizure and full forensic examination of the devices required a warrant, and because the supporting affidavit was a bare-bones, conclusory statement that recited only that a consented search had 'become apparent' incriminating — without any facts a magistrate could independently weigh — it failed to establish probable cause, and the good-faith exception could not save so deficient a warrant."
aliases:
  - United States v. Lewis
  - "United States v. Lewis (6th Cir. 2023)"
  - United States v. Edward Leonidas Lewis
---

# United States v. Lewis

*No. 22-5593, slip op. (6th Cir. 2023)* · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9424185 → published opinion 9829122 (Moore, J.; Nos. 22-5593/5800, RECOMMENDED FOR PUBLICATION 23a0206p.06, decided Sept. 1, 2023). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (published opinion; no F.4th reporter page locatable from any independent source — S2 A3, S9 verifies). -->

## Background
Acting on a foreign-agency tip, Kentucky State Police Detective Gatson and federal agents went to Edward Lewis's home; Lewis let them in and signed a form consenting to a complete search of the premises and his named laptop and cell phone. A forensic examiner "previewed" the devices on-site, surfacing file names indicative of child pornography and thumbnail images. Officers stopped, arrested Lewis, and seized the devices; a Commonwealth prosecutor advised obtaining a warrant, and a later forensic examination under that warrant produced the charged evidence. The district court found the warrant lacked probable cause but denied suppression under the [[The Good-Faith Exception|good-faith exception]]; Lewis pleaded guilty reserving his appeal.

## Issue
Whether the warrant authorizing the full forensic search of Lewis's seized devices was supported by probable cause and, if not, whether the [[The Good-Faith Exception|good-faith exception]] nonetheless barred suppression.

## Rule
Probable cause is judged within the "four corners of the affidavit," which must state facts showing a fair probability that evidence will be found — not a mere conclusion — and on so bare-bones an affidavit the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] is unavailable. The court held Detective Gatson's affidavit fell short: "That conclusory statement was too vague and insubstantial to establish probable cause to search Lewis's electronic devices. ... The search warrant that was issued based on Detective Gatson's affidavit therefore violated the Fourth Amendment's probable-cause requirement." — slip op. at 7. ^pin-slip7

## Application
Lewis's consent authorized only the initial on-scene preview; the officers' subsequent seizure and full forensic examination of the devices required a warrant. But the affidavit supplied only Gatson's say-so — that during a consented search "it became apparent" Lewis had viewed illegal images — with no description of the evidence or investigative steps a magistrate could evaluate. Like the affidavits condemned in *Nathanson* and *[[Aguilar v. Texas|Aguilar]]*, it was "wholly inadequate," so "[n]o reasonable officer" could have relied on it in good faith. The [[The Good-Faith Exception|good-faith exception]] did not apply.

## Conclusion
**Reversed, [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]].** The Sixth Circuit reversed the denial of suppression, [[Reading and Citing Cases#vacated|vacated]] Lewis's conviction, and [[Reading and Citing Cases#on-remand|remanded]] for further proceedings. Judge Moore wrote for the panel (Moore, Clay, Gibbons, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Lewis* teaches two connected limits: consent to a narrow on-site device "preview" does not authorize a later full forensic search — for which the heightened privacy interest in digital data (*[[Riley v. California|Riley]]*) demands a warrant — and a bare-bones affidavit forfeits *[[United States v. Leon|Leon]]* good faith. Published Sixth Circuit opinion (23a0206p.06); rendered slip-style here because no Federal [[Reading and Citing Cases#reporter|Reporter]] page could be independently confirmed.

## Appears on
- [[Consent Searches]] — *Key*

## Sources
- [*United States v. Edward Leonidas Lewis*, No. 22-5593, slip op. (6th Cir. 2023)](https://www.courtlistener.com/opinion/9424185/united-states-v-edward-leonidas-lewis/) — pinpoint: slip op. at 7 (bare-bones affidavit fails probable cause; good faith unavailable). Rule quote string-matched to the CL opinion text 2026-07-07. Published as 6th Cir. op. 23a0206p.06; the CL cluster carries no citations[] and no F.4th page was independently locatable (S2 A3 slip render).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f57ca31a787982e9", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 22-5593, slip op. (6th Cir. 2023)", "court": "U.S. Court of Appeals, 6th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Lewis", "year": "2023"}}
{"assertion_id": "5fb24f51685f8fe5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A homeowner's consent to an on-site 'preview' of his laptop and cell phone authorized only that limited search; the later seizure and full forensic examination of the devices required a warrant, and because the supporting affidavit was a bare-bones, conclusory statement that recited only that a consented search had 'become apparent' incriminating — without any facts a magistrate could independently weigh — it failed to establish probable cause, and the good-faith exception could not save so deficient a warrant.", "title": "United States v. Lewis"}}
{"assertion_id": "81bbd0b77799a8ad", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Key", "title": "United States v. Lewis"}}
{"assertion_id": "17735ab47bb5e02b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 6th Cir.", "title": "United States v. Lewis"}}
{"assertion_id": "fbadcf3e5d4678dd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Lewis", "varies_by_point": "false"}}
```

### lake record — United States v. Lewis

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Lewis",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Edward Leonidas Lewis",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Lewis",
    "court": "U.S. Court of Appeals, 6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": "2023-09-01",
    "year": 2023,
    "docket": "22-5593",
    "cluster_id": 9424185,
    "lead_opinion_id": 9829122,
    "sibling_ids": [],
    "absolute_url": "/opinion/9424185/united-states-v-edward-leonidas-lewis/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "coa",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "W9 slip disposition (previously R3-escalated; pre-W5 re-key landed correct identity United States v. Edward Leonidas Lewis, 6th Cir. No. 22-5593, decided 2023-09-01, consent-scope reversal). CL cluster 9424185 Published but citations[] empty (live-verified 2026-07-07). Published as 6th Cir. op. 23a0206p; no F.4th reporter page locatable from any independent source (Justia/FindLaw/vLex index by docket only) \u2014 no-fabrication slip render pending reporter pagination.",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://www.opn.ca6.uscourts.gov/opinions.pdf/23a0206p-06.pdf",
          "cite": "6th Cir. op. 23a0206p, No. 22-5593, RECOMMENDED FOR PUBLICATION, 2023-09-01"
        },
        {
          "source": "Justia",
          "url": "https://law.justia.com/cases/federal/appellate-courts/ca6/22-5593/22-5593-2023-09-01.html",
          "cite": "No. 22-5593 (6th Cir. 2023), no F.4th cite listed"
        }
      ]
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
    "date_created": "2026-07-07T13:49:58Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:50:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:50:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:50:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:50:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-lewis--9424185",
      "to_record_id": "United States v. Lewis",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Lewis

```
                                 RECOMMENDED FOR PUBLICATION
                                 Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                        File Name: 23a0206p.06

                    UNITED STATES COURT OF APPEALS
                                   FOR THE SIXTH CIRCUIT



                                                              ┐
 UNITED STATES OF AMERICA,
                                                              │
                                     Plaintiff-Appellee,      │
                                                               >        Nos. 22-5593/5800
                                                              │
        v.                                                    │
                                                              │
 EDWARD LEONIDAS LEWIS,                                       │
                                  Defendant-Appellant.        │
                                                              ┘

 Appeal from the United States District Court for the Eastern District of Kentucky at Frankfort.
               No. 3:21-cr-00021—Gregory F. Van Tatenhove, District Judge.

                             Decided and Filed: September 1, 2023

                   Before: MOORE, CLAY, and GIBBONS, Circuit Judges.

                                       _________________

                                             COUNSEL

ON BRIEF: David J. Guarnieri, MCBRAYER PLLC, Lexington, Kentucky, for Appellant.
Lauren Tanner Bradley, Charles P. Wisdom, Jr., UNITED STATES ATTORNEY’S OFFICE,
Lexington, Kentucky, for Appellee.
                                       _________________

                                              OPINION
                                       _________________

       KAREN NELSON MOORE, Circuit Judge. Kentucky State Police officers searched
Edward Lewis’s laptop, cell phone, and thumb drive and found evidence of child pornography.
Lewis moved to suppress the evidence, arguing that it was obtained through an unlawful search
and seizure of his electronic devices. The district court found that the good-faith exception to the
exclusionary rule applied and denied Lewis’s motion, and Lewis pleaded guilty while reserving
 Nos. 22-5593/5800                    United States v. Lewis                               Page 2


his right to bring this appeal. We REVERSE the district court’s order denying Lewis’s motion
to suppress, VACATE Lewis’s conviction, and REMAND for further proceedings.

                                      I. BACKGROUND

       In 2019, federal Homeland Security agents received a tip from a foreign law-enforcement
agency that an internet-protocol address later connected to Lewis was “viewing child sexual
exploitation online[.]” R. 35 (Hr’g Tr. at 11, 78–79) (Page ID #207, 274–75). The agents
notified the Kentucky State Police, who opened an investigation. Id. at 10–12 (Page ID #206–
08).

       Two years later, in February 2021, Detective Anthony Gatson of the Kentucky State
Police and Homeland Security Special Agents Brian Minnick and Brandon Even traveled to
Lewis’s home as part of their ongoing investigation. Id. at 13, 56–57 (Page ID #209, 252–53).
Detective Gatson knocked on Lewis’s door, which Lewis answered. Id. at 13 (Page ID #209).
Detective Gatson identified himself and the Homeland Security agents to Lewis, and “asked if
[they] could speak to [Lewis] about a federal complaint of some alleged crimes over the internet
from the federal government.” Id. Lewis invited Detective Gatson and the agents inside. Id.

       Inside Lewis’s home, Detective Gatson explained that he had “been told there was child
sexual exploitation activity at the house.” Id. Detective Gatson asked Lewis “if he would mind
if someone came over and looked at . . . his devices.” Id. Lewis responded that he had no
objection, id., and agreed to sign a consent form stating that he “consent[ed] to a complete search
of the premises, property or vehicle located” at his residence “and more particularly described as
Samsung Galaxy Note 9 [and] HP Pavilion Laptop[,]” R. 26-2 (Consent Form at 1) (Page ID
#141). Detective Gatson then called for a forensic examiner to come to Lewis’s home and
“preview the items” described in the signed consent form. R. 35 (Hr’g Tr. at 13–14) (Page ID
#209–10).

       Approximately twenty minutes later, Jason Rollins, a forensic examiner with the
Kentucky State Police, arrived at Lewis’s home. Id. at 20 (Page ID #216). Rollins generated a
preview of Lewis’s laptop, which revealed several file names indicative of child pornography,
including “2yo_boy,” “Tara,” and “pedomom.” Id. at 21–22 (Page ID #217–18). Rollins also
 Nos. 22-5593/5800                    United States v. Lewis                               Page 3


reviewed Lewis’s cell phone, where he found thumbnail images, which were determined on an
unspecified later date to be taken from videos of Lewis’s cousin’s children bathing naked in a
bathroom. Id. at 23–24 (Page ID #219–20). As Rollins was searching Lewis’s laptop and cell
phone, Lewis reportedly stated that he knew it was illegal to save child pornography but that he
did not know that it was illegal merely to look at it. Id. at 39 (Page ID #235). Rollins shared the
results of his initial searches with Detective Gatson, but neither Rollins nor Detective Gatson
opened any of the files or thumbnail images on Lewis’s laptop or cell phone. Id. at 23 (Page ID
#219).

         Detective Gatson called a Commonwealth prosecutor to ask for advice. Id. at 25 (Page
ID #221). The prosecutor told Detective Gatson to arrest Lewis and obtain a search warrant for
his residence. Id. Following that advice, Detective Gatson asked Lewis to step outside and read
him his Miranda rights. Id. at 26 (Page ID #222); see also Miranda v. Arizona, 384 U.S. 436
(1966). Lewis invoked his rights, but he did not say that he was revoking his consent to the
search of his electronic devices or his home. R. 35 (Hr’g Tr. at 28) (Page ID #224). Another
Kentucky State Police officer then arrived and drove Lewis to jail. Id. at 18, 52 (Page ID #214,
248).

         After Lewis was arrested, Detective Gatson returned to his office while Special Agents
Minnick and Even “sat on the front porch to secure the house[.]” Id. at 29 (Page ID #225).
Detective Gatson prepared a search warrant for Lewis’s house and any electronic devices stored
inside the home that could contain evidence of child pornography, including the laptop and cell
phone that Detective Gatson and Rollins had reviewed at Lewis’s home. Id. Detective Gatson
did not share the proposed search warrant or his affidavit in support of the warrant with a
prosecutor, but instead took the documents directly to a Franklin County judge. Id. at 57 (Page
ID #253). Detective Gatson did not provide the state judge with any additional information
beyond what he included in the proposed search warrant and his affidavit. Id. at 29 (Page ID
#225). The state judge signed the search warrant. Id.; R. 24-3 (Search Warrant at 6) (Page ID
#107).
 Nos. 22-5593/5800                   United States v. Lewis                               Page 4


       Law-enforcement officers subsequently executed the search warrant, searching Lewis’s
home and seizing his laptop, cell phone, and other electronic devices. R. 35 (Hr’g Tr. at 31)
(Page ID #227). The officers took the devices to a state laboratory, where the devices were
forensically searched. Id. The forensic search revealed evidence of child pornography on
Lewis’s laptop, cell phone, and USB thumb drive. Id.; R. 24-3 (Search Warrant Return at 1)
(Page ID #111).

       Lewis was indicted in October 2021 and charged with seven counts of producing,
receiving, and possessing child pornography, in violation of 18 U.S.C. §§ 2251(a) and
(e), 2252(a)(2), and 2251(a)(4)(B). R. 1 (Indictment at 1–4) (Page ID #1–4). Lewis pleaded not
guilty and later moved under the Fourth Amendment to suppress the evidence obtained from his
laptop, cell phone, and thumb drive as the fruits of an unlawful search and seizure. R. 11
(Minute Entry at 1) (Page ID #28); R. 24 (Mot. to Suppress at 1) (Page ID #82). He argued that
the search warrant authorizing the search and seizure of his electronic devices was not supported
by probable cause and, among other things, that the affidavit Detective Gatson submitted in
support of the search warrant was a bare-bones affidavit. R. 24-1 (Mem. at 3–4) (Page ID #86–
87).

       A magistrate judge held a hearing on Lewis’s motion to suppress and later issued a report
and recommendation to the district court recommending that Lewis’s motion be denied. United
States v. Lewis, No. 3:21-CR-00021-GFVT-EBA, 2022 WL 1284061, at *1 (E.D. Ky. Jan. 11,
2022) (Lewis I), report and recommendation rejected, 591 F. Supp. 3d 177 (E.D. Ky. 2022)
(Lewis II). The magistrate judge declined to address Lewis’s challenges to the search warrant.
Lewis I, 2022 WL 1284061, at *7. The magistrate judge instead found that Lewis had knowingly
and voluntarily consented to the search of his electronic devices, that Lewis’s consent authorized
not only the initial preview of his devices but also the subsequent seizure and forensic
examination of the devices, and that Lewis had not withdrawn his consent at any time. Id. at *4–
6. Lewis objected to the report and recommendation. R. 36 (Objs. to R&R at 1–19) (Page ID
#284–302).

       The district court declined to adopt the report and recommendation but agreed that
Lewis’s motion should be denied on other grounds. Lewis II, 591 F. Supp. 3d at 181. The
 Nos. 22-5593/5800                     United States v. Lewis                               Page 5


district court disagreed with the magistrate judge’s analysis of the scope of Lewis’s consent,
finding that Lewis had consented to the preview of his electronic devices but not to the
subsequent seizure or search of those devices. Id. at 185. The district court further agreed with
Lewis that the search warrant failed to establish probable cause to believe that his electronic
devices contained evidence of a crime. Id. at 186–87. But the district court ultimately found that
suppression was inappropriate because law-enforcement officers had relied on the search warrant
in good faith. Id. at 187–88. The district court therefore denied Lewis’s motion to suppress. Id.
at 190–91.

         Following the denial of his motion to suppress, Lewis signed a conditional plea
agreement pursuant to which he pleaded guilty to one count of producing child pornography, in
violation of 18 U.S.C. § 2251(a), but retained his right to appeal the district court’s suppression
order and to withdraw his plea if he prevailed on that appeal. R. 46 (Plea Agreement at 1–2)
(Page ID #359–60). The district court sentenced Lewis to 300 months’ imprisonment and a life
term of supervised release. R. 57 (Am. Judgment at 2–3) (Page ID #409–10). Lewis filed this
timely appeal.

                                          II. ANALYSIS

         Lewis appeals the denial of his motion to suppress, challenging the district court’s finding
that the good-faith exception to the exclusionary rule precludes suppression of evidence
recovered from his electronic devices. We review the district court’s conclusions of law de novo
and its factual findings for clear error. United States v. Master, 614 F.3d 236, 238 (6th Cir.
2010).

A. The Search Warrant

         The district court found that the search warrant was not supported by probable cause but
that the good-faith exception applied. Lewis II, 591 F. Supp. 3d at 187. We accord “great
deference” to the state magistrate’s probable-cause determination, but we give no particular
weight to the district court’s review of that determination. United States v. Lapsins, 570 F.3d
758, 763 (6th Cir. 2009) (quotation omitted) (quoting United States v. Terry, 522 F.3d 645, 647
 Nos. 22-5593/5800                   United States v. Lewis                               Page 6


(6th Cir. 2008)). The district court’s finding that the “good faith exception applies is a legal
conclusion that we review de novo.” United States v. Frazier, 423 F.3d 526, 533 (6th Cir. 2005).

       1. Probable Cause

       The Fourth Amendment provides that a search warrant may issue only “upon probable
cause, supported by Oath or affirmation[.]” U.S. Const. amend IV. When determining whether
a search warrant was supported by probable cause, we limit our review to the “four corners of the
affidavit.” United States v. Brooks, 594 F.3d 488, 492 (6th Cir. 2010). To establish probable
cause for a search warrant, “an affidavit must contain facts that indicate a fair probability that
evidence of a crime will be located on the premises of the proposed search.” United States v.
Abboud, 438 F.3d 554, 572 (6th Cir. 2006) (quoting Frazier, 423 F.3d at 531).

       Here, the state-court judge issued a search warrant based on Detective Gatson’s affidavit.
In the government’s words, Detective Gatson’s affidavit “detailed his considerable experience
investigating child sexual exploitation crimes and included boilerplate language concerning such
investigations.” Appellee Br. at 4–5. The affidavit then “set forth only the facts that” Detective
Gatson “believe[d] [were] necessary to establish probable cause to believe that evidence, fruits
and instrumentalities of violations of” Kentucky’s child sexual-exploitation laws were “present
at” Lewis’s home. R. 24-3 (Gatson Aff. at 4) (Page ID #105). Those facts were:

       An HSI investigation identified Edward L Lewis . . . as a person of interest. HSI
       SA Minnick requested assistance with interviewing Mr. Lewis. Mr. Lewis was
       located at his residence at [address.] Mr. Lewis gave consent to search his laptop
       and cell phone. During [the] search it became apparent that Mr. Lewis had used
       his laptop to view images of child sexual exploitation. The search based on
       consent was stopped and Mr. Lewis was arrested.
       Based on the affiant’s knowledge, experience and training, Edward L Lewis has
       demonstrated a pattern of criminal activity related to child pornography, and there
       is a reasonable likelihood that the user treats child pornography as a valuable
       commodity to be retained and collected, a characteristic common to many people
       interested in child pornography. It is, therefore, likely that evidence of the
       contraband remains in the user’s possession[.]

Id.
 Nos. 22-5593/5800                    United States v. Lewis                                   Page 7


       The government does not dispute that Detective Gatson’s affidavit failed to establish
probable cause. “Detective Gatson provided the state judge only one fact in support of the
existence of probable cause: that a search of Mr. Lewis’s laptop and cell phone had occurred.”
Lewis II, 591 F. Supp. 3d at 186. Absent additional information, such as a description of the
evidence uncovered during that search, Detective Gatson’s affidavit merely stated his belief that
Lewis had viewed child pornography.           That conclusory statement was too vague and
insubstantial to establish probable cause to search Lewis’s electronic devices. See United States
v. Carpenter, 360 F.3d 591, 595 (6th Cir. 2004) (en banc). The search warrant that was issued
based on Detective Gatson’s affidavit therefore violated the Fourth Amendment’s probable-cause
requirement.

       2. Good Faith

       Generally, evidence obtained in violation of the Fourth Amendment must be excluded.
See United States v. Rice, 478 F.3d 704, 711 (6th Cir. 2007). In United States v. Leon, however,
the Supreme Court recognized a good-faith exception to the exclusionary rule that applies when
“reliable physical evidence [is] seized by officers reasonably relying on a warrant issued by a
detached and neutral magistrate[.]” 468 U.S. 897, 913 (1984). The good-faith exception, the
Court explained, is premised on the conclusion “that the marginal or nonexistent benefits
produced by suppressing evidence obtained in objectively reasonable reliance on a subsequently
invalidated search warrant cannot justify the substantial costs of exclusion.” Id. at 922.

       Leon declined to go so far as to hold “that exclusion is always inappropriate in cases
where an officer has obtained a warrant and abided by its terms.”           Id. Rather, the Court
recognized that exclusion’s benefits outweigh its costs—and “[s]uppression therefore remains an
appropriate remedy”—when a law-enforcement officer lacks “reasonable grounds for believing
that the warrant was properly issued.” Id. at 922–23. A law-enforcement officer lacks such
reasonable grounds, and the good-faith exception is inapposite, in at least four situations:

       (1) where the issuing magistrate was misled by information in an affidavit that the
       affiant knew was false or would have known was false except for his reckless
       disregard for the truth; (2) where the issuing magistrate wholly abandoned his
       judicial role and failed to act in a neutral and detached fashion, serving merely as
       a rubber stamp for the police; (3) where the affidavit was nothing more than a
 Nos. 22-5593/5800                          United States v. Lewis                                          Page 8


        “bare bones” affidavit that did not provide the magistrate with a substantial basis
        for determining the existence of probable cause, or where the affidavit was so
        lacking in indicia of probable cause as to render official belief in its existence
        entirely unreasonable; and (4) where the officer’s reliance on the warrant was not
        in good faith or objectively reasonable, such as where the warrant is facially
        deficient.

Rice, 478 F.3d at 712 (quoting United States v. Hython, 443 F.3d 480, 484 (6th Cir. 2006)).

        In this case, the issue is whether law-enforcement officers reasonably relied on the search
warrant. Lewis argues that the application of the good-faith exception is inapposite because
Detective Gatson’s affidavit was a “bare bones” affidavit.1                     “Suppression . . . remains an
appropriate remedy” when “a warrant [is] based on an affidavit so lacking in indicia of probable
cause as to render official belief in its existence entirely unreasonable.” Leon, 468 U.S. at 923
(internal quotations omitted). “Affidavits that are ‘so lacking in indicia of probable cause’ have
come to be known as ‘bare bones’ affidavits.” United States v. Laughton, 409 F.3d 744, 748 (6th
Cir. 2005). A bare-bones affidavit is an affidavit “that states suspicions, beliefs, or conclusions,
without providing some underlying factual circumstances regarding veracity, reliability, and
basis of knowledge[.]” United States v. Weaver, 99 F.3d 1372, 1378 (6th Cir. 1996). Put
differently, a bare-bones affidavit is “a conclusory affidavit” that “states only the affiant’s belief
that probable cause existed.” United States v. Williams, 224 F.3d 530, 533 (6th Cir. 2000)
(quotation omitted).

        We agree with Lewis that the law-enforcement officers did not reasonably rely on
Detective Gatson’s affidavit because the affidavit was a bare-bones affidavit.                            Although
Detective Gatson’s affidavit fell well short of establishing probable cause, “[a]n affidavit cannot
be labeled ‘bare bones’ simply because it lacks the requisite facts and inferences to sustain the
magistrate’s probable-cause finding[.]” United States v. White, 874 F.3d 490, 497 (6th Cir.
2017). Rather, the affidavit “must be so lacking in indicia of probable cause that, despite a
judicial officer having issued a warrant, no reasonable officer would rely on it.” Id. Considering
the complete lack of factual information included in Detective Gatson’s affidavit, we hold that

        1Lewis also argues that the other three situations in which the good-faith exception is inapposite are present
here. Because we agree that Detective Gatson’s affidavit was a bare-bones affidavit, we decline to reach Lewis’s
other arguments.
 Nos. 22-5593/5800                    United States v. Lewis                               Page 9


no reasonable officer would rely on the affidavit to establish probable cause to believe that
Lewis’s electronic devices would contain evidence of a child sexual-exploitation offense or any
other crime.

       As discussed above, the non-boilerplate portion of Detective Gatson’s affidavit begins by
stating that “[a]n HSI investigation identified Edward L Lewis . . . as a person of interest.”
R. 24-3 (Gatson Aff. at 4) (Page ID #105). The affidavit does not explain what “HSI” stands for,
why HSI considered Lewis to be a person of interest, or the significance of HSI’s person-of-
interest designation. Reading that initial portion of Detective Gatson’s affidavit, a judge would
have no factual basis upon which to conclude that Lewis may have committed any crime, let
alone the specific crime of child sexual exploitation as defined by Kentucky law.

       Next, the affidavit states that Lewis “consent[ed] to [a] search [of] his laptop and cell
phone” and that “[d]uring [the] search it became apparent that Mr. Lewis had used his laptop to
view images of child sexual exploitation.” Id. This section clearly expresses Detective Gatson’s
belief that Lewis had committed a crime, but it does not provide a factual basis upon which a
magistrate could independently reach that conclusion. Indeed, Detective Gatson’s conclusion
that “it became apparent that” Lewis had “view[ed] images of child sexual exploitation” was “a
mere conclusory statement that [gave] the magistrate virtually no basis at all for making a
judgment regarding probable cause.” Illinois v. Gates, 462 U.S. 213, 239 (1983). A magistrate
could conclude that there was probable cause to search Lewis’s electronic devices only by
substituting Detective Gatson’s evaluation of the evidence for the magistrate’s own evaluation.

       Lastly, the affidavit states that “[b]ased on [Detective Gatson’s] knowledge, experience
and training, Edward L Lewis has demonstrated a pattern of criminal activity related to child
pornography, and there is a reasonable likelihood that the user treats child pornography as a
valuable commodity to be retained and collected, a characteristic common to many people
interested in child pornography.” R. 24-3 (Gatson Aff. at 4) (Page ID #105). This final
statement likewise fails to set forth any factual information. It is tantamount to a statement that
“probable cause existed”—the very definition of a conclusory statement. Williams, 224 F.3d at
533.
 Nos. 22-5593/5800                      United States v. Lewis                             Page 10


          Taking a step back and considering Detective Gatson’s affidavit under the totality of the
circumstances, “the combined boilerplate language and minimal . . . information provide few, if
any, particularized facts of an incriminating nature and little more than conclusory statements of
affiant’s belief that probable cause existed regarding criminal activity.” Weaver, 99 F.3d at
1379. By omitting the essential facts of his investigation and communicating only his bottom-
line conclusion, Detective Gatson asked the magistrate to find probable cause based solely on his
say-so.     “No reasonable officer could have believed” under those circumstances “that the
affidavit was not so lacking in indicia of probable cause as to be reliable.” Laughton, 409 F.3d at
751.

          Our conclusion is consistent with United States v. White. 874 F.3d 490. White addressed
a search-warrant affidavit stating that an investigator had received information that White was
selling marijuana from a residence and that the investigator had used a confidential source to
purchase marijuana directly from White in the driveway outside that same residence. Id. at 494.
Rejecting White’s argument that the affidavit was a bare-bones affidavit, we contrasted the
affidavit with those held to be insufficiently detailed in Nathanson v. United States, 290 U.S. 41
(1933), and Aguilar v. Texas, 378 U.S. 108 (1964). White, 874 F.3d at 498–99.

          “In Nathanson, the affiant stated under oath that ‘he has cause to suspect and does believe
that’ liquor illegally brought into the United States ‘is now deposited and contained within the
premises’ belonging to the defendant.” Id. at 498 (quoting Nathanson, 290 U.S. at 44). And
“[i]n Aguilar, the affiants stated that they ‘received reliable information from a credible person
and do believe that heroin, marijuana, barbiturates and other narcotics and narcotic paraphernalia
are being kept at the above described premises for the purpose of sale and use contrary to the
provisions of the law.’” Id. (quoting Aguilar, 378 U.S. at 109). White explained that “[t]hese
affidavits were wholly inadequate—what we would call ‘bare bones’ nowadays—because they
presented ‘a mere affirmation of suspicion and belief without any statement of adequate
supporting facts.’” Id. (quoting Nathanson, 290 U.S. at 46; Aguilar, 378 U.S. at 113–14). By
contrast, the investigator in White “showed his work, explaining that White engaged in a
recorded drug deal on the premises, that White had a history of drug offenses, and that White had
dogs inside the residence.” Id. at 499.
 Nos. 22-5593/5800                     United States v. Lewis                               Page 11


       The affidavit here much more closely resembles the bare-bones affidavits in Nathanson
and Aguilar than the affidavit in White. The White investigator “showed his work[.]” Id. He
stated in his affidavit that he had “received information that marijuana was being sold . . . by . . .
White” at a particular address and that the investigator “initiated a controlled purchase of
marijuana with the use of a confidential source” from White outside that same residence. Id. at
494. This information would allow a magistrate to make an independent finding that White had
sold marijuana, and to infer that it was possible that additional marijuana could be found inside
the home. Detective Gatson, by contrast, skipped over his work. He stated in his affidavit that
he searched Lewis’s laptop and cell phone and that “it became apparent that Mr. Lewis had used
his laptop to view images of child sexual exploitation.” R. 24-3 (Gatson Aff. at 4) (Page ID
#105). Nowhere did he explain the evidence that compelled him to reach that conclusion; the
investigative process that was explained in White went left unsaid here. Like the Nathanson and
Aguilar affidavits, then, Detective Gatson’s affidavit was “wholly inadequate . . . because [it]
presented ‘a mere affirmation of suspicion and belief without any statement of adequate
supporting facts.’” White, 874 F.3d at 498 (quoting Nathanson, 290 U.S. at 46; Aguilar, 378
U.S. at 113–14). No reasonable officer would rely on Detective Gatson’s affidavit to establish
probable cause to believe that Lewis’s electronic devices contained evidence of child sexual
exploitation.

       The government suggests that “reasonable inferences” can rescue Detective Gatson’s
affidavit. “[R]easonable inferences that are not sufficient to sustain probable cause in the first
place may suffice to save the ensuing search as objectively reasonable.”           Id. at 500. For
example, United States v. Paull held that the good-faith exception applied where a search
warrant for evidence of child pornography “relied on events that were at least thirteen months
[after] the last time the accused subscribed to the suspect website.” 551 F.3d 516, 522 (6th Cir.
2009) (internal quotation omitted). Paull reasoned that “[t]o the extent that one is persuaded that
there are gaps in the evidence caused by the delay between the investigation and the search, they
were filled in by [the affiant’s] experience, whose familiarity with consumers of child
pornographers gave her adequate reason to suspect that Paull continued to possess illegal
images.” Id. at 523.
 Nos. 22-5593/5800                    United States v. Lewis                             Page 12


       No comparable inference can be drawn here. The flaw in Detective Gatson’s affidavit is
not that it does not explicitly draw connections between information included in the affidavit or
explain the inferences needed to support probable cause. Rather, the inescapable flaw is that the
affidavit does not identify a sufficient factual basis for believing that Lewis’s devices contained
evidence of child pornography. Paull and White hold that a court may draw certain reasonable
inferences from the information presented in a search warrant affidavit. But neither decision
suggests that a court can “infer” facts that are entirely missing from the affidavit. Yet that is
what a magistrate would have to do to save Detective Gatson’s warrant: the magistrate would
have to “infer” that Detective Gatson possessed sufficient—yet undisclosed—evidence to
support his conclusion that it was “apparent that Mr. Lewis had used his laptop to view images of
child sexual exploitation.” R. 24-3 (Gatson Aff. at 4) (Page ID #105). If a court could simply
presume that sufficient evidence supported a law-enforcement affiant’s “suspicions, beliefs, or
conclusions,” no affidavit would ever be held to be bare bones. Weaver, 99 F.3d at 1378.

       Under these circumstances, application of the good-faith exception would be
inappropriate. The purpose of the exclusionary rule “is to deter future Fourth Amendment
violations.” Davis v. United States, 564 U.S. 229, 236–37 (2011). The good-faith exception
promotes that purpose by precluding suppression where the remedy would “[p]enaliz[e] the
officer for the magistrate’s error, rather than his own[.]” Leon, 468 U.S. at 921. Where “the
officer’s reliance on the magistrate’s probable-cause determination” is “entirely unreasonable[,]”
however, suppression promotes deterrence and the good-faith exception is inapposite Id. at 922–
23. That is the case here.

       Neither the laws nor the facts are complex. A law-enforcement officer with as much
training and experience as Detective Gatson—and indeed any reasonable law-enforcement
officer—should know that a warrant affidavit must provide enough non-conclusory information
to allow a neutral magistrate to determine whether there is probable cause. See Nathanson, 290
U.S. 41; Aguilar, 378 U.S. 108. And here, providing the magistrate with those facts would have
been straightforward: officers found incriminating evidence on Lewis’s computer and Lewis
made incriminating statements during their conversation. Yet Detective Gatson chose not to
provide that information in his affidavit. See R. 24-3 (Gatson Aff. at 4) (Page ID #105); R. 35
 Nos. 22-5593/5800                    United States v. Lewis                              Page 13


(Hr’g Tr. at 49) (Page ID #245).       As a result, law-enforcement officers searched Lewis’s
electronic devices based on an affidavit that any reasonable officer would have known lacked
sufficient information to establish probable cause. Rejecting the application of the good-faith
exception is necessary to demonstrate that Detective Gatson and the other officers had a duty to
ensure that the affidavit was free of obvious constitutional defects and to underscore the costs of
not discharging that duty.

       For all these reasons, we conclude that the good-faith exception is inapplicable here. A
search-warrant affidavit that states only the affiant’s conclusory belief that a suspect committed a
crime is a bare-bones affidavit that cannot establish probable cause to search and that precludes
application of the good-faith exception to the exclusionary rule. Because the search warrant here
was supported by only Detective Gatson’s bare-bones affidavit, the warrant did not authorize
law-enforcement officers to search or seize Lewis’s electronic devices and the fruits of those
searches must be excluded unless an exception to the Fourth Amendment’s warrant requirement
applies.

B. Exceptions to the Warrant Requirement

       Warrantless searches and seizures “are per se unreasonable under the Fourth
Amendment—subject only to a few specifically established and well-delineated exceptions.”
Mincey v. Arizona, 437 U.S. 385, 390 (1978) (quoting Katz v. United States, 389 U.S. 347, 357
(1967)). Thus, the evidence recovered from Lewis’s electronic devices must be suppressed
unless an exception to the warrant requirement permitted the search and seizure of the devices.
The government invokes two exceptions: consent and the plain-view doctrine.

       1. Consent

       The government first contends that Lewis consented to the search and seizure of his
electronic devices. Consent is an exception to the Fourth Amendment’s warrant requirement.
Schneckloth v. Bustamonte, 412 U.S. 218, 219 (1973). Lewis concedes that he consented to an
initial search of his laptop and cell phone and that Detective Gatson and forensic examiner
Rollins were entitled to perform that search without first securing a warrant. Lewis argues,
 Nos. 22-5593/5800                   United States v. Lewis                              Page 14


however, that he did not consent to the seizure or subsequent forensic examination of his
electronic devices.

       The district court found that Lewis consented to the initial search of his laptop and cell
phone performed by Rollins at Lewis’s home, but that the law-enforcement officers exceeded the
scope of Lewis’s consent when they seized his electronic devices and later forensically examined
them. Lewis II, 591 F. Supp. 3d at 183–85. “The district court’s determination of whether a
search” or seizure “exceeded the scope of consent is a question of fact that we review for clear
error.” United States v. Garrido-Santana, 360 F.3d 565, 570 (6th Cir. 2004). “A factual finding
will only be clearly erroneous when, although there may be evidence to support it, the reviewing
court on the entire evidence is left with the definite and firm conviction that a mistake has been
committed.” United States v. Henry, 429 F.3d 603, 608 (6th Cir. 2005) (quoting United States v.
Oliver, 397 F.3d 369, 374 (6th Cir. 2005)).

       “The standard for measuring the scope of a suspect’s consent under the Fourth
Amendment is that of ‘objective’ reasonableness—what would the typical reasonable person
have understood by the exchange between the officer and the suspect?” Florida v. Jimeno, 500
U.S. 248, 251 (1991). To determine what a reasonable person would have understood the scope
of their consent to be, we look to the “expressed object” of the search or seizure. Id. A
reasonable person who consents to the search of his car for narcotics, for example, would
understand that the law-enforcement officer could “search containers within that car which might
bear drugs.” Id.

       The parties agree that Lewis consented to the initial search of his laptop and cell phone at
his home. Detective Gatson specifically told Lewis that he was looking for evidence of child
pornography and asked Lewis “if he would mind if someone came over and looked at . . . his
devices” for that evidence. R. 35 (Hr’g Tr. at 13) (Page ID #209). Lewis did not object to
Detective Gatson’s request, and he then signed a consent-to-search form that authorized “a
complete search of the premises, property or vehicle located at [his address] and more
particularly described as Samsung Galaxy Note 9 [and] HP Pavilion Laptop[.]”              R. 26-2
(Consent Form at 1) (Page ID #141). Lewis was then present as Rollins searched and generated
the preview of his laptop and looked through his phone. R. 35 (Hr’g Tr. at 20–26) (Page ID
 Nos. 22-5593/5800                     United States v. Lewis                                Page 15


#216–22).      Lewis never attempted to withdraw his consent while Rollins performed these
searches or generated the preview of his laptop. Id. at 28 (Page ID #224). A reasonable person
would have understood these events to authorize Detective Gatson and Rollins to search Lewis’s
laptop and cell phone for evidence of child pornography and to generate the preview of Lewis’s
laptop.

          The government argues that Lewis also consented to the seizure and forensic examination
of his electronic devices. The district court rejected the government’s argument, finding that
nothing in Lewis’s exchange with Detective Gatson or the other law-enforcement officers would
suggest to a reasonable person that Lewis had consented to anything more than the initial search
of his devices. The district court’s findings are consistent with Lewis’s exchange with the law-
enforcement officers and those officers’ actions, and therefore are not clearly erroneous.

          At the suppression hearing, Detective Gatson, Special Agent Minnick, and Special Agent
Even testified that Detective Gatson asked Lewis something to the effect of whether he
“mind[ed] if [they] look[ed]” at his devices. Id. at 78 (Page ID #274); see also id. at 15 (Page ID
#211) (Detective Gatson recounting that he asked Lewis “if he would mind . . . if we could look
at his devices”); id. at 64 (Page ID #260) (Special Agent Minnick testifying that Detective
Gatson asked Lewis “for consent to search some media”). None of the law-enforcement officers
testified that Lewis was asked for his consent to seize his devices or to a perform a second, more
invasive search of the devices at a state forensic laboratory, or that he voluntarily consented to
those actions.

          Although Lewis signed a consent form that authorized “a complete search” (but not a
seizure) of his “premises, property or vehicle[,]” R. 26-2 (Consent Form at 1) (Page ID #141),
Detective Gatson said that he understood Lewis to be “giving consent for a forensic examiner to
come out and preview devices” and not “to come out and look around” more broadly, see R. 35
(Hr’g Tr. at 43) (Page ID #239). Detective Gatson’s stated understanding of the limited scope of
Lewis’s consent is consistent with the actions that he and other officers took before, during, and
after the initial search of Lewis’s laptop and cell phone. As just noted above, Detective Gatson
asked Lewis for his consent to have Rollins come to Lewis’s home and look through his laptop
and cell phone, not to engage in an exhaustive examination of all of Lewis’s devices or to
 Nos. 22-5593/5800                   United States v. Lewis                             Page 16


conduct a forensic examination of them. R. 35 (Hr’g Tr. at 43) (Page ID #239). After Rollins
searched Lewis’s laptop and cell phone, Detective Gatson told Lewis that he was placing him
under arrest, that the consent search was complete, and that he would seek a search warrant for
Lewis’s devices.     Id. at 25–28 (Page ID #221–24); see also Appellant Reply Br. at 6
(transcribing recorded conversation). Lewis was then transported to jail, and Detective Gatson
left Lewis’s home while the agents stood guard outside of it. Id. at 26–29, 51–52 (Page ID
#222–25, 247–48).

       The district court did not clearly err in finding that Detective Gatson and the other law-
enforcement officers exceeded the scope of Lewis’s consent when they seized his electronic
devices and forensically examined them. As the district court observed, searches and seizures
implicate different Fourth Amendment interests. See Horton v. California, 496 U.S. 128, 133
(1990); see also Soldal v. Cook County, 506 U.S. 56, 66 (1992). Nothing in Lewis’s exchange
with Detective Gatson or in the law-enforcement officers’ actions would suggest to a reasonable
person that Lewis had consented to the seizure of all the electronic devices in his home. The
officers did not ask for his consent to seize, and the consent form Lewis signed did not authorize
a seizure. Further, all agree that Lewis allowed Rollins to search his devices while Rollins,
Lewis, and the law-enforcement officers were present in Lewis’s home.             But the events
recounted above demonstrate that Detective Gatson and the other officers reached the limit of
Lewis’s consent once they terminated the consent search, arrested Lewis, and left his home to
obtain a search warrant. Thus, Lewis’s consent did not authorize the seizure and forensic
examination of his devices.

       2. Plain View

       The government invokes one other exception to the Fourth Amendment’s warrant
requirement: the plain-view doctrine. “Under [the plain-view] doctrine, if police are lawfully in
a position from which they view an object, if its incriminating character is immediately apparent,
and if the officers have a lawful right of access to the object, they may seize it without a
warrant.” Minnesota v. Dickerson, 508 U.S. 366, 375 (1993). The government argues that
Detective Gatson and Rollins were entitled to seize Lewis’s electronic devices and later
 Nos. 22-5593/5800                    United States v. Lewis                             Page 17


forensically search them after they saw incriminating file names on the laptop during the initial
consent search.

       The government’s plain-view argument falls flat. To start, the argument is forfeited. The
government did not invoke the plain-view doctrine in the district court proceedings below. See
generally R. 26-1 (Gov’t Suppression Mem.) (Page ID #131–40); R. 35 (Suppression Hr’g Tr.)
(Page ID #197–281). It was not until the government filed its brief with this court that it cited
the doctrine for the first time.   We have made clear under similar circumstances that the
government is subject to the same forfeiture rules as any other litigant. See United States v.
Russell, 26 F.4th 371, 376 (6th Cir. 2022); United States v. Noble, 762 F.3d 509, 526–28 (6th
Cir. 2014). Given its forfeiture, “the government must show that the forfeited error was clear
and affected its substantial rights.” Russell, 26 F.4th at 376. The government cannot do so here.

       The plain-view doctrine permits certain warrantless seizures, not searches. See Hopkins
v. Nichols, 37 F.4th 1110, 1118 (6th Cir. 2022). Here, the government did not uncover the
evidence Lewis seeks to suppress until after it seized his devices and then forensically examined
them at the state laboratory. See R. 35 (Hr’g Tr. at 23, 31, 47–48) (Page ID #219, 227, 243–44).
During the suppression hearing, Detective Gatson confirmed that the evidence that formed the
basis of the charges brought against Lewis were the files recovered after the electronic devices
were seized and forensically examined at the state laboratory, and not the results of the preview
search conducted at Lewis’s home. Id. Thus, even if we agreed with the government that the
plain-view doctrine permitted the law-enforcement officers to seize Lewis’s laptop and cell
phone, cf. United States v. Herndon, 501 F.3d 683, 686, 692–94 (6th Cir. 2007) (plain-view
doctrine permitted warrantless seizure of laptop and hard drives that were later searched in
greater detail pursuant to a search warrant), the officers still would need some other Fourth
Amendment justification to conduct the complete forensic examination of the devices. See
Horton, 496 U.S. at 141 & n.11 (noting that “the seizure of an object in plain view does not
involve an intrusion on privacy” and that when the “item is a container . . . it may only be opened
pursuant to either a search warrant . . . or one of the well-delineated exceptions to the warrant
requirement.”). The plain-view doctrine cannot provide that justification, and therefore the
government has not shown plain error.
 Nos. 22-5593/5800                  United States v. Lewis                             Page 18


                                     III. CONCLUSION

       Lewis consented to the initial search of his laptop and cell phone performed at his home,
and the law-enforcement officers’ account of that search and the preview generated during the
search were validly obtained and are admissible under the Fourth Amendment.           All other
evidence taken from Lewis’s electronic devices, by contrast, was obtained through searches and
seizures that were not supported by a valid warrant or a valid claim to an exception to the
warrant requirement. Accordingly, we REVERSE the district court’s order denying Lewis’s
motion to suppress, VACATE Lewis’s conviction, and REMAND for further proceedings.

```

---

## GROUP: content/cases/United States v. Loines.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Loines
type: case
citation: "56 F.4th 1099 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 6th Cir.
court_level: coa
circuit: ca6
year: 2023
date_decided: 2023-01-06
docket: 21-1516
authority_weight: "Binding in-circuit — 6th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9357039/united-states-v-aaron-loines/"
  cluster_id: 9357039
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Loines
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Plain View Doctrine]]"
    role: Key
related:
  - "[[Plain View Doctrine]]"
  - "[[Arizona v. Hicks]]"
  - "[[Texas v. Brown]]"
  - "[[Horton v. California]]"
tags:
  - case
  - fourth-amendment
  - search
  - plain-view
  - probable-cause
  - immediately-apparent
  - automobile-exception
  - sixth-circuit
holding: "The Sixth Circuit reversed the denial of suppression and vacated the conviction, holding that the plain-view doctrine did not supply probable cause to search Loines's car: a detective's claim to have seen a 'bag of dope' through a tinted window was not plausible on the record, and in any event the objects — a plastic bag near a cigar wrapper and a lottery ticket — were not immediately and apparently incriminating from outside the car, their criminal character emerging only after officers entered and closely inspected the console, itself a further search unsupported by probable cause."
---

# United States v. Loines

*56 F.4th 1099 (6th Cir. 2023)* (No. 22-3073) · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9357039 → opinion 9352511 (56 F.4th 1099, decided 2023-01-06, Clay, J.). NOTE: appeal docket is No. 22-3073 (per the opinion caption); the lake stub's docket field reads 21-1516 (stale — flag for S2). Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In April 2020, Cleveland detective Donald Kopchak was investigating Mekhel Rivers for drug trafficking; after surveillance, police obtained and executed a search warrant for Rivers's Euclid, Ohio house. During the search, Kopchak walked to a red Nissan parked on the street, cupped a hand to the tinted window, leaned in, and claimed to see a "bag of dope" — a small plastic bag near a Black & Mild cigar wrapper and a folded lottery ticket — in the center console; a lieutenant said he saw it too. Officers found Aaron Loines inside the house; Loines said the car keys were his (confirmed by sounding the alarm). The Nissan was towed and searched without a warrant, yielding a firearm, suspected narcotics, a press, and a scale. Loines moved to suppress; the government justified the warrantless search solely on the "plain view" of the "bag of dope," with Kopchak the only witness. The district court denied the motion, and Loines pled guilty to controlled-substance and § 924(c) firearm offenses, preserving the appeal.

## Issue
Whether the [[Plain View Doctrine|plain-view doctrine]] gave the officers probable cause to search Loines's vehicle without a warrant — in particular, whether the objects the detective claimed to see through the tinted window were actually in plain view and whether their incriminating character was "immediately apparent."

## Rule
The plain-view exception requires that the item be in plain view, that its incriminating character be **immediately apparent**, that the officer be lawfully positioned to see it, and that he have a lawful right of access. "Immediately apparent" means the object's criminal character is apparent at the time of discovery without further inspection; lawful, innocuous items cannot be seized under the doctrine absent an immediately apparent association with criminal activity. Applying that standard, the court held the predicate failed: "The objects purportedly seen by Kopchak were not immediately and apparently incriminating. Accordingly, the officers lacked probable cause to search the vehicle." — 56 F.4th 1099, slip op. at 13. ^pin-op13

## Application
The court found the detective's account — that he saw a "bag of dope" through the tinted window from outside the car — not plausible on the record: Kopchak never claimed to see narcotics or residue on the lottery ticket, did not claim the cigar wrapper was contraband, and gave no description of the plastic bag as seen from outside. The bag's incriminating character emerged only after the officers entered the vehicle and closely inspected the center console — and that close inspection constituted a further search unsupported by probable cause. Because the innocuous items were not immediately and apparently incriminating, there was no probable cause, so the plain-view rationale failed — and with it the automobile exception, which the government had tied to the same predicate. Having found the objects were not in plain view, the court did not reach whether Kopchak's cupping his hands against the window was itself an unlawful trespass.

## Conclusion
**Reversed, conviction [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]].** Judge Clay wrote for the panel (Cole, Clay, and Mathis, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Loines* is a clean cautionary application of the **plain-view / "immediately apparent"** prong: an officer's bare say-so that he saw contraband through a tinted window does not establish plain view where the item's criminal character becomes apparent only after a closer intrusion — echoing *[[Arizona v. Hicks|Hicks]]* (developing probable cause by closer inspection is itself a search) and the rule that innocuous items are not seizable without an immediately apparent criminal association.

## Appears on
- [[Plain View Doctrine]] — *Key*

## Sources
- [*United States v. Loines*, 56 F.4th 1099 (6th Cir. 2023)](https://www.courtlistener.com/opinion/9357039/united-states-v-aaron-loines/) — pinpoint: slip op. at 13 (not-immediately-apparent / no-probable-cause holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "15e845db3b45043e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "56 F.4th 1099 (2023)", "court": "6th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Loines", "year": "2023"}}
{"assertion_id": "0f34d5ae9ade49ba", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key", "title": "United States v. Loines"}}
{"assertion_id": "14e2465ed821d504", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Circuit reversed the denial of suppression and vacated the conviction, holding that the plain-view doctrine did not supply probable cause to search Loines's car: a detective's claim to have seen a 'bag of dope' through a tinted window was not plausible on the record, and in any event the objects — a plastic bag near a cigar wrapper and a lottery ticket — were not immediately and apparently incriminating from outside the car, their criminal character emerging only after officers entered and closely inspected the console, itself a further search unsupported by probable cause.", "title": "United States v. Loines"}}
{"assertion_id": "99bc2f623f827726", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 6th Cir.", "title": "United States v. Loines"}}
{"assertion_id": "ff1e25854a385e99", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Loines", "varies_by_point": "false"}}
```

### lake record — United States v. Loines

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Loines",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Aaron Loines",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Loines",
    "court": "6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": "2023-01-06",
    "year": 2023,
    "docket": "21-1516",
    "cluster_id": 9357039,
    "lead_opinion_id": 9352511,
    "sibling_ids": [],
    "absolute_url": "/opinion/9357039/united-states-v-aaron-loines/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "56 F.4th 1099",
      "volume": "56",
      "reporter": "F.4th",
      "page": "1099",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "56 F.4th 1099",
        "volume": "56",
        "reporter": "F.4th",
        "page": "1099",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "56 F.4th 1099",
    "official_selection": {
      "court_class": "coa",
      "selected": "56 F.4th 1099",
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
    "date_created": "2026-07-07T18:19:57Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:20:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:20:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-loines--9357039",
      "to_record_id": "United States v. Loines",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Loines

```
                                RECOMMENDED FOR PUBLICATION
                                Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                       File Name: 23a0004p.06

                    UNITED STATES COURT OF APPEALS
                                   FOR THE SIXTH CIRCUIT



                                                             ┐
 UNITED STATES OF AMERICA,
                                                             │
                                    Plaintiff-Appellee,      │
                                                              >        No. 22-3073
                                                             │
        v.                                                   │
                                                             │
 AARON LOINES,                                               │
                                 Defendant-Appellant.        │
                                                             ┘

  Appeal from the United States District Court for the Northern District of Ohio at Cleveland.
                  No. 1:20-cr-00293-2—Donald C. Nugent, District Judge.

                                   Argued: October 27, 2022

                               Decided and Filed: January 6, 2023

                     Before: COLE, CLAY, and MATHIS, Circuit Judges.

                                      _________________

                                            COUNSEL

ARGUED: John J. Spellacy, JOHN J. SPELLACY & ASSOCIATES, CO., Cleveland, Ohio,
for Appellant. Matthew B. Kall, UNITED STATES ATTORNEY’S OFFICE, Cleveland, Ohio,
for Appellee. ON BRIEF: John J. Spellacy, JOHN J. SPELLACY & ASSOCIATES, CO.,
Cleveland, Ohio, for Appellant. Matthew B. Kall, UNITED STATES ATTORNEY’S OFFICE,
Cleveland, Ohio, for Appellee.
                                      _________________

                                             OPINION
                                      _________________

       CLAY, Circuit Judge. Defendant Aaron Loines appeals the district court’s denial of his
pretrial motion to suppress preceding his guilty plea to controlled substance offenses in violation
of 21 U.S.C. §§ 846, 841(a)(1), 841(b)(1)(C); and a firearm offense in violation of 18 U.S.C.
 No. 22-3073                              United States v. Loines                                      Page 2


§ 924(c)(1)(A). For the reasons set forth below, the Court REVERSES the district court’s
denial of Loines’ motion to suppress, VACATES his conviction, and REMANDS the case for
further proceedings consistent with this opinion.

                                            I. BACKGROUND

                                         A. Factual Background

        In 2020, Detective Donald Kopchak of the Cleveland Police Department was aiding in an
investigation into potential drug trafficking activities by Mekhel Rivers, who was subsequently
charged as a co-defendant. Police investigators suspected Rivers of distributing heroin and
fentanyl. During the investigation, on April 21, 2020, Kopchak observed Rivers leaving a house
on East 221st Street, in Euclid, Ohio, driving a red Nissan Ultima to a meeting place to sell drugs
to an informant, and then returning to the same Euclid house.                      After numerous days of
surveillance, investigators determined that Rivers lived at the East 221st Street house, obtained a
search warrant for the house, and executed the warrant on April 30, 2020.

        After arrving at the house, while executing the search warrant, Kopchak again observed
the red Nissan Ultima parked on the street near the residence, bearing the same license plate
number he previously observed. Kopchak walked up to the passenger side of the car, cupped a
hand to the tinted window,1 and leaned in to attempt to see into the vehicle. While leaning
against the vehicle and looking through the window, Kopchak allegedly observed a Black and
Mild cigar wrapper and “a folded piece of paper” in the center console of the car. (Tr. of Mot. to
Suppress Hr’g, R. 142, Page ID #729). From this vantage point, Kopchak claims he was also
able to view a small plastic bag that he immediately identified as “a bag of dope.” (Id. at Page
ID ##726, 729). Lieutenant Charles DiPenti approached the car’s passenger side, looked through
the window, and verbally indicated that he also saw the “bag of dope.” (Id. at Page ID #728).

        After Kopchak purportedly saw the “bag of dope” in the vehicle, he went into the East
221st Street residence. Officers found Loines in Rivers’ residence, along with other individuals


        1InOhio, side windows may be tinted, but they must permit fifty percent of the light through. Ohio Admin.
Code § 4501-41-03(A)(3). The government does not argue that Loines’ tinted windows were in violation of Ohio
law.
 No. 22-3073                               United States v. Loines                                        Page 3


implicated in this case. Kopchak read the individuals their Miranda rights and inquired about car
keys found in the home. In response, Loines volunteered that the keys were his. Kopchak then
confirmed that the car keys belonged to the Nissan by using the key to sound the car alarm.

        The car was then towed for an inventory search. During the inventory search of the
inside of the car, the officers took a picture of the car’s center console from the driver’s seat.
That picture showed a small plastic bag underneath a cigar wrapper, with a lottery ticket placed
beside it. Law enforcement searched the vehicle after it was towed and found a firearm, the bag
of suspected narcotics, a larger bag of purported narcotics,2 a press,3 and a scale. Police did not
obtain a warrant to search the automobile before or during the investigation.

        Loines moved to suppress the evidence seized from his vehicle, and during the motion to
suppress hearing, Kopchak sought to justify the warrantless search by averring that he had
probable cause to search the vehicle based on the “plain view” of the “bag of dope.” Kopchak
was the only witness called to testify at the hearing. To support Kopchak’s testimony that he
saw the “bag of dope” in plain view and thus had probable cause to search the vehicle, the
government relied upon: (1) videos of Kopchak and other officers walking around and peering
into the car; and (2) a photo taken while inside the car from the vantage point of one sitting in the
driver’s seat.

        Based on Kopchak’s testimony, the videos provided evidence of where the car was in
proximity to the East 221st Street residence, Kopchak’s position looking into the passenger side
window of the car, and Kopchak’s claim that he saw a “bag of dope.” (Tr. of Mot. to Suppress
Hr’g, R. 142, Page ID # 721–26). The videos also provide Lieutenant DiPenti’s perspective


        2The    government has not provided information as to whether the bags found in the vehicle contained
controlled substances. The only information found on the record as to whether a controlled substance was found in
the vehicle is by the government in its response to the Defendant’s motion to suppress in the court below. The
government contends that approximately “70+ of heroin” appeared in the bags and includes a footnote stating that
“[t]he lab tests on this substance showed no scheduled controlled substance.” (Resp. to Mot. to Suppress, R. 61,
Page ID # 338). There is no additional information offered as to what “70 + of heroin” means, or if any lab test was
performed to confirm that the bags found in the car contained controlled substances. However, this issue is not on
appeal. Because the Court finds that the vehicle was not lawfully searched, we need not address whether officers
actually found narcotics in the vehicle.
          3Kopchak defines a press as an object used by drug traffickers to combine, by means of compacting,
different substances together, to prepare the finished product for sale.
 No. 22-3073                         United States v. Loines                               Page 4


when looking through the passenger side window, without pressing his hands against the
window, confirming Kopchak’s observation. The photograph taken from the inside of the
vehicle illustrates a lottery ticket, cigar wrapper, and beneath the cigar wrapper, a small plastic
bag. At issue, however, is whether Kopchak and DiPenti could actually see the small plastic bag
from outside of the car.

       The government claims that the officers’ body camera footage and associated screenshots
“show[] that a person standing next to the car could see through the window, even though it was
partially tinted.” (Resp’t’s Br., ECF No. 15, 14). Furthermore, the government contends that
while no cameras were “positioned at the proper angle to show the suspected drugs,” the videos
establish that an officer could see inside the car. (Id. at 15). Neither proposition is convincing.
The videos themselves do not establish that Kopchak, from his vantage point outside the vehicle,
had a sufficiently clear view to identify the presence of drugs inside the car. Instead, the videos
show only the position of the officers when peering into the vehicle. In an attempt to provide a
better illustration of what was seen from outside the car, screenshots of the video were provided
by the government in their appellate briefing; however, those screenshots are dark to the point of
being indecipherable. Besides conclusory statements as to what officers saw, the government
has furnished no evidence to establish that the photo taken from inside the car was an accurate
depiction of what was seen from outside the vehicle.

                                     B. Procedural History

       A grand jury indicted Loines in the underlying matter on June 11, 2020. The grand jury
charged Loines with the following: one count of Conspiracy to Distribute and Possess with
Intent to Distribute Controlled Substances in violation of 21 U.S.C. § 846; one count of
Possession with Intent to Distribute Controlled Substances in violation of 21 U.S.C. §§ 841(a)(1)
and (b)(1)(C); and one count of Possession of a Firearm in Furtherance of a Drug Trafficking
Crime in violation of 18 U.S.C. § 924(c)(1)(A)(i).

       Loines filed a motion to suppress on December 22, 2020, contending that the
investigating officers conducted an unlawful warrantless search of his vehicle and any inventory
search of the vehicle in question was done improperly. After the government filed its response,
 No. 22-3073                           United States v. Loines                               Page 5


and Loines filed his reply, the district court conducted a suppression hearing on May 17, 2021.
Kopchak was the only witness in the hearing; and the government introduced, without objection,
three videos and one picture. After listening to the testimony and considering the evidence, the
court orally denied Loines’ suppression motion.

          On September 13, 2021, Loines pleaded guilty to all three counts pursuant to a plea
agreement, and reserved the right to appeal the district court’s denial of his motion to suppress.
The district court sentenced Loines to 93 months’ imprisonment, after which Loines filed this
timely appeal.

                                          II. DISCUSSION

                                       A. Standard of Review

          The Court reviews a district court’s decision on a suppression motion for clear error as to
factual findings and de novo as to conclusions of law. United States v. Jenkins, 396 F.3d 751,
757 (6th Cir. 2005). Because the appeal of the district court’s denial of Loines’ suppression
motion is based on factual findings, this Court reviews the decision for clear error. See id.
“Clear error will be found only when the reviewing court is left with the definite and firm
conviction that a mistake has been committed.” Max Trucking, LLC v. Liberty Mut. Ins. Corp.,
802 F.3d 793, 808 (6th Cir. 2015) (citing Anderson v. City of Bessemer City, 470 U.S. 564, 573
(1985)).

          “Whether a search was reasonable under the Fourth Amendment is a question of law
which is reviewed de novo.” United States v. Pearce, 531 F.3d 374, 379 (6th Cir. 2008) (citing
United States v. Blair, 524 F.3d 740, 747 (6th Cir. 2008)). “When a district court has denied the
motion to suppress, we must ‘consider the evidence in the light most favorable to the
government.’” Id. (quoting United States v. Carter, 378 F.3d 584, 587 (6th Cir. 2004) (en
banc)).

                                             B. Analysis

          The Fourth Amendment provides that “[t]he right of the people to be secure in their
persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be
 No. 22-3073                               United States v. Loines                                        Page 6


violated[.]” U.S. Const. amend. IV. “The basic purpose of this Amendment, as recognized in
countless decisions of [the Supreme] Court, is to safeguard the privacy and security of
individuals against arbitrary invasions by governmental officials.” Camara v. Mun. Ct. of City &
Cnty. of S.F., 387 U.S. 523, 528 (1967). “[S]earches conducted outside the judicial process,
without prior approval by judge or magistrate, are per se unreasonable under the Fourth
Amendment—subject only to a few specifically established and well-delineated exceptions.”
Katz v. United States, 389 U.S. 347, 357 (1967) (internal citations omitted). The government
bears the burden of demonstrating that an exception to the warrant requirement applies. United
States v. Jeffers, 342 U.S. 48, 51 (1951).

        Kopchak’s entrance into the car to obtain evidence necessary to indict Loines was subject
to the Fourth Amendment protections. The interior of a vehicle is a constitutionally protected
area, into which a government official is not permitted to intrude without probable cause. See
New York v. Class, 475 U.S. 106, 114–15 (1986) (“[A] car’s interior as a whole is [ ] subject to
Fourth Amendment protection from unreasonable intrusions by the police.”); United States v.
Jones, 565 U.S. 400, 404 (2012) (“It is beyond dispute that a vehicle is an ‘effect’ as that term is
used in the [Fourth] Amendment.”) (quoting United States v. Chadwick, 433 U.S. 1, 12 (1977)).
Officers found the evidence used to indict Loines inside of Loines’ vehicle and without a
warrant. Accordingly, for the search to be reasonable, an exception to the warrant requirement
must apply. See Katz, 389 U.S. at 357. The government asserts that Kopchak’s conduct was
permissible under two exceptions: the “plain view doctrine” and the “automobile exception.”
See Maryland v. Dyson, 527 U.S. 465, 466–67 (1999) (per curiam); Minnesota v. Dickerson, 508
U.S. 366, 374–75 (1993). Neither asserted exception applies in this case.4




        4Loines   argues that the inventory search exception does not apply in this case. However, the inventory
search exception is not properly before this Court. The government explicitly waived the inventory search exception
argument, stating “the government . . . is not relying on [the inventory search exception] directly in this appeal.”
(Resp’t.’s Br., ECF No. 15, 18). To preserve an issue for appellate review, a party must develop its argument in its
appellate briefing; a requirement that the government does not meet on this issue. Puckett v. Lexington-Fayette Urb.
Cnty. Gov’t, 833 F.3d 590, 610–11 (6th Cir. 2016); see also Bolden v. City of Euclid, 595 F. App’x 464, 468 (6th
Cir. 2014).
 No. 22-3073                          United States v. Loines                              Page 7


1. Plain View Doctrine

       The government argues that the bag with the narcotics was in plain view. This claim has
not been substantiated.

       “Warrantless seizures presumptively violate the Fourth Amendment, but under certain
circumstances an officer may seize evidence in plain view without a warrant.” United States v.
Mathis, 738 F.3d 719, 732 (6th Cir. 2013) (citing Arizona v. Hicks, 480 U.S. 321, 326–27
(1987)). “[O]bjects falling in the plain view of an officer who has a right to be in the position to
have that view are subject to seizure and may be introduced in evidence.” Harris v. United
States, 390 U.S. 234, 236 (1968) (citations omitted). Under the plain view doctrine, four factors
must be satisfied: “(1) the item seized must be in plain view, (2) the item’s incriminating
character must be immediately apparent, (3) the officer must lawfully be in the place from where
the item can be plainly seen, and (4) the officer must have a lawful right of access to the item.”
Mathis, 738 F.3d at 732 (citing Horton v. California, 496 U.S. 128, 136–37 (1990)). Loines
argues that the first three elements of the standard are not met; because the Court finds that the
plain view doctrine does not apply in this case, it does not need to reach a determination as to the
fourth factor, which is not argued by either party.

       a. Plain View

       Officer Kopchak testified that he looked through the red Nissan’s passenger side window
and saw a “bag of dope” in plain view in the car’s center console. To support Kopchak’s
testimony, the government points to the photograph taken from inside the vehicle, body camera
footage, and screenshots taken from the body camera footage. However, Kopchak provides no
testimony or evidence as to what was seen of the small, partially obstructed bag from outside the
vehicle. Instead, he simply asserts that he saw a “bag of dope.” (Tr. of Mot. to Suppress Hr’g,
R. 142, Page ID #731–32).

       For the object to be in plain view, Kopchak’s view of the bag must have been from his
vantage point outside the passenger side window. Moreover, he “must discover incriminating
evidence ‘inadvertently’. . . he may not ‘know in advance the location of [certain] evidence and
 No. 22-3073                          United States v. Loines                                Page 8


intend to seize it,’ relying on the plain view doctrine only as a pretext.” Texas v. Brown, 460
U.S. 730, 737 (1983) (quoting Coolidge v. New Hampshire, 403 U.S. 443, 470 (1971)).

         The government’s evidence purported to establish that the plastic bag was plainly visible
from outside the vehicle is deficient, and instead, leads to the opposite conclusion. First, a
photograph taken inside the vehicle from the vantage point of the driver, is insufficient to
demonstrate the bag was visible from outside the car. The only objective evidence provided by
the government illustrating the view from outside the vehicle are three videos from body camera
footage, and two screenshots from those videos. The body camera videos simply provide the
position of the car and each officer, but do not provide the Court with what Kopchak saw when
observing the inside of the vehicle. The screenshots of the footage are dark, the center console is
barely visible, and there is no clear view into the interior of car through the passenger side
window. The screenshots display no small plastic bag, no lottery ticket, and no cigar wrapper.

         Kopchak’s testimony provides support for the Court’s observation: he states that the
twisted plastic was not apparent in the “still frame . . . but there’s another picture that was taken
of the center console with the bag of dope . . . . packaged . . . in those small plastic bags with the
tie off.” (Tr. of Mot. to Suppress Hr’g, R. 142, Page ID #729, 731). This other picture
referenced in Kopchak’s testimony is the photograph taken during the inventory search from
inside the car. Kopchak did not provide testimony as to what he saw from outside the vehicle,
except for the simple statement that he saw a “bag of dope.” (Tr. of Mot. to Suppress Hr’g, R.
142, Page ID #731–32).

         Accordingly, the only evidence supporting the government’s position is Kopchak’s own
unsupported testimony that he saw a bag of narcotics. Simple statements from the officers
contending that they saw “a bag of narcotics” in the car are not enough to establish that an object
was in plain view when the screenshots that the government presented contradict the officers’
statements. This Circuit recognizes that when evaluating an application of the plain view
doctrine, an officer’s testimony can be “sufficient to establish that the [incriminating evidence]
was visible from outside the car.” United States v. Galaviz, 645 F.3d 347, 356–57 (6th Cir.
2011).    In Galaviz the government provided photographic evidence that the incriminating
evidence was visible from outside the car; however, the photo was taken from inside the car at a
 No. 22-3073                          United States v. Loines                               Page 9


position below the window. Id. The court acknowledged that the photo provided by the
government was insufficient to show that the incriminating evidence was visible from outside the
car, but ultimately found that the testimony provided by the officer was enough to prove the
object was in plain view. Id. However, in Galaviz, no evidence contradicted the officer’s
statement. This case is distinguishable in that the photos provided by the government illustrate
that it was implausible for an individual to view the “bag of dope” from outside the car, thereby
directly contradicting the officer’s testimony. The government offers no plausible explanation as
to how the officers could see the “bag of dope” through the tinted window, but the cameras could
not capture any view into the interior of the car.        Had the photo corroborated Kopchak’s
testimony, Galaviz would apply.

       Kopchak, based on his prior observations of the vehicle at issue, may have had a strong
suspicion about the contents of the car, but without any incriminating evidence being in plain
view from outside of the car, Kopchak did not have lawful access to the contents of the car. See
Brown, 460 U.S. at 737. In sum, from the vantage point of an individual looking through the
passenger side window from outside the vehicle, the plastic bag was not in plain view. We
acknowledge that under the clear error standard, if “the district court’s account of the evidence is
plausible in light of the record viewed in its entirety, the court of appeals may not reverse it even
though [the court may be] convinced that had it been sitting as the trier of fact, it would have
weighed the evidence differently.” Anderson, 470 U.S. at 573–74. But even given the great
deference afforded to the district court under the clear error standard, the photographic evidence
provided by the government does not establish that the “bag of dope” was in plain view. In fact,
the photographs plainly and directly contradict the officer’s testimony.

       We find that the district court’s account of the evidence is not plausible in light of the
record viewed in its entirety. Accordingly, the Court reverses the district court’s holding as to
the denial of Defendant’s motion to suppress.
 No. 22-3073                          United States v. Loines                            Page 10


       b. Incriminating Nature is Immediately Apparent

       The government argues that “the way that the powder was packaged and its proximity to
a folded lottery ticket—commonly used to deliver drugs—made the powder’s incriminating
character obvious.” (Resp’t’s Br., ECF No. 15, 20). We disagree.

       To determine whether an object’s incriminating nature is “immediately apparent,” the
Court looks to four instructive factors:

       (1) a nexus between the seized object and the items particularized in the search
       warrant; (2) whether the ‘intrinsic nature’ or appearance of the seized object gives
       probable cause to believe that it is associated with criminal activity; (3) whether
       the executing officers can at the time of discovery of the object on the facts then
       available to them determine probable cause of the object’s incriminating
       nature; . . . . [and (4) whether the officer can] recognize the incriminating nature
       of an object as a result of his immediate or instantaneous sensory perception.

United States v. Garcia, 496 F.3d 495, 510–11 (6th Cir. 2007) (emphasis in original) (quotations
and citations omitted). “Requiring that evidence be ‘immediate’ and ‘apparent’ constrains the
expansion of the limited search authorized by the warrant into a generalized search, and it
prevents officers from having an opportunity to create a reason to expand the search.” United
States v. McLevain, 310 F.3d 434, 440 (6th Cir. 2002) (quoting United States v. McLernon, 746
F.2d 1098, 1125 (6th Cir. 1984)). In considering whether evidence was “apparent” to the
executing officers, courts “should be duly mindful of the executing officers’ particular,
subjective training and experiences.” United States v. Szymkowiak, 727 F.2d 95, 98 (6th Cir.
1984) (first citing Brown, 460 U.S. at 745–46 (Powell, J., concurring); and then citing United
States v. Cortez, 449 U.S. 411, 418 (1981)); see also United States v. Pacheco, 841 F.3d 384,
395–96 (6th Cir. 2016). Probable cause “merely requires that the facts available to the officer
would ‘warrant a man of reasonable caution in the belief’ . . . that certain items may be
contraband or stolen property or useful as evidence of a crime . . . .” Brown, 460 U.S. at 742
(first quoting Carroll v. United States, 267 U.S. 132, 162 (1925); and then citing Brinegar v.
United States, 338 U.S. 160, 176 (1949)).

       Applying the first factor articulated in Garcia, neither Loines nor the vehicle were subject
to the search warrant in this case.        See Garcia, 496 F.3d at 510 (“Requiring particular
 No. 22-3073                         United States v. Loines                             Page 11


descriptions in search warrants prevents police officers from engaging in general exploratory
searches[.]” (citing Coolidge, 403 U.S. at 465)). Therefore, there is no nexus between Loines’
vehicle, parked away from the house, and the items particularized in the search warrant. Even
though the intention of the warrant was to locate controlled substances, the warrant did not
permit law enforcement to search beyond the geographical location described within. This is
especially true considering the officers had ample opportunity to obtain a valid warrant for the
vehicle. See Garcia, 496 F.3d at 510; Coolidge, 403 U.S. at 465. “An overbroad reading of the
immediately apparent requirement subverts and jeopardizes fundamental Fourth Amendment
principles.” Garcia, 496 F.3d at 510.

       As to the remaining Garcia factors, the government relies on two cases to support its
claim that the bag containing the alleged heroin was “immediately apparent.”             First the
government analogizes to Brown, where an officer conducting a routine driver’s license
checkpoint saw narcotics in plain view after the defendant removed his hand from his pocket to
retrieve his license, and dropped on the floor an “opaque, green party balloon, knotted about one
half inch from the tip.” Brown, 460 U.S. at 733. The officer alleged that his previous experience
making arrests for drug offenses informed him that the dropped substance was a narcotic. Id. at
734. The officer’s knowledge of how narcotics are packaged, and the appearance of the balloon,
without knowledge of the contents, were enough to establish that the officer properly seized the
narcotics under the plain view exception. Id. at 743–44. Second, the government references
Pacheco, where an officer conducting a protective frisk of an individual during a traffic stop felt
a solid “brick-like object protruding approximately one inch out of [the defendant’s] cargo
pocket” and determined that the object was “around six-to-eight inches long.” Pacheco, 841
F.3d at 395. The court found that because the object’s incriminating nature was readily apparent,
the seizure was appropriate under the plain view exception. Id. at 396.

       The government argues that that Kopchak was able to identify the “bag of dope”
immediately as the twisted end of the bag resembled items from earlier in the investigation, and
the lottery ticket’s presence corroborated his belief that the plastic he could see was a bag of
narcotics. Further, the government asserts that given Kopchak’s extensive experience in the
field, and that Kopchak had participated in a controlled buy on April 21, 2020, during which
 No. 22-3073                          United States v. Loines                            Page 12


time Rivers used the vehicle to sell drugs to an informant in a package almost identical to the one
seen in this search, the incriminating nature of the plastic bag was readily apparent.

       However, as discussed above, from the vantage point of the street, or through the
Nissan’s tinted windows, the purported bag of narcotics is not visible. What Kopchak saw of the
plastic bag from outside the vehicle, besides a simple statement that he saw a “bag of dope,” has
not been established on the record. However, assuming Kopchak could see inside the car, he
testifies that he could see a Black and Mild cigar wrapper and a lottery ticket from outside the
vehicle. Neither are “intrinsically incriminating.” McLevain, 310 F.3d at 442–43. Officers are
not authorized to seize items “merely because [they are] in ‘plain view.’” Id. at 441 (emphasis in
original) (quoting McLernon, 746 F.2d at 1125). “[L]awful and innocuous items” cannot be
seized under the plain view exception without an immediately apparent association between the
items and the purported criminal activity. Garcia, 496 F.3d at 511; see also McLernon, 746 F.2d
at 1125 (The officer’s immediate perceptions must produce more than “visual images of . . .
‘intrinsically innocent’ items.” (citations omitted)). Innocuous items that could be used for
criminal activity are not enough to establish probable cause. See United States v. Beal, 810 F.2d
574, 577 (6th Cir. 1987).

       Kopchak does not claim to have seen narcotics or any residue on the lottery ticket, makes
no claim that the cigar wrappers could be contraband, and provides no description of the plastic
bag from outside the vehicle. It was not until the officers entered the vehicle and closely
inspected the center console, that the “bag of dope” was observed to be apparently incriminating.
This close inspection of the inside of the car constituted a further search unsupported by probable
cause. See United States v. Tatman, 397 F. App’x 152, 175 (6th Cir. 2010) (“[W]hen an item
appears suspicious to an officer but further investigation is required to establish probable cause
as to its association with criminal activity, the item is not immediately incriminating.”(quoting
McLevain, 310 F.3d at 443)); see also Beal, 810 F.2d at 577. In Pacheco, the officer felt a solid,
brick-like object that was six to eight inches long, whereas in this case, the purported bag of
narcotics is not seen, or descriptively identified, except for the photograph taken inside the
vehicle. See Pacheco, 841 F.3d at 395–96. Similarly, in Brown, the officer, with the aid of a
flashlight, clearly saw an opaque, green party balloon drop from the defendant’s hand. See
 No. 22-3073                        United States v. Loines                             Page 13


Brown, 460 U.S. at 733–34. In this case, by contrast, the purported bag of narcotics was not
apparent when officers looked into the car from the tinted windows.

       The objects purportedly seen by Kopchak were not immediately and apparently
incriminating. Accordingly, the officers lacked probable cause to search the vehicle. See Beal,
810 F.2d at 578 (“[T]his circuit has vigorously adhered to the requirement that probable cause
must be both immediate and apparent.”).

       c. Legally Present

       Loines argues that Kopchak committed trespass when he cupped his hand or hands
against the Nissan’s tinted windows to see inside Loines’ vehicle, and therefore, Kopchak’s
touching of the car is per se unreasonable under the Fourth Amendment. Because we find that
the objects claimed to be seen by Kopchak were not in plain view, the Court need not determine
whether he was legally permitted to place his hand on the car window to facilitate or enhance his
view of the inside of the car.

2. Automobile Exception

       Under the automobile exception, officers may search a vehicle without a warrant if they
have “probable cause to believe that the vehicle contains evidence of a crime.” United States v.
Smith, 510 F.3d 641, 647 (6th Cir. 2007) (first quoting United States v. Lumpkin, 159 F.3d 983,
986 (6th Cir. 1998); and then citing Smith v. Thornburg, 136 F.3d 1070, 1074 (6th Cir.1998)).
Traditionally, this exception was based on the “ready mobility” of the automobile, which created
“an exigency sufficient to excuse failure to obtain a search warrant once probable cause to
conduct the search [was] clear.” Pennsylvania v. Labron, 518 U.S. 938, 940 (1996) (quoting
California v. Carney, 471 U.S. 386, 390–91 (1985)). More recent cases no longer require that
the automobile exception rest on an independent showing of exigency, because “[e]ven in cases
where an automobile was not immediately mobile, the lesser expectation of privacy resulting
from its use as a readily mobile vehicle justified application of the vehicular exception.” Smith,
510 F.3d at 647 (quoting Carney, 471 U.S. at 391).
 No. 22-3073                         United States v. Loines                          Page 14


       The government argues that Kopchak’s belief that the vehicle contained evidence of a
crime was based on the “bag of dope” seen in plain view.           Therefore, according to the
government’s argument, Kopchak was only legally permitted to search the inside of the vehicle
under the automobile exception if the plain view exception applied. As indicated above, because
the “bag of dope” was not in plain view, there was no probable cause to search the vehicle, and
thus, the government does not properly satisfy the automobile exception.

                                      III. CONCLUSION

       For the reasons set forth above, this Court REVERSES the district court’s denial of
Defendant’s motion to suppress, VACATES his conviction, and REMANDS the case for further
proceedings consistent with this decision.

```

---
