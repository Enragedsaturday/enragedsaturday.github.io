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

## GROUP: content/cases/United States v. Neugin.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Neugin"
type: case
citation: "958 F.3d 924 (2020)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Tenth Circuit"
court_level: coa
circuit: 10th
year: 2020
date_decided: 2020-05-01
docket: 19-7043
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2020-05-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Neugin
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4750564/united-states-v-neugin/"
  cluster_id: 4750564
  opinion_id: 4530911
  identity_checked: true
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Recent development (role-based)"
related: ["[[Nix v. Williams]]", "[[Brigham City v. Stuart]]", "[[Horton v. California]]"]
aliases: ["United States v. Neugin (10th Cir. 2020)"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "inevitable-discovery", "community-caretaking", "tenth-circuit"]
holding: "Illustrative application of inevitable discovery where the exception did NOT apply: the chain to discovery was too speculative, so…"
lake:
  record_id: United States v. Neugin
  status: verified
  projected_at: 2026-07-09
---

# United States v. Neugin

*958 F.3d 924 (10th Cir. 2020)* · U.S. Court of Appeals, Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During a domestic-dispute stop, officers let Neugin's wife retrieve her belongings from a truck. Deputy Clinton opened the camper shell on the back of the truck and looked inside without consent, saw a bucket of ammunition, and arrested Neugin, a felon. The truck was later impounded and a shotgun was found. Neugin moved to suppress the ammunition and firearm. The district court denied the motion under the community-caretaking exception, and Neugin appealed.

## Issue
Whether the warrantless opening of the camper was justified by the community-caretaking exception, and, if not, whether the evidence was admissible under the inevitable-discovery exception to the exclusionary rule.

## Rule
The inevitable-discovery exception lets the government avoid suppression only by showing the evidence would have been discovered by lawful means independent of the violation; it cannot rest on speculation. The court reiterated that "the inevitable discovery exception to the exclusionary rule cannot be invoked because of [a] highly speculative assumption of 'inevitability.'" — *United States v. Neugin*, 958 F.3d 924 (10th Cir. 2020) (slip op., at 15) (quoting *United States v. Owens*, 782 F.2d 146, 153 (10th Cir. 1986)). ^pin-op15

## Application
Each link in the asserted chain of inevitability was too speculative. The court reasoned: "Without the violation, therefore, Mr. Neugin would not inevitably have been arrested. And without the arrest, the truck would not inevitably have been impounded and searched." — [*Id.*](https://www.courtlistener.com/opinion/4750564/united-states-v-neugin/#:~:text=Without%20the%20violation%2C%20therefore%2C%20Mr.) ^pin-op15a

The truck sat in a restaurant parking lot, and Neugin could have called his own towing company or a mechanic, so impoundment and an inventory search were not inevitable. Because the unconstitutional opening of the camper is what caused the discovery, the ammunition and shotgun were [[Common Legal Terms#fruit-of-the-poisonous-tree|fruit of the poisonous tree]]: "the police would not have inevitably discovered the evidence absent the Fourth Amendment violation . . . that evidence is fruit of the poisonous tree and should have been suppressed." — *Id.* (slip op., at 17). ^pin-op17

## Conclusion
Opening the camper was an unconstitutional search that neither the community-caretaking nor the inevitable-discovery exception saved; the evidence should have been suppressed, and the Tenth Circuit reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- No negative treatment. *Neugin* is an illustrative application in which [[Inevitable Discovery and Independent Source|inevitable discovery]] **failed**: a speculative chain (arrest → impoundment → inventory) cannot establish that evidence would inevitably have been found.

## Appears on
- [[The Exclusionary Rule]] — *Recent development (role-based)*

## Sources
- *United States v. Neugin*, 958 F.3d 924 (10th Cir. 2020) — https://www.courtlistener.com/opinion/4750564/united-states-v-neugin/ — pinpoints given as slip-opinion pages (CourtListener carries the slip opinion; cluster 4750564 → opinion 4530911).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5f4b9b1a51ddab5a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "958 F.3d 924 (2020)", "court": "U.S. Court of Appeals, Tenth Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Neugin", "year": "2020"}}
{"assertion_id": "59fc9d94619e3c08", "dimension": "support", "kind": "home_role", "locator": {"home": "Inevitable Discovery & Independent Source"}, "payload": {"home": "Inevitable Discovery & Independent Source", "role": "Recent development (role-based)", "title": "United States v. Neugin"}}
{"assertion_id": "b5c0858a788dfae4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Illustrative application of inevitable discovery where the exception did NOT apply: the chain to discovery was too speculative, so…", "title": "United States v. Neugin"}}
{"assertion_id": "14b77a510943e4a1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Neugin"}}
{"assertion_id": "5f88a3cc80cb6f40", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2020-05-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Neugin", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Neugin", "varies_by_point": "false"}}
```

### lake record — United States v. Neugin

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Neugin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Neugin",
    "case_name_short": "Neugin",
    "case_name_full": "",
    "input_case_name": "United States v. Neugin",
    "court": "U.S. Court of Appeals, Tenth Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "2020-05-01",
    "year": 2020,
    "docket": "19-7043",
    "cluster_id": 4750564,
    "lead_opinion_id": 4530911,
    "sibling_ids": [
      4530911
    ],
    "absolute_url": "/opinion/4750564/united-states-v-neugin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "958 F.3d 924",
      "volume": "958",
      "reporter": "F.3d",
      "page": "924",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "958 F.3d 924",
        "volume": "958",
        "reporter": "F.3d",
        "page": "924",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "958 F.3d 924",
    "official_selection": {
      "court_class": "coa",
      "selected": "958 F.3d 924",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op15",
      "page": null,
      "quote": "--- # United States v. Neugin *958 F.3d 924 (10th Cir. 2020)* \u00b7 U.S. Court of Appeals, Tenth Circuit \u00b7 **Binding in-circuit \u2014 10th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a domestic-dispute stop, officers let Neugin's wife retrieve her belongings from a truck. Deputy Clinton opened the camper shell on the back of the truck and looked inside without consent, saw a bucket of ammunition, and arrested Neugin, a felon. The truck was later impounded and a shotgun was found. Neugin moved to suppress the ammunition and firearm. The district court denied the motion under the community-caretaking exception, and Neugin appealed. ## Issue Whether the warrantless opening of the camper was justified by the community-caretaking exception, and, if not, whether the evidence was admissible under the inevitable-discovery exception to the exclusionary rule. ## Rule The inevitable-discovery exception lets the government avoid suppression only by showing the evidence would have been discovered by lawful means independent of the violation; it cannot rest on speculation. The court reiterated that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op15a",
      "page": null,
      "quote": "Without the violation, therefore, Mr. Neugin would not inevitably have been arrested. And without the arrest, the truck would not inevitably have been impounded and searched.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 26229,
      "fragment": "#:~:text=Without%20the%20violation%2C%20therefore%2C%20Mr.",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-op17",
      "page": null,
      "quote": "the police would not have inevitably discovered the evidence absent the Fourth Amendment violation . . . that evidence is fruit of the poisonous tree and should have been suppressed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2020-05-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Neugin",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Chavez",
          "cluster_id": 4848966,
          "cite": [
            "985 F.3d 1234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Neugin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Braxton",
          "cluster_id": 9381854,
          "cite": [
            "61 F.4th 830"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Neugin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. O'Neil",
          "cluster_id": 9384735,
          "cite": [
            "62 F.4th 1281"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Neugin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tolbert",
          "cluster_id": 9476605,
          "cite": [
            "92 F.4th 1265"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Neugin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Elmore",
          "cluster_id": 9505983,
          "cite": [
            "101 F.4th 1210"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Neugin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4530911) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(4530911)",
        "reviewed": 5,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4530911)",
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
    "complete_query": "cites:(4530911)",
    "indexed_citing_opinions": 5,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4530911,
        "count": 5,
        "count_source": "search"
      }
    ],
    "citation_count": 10,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-neugin.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 5,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4530911,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 118354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 163326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 164194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 166076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 166206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 167957,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 168633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 169130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 173471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 202887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 215288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 463621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 577177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 593396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 628620,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 672925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 687706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 708240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 770086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 779347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 781963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4530911,
        "cited_id": 856347,
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
    "date_created": "2026-07-06T01:54:24Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:54:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:54:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:55:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:54:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Neugin

```
                                                                                  FILED
                                                                      United States Court of Appeals
                                        PUBLISH                               Tenth Circuit

                      UNITED STATES COURT OF APPEALS                          May 1, 2020

                                                                         Christopher M. Wolpert
                             FOR THE TENTH CIRCUIT                           Clerk of Court
                         _________________________________

 UNITED STATES OF AMERICA,

       Plaintiff - Appellee,

v.                                                                No. 19-7043

JACK DEWAYNE NEUGIN,

       Defendant - Appellant.
                      _________________________________

                     Appeal from the United States District Court
                        for the Eastern District of Oklahoma
                         (D.C. No. 6:18-CR-00059-RAW-1)
                       _________________________________

Neil D. Van Dalsem, Assistant Federal Public Defender, (Julia L. O’Connell, Federal
Public Defender, with him on the briefs), Office of the Federal Public Defender,
Muskogee, Oklahoma, for Defendant - Appellant.

Linda A. Epperley, Assistant U.S. Attorney, (Brian J. Kuester, U. S. Attorney, and Sarah
McAmis, Assistant U.S. Attorney, with her on the brief), Muskogee, Oklahoma, for
Plaintiff -Appellee.
                       _________________________________

Before HARTZ, EBEL, and MATHESON, Circuit Judges.
                  _________________________________

MATHESON, Circuit Judge.
                   _________________________________

       Jack Dewayne Neugin pled guilty to being a felon in possession of a firearm and

ammunition in violation of 18 U.S.C. §§ 922(g)(1) and 924(a)(2). He pled on the

condition that he could appeal the district court’s denial of his motion to suppress
evidence—the ammunition and firearm—that police found in the bed of his pickup truck.

He argued the officers discovered the evidence during an unconstitutional search under

the Fourth Amendment.

       The officers were responding to a reported verbal altercation between Mr. Neugin

and his girlfriend, Julie Parrish. One of the officers saw ammunition in the back of the

couple’s pickup truck after he lifted the truck’s camper lid to allow Ms. Parrish to retrieve

her belongings. The district court concluded the officer was acting “in a lawful position”

as a “community caretak[er].” ROA at 39. It found no Fourth Amendment violation.

       Exercising jurisdiction under 28 U.S.C. § 1291, we reverse. We conclude that

(1) the officer conducted a search without a warrant or probable cause, (2) the community

caretaking exception to the warrant requirement does not apply, and (3) the inevitable

discovery exception to the exclusionary rule does not apply. The evidence seized should

have been suppressed.

                                   I. BACKGROUND

                                 A. Factual Background

       Cherokee Nation Deputy Buddy Clinton was dispatched to a restaurant parking lot

to respond to a verbal altercation between Mr. Neugin and Ms. Parrish. Their pickup

truck was broken down. Deputy Clinton arrived and found Mr. Neugin sitting on the

curb. Ms. Parrish was in the restaurant.

       While Deputy Clinton and Mr. Neugin talked, Cherokee Nation Sergeant John

Wofford arrived. He stayed with Mr. Neugin while Deputy Clinton went inside the

                                             2
restaurant to help Ms. Parrish arrange a ride. Ms. Parrish told Deputy Clinton she needed

to retrieve her belongings, and Deputy Clinton accompanied her to the truck. Id. at 60.

He and Sergeant Wofford stood at the back of the truck. Id. Deputy Clinton “had Ms.

Parrish stand on the right” and “Mr. Neugin stand on the left” “so there was no

interaction.” Id. Mr. Neugin objected to Ms. Parrish’s taking his grandmother’s jewelry.

Supp. ROA at 7. Without asking, Deputy Clinton opened the lid of the “camper”

attached to the back of the truck. ROA at 60, 68.1

       As he opened the camper, Deputy Clinton looked inside and saw “a large bucket

containing several rounds of ammunition.” Id. at 60. He asked who owned the

ammunition, and Mr. Neugin said he obtained it from a deceased family member.

Deputy Clinton set the bucket aside while Ms. Parrish continued to remove items from

the truck.

       Deputy Clinton requested dispatch to run a background check on Mr. Neugin,

which showed Mr. Neugin was a felon. Deputy Clinton and Sergeant Wofford

determined it was unlawful for Mr. Neugin to possess ammunition or firearms.

       Deputy Clinton asked Mr. Neugin if he had a firearm, and Mr. Neugin said no.

Mr. Neugin declined Deputy Clinton’s request for permission to search the truck, and

explained he purchased the truck for Ms. Parrish.




       1
           The camper was a hard shell covering the truck’s bed.

                                              3
       Deputy Clinton asked Ms. Parrish whether Mr. Neugin had a firearm. She said he

had a shotgun in the truck and had threatened her with it the evening before. Ms. Parrish

told Deputy Clinton that she and Mr. Neugin owned the truck, and she consented to a

search of the vehicle.2

       When Deputy Clinton returned to the truck, he saw the stock of a firearm

protruding from under a suitcase in the back. He asked Mr. Neugin if the firearm

belonged to him, and Mr. Neugin said he did not know where it came from. Deputy

Clinton removed the firearm, which turned out to be a shotgun, and Mr. Neugin was

arrested. The truck was impounded and inventoried.

                              B. Procedural Background

       Mr. Neugin was indicted for firearm and ammunition possession by a felon in

violation of 18 U.S.C. §§ 922(g)(1) and 924(a)(2). He moved to suppress the evidence

seized from the truck as the fruit of an unlawful search. After an evidentiary hearing at

which Deputy Clinton testified, a magistrate judge recommended denial of the motion.

The district court agreed.

       The district court reasoned that Deputy Clinton acted as a “community

caretak[er]” when he opened the camper and therefore did not commit an unconstitutional

search. ROA at 39. It found that the ammunition was in plain view once the camper was


       2
         Deputy Clinton testified that Mr. Neugin said he bought the truck for Ms.
Parrish. Mr. Neugin had the keys, but the seller had not yet transferred the title. The
Government does not contest Mr. Neugin’s standing to bring his Fourth Amendment
challenge.

                                             4
open and became subject to seizure when Deputy Clinton learned Mr. Neugin was a

felon. It also reasoned that once Deputy Clinton saw the ammunition, learned Mr.

Neugin was a felon, heard about Mr. Neugin’s threatening Ms. Parrish with the shotgun,

and saw the shotgun, he had probable cause to arrest Mr. Neugin and seize the

evidence. Alternatively, because the truck was impounded and inventoried, the court said

discovery of the evidence was inevitable.

      Mr. Neugin entered a conditional guilty plea and was sentenced to 60 months in

prison followed by three years of supervised release. He appealed the district court’s

denial of the motion to suppress.

                                      II. DISCUSSION

                                    A. Standard of Review

      In reviewing the denial of a motion to suppress, we accept the district court’s

factual findings unless clearly erroneous. United States v. Moore, 795 F.3d 1224, 1228

(10th Cir. 2015). We “give due weight to inferences drawn from those facts by resident

judges and local law enforcement officers,” Ornelas v. United States, 517 U.S. 690, 699

(1996), and view the evidence in the light most favorable to the government, Moore, 795

F.3d at 1228. We review legal questions de novo. United States v. Hernandez, 847 F.3d

1257, 1263 (10th Cir. 2017).




                                             5
                       B. Legal Background – Fourth Amendment

       This case concerns three areas of Fourth Amendment law: (1) what constitutes a

search, (2) the community-caretaking exception to the warrant requirement, and (3) the

inevitable discovery exception to the exclusionary rule. We address each in turn.

   Search

       The Fourth Amendment protects people from unreasonable government searches

of their “persons, houses, papers, and effects.” U.S. Const. amend. IV. The government

conducts a search “when it infringes on a reasonable expectation of privacy.” United

States v. Ackerman, 831 F.3d 1292, 1307 (10th Cir. 2016). To establish a Fourth

Amendment search, a defendant must show both “a subjective expectation of privacy in

the object of the challenged [intrusion],” and that “society [is] willing to recognize that

expectation as reasonable.” California v. Ciraolo, 476 U.S. 207, 211 (1986); accord

Reeves v. Churchich, 484 F.3d 1244, 1254 (10th Cir. 2007).

       “[A]n individual’s privacy interest in her automobile is constitutionally protected.”

Romo v. Champion, 46 F.3d 1013, 1017 (10th Cir. 1995) (citing California v. Carney,

471 U.S. 386, 390 (1985)). “[T]his protection clearly extends to a car’s trunk.” Id. It is,

therefore, “well settled that a trooper’s opening of a car trunk is a search . . . .” United

States v. Ludwig, 641 F.3d 1243, 1250 (10th Cir. 2011).

   The Warrant Requirement and the Community-Caretaking Exception

       A search typically requires a warrant based on probable cause. See United States

v. Dalton, 918 F.3d 1117, 1127 (10th Cir. 2019). “Searches conducted without a warrant

                                               6
are per se unreasonable under the Fourth Amendment—subject only to a few

‘specifically established and well-delineated exceptions.’” Roska ex rel. Roska v.

Peterson, 328 F.3d 1230, 1248 (10th Cir. 2003) (quoting Katz v. United States, 389 U.S.

347, 357 (1967)).3 Although “the defendant bears the burden of proving whether and

when the Fourth Amendment was implicated,” Hernandez, 847 F.3d at 1263 (quotations

omitted), “[t]he government then bears the burden of proving that its warrantless actions

were justified [by an exception],” United States v. Carhee, 27 F.3d 1493, 1496 (10th Cir.

1994). If the government establishes that an exception to the warrant requirement

applies, the search is constitutional. See United States v. Maestas, 2 F.3d 1485, 1491-92

(10th Cir. 1993). The Government relies on the community-caretaking exception here.4

       The community-caretaking exception allows the government to introduce evidence

obtained through searches that are “totally divorced from the detection, investigation, or

acquisition of evidence relating to the violation of a criminal statute.” Cady v.




       3
        Under the automobile exception to the warrant requirement, “police may search
an automobile and the containers within it where they have probable cause to believe
contraband or evidence is contained.” United States v. Stewart, 473 F.3d 1265, 1270
(10th Cir. 2007) (quotations omitted). Deputy Clinton did not have probable cause to
open the camper, so the automobile exception does not apply.
       4
         The Government also invokes the plain view exception to the warrant
requirement. When an officer “is lawfully positioned in a place from which an object can
be plainly viewed,” . . . the “incriminating character of the object is immediately
apparent,” and “the officer has a lawful right of access to the object,” the officer may
seize the object without a warrant. United States v. Gordon, 741 F.3d 64, 71 (10th Cir.
2014) (quotations omitted). As we explain below, however, the plain view exception
does not apply because the community-caretaking exception does not apply.

                                             7
Dombrowski, 413 U.S. 433, 441 (1973).5 “Noninvestigatory searches of automobiles

pursuant to this function . . . do not offend Fourth Amendment principles so long as such

activities are warranted in terms of state law or sound police procedure, and are justified

by concern for the safety of the general public . . . .” United States v. Lugo, 978 F.2d

631, 635 (10th Cir. 1992) (quotations omitted).

       The government must also point to “specific and articulable facts which

reasonably warrant an intrusion into the individual’s liberty,” and must show that “the

government’s interest . . . outweigh[s] the individual’s interest in being free from

arbitrary governmental interference.” United States v. Garner, 416 F.3d 1208, 1213

(10th Cir. 2005) (quotations omitted and alterations incorporated). Although officers are

entitled to “some latitude in undertaking their community caretaking role,” their actions

must be “reasonably related in scope” to the underlying justification. Lundstrom v.

Romero, 616 F.3d 1108, 1123 (10th Cir. 2010); see also Garner, 416 F.3d at 1213

(explaining that the “scope [of a community-caretaking detention] must be carefully

tailored to its underlying justification”).

       The Supreme Court applied the community-caretaking exception to the warrant

requirement when law enforcement, for safety purposes, removed a defendant’s damaged

car from the highway and later searched the car, including the trunk, under standard


       5
        Although the district court reasoned that Deputy Clinton “was not conducting a
search” because he was community caretaking, ROA at 39, we have treated community
caretaking as an exception to the warrant requirement. See, e.g., United States v.
Thomson, 354 F.3d 1197, 1200 n.1 (10th Cir. 2003).

                                              8
police procedure. Cady, 413 U.S. at 448. We applied the exception when officers

detained a man for questioning after finding him lying in a field and possibly in need of

medical help. Garner, 416 F.3d at 1214.

       By contrast, when an officer found cocaine under an interior door panel while

conducting an inventory search of a damaged car, we declined to apply the exception

because the officer testified to no public danger justifying his removal of the panel.

Lugo, 978 F.2d at 636. Because the officer cited no suspicion that the compartment

contained a weapon, opening it was not community caretaking. Id. We also declined to

apply the exception when, in response to a neighbor’s call regarding a loud argument

between a man and his spouse, police ordered the man to step outside and arrested him

when he declined. Storey v. Taylor, 696 F.3d 987, 996 (10th Cir. 2012). We explained

that “no specific and articulable facts” indicated that seizing the man was “necessary to

protect the safety of [him], his wife, the officers, or others.” Id. (quotations omitted). We

concluded that, “[a]bsent additional facts indicating a greater possibility of violence, a

loud argument between spouses does not suffice to justify a warrantless seizure within

the home.” Id. at 997.

   The Exclusionary Rule and the Inevitable Discovery Exception

       When the government obtains evidence though an unconstitutional search, the

evidence is inadmissible under the exclusionary rule unless an exception applies. Mapp

v. Ohio, 367 U.S. 643, 655-58 (1961); United States v. Knox, 883 F.3d 1262, 1273 (10th

Cir. 2018). “In addition, a defendant may also suppress any other evidence deemed to be

                                              9
‘fruit of the poisonous tree,’ (i.e., evidence discovered as a direct result of the unlawful

activity), by showing the requisite factual nexus between the illegality and the challenged

evidence.” United States v. Olivares-Rangel, 458 F.3d 1104, 1108-09 (10th Cir. 2006)

(citing Wong Sun v. United States, 371 U.S. 471, 488 (1963)). One of the exceptions to

the exclusionary rule is the inevitable discovery doctrine. United States v. Cunningham,

413 F.3d 1199, 1203 (10th Cir. 2005).

       “Although a search may violate the Fourth Amendment, the exclusionary rule is

inapplicable if the evidence inevitably would have been discovered by lawful means.”

United States v. Souza, 223 F.3d 1197, 1202 (10th Cir. 2000). “[T]he government has the

burden of proving by a preponderance of the evidence that the evidence in question

would have been discovered in the absence of the Fourth Amendment violation.” United

States v. Eylicio-Montoya, 70 F.3d 1158, 1165 (10th Cir. 1995). The government may

carry its burden by showing that if police officers had not violated the Fourth

Amendment, they still would have discovered the evidence through a lawful inventory

search of the car. See United States v. Ibarra, 955 F.2d 1405, 1410 (10th Cir. 1992).

       “In determining whether the government has met its burden of proof, we consider

‘demonstrated historical facts,’ not ‘speculative elements.’” United States v. White, 326

F.3d 1135, 1138 (10th Cir. 2003) (quoting Nix v. Williams, 467 U.S. 431, 444 n.5

(1984)); accord United States v. Owens, 782 F.2d 146, 153 (10th Cir. 1986) (“[T]he

inevitable discovery exception to the exclusionary rule cannot be invoked because of [a]

highly speculative assumption of ‘inevitability.’”).

                                              10
                                       C. Analysis

       We first analyze whether Deputy Clinton conducted a search when he opened the

camper and looked in. Finding that he did, we next determine whether the evidence is

admissible under the community-caretaking exception to the warrant requirement or the

inevitable discovery exception to the exclusionary rule. Because neither exception

applies, we reverse the district court’s denial of Mr. Neugin’s motion to suppress.

   Search

       Deputy Clinton searched the back of the truck when he opened the camper and

examined its contents. See Ludwig, 641 F.3d at 1250. The district court concluded, ROA

at 37-38, and the Government does not contest, that Mr. Neugin had a reasonable

expectation of privacy in the inside of the pickup truck. By covering the truck’s bed with

a camper shell, Mr. Neugin manifested an expectation that the contents inside would

remain hidden. As with a closed trunk, “society [would be] willing to recognize that

expectation as reasonable.” Ciraolo, 476 U.S. at 211; see also Romo, 46 F.3d at 1017;

Ludwig, 641 F.3d at 1250. Deputy Clinton intruded on that privacy expectation when he

lifted the latch and looked in. In so doing, he obtained evidence used to charge Mr.

Neugin with a crime. He therefore conducted a search under the Fourth Amendment.6



       6
         The Government contends that when Deputy Clinton “opened the back of the
camper, he was not intending to initiate a search.” Aplee. Br. at 8. United States v.
Jones, 565 U.S. 400 (2012), ostensibly supports this argument. In Jones, the Supreme
Court said law enforcement’s attaching a GPS monitor to the outside of the defendant’s
car was a search under the Fourth Amendment because the officer “physically occupied
private property for the purpose of obtaining information.” Id. at 404. In a footnote
                                             11
   Community-Caretaking Function

       The district court held that opening the camper was constitutional because Deputy

Clinton did so in a community-caretaking role. Mr. Neugin argues that the community-




unrelated to its holding, the Jones Court observed that an “invasion of privacy[] is not
alone a search unless it is done to obtain information.” Id. at 408 n.5.
        For several reasons, we decline to consider, as a possible alternative ground to
affirm, a theory that Deputy Clinton did not conduct a search because he did not intend
“to obtain information” when he opened the camper. Id.
        First, the Government does not cite Jones in its brief, much less develop an
argument based on the footnote. See Harvey v. United States, 685 F.3d 939, 950 n.5
(10th Cir. 2012) (“In exercising [our] discretion [to affirm on an alternative ground] we
consider whether the ground was fully briefed and argued here and below.” (quotations
omitted)); United States v. Carloss, 818 F.3d 988, 992 n.2 (10th Cir. 2016) (declining to
consider an unargued search theory).
        Second, the district court made no findings as to whether Deputy Clinton intended
to obtain information when he opened the camper.
        Third, under longstanding Fourth Amendment law, “[t]he subjective intent of the
law enforcement officer is irrelevant in determining whether that officer’s actions violate
the Fourth Amendment.” Bond v. United States, 529 U.S. 334, 339 n.2 (2000).
        Fourth, after Jones was decided, we recognized in Ackerman, 831 F.3d at 1307,
that the “reasonable expectation of privacy” test remains “one way to determine if a
constitutionally qualifying ‘search’ has taken place.” Consistent with Ackerman, the
Supreme Court has clarified that “[t]he Katz reasonable-expectations test has been added
to, not substituted for, the [Jones] understanding.” Florida v. Jardines, 569 U.S. 1, 11
(2013) (quotations omitted).
        Fifth, Jones involved very different circumstances from this case, and the Court
declined to consider whether officers invaded the defendant’s expectation of privacy.
565 U.S. at 406. Because the reach of Jones is unclear, its footnote dictum that an
“invasion of privacy[] is not alone a search unless it is done to obtain information,” 565
U.S. at 408 n.5, “do[es] not appear to be of the considered sort that would compel us to”
apply it here, Tokoph v. United States, 774 F.3d 1300, 1304 (10th Cir. 2014) as amended
on reh’g (Jan. 26, 2015).
        Without adequate argument from the Government, further direction from the
Supreme Court, and for the other stated reasons, we decline to consider affirming on this
alternative ground.

                                            12
caretaking exception to the warrant requirement does not apply simply because Deputy

Clinton was “trying to help.” Aplt. Br. at 27. We agree with Mr. Neugin.

       The Government has not shown that “state law or sound police procedure”

warranted opening the camper. Lugo, 978 F.2d at 635 (quotations omitted). Nor has it

demonstrated how opening the camper was “justified by concern for the safety of the

general public.” Id. (quotations omitted). Ms. Parrish could have opened the camper

herself, and the Government fails to explain how her doing so might have created any

danger. It identifies “no specific and articulable facts” demonstrating Deputy Clinton

needed to stand behind the tailgate, lift the camper’s hatch, or look into the bed of the

truck. Storey, 696 F.3d at 996 (quotations omitted). Nor was opening the camper

“necessary to protect” Ms. Parrish, Mr. Neugin, the officers, or others. Id. (quotations

omitted).

       The Government points out that Deputy Clinton needed to “separate a feuding

couple.” Aplee. Br. at 12. But this does not explain why he needed to open the camper

or look inside.7 He and Sergeant Wofford could have remained with Mr. Neugin nearby


       7
         The dissent claims that “[i]f Clinton was to mediate the situation, and to prevent
new disputes from escalating animosity, he could not just stand by and allow Ms. Parrish
to rummage through the belongings in the vehicle without being observed.” Dissent at 4.
It cites Mr. Neugin’s “concern that Ms. Parrish would take his grandmother’s jewelry
from the vehicle.” Id.
        But the record does not bear this out. First, the Government points to no evidence
that Mr. Neugin—who was sitting peacefully on the curb when police arrived—would
have turned to violence with two officers on the scene. Second, the officers said they
were not concerned about Ms. Parrish’s taking Mr. Neugin’s property. See ROA at 62
(“[Sergeant Wofford] made the statement that we were not going to worry about the
jewelry, or release it to Ms. Parrish. . . . Right now our main concern was just [letting her
                                                13
while Ms. Parrish retrieved her belongings from the truck.8 Nor was there evidence the

couple was feuding at this time.

       The dissent emphasizes the general importance of law enforcement’s community

caretaking role, observing that “[p]olice must frequently care for those who cannot care

for themselves: the destitute, the inebriated, the addicted and the very young.” Dissent at

1 (quoting Debra Livingston, Police, Community Caretaking, and the Fourth

Amendment, 1998 U. Chi. Legal F. 261, 272 (1998)). We agree. But Ms. Parrish was




get] her personal belongings . . . [and preventing] more altercation.”). Nor would
preventing Ms. Parrish from taking jewelry have supported the community-caretaking
exception to the warrant requirement.
       8
         The dissent notes that “the test of reasonableness in this context is not whether
[the officer] chose the least intrusive alternative.” Dissent at 5. It quotes Cady: “The fact
that the protection of the public might, in the abstract, have been accomplished by ‘less
intrusive’ means does not, by itself, render the search unreasonable.” 413 U.S. 433, 447
(1973). But the words “by itself” show that Cady does not foreclose consideration of an
officer’s failure to pursue nonintrusive means, especially when the intrusion offered no
additional public protection. See United States v. Sanders, 796 F.3d 1241, 1251 (10th
Cir. 2015) (declining to apply the community-caretaking exception when police
impounded an arrestee’s car from a store parking lot “without offering her the
opportunity to make alternative arrangements”).
        Deputy Clinton could have achieved his alleged community-caretaking purpose—
preventing further altercation—simply by standing with Mr. Neugin nearby, or by
standing back and letting Ms. Parrish open the camper. Instead, he opted to invade Mr.
Neugin’s reasonable expectation of privacy, despite clear noninvasive alternatives. See
Garner, 416 F.3d at 1213 (explaining that a community-caretaking intrusion “must be
carefully tailored to its underlying justification.”).

                                             14
none of those. She was perfectly capable of retrieving her belongings without Deputy

Clinton’s “help” in opening the camper and looking inside.9

       Nor do we share the dissent’s view that the invasion of privacy was so “de

minimis” as to except it from the Fourth Amendment’s protection. Dissent at 5. Deputy

Clinton intruded into Mr. Neugin’s enclosed truck without asking, saw contraband, and

made an arrest. His asserted benign motive does not render this reasonable as to Mr.

Neugin. An invasion of privacy is not reasonable simply because the officer assumed his

actions were inoffensive. See, e.g., Brigham City, Utah v. Stuart, 547 U.S. 398, 404

(2006) (In assessing reasonableness, “[t]he officer’s subjective motivation is irrelevant”).

The community-caretaking exception thus does not apply to Deputy Clinton’s Fourth

Amendment violation.10

   Inevitable Discovery

       The Government argues that even if opening the camper was unconstitutional, the

evidence should not have been suppressed because the truck inevitably would have been

impounded and searched. We disagree.




       9
         The dissent claims Deputy Clinton needed to “observe” or “keep an eye on” Ms.
Parrish as she retrieved her belongings. Dissent at 3, 4, 5. But (a) “observing” and (b)
physically opening the camper and looking in are two different things.
       10
         It follows that the plain view exception does not apply because Deputy Clinton’s
violation of the Fourth Amendment enabled him to see the ammunition. See Horton v.
California, 496 U.S. 128, 136 (1990) (explaining the plain view exception applies only
when the officer complies with the Fourth Amendment “in arriving at the place from
which the evidence [is] plainly viewed”).

                                             15
       The Government has not shown that it would have discovered the ammunition and

shotgun if Deputy Clinton had not opened the camper in violation of the Fourth

Amendment. If Deputy Clinton had not opened the camper, we cannot say he inevitably

would have seen the ammunition, run a criminal history check, or found the gun.

Without the violation, therefore, Mr. Neugin would not inevitably have been arrested.

And without the arrest, the truck would not inevitably have been impounded and

searched. The truck was in a restaurant parking lot, and Mr. Neugin could have called his

own towing company or a mechanic. The inevitable discovery exception thus does not

apply. See Owens, 782 F.2d at 153 (“[T]he inevitable discovery exception to the

exclusionary rule cannot be invoked because of [a] highly speculative assumption of

‘inevitability.’”).11




       11
          The dissent contends that “even if Ms. Parrish were the one who opened the lid,
[Deputy Clinton] would [have] need[ed] to stand close to be able to observe what she
took and be sure that she did not harm any property.” Dissent at 5. But any suggestion
that the officers would inevitably have discovered the evidence even if Deputy Clinton
had not opened the camper does not help the Government.
        First, the Government did not brief this alternative inevitable discovery theory.
        Second, even if it had, that theory would not provide a ground to affirm. Although
Ms. Parrish might have opened the camper and one of the officers might have seen the
ammunition, inevitable discovery cannot be based on such speculation. See Owens, 782
F.2d at 153.
        Third, there is reason to doubt Deputy Clinton would have seen the ammunition
had Ms. Parrish opened the camper. The bucket of ammunition was tucked against the
inside of the truck’s tailgate. ROA at 71. Deputy Clinton may not have seen it had he
stood back and let Ms. Parrish approach the truck so she could open the lid. And, to keep
the ammunition hidden, Ms. Parrish might have refrained from opening the camper with
Deputy Clinton watching.

                                           16
                                  III. CONCLUSION

      Deputy Clinton unconstitutionally searched the truck when he opened the camper

and looked in. He exceeded any community-caretaking role, and the police would not

have inevitably discovered the evidence absent the Fourth Amendment violation.

Because the violation caused the discovery of the ammunition and firearm, that evidence

is fruit of the poisonous tree and should have been suppressed. We therefore reverse.12




      12
          The Government argued in district court that Ms. Parrish expressly consented to
a search of the truck when Deputy Clinton asked. But even if she did and had the
authority to consent, she told the officers they could search only after Deputy Clinton
opened the camper and found the ammunition. Her consent thus would not have
validated the initial unconstitutional search.
       As to whether Mr. Neugin implicitly consented to Deputy Clinton opening the
camper, he accompanied the officers to the truck so Ms. Parrish could gather her things.
He stood next to the officers when Deputy Clinton lifted the latch. And he “made no
attempt to stop the officers—through words or otherwise.” United States v. Jones, 701
F.3d 1300, 1321 (10th Cir. 2012) (“[T]he Fourth Amendment requires only that the
police reasonably believe the search to be consensual.” (quotations omitted)). Still, we
decline to affirm on this alternative ground because the Government disclaimed the
argument and the parties did not develop the record regarding the issue. See Oral Arg. at
24:55-27:00.
                                               17
19-7043, United States v. Neugin
HARTZ, Circuit Judge, dissenting.

       I respectfully dissent. In my view the district court correctly ruled that Deputy

Clinton acted lawfully under the community-caretaker doctrine.

       This is an important decision. It has implications for a great deal of the work of

law-enforcement officers. As summarized by then-professor Livingston:

       Community caretaking denotes a wide range of everyday police activities
       undertaken to aid those in danger of physical harm, to preserve property, or
       to create and maintain a feeling of security in the community. It includes
       things like the mediation of noise disputes, the response to complaints
       about stray and injured animals, and the provision of assistance to the ill or
       injured. Police must frequently care for those who cannot care for
       themselves: the destitute, the inebriated, the addicted and the very young.
       They are often charged with taking lost property into their possession; they
       not infrequently see to the removal of abandoned property. In those places
       where social disorganization is at its highest, police are even called upon to
       serve as surrogate parent or other relative, and to fill in for social workers,
       housing inspectors, attorneys, physicians and psychiatrists.

Debra Livingston, Police, Community Caretaking, and the Fourth Amendment, 1998 U.

Chi. Legal F. 261, 272 (ellipses, footnotes, and internal quotation marks omitted); see

also id. at 302 (identifying the responsibilities “to search for missing persons, to mediate

disputes, . . . to aid the ill or injured [,] . . . [and] to provide services in an emergency” as

“a core set of community caretaking activities that have a longstanding tradition and that

have achieved relatively unquestioned acceptance in local communities” (emphasis

added)).

       Courts should be careful about constraining the reasonable conduct of police

officers in performing these functions. To be sure, some constraints are essential. There
must be strong reasons to justify entry into a home without a warrant. See, e.g., Brigham

City, Utah v. Stuart, 547 U.S. 398 (2006); Roska ex rel. Roska v. Peterson, 328 F.3d 1230

(10th Cir. 2003) (unlawful warrantless removal of child from home by social worker).

Programmatic searches and seizures ostensibly for community-caretaking purposes (such

as traffic checkpoints and inventory searches) must be examined to make sure that they

are not pretexts for crime control. See Brigham City, 547 U.S. at 405. And more

generally, tighter restrictions may be required when there is an overlap between

community-caretaking functions and law-enforcement functions. But rather than trying

to pigeonhole each example of community caretaking into doctrine that has been applied

to one particular species of community caretaking (such as protecting property in an

automobile when the driver is no longer present, or entering a home to protect

inhabitants), each type of intrusion should be examined under a general Fourth

Amendment reasonableness standard. See New Jersey v. T.L.O., 469 U.S. 325, 337

(1985) (“[T]he underlying command of the Fourth Amendment is always that searches

and seizures be reasonable[; and] what is reasonable depends on the context within which

a search takes place.”). See generally Livingston, supra. I agree with the First Circuit’s

formulation: “The community caretaking doctrine gives officers a great deal of

flexibility in how they carry out their community caretaking function. The ultimate

inquiry is whether, under the circumstances, the officer acted within the realm of

reason.” Lockhart-Bembery v. Sauro, 498 F.3d 69, 75 (2007) (citation and internal

quotation marks omitted).



                                             2
       One important factor is whether any law-enforcement purpose is implicated. If

there is little likelihood of an officer’s using the community-caretaking doctrine as a

pretext for criminal investigation, there is no need for prophylactic rules to prevent abuse.

In the case before us, the police conduct in question occurred before anyone would have

been thinking about criminal misconduct. There can be no question that Deputy

Clinton’s sole possible purpose before he saw the ammunition was to mediate a dispute.

The court’s reasonableness inquiry should be pursued in that light.

       Clinton’s conduct was eminently reasonable. Defendant and Ms. Parrish had been

traveling together and were having a dispute when their vehicle broke down. Clinton’s

role was to separate them amicably without incident. Some of Ms. Parrish’s belongings

were in the vehicle, and she needed to get them. I would have thought that common

sense (and standard procedure) would require Clinton to keep an eye on her while she

retrieved her things, so there would be no question about what she took and whether she

damaged any of his property in the process. In any event, there were specific reasons to

be concerned about such matters in this case. In Clinton’s initial conversation with

Defendant, Defendant claimed that during his argument with Ms. Parrish in the parking

lot she had thrown one of his cell phones to the ground, breaking the screen, and took the

other into the gift shop.1 When Clinton asked her about the cell phones, she said that the




1
  This information comes from Clinton’s probable-cause affidavit in the tribal
prosecution. The affidavit was an exhibit at the evidentiary hearing before the magistrate
judge. Although it was not formally admitted as evidence, apparently everyone treated it
as evidence. Defendant cites it in his opening brief on appeal.

                                             3
cell phone she had was her own; she admitted throwing a cell phone of Defendant’s at

him, saying that was to keep him from following her into the gift shop, but she said that

the screen had already been broken. Later, Defendant expressed concern that Ms. Parrish

would take his grandmother’s jewelry from the vehicle. She said that she did not have

any jewelry belonging to his grandmother. (The officers ultimately decided that he

should retain the jewelry for the time being.) If Clinton was to mediate the situation, and

to prevent new disputes from escalating animosity, he could not just stand by and allow

Ms. Parrish to rummage through the belongings in the vehicle without being observed.

Even if no personal violence was likely, the community-caretaking exception should

authorize reasonable actions to prevent the theft or destruction of property.2

       In this context, it was proper for Clinton to open the lid of the camper shell. His

duty was to prevent any further problems. See Brigham City, 547 U.S. at 406 (“The role

of a peace officer includes preventing violence and restoring order, not simply rendering

first aid to casualties; an officer is not like a boxing (or hockey) referee, poised to stop a

bout only if it becomes too one-sided.”); cf. Henderson v. City of Simi Valley, 305 F.3d

1052, 1060 (9th Cir. 2002) (officers properly accompanied daughter in retrieving her

property from mother’s home; “[t]hey merely stood by to prevent a breach of the peace”).



2
  The majority opinion asserts that “the officers said they were not concerned about Ms.
Parrish’s taking Mr. Neugin’s property.” Maj. Op. at 13 n.7. But properly understood,
the testimony cited in support of that proposition was only that the officers were not
going to resolve at that time who owned the jewelry. They were in fact concerned about
Ms. Parrish’s taking the jewelry and therefore required her to leave it for the time being.
In any event, the officers’ subjective state of mind is irrelevant.

                                               4
The lid was going to be opened anyway if Ms. Parrish was to obtain her possessions. The

majority opinion acknowledges that “Ms. Parrish could have opened the camper herself.”

Maj. Op. at 13. Clinton’s opening the lid established that he was in control of the

situation, a control that was useful, and perhaps essential, to keeping the parties calm.

And even if Ms. Parrish were the one who opened the lid, he would need to stand close to

be able to observe what she took and be sure that she did not harm any property. (After

all, Defendant had already accused her of damaging one of his cell phones, claiming that

she owned the other, and claiming his grandmother’s jewelry.) His being the one to open

the lid was in itself only a de minimis invasion of anyone’s property or privacy interests.

Doing so was constitutionally permissible. See T.L.O., 469 U.S. at 337 (“The

determination of the standard of reasonableness governing any specific class of searches

requires balancing the need to search against the invasion which the search entails.”

(internal quotation marks omitted)).

       In any event, even if Deputy Clinton could have been a bit more sensitive to the

parties’ privacy and property rights in performing his duties, the test of reasonableness in

this context is not whether he chose the least intrusive alternative. As the Supreme Court

said in Cady v. Dombrowski, the leading Supreme Court decision on community

caretaking, “The fact that the protection of the public might, in the abstract, have been

accomplished by ‘less intrusive’ means does not, by itself, render the search

unreasonable.” 413 U.S. 433, 447 (1973). I do not think it advances the purposes of the

Fourth Amendment or furthers respect for the Constitution to say that it would have been

fine for Deputy Clinton to let Ms. Parrish lift the latch and then watch her every move

                                              5
while in the truck but it would violate the Constitution for him to take charge and lift the

latch himself.

       Because I think that Deputy Clinton did not act unreasonably in his efforts to calm

a domestic dispute, I would affirm the judgment below.




                                              6

```

---

## GROUP: content/cases/United States v. Oliveras.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Oliveras
type: case
citation: "96 F.4th 298 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 2d Cir. 2024
court_level: coa
circuit: ca2
year: 2024
date_decided: 2024-03-15
docket: 21-2954
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
  opinion_url: "https://www.courtlistener.com/opinion/9484364/united-states-v-oliveras/"
  cluster_id: 9484364
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Oliveras
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: Key
related:
  - "[[Special Needs and Administrative Searches]]"
  - "[[Griffin v. Wisconsin]]"
  - "[[Samson v. California]]"
  - "[[United States v. Knights]]"
tags:
  - case
  - fourth-amendment
  - special-needs
  - supervised-release
  - suspicionless-search
  - probation
  - second-circuit
holding: "Under the special-needs doctrine, a district court may impose a special condition of supervised release authorizing a probation officer to conduct suspicionless searches of the defendant's person, property, vehicle, or residence, where the record sufficiently supports it under 18 U.S.C. § 3583(d); but because the district court here made no individualized assessment tying the search condition to the statutory factors, the condition was vacated and remanded even though the special-needs authorization itself was sound."
aliases:
  - United States v. Oliveras
  - "United States v. Oliveras (2d Cir. 2024)"
---

# United States v. Oliveras

*96 F.4th 298 (2d Cir. 2024)* (No. 21-2954) · U.S. Court of Appeals for the Second Circuit · **Binding in-circuit — 2d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9484364 → lead opinion 9950977 (96 F.4th 298, decided 2024-03-15; panel Lynch, Bianco, Pérez, JJ.); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
Alex Oliveras pleaded guilty in the Western District of New York to possessing cocaine with intent to distribute and to possessing a firearm in furtherance of drug trafficking, and was sentenced principally to sixty-three months' imprisonment followed by a three-year term of supervised release. Among the conditions of that release, the district court imposed a special "Search Condition" subjecting Oliveras to suspicionless searches of his person, property, vehicle, residence, or any other property under his control by a probation officer. His sole contention on appeal was that the suspicionless-search condition violated the Fourth Amendment.

## Issue
Whether the "special needs" doctrine permits a district court to impose a special condition of supervised release authorizing a probation officer to conduct suspicionless searches of a supervisee, and whether the condition imposed here was adequately justified.

## Rule
The "special needs" of a supervision system — beyond ordinary law enforcement — can justify departures from the usual warrant and probable-cause requirements, and a supervisee's diminished expectation of privacy makes suspicionless conditions permissible when the record supports them. The panel held: "We conclude that the 'special needs' doctrine of the Fourth Amendment permits, when sufficiently supported by the record, the imposition of a special condition of supervised release that allows the probation officer to conduct a suspicionless search of the defendant's person, property, vehicle, place of residence, or any other property under his or her control." — 96 F.4th 298, slip op. at 2. ^pin-op2

## Application
The Second Circuit rejected Oliveras's categorical Fourth Amendment challenge: recognizing the diminished privacy interests of supervisees and the special needs of probation officers in fulfilling their supervisory role, a suspicionless-search condition can be imposed if sufficiently supported by the record under the § 3583(d) factors. But the doctrine's availability did not save this condition. The district court had made no individualized assessment explaining how a suspicionless-search requirement was reasonably related to the applicable statutory factors in Oliveras's particular case. Because that individualized justification was missing, the court held that imposing the condition exceeded the district court's discretion, [[Reading and Citing Cases#vacated|vacated]] the condition, and [[Reading and Citing Cases#on-remand|remanded]] for the required particularized findings.

## Conclusion
The special-needs authorization for suspicionless supervised-release search conditions was **upheld in principle**, but the condition imposed on Oliveras was **[[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]]** for an individualized § 3583(d) assessment. The panel comprised Lynch, Bianco, and Pérez, Circuit Judges.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Oliveras* extends the *[[Griffin v. Wisconsin|Griffin]]*/*[[Samson v. California|Samson]]*/*[[United States v. Knights|Knights]]* line — the **special-needs / diminished-expectation** rationale for supervising probationers and parolees — to hold that a **suspicionless** search condition is permissible on federal **supervised release** when adequately supported. Teach the two moves separately: the doctrine authorizes such a condition, but § 3583(d) still requires a case-specific, individualized justification before it may be imposed.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key*

## Sources
- [*United States v. Oliveras*, 96 F.4th 298 (2d Cir. 2024)](https://www.courtlistener.com/opinion/9484364/united-states-v-oliveras/) — pinpoint: slip op. at 2 (special-needs authorization of a suspicionless supervised-release search condition; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cbe71f3e0f7e2860", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "96 F.4th 298 (2024)", "court": "2d Cir. 2024", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Oliveras", "year": "2024"}}
{"assertion_id": "9fb76a42795cad61", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key", "title": "United States v. Oliveras"}}
{"assertion_id": "dc204182fe5b4f06", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under the special-needs doctrine, a district court may impose a special condition of supervised release authorizing a probation officer to conduct suspicionless searches of the defendant's person, property, vehicle, or residence, where the record sufficiently supports it under 18 U.S.C. § 3583(d); but because the district court here made no individualized assessment tying the search condition to the statutory factors, the condition was vacated and remanded even though the special-needs authorization itself was sound.", "title": "United States v. Oliveras"}}
{"assertion_id": "5502729b80bad469", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Oliveras", "varies_by_point": "false"}}
{"assertion_id": "5c9e0bfa737ec0d6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 2d Cir.", "title": "United States v. Oliveras"}}
```

### lake record — United States v. Oliveras

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Oliveras",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Oliveras",
    "case_name_short": "Oliveras",
    "case_name_full": "",
    "input_case_name": "United States v. Oliveras",
    "court": "2d Cir. 2024",
    "court_id": "ca2",
    "court_level": "coa",
    "circuit": "ca2",
    "state": null,
    "date_decided": "2024-03-15",
    "year": 2024,
    "docket": "21-2954",
    "cluster_id": 9484364,
    "lead_opinion_id": 9950977,
    "sibling_ids": [],
    "absolute_url": "/opinion/9484364/united-states-v-oliveras/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "96 F.4th 298",
      "volume": "96",
      "reporter": "F.4th",
      "page": "298",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "96 F.4th 298",
        "volume": "96",
        "reporter": "F.4th",
        "page": "298",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "96 F.4th 298",
    "official_selection": {
      "court_class": "state",
      "selected": "96 F.4th 298",
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
    "date_created": "2026-07-06T05:57:05Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:57:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:57:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-oliveras--9484364",
      "to_record_id": "United States v. Oliveras",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Oliveras

```
21-2954
United States v. Oliveras


                      United States Court of Appeals
                                   for the Second Circuit
                            _____________________________________

                                        August Term 2022

                    (Argued: June 30, 2023        Decided: March 15, 2024)

                                           No. 21-2954

                            _____________________________________

                                   UNITED STATES OF AMERICA,

                                             Appellee,

                                             — v. —

                                         ALEX OLIVERAS,

                                       Defendant-Appellant.

                            _____________________________________

Before:                     LYNCH, BIANCO, AND PÉREZ, Circuit Judges.

       Defendant-Appellant Alex Oliveras appeals from a judgment of the United
States District Court for the Western District of New York (Arcara, J.), entered
November 23, 2021, following his guilty plea, sentencing him principally to sixty-
three months’ imprisonment and a three-year supervised release term for
possessing cocaine with intent to distribute in violation of 21 U.S.C. § 841(a)(1) and
(b)(1)(C), and possessing a firearm in furtherance of drug trafficking in violation
of 18 U.S.C. § 924(c)(1)(A)(i). Oliveras’s sole contention on appeal is that the
imposition of a special condition of supervised release that subjects him to
suspicionless searches by a probation officer (the “Search Condition”) violates the
Fourth Amendment.

       We conclude that the “special needs” doctrine of the Fourth Amendment
permits, when sufficiently supported by the record, the imposition of a special
condition of supervised release that allows the probation officer to conduct a
suspicionless search of the defendant’s person, property, vehicle, place of
residence, or any other property under his or her control. However, the district
court exceeded its discretion in imposing that special condition here because it
failed to make the individualized assessment required to support the special
condition under 18 U.S.C. § 3583(d), including a sufficient explanation as to how
the condition is reasonably related in this particular case to the applicable statutory
factors under 18 U.S.C. § 3553(a) and involves no greater deprivation of liberty
than is reasonably necessary under those factors.

       Accordingly, we VACATE the Search Condition and REMAND to the
district court for further consideration of whether it is necessary to impose the
Search Condition in this particular case and, if so, for the district court to explain
the individualized basis for imposing the Search Condition.

                                              TIFFANY H. LEE, Assistant United States
                                              Attorney, for Trini E. Ross, United
                                              States Attorney for the Western District
                                              of New York, Buffalo, NY.

                                              TIMOTHY P. MURPHY, Assistant Federal
                                              Public Defender, Federal Public
                                              Defender’s Office, Buffalo, NY.

JOSEPH F. BIANCO, Circuit Judge:

      Defendant-Appellant Alex Oliveras appeals from a judgment of the United

States District Court for the Western District of New York (Arcara, J.), entered



                                          2
November 23, 2021, following his guilty plea, sentencing him principally to sixty-

three months’ imprisonment and a three-year supervised release term for

possessing cocaine with intent to distribute in violation of 21 U.S.C. § 841(a)(1) and

(b)(1)(C), and possessing a firearm in furtherance of drug trafficking in violation

of 18 U.S.C. § 924(c)(1)(A)(i). Oliveras’s sole contention on appeal is that the

imposition of a special condition of supervised release that subjects him to

suspicionless searches by a probation officer (the “Search Condition”) violates the

Fourth Amendment.

      We conclude that the “special needs” doctrine of the Fourth Amendment

permits, when sufficiently supported by the record, the imposition of a special

condition of supervised release that allows the probation officer to conduct a

suspicionless search of the defendant’s person, property, vehicle, place of

residence or any other property under his or her control. However, the district

court exceeded its discretion in imposing that special condition here because it

failed to make the individualized assessment required to support the special

condition under 18 U.S.C. § 3583(d), including a sufficient explanation as to how

the condition is reasonably related in this particular case to the applicable statutory




                                           3
factors under 18 U.S.C. § 3553(a) and involves no greater deprivation of liberty

than is reasonably necessary under those factors.

      Accordingly, we VACATE the Search Condition and REMAND to the

district court for further consideration of whether it is necessary to impose the

Search Condition in this particular case and, if so, for the district court to explain

the individualized basis for imposing the Search Condition.

                                 BACKGROUND

      On November 27, 2018, Oliveras was charged in an indictment in the

Western District of New York with the following: two counts of possession of

cocaine with intent to distribute in violation 21 U.S.C. § 841(a)(1) and (b)(1)(C)

(Counts One and Two); one count of maintaining a drug-involved premises in

violation of 21 U.S.C. § 856(a)(1) (Count Three); one count of possession of a

firearm in furtherance of drug trafficking in violation of 18 U.S.C. § 924(c)(1)(A)(i)

(Count Four); one count of being a felon in possession of a firearm in violation of

18 U.S.C. §§ 922(g)(1) and 924(a)(2) (Count Five); and one count of possession of a

defaced firearm in violation of 18 U.S.C. §§ 922(k) and 924(a)(1)(B) (Count Six).

      On October 22, 2020, Oliveras pled guilty to Count One (possessing cocaine

with intent to distribute) and Count Four (possessing a firearm in furtherance of



                                          4
drug trafficking), pursuant to a plea agreement with the government.           On

November 23, 2021, the district court sentenced Oliveras principally to sixty-three

months’ imprisonment and a three-year supervised release term. In connection

with the supervised release term, the district court imposed the Search Condition

at issue on this appeal, to which Oliveras objected both in writing prior to the

sentencing and at the sentencing proceeding.

      Prior to Oliveras’s sentencing, the United States Probation Office prepared

a Presentence Investigation Report (“PSR”) in which it recommended a search

condition as a special condition of supervised release. The search condition

initially provided for searches “based upon reasonable suspicion.” United States

v. Oliveras, No. 18-cr-00234, Dkt. No. 82 at 23 (Initial PSR). The Probation Office

subsequently, without explanation, revised the proposed condition to remove the

reasonable suspicion requirement. See Oliveras, No. 18-cr-00234, Dkt. No. 101 at

24 (First Revised PSR). More specifically, the Search Condition provided:

      The defendant shall submit to a search of his person, property,
      vehicle, place of residence or any other property under his control,
      and permit confiscation of any evidence or contraband discovered.
      (This condition serves the statutory sentencing purposes of




                                         5
      deterrence, public      protection,       and   rehabilitation.   18   U.S.C.
      § 3553(a)(2)(B)-(D)).

Id.

      Oliveras did not object to the search condition as initially proposed.

However, in his sentencing submission, he objected to the Search Condition as

revised because it omitted reasonable suspicion as a requirement for any search

by the probation officer. See Oliveras, No. 18-cr-00234, Dkt. No. 106 at 2 (Statement

with Respect to Sentencing Factors).

      In response to Oliveras’s objection, the Probation Office submitted another

revised PSR with an addendum that explained the omission of the reasonable

suspicion language from the Search Condition by relying on this Court’s decision

in United States v. Braggs, 5 F.4th 183 (2d Cir. 2021). Specifically, the PSR stated:

      Under the special needs doctrine, a parole officer may search a
      parolee, without violating the Fourth Amendment, so long as the
      search is reasonably related to performance of the officer’s duties.
      The duties of a parole officer include the supervision, rehabilitation,
      and societal reintegration of parolees, as well as assuring that the
      community is not harmed by parolees being at large. Because a search
      undertaken by a parole officer of a parolee to detect parole violations
      is reasonably related to the parole officer's duties, such a search is




                                            6
      permissible under the special needs doctrine and accordingly
      comports with [the] Fourth Amendment.

Oliveras, No. 18-cr-00234, Dkt. No. 109 at 25 (Second Revised PSR) (citing Braggs, 5

F.4th at 184). The Second Revised PSR also relied on this Court’s reasoning in

United States v. Grimes, 225 F.3d 254 (2d Cir. 2000), and stated:

      [W]hile parolees do not surrender their constitutional protection from
      unreasonable searches and seizures, their status as parolees
      diminishes the extent of their Fourth Amendment protection.
      Parolees may be subject to warrantless searches and seizures by a
      parole officer, as long as the officer's conduct is rationally and
      reasonably related to the performance of his or her duties.

Second Revised PSR at 25. The Probation Office noted that both Braggs and Grimes

involved “individuals under a sentence of state parole supervision,” but

concluded that “the same analysis applies to a defendant who is under a sentence

of supervised release, which is the federal counterpart or equivalent of state

parole.” Id. at 25–26.

      At sentencing, the district judge rejected Oliveras’s objection, imposing the

Search Condition as a special condition of his supervised release and declining to

add the reasonable suspicion requirement.          In doing so, the district judge




                                          7
explained that he had a “problem with the reasonable suspicion requirement”

given his view regarding the nature of supervised release:

       [W]hen you're on supervised release, that [is] to allow [you] out of
       prison at an earlier time. And it seems to me that, all of a sudden, you
       have some legal rights that you would not have when you were in
       prison, and that is a search of the cell based on reasonable suspicion.
       They can search a cell any time whenever they feel.

Joint App’x at 100. The district judge stated that he was “open-minded,” but that

he was “not inclined to put the reasonable suspicion [requirement] in [his]

sentences unless somebody can point to [him] a valid reason why in a particular

case it should” be included. Id. He further clarified:

       So I’m going to not require reasonable suspicion in my sentences. I
       don’t want to say all the time. I always want to keep an open mind
       . . . . [I]t’s my intention that [in] the general case, I will provide [that]
       reasonable suspicion is not required, but I’ll keep an open mind, and
       I’ll note in this case here, I’m not going to require reasonable
       suspicion. I can tell you up front.

Id. at 100-01.

       As to the legal basis for the ruling, the district judge, referring to Braggs,

explained that this Court has “clearly indicated” that reasonable suspicion is not

required. Id. at 101. Further, the district judge stated that “even before [Braggs],”

he “was always somewhat surprised in a way that the probation office was




                                            8
requiring this reasonable suspicion requirement” and that he “just never went

along with it.” Id.

      In response, defense counsel attempted to distinguish Braggs, pointing out

that “Braggs involved a defendant who was on New York State Parole . . . . not a

defendant who was on federal supervised release.” Id. Further, defense counsel

noted that “there has not been a Second Circuit or a United States Supreme Court

decision that has expressly decided that there is anything lower than reasonable

suspicion required for the search of a person's home while on federal supervised

release.” Id. The district judge, however, maintained that reasonable suspicion

should not be required for a probation officer to search a defendant on supervised

release, particularly in this case which involved drugs. The district judge stated

his view, based upon past cases, that individuals convicted of drug offenses “often

are involved in drugs when they’re on supervised release.” Id. at 102. In addition,

the district judge noted that, because “[d]rugs are normally a surreptitious type of

thing” and are not “out in the open generally,” a probation officer should be able

to conduct a search without a showing of reasonable suspicion. Id. Accordingly,




                                         9
the district judge adopted the Search Condition as recommended by the Probation

Department, which included no requirement of individualized suspicion.

      This appeal followed.

                                  DISCUSSION

      This Court generally reviews the imposition of supervised release

conditions for abuse of discretion. United States v. Boles, 914 F.3d 95, 111 (2d Cir.

2019). “When a challenge to a condition of supervised release presents an issue of

law, however, we review the imposition of that condition de novo, bearing in mind

that any error of law necessarily constitutes an abuse of discretion.” Id. (quoting

United States v. McLaurin, 731 F.3d 258, 261 (2d Cir. 2013) (internal quotation marks

omitted)). In addition, “[w]here a condition of supervised release implicates a

constitutional right, we conduct a more searching review in light of the

‘heightened constitutional concerns’ presented in such cases.” United States v.

Eaglin, 913 F.3d 88, 95 (2d Cir. 2019) (quoting United States v. Myers, 426 F.3d 117,

126 (2d Cir. 2005)).

      On appeal, Oliveras challenges the district court’s imposition of the Search

Condition. He contends that the Search Condition is unconstitutional because

suspicionless searches by his probation officer would violate his rights under the



                                         10
Fourth Amendment. Oliveras also argues that the condition is unreasonable

because the district court did not make an individualized assessment for imposing

the Search Condition, nor sufficiently state its reasons for doing so.

      For the reasons set forth below, we conclude that a suspicionless search

condition for an individual on supervised release is permissible under the Fourth

Amendment, when supported by the record, because a supervisee has a

diminished expectation of privacy and the effective administration of supervised

release by a probation officer presents a “special need” that “permit[s] a degree of

impingement upon privacy that would not be constitutional if applied to the

public at large.” United States v. Reyes, 283 F.3d 446, 461 (2d Cir. 2002) (internal

quotation marks and citation omitted). However, we also conclude that the

district court exceeded its discretion in imposing the Search Condition here

because it did not make an individualized assessment as to the need for the

imposition of the Special Condition on Oliveras, nor did it sufficiently state its

reasons for imposing the condition.

I.    The Fourth Amendment and Search Conditions

      The Fourth Amendment protects “against unreasonable searches and

seizures.” U.S. Const. amend. IV. In determining whether a search is reasonable,



                                         11
courts must balance “the degree to which [the search] intrudes upon an

individual’s privacy” with “the degree to which it is needed for the promotion of

legitimate governmental interests.” Samson v. California, 547 U.S. 843, 848 (2006)

(internal quotation marks and citation omitted). In doing so, we are required to

“examine the totality of the circumstances.” Id. (alteration adopted) (internal

quotation marks and citation omitted). Under this approach, a search generally is

“not reasonable unless it is accomplished pursuant to a judicial warrant issued

upon probable cause.” Skinner v. Ry. Lab. Execs.’ Ass’n, 489 U.S. 602, 619 (1989).

However, the “Fourth Amendment protections extend only to ‘unreasonable

government intrusions into . . . legitimate expectations of privacy.’” United States

v. Thomas, 729 F.2d 120, 122 (2d Cir. 1984) (quoting United States v. Chadwick, 433

U.S. 1, 7 (1977)).

       In particular, as relevant here, in Griffin v. Wisconsin, 483 U.S. 868, 873–74

(1987), the Supreme Court recognized that “[a] State’s operation of a probation

system . . . presents ‘special needs’ beyond normal law enforcement that may

justify departures from the usual warrant and probable-cause requirements.” In

assessing whether a special need justifies a search, we have explained that: (1)

“the government must allege a special need, the importance of which derives both



                                         12
from the particular context in which it seeks to implement searches . . . and what

the searches are designed to discover”; (2) “those subject to the search must enjoy

a diminished expectation of privacy, partly occasioned by the special nature of

their situation, and partly derived from the fact that they are notified in advance

of the search policy”; and (3) “the search program at issue must seek a minimum

of intrusiveness coupled with maximum effectiveness so that the searches bear a

close and substantial relationship to the government’s special needs.” United

States v. Lifshitz, 369 F.3d 173, 186 (2d Cir. 2004) (internal quotation marks omitted).

      Although neither the Supreme Court nor this Court has specifically

addressed the constitutionality of a suspicionless search by a probation officer of

a defendant on supervised release, we do not analyze this issue on a blank slate.

Indeed, over the last several decades, both the Supreme Court and this Court have

analyzed the Fourth Amendment standard for searches authorized in connection

with individuals under various forms of post-sentence supervision—such as

probation, parole, or supervised release. Because this case authority is instructive

in analyzing the constitutional issue presented in this appeal, we begin by

summarizing the relevant precedent in each category of supervision.




                                          13
      A.    Probation Supervision

      In United States v. Knights, 534 U.S. 112, 121–22 (2001), the Supreme Court

held that a warrantless search of a probationer’s apartment, supported by

reasonable suspicion and authorized by a probation condition, was reasonable

within the meaning of the Fourth Amendment. In reaching this decision, the

Supreme Court explained:

      Probation, like incarceration, is a form of criminal sanction imposed
      by a court upon an offender after verdict, finding, or plea of guilty.
      Probation is one point . . . on a continuum of possible punishments
      ranging from solitary confinement in a maximum-security facility to
      a few hours of mandatory community service. Inherent in the very
      nature of probation is that probationers do not enjoy the absolute
      liberty to which every citizen is entitled. Just as other punishments
      for criminal convictions curtail an offender’s freedoms, a court
      granting probation may impose reasonable conditions that deprive
      the offender of some freedoms enjoyed by law-abiding citizens.

Id. at 119 (internal quotation marks and citations omitted). The Supreme Court

emphasized that “[i]t was reasonable to conclude that the search condition would

further the two primary goals of probation—rehabilitation and protecting society

from future criminal violations.” Id. The Supreme Court also noted that, “[i]n

assessing the governmental interest side of the balance, it must be remembered

that the very assumption of the institution of probation is that the probationer is

more likely than the ordinary citizen to violate the law.” Id. at 120 (internal


                                        14
quotation marks and citation omitted). Thus, although recognizing “the hope that

[the probationer] will successfully complete probation and be integrated back into

society,” the Supreme Court held “that the balance of these considerations requires

no more than reasonable suspicion to conduct a search of [the] probationer’s

house. Id. at 120–21. The Supreme Court, however, explicitly left open the

question of “whether the probation condition so diminished, or completely

eliminated, [the probationer’s] reasonable expectation of privacy (or constituted

consent) that a search by a law enforcement officer without any individualized

suspicion would have satisfied the reasonableness requirement of the Fourth

Amendment.” Id. at 120 n.6 (emphasis added) (citation omitted).

      B.     Parole Supervision

      In Samson v. California, the Supreme Court answered, in the context of a

parolee, the question left open in Knights and held that suspicionless searches of a

parolee do not violate the Fourth Amendment. 547 U.S. at 857. In that case, a

police officer searched a parolee—pursuant to a California statute that requires

every prisoner eligible for release on state parole to “agree in writing to be subject

to search or seizure by a parole officer or other peace officer at any time of the day

or night, with or without a search warrant and with or without cause”—and found



                                          15
contraband. Id. at 846–47 (citation omitted). The Supreme Court reviewed the

totality of the circumstances pertaining to the petitioner’s status as a parolee,

including his acceptance of the clear and unambiguous search condition, and

concluded that he “did not have an expectation of privacy that society would

recognize as legitimate.” Id. at 852. With respect to his status of a parolee, and the

diminished expectation of privacy resulting therefrom, the Supreme Court

explained:

      As we noted in Knights, parolees are on the continuum of state-
      imposed punishments. On this continuum, parolees have fewer
      expectations of privacy than probationers, because parole is more
      akin to imprisonment than probation is to imprisonment. As this
      Court has pointed out, parole is an established variation on
      imprisonment of convicted criminals. . . . The essence of parole is
      release from prison, before the completion of sentence, on the
      condition that the prisoner abide by certain rules during the balance
      of the sentence. In most cases, the State is willing to extend parole
      only because it is able to condition it upon compliance with certain
      requirements.

Id. at 850 (internal quotation marks and citations omitted). In this context, the

Supreme Court emphasized that “California’s ability to conduct suspicionless

searches of parolees serves its interest in reducing recidivism, in a manner that

aids, rather than hinders, the reintegration of parolees into productive society.” Id.

at 854. Pursuant to that state interest, the Supreme Court “conclude[d] that the



                                         16
Fourth Amendment does not prohibit a police officer from conducting a

suspicionless search of a parolee.” Id. at 857.

      We likewise addressed the scope of suspicionless searches in the context of

parolees in United States v. Braggs, 5 F.4th 183 (2d Cir. 2021). Although noting that

the search at issue was conducted by parole officers rather than by municipal

police officers as in Samson, we concluded that the suspicionless search did not

violate the Fourth Amendment, under the special needs doctrine, when New York

state parole officers were performing a search reasonably related to their duties.

Id. at 187–88. In Braggs, the government appealed from the district court’s decision

suppressing evidence gathered in connection with a parole search of the

defendant’s house. Id. at 184. The government conceded that it lacked reasonable

suspicion, but argued that special needs still permitted the search. Id. On appeal,

this Court agreed and reasoned that “in light of [] special needs” such as “a [s]tate’s

operation of a probation system,” “a search of a parolee is permissible so long as

it is reasonably related to the parole officer’s duties.” Id. at 186–87 (alterations

adopted) (internal quotation marks and citations omitted). “Among these duties

are the supervision, rehabilitation, and societal reintegration of the parolee, as well

as assuring that the community is not harmed by the parolee’s being at large.” Id.



                                          17
at 187 (alterations adopted) (internal quotation marks and citations omitted).

Thus, because the parole officers’ search for a gun in the parolee’s home was

reasonably related to those duties, we held that “the district court erred in holding

that reasonable suspicion was required in this context.” Id. at 188.

      C.     Supervised Release

      Although the Supreme Court has not addressed suspicionless searches in

the context of a defendant on supervised release, this Court has explored that issue

in certain contexts. For example, in United States v. Reyes, 283 F.3d 446, 462 (2d Cir.

2002), we held that a suspicionless visit to the home of a defendant serving a term

of supervised release did not violate the Fourth Amendment. In doing so, we

explained that the diminished Fourth Amendment rights of parolees “appl[y] with

equal force to individuals, like Reyes, subject to federal supervised release—the

reformed successor to federal parole.” Id. at 458. Moreover, we described in detail

the role of the probation officer and emphasized:

      In the same way that a parole officer, of necessity, must have
      investigative powers to gather information about the parolee’s
      activities, environment, and social contacts so as to ensure that the
      conditions of parole are not being violated and to monitor the
      parolee’s progress of reintegration into society, field contacts with a
      convicted person serving a term of federal supervised release are vital
      to ensure that the probation officer is aware of the offender’s conduct
      and condition.


                                          18
Id. at 458 (alterations adopted) (internal quotation marks and citations omitted).

Thus, we held, under the special needs doctrine, that probation officers could

conduct “at any time” a home visit to determine whether the supervisee was

violating the terms of his supervised release, without any individualized

suspicion. Id. at 459–61.

      In United States v. Balon, 384 F.3d 38, 43–44 (2d Cir. 2004), we again discussed

the Fourth Amendment standard for defendants on supervised release in

connection with a challenge to a search condition allowing for remote monitoring

of a defendant’s computer. Balon involved a defendant who was convicted of

transporting child pornography in interstate commerce through the use of a

computer, and, in addition to being sentenced to prison term, was subjected to

conditions of supervised release, including the Probation Department’s remote

monitoring of his use of computers. Id. at 41. In articulating the standard for the

defendant’s Fourth Amendment challenge to that condition of supervised release,

we identified the first part of the inquiry as requiring a determination as to

“whether a convicted person serving a term of federal supervised release[] has a

legitimate expectation of privacy.” Id. at 44 (internal quotation marks, alteration,

and citation omitted). We then reiterated that “[a]n offender on supervised release



                                         19
has a ‘diminished expectation of privacy that is inherent in the very term

“supervised release.”’” Id. (quoting Reyes, 283 F.3d at 460) (emphasis omitted); see

also United States v. Edelman, 726 F.3d 305, 310 (2d Cir. 2013) (noting that

supervisees “who sign waivers manifest an awareness that supervision can

include intrusions into their residence and, thus, have a severely diminished

expectation of privacy” (alteration adopted) (quoting United States v. Newton, 369

F.3d 659, 665 (2d Cir. 2004))). 1



1
    In support of this conclusion, we suggested in Balon that “on the continuum of
supervised release, parole and probation, restrictions imposed by supervised release are
’[t]he most severe.’” 384 F.3d at 44 (quoting Lifshitz, 369 F.3d at 181 n.4). We note that
this suggestion in Balon and Lifshitz may be a misreading of Reyes, which Lifshitz cites for
this proposition. See Lifshitz, 369 F.3d at 181 n.4 (“The most severe [among supervised
release, parole, and probation] is ‘supervised release,’ which is ‘meted out in addition to,
not in lieu of, incarceration’ . . . .” (quoting Reyes, 283 F.3d at 461)). Reyes did state that
the principles supporting the special needs doctrine in the context of probation “apply a
fortiori to federal supervised release, which, in contrast to probation, is meted out in
addition to, not in lieu of, incarceration.” 283 F.3d at 461 (internal quotation marks and
citation omitted). However, while it suggested that the grounds for the special needs
doctrine were even stronger for individuals on supervised release as compared to
probation, we do not read Reyes to suggest that the restrictions imposed by supervised
release are more severe than parole. Indeed, Oliveras asserts that parole is the most
severe on the continuum of forms of post-release supervision because “parole is a
constructive extension of a prison sentence” while “supervised release is imposed in
addition to prison, not as an alternative to it.” Appellant’s Br. at 14. In any event, even if
we accept that construction for purposes of our analysis (notwithstanding the language
in Balon and Lifshitz), we still conclude, as articulated in Reyes, that the governmental
interests supporting suspicionless searches of parolees apply with “equal force” to
supervisees, see 283 F.3d at 458, and, as discussed infra, support the constitutionality of
such searches in the supervised release context.


                                              20
       We further emphasized that “when evaluating conditions of supervised

release under the Fourth Amendment we remain mindful that the alternative

facing defendants on supervised release in the absence of a computer monitoring

probation condition might well be the more extreme deprivation of privacy

wrought by imprisonment.” Balon, 384 F.3d at 44 (alterations adopted) (internal

quotation marks and citation omitted).              Thus, we concluded that “[the

supervisee’s] expectation of privacy is subject to the special needs of supervised

release,” which we then summarized:

       A number of these special needs are set out in Sections 3583(d) and
       3553(a), and provide that conditions reasonably relating to the nature
       and circumstances of the offense and the history and characteristics
       of the defendant must: (i) “afford adequate deterrence to criminal
       conduct”; (ii) “protect the public from further crimes of the
       defendant”; and (iii) “provide the defendant with needed educational
       or vocational training, medical care, or other correctional treatment in
       the most effective manner.” 18 U.S.C. § 3553(a) (cited in 18 U.S.C.
       § 3583(d)). These statutes also require that the conditions “involve[]
       no greater deprivation of liberty than is reasonably necessary” to
       achieve “the[se] purposes.” Id. § 3583(d)(2).

Id. at 44–45. 2



2
   We also note that the policy statement in the Sentencing Guidelines recommends
including certain special conditions of supervised release in cases involving sex offenses,
including a condition that allows a search by a probation officer, without reasonable
suspicion, “in the lawful discharge of the officer’s supervision functions.” U.S.S.G.
§ 5D1.3(d)(7)(C); see also United States v. Parisi, 821 F.3d 343, 348 (2d Cir. 2016) (per
curiam).
                                            21
      We then explained that “[b]ecause of these special needs, the requirements

of effective special conditions define the parameters of a supervised releasee's

Fourth Amendment rights.” Id. at 45. We acknowledged, however, that “the

efficacy of special conditions with respect to computer monitoring, and therefore

the extent to which they must intrude upon a supervised releasee’s privacy in light

of the special needs of supervised release, is fundamentally a question of

technology.” Id. Because the technology at issue is “constantly and rapidly

changing” and “Balon [would] not begin his term of supervised release for three

years,” we concluded that “it [would be] impossible to evaluate at th[at] time

whether one method or another, or a combination of methods, [would] occasion a

greater deprivation of his liberty than necessary in light of the special needs of

supervised release.”   Id. at 46.   We thus dismissed that Fourth Amendment

challenge as unripe for review and directed the district court to reconsider this

issue, at the request of either party, at a time closer to Balon’s release to

supervision. Id.

II.   Suspicionless Search for Defendants on Supervised Release

      Oliveras argues that the Special Condition violates the Fourth Amendment

because it requires him to submit to searches by the probation officer without



                                        22
reasonable suspicion, which infringes on his constitutional right to privacy. We

find this argument, stated so broadly, unpersuasive.

      As we recognized in Reyes, Oliveras has a diminished expectation of privacy

during his period of supervision because he is a “convicted person serving a court-

imposed term of federal supervised release.” 283 F.3d at 457; see also Mont v. United

States, 139 S. Ct. 1826, 1833 (2019) (“Supervised release is a form of

postconfinement monitoring that permits a defendant a kind of conditional liberty

by allowing him to serve part of his sentence outside of prison.” (internal

quotation marks and citation omitted)); United States v. Peguero, 34 F.4th 143, 160-

61 (2d Cir. 2022) (“[P]recedent and logic make clear that a term of supervised

release is imposed as part and parcel of the original sentence—an inextricable part

of the penalty for the initial offense.” (internal quotation marks and citation

omitted)); United States v. Harper, 805 F.3d 818, 822 (7th Cir. 2015) (“[P]rison and

supervised release can be substitutes as well as complements, since, realistically,

supervised release is a form of custody (like parole, which it largely replaced in

the federal system of criminal justice) because it can and often does impose severe

limitations on a defendant’s post-release liberty.” (internal quotation marks and

citation omitted)); see generally United States v. Leon, 663 F.3d 552, 556 (2d Cir. 2011)



                                           23
(“District courts are permitted . . . to hedge against a relatively lenient term of

imprisonment by imposing a longer term of supervised release.” (alterations

adopted) (internal quotation marks and citation omitted)).

      Moreover, Oliveras would be fully aware that he is subject to the Search

Condition during his release, and thus would “[know] that his expectation of

privacy [is] diminished by virtue of his status as a convicted person serving a term

of federal supervised release.” Reyes, 283 F.3d at 460; see also Peguero, 34 F. 4th at

161 (“[E]ven though supervised release fulfills rehabilitative ends, distinct from

those served by incarceration, it is still, like probation or parole, a grant of leniency

based on a defendant’s promise to follow certain conditions.” (internal quotation

marks and citation omitted)).

      Balanced against his diminished expectation of privacy, the government’s

interest in proper and effective supervision of individuals on supervised release is

substantial. The Supreme Court “has repeatedly acknowledged that a State’s

interests in reducing recidivism and thereby promoting reintegration and positive

citizenship among probationers and parolees warrant privacy intrusions that

would not otherwise be tolerated under the Fourth Amendment.” Samson, 547

U.S. at 853. Thus, in Samson, the Supreme Court held that a state’s "ability to



                                           24
conduct suspicionless searches of parolees serves its interest in reducing

recidivism” and that a suspicionless search by a law enforcement officer of a

parolee was not a violation of the Fourth Amendment. Id. at 854, 857. That same

governmental interest in “supervision, rehabilitation, and societal reintegration”

supports a suspicionless search of an individual by his probation officer under the

special needs doctrine during a term of supervised release because such a search

is “reasonably related to the [probation] officer’s duties.” See Braggs, 5 F.4th at

187–88.

      To the extent that Oliveras argues that his status on supervised release

increases his expectation of privacy and/or reduces the government’s interests in

this context when compared to a parolee, such that a suspicionless search cannot

be tolerated by the Fourth Amendment, we are unpersuaded. In rejecting this

argument, we rely on our analysis in Reyes, which thoroughly explained why the

government’s compelling interests in effective supervision during parole are not

diminished simply because an individual is on supervised release.

      To be sure, we recognized that, while both forms of supervision follow

incarceration, supervised release “differs from parole in an important respect:

unlike parole, supervised release does not replace a part of the term of



                                        25
incarceration, but instead is given in addition to any term of imprisonment imposed

by a court.” 3 Reyes, 283 F.3d at 458. Notwithstanding that important distinction,

we concluded that the government’s “special need” to enforce conditions of

supervision imposed on individuals on supervised release is comparable to its

need to enforce such conditions over those on parole and justified a suspicionless

home visit:

       One of the principal purposes of a probation/parole officer’s
       observation and supervision responsibilities is to ensure that a
       convicted person under supervision does not again commit a crime.
       We have long recognized a duty on the part of the parole officer to
       investigate whether a parolee is violating the conditions of his
       parole—one of which, of course, is that the parolee commit no further
       crimes—when the possibility of violation is brought to the officer’s
       attention. Federal probation officers overseeing convicted persons
       serving terms of federal supervised release are similarly charged with
       monitoring supervisees’ adherence to the conditions of their release—
       which, as in the case of parole, includes the requirement that
       supervisees not commit further crimes. Accordingly, because
       probation officers monitoring convicted persons on supervised
       release bear the same supervisory responsibility as when acting as
       parole officers, we conclude that probation officers are required to
       investigate the conduct and condition of a supervisee by, inter alia,
       undertaking “at any time” a home visit to determine whether the
       supervisee is violating the terms of his supervised release, including
       the condition that he not commit any further crimes.

3
  Thus, the district court erred to the extent it suggested that supervised release shortens
a term of imprisonment. See Joint App’x at 100 (“when you’re on supervised release, that
was to allow someone out of prison at an earlier time”). As Reyes explains, supervised
release follows a term of imprisonment, while parole conditionally shortens a term of
imprisonment. See Reyes, 283 F.3d at 458.
                                            26
Id. at 459–60 (internal quotation marks, citations, and footnotes omitted). 4

       In short, recognizing as we did in Reyes the diminished expectation of

privacy of supervisees, and the special needs of probation officers to fulfill their

supervisory roles in that capacity, we hold that the imposition of a special

condition of supervised release that allows for searches without individualized

suspicion does not violate the Fourth Amendment and, thus, can be imposed if

sufficiently supported by the record under the factors set forth in Section 3583(d).

Such a condition gives probation officers the “considerable investigative leeway”

they need to monitor an individual on supervised release, such that they can act

as the “eyes and ears” for the court. Reyes, 283 F.3d at 455, 457 (internal quotation




4
  In contexts other than search conditions, the Supreme Court has expressed a variety of
views on the extent to which supervised release is similar to or different from traditional
parole. See United States v. Haymond, 139 S. Ct. 2369, 2382 (2019) (plurality opinion)
(“[U]nlike parole, supervised release wasn’t introduced to replace a portion of the
defendant’s prison term, only to encourage rehabilitation after the completion of his
prison term. . . . [T]hat structural difference bears constitutional consequences.” (internal
quotation marks omitted)); id. at 2385 (Breyer, J., concurring in judgment) (“[T]he role of
the judge in a supervised-release proceeding is consistent with traditional parole.”); id. at
2388 (Alito, J., dissenting) (Although “parole relieved a prisoner from serving part of the
prison sentence originally imposed, whereas a term of supervised release is added to the
term of imprisonment specified by the sentencing judge[,] . . . this difference is purely
formal and should have no constitutional consequences.”); Mont, 139 S. Ct. at 1833–34
(five-justice majority describing supervised release as both “a form of punishment” and
“a form of postconfinement monitoring that permits a defendant a kind of conditional
liberty by allowing him to serve part of his sentence outside of prison” (internal quotation
marks and citation omitted)).
                                             27
marks and citations omitted).       In other words, the special condition allows

probation officers “to determine whether the supervisee is violating the terms of

his supervised release, including the condition that he not commit any further

crimes.” Id. at 460.

      Our sister circuits who have addressed this issue have reached the same

conclusion under analogous circumstances. For example, in United States v. Betts,

511 F.3d 872, 876 (9th Cir. 2007), the Ninth Circuit upheld a condition of supervised

release that provided that “the defendant shall submit person and property to

search and seizure at any time of the day or night by any law enforcement officer,

with or without a warrant.” 5 In finding no abuse of discretion in imposing that

“very intrusive” condition, the Ninth Circuit relied heavily on the Supreme

Court’s decision in Samson:

      [T]he Supreme Court recently held in Samson v. California, that a
      similarly worded condition imposed by statute on all California
      parolees did not violate the Fourth Amendment, even though the
      condition did not require reasonable suspicion. The Court considered
      the high risk of recidivism for people convicted of crimes, and the
      problem that “[i]mposing a reasonable suspicion requirement . . .
      would give parolees greater opportunity to anticipate searches and
      conceal criminality.” Because the blanket requirement imposed by

5 Because the Special Condition here allowed suspicionless searches only by probation
officers, we do not reach the question of whether law enforcement officers other than the
probation officer(s) conducting the supervision may conduct such searches pursuant to
the special condition.
                                           28
      California on state parolees did not violate the Fourth Amendment, a
      fortiori the individualized requirement imposed in this case on
      supervised release does not. There is no sound reason for
      distinguishing parole from supervised release with respect to this
      condition. The federal system has abolished parole, and uses
      supervised release to supervise felons after they get out of prison.
      People on supervised release have not completed their sentences, they
      are serving them. The Court in Samson itself drew the analogy to
      supervised release. After Samson, there is no room for treating the
      search condition in this case as an abuse of discretion.

Id. (footnotes omitted) (quoting Samson, 547 U.S. at 854–55).

      Similarly, in United States v. Hanrahan, 508 F.3d 962, 971 (10th Cir. 2007), the

Tenth Circuit upheld a special condition of supervised release, for a defendant

convicted of unlawfully possessing a firearm, that required the defendant to

“submit to a search of his person, property, or automobile under his control”

without any level of suspicion. The court noted that “one effective means of

preventing [the defendant] from committing a similar offense in the future is to

require him to submit to suspicionless searches after he has been released from

prison but while he is still under the supervision of the Probation Officer.” Id. The

court further explained that “[s]earches based on some particularized level of

suspicion, by way of contrast, would likely not be as effective at deterring future

crimes of possession since the defendant could easily conceal such wrongdoing.”

Id. It therefore held that the district court acted within its discretion in imposing


                                         29
the suspicionless search condition. Id.; see also United States v. Sulik, 807 F. App’x

489, 493 (6th Cir. 2020) (summary order) (concluding that “the current legal

landscape forecloses any claim that a suspicionless-search condition for

individuals on supervised release ‘plainly’ violates the Fourth Amendment”);

United States v. Oswald, 711 F. App’x 593, 594–95 (11th Cir. 2018) (summary order)

(holding no plain error in imposition of suspicionless search condition of

supervised release); United States v. Erwin, 675 F. App’x 471, 472 (5th Cir. 2017)

(summary order) (same); United States v. Jackson, 866 F.3d 982, 985 (8th Cir. 2017)

(upholding suspicionless search of cell phone of defendant on supervised release

at a residential correctional facility). 6




6
   Other courts, with respect to probation supervision, have likewise found that a
condition allowing for a suspicionless search of a probationer’s residence does not violate
the Fourth Amendment. See, e.g., United States v. Tessier, 814 F.3d 432, 433 (6th Cir. 2016)
(holding that a condition to search probationer’s person, vehicle, property or place of
residence without suspicion did not violate the Fourth Amendment); United States v. King,
736 F.3d 805, 806 (9th Cir. 2013) (holding that suspicionless search of probationer’s
residence is permissible under the Fourth Amendment “when, as here, a violent felon has
accepted a suspicion-less search condition as part of a probation agreement”); Owens v.
Kelley, 681 F.2d 1362, 1368 (11th Cir. 1982) (holding that suspicionless search of
probationer’s residence is permissible under the Fourth Amendment because “[i]t is clear
that a requirement that searches only be conducted when officers have ‘reasonable
suspicion’ or probable cause that a crime has been committed or that a condition of
probation has been violated could completely undermine the [deterrence] purpose of the
search condition”). We have no occasion here to address the constitutionality of
suspicionless searches of probationers.
                                             30
         In sum, we conclude that the special needs doctrine of the Fourth

Amendment permits, when sufficiently supported by the record, the imposition

of a special condition of supervised release by the district court that allows the

probation officer conducting the supervision to search the defendant’s person,

property, vehicle, place of residence, or any other property under his control,

without any level of suspicion.

III.     Procedural Reasonableness of the Search Condition in this Case

         Oliveras alternatively argues that the imposition of the Search Condition

was procedurally unreasonable in this case because the district court did not make

an individualized assessment as to the need to impose the condition, nor

sufficiently state its reasons as to why the imposition of the condition in this case

was reasonably related to the relevant sentence factors under Section 3553(a). We

agree.

         “For a sentence to be procedurally reasonable, a [d]istrict [c]ourt must ‘make

an individualized assessment when determining whether to impose a special

condition of supervised release, and . . . state on the record the reason for imposing

it.’” Eaglin, 913 F.3d at 94 (2d Cir. 2019) (quoting United States v. Betts, 886 F.3d

198, 202 (2d Cir. 2018)). “In the absence of such an explanation, we may uphold



                                           31
the condition imposed only if the district court’s reasoning is ‘self-evident in the

record.’” Betts, 886 F.3d at 202 (quoting Balon, 384 F.3d at 41 n.1).

      In imposing conditions of supervised release, district courts possess broad

discretion. United States v. Myers, 426 F.3d 117, 124 (2d Cir. 2005). The district

court may impose a special condition of supervised release that is “reasonably

related to (A) the nature and circumstances of the offense and the history and

characteristics of the defendant; (B) the need for the sentence imposed to afford

adequate deterrence to criminal conduct; (C) the need to protect the public from

further crimes of the defendant; and (D) the need to provide the defendant with

needed educational or vocational training, medical care, or other correctional

treatment in the most effective manner.” U.S.S.G. § 5D1.3(b); accord 18 U.S.C.

§§ 3583(d)(1), 3553(a); United States v. Johnson, 446 F.3d 272, 277 (2d Cir. 2006).

Notwithstanding the use of the conjunctive in the Guidelines, “a condition may be

imposed if it is reasonably related to any one or more of the specified factors.”

United States v. Amer, 110 F.3d 873, 883 (2d Cir. 1997) (internal quotation marks and

citation omitted).   Moreover, a special condition must involve “no greater

deprivation of liberty than is reasonably necessary for the purposes” of sentencing,

and it must be “consistent with any pertinent policy statements issued by the



                                          32
Sentencing Commission.” 18 U.S.C. § 3583(d)(2), (3); see also U.S.S.G. § 5D1.3(b);

accord Balon, 384 F.3d at 42. Importantly, a district court’s discretion to impose

special conditions is not “untrammelled,” and we will “carefully scrutinize

unusual and severe conditions.” Myers, 426 F.3d at 124 (internal quotation marks

and citations omitted).

      Here, the district court failed to make an individualized assessment to

support the imposition of the suspicionless Search Condition as to Oliveras.

Indeed, the district court made clear that it was not making an individualized

assessment as to the need to impose the condition on Oliveras when it stated that

it was “not inclined to put the reasonable suspicion requirement in [its] sentences

unless somebody can point to . . . a valid reason why in a particular case it should,”

and thus, in “the general case, [the district court] will provide reasonable suspicion

is not required.” Joint App’x at 100. Rather than making an individualized

assessment at the start, the district court espoused the presumptive application of

the Search Condition in drug cases, relying on broad statements about its views

regarding supervision in drug cases generally, untethered to any specific

consideration to the facts and circumstances in this particular case. For example,

the district court justified the Search Condition with its observation that



                                         33
individuals convicted of drug offenses tended to reoffend while on supervised

release. Additionally, the district court reasoned that, because offenders do not

leave drugs out in the open, probation officers should be afforded the ability to

conduct searches without a showing of reasonable suspicion. The district court

also stated that, given the high risk of recidivism in drug cases, requiring

reasonable suspicion would undermine the needs of the probation officer to

supervise those particular offenders on release.

      We recognize that the district court generally expressed some valid reasons

as to why a suspicionless search could be reasonably related to the relevant factors,

under Section 3553(a), in cases involving drug offenses. However, exclusive

reliance on those generalized considerations is inconsistent with the requirement

that the district court make an “individualized assessment” as to each defendant

when determining whether to impose a special condition. Eaglin, 913 F.3d at 94

(internal quotation marks and citation omitted); see also United States v. Arbaugh,

951 F.3d 167, 179 (4th Cir. 2020) (“[T]he district court cannot fulfill its duty by

generally referring to the legal standards in § 3553(a) and § 3583(d), which govern

how the court should exercise its discretion in imposing any special conditions of

release. Instead, the district court had to explain what facts led to its decision to



                                         34
impose the computer-related special conditions[, which permitted random

inspections of defendant’s personal computing devices,] on this defendant.”

(emphasis added)); cf. United States v. Germosen, 139 F.3d 120, 131–32 (2d Cir. 1998)

(upholding search condition permitting searches of defendant’s person and

property “necessary to secure financial information” in a fraud case involving

restitution order, where the district court’s “reasoning behind the condition, as

with her reasoning behind other aspects of [the defendant’s] sentence, was made

clear during the sentencing hearing”); United States v. Winston, 850 F.3d 377, 380–

81 (8th Cir. 2017) (holding district court did not commit plain error in imposing

reasonable suspicion based search condition on a narcotics offender where the

probation officer’s motion and the court’s statement at sentencing explained the

need for the condition); United States v. Monteiro, 270 F.3d 465, 469 (7th Cir. 2001)

(upholding search condition requiring defendant to submit to search “upon

demand” in a fraud case where, “[i]n imposing the special condition . . . , the

district court explained that [the defendant’s] history of fraudulent endeavors

demonstrated the need for ‘exceptional vigilance’ on the part of law enforcement

officials to discourage recidivism”).




                                         35
      The district court’s responsibility to conduct an individualized assessment

is not suspended in drug cases, nor is it permissible to have a presumption that a

suspicionless search condition is warranted in every drug case unless a defendant

can demonstrate otherwise. Indeed, it is not difficult to imagine individualized

cases where, although a defendant was convicted of a drug offense, the nature of

his involvement in that offense, combined with an assessment of the other

applicable statutory factors, would not support a finding that such a highly

intrusive suspicionless search condition is reasonable. Therefore, any decision by

a district court to this or any other special condition must be supported, including

in drug cases, by an individualized assessment and explanation as to why that

condition is “reasonably related” to the sentencing objectives and “involve[s] no

greater deprivation of liberty than is reasonably necessary” for these purposes.

U.S.S.G. § 5D1.3(b); see also Eaglin, 913 F.3d at 100 (emphasizing that “[b]efore

imposing a special condition . . . , a district court must make factual findings

supporting its view that the condition is designed to address a realistic danger and

the deprivation the condition creates is not greater than reasonably necessary to

serve the sentencing factors”).




                                         36
      Moreover, while we agree with the government that a condition of

supervised release permitting suspicionless searches does not per se violate the

Fourth Amendment, and may in appropriate cases be supported by the special

needs of supervision, it does not follow that such a condition may be imposed as

a routine matter. As with other conditions of supervised release that implicate

constitutionally protected interests, such a broad authorization to conduct

unlimited searches must be carefully considered by sentencing courts “and

supported by particularized findings that it does not constitute a greater

deprivation of liberty than reasonably necessary to accomplish the goals of

sentencing.” United States v. Matta, 777 F.3d 116, 123 (2d Cir. 2015) (internal

quotation marks and citations omitted).

      In Reyes, our approval of the condition authorizing suspicionless home visits

rested, in part, on the recognition that “a home visit is far less intrusive than a [full-

scale] probation search,” 283 F.3d at 462 (emphasis omitted), and we have

heretofore approved conditions permitting searches of a supervisee’s home only

upon reasonable suspicion. As we have repeatedly explained in affirming such

search conditions, those conditions do not constitute a greater deprivation than




                                           37
reasonably necessary because they require reasonable suspicion. 7 The requirement

of reasonable suspicion does not set a high bar, and the government cites no

empirical evidence that the ordinary practice of courts within this Circuit of

imposing search conditions based on reasonable suspicion has failed to satisfy the

Probation Department’s “special needs” of supervision in the vast majority of

cases, such that suspicionless search conditions are required. Permitting such

highly intrusive, full-scale searches for no particular reason, without limitation as

to frequency or scope, subjects the supervisee to the prospect of frequent,

unlimited searches without any factual precondition. Such conditions may be

justified, but they require careful consideration as to the need for such broad

discretion to search in each particular case. 8



7
  See United States v. Stiteler, No. 22-2732, 2023 WL 4004573, at *1 (2d Cir. June 15, 2023)
(summary order) (finding that the district court did not abuse its discretion in “finding
that the search condition [did] not depriv[e] [the defendant] of liberty greater than
necessary because it requires . . . reasonable suspicion before the search can be
conducted.” (internal quotation marks and citation omitted)); United States v. Rakhmatov,
No. 21-151, 2022 WL 16984536, at *3 (2d Cir. Nov. 17, 2022) (summary order) (explaining
that the “condition’s limitations on searches to circumstances in which reasonable
suspicion of a supervised release violation exists and to a reasonable time and manner of
search ensure that the condition imposes no greater restraint on liberty than is reasonably
necessary” (alterations adopted) (internal quotation marks and citation omitted)).

8 As we have long acknowledged, “searching for illegal drug use” is a “particularly apt
analogy to monitoring for computer-related sex offenses.” Lifshitz, 369 F.3d at 189. In
light of the constitutional rights implicated by conditions of supervised release


                                            38
       Accordingly, we conclude that the district court committed procedural

error, and therefore exceeded the scope of its discretion, because it did not make

an individualized assessment in deciding whether to impose the Search Condition

or provide adequate reasons for us to decide whether the Search Condition is

reasonable under Section 3583(d), including a sufficient explanation as to how the

condition is reasonably related in this particular case to the applicable statutory

factors under Section 3553(a). 9



permitting monitoring of computer devices or restricting access to the internet, we have
repeatedly emphasized that such conditions must be “narrowly tailored” and “robustly
supported” by a district court. Eaglin, 913 F.3d at 91, 98. Thus, we have not hesitated to
remand monitoring conditions where a less intrusive condition appeared to be a “viable
option” and the record “d[id] not explain why such [an alternative condition] was
insufficient.” Id. at 98; see also United States v. Salazar, No. 22-1385, 2023 WL 4363247, at
*3 (2d Cir. July 6, 2023) (summary order) (vacating monitoring condition authorizing
suspicionless search of defendant’s internet-capable devices, where “narrower options
were available to the district court” and there was “no indication that the district
considered such a [narrower] condition” or “explan[ation] why a more stringent
condition was necessary”).

9
   We recognize that, even in the absence of an explanation, we can uphold the Search
Condition “if the district court’s reasoning is ‘self-evident in the record,’” Betts, 886 F.3d
at 202 (quoting Balon, 384 F.3d at 41 n.1), and the record here does indicate that drugs and
a firearm were seized from a residence in Buffalo attributed to Oliveras. However, that
seizure occurred more than three years prior to his sentence and it is self-evident, based
upon the discussion at sentencing, that the district court’s reasoning did not contain the
requisite individualized assessment of Oliveras at the time of sentencing as it relates to
the Special Condition. Thus, under the circumstances, we conclude that a remand is
necessary for the district court to make that individualized assessment after the parties
have had an opportunity to present any relevant information on this issue that could bear
on the applicable statutory factors.
                                             39
                                 CONCLUSION

      For the reasons set forth above, we VACATE the Search Condition and

REMAND to the district court for further consideration of whether it is necessary

to impose the Search Condition in this particular case and, if so, for the district

court to explain the individualized basis for imposing the Search Condition.




                                        40

```

---

## GROUP: content/cases/United States v. Payne.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Payne
type: case
citation: "99 F.4th 495 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 9th Cir. 2024
court_level: coa
circuit: ca9
year: 2024
date_decided: 2024-04-17
docket: 22-50262
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
  opinion_url: "https://www.courtlistener.com/opinion/9494371/united-states-v-jeremy-payne/"
  cluster_id: 9494371
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Payne
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: Key
related:
  - "[[Special Needs and Administrative Searches]]"
  - "[[Samson v. California]]"
  - "[[Riley v. California]]"
  - "[[United States v. Knights]]"
tags:
  - case
  - fourth-amendment
  - fifth-amendment
  - parole-search
  - suspicionless-search
  - cell-phone
  - biometric-unlock
  - ninth-circuit
holding: "A California parolee is subject to a valid suspicionless search condition, and because parole searches require no probable cause as to the place or thing searched, CHP officers who stopped Payne for a traffic violation and, learning he was a parolee, searched his cell phone acted reasonably; the court declined to extend Riley — a search-incident-to-arrest case — to parole searches of a cell phone, and separately held that compelling Payne to unlock the phone with his thumbprint did not violate the Fifth Amendment because the act was non-testimonial."
aliases:
  - United States v. Payne
  - "United States v. Payne (9th Cir. 2024)"
---

# United States v. Payne

*99 F.4th 495 (9th Cir. 2024)* (No. 22-50262) · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9494371 → lead opinion 9960984 (99 F.4th 495, decided 2024-04-17); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
California Highway Patrol officers stopped Jeremy Payne for a vehicle-code window-tint violation. During the stop they learned he was a California parolee subject to a search condition. After finding nothing illegal on his person or in the car, an officer searched Payne's cell phone — compelling him to unlock it by grabbing his thumb and pressing it to the sensor while Payne was handcuffed in the back of a patrol vehicle — and reviewed his photos, videos, and maps, uncovering evidence. Payne moved to suppress, arguing the phone search was an unreasonable parole search and that compelling the biometric unlock violated his Fifth Amendment privilege. The district court denied the motion.

## Issue
Whether the suspicionless search of a parolee's cell phone under a parole search condition was reasonable under the Fourth Amendment (and whether *[[Riley v. California|Riley]]* required otherwise), and whether compelling the parolee to unlock the phone with his fingerprint violated the Fifth Amendment.

## Rule
Parolees have a severely diminished expectation of privacy, and a search conducted pursuant to a valid parole search condition need not rest on individualized suspicion or probable cause. As the panel put it: "Parole searches, on the other hand, require no such probable cause determination as to the place or thing being searched." — 99 F.4th 495, slip op. at 20. ^pin-op20

## Application
Because Payne's statutorily mandated parole search condition independently authorized the search, and the officers displayed no arbitrary, capricious, or harassing conduct, the search of his phone was reasonable under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. The court rejected Payne's reliance on *[[Riley v. California|Riley]]*: that decision barred warrantless cell-phone [[Search Incident to Arrest|searches incident to arrest]], but the court had already declined to extend *[[Riley v. California|Riley]]*'s reasoning to parole searches, and it declined again here — a parole search of a phone is governed by the parolee's diminished privacy interests, not by *[[Riley v. California|Riley]]*. On the Fifth Amendment, the court held that compelling Payne to press his thumb to the sensor was not testimonial: like a blood draw or a booking fingerprint, the act required no cognitive assertion and merely provided access, so it did not compel Payne to be a witness against himself.

## Conclusion
**Affirmed.** The Ninth Circuit rejected both the Fourth Amendment parole-search challenge and the Fifth Amendment compelled-unlock challenge and upheld the denial of suppression.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Payne* applies the *[[Samson v. California|Samson]]* diminished-privacy rationale to a **cell-phone** parole search: suspicionless parole searches need no probable cause, and *[[Riley v. California|Riley]]* — a search-incident-to-arrest rule — does not govern them. Its distinct **Fifth Amendment** holding (compelled biometric unlock is non-testimonial) belongs to the self-incrimination materials; here, teach the parole/administrative-search rationale and the boundary between *[[Riley v. California|Riley]]* and suspicionless supervision searches.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key*

## Sources
- [*United States v. Payne*, 99 F.4th 495 (9th Cir. 2024)](https://www.courtlistener.com/opinion/9494371/united-states-v-jeremy-payne/) — pinpoint: slip op. at 20 (parole searches require no probable cause; *Riley* not extended to parole phone searches; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "31243428ffb16878", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "99 F.4th 495 (2024)", "court": "9th Cir. 2024", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Payne", "year": "2024"}}
{"assertion_id": "3e49fb9c85cb6eb4", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key", "title": "United States v. Payne"}}
{"assertion_id": "b735c2ada0a47792", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A California parolee is subject to a valid suspicionless search condition, and because parole searches require no probable cause as to the place or thing searched, CHP officers who stopped Payne for a traffic violation and, learning he was a parolee, searched his cell phone acted reasonably; the court declined to extend Riley — a search-incident-to-arrest case — to parole searches of a cell phone, and separately held that compelling Payne to unlock the phone with his thumbprint did not violate the Fifth Amendment because the act was non-testimonial.", "title": "United States v. Payne"}}
{"assertion_id": "371b5a469521f082", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Payne", "varies_by_point": "false"}}
{"assertion_id": "4f7863ad3a1f6dc8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Payne"}}
```

### lake record — United States v. Payne

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Payne",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Jeremy Payne",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Payne",
    "court": "9th Cir. 2024",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2024-04-17",
    "year": 2024,
    "docket": "22-50262",
    "cluster_id": 9494371,
    "lead_opinion_id": 9960984,
    "sibling_ids": [],
    "absolute_url": "/opinion/9494371/united-states-v-jeremy-payne/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "99 F.4th 495",
      "volume": "99",
      "reporter": "F.4th",
      "page": "495",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "99 F.4th 495",
        "volume": "99",
        "reporter": "F.4th",
        "page": "495",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "99 F.4th 495",
    "official_selection": {
      "court_class": "state",
      "selected": "99 F.4th 495",
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
    "date_created": "2026-07-06T05:57:18Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:57:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:57:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-payne--9494371",
      "to_record_id": "United States v. Payne",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Payne

```
                     FOR PUBLICATION

     UNITED STATES COURT OF APPEALS
          FOR THE NINTH CIRCUIT

UNITED STATES OF AMERICA,                          No. 22-50262

                 Plaintiff-Appellee,             D.C. No. 5:22-cr-
                                                   00054-PA-1
    v.

JEREMY TRAVIS PAYNE, AKA                             OPINION
Jeramey Travis Payne,

                 Defendant-Appellant.

         Appeal from the United States District Court
            for the Central District of California
          Percy Anderson, District Judge, Presiding

           Argued and Submitted February 14, 2024
                    Pasadena, California

                       Filed April 17, 2024

    Before: Richard C. Tallman and Consuelo M. Callahan,
     Circuit Judges, and Robert S. Lasnik, * District Judge.

                   Opinion by Judge Tallman

*
 The Honorable Robert S. Lasnik, United States District Judge for the
Western District of Washington, sitting by designation.
2                          USA V. PAYNE


                          SUMMARY **


                          Criminal Law

   The panel affirmed the district court’s denial of Jeremy
Travis Payne’s motion to suppress evidence.
    Payne, a California parolee, was arrested and charged
with possession with intent to distribute fentanyl,
fluorofentanyl, and cocaine. After the district court denied
his motion to suppress evidence of these crimes that
California Highway Patrol officers had recovered from a
house in Palm Desert, California, he entered a conditional
guilty plea to possession of fentanyl with intent to distribute.
    The panel held that the CHP officers did not violate the
Fourth Amendment in their search, during a traffic stop, of
Payne’s cell phone, made possible by the officers’ forced use
of his thumb to unlock the device. The panel held that,
despite the language of a special search condition of Payne’s
parole, requiring him to surrender any electronic device and
provide a pass key or code, but not requiring him to provide
a biometric identifier to unlock the device, the search was
authorized under a general search condition, mandated by
California law, allowing the suspicionless search of any
property under Payne’s control. The panel concluded that
any ambiguity created by the special condition, when
factored into the totality of the circumstances, did not
increase Payne’s expectation of privacy in his cell phone to
render the search unreasonable under the Fourth
Amendment. The panel further held that the search of the

**
  This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                        USA V. PAYNE                        3


cell phone was not unreasonable on a theory that it violated
California’s prohibition against arbitrary, capricious, or
harassing searches. In addition, the search of Payne’s
photos, videos, and maps on his cell phone did not run afoul
of Riley v. California, which held that officers cannot search
the contents of an individual’s cell phone incident to their
arrest, because Riley does not apply to parole searches of a
cell phone.
     The panel held that the CHP officers did not violate
Payne’s Fifth Amendment privilege against self-
incrimination when they compelled him to unlock his cell
phone using his fingerprint. Payne established that the
communication       at    issue     was    compelled       and
incriminating. The panel held, however, that the compelled
use of a biometric to unlock an electronic device was not
testimonial because it required no cognitive exertion, placing
it in the same category as a blood draw or a fingerprint taken
at booking, and merely provided the CHP with access to a
source of potential information. Accordingly, the Fifth
Amendment did not apply.
    The panel held that there was sufficient probable cause
to support issuance of a search warrant without regard to
observations CHP officers made during a challenged
protective sweep of the Palm Desert House.
4                       USA V. PAYNE


                         COUNSEL

Caroline S. Platt (argued), Assistant Federal Public
Defender; Cuauhtemoc Ortega, Federal Public Defender;
Federal Public Defender’s Office, Los Angeles, for
Defendant-Appellant.
Haoxiaohan H. Cai (argued), Assistant United States
Attorney, General Crimes Section; Bram M. Alden,
Assistant United States Attorney, Chief, Criminal Appeals
Section; E. Martin Estrada, United States Attorney; United
States Department of Justice, Office of the United States
Attorney, Los Angeles, California, for Plaintiff-Appellee.


                         OPINION

TALLMAN, Circuit Judge:

    Appellant Jeremy Travis Payne was a California parolee
when he was arrested and charged with three counts of
possession with intent to distribute fentanyl, fluorofentanyl,
and cocaine. After the district court denied Payne’s motion
to suppress evidence of these crimes recovered from a home
in Palm Desert, California, Payne entered a conditional
guilty plea to possession of fentanyl with intent to distribute
at least 40 grams in violation of 21 U.S.C. § 841(a)(1),
(b)(1)(B)(vi). On appeal, Payne challenges the district
court’s denial of his motion to suppress, arguing that
California Highway Patrol (“CHP”) officers violated his
Fourth and Fifth Amendment rights.
                            USA V. PAYNE                              5


                                   I
    In November 2018, Payne was arrested for assault with
a deadly weapon on a peace officer, in violation of Cal. Penal
Code § 245(c).      He was sentenced to three years
imprisonment and later released on parole. On September
23, 2020, Payne signed a one-page “Notice and Conditions
of Parole” document and a separate, three-page “Special
Conditions of Parole” document. Pursuant to Cal. Penal
Code § 3067(b)(3) and 15 Cal. Code Regs. § 2511(b)(4),
Payne’s Notice and Conditions of Parole included the
following condition (“general search condition”) 1:

        You, your residence, and any property under
        your control are subject to search or seizure
        by a probation officer, an agent or officer of
        the California Department of Corrections and
        Rehabilitation, or any other peace officer, at
        any time of the day or night, with or without
        a search warrant, with or without cause.

Payne’s Special Conditions of Parole included a more
detailed condition (“special search condition”) concerning
electronic devices:

        You shall surrender any digital/electronic
        device and provide a pass key/code to unlock
        the device to any law enforcement officer for
        inspection other than what is visible on the
        display screen.        This includes any

1
 This general search condition is “mandated as a term of every parolee’s
release” in the State of California. People v. Delrio, 259 Cal. Rptr. 3d
301, 305 (Ct. App. 2020); see People v. Schmitz, 288 P.3d 1259, 1264–
65 (Cal. 2012).
6                       USA V. PAYNE


       digital/electronic device in your vicinity.
       Failure to comply can result in your arrest
       pending further investigation and/or
       confiscation of any device pending
       investigation.

    On November 3, 2021, CHP officers Coddington and
Garcia—who were both assigned to the Coachella Valley
Violent Crime Gang Taskforce—were patrolling an area in
Desert Hot Springs, California. They saw a gold Nissan with
what they perceived to be unlawfully tinted front windows
and initiated a traffic stop for a suspected violation of Cal.
Veh. Code § 26708. Officer Coddington approached the
vehicle and asked the driver, Payne, to provide his driver’s
license, vehicle registration, and proof of insurance. Officer
Coddington later reported that Payne was “extremely
nervous,” “trembling as he fumbled for the documents,”
“sweating profusely,” and “stammering when he spoke.”
Payne informed the officers that he was on California parole.
After confirming Payne’s California parole status with
Riverside County Sheriff’s Dispatch, Officer Coddington
asked Payne and his female passenger to get out of the car.
Payne was handcuffed and eventually detained in the back
of a squad car.
    Officers searched Payne’s person pursuant to his parole
conditions and found in his pockets $1,270 cash and a key
ring with several keys, including a key to a BMW. After
searching the vehicle, Officer Coddington asked Payne if he
had a phone. Payne responded that “his phone was in the
driver’s door panel and was green in color.” The phone was
where Payne said it would be. Officer Coddington retrieved
it and asked Payne to provide the passcode. Despite
confirming that he had a phone, and informing officers of its
                            USA V. PAYNE                              7


location and color, Payne changed his story and began
denying ownership, stating “the phone was not his and he
did not have the password.”
    At this juncture, CHP officers would have been justified
under Payne’s special search condition in either
“confiscati[ng] . . . [the] device” or “arrest[ing] Payne
pending further investigation.” Instead, Officer Coddington
forcibly grabbed Payne’s thumb and used it to unlock the
phone via a built-in biometric unlocking feature. 2 Once
unlocked, Officer Coddington opened the phone’s settings
and confirmed that Payne’s full name was listed in the
owner’s information section. Next, he began looking
through the device’s stored media and found two important
videos.
    The first video was recorded on the phone the same day,
November 3, 2021, just three hours before the traffic stop. It
showed the inside of a room with what Officer Coddington
believed to be “a large amount of U.S. currency, several bags
of blue pills (suspected to be fentanyl), and a gold-colored
money counting machine.” An individual, who Officer
Coddington presumed was Payne, could be heard on the
video referring to the room as his “office.” The second video
was taken outside of a residence with a gray-brick wall
around the front. Again, an individual, who Officer
Coddington presumed was Payne, could be heard saying
“life is good in Palm Desert” and “I got the Beamer out


2
 Whether Officer Coddington forcibly used Payne’s thumb to unlock the
phone or Payne “reluctantly unlocked the cell phone using his thumb
print” was disputed before the district court. For the purposes of this
appeal, however, the government—both in its answering brief and during
oral argument—accepted the defendant’s version of the facts, i.e., “that
defendant’s thumbprint was compelled.”
8                        USA V. PAYNE


front,” referring to a parked BMW vehicle shown in the
video.
    Finally, Officer Coddington opened the maps application
on Payne’s cell phone, which showed a pin dropped to a
parked vehicle on a street called El Cortez Way in Palm
Desert, California, about twenty-five miles away. Despite
what Officer Coddington found on the phone concerning the
parked car in Palm Desert, Payne insisted that he resided
with his mother at her home in Indio, California; Payne’s
female passenger told officers the same thing in a later
interview. Based on what CHP officers found on Payne’s
person and phone, they drove Payne to the location of the
parked car on El Cortez Way.
    When the officers arrived, they saw a silver BMW
parked in front of a house. The car was registered to Payne
and the BMW key recovered from Payne’s person unlocked
it. Before obtaining a warrant, Officer Coddington walked
to the front door of what was marked Unit B and unlocked
the door with one of the keys from Payne’s keyring. Officers
entered the home and conducted what they reported as a
“security sweep” to “make sure there was no one inside the
residence who could possibly come out of the residence and
harm [the officers].” During this initial search of the home,
officers observed in plain sight several bags of blue pills they
suspected of being fentanyl and a money-counting machine,
consistent with what they had earlier observed in the first
video on Payne’s cell phone.
     Officer Coddington then wrote a search warrant
application for the house on El Cortez Way. The application
listed all the information that Officer Coddington had
learned from his search of Payne’s cell phone. The
application also attested that Officer Coddington:
                        USA V. PAYNE                       9


(1) observed a BMW outside of Payne’s residence that the
key recovered from Payne’s person unlocked; (2) confirmed
the BMW was registered to Payne; (3) accessed Unit B with
another key on Payne’s keyring; and (4) saw several bags of
blue pills (suspected to be fentanyl) and a gold money-
counting machine during the initial sweep of the residence.
Two hours later, a Riverside County Superior Court judge
authorized the search warrant.
    The search of El Cortez Way under the authority of that
warrant was more thorough. Officers found several
documents, including pieces of mail, bearing Payne’s full
name. They also discovered a “white powdery substance”
throughout the home and a total of 104.3 grams of blue pills
marked “M/30.” The pills and powder were later confirmed
to be fentanyl, fluorofentanyl, and cocaine. In addition to
the drugs, officers recovered a total of $13,992 in cash, a
digital scale, the gold money-counting machine, and six cell
phones. Payne was arrested following the second search.
    On February 23, 2022, a federal grand jury returned an
indictment charging Payne with: (1) possession with intent
to distribute a mixture and substance containing fentanyl in
violation of 21 U.S.C. § 841(a)(1), (b)(1)(B)(vi);
(2) possession with intent to distribute fluorofentanyl in
violation of 21 U.S.C. § 841(a)(1), (b)(1)(C); and
(3) possession with intent to distribute cocaine in violation
of 21 U.S.C. § 841(a)(1), (b)(1)(C). Payne filed a motion to
suppress the evidence seized from the house on El Cortez
Way on April 25, 2022. He primarily argued that the
searches of his phone and the house on El Cortez Way
violated his Fourth and Fifth Amendment rights.
   The district court denied Payne’s motion in an oral ruling
on May 24, 2022. The court found that the search of Payne’s
10                      USA V. PAYNE


cell phone was reasonable under the Fourth Amendment
given that Payne was on parole in California and subject to
California’s standard search conditions that covered his
electronic devices. Further, the court determined that the
compelled use of Payne’s thumb to access the phone was a
nontestimonial act, placing it outside of Payne’s Fifth
Amendment privilege against self-incrimination. The court
found no separate Fourth Amendment violation for the first,
warrantless search of the house on El Cortez Way for two
reasons. First, because the search was justified under
Payne’s parole conditions and, second, because the search
warrant officers later obtained would have still been valid
after excising the information included in the warrant
application from the protective sweep of the home.
    Payne was sentenced on November 7, 2022, to 144
months in prison. After the district court entered final
judgment, Payne filed a timely notice of appeal. We have
jurisdiction under 28 U.S.C. § 1291.
                             II
    We begin with Payne’s Fourth Amendment challenges
to the CHP officers’ search of his cell phone. Given Payne
raises his Fourth Amendment claim in the context of a
challenge to the district court’s denial of his motion to
suppress, we review the denial of that motion de novo and
the district court’s factual findings for clear error. United
States v. Sullivan, 797 F.3d 623, 632–33 (9th Cir. 2015).
    The general suspicionless search condition in Payne’s
Notice and Conditions of Parole is mandated by California
law. See Cal. Penal Code § 3067(b)(3); 15 Cal. Code Regs.
§ 2511(b)(4). The California Supreme Court held the
condition was reasonable under the Fourth Amendment, in
large part because parolees, who enjoy only “conditional
                        USA V. PAYNE                        11


freedom,” have a significantly diminished expectation of
privacy, while the government has a strong interest in
assessing parolees’ rehabilitation and reentry while
simultaneously protecting the public. People v. Reyes, 968
P.2d 445, 450–51 (Cal. 1998); People v. Bryant, 491 P.3d
1046, 1054 (Cal. 2021) (“[A] warrantless search of a
parolee’s property or residence . . . is per se reasonable.”);
see also United States v. Johnson, 875 F.3d 1265, 1275 (9th
Cir. 2017). The Supreme Court of the United States agreed,
upholding suspicionless searches of parolees based on the
totality of the circumstances provided they are not “arbitrary,
capricious, or harassing.” Samson v. California, 547 U.S.
843, 856–57 (2006). In the years since Samson, we have
made clear that suspicionless parolee searches that
“compl[y] with the terms of a valid search condition will
usually be deemed reasonable under the Fourth
Amendment.” United States v. Cervantes, 859 F.3d 1175,
1183 (9th Cir. 2017).
    Our more recent cases have articulated the narrow set of
constraints that apply to law enforcement officers
conducting suspicionless parole searches. First, the officer
conducting the parole search must have probable cause to
believe “that the individual to be searched is on active
parole, and an applicable parole condition authorizes the
search or seizure at issue.” United States v. Estrella, 69
F.4th 958, 972 (9th Cir. 2023). Second, those searches
cannot be “arbitrary, capricious, or harassing.” Id. (internal
quotations and citations omitted); Reyes, 968 P.2d at 450;
see Cal. Penal Code § 3067(d) (“It is not the intent of the
Legislature to authorize law enforcement officers to conduct
searches for the sole purpose of harassment.”).
   Payne raises two distinct, yet inexorably entwined,
arguments: (1) that the officers on scene during the traffic
12                          USA V. PAYNE


stop used “unreasonable means” to unlock his phone
considering the language of his special search condition;3
and (2) that the search was arbitrary, capricious, or
harassing.
                                  A
    Payne’s unreasonable means argument most closely
implicates the principle, from Estrella, that officers must
have probable cause to believe an individual is on parole and
subject to an applicable parole condition that authorizes the
search at issue. 69 F.4th at 972. Here, the search at issue is
of Payne’s phone, made possible by the forced use of
Payne’s thumb to unlock the device. Payne posits the
question of whether CHP officers complied with the precise
terms of his parole conditions when they searched his cell
phone as a threshold one. In other words, he argues that the
parole search exception to the warrant requirement cannot
apply when officers do not follow the precise terms or
commands of a parole condition. He points to the language
in special parole condition number sixty-four for support,
which compelled Payne to surrender his cell phone to any
law enforcement officer for inspection and “provide [the]
pass key/code to unlock the device.” It further states that
“[f]ailure to comply can result in your arrest pending further
investigation and/or confiscation of any device pending

3
  Invoking Fed. R. Crim. P. 12, the government argues that Payne
forfeited his “unreasonable means” argument because he failed to
squarely present it in his motion to suppress. However, Payne’s
argument centers on the precise language of his parole conditions, which
was presented to and analyzed by the district court during the
suppression hearing. See United States v. Magdirila, 962 F.3d 1152,
1155–57 (9th Cir. 2020). Because Payne’s argument does not rely on
new facts or wholly distinct legal theories, we decline to deem it
forfeited.
                         USA V. PAYNE                        13


investigation.” Relying on the condition’s plain language,
Payne argues that the officers could not use his thumb to
unlock his phone when he refused to provide the numerical
passcode—their only recourse was to confiscate the device
or arrest him pending investigation, as outlined in the special
search condition.
    Textually, Payne’s unreasonable means argument has
certain cogency. The special search condition did not
require Payne to provide a biometric identifier to unlock any
electronic devices in his vicinity and it did include an express
enforcement provision. However, Payne’s argument suffers
from two fatal flaws. First, it ignores the more general,
statutorily mandated search condition included in his—and
every California parolee’s—Notice of Conditions of Parole.
Second, Payne’s proposed approach decouples the analysis
from the “totality of the circumstances” and
“reasonableness” inquiries that form the foundation of our
Fourth Amendment jurisprudence, including in the parolee
search context. See, e.g., Brigham City, Utah v. Stuart, 547
U.S. 398, 403 (2006); United States v. Knights, 534 U.S.
112, 118 (2001).
    While Payne’s special search condition addresses
electronic devices specifically, his general search condition,
mandated by California law, states that “any property under
[Payne’s] control are subject to search or seizure by . . . any
other peace officer, at any time of the day or night, with or
without a search warrant, with or without cause.” We have
before held that California’s statutory framework governing
the suspicionless search of parolees authorizes officers to
conduct warrantless searches of parolees’ cell phones. See
Johnson, 875 F.3d at 1275. The language of California’s
general search condition, written into all California parole
notices, is abundantly clear, putting parolees like Payne on
14                      USA V. PAYNE


notice that their person, home, phone, and other belongings
may be searched at any time without cause or a warrant. This
“clear and unambiguous search condition” serves to
“significantly diminish[] [parolees’] reasonable expectation
of privacy.” Samson, 547 U.S. at 852. Thus, under the
general search condition of Payne’s parole, he did not have
an “expectation of privacy that society would recognize as
legitimate” in the contents of his cell phone. Id. The
question then becomes whether the inclusion of the special
search condition in any way alters that reality.
    In applying Supreme Court precedent governing
warrantless parolee and probationer searches, we have
acknowledged that officers are generally required to conduct
these searches pursuant to valid search conditions. In United
States v. Caseres, we held that warrantless parole searches
do not withstand scrutiny when officers are unaware that
§ 3067, or a similar parole search statute or condition,
applies. 533 F.3d 1064, 1076 (9th Cir. 2008). Caseres drew
on well-founded concerns that officers could seek to use
broad parole search conditions—discovered to apply only
after a warrantless search took place—to retroactively justify
their actions. See id.; Samson, 547 U.S. at 856 n.5 (“[A]n
officer would not act reasonably in conducting a
suspicionless search absent knowledge that the person
stopped for the search is a parolee.”); Moreno v. Baca, 431
F.3d 633, 641 (9th Cir. 2005) (“[P]olice officers cannot
retroactively justify a suspicionless search and arrest on the
basis of an after-the-fact discovery of . . . a parole
condition.”); Fitzgerald v. City of Los Angeles, 485 F. Supp.
2d 1137, 1143 (C.D. Cal. 2007) (“[A]dvance knowledge of
a parolee’s status is critical to the constitutionality of a
suspicionless search of a parolee.”). These cases, on which
Caseres relied, did not hold that officers must have
                        USA V. PAYNE                       15


knowledge of the exact language of a parole condition.
Rather, they focused on whether the searching officers had
knowledge of a parolee’s status.
    In Estrella, we refined the prior knowledge language
from Caseres to mean that an officer must have both:
(1) “probable cause to believe that an individual is on active
parole before conducting a suspicionless search,” and
(2) probable cause to believe that “an applicable parole
condition authorizes the search . . . at issue.” 69 F.4th at
971–72. We opted for this standard, in lieu of an “actual
knowledge” standard, on the basis that the Fourth
Amendment “calls for reasonable determinations, and does
not demand certainty.” Id. at 968 (citing Hill v. California,
401 U.S. 797, 804 (1971)).
    Our decisions in Caseres and Estrella do not support
Payne’s proposition that the officers were compelled to
follow the special search condition to the letter or that the
special search condition served to override the general
search condition. Instead, they support the government’s
position that the general search condition authorized the
search of Payne’s cell phone. If we were to accept Payne’s
proposition, it would impose an impractical burden on
officers in the field to study a parolee’s specific parole
conditions before conducting the investigations they deem
necessary based on the circumstances with which they are
confronted. See Estrella, 69 F.4th at 968 (noting that
officers cannot be expected to possess “‘up-to-the-minute’
information of a parolee’s status before proceeding with a
routine compliance check”).
   Here, having confirmed Payne’s California parole status
with the Riverside County Sheriff’s dispatch, Officer
Coddington was on notice of Payne’s general search
16                      USA V. PAYNE


condition, which subjected all “property under [Payne’s]
control” to “search or seizure . . . at any time of the day or
night, with or without a search warrant, with or without
cause.” As a California officer, dealing with a California
parolee, he reasonably believed that §§ 3067(b)(3) and
2511(b)(4) authorized him to search Payne, his vehicle, and
his belongings, including his cell phone. The search was
thus independently justified under Payne’s general search
condition.
    That Payne was also subject to a special electronic
device search condition, of which Officer Coddington was
also aware, does not place the search of Payne’s cell phone
outside of the realm of reasonableness, even considering the
way Officer Coddington accessed its contents. In Delrio, the
California Court of Appeal considered the interplay between
California’s mandatory search conditions and other various
special conditions to which a parolee may be subjected. See
People v. Delrio, 259 Cal. Rptr. 3d 301, 304–09 (Ct. App.
2020). There, the court found that special conditions of
California parole, like special condition sixty-four in
Payne’s case, “do not appear intended to set restrictions on
the searches and seizures authorized by Penal Code section
3067, subdivision (b)(3), or to elevate a parolee’s
expectations of privacy.” Id. at 308. Instead, the court saw
the terms as interposing additional penalties for possible
parole violations. Id. (“When such special conditions are
selected, the parolee’s failure to adhere may give rise to
parole violation charges . . . .”). We agree.
   As Payne would have it, CHP officers’ only recourse for
Payne’s refusal to provide his numerical passcode would
have been the two options textually set forth in his special
parole condition: “arrest pending further investigation
and/or confiscation of any device pending investigation.”
                        USA V. PAYNE                        17


Payne argues that any officer conduct outside of those
measures would be per se unreasonable. But so drastically
limiting the range of permissible officer conduct based on
whether a parolee is subject to a special search condition
would lead to bizarre results. Nor do parole search
conditions have the strict textual force that Payne suggests
they should. See People v. Schmitz, 288 P.3d 1259, 1273
(Cal. 2012) (noting that the scope of a parole search is not
“strictly tied to the literal wording of the notification given
to the parolee upon release”); Delrio, 259 Cal. Rptr. 3d at
309 (“[T]he officers who performed the parole search of
defendant were not required to first ascertain and parse the
language of the [parole] form”).
    Law enforcement officers in the field can proceed with a
search under a parolee’s general search condition, assuming
that search is reasonable.        After all, the California
Department of Corrections and Rehabilitation defines
special conditions of parole as “rules imposed in addition to
the general conditions of parole,” not in place of those
general conditions. Parole Conditions, Cal. Dep’t of Corrs.
&       Rehab.,       https://www.cdcr.ca.gov/parole/parole-
conditions/ (last visited Apr. 10, 2024) (emphasis added).
These special conditions are imposed based on a parolee’s
particular offense and criminal history—i.e., aggravating
factors—and are designed as a further means by which the
department can “discourage criminal behavior.” Id. It
would thus make little sense to hold that Payne’s special
search condition materially raised his expectation of
privacy, providing him with a way to shield the contents of
his phone from officer inspection by refusing to provide his
passcode.
   At best, the special condition of Payne’s parole created
some minimal ambiguity concerning the reach of his parole
18                      USA V. PAYNE


conditions in the aggregate. In reviewing suspicionless
searches of parolees, the Supreme Court of the United States,
the Ninth Circuit, and the Supreme Court of California have
often analyzed parole conditions, their clarity, and officers’
knowledge of their express terms as factors to consider in a
comprehensive reasonableness analysis. For example, in
Samson, the Supreme Court of the United States found the
clear expression of a parole search condition as “salient,” but
still examined the search under the “totality of the
circumstances.” Samson, 547 U.S. at 852; see also Knights,
534 U.S. at 118; Johnson, 875 F.3d at 1275; People v.
Sanders, 73 P.3d 496, 506–07 (Cal. 2003). This totality of
the circumstances approach is sound, especially considering
that a parole search is an exception to the warrant
requirement, well-situated in broader Fourth Amendment
jurisprudence. See, e.g., Griffin v. Wisconsin, 483 U.S. 868,
873 (1987). With that approach in mind, we assess “on the
one hand, the degree to which [the search] intrudes upon an
individual’s privacy and, on the other, the degree to which it
is needed for the promotion of legitimate governmental
interests.” Knights, 534 U.S. at 119 (quoting Wyoming v.
Houghton, 526 U.S. 295, 300 (1999)).
    Payne’s parole status alone subjected him to a
significantly diminished expectation of privacy.        See
Johnson, 875 F.3d at 1275. With respect to his cell phone,
Payne signed and acknowledged multiple explicit parole
search conditions that required him to surrender any device
in his vicinity for search without cause. To the extent that
Payne’s special search condition created an ambiguity over
how far his general search condition could sweep, that
ambiguity may have marginally increased Payne’s
expectation of privacy in his cell phone. But any increase
based on these facts is de minimis. Payne knew he was on
                        USA V. PAYNE                       19


parole. He knew that, based on his parole conditions, all his
belongings could be searched at any time, including the
contents of his cell phone. Officer Coddington’s use of
means not specifically contemplated by Payne’s special
search condition to access a device over which Payne had no
significant privacy interest does not appear to have been
unreasonable.
    The reasonableness of the search is compounded when
Payne’s diminished privacy interest is weighed against the
government’s interest in supervising parolees. “[A] State’s
interests in reducing recidivism and thereby promoting
reintegration and positive citizenship among probationers
and parolees warrant privacy intrusions that would not
otherwise be tolerated under the Fourth Amendment.”
Samson, 547 U.S. at 853. The Supreme Court has described
this government interest as “overwhelming” based on
parolees increased propensity “to commit future criminal
offenses.” Id. (quoting Pennsylvania Bd. of Prob. & Parole
v. Scott, 524 U.S. 357, 365 (1998)). Here, the State’s already
significant interest was even greater based on Officer
Coddington’s knowledge of Payne’s assault with a deadly
weapon charge, Payne’s extreme nervousness during the
traffic stop, and Payne’s possession of over $1,000 in cash.
    Accordingly, we hold that the inclusion of Payne’s
special search condition did not vitiate the force of his
statutorily mandated general search condition, which
independently authorized the search at issue in this case.
Moreover, we hold that any ambiguity created by the
inclusion of the special condition, when factored into the
totality of the circumstances, did not increase Payne’s
expectation of privacy in his cell phone to render the search
unreasonable under the Fourth Amendment.
20                       USA V. PAYNE


                               B
    In addition to his unreasonable means argument, Payne
claims that the search of his cell phone violated California’s
prohibition against arbitrary, capricious, or harassing parole
searches.     Suspicionless parole searches that violate
California’s prohibition against arbitrary, capricious, or
harassing searches are constitutionally unreasonable.
Cervantes, 859 F.3d at 1183. This prohibition, however, is
“decidedly narrow” and only applies to situations where, for
example, a search “is based merely on a whim or caprice or
when there is no reasonable claim of a legitimate law
enforcement purpose.” Estrella, 69 F.4th at 972 (quoting
People v. Cervantes, 127 Cal. Rptr. 2d 468, 471 (Ct. App.
2002), as modified (Dec. 23, 2002)).
    Payne argues that “[o]nce the officers found nothing
illegal on [his] person or in his vehicle, that should have been
the end of the matter,” but he does not cite to any authority
suggesting that an officer’s failure to abandon their
investigation under these circumstances rises to the level of
a violation of the arbitrary, capricious, or harassing standard.
Instead, he cites cases involving the automobile exception
for the proposition that officers had no reason to search the
contents of Payne’s phone for evidence of his window tint
violation. Those cases, however, are inapposite because
officers must have probable cause to conduct a search under
the automobile exception to the warrant requirement. Parole
searches, on the other hand, require no such probable cause
determination as to the place or thing being searched.
   Finally, Payne claims that the officers’ search of his
photos, videos, and maps ran afoul of the Supreme Court’s
decision in Riley v. California, which held that officers could
not search the contents of an individual’s cell phone as
                             USA V. PAYNE                               21


incident to their arrest. 573 U.S. 373, 401 (2014). However,
we clearly rejected the argument that Riley applies to parole
searches of a cell phone in Johnson. 875 F.3d at 1273–75.
We therefore decline to extend Riley’s reasoning to the facts
of this case.
    The CHP officers who legitimately stopped Payne did so
based on their independent suspicion that Payne had violated
California’s Vehicle Code. They proceeded with their
investigation logically and appropriately after learning
Payne was a California parolee and observing his behavior.
Having failed to present any evidence that the CHP officers
who stopped Payne and eventually searched his cell phone
demonstrated any “arbitrary or oppressive conduct,” Reyes,
968 P.2d at 451 (citations omitted), we hold that the search
of Payne’s cell phone was reasonable. 4
                                   III
    Next, we consider Payne’s argument that CHP officers
violated his Fifth Amendment privilege against self-
incrimination when they compelled him to unlock his cell
phone using his fingerprint. Again, we review the district
court’s denial of Payne’s motion to suppress de novo, and its
factual findings for clear error. Sullivan, 797 F.3d at 632–
33.
    Ratified in 1791, the Fifth Amendment provides that
“[n]o person shall be . . . compelled in any criminal case to
be a witness against himself.” U.S. Const. amend. V. While


4
  To the extent that determination required the court to apply facts to law
in a way that was “essentially factual,” we discern no clear error in the
court’s conclusion. United States v. Franklin, 18 F.4th 1105, 1115 (9th
Cir. 2021) (quoting United States v. Hinkson, 585 F.3d 1247, 1259–60
(9th Cir. 2009) (en banc)).
22                      USA V. PAYNE


the precise scope of the privilege has, and continues to be,
subject to great debate, what has emerged is a three-prong
analysis, with each prong representing a standalone inquiry.
For a criminal defendant to benefit from the Fifth
Amendment privilege, there must be a “communication” at
issue that is: (1) compelled; (2) incriminating; and
(3) testimonial. See Hiibel v. Sixth Jud. Dist. Ct. of Nev.,
Humboldt Cnty., 542 U.S. 177, 189 (2004). The government
all but concedes that Payne has established the compelled
and incriminating prongs of the analysis, so we address them
only briefly.
    The district court implicitly found that CHP officers
compelled Payne to use his thumb to open the device, despite
Officer Coddington’s attestation that Payne reluctantly
opened the device on his own. For the purposes of this
appeal, the government has accepted Payne’s version of
events. Payne averred that, after he refused to give officers
his passcode, one of them “grabbed [his] thumb and
unlocked the phone.” This transpired while Payne was
handcuffed and in the back of a patrol vehicle. Compulsion
is present for Fifth Amendment purposes when,
“considering the totality of the circumstances, the free will
of the witness was overborne.” United States v. Anderson,
79 F.3d 1522, 1526 (9th Cir. 1996) (quoting United States v.
Washington, 431 U.S. 181, 188 (1977)). Based on Payne’s
version of events, the use of his thumb to unlock his phone
was compelled. He was physically restrained, in the back of
a squad car, and had already refused to provide officers with
the passcode to unlock the phone. Based on this resistance,
CHP officers took matters into their own hands, physically
selecting one of Payne’s thumbs to unlock the device.
    The use of Payne’s thumb to unlock his device was also
“incriminating.” This prong of the Fifth Amendment
                        USA V. PAYNE                        23


analysis has been interpreted to encompass “any disclosures
which the witness reasonably believes could be used in a
criminal prosecution or could lead to other evidence that
might be so used.” Kastigar v. United States, 406 U.S. 441,
445 (1972). Here, Payne could have reasonably concluded
that giving up his thumbprint, and thereby access to the vast
trove of personal information contained on his cell phone,
would lead to evidence that could be used against him in a
criminal prosecution. Indeed, that is exactly what happened.
    The more difficult question is whether the compelled use
of Payne’s thumb to unlock his phone was testimonial. To
date, neither the Supreme Court nor any of our sister circuits
have addressed whether the compelled use of a biometric to
unlock an electronic device is testimonial. Testimonial
communications are those that, “explicitly or implicitly,
relate a factual assertion or disclose information.” Doe v.
United States, 487 U.S. 201, 210 (1988). Of course, there
are no explicit communications on this record. Payne said
nothing when CHP officers used his thumb to unlock his
phone. His Fifth Amendment claim thus rests entirely on
whether the use of his thumb implicitly related certain facts
to officers such that he can avail himself of the privilege
against self-incrimination. This argument implicates two
lines of Supreme Court precedent: the physical trait cases
and the act of production doctrine.
    Compelled physical acts—i.e., those that require an
individual to serve as a “donor”—are not testimonial. The
physical trait cases have addressed circumstances where an
individual is compelled to: don a particular piece of clothing,
Holt v. United States, 218 U.S. 245, 252–53 (1910); stand in
a lineup, United States v. Wade, 388 U.S. 218, 223 (1967);
provide a handwriting or voice exemplar, Gilbert v.
California, 388 U.S. 263, 266–67 (1967) (handwriting
24                       USA V. PAYNE


exemplar); Wade, 388 U.S. at 222–23 (1967) (voice
exemplar); submit to fingerprinting, Wade, 388 U.S. at 223;
or have their blood drawn for DUI testing, Schmerber v.
California, 384 U.S. 757, 761 (1966). Each case reached the
same conclusion: not testimonial. In Schmerber, for
example, the Court recognized that history and lower court
precedent made clear that the privilege against self-
incrimination was designed to ward off “situations in which
the State seeks to . . . obtain[] the evidence against an
accused through the cruel, simple expedient of compelling it
from his own mouth.” Schmerber, 384 U.S. at 763 (internal
quotation marks omitted). Because the “[p]etitioner’s
testimonial capacities were in no way implicated” and his
“participation, except as a donor, was irrelevant to the results
of the test,” the Court held that the compelled blood draw
was not testimonial under the Fifth Amendment. Id. at 765.
    On its face, the use of Payne’s thumb to unlock his phone
appears no different from a blood draw or fingerprinting at
booking. These actions do not involve the testimonial
capacities of the accused and instead only compel an
individual to provide law enforcement with access to an
immutable physical characteristic. See Wade, 388 U.S. at
222–23. The next step of the investigation depends on the
“independent labor of [the state’s] officers.” Estelle v.
Smith, 451 U.S. 454, 462 (1981) (quoting Culombe v.
Connecticut, 367 U.S. 568, 581–82 (1961)). But Payne
maintains that the use of his thumb to unlock his phone is
fundamentally different from the compelled acts in past
physical trait cases, including the fingerprinting discussed in
Schmerber and Wade. See Schmerber, 384 U.S. at 764;
Wade, 388 U.S. at 223. According to Payne, this is because
of what the compelled use of his biometric implicitly
                              USA V. PAYNE                               25


communicated. He looks to the act of production doctrine
for support.
    Under the act of production doctrine, a purely physical
act may nonetheless be testimonial because of what it
communicates “wholly aside from the contents” of the thing
produced. Fisher v. United States, 425 U.S. 391, 410 (1976).
Although act of production cases have dealt exclusively with
responses to document subpoenas, their reasoning applies to
other situations. 5 The Supreme Court has reasoned that
producing a trove of documents in response to a subpoena
may implicitly communicate “the existence of the papers
demanded and their possession or control by the
[individual],” as well as the individual’s “belief that the
papers are those described in the subpoena.” Id. (citing
Curcio v. United States, 354 U.S. 118, 125 (1957)).
    The act of production doctrine’s triggering point
becomes clearer upon close reading of the Supreme Court’s
decisions in Doe, 487 U.S. 201, and United States v.
Hubbell, 530 U.S. 27 (2000). In Doe, the government
compelled an individual to “sign 12 forms consenting to
disclosure of any bank records respectively relating to 12
foreign bank accounts over which the Government knew or
suspected that Doe had control.” 487 U.S. at 203. However,
the consent forms did not force Doe to himself collect and

5
   The government suggests the doctrine only applies to subpoena
responses, arguing that there is “no basis to extend that doctrine to the
act of biometric unlock.” We are not so sure. The Supreme Court has
stated in its act of production jurisprudence that “[t]he difficult question
whether a compelled communication is testimonial for purposes of
applying the Fifth Amendment often depends on the facts and
circumstances of the particular case.” Doe, 487 U.S. at 214–15; see also
Fisher, 425 U.S. at 410 (noting questions of whether “tacit averments”
are testimonial “do not lend themselves to categorical answers”).
26                         USA V. PAYNE


turn over any documents. The Court held that this was not a
testimonial production, reasoning that the signing of the
forms related no information about existence, control, or
authenticity of the records that the bank could ultimately be
forced to produce. Id. at 215–16. For these reasons, the
consent forms were more akin to producing “a handwriting
sample or voice exemplar” because the act was not
“compelled to obtain ‘any knowledge [the suspect] might
have.’” Id. at 217 (quoting Wade, 388 U.S. at 222). 6 The
forms only provided the government with “access to a
potential source of evidence,” but locating the evidence itself
required “the independent labor of its officers.” Id. at 215
(internal quotation marks omitted and emphasis added).
    Hubbell, on the other hand, involved a “subpoena duces
tecum calling for the production of 11 categories of
documents.” Hubbell, 530 U.S. at 31. The suspect
eventually “produced 13,120 pages of documents and
records and responded to a series of questions that
established that those were all of the documents in his
custody or control that were responsive to the commands in
the subpoena.” Id. The Court held that this act of production
was of a fundamentally different kind than that at issue in
Doe because it was “unquestionably necessary for
respondent to make extensive use of ‘the contents of his own
mind’ in identifying the hundreds of documents responsive
to the requests in the subpoena.” Id. at 43. The “assembly
of those documents was like telling an inquisitor the

6
  Justice Stevens dissented from the majority opinion in Doe but
introduced an analogy that was central to his majority opinion in
Hubbell. He wrote that a defendant “may in some cases be forced to
surrender a key to a strongbox containing incriminating documents, but
I do not believe he can be compelled to reveal the combination to his
wall safe.” Doe, 487 U.S. at 219 (Stevens, J. dissenting).
                        USA V. PAYNE                       27


combination to a wall safe, not like being forced to surrender
the key to a strongbox.” Id. (citing Doe, 487 U.S. at 210
n.9). Thus, the dividing line between Doe and Hubbell
centers on the mental process involved in a compelled act,
and an inquiry into whether that act implicitly communicates
the existence, control, or authenticity of potential evidence.
     District courts applying Doe and Hubbell have arrived at
different conclusions on the biometric unlock question.
Payne relies heavily on a Northern District of California case
that held forced biometric unlocks violate the Fifth
Amendment. In re Residence in Oakland, Cal., 354 F. Supp.
3d 1010 (N.D. Cal. 2019) [hereinafter Oakland]. There, a
magistrate judge determined the act of production doctrine
applied for two primary reasons. First, because compelling
an individual to unlock a device with a biometric identifier
is the functional equivalent of compelling that person to turn
over their alphanumeric passcode, an act that is generally
accepted to be protected by the Fifth Amendment because it
requires an individual to divulge the contents of his mind.
Id. at 1015–16 (“[I]f a person cannot be compelled to
provide a passcode because it is a testimonial
communication, a person cannot be compelled to provide
one’s finger, thumb, iris, face, or other biometric feature to
unlock that same device.”). Second, because the act
instantly concedes “that the phone was in the possession and
control of the suspect, and authenticates ownership or access
to the phone and all of its digital contents.” Id. at 1016.
Other district courts have come to similar conclusions. See,
e.g., United States v. Wright, 431 F. Supp. 3d 1175, 1187–
88 (D. Nev. 2020); In re Single-Family Home & Attached
Garage, No. 17 M 85, 2017 WL 4563870, at *7 (N.D. Ill.
Feb. 21, 2017).
28                          USA V. PAYNE


     Still other district courts have come to the opposite
result. Addressing the Oakland court’s reasoning, these
cases assert that whether a passcode and a fingerprint unlock
are functional equivalents is an observation with no legal
significance to the Fifth Amendment analysis. See In re
Search Warrant No. 5165, 470 F. Supp. 3d 715, 734 (E.D.
Ky. 2020) (“The Court stands by the unambiguous
distinction in both the law and common sense between
something intangibly held in the most sacred of places—
one’s own mind—and an immutable physical
characteristic.”). Moreover, responding to the argument that
“if the device unlocks, then the incriminating inference is
that the person had possession or control of the device,”
these courts note that such a line of analysis improperly
conflates the incrimination prong with the testimonial prong.
See In re Search Warrant Application for [redacted text],
279 F. Supp. 3d 800, 805 (N.D. Ill. 2017). They ultimately
conclude that biometric unlock cases are no different than
other physical trait cases, like subjecting an individual to
fingerprinting or drawing a person’s blood, because the acts
at issue “do not themselves communicate anything.” Id. 7
    In Payne’s case, the Fifth Amendment question
stemming from the compelled use of his thumb to unlock his
phone bears striking resemblance to Justice Steven’s key vs.
combination analogy. While providing law enforcement
officers with a combination to a safe or passcode to a phone
would require an individual to divulge the “contents of his

7
  State courts are equally split on the issue. Compare, e.g., State v.
Pittman, 479 P.3d 1028, 1040–43 (Or. 2021) (unlocking phone using
biometrics is testimonial), with State v. Diamond, 905 N.W.2d 870, 874–
78 (Minn. 2018) (unlocking phone using biometrics is not testimonial);
People v. Ramirez, 316 Cal. Rptr. 3d 520, 544–50 (Ct. App. 2023)
(same).
                        USA V. PAYNE                        29


own mind,” turning over a key to a safe or a thumb to unlock
a phone requires no such mental process. Hubbell, 530 U.S.
at 43. To say that a passcode and a biometric are equivalents
and thus cannot receive different treatment under the law is
a syllogistic fallacy. The logic goes: biometrics are the
equivalent of or a substitute for a passcode and passcodes are
protected under the Fifth Amendment, so, biometrics are
also protected under the Fifth Amendment. The flaw lies in
the fact that the Supreme Court has framed the question
around whether a particular action requires a defendant to
divulge the contents of his mind, not whether two actions
yield the same result. See Hubbell, 530 U.S. at 43. The
functional equivalent argument attempts to make an end run
around this central piece of the Fifth Amendment inquiry.
When Officer Coddington used Payne’s thumb to unlock his
phone—which he could have accomplished even if Payne
had been unconscious—he did not intrude on the contents of
Payne’s mind.
    While we find the fact that there was no “cognitive
exertion” on Payne’s part most determinative, In re Search
of [redacted] Washington, D.C., 317 F. Supp. 3d 523, 538
(D.D.C. 2018), the relative level of existence, control, and
authentication established through a biometric unlock
compared to a comprehensive response to a subpoena is also
instructive. See Hubbell, 530 U.S. at 43. Payne concedes
that “the use of biometrics to open an electronic device is
akin to providing a physical key to a safe,” but argues it is
nonetheless a testimonial act because it “simultaneously
confirm[s] ownership and authentication of its contents.”
However, Payne was never compelled to acknowledge the
existence of any incriminating information. He merely had
to provide access to a source of potential information, just as
was the case in Doe and Schmerber. See Doe, 487 U.S. at
30                      USA V. PAYNE


215; Schmerber, 384 U.S. at 765. The officers were left to
identify any incriminating evidence through their own
investigation. This is decidedly unlike Hubbell, where the
subpoena respondent was implicitly conceding the
“existence, authenticity, and custody” of specific documents
that prosecutors could use in building its case against the
respondent. Hubbell, 530 U.S. at 41–42.
    One can imagine how Payne’s case might alternatively
fit more neatly in the Hubbell framework. For example, had
officers somehow compelled Payne to cull through the
information in his phone and produce any photos or videos
that demonstrated his participation in fentanyl trafficking,
there may have been a testimonial act of production.
Turning over those photos or videos would implicitly
concede that Payne had such videos, that they depicted what
the officers were looking for, and that they related to his
specific activities. Obviously, that is not the case here.
     The Supreme Court has also observed that implicit
authentication is the “prevailing justification” for extending
Fifth Amendment protection to acts of documentary
production because responding to a subpoena may be akin to
requiring a suspect to “implicitly testif[y] that the evidence
he brings forth is in fact the evidence demanded.” Fisher,
425 U.S. at 412 n.12 (internal quotations omitted) (quoting
Couch v. United States, 409 U.S. 322, 346 (1973) (Marshall,
J., dissenting)). But “[t]he fact that an individual is able to
unlock a phone with a physical characteristic does not
automatically make each individual set of data, such as
photos, videos . . . immediately authentic.” In re Search
Warrant Application for the Cellular Telephone in United
States v. Barrera, 415 F. Supp. 3d 832, 841 (N.D. Ill. 2019).
Authentication is not established in the same way here
compared to a response to a subpoena where the respondent
                        USA V. PAYNE                      31


is essentially stating the “item is what the proponent claims
it is.” Id. (quoting Fed. R. Evid. 901(a)). Phones like
Payne’s “can often be programmed to use multiple
individuals’ biometrics.” In re Search Warrant No. 5165,
470 F. Supp. 3d at 733. While the fact that Payne’s thumb
unlocked the phone proved to be incriminating, it alone
certainly did not serve to authenticate all the phone’s
contents.
    To the extent Payne relies on the Oakland court’s
attempt to distinguish biometric unlocks from “requiring a
suspect to submit to fingerprinting” because it immediately
results in access to more physical evidence and “there is no
comparison . . . required to confirm a positive match,” this
line of analysis conflates what is incriminating with what is
testimonial. Oakland, 354 F. Supp. 3d at 1016; see Doe, 487
U.S. at 210 (“[C]ertain acts, though incriminating, are not
within the privilege.”). All physical trait cases have dealt
with compelled acts eventually leading to incriminating
evidence that can be used in a suspect’s prosecution. See In
re Search Warrant Application for [redacted text], 279 F.
Supp. 3d at 805 (noting the “distinction—between whether
an act is testimonial versus whether the act is
incriminating—explains why physical characteristics, like
fingerprints, blood samples, handwriting, and so on are not
protected by the privilege even though they often are highly
incriminating”). The compelled use of an individual’s
thumb to unlock a device shares many of the same
incriminating inferences as comparing a suspect’s
thumbprint to a thumbprint lifted from a murder weapon.
The time it takes to make the connection, or the amount of
incriminating information that flows from the
nontestimonial act, is of little consequence.
32                          USA V. PAYNE


    Accordingly, we hold that the compelled use of Payne’s
thumb to unlock his phone (which he had already identified
for the officers) required no cognitive exertion, placing it
firmly in the same category as a blood draw or fingerprint
taken at booking. The act itself merely provided CHP with
access to a source of potential information, much like the
consent directive in Doe. The considerations regarding
existence, control, and authentication that were present in
Hubbell are absent or, at a minimum, significantly less
compelling in this case. Accordingly, under the current
binding Supreme Court framework, the use of Payne’s
thumb to unlock his phone was not a testimonial act and the
Fifth Amendment does not apply. 8
    We would be remiss not to mention that Fifth
Amendment questions like this one are highly fact dependent
and the line between what is testimonial and what is not is
particularly fine. Our opinion should not be read to extend
to all instances where a biometric is used to unlock an
electronic device. Indeed, the outcome on the testimonial
prong may have been different had Officer Coddington
required Payne to independently select the finger that he
placed on the phone. See In re Search Warrant Application
for [redacted text], 279 F. Supp. 3d at 804 (discussing how

8
  Payne argues that the Supreme Court’s decision in Riley supports a
different result because there the Court recognized that modern
technological advances like the use of smart phones may require
reexamination of certain privacy principles. 573 U.S. at 403. But Riley
analyzed cell phone searches under the Fourth Amendment, which calls
for a reasonableness analysis. See In re Search Warrant Application for
[redacted text], 279 F. Supp. 3d at 806. The Fifth Amendment demands
no such reasonableness inquiry. The narrow question before us is
whether the compelled use of Payne’s thumb is testimonial. Existing
Supreme Court precedent provides the necessary tools to answer that
question.
                        USA V. PAYNE                        33


a suspect would be required to engage in some thought
process if the government compels them to “decide which
finger (or fingers) to apply” to a sensor). And if that were
the case, we may have had to grapple with the so-called
foregone conclusion doctrine. See Fisher, 425 U.S. at 411.
We mention these possibilities not to opine on the right result
in those future cases, but only to demonstrate the complex
nature of the inquiry.
                              IV
    Having determined that the search of Payne’s cell phone
did not violate the Fourth or Fifth Amendment, Payne’s
argument that the evidence seized from El Cortez Way must
be suppressed as “fruit of the poisonous tree” fails.
    Next, Payne contends that the pre-warrant search of the
house on El Cortez Way independently violated his Fourth
Amendment rights. The government offers three possible
reasons why either the pre-warrant search was legal, or the
constitutionality of the pre-warrant search is immaterial to
the outcome of this case. First, it claims the search was valid
pursuant to Payne’s parole conditions. Second, it claims that
the search warrant CHP officers eventually obtained was
valid notwithstanding the constitutionality of the pre-
warrant search. Third, it claims that even if the search
warrant was invalid, the good faith exception to the
exclusionary rule applies. We agree with the government’s
second argument and, thus, do not address its first or third.
    We review the district court’s denial of Payne’s motion
to suppress de novo and can affirm on any basis the record
supports. United States v. Ruiz, 428 F.3d 877, 880 (9th Cir.
2005).
34                      USA V. PAYNE


    When a search warrant application includes “illegally
obtained information,” a reviewing court must determine
whether the warrant was supported by probable cause after
“properly purg[ing] the affidavit of the offending facts.”
United States v. Bishop, 264 F.3d 919, 924 (9th Cir. 2001).
Here, the district court held that “when you eliminate the
facts uncovered during the sweep, the warrant contained
probable cause.” In his reply brief, Payne expressly
conceded that he “agrees with the government . . . that the
information from his phone likely would have been
sufficient for probable cause even without the information
garnered during the illegal protective sweep.” We agree.
    Assuming without deciding that the pre-warrant sweep
of El Cortez Way violated Payne’s Fourth Amendment
rights, whether the warrant CHP officers obtained was
supported by probable cause —i.e., a “probability or
substantial chance of criminal activity”—depends on the
facts included in the warrant application that CHP officers
knew before the sweep. District of Columbia v. Wesby, 583
U.S. 48, 57 (2018). These included: (1) Payne was
extremely nervous, sweating profusely, and fumbling for his
documents when he was initially pulled over; (2) Payne
confirmed that he was on parole; (3) a search of Payne’s cell
phone showed a video depicting a large amount of cash, a
money-counting machine, and several bags of what officers
suspected to be fentanyl; (4) a separate video from Payne’s
phone showed the outside of the home on El Cortez Way;
(5) the map application on Payne’s phone showed a pin to a
parked vehicle outside a residence on El Cortez Way; and
(6) upon driving to the location on El Cortez Way, Officer
Coddington observed a silver BMW, confirmed it was
registered to Payne, and was able to unlock the vehicle using
the key seized from Payne’s person.
                        USA V. PAYNE                        35


    As Payne acknowledges in his reply brief, these facts go
well beyond establishing probable cause to believe that a
search of the house would uncover evidence of criminal drug
possession and trafficking. Thus, the search warrant was
valid even after excising the facts included in the application
from the pre-warrant protective sweep. The district court
rightfully denied Payne’s motion to suppress.
                       CONCLUSION
   We AFFIRM the denial of Payne’s motion to suppress.

```

---

## GROUP: content/cases/United States v. Perez-Rodriguez.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Perez-Rodriguez
type: case
citation: "13 F.4th 1 (2021)"
parallel_cite: ""
neutral_cite: ""
court: 1st Cir. 2021
court_level: coa
circuit: ca1
year: 2021
date_decided: 2021-09-02
docket: 19-1538P
authority_weight: "Binding in-circuit — 1st Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/5067201/united-states-v-perez-rodriguez/"
  cluster_id: 5067201
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Perez-Rodriguez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Entrapment]]"
    role: Key
related:
  - "[[Entrapment]]"
  - "[[Jacobson v. United States]]"
  - "[[Sherman v. United States]]"
tags:
  - case
  - entrapment
  - inducement
  - predisposition
  - jury-instruction
  - plain-error
  - first-circuit
holding: "The entrapment defense has two prongs — improper government inducement and the defendant's lack of predisposition — and a defendant who makes a modest production showing on both is entitled to have the jury instructed on entrapment; where an undercover agent posing on a dating app steered a target toward a sexual encounter with a fictitious minor, the district court's refusal to give the entrapment instruction was plain error, and the conviction was vacated and remanded for a new trial."
aliases:
  - United States v. Perez-Rodriguez
  - "United States v. Pérez-Rodríguez"
  - "United States v. Perez-Rodriguez (1st Cir. 2021)"
---

# United States v. Perez-Rodriguez

*13 F.4th 1 (1st Cir. 2021)* (No. 19-1538P) · U.S. Court of Appeals for the First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 5067201 → lead opinion 4882594 (13 F.4th 1, decided 2021-09-02); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
A Homeland Security Investigations agent ran a sting on an adults-only dating application, posing as a gay adult man. After Pérez-Rodríguez contacted the persona, the agent offered to arrange a sexual encounter with the agent's fictitious minor "boyfriend," an invented eleven-year-old. Pérez was charged with attempted enticement of a minor under 18 U.S.C. § 2422(b). He requested a jury instruction on entrapment, which the district court denied, and a jury convicted him. On appeal he challenged both the sufficiency of the evidence and the refusal to instruct on entrapment.

## Issue
Whether the district court erred in refusing to instruct the jury on entrapment, given the evidence of the government's inducement and the question of Pérez's predisposition.

## Rule
Entrapment shields a defendant who was not otherwise disposed to commit the crime but was induced to do so by the government, and a defendant is entitled to the instruction on a modest production showing as to each element. As the panel stated: "The defense has two prongs: (1) improper government inducement and (2) the defendant's lack of predisposition to commit the offense charged." — 13 F.4th 1, slip op. at 21. ^pin-op21

## Application
Although the court found the evidence sufficient to convict, it held that Pérez had made the modest showing needed to put entrapment to the jury. The agent had not merely furnished an ordinary opportunity to offend; posing as an adult romantic interest and then steering the exchange toward a fabricated child supplied evidence of improper inducement, and the record did not so conclusively establish predisposition as to withhold the question from the jury. Because the two prongs draw on overlapping facts and the evidence had to be viewed in the light most favorable to the defendant, the refusal to instruct deprived Pérez of his primary defense. Reviewing for plain error — because the objection was not renewed after the charge — the court found the error clear, prejudicial, and one that undermined the fairness of the proceeding.

## Conclusion
The conviction was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]] for a new trial**: the district court committed plain error in failing to instruct the jury on entrapment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Perez-Rodriguez* is a clean statement of the **two-prong** entrapment framework from *[[Jacobson v. United States|Jacobson]]* and *[[Sherman v. United States|Sherman]]* — improper inducement plus lack of predisposition — and of the **modest burden of production** that entitles a defendant to the instruction. Teach it for the inducement/predisposition split and for the rule that ambiguous entrapment evidence goes to the jury.

## Appears on
- [[Entrapment]] — *Key*

## Sources
- [*United States v. Perez-Rodriguez*, 13 F.4th 1 (1st Cir. 2021)](https://www.courtlistener.com/opinion/5067201/united-states-v-perez-rodriguez/) — pinpoint: slip op. at 21 (two-prong entrapment framework and burden of production; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6897520858dede74", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "13 F.4th 1 (2021)", "court": "1st Cir. 2021", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Perez-Rodriguez", "year": "2021"}}
{"assertion_id": "72ce9a038b84ea65", "dimension": "support", "kind": "home_role", "locator": {"home": "Entrapment"}, "payload": {"home": "Entrapment", "role": "Key", "title": "United States v. Perez-Rodriguez"}}
{"assertion_id": "f3058b38e5b9179f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The entrapment defense has two prongs — improper government inducement and the defendant's lack of predisposition — and a defendant who makes a modest production showing on both is entitled to have the jury instructed on entrapment; where an undercover agent posing on a dating app steered a target toward a sexual encounter with a fictitious minor, the district court's refusal to give the entrapment instruction was plain error, and the conviction was vacated and remanded for a new trial.", "title": "United States v. Perez-Rodriguez"}}
{"assertion_id": "4c3a7a4075b84bcd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 1st Cir.", "title": "United States v. Perez-Rodriguez"}}
{"assertion_id": "e49f4f375ba3f93b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Perez-Rodriguez", "varies_by_point": "false"}}
```

### lake record — United States v. Perez-Rodriguez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Perez-Rodriguez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Perez-Rodriguez",
    "case_name_short": "Perez-Rodriguez",
    "case_name_full": "",
    "input_case_name": "United States v. Perez-Rodriguez",
    "court": "1st Cir. 2021",
    "court_id": "ca1",
    "court_level": "coa",
    "circuit": "ca1",
    "state": null,
    "date_decided": "2021-09-02",
    "year": 2021,
    "docket": "19-1538P",
    "cluster_id": 5067201,
    "lead_opinion_id": 4882594,
    "sibling_ids": [],
    "absolute_url": "/opinion/5067201/united-states-v-perez-rodriguez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "13 F.4th 1",
      "volume": "13",
      "reporter": "F.4th",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "13 F.4th 1",
        "volume": "13",
        "reporter": "F.4th",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "13 F.4th 1",
    "official_selection": {
      "court_class": "state",
      "selected": "13 F.4th 1",
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
    "date_created": "2026-07-06T05:57:38Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:57:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:57:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-perez-rodriguez--5067201",
      "to_record_id": "United States v. Perez-Rodriguez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Perez-Rodriguez

```
          United States Court of Appeals
                     For the First Circuit


No. 19-1538

                    UNITED STATES OF AMERICA,

                            Appellee,

                               v.

                     RAFAEL PÉREZ-RODRÍGUEZ,

                      Defendant, Appellant.


          APPEAL FROM THE UNITED STATES DISTRICT COURT
                FOR THE DISTRICT OF PUERTO RICO

     [Hon. Pedro A. Delgado-Hernández, U.S. District Judge]


                             Before

           Kayatta, Lipez, and Barron, Circuit Judges.


     Linda A. Backiel for appellant.
     Julia Meconiates, Assistant United States Attorney, with whom
W. Stephen Muldrow, United States Attorney, and Mariana E. Bauzá-
Almonte, Assistant United States Attorney, were on brief, for
appellee.


                        September 2, 2021
            LIPEZ,        Circuit     Judge.         Rafael    Pérez-Rodríguez      was

convicted by a jury of attempted enticement of a minor for unlawful

sexual activity in violation of 18 U.S.C. § 2422(b).                            He was

apprehended through a sting operation in which a government agent

created a profile on an adults-only dating application posing as

a gay adult man, and, after being contacted by Pérez, then offered

to arrange a sexual encounter with his minor "boyfriend."                          Pérez

appeals    on       several     grounds,     including      insufficiency     of    the

evidence and the denial of a jury instruction on the entrapment

defense.     While we find Pérez's challenge to the sufficiency of

the   evidence        meritless,     we   conclude     that    the   district    court

committed       plain        error   in    failing     to     give   the   entrapment

instruction.          We therefore vacate the conviction and remand for a

new trial.

                                            I.

            In 2015, Ryan Seig, a special agent with the child

exploitation unit of Homeland Security Investigations ("HSI"),

conducted       a    sting     operation    using     the     geosocial    networking

application Grindr.            Agent Seig testified that the purpose of the

application is "to talk and usually meet with someone else who

shares your interests."               On cross-examination, he added "it's

social networking among homosexuals."                 Grindr describes itself as

"the largest social networking app for gay, bi, trans, and queer

people."            About,    Grindr,     https://www.grindr.com/about/            (last


                                             - 2 -
visited August 25, 2021).         Grindr allows users to create profiles

and to exchange messages with other users with profiles in their

geographic area.     Per Agent Seig's testimony, "[a] profile is a

small blurb about what you are looking for, possibly what you look

like, and sort of a general description of who you are and what

you want."     Grindr requires users to be eighteen years of age or

older and does not allow individuals to use the platform to seek

sexual encounters with minors.

          Agent Seig created a Grindr profile under the name "Dave

W."   He wrote in his profile, "Looking for young fun or to share

my young fun."    He testified that he chose this text as a "veiled"

reference to a sexual encounter with a minor, explaining that

"someone who was familiar with the way pedophiles communicate on

the internet could read this and know what it meant."           The profile

also described "Dave W." as "Muscular, White, Single."

          On     December   30,    2015,   the   Dave   undercover   profile

received a message from a profile with the name "Mirando," a

profile created by Pérez.         Dave and "Mirando" exchanged messages

on Grindr, and then moved to text messaging.            The precise language

of the messages is crucial to this case.1          Thus, we reproduce key

parts of the exchange in full.        The conversation began as follows:




      1The messages were primarily in Spanish. We draw from the
certified English translations that were admitted into evidence.


                                       - 3 -
Pérez: Hello what are you doing?

Dave: Hey what's up

Pérez: Let's see you

Dave: Cool, do you like really young guys?

Pérez: Yes
       Age?
       I started at 8

Dave: Me? 35, but my boyfriend is young

Pérez: Hahhaha Okk
       How old is he?
       What does your boyfriend like?

Dave: He likes everything :)
      He is very young, what age do you like?

Pérez: The younger the better
       I don't discriminate
       I started at 8 hehehhe
       So you tell me
       What does he like to do?
       We are close, we can come up with some fun
       From there up I do it all

Dave: Do you understand English? I speak only a little
      Spanish
      My boyfriend is 11 years old. Do you want to play
      with him?

Pérez: Mmmm yessss
       Where is he?
       I speak little only a little English?
       Share pics??
       You tell me when and where???
       Do you prefer to call?
       Yes, I want to play

Dave:   We live in[] San Juan.
        We're free next week.




                        - 4 -
          Pérez: Ok
                 Have whatsapp?
                 Send me pics?
                 Can you now?

          Dave: Yes I'm busy with a party

          Pérez: Ok, but you are close
                 Can you get away?
                 Can you*

          Dave: Last night, no haha :)
                Do you want anal with him or oral?

          Pérez: Everything
                 I want the 3 of us to play
                 You for a while and me for a while.   You like?

          Dave:   Me too
                  Yes

          Pérez: Send me something to see you playing with him
                 I like taboo

          Dave:   Me too :)

          Pérez: Have a pic?
                 Are you with him at the party

          Dave: I don't want to send a pic because I won't know
                who you are until we meet
                Yes, he is here
                You can take pics if this happens. Just no faces
                I don't have whatsapp
                But I can text

          Pérez: Text is better

Pérez then sent two photos of himself to "Dave," and Dave provided

Pérez with a telephone number.

          The next day, December 31, Pérez sent Dave a text message

to continue the conversation.    He again expressed sexual interest

in "Dave's" minor "boyfriend."     Dave messaged, "we're going to


                                  - 5 -
have a lot of fun, friend. :) . . . Him you and I[.]"          Pérez

requested pictures of "Dave."       Pérez asked Dave questions about

his relationship with the minor.     ("How did you get him?" and "How

long have you had him?").

             On January 1, Pérez messaged Dave and said, "Happy New

Year."   He again said, "I want your boyfriend."      Pérez and Dave

discussed their availability for a meeting that week.           They

exchanged messages about what Pérez wants to do during the sexual

encounter.     Pérez asked several questions about how Dave met the

minor, what the minor's parents think, and whether "Dave's" family

knows about the minor.    "Dave's" answers included "He's my friend"

and "I am a 'good influence.'"

             On January 2, Dave initiated the conversation.       He

writes, "Just saying hi.        Very busy with family!     Happy new

year ;)[.]"     The following day, Dave and Pérez discussed meeting.

             Pérez: Let's see each other tomorrow to get to know you

             Dave: Ok, what time can you do it?

             Pérez: Write me when you wake up
                    I get up early
                    Where should we meet?

             Dave: Are we using your house or mine for the threesome?

             Pérez: Yes. I live alone. But if it's at home, then it
                    should be in the afternoon
                    But I want to see you before to get to know you
                    and see what you want to do so that I'm
                    comfortable

             Dave: I understand.   Me too.


                                    - 6 -
             Pérez: Ok

             Dave: Where is a good place for us all to meet?

             Pérez: Where should we meet

             Dave: We can meet and then go to your house for sex with
                   all of us?
                   I can meet anywhere. It doesn't matter. We'll
                   talk in the morning when you know more concerning
                   your schedule

             Pérez: Yes
                    Depends on what we talk about and we'll go
                    I am free. Write to me tomorrow.

Pérez then requested a picture of Dave again.           He asked Dave

several more questions about his relationship with the minor. Dave

said that the minor is "excited, happy" about the planned sexual

encounter.     They agreed to meet at Guaynabo Plaza.    Pérez stated

"first I see you" and asked "Can you come alone?"       Dave replied,

"I can leave him at my place and you can follow me there, ok?"

Pérez responded, "Yes."

             The following morning, Monday, January 4, Dave started

the conversation again, initiating this exchange:

             Dave: Can you meet at 3?

             Pérez: Ok

             Dave: Cool

             Pérez: Ok

             Dave: I spoke with him and he's excited :)
                   He's worrie[d] about what clothes to bring
                   LOL
                   What parking do you want to meet in?
                   Are you busy?


                                   - 7 -
Pérez: Hahahhahha
       Go to Guaynabo Plaza and I'll tell you where
       we'll meet
       Remember that I want to talk to you first. I
       need to feel safe.

Dave: Yes, me too, it's a good idea.
      I am also scared.

Pérez: That's why I want to see you by yourself.
       I would like to know you first.

Dave: Yes, he will be at my house

Pérez: Ok

Dave: Waiting with the XBOX and beers LOL

Pérez: What are you like, physically?
      Mmmmm
      I like beer
      He doesn't get in trouble for drinking?

Dave: Like in my profile.
      5'9" or 5'10". Brown hair.

Pérez: Gym body?

Dave: Yes, I lift weights 4-5 days a week
      I am not fat

Pérez: And what's he like?

Dave: Skinny, like a young guy.     He is Boricua, with
      short hair.

Pérez: Ok

Dave: He likes soccer jerseys?
      He's very intelligent and friendly

Pérez: Let's see one another now to talk and be horny
       about what we're going to do.




                      - 8 -
The two men eventually agreed to meet at the Martinez Nadal train

station at 4 p.m.

          At the appointed time, Agent Seig drove to the station

and parked his vehicle in the parking lot.   Seig had informed other

members of his unit about the meeting, and several additional HSI

agents were also waiting in the parking lot.    Pérez drove into the

parking lot, pulled up alongside Agent Seig's vehicle, and got out

of his car.    HSI agents immediately arrested him.

          On January 27, 2016, a grand jury returned an indictment

charging Pérez with one count of attempted enticement of a minor

in violation of 18 U.S.C. § 2422(b).    Prior to commencement of the

jury trial, the parties submitted proposed jury instructions.

Pérez filed a separate ex parte request for an entrapment jury

instruction.

          A two-day jury trial was held beginning on May 15, 2017.

The   government's   case   primarily   consisted   of   Agent   Seig's

testimony and the transcripts of the Grindr and text messages.2

Pérez did not present any witnesses.3 At the close of the evidence,




      2The government also presented testimony from two other HSI
agents present at the arrest.     An AT&T security manager also
explained how he confirmed that the phone which sent the messages
belonged to Pérez.

      3Pérez attempted to present character witnesses, but the
court excluded the testimony as impermissible under the Federal
Rules of Evidence because there was no pertinent character trait
associated with the crime charged.


                                   - 9 -
Pérez moved for acquittal under Rule 29. The district court denied

the motion.          The parties participated in a charging conference,

which was not recorded.            Nevertheless, the record indicates that

Pérez renewed his request for an entrapment jury instruction at

that conference because the district court denied the entrapment

instruction in a docket entry, stating, "The ruling is based on

the arguments presented by the government and defendant's response

during the charging conference in connection with predisposition.

In the end, the evidence presented at trial did not justify an

entrapment instruction."              Before instructing the jury, the court

asked       the     parties   if   there      were    "any     objections      to   the

instructions."         Pérez did not raise any objections at that time.

After       charging    the   jury,    the   district    court    did    not    invite

objections from the parties.               Pérez did not raise any objection.

The jury deliberated for less than one hour and returned a guilty

verdict.          On May 14, 2019, Pérez was sentenced to 151 months of

incarceration.

               Pérez    timely     filed     this    appeal.      In    addition    to

challenging the sufficiency of the evidence, he asserts that the

district court erred in rejecting his request for an entrapment

instruction.4



      Pérez raises four additional claims of error: (1) inadequate
        4

questioning during voir dire, (2) violations of the Jones Act, see
48 U.S.C. § 864 (requiring that all trial proceedings in the



                                             - 10 -
                                  II.

            We review de novo the district court's denial of Pérez's

properly preserved claim that the evidence presented at trial was

insufficient to support the jury's verdict.        See United States v.

Tanco-Baez, 942 F.3d 7, 15 (1st Cir. 2019).             In evaluating a

sufficiency of the evidence claim, "we examine the evidence, both

direct and circumstantial, in the light most favorable to the

prosecution   and   decide   whether    that   evidence,   including   all

plausible   inferences   drawn   therefrom,    would   allow   a   rational

factfinder to conclude beyond a reasonable doubt that the defendant

committed the charged count or crime." United States v. Velázquez-

Aponte, 940 F.3d 785, 798 (1st Cir. 2019) (quoting United States

v. Díaz-Rosado, 857 F.3d 116, 120–21 (1st Cir. 2017)).

A. The Elements of the Offense

            Pérez was found guilty of violating 18 U.S.C. § 2422(b),

which provides:

            Whoever, using the mail or any facility or
            means of interstate or foreign commerce, or
            within the special maritime and territorial
            jurisdiction of the United States knowingly
            persuades, induces, entices, or coerces any
            individual who has not attained the age of 18


District of Puerto Rico be conducted in English), and the Court
Reporter Act, see 28 U.S.C. § 753(b) (requiring federal court
proceedings to be recorded verbatim), (3) improper opinion
testimony, and (4) improper exclusion of a character witness.
Except for some observations on the voir dire process, we do not
address the other issues raised given our conclusion that Pérez's
conviction must be vacated on the basis of the court's failure to
give an entrapment instruction.


                                   - 11 -
            years, to engage in prostitution or any sexual
            activity for which any person can be charged
            with a criminal offense, or attempts to do so,
            shall be fined under this title and imprisoned
            not less than 10 years or for life.

To support a conviction under the attempt portion of the statute,

the government must show that the defendant attempted to "(1) use

a facility of interstate commerce (2) to knowingly persuade,

induce, entice, or coerce (3) an individual under the age of 18

(4) to engage in illegal sexual activity."5       United States v. Berk,

652 F.3d 132, 138 (1st Cir. 2011) (quoting United States v.

Gravenhorst, 190 F. App'x 1, 3 (1st Cir. 2006) (per curiam)).

            To prove an attempt, the government must establish both

a   specific   intent   to   commit   the   substantive   offense   and   a

substantial step toward its commission.         Id. at 140.   Hence, for

conviction under § 2422, the specific intent required is the intent

to persuade, induce, entice, or coerce a minor into engaging in

illegal sexual activity.      We have interpreted this requirement as

broadly requiring an intent "to achieve a mental state -- a minor's

assent -- regardless of the accused's intentions vis-à-vis the

actual consummation of sexual activities with the minor."           United

States v. Dwinells, 508 F.3d 63, 71 (1st Cir. 2007) (emphasis

omitted).


      5Here, the government argued, the illegal sexual activity
was sexual assault under Puerto Rico law. See P.R. Laws Ann. tit.
33, § 5191(a) (defining sexual assault to include sex with someone
under age sixteen).


                                      - 12 -
            A substantial step toward commission of an offense is

"less than what is necessary to complete the substantive crime,

but more than 'mere preparation.'"      Berk, 652 F.3d at 140 (quoting

United States v. Piesak, 521 F.3d 41, 44 (1st Cir. 2008)).             This

requirement    serves   to   "distinguish   between   those   who   express

criminal aims without doing much to act on them and others who

have proved themselves dangerous by taking a substantial step down

a path of conduct reasonably calculated to end in the substantive

offense."     United States v. Doyon, 194 F.3d 207, 211 (1st Cir.

1999).   We have found that a variety of actions, including actions

short of meeting the minor in person, can constitute a substantial

step toward a § 2422(b) offense.       See United States v. Rang, 919

F.3d 113, 121 (1st Cir. 2019) (defendant reserved hotel room and

sought consent from the minor's mother for a "sleepover" with the

minor); Berk, 652 F.3d at 140 (defendant offered to help a woman

find housing in exchange for sex with her daughter and sent the

woman leads about homes for rent); Gravenhorst, 190 F. App'x at 4

(defendant sent minors sexually explicit messages and proposed

meeting in person).     But see Berk, 652 F.3d at 140-41 (noting that

"explicit sexual talk alone" does not constitute a substantial

step toward a § 2422(b) offense (citing United States v. Gladish,

536 F.3d 646, 652 (7th Cir. 2008))).         Direct communication with a

minor, real or fictitious, is not required.           A person can commit

a § 2422(b) offense by communicating with an adult who acts as an


                                    - 13 -
"intermediary" between the defendant and a minor.    See Berk, 652

F.3d at 140.

B. The Sufficiency of the Evidence Against Pérez

           On the first element, intent, Pérez argues that the

government failed to provide enough evidence to allow a jury to

conclude that he intended to persuade, induce, entice, or coerce

a minor.    He asserts: "There was no reason to do that [i.e.,

persuade, induce, entice, or coerce] here because the agent offered

[a minor] he presented as already ready, willing, and experienced,

'lik[ing] everything.'"   In his view, the evidence, at most, could

allow the jury to conclude that Pérez communicated with an adult

with the intention of "bringing about a meeting at which prohibited

conduct was supposed to, or likely to occur."

           Pérez's focus on the fictitious minor's supposed sexual

experience and willing participation is seriously misplaced.     A

child who has previously been sexually abused or is otherwise

depicted as "experienced" can still be a victim of persuasion,

inducement, enticement, or coercion.   See United States v. Hinkel,

837 F.3d 111, 116 (1st Cir. 2016) (upholding a § 2422(b) conviction

where the minor was described as "15 but experienced").      And a

child's expression that he "like[s] it" and wants to engage in

illegal sexual activity does not mean that persuasion, inducement,

enticement, or coercion could not possibly play a role.        See

Dwinells, 508 F.3d at 67 (upholding a § 2422(b) conviction where


                                 - 14 -
law enforcement agents posing as minors responded positively to

the defendant's sexual advances, including one fictitious minor

who "assured him that she would consent" to sexual activity in

person).   To suggest otherwise is to misunderstand the nature of

child sexual abuse.   See United States v. Gonyer, 761 F.3d 157,

167 (1st Cir. 2014) (describing the process of a sexual predator

"grooming" a child to form an emotional connection which would

lead the child to be persuaded to engage in sexual activity);

United States v. Brand, 467 F.3d 179, 203 (2d Cir. 2006) ("Child

sexual abuse is often effectuated following a period of 'grooming'

and the sexualization of the relationship." (quoting Sana Loue,

Legal and Epidemiological Aspects of Child Maltreatment, 19 J.

Legal Med. 471, 479 (1998))).

           It was reasonable for the jury to believe that the

fictitious eleven-year-old boy Dave "offered" to Pérez would not

participate in the planned sexual encounter absent persuasion,

inducement, coercion, or enticement -- at a minimum, "implicit

coaxing or encouragement."    See United States v. Montijo-Maysonet,

974 F.3d 34, 42 (1st Cir. 2020) ("[T]he four verbs Congress

used -- including 'entice' and 'induce' -- plainly reach implicit

coaxing or encouragement designed to 'achieve . . . the minor's

assent' to unlawful sex[.]" (second omission in original) (quoting

Dwinells, 508 F.3d at 71)).    And it was reasonable for the jury to

conclude that Pérez must have been cognizant of that reality and


                                  - 15 -
was relying on Dave to affect his "boyfriend's" mental state such

that the minor would participate.          Although Agent Seig's text

messages can be read to imply that Dave had already groomed the

minor for the sexual activity, the jury could reasonably infer

that Pérez intended to use Dave as an intermediary to "entice"

(meaning "to draw on by arousing hope or desire: allure, attract,"

id.) the minor into participating in illegal sexual activity with

Pérez on January 4, 2016.

          On    the   second    element,    substantial   step,     Pérez

emphasizes that he never communicated directly with a minor.          Such

communication is not required to establish a substantial step

towards commission of a § 2422(b) offense.      In Berk, we recognized

that "a defendant can be convicted [of a § 2422(b) offense] even

if the relevant communications are with an intermediary."             652

F.3d at 140.    Berk involved communications between the defendant

and parents of minor children, but we did not state that only

parents could serve as intermediaries in the commission of a

§ 2422(b) offense.    See id.   Indeed, the rationale for relying on

a sexual predator's use of intermediaries extends to any adult

with sufficient influence or control over a minor.           As explained

by the Third Circuit, in an opinion cited in Berk,           § 2422(b) is

"part of an overall policy to aggressively combat computer-related

sex   crimes   against   children[]   [and]   [i]t   would     be   wholly

inconsistent with the purpose and policy of the statute to allow


                                   - 16 -
sexual predators to use adult intermediaries to shield themselves

from prosecution."       United States v. Nestor, 574 F.3d 159, 162 (3d

Cir. 2009); see also Montijo-Maysonet, 974 F.3d at 42 ("Congress

. . . meant to cast a broad net (consistent with the Constitution)

to catch predators who use the Internet to lure children into

sexual encounters." (citing H.R. Rep. 105-557, at 21 (1998), as

reprinted in 1998 U.S.C.C.A.N. 678, 678–79)).

             The "broad net" plainly must cover a defendant who

attempted    to    use     any   intermediary    adult   perceived    to    have

sufficient    sway    to    "lead   a   child    to   participate    in   sexual

activity."     See United States v. Douglas, 626 F.3d 161, 164 (2d

Cir. 2010). The defendant's understanding of the nature and degree

of the adult's control over the minor is a question of fact for

the jury.    Here, the jury could reasonably infer that an adult man

whose "boyfriend" is a minor, and who confidently invites another

man to have sex with the child, would have been viewed by the

defendant as      someone with the power        to elicit the minor's assent

to illegal sexual activity.6

             Pérez   similarly      argues   a    lack   of   evidence     of   a

substantial step because the evidence showed he arrived at the




     6 Pérez mischaracterizes the evidence by describing Dave as
"a part-time tutor" to the minor. While Dave did mention that the
minor was his student, he more importantly described him as his
"boyfriend" and a person with whom he had an ongoing sexual
relationship for six months.


                                        - 17 -
parking lot to meet Dave, not the minor. We agree with the district

court that "the act of traveling to meet an intermediary . . . has

been held sufficient to establish a 'substantial step.'"            United

States v. Pérez-Rodríguez, No. 16-041 2016, WL 7442650, at *2

(D.P.R. Dec. 27, 2016) (citing Berk, 652 F.3d at 140).             Drawing

all inferences in favor of the government, a rational jury could

find that Pérez's communications with Dave and his subsequent

arrival   at   the   meeting   he   arranged   with   Dave   constituted   a

substantial step to persuade, induce, entice, or coerce a minor.

Thus, there was sufficient evidence to convict and the motion for

acquittal was properly denied.

                                    III.

           The district court declined to instruct the jury as to

the elements of Pérez's primary defense, entrapment, because, in

its view, the record did not contain sufficient evidence to warrant

the instruction.      Pérez argues that this omission denied him a

fair trial.

A. Standard of Review

           Preserved objections to the denial of a requested jury

instruction are subject to plenary review. United States v. Joost,

92 F.3d 7, 12 (1st Cir. 1996).        If, however, the defendant fails

to preserve his claim of entitlement to a jury instruction, the

claim is forfeited, and we review the district court's decision

under the plain error standard of Rule 52(b) of the Federal Rules


                                      - 18 -
of Criminal Procedure.            United States v. Baltas, 236 F.3d 27, 36

(1st Cir. 2001).          It has been the longstanding rule of this circuit

to treat a challenge to jury instructions as forfeited if the

defendant fails to object to the instructions after the judge has

charged the jury, regardless of whether he previously brought the

matter to the judge's attention.               United States v. Wilkinson, 926

F.2d 22, 26 (1st Cir. 1991) ("As we have repeatedly held, . . .

[a] party may not claim error in the judge's charge to the jury

unless that party 'objects' after the judge gives the charge but

before the 'jury retires . . . .'" (quoting Fed. R. Crim. P. 30)),

overruled on other grounds by Bailey v. United States, 516 U.S.

137, 149 (1995).          Though Pérez requested an entrapment instruction

before the trial and argued for it at a charging conference, he

did   not   lodge     a    post-charge    objection    to   the    denial   of   the

instruction.7         Thus, Pérez's claim is subject to plain error

review.

            To meet the heavy burden of establishing plain error, an

appellant must show "(1) that an error occurred (2) which was clear

or    obvious   and       which   not   only   (3)   affected     the   defendant's

substantial rights, but also (4) seriously impaired the fairness,



       Pérez also failed to make an objection when the judge invited
       7

objections on the record directly before instructing the jury.
Even if Pérez had made such an objection, his claim would still be
subject to plain error review under our precedent because he did
not renew it after the instruction, and we hold parties strictly
to that timing. See Wilkinson, 926 F.2d at 26.


                                           - 19 -
integrity, or public reputation of judicial proceedings."                United

States v. Duarte, 246 F.3d 56, 60 (1st Cir. 2001).                   The first

prong, "error," consists of "[d]eviation from a legal rule."

United States v. Olano, 507 U.S. 725, 732-33 (1993).                 The second

prong requires that the error identified in the first prong is not

"open to doubt or question," though an appellant can meet this

requirement even in the "absence of a decision directly on point."

United States v. Morales, 801 F.3d 1, 10 (1st Cir. 2015).8                    To

establish the third prong, the appellant must show that "it is

reasonably probable that the . . . error affected the result of

the proceedings."        United States v. Latorre-Cacho, 874 F.3d 299,

303 (1st Cir. 2017).            Our analysis under the fourth prong is

guided by our fundamental concern with "the public legitimacy of

our    justice    system[,]     [which]   relies   on   procedures    that   are

'neutral, accurate, consistent, trustworthy, and fair.'"               Rosales-

Mireles v. United States, 138 S. Ct. 1897, 1908 (2018) (quoting

Josh       Bowers &   Paul H.    Robinson,    Perceptions of Fairness and




       We note that, in our circuit, the second prong is sometimes
       8

described as "clear and obvious error," e.g., United States v.
Scott, 877 F.3d 42, 49 (1st Cir. 2017), while in other opinions it
is phrased as "clear or obvious error," e.g., United States v.
Aquino-Florenciani, 894 F.3d 4, 7 (1st Cir. 2018). As far as we
can tell, there is no substantive difference between the two
usages. In fact, we are unaware of any decision suggesting that
the words "clear" and "obvious" have different meanings. We will
use the "clear or obvious" formulation here, which appears to be
the more frequent usage.


                                          - 20 -
Justice: The Shared Aims and Occasional Conflicts of Legitimacy

and Moral Credibility, 47 Wake Forest L. Rev. 211, 215–16 (2012)).

            The plain error standard is a difficult burden for any

appellant to meet.      See United States v. Gelin, 712 F.3d 612, 620

(1st Cir. 2013) ("This multi-factor analysis makes the road to

success   under   the    plain      error       standard     rather    steep;   hence,

reversal constitutes a remedy that is granted sparingly.").                        It is

a particularly challenging standard to meet in the context of an

unpreserved objection to jury instructions.                   See United States v.

Paniagua–Ramos, 251 F.3d 242, 246 (1st Cir. 2001) ("[T]he plain

error hurdle, high in all events, nowhere looms larger than in the

context of alleged instructional errors.").                   Nonetheless, on rare

occasions, the severity of an error in instructing the jury does

rise to the level of plain error and requires vacatur of the

conviction.    See, e.g., Latorre-Cacho, 874 F.3d at 310; United

States v. Delgado-Marrero, 744 F.3d 167, 189 (1st Cir. 2014).

B. The Entrapment Defense

            Entrapment       provides       a    defense      if    law   enforcement

officers "originate a criminal design, implant in an innocent

person's mind the disposition to commit a criminal act, and then

induce    commission    of    the    crime       so   that    the     Government    may

prosecute."    Jacobson v. United States, 503 U.S. 540, 548 (1992);

see United States v. Teleguz, 492 F.3d 80, 84 (1st Cir. 2007)

("Congress could not have intended that its statutes were to be


                                            - 21 -
enforced by tempting innocent persons into violations." (quoting

Sherman v. United States, 356 U.S. 369, 372 (1958)).                     The defense

has two prongs: (1) improper government inducement and (2) the

defendant's lack of predisposition to commit the offense charged.

Id.

             1. Improper Inducement

             Improper inducement, also referred to as "government

overreaching,"     occurs    when   law     enforcement        agents     engage    in

conduct "of the type that would cause a person not otherwise

predisposed to commit a crime to do so."                Hinkel, 837 F.3d at 117.

The mere creation of an "opportunity to commit a crime" through a

"sting" operation does not, in and of itself, constitute improper

inducement.    United States v. Gendron, 18 F.3d 955, 961 (1st Cir.

1994)   (quoting   Jacobson,       503    U.S.     at    550).      Rather,     "[a]n

'inducement' consists of an 'opportunity' plus something else --

typically, excessive pressure by the government upon the defendant

or the government's taking advantage of an alternative, non-

criminal type of motive."           Id.     "Plus" factors that may tip a

government    operation     from    a     permissible      sting       operation   to

improper     inducement     include,      for    example,        intimidation      and

threats,     "dogged   insistence,"         playing       on     the    defendant's

sympathies, and "repeated suggestions."                 Id. (collecting cases).

"[E]ven very subtle governmental pressure, if skillfully applied,

can amount to inducement."          United States v. Poehlman, 217 F.3d


                                          - 22 -
692, 701 (9th Cir. 2000).        The judgment of whether government

conduct has crossed the line from valid law enforcement tactic to

improper inducement is often a difficult factfinding question for

the jury because "the facts [may] fall somewhere in a middle ground

between what is plainly proper and what is plainly improper."

United States v. Acosta, 67 F.3d 334, 338 (1st Cir. 1995); see

also id. ("To assume that we are dealing with a sharp boundary

rather than a spectrum is an illusion.").

             2. Lack of Predisposition

             The second element of the entrapment defense turns on

whether the "defendant was disposed to commit the criminal act

prior to first being approached by Government agents."          Jacobson,

503   U.S.   at   549.   Our   decision   in   Gendron   sets   forth   our

understanding of this element as follows:

             The right way to ask the question, it seems to
             us, is to abstract from -- to assume away --
             the present circumstances insofar as they
             reveal government overreaching. That is to
             say, we should ask how the defendant likely
             would have reacted to an ordinary opportunity
             to commit the crime. By using the word
             "ordinary," we mean an opportunity that lacked
             those special features of the government's
             conduct that made of it an "inducement," or an
             "overreaching."      Was     the     defendant
             "predisposed" to respond affirmatively to a
             proper, not to an improper, lure?

Gendron, 18 F.3d at 962 (citation omitted).         The purpose of this

predisposition inquiry is to determine whether the defendant is

"someone who would likely commit the crime under the circumstances


                                    - 23 -
and for the reasons normally associated with that crime, and who

therefore poses the sort of threat to society that the statute

seeks to control, and which the government, through the 'sting,'

seeks to stop."       Id. at 963.          The "critical time"       for the

predisposition analysis is the time "in advance of the government's

initial intervention."       United States v. Gifford, 17 F.3d 462, 469

(1st Cir. 1994); see also United States v. Gamache, 156 F.3d 1, 12

(1st Cir. 1998) ("[T]he concept of predisposition has a definite

temporal reference: 'the inquiry must focus on a defendant's

predisposition     before     contact    with    government   officers    or

agents.'" (quoting United States v. Brown, 43 F.3d 618, 627 (11th

Cir. 1995)); Poehlman, 217 F.3d at 703 ("Quite obviously, by the

time a defendant actually commits the crime, he will have become

disposed to do so.    However, the relevant time frame for assessing

a defendant's disposition comes before he has any contact with

government     agents,      which   is    doubtless    why    it's    called

predisposition.").       While evidence of the defendant's response to

the government's inducement may be relevant to the predisposition

inquiry, that evidence must be evaluated in terms of what it

reveals about the defendant's readiness to commit the crime before

the government contacted him.       See Gifford, 17 F.3d at 469.

             We have advised trial courts that the following factors

may be useful in evaluating the evidence of predisposition or lack

thereof:


                                        - 24 -
          (1) the character or reputation of the
          defendant; (2) whether the initial suggestion
          of criminal activity was made by the
          Government; (3) whether the defendant was
          engaged in the criminal activity for profit;
          (4) whether the defendant showed reluctance to
          commit the offense, which was overcome by the
          governmental persuasion; and (5) the nature of
          the inducement or persuasion offered by the
          Government.

Gamache, 156 F.3d at 9–10.     The second, fourth, and fifth of these

factors are also relevant to the improper inducement analysis.

Thus, while improper inducement and lack of predisposition are two

separate prongs, the same factual evidence will often be relevant

to both prongs.

          3. The Defendant's Burden of Production

          A   defendant   is   entitled   to   a   jury   instruction   on

entrapment if he meets a modest burden of production on the two

prongs of the defense.     United States v. Rodriguez, 858 F.2d 809,

814 (1st Cir. 1988).      This rule is in keeping with the "general

proposition [that] a defendant is entitled to an instruction as to

any recognized defense for which there exists evidence sufficient

for a reasonable jury to find in his favor."          Mathews v. United

States, 485 U.S. 58, 63 (1988).

          In analyzing whether the defendant has met his burden,

the court must construe the evidence in the light most favorable

to the defendant.    Rodriguez, 858 F.2d at 813.           An entrapment

instruction is required if the evidence, viewed in this charitable



                                   - 25 -
fashion, "furnishes an arguable basis for application of the

proposed rule of law."    Id. at 814 (quoting United States v. Coady,

809 F.2d 119, 121 (1st Cir. 1987)).            In other words, the record

must contain evidence that makes the entrapment theory "plausible"

or "superficially reasonable."         Gamache, 156 F.3d at 9.        As we

have previously emphasized, "[t]his is not a very high standard to

meet."   Id.

          A defendant does not need to introduce his own evidence

to meet this burden.     Rodriguez, 858 F.2d at 813.        He may rely on

"evidence adduced during the government's case" or "any probative

material in the record."       Id.    The proof may be "circumstantial

rather than direct."     Id.    If there are factual disputes in the

record, the court is not permitted to "weigh the evidence, make

credibility determinations, or resolve conflicts in the proof."

Gamache, 156 F.3d at 9. If the parties argue competing inferences,

the court must draw all reasonable inferences in favor of the

defendant's entrapment theory.        Id.   Ultimately, if "a reasonable

jury could view the evidence as establishing that defendant was

entrapped . . . [the defendant] [i]s entitled to an entrapment

instruction."     Teleguz,     492   F.3d   at   84.   Determining   whether

government conduct has crossed the line into improper inducement

or whether a person was predisposed to commit an offense are

delicate questions of fact for the jury to sort out.           See Acosta,

67 F.3d at 338.    Thus, a judge should not hesitate to send the


                                      - 26 -
question to the jury if there is even ambiguous evidence of

entrapment.

           Once   the   defendant   meets   his    burden   of    production,

entrapment becomes a question of fact for the jury.              Id.    At that

stage,   the   government   bears   the   burden    of   proving       beyond   a

reasonable doubt either that there was no improper inducement or

that the defendant was predisposed to commit the offense.               Id.     If

"a rational jury could decide either way, its verdict will not be

disturbed."    Id.

                                    IV.

           Consistent with our earlier explanation of the plain

error standard, Pérez is entitled to relief if he is able to

demonstrate that: (1) the district court erred in failing to give

an entrapment instruction; (2) his entitlement to that instruction

was clear or obvious; (3) the omission affected his substantial

rights; and (4) it undermined the fundamental fairness of the

trial.   See Duarte, 246 F.3d at 60.

A.   Error

           The district court denied Pérez's requested entrapment

instruction for failure to meet his burden of production on the

lack of predisposition prong, without addressing whether Pérez had

met his burden of production on the improper inducement prong.

Because the defendant is required to meet the burden of production

on both prongs, a court may deny an entrapment instruction based


                                    - 27 -
on a failure to show evidence on one prong or the other, without

discussing both.    See, e.g., United States v. Rivera-Ruperto, 846

F.3d 417, 431 (1st Cir. 2017); United States v. Sánchez-Berríos,

424 F.3d 65, 77 (1st Cir. 2005).           Because we disagree with the

district court's assessment of the evidence on predisposition, we

must consider both prongs.        If the defendant failed to meet his

burden of production on the improper inducement prong, an error by

the judge in the assessment of the predisposition prong would be

harmless.

            We   also    repeat     that      improper     inducement      and

predisposition     are   analytically        linked   in     that     improper

inducement, and the defendant's responses to it, are part of the

evidence courts should consider in deciding whether the defendant

met his burden of production on the lack of predisposition prong.

Gamache, 156 F.3d at 9–10; see Joost, 92 F.3d at 13-14 ("As for

the absence of predisposition prong, much of what we have pointed

to [in the improper inducement analysis] is relevant.").                    In

evaluating the question of whether the defendant was predisposed,

the factfinder must "abstract from -- . . . assume away -- the

present     circumstances   insofar     as     they      reveal     government

overreaching."     Gendron, 18 F.3d at 962 (emphasis omitted).              If

there was no improper inducement, we already have our answer as to

how the defendant would respond to "an ordinary opportunity to

commit the crime" and any further analysis of predisposition is


                                    - 28 -
unnecessary.    Id. (emphasis omitted).           But if there was improper

inducement, the nature of that inducement and the defendant's

responses to it are relevant to the predisposition analysis to the

extent that they allow inferences about the defendant's state of

mind prior to the government's intervention.            Rodriguez, 858 F.2d

at 816 (considering evidence of the defendant's responses to

improper inducement because "later events often may shed light on

earlier motivations").

           1.   Improper Inducement

           Agent Seig created a Grindr profile appearing to belong

to an adult named "Dave W."               The profile described Dave as

"[m]uscular, [w]hite, [s]ingle."            Pérez sent a message to that

profile, presumably believing he was speaking with that adult man.

Dave quickly turned the conversation towards sexual activity with

a minor by offering to arrange a sexual encounter with his eleven-

year-old "boyfriend."       Dave said that both he and the minor would

be part of the encounter, stating it would be "him you and I" and

describing the encounter as a "threesome."            This type of "bundling

of licit and illicit sex into a package deal" can constitute a

"plus factor" for purposes of establishing improper inducement.

Hinkel,   837   F.3d   at   118;   see    also    Gendron,   18   F.3d   at   961

(describing "the government's taking advantage of an alternative,

non-criminal type of motive" as a "typical[]" example of an

inducement plus factor).


                                         - 29 -
            Agent Seig, writing as Dave, represented from the start

that the eleven-year-old minor was his "boyfriend" -- a term which

suggests    the legally impossible notion that         the minor was a

consenting participant in a sexual and romantic relationship with

Dave.   Agent Seig repeatedly stated that this imagined encounter

would be a positive experience for the minor.             Such repeated

suggestions "downplay[ing] the harm" caused by child sexual abuse,

or otherwise justifying it, can constitute a "plus factor" which

a jury may rely on to find improper inducement.          See Hinkel, 837

F.3d at 118 (stating that the defendant presented evidence of

"clever and sophisticated inducement" where the law enforcement

agent "on numerous occasions, downplayed the harm that could be

expected to flow from the commission of the crime by describing

how 'amazing' the encounter would be, how 'excited' 'Samantha'

was, and how 'Lisa' 'appreciate[d]' how 'honest and caring' Hinkel

had been in his messages"); Gamache, 156 F.3d at 11 (stating that

the   law   enforcement   agent's   repeated   "justifications   for   the

illicit activity (intergenerational sex) by describing 'herself'

as glad that Gamache was 'liberal' like her, expressing that she,

as the mother of the children, strongly approved of the illegal

activity, and explaining that she had engaged in this conduct as

a child and found it beneficial" constituted evidence of improper

inducement); see also Jacobson, 503 U.S. at 540 (describing the

government's     improper     inducement       as   including    repeated


                                     - 30 -
"suggesti[ons] that petitioner ought to be allowed to do what he

had been solicited to do," i.e., purchase child pornography).

            Hence, the record contained evidence that would allow a

jury to find      two significant "plus" factors in Agent Seig's

communications with Pérez: first, Seig's linking the opportunity

for adult sexual activity, a lawful objective of Grindr users,

with the unlawful sexual activity involving a minor -- establishing

a kind of prerequisite for the adult activity; second, Seig's

repeated suggestions that the illegal conduct was not harmful, but

actually beneficial, to the minor.        Thus, a reasonable jury could

have found improper inducement -- a necessary precondition for a

defendant    to     meet   his   burden   of   production   on   lack   of

predisposition.

            2.    Lack of Predisposition

            Pérez met his burden of production on the lack of

predisposition prong if the record would permit a reasonable

inference by the jurors that, before his interaction with Agent

Seig, Pérez was not predisposed to commit the crime of enticing a

minor to commit unlawful sexual activity.        See Gendron, 18 F.3d at

962.   The five factors identified in Gamache guide our analysis.

See 156 F.3d at 9-10.

            As to the first factor, the character or reputation of

the    defendant,    the   evidence    might   include   prior   criminal

convictions for similar offenses or a history of sexual interest


                                      - 31 -
in minors.      Tellingly, the record contains no such evidence.                   See

id. at 12 ("[T]here was no evidence presented that Gamache had

engaged in similar activities independent of this sting operation.

The jury could have relied on this evidence to find a lack of

predisposition . . . ."); see also Hinkel, 837 F.3d at 118 (stating

that the defendant produced sufficient evidence to "clearly" meet

his prima facie burden of a lack of predisposition because, inter

alia, "the government had not uncovered any evidence suggesting

that he had other underage victims").               The absence of any kind of

negative    character       evidence    relating     to    sexual    activity     with

minors     is   one   point     in     favor   of    allowing       the   entrapment

instruction.

             There    are    two     statements     from   Pérez     early   in   the

conversation with Dave that "I started at 8."                   As noted earlier,

the exchange begins as follows:

             Pérez: Hello what are you doing?

             Dave: Hey what's up

             Pérez: Let's see you

             Dave: Cool, do you like really young guys?


             Pérez: Yes
                    Age?
                    I started at 8

             Dave: Me? 35, but my boyfriend is young

             Pérez: Hahhaha Okk
                    How old is he?


                                          - 32 -
                 What does your boyfriend like?

          Dave: He likes everything :)
                He is very young, what age do you like?

          Pérez: The younger the better
                 I don't discriminate
                 I started at 8 hehehhe
                 So you tell me
                 What does he like to do?
                 We are close, we can come up with some fun
                 From there up I do it all

          Dave: Do you understand English? I speak only a little
                Spanish
                My boyfriend is 11 years old. Do you want to play
                with him?

          Pérez: Mmmm yessss
                 Where is he?
                 I speak little only a little English?
                 Share pics??
                 You tell me when and where???
                 Do you prefer to call?
                 Yes, I want to play


          The dissent states that, "in context," the exchange

plainly reflects a "stark pre-dispositional admission by Pérez."

In fact, however, the dissent ignores the context of Pérez's

statements that "I started at 8."   Both statements are made before

the notion of sex with a minor entered the conversation ("My

boyfriend is 11 years old.   Do you want to play with him?").    Until

Dave   talks   about   his    eleven-year-old     "boyfriend,"    the

conversation, which took place on a dating app for adults, can be

read as discussing sex with young adults.       When Dave refers to

himself as thirty-five, he could be saying that he is thirty-five



                                 - 33 -
years old, or that he started having his sexual experiences at age

thirty-five.     Clearly, he (i.e., Agent Seig, posing as Dave) is

not saying that his partners in his sexual experiences are thirty-

five.     It thus remains unclear, when Pérez reiterates that he

"started at 8," whether he is referring to the beginning of his

own sexual experiences or the age of boys with whom he has had

sex.

            The dissent similarly ignores the context when Pérez

says, "the younger the better."          Here, too, he makes the statement

before Dave made any reference to his "boyfriend" being underage.

Thus, it is hardly clear that Pérez is admitting to having an

interest in children rather than meaning that he is interested in

younger    adults.      The    latter      interpretation    is    plausible,

particularly in light of Dave's reference to "really young guys,"

(the word "guys" tending to imply adults), and the fact that Pérez

made the comments on an adults-only dating app.              As for Pérez's

apparent eagerness when he discovers that Dave's "boyfriend" is

only eleven, we have said in our case law that " eagerness alone

. . . is not sufficient to remove the predisposition question from

the jury's purview."     Gamache, 156 F.3d at 12.

            Hence, the text is ambiguous enough that a jury, not a

judge, needed to determine its meaning.               See id. at 9 ("[T]he

court's function is to examine the evidence on the record and to

draw    those   inferences    as   can   reasonably   be   drawn   therefrom,


                                         - 34 -
determining whether the proof, taken in the light most favorable

to the defense can plausibly support the theory of the defense.").

Thus,       for   the   purpose   of     evaluating   the   evidence   on   the

predisposition prong, the "I started at 8" statements do not

provide evidence of a history of sexual interest in minors.

              On the second factor, the initial suggestion of criminal

activity, it is indisputable that the government first suggested

the sexual abuse of a minor.              In fact, as we have noted, Pérez

encountered law enforcement on a forum intended to be used only by

adults.9      The jury could reasonably draw the inference from Pérez's

use of Grindr that, before his conversation with "Dave," he was

interested in sex with other adult men, not children.             Indeed, the

expert psychologist who testified at sentencing drew this same

inference, stating: "A pedophile will not be using, my personal

clinical opinion, I don't think they will use Grindr because he

will be easily identified."            Although Agent Seig testified that he

designed his profile to contain "veiled" references which would be

understood as suggesting sexual abuse of a minor "by someone who

was versed in communicating in the realm of pedophiles," we must

interpret the evidence in the manner most charitable to Pérez.




      Agent Seig testified that profiles explicitly seeking sexual
        9

encounters with minors "would be removed from the social network,
because many people would report that and then the owners of the
network would remove it."


                                          - 35 -
Here, there is no basis for concluding on this record that Pérez

understood these veiled references.

             The third factor -- whether the defendant engaged in the

criminal activity for profit -- is not relevant here, but we note

that monetary profit was not at issue.

             As for the fourth factor, "whether the defendant showed

reluctance to commit the offense," the transcripts show that Pérez

insisted on meeting Dave without the minor's presence.      Taken in

the light most favorable to Pérez, as it must be at this stage,

this insistence can be read as a sign of some reluctance to commit

the crime.     Pérez made clear that any subsequent meeting with the

minor would depend on how the meeting with Dave went, and it is a

reasonable inference from the messages that Pérez had not made up

his mind about actually meeting the child.        A jury could also

conclude from Pérez's insistence on meeting with Dave alone, his

repeated statements that he wanted to get to know Dave first, and

his clear interest in Dave, that Pérez was hesitant about moving

beyond the realm of fantasy with a minor and was motivated by a

desire to "be horny" with an adult in whom he was sexually

interested.      Although a jury could also conclude that Pérez

intended to proceed directly to a meeting with the minor after

seeing Dave and ensuring he was not a law enforcement officer,

that plausible inference is not sufficient to take the entrapment

defense from the jury.      See Gamache, 156 F.3d at 10 (explaining


                                   - 36 -
that whether the government disputes the defendant's version of

the facts is "irrelevant to the question of whether it raises an

issue of entrapment to be put before the jury"); Rodriguez, 858

F.2d   at   815    (explaining   that    it    is   sufficient      that   "[the

defendant's] version, whether or not it strikes us as particularly

credible,    is    neither   thoroughly       implausible    nor    constructed

entirely of gauzy generalities").

            The fifth factor, "the nature of the inducement or

persuasion offered by the Government," brings us back to the

improper inducement analysis.           From the very beginning of the

conversation, Pérez expressed his interest in "Dave," an adult

man.   Before either party said anything about a minor, Pérez said

to Dave, "Let's see you," likely meaning that he wanted to see a

picture of "Dave."        Later in the conversation, Pérez asked Dave

for pictures again and for a physical description of his body.                 A

juror could reasonably infer that Pérez was primarily motivated by

sexual interest in "Dave," not the minor.             Pérez also asked Dave

questions about how he "got" his "boyfriend."               Drawing inferences

in favor of Pérez, these questions suggest that he asked them

because he had not ever thought about or tried to entice a minor

into sex before, and would not do so without the encouragement of

the government agent and repeated statements "downplaying the

harm,"   Hinkel,    837   F.3d   at   118,    or,   even    more   offensively,

normalizing the sexual behavior with the minor.


                                        - 37 -
          To be sure, there are different inferences one could

draw from the communications between Pérez and Dave.        But, in

determining whether the defendant has met his burden of production,

we are required to draw all inferences in favor of the defendant.

The evidence relevant to the factors listed in Gamache provides at

least some evidence of lack of predisposition.    Thus, the record

met Pérez's modest burden of production, and the district court

erred by denying the entrapment instruction.

B.   Clear or Obvious Error

          1.   Relevant First Circuit Precedent

          Prior to Pérez's trial in May 2017, our court had decided

two significant cases addressing the circumstances in which a

defendant is entitled to jury instructions on the entrapment

defense in the context of child sexual abuse sting operations:

Hinkel, 837 F.3d at 111, and Gamache, 156 F.3d at 1.   Because these

cases reveal the clarity of the district court's error, we describe

their facts in some detail.

          a.   Hinkel

          Hinkel was convicted of attempted enticement of a minor

in violation of § 2422(b) -- the precise offense at issue here --

after email correspondence with a law enforcement agent posing as

"Lisa," the thirty-eight-year-old mother of a fictitious fifteen-

year-old girl, "Samantha."    Hinkel, 837 F.3d at 116.       Hinkel

contacted "Lisa" based on a personal ad posted to an "online


                                - 38 -
message      board    .    .   .    frequented        by     those   seeking     adult    sex

partners."      Id. at 115.             The ad stated, "mom with daughter looking

for taboo relationship."                  Id. at 116.        Hinkel responded with an

email containing "graphic descriptions of sexual acts that he

imagined engaging in with 'Lisa' and her daughter."                               Id.     The

government agent posing as "Lisa" promptly told Hinkel that her

daughter was "15 but experienced," to which Hinkel responded,

"Sounds very naughty!              I am concerned about her age since legally

she should be 16 or older."                 Id.      The agent answered "she[']s not

[16 or older] so i guess this conversation is over."                            Id.    Hinkel

immediately replied, "Nope..... It is not over! I want to talk

more!   I'm    very       intrigued        by   it    all.    Such   taboo   and      naughty

play!!!!"      Id.

              For the next month, Hinkel continued to correspond with

Lisa    in    "lurid      detail"         about    his     desire    to   have    sex    with

"Samantha,"      though            he     occasionally        expressed      "conflicting

feelings." Id. at 116-17. Lisa reassured Hinkel, writing "i think

you will love her...and i appreciate the way you describe our

situation."      Id. at 117.              Hinkel also exchanged sexually graphic

emails with Samantha directly.                    Id.      Hinkel and Lisa made plans

for Hinkel to visit and have sex with Samantha.                           Id.    Lisa told

him that the planned encounter would be "such an amazing experience

for us to have together." Id. When Hinkel arrived at the appointed

time and place, he was arrested and subsequently charged and


                                                  - 39 -
convicted of a § 2422(b) offense. Id. At his trial, the government

introduced evidence of "five cartoons, which consist of detailed

anime drawings of adults and minors engaged in sex acts" that law

enforcement had found on Hinkel's computer.    Id. at 122.

          Hinkel's primary defense at his trial was entrapment,

and -- unlike here -- the district court instructed the jury on

the elements of that defense.   Id.    On appeal, Hinkel claimed the

government's evidence was insufficient to overcome the entrapment

defense. Id. We rejected that challenge because it was reasonable

for the jury to find that entrapment had not occurred.       Id. at

120.   Of importance here, however, is our explicit consideration

of whether Hinkel had satisfied his burden of production even

though the district court had instructed the jury on entrapment.

Id. at 118.    Hence, although the posture of Hinkel was different,

its discussion of the facts that clearly met the threshold for an

entrapment instruction is directly applicable here.

          b.   Gamache

          Following a postal service correspondence with a law

enforcement agent posing as a mother of three young children,

Gamache was convicted of travel with intent to engage in illicit

sexual conduct with a minor in violation of 18 U.S.C. § 2423(b),

and an attempt to use a minor to produce sexually explicit images

in violation of 18 U.S.C. § 2251(a).    Gamache, 156 F.3d at 2.   The

agent had published a personal ad in an adult magazine which read,


                                 - 40 -
in part, "female, 31; Single mom, two girls, one boy, seeks male

as partner and mentor, seeks fun, enjoys travel and photography."

Id. at 3.     Gamache responded with interest in the adult female

author of the advertisement.    Id.

            The   agent,   posing     as     "Frances,"     steered   the

correspondence toward sex with her three minor children, ages

twelve, ten, and eight.    Id. at 4.       Frances wrote that she wanted

to "introduc[e] an adult male to further [her] children's sexual

education and experiences."    Id.     Gamache responded that he was

"not shocked" and that he would be "honored" to be chosen as the

adult man to have sex with Frances's children.        Id.    Over several

months of continuing correspondence, Frances described sexual

activities she wanted Gamache to engage in with her children, and

Gamache replied in kind, sharing his own ideas and desires.           Id.

at 4-7.   He also sent a letter to the children describing sexual

activities he planned to engage in with them. Id. at 7. Throughout

the correspondence, Frances referenced a "kind" uncle who "taught

[her] about sex when [she] was very young, and wanting the same

type of experience for [her] children."         Id. at 4-5 (alterations

in original).     She told Gamache the children were "very excited

about meeting" him, and they arranged for Gamache to meet "Frances"

and her children at a motel.   Id. at 5-7.       When Gamache arrived at

the motel, he was arrested.    Id. at 7.




                                    - 41 -
          Gamache   requested   an     entrapment     instruction   at   his

trial, and the court rejected his request. Id. at 3. His objection

was properly preserved and subject to plenary review.            Id. at 9.

We held that Gamache had met his burden of production on both

prongs of the entrapment defense and that the court erred in

failing to give the instruction.          Id. at 12.      We vacated the

conviction and remanded for a new trial.

          c. Common Principles in Hinkel and Gamache

          Our review of Hinkel and Gamache reveals that, at the

time the district court rejected Pérez's request for an entrapment

instruction,   we   had   previously    held   that    certain   facts    in

combination -- present in both of those cases -- entitled a

defendant to an entrapment instruction.

          In both cases, the government originated the criminal

design and invited the defendants to participate by placing an

ambiguous advertisement in an adults-only forum; then, when the

defendants responded to the advertisements, the government offered

to arrange a sexual encounter involving a minor.         Hinkel, 837 F.3d

at 116; Gamache, 156 F.3d at 10.       In both cases, we noted that the

government agents used the tactic of "bundling . . . licit and

illicit sex into a package deal," meaning that they offered a

sexual encounter that would include both legal sex with an adult

and illegal sex with a minor.     Hinkel, 837 F.3d at 118; see also

Gamache, 156 F.3d at 10.    A key component of the government agent's


                                     - 42 -
strategy in both cases was "downplay[ing] the harm" that would

flow from the crime through repeated statements portraying sex

with a minor as normal or even beneficial.             Hinkel, 837 F.3d at

116; see Gamache, 156 F.3d at 10-11.        In both cases, the defendants

manifested some hesitancy to commit the offense, though most of

their   communications     expressed       eagerness    to   do   so,      and,

ultimately, both defendants showed up for a meeting with the minor.

Finally, in both cases, there was no evidence of the defendants'

prior sexual activity with minors.             Hinkel, 837 F.3d at 116;

Gamache, 156 F.3d at 10.

             Not surprisingly, given these similarities, we cited

Gamache as apt precedent in stating that the defendant met his

burden of production in Hinkel.         The cases, of course, are not

identical.       Gamache   involved    a    more   prolonged      period     of

correspondence and, arguably, more severe government manipulation.

Despite those differences, however, when all inferences are drawn

in favor of the defendant, the record in each case told, in

essence, the same story: a defendant without any known prior sexual

contact with minors moved from his initial, lawful inquiry about

adult sex to what a jury could find was an attempt to commit an

offense involving sexual exploitation of a minor, prompted by

encouragement from the government that a reasonable juror could

deem improper inducement.




                                      - 43 -
             2.   Comparing Pérez's Case with Hinkel and Gamache

             a. Initiation by the Government Agent

             Like the law enforcement agents in Hinkel and Gamache,

Agent Seig purported to be an adult using a forum for adults

seeking adult sexual partners, and alluded to the possibility of

a relationship with a younger person without specifying the nature

of the relationship or the age of the young person.      See Hinkel,

837 F.3d at 116; Gamache, 156 F.3d at 10.     Pérez took the bait and

contacted the agent.     Like Hinkel and Gamache, his initial message

did not include any reference to sex with a minor.         He wrote,

"Hello what are you doing?" and then "Let's see you."      It was the

government agent who turned the conversation to sex with minors,

asking if Pérez "liked really young guys," and then, when he

responded affirmatively, making the offer of sex with a minor: "My

boyfriend is 11 years old.      Do you want to play with him?"     When

Pérez again responded affirmatively, Agent Seig made that offer

more explicit, asking what sex act Pérez wanted to engage in with

the minor.    While Pérez expressed enthusiastic interest, "[i]t was

the Government that first mentioned the 'child[]' as [a] sex

object[]; it was the Government that first used sexually explicit

language involving the 'child[]'; [and] it was the Government that

escalated the subject of sex with [the] child[]."       Gamache, 156

F.3d at 10.




                                   - 44 -
          b. Government's Bundling of Licit and Illicit Sex

          Agent Seig's sting operation relied on precisely the

same tactic we described in Hinkel and Gamache: the "bundling of

licit and illicit sex into a package deal." Hinkel, 837 F.3d at

118; see also Gamache 156 F.3d at 10.      Pérez reached out to Dave

-- described as a "[m]uscular, [w]hite, [s]ingle" adult man -- on

an adult dating application.     He clearly remained interested in

the adult throughout the conversation, including asking for photos

just of Dave when Dave would not send photos of the minor.        These

circumstances permit a plausible inference that Pérez was not

predisposed to sexually abuse a child, but, rather, was motivated

by interest in sex with Dave.   See Gamache, 156 F.3d at 10 (noting

a plausible argument that "all of [Gamache's] correspondence about

sex with minors was a ruse to have sex with 'Frances,' who was his

target from the time that he answered the ad").

          c.   Government   Agent's   Statements   Normalizing   Sexual

     Abuse

          Dave's comments repeatedly portraying sex with a minor

as normal or even beneficial resemble those made by the agents in

Hinkel and Gamache.   See Hinkel, 837 F.3d at 118 (stating that the

agent "downplayed the harm that could be expected to flow from the

commission of the crime by describing how 'amazing' the encounter

would be"); Gamache, 156 F.3d at 11 ("[T]he government agent

provided justifications for the illicit activity         [by]    . . .


                                  - 45 -
expressing that she, as the mother of the children, strongly

approved of the illegal activity, and explaining that she had

engaged in this conduct as a child and found it beneficial to

her."). The government's perverse statements that the minors would

enjoy and benefit from sexual exploitation were important because

such suggestions have the potential to influence the mind of a

person who is not predisposed to abuse children and convince him

that sex with a minor is acceptable. See Gamache, 156 F.3d at 11

("These solicitations suggested that Gamache ought to be allowed

to engage in the illicit activity . . . .").

          d. Defendant's Reluctance to Commit the Offense

          As in Hinkel and Gamache, some of Pérez's actions could

be interpreted as reluctance to commit the offense.   He repeatedly

insisted on meeting with Dave alone, without the minor's presence.

That demand could be interpreted as an indication that he was

reluctant to go through with meeting the minor, despite his many

statements of enthusiasm about doing so.

          To be sure, Pérez's plausible expression of reluctance

differed from the more explicit statements in Hinkel and Gamache.

Still, there was no outright rejection of the criminal conduct in

either of those cases.   Hinkel briefly indicated hesitation when

"Lisa" told him that her daughter was fifteen, but clearly overcame

his reluctance just moments later, stating in response to an

obvious exit opportunity, "Nope..... It is not over! I want to


                                - 46 -
talk more! I'm very intrigued by it all.      Such taboo and naughty

play!!!!"10    See Hinkel, 837 F.3d at 116.   Hinkel subsequently did

arrange and show up at a meeting with the fictitious fifteen-year-

old. Id. at 117.     Gamache initially resisted Frances's suggestion

that he bring a video camera, but he stated his hesitance was based

on technological ignorance, not any moral opposition to creating

child pornography.     See Gamache, 156 F.3d at 12.      In the end,

Gamache did show up for a meeting with the children and brought a

video camera with him.

             e. Defendant's Eagerness to Commit the Offense

             Aside from his insistence on meeting Dave separately

prior to meeting the minor, Pérez's responses to Dave's suggestions

of sexual activity with an eleven-year-old boy were decidedly not

reluctant.    His immediate response to Dave's offer of sex with his

"boyfriend" was "yes," and he made explicit statements about the

sex acts he wanted to engage in with the boy.11    Gamache and Hinkel


     10In an apparent attempt to suggest that Hinkel was reluctant
to engage in sex with a minor in a way that Pérez was not, the
dissent ignores this quick abandonment of any hesitation in its
characterization of Hinkel's response to the prospect of sex with
a minor.

     11The dissent focuses on this immediate affirmative response,
suggesting that Pérez's enthusiasm made the necessity of an
entrapment instruction in this case unclear, and, thus, its
omission was not plain error. But our precedent has been clear on
this point: "[E]agerness alone . . . is not sufficient to remove
the predisposition question from the jury's purview."     Gamache,
156 F.3d at 12. Similarly, the dissent emphasizes that Pérez went



                                  - 47 -
expressed similar reactions to law enforcement agents' criminal

suggestions.        See    Hinkel,      837    F.3d     at   118    (describing          the

defendant's    response        as    "eager[]");      Gamache,      156    F.3d     at   11

(describing the defendant's response as "enthusiastic").                              Both

Hinkel and Gamache gave graphic descriptions of the sex acts they

wanted to engage in with minors.                 See Hinkel, 837 F.3d at 116

(stating that "Hinkel corresponded frequently and in lurid detail

with 'Lisa' and her fictitious daughter 'Samantha'" and that he

"describ[ed] his own sexual desires in detail"); Gamache, 156 F.3d

at   6   (describing       a    letter    from        Gamache      to     Frances     that

"explain[ed], at length and in detail, how he will carry about the

sexual 'education' of 'Frances'' 'children'").

            Our holdings in Hinkel and Gamache make clear that a

defendant     can   meet       his    burden     of     production        on   lack      of

predisposition even if he responded eagerly or enthusiastically to

the proposed criminal conduct.                As we have noted, in Gamache we

explained, "[W]hile 'ready commission of the criminal act can



to meet with Dave just five days after the first message. This
time frame may be another display of eagerness, certainly worthy
of the jury's consideration, but it did not warrant withholding
the entrapment instruction from the jury when other evidence in
the record supported a finding of a lack of predisposition. The
dissent also overlooks the fact that Pérez was arrested, not at a
planned meeting with the minor, but rather, at a meeting with Dave.
Read in the light most favorable to Pérez, he was prepared to meet
with the adult intermediary alone, but had not clearly agreed to
meet with the minor. By contrast, Hinkel and Gamache were arrested
at planned meetings with minors.     See Hinkel, 837 F.3d at 116;
Gamache, 156 F.3d at 7.


                                          - 48 -
itself adequately evince an individual's predisposition' and thus

provide sufficient evidence to support a jury's finding that the

defendant was predisposed to commit the offense, eagerness alone,

when coupled with the 'extra elements' present in this sting

operation, is not sufficient to remove the predisposition question

from the jury's purview."          156 F.3d at 12 (citation omitted)

(quoting   Gifford,    17   F.3d   at    469);   see   also    id.    at   11-12

("[W]illingness to commit the crime, although clearly relevant to

the jury's inquiry, is not sufficient by itself to mandate a

finding that he was predisposed."); Rodriguez, 858 F.2d at 816

("Although a jury might well find that Rodriguez's wiliness, and

the level of experience and enthusiasm which he subsequently

exhibited,     were   inconsistent       with    the   claim     of    initial

unreadiness, such a finding would not be inevitable.").

             f. Prior Sexual Interest in Children

             As Pérez notes, the trial record contained "absolutely

no evidence that, aside from this virtual conversation, Mr. Pérez

had engaged, tried to engage, or would have considered engaging in

sex with a minor."12    In Gamache, we emphasized the importance of

the absence of evidence of prior similar conduct in meeting the

defendant's burden of production on lack of predisposition. See


     12 As noted    above in Section IV.A.2., the meaning of Pérez's
statements that    "I started at 8" is ambiguous. If all inferences
are drawn in his   favor, those statements do not constitute evidence
of prior sexual    interest in children.


                                        - 49 -
Gamache, 156 F.3d at 12 ("[T]here was no evidence presented that

Gamache had engaged in similar activities independent of this sting

operation.    The jury could have relied on this evidence to find a

lack of predisposition . . . .").

             Of course, to address the burden of production on the

predisposition issue, a defendant could introduce some evidence of

positive relationships with children, though Gamache makes clear

that the defendant need not introduce such evidence to meet that

burden.   See id.     Indeed, Hinkel offered evidence that he "had

raised two adult children and had not been accused of having an

inappropriate relationship with either of them."       Hinkel, 837 F.3d

at 118.      However, in Hinkel, there was contrary evidence that

Hinkel had sexual interest in children before the contact with the

government, in the form of cartoon images of adult sexual conduct

with children recovered from his computer.        Id. at 122.      Hinkel

challenged the admission of that evidence on appeal.              Id.   In

rejecting that claim, we recognized that the images were "probative

of   Hinkel's    predisposition"   and   may   tend   to   show   "sexual

inclination towards children."       Id. (quoting United States v.

Chambers, 642 F.3d 588, 595–96 (7th Cir. 2011)).       Still, even with

the record containing evidence of Hinkel's sexual inclination

towards children, we agreed with the district court that Hinkel

had provided enough evidence of lack of predisposition to mount a




                                   - 50 -
"credible entrapment case." Id. at 118.                 Again, there was no such

evidence of Pérez's prior sexual interest in children.

            3.      Conclusion

            As we have described, this case is strikingly similar to

Hinkel and Gamache.          Agent Seig used the same tactics we saw in

those cases -- placing an ambiguous lure on an adults-only forum,

inviting the defendant who responded to the lure to engage in a

"bundled"    sexual     encounter    with     an    adult     and    a    child,    and

repeatedly insisting that this sexual abuse was beneficial to the

child.      Pérez    responded     similarly       to   Hinkel      and   Gamache   --

enthusiastic     interest        coupled     with       a   weak     expression     of

reluctance.      And as in Gamache, the record at Pérez's trial

contained no evidence of any sexual interest in children prior to

the government's intervention.

            In Hinkel, we stated that the facts "clearly" met the

defendant's "'modest' burden of making a prima facie showing that

there is some evidence both elements [of the entrapment defense]

are satisfied."        Hinkel, 837 F.3d at 117; see also id. at 118

(stating that the evidence at Hinkel's trial supported "a credible

entrapment case").       In Gamache, we concluded that "appellant met

the dual burdens required for an instruction on entrapment, because

the   evidence      raises   a   reasonable     doubt       that    the   Government

improperly induced a citizen to commit crimes that he was not

predisposed to commit, yet crimes for which he was charged and


                                           - 51 -
convicted."   Gamache, 156 F.3d at 12.    The district court ignored

our precedents when it decided a trial record containing strikingly

similar core facts did not warrant an entrapment instruction

because the defendant did not meet his burden of production on the

predisposition prong of the defense.

          Tellingly, the government's brief on appeal does not

even mention Hinkel or Gamache, much less attempt to distinguish

those cases from the circumstances present here.    The government's

primary argument is that Pérez cannot meet his burden on lack of

predisposition because he "jumped at the opportunity to 'play'

with the 11-year-old boyfriend."         That position is obviously

foreclosed by our case law, and, if it influenced the district

court's decision to deny the entrapment instruction, it should not

have.

          The dissent claims that comparing this case to Hinkel

and Gamache is like "saying apples and oranges are 'clearly and

obviously' the same because they both grow on trees in orchards."

To be sure, there are distinctions among the three cases, but all

three involve a mix of evidence -- some favorable to the entrapment

defense, some tending to disprove entrapment.     Each case involved

statements reflecting eagerness and others reflecting reluctance.

Although those statements appeared in conversations which played

out across different time frames featuring different modes of

communication, and the specific facts of the cases do not perfectly


                                - 52 -
align, there is the significant overlap in the categories of facts

that we have described.   The district court's failure to see that

overlap between this case on the one hand, and Hinkel and Gamache

on the other -- cases in which we stated the predisposition issue

needed to go to the jury -- was a clear error.    Although there are

many varieties of apples, they are apples all the same.

C.   Substantial Rights

          Next, we ask whether the clear or obvious error affected

the defendant's substantial rights.       By refusing to give an

entrapment instruction, the court denied Pérez an opportunity to

have the jury consider his primary defense.     See United States v.

Benavidez, 558 F.2d 308, 309 (5th Cir. 1977).    As we have discussed

at length, Pérez's entrapment defense, reviewed in the light most

favorable to him, as required by law, was plausible.     There was a

reasonable probability that a rational jury could credit the

defense, even in the face of the government's attempt to disprove

the entrapment defense beyond a reasonable doubt.         See United

States v. Benjamin, 252 F.3d 1, 9 (1st Cir. 2001) (stating that to

determine whether an error affected the defendant's substantial

rights, the court "must determine 'whether the record contains

evidence that could rationally lead to a contrary finding with

respect to the omitted [jury instruction]'" (quoting Neder v.

United States, 527 U.S. 1, 19 (1999))).   Thus, Pérez's substantial

rights were affected.


                                - 53 -
D.   Fundamental Fairness

            Finally,   we    ask   whether     this   error   is   one   that

"impugn[ed] the fairness, integrity, or public reputation of the

criminal proceeding as a whole."         United States v. Padilla, 415

F.3d 211, 221 (1st Cir. 2005). Our analysis under this final prong

of plain error review is "flexible . . . and depends significantly

on the nature of the error, its context, and the facts of the

case."     United States v. Gandia-Maysonet, 227 F.3d 1, 6 (1st Cir.

2000).

            Entrapment is a judicially created defense reflecting a

recognition that "[m]anifestly, [the law enforcement] function

does not include the manufacturing of crime."            Sherman, 356 U.S.

at 369 (citing Sorrells v. United States, 287 U.S. 435, 443

(1932)).      Given the importance of the defense,            erroneous or

confusing jury instructions regarding entrapment compromise the

fairness of a trial.        E.g., United States v. Kopstein, 759 F.3d

168, 182 (2d Cir. 2014) (holding that misleading jury instructions

regarding    entrapment,    the    defendant's   "only   viable    defense,"

created so much confusion as to "call into question the fairness

and integrity of [the defendant's] conviction" (quoting United

States v. Rossomando, 144 F.3d 197, 201 (2d Cir. 1998))); United

States v. Burt, 143 F.3d 1215, 1219 (9th Cir. 1998); United States

v. Duran, 133 F.3d 1324, 1335 (10th Cir. 1998); Here, we did not

have an instruction that was problematic because it was confusing.


                                      - 54 -
Rather, we had a complete failure to instruct the jury on the

defendant's primary defense.       See Benavidez, 558 F.2d at 310.

Because   of   the   court's   refusal   to   give    Pérez's   requested

instruction, "the jury was not in a position to fairly evaluate

the defendant's case," see id., as it did not know that the

government was required to prove beyond a reasonable doubt that

either no improper inducement took place, or that Pérez was

predisposed to commit the offense.       It is fundamentally unfair to

allow a jury to convict without instructing it on the law relevant

to a plausible entrapment theory that was "fairly raised" at trial.

Id.

          This is not the common plain error case where the failure

of a defendant to properly preserve an objection for de novo review

means that the trial court never had an opportunity to rule on the

matter at issue.     Pérez requested an entrapment instruction before

trial and renewed his request at a charging conference shortly

before the jury instructions were delivered.         Although these steps

did not preserve Pérez's challenge under our circuit's law --

because he did not renew his objection after the court charged the

jury -- the fact remains that the court was fully advised that

Pérez sought the instruction, and objected to its denial, because

he intended to rely, and did in fact rely, on entrapment as a




                                   - 55 -
defense.13 Yet, the court denied the request in a single conclusory

sentence, providing no explanation for its determination that

Pérez had not met his burden of production on the predisposition

prong of the defense.14

             Pérez is now serving a sentence of 151 months' (twelve

and a half years') imprisonment based on the outcome of a trial at

which the court summarily and improperly excluded his primary

defense.     Under these circumstances, the trial court's clear or

obvious error in refusing to present Pérez's entrapment defense to

the   jury   affected   his   substantial   rights   and   undermined   the

fundamental fairness of his trial.       To correct that error, we must

remand for a new trial.

                                    V.

             Given that we are remanding for a new trial, we choose

to comment on one aspect of any new trial: the voir dire process.




       As noted above, Pérez also failed to object on the record
      13

when the judge invited objections immediately before instructing
the jury.   Despite this omission, the trial record makes clear
that the district court was aware of Pérez's objection.

       To the extent that it might be relevant to the fourth prong
      14

analysis, we note that the retrial in this case will not require
a victim to endure a second trial. Obviously, there was no actual
victim of child sexual abuse in this attempt case.      Cf. United
States v. Colon-Nales, 464 F.3d 21, 29 (1st Cir. 2006) ("Given the
unchallenged nature of the evidence in this case . . . the greater
threat to the 'fairness, integrity and public reputation of
judicial proceedings' would be to send this back for trial . . .
thereby requiring the carjacking and rape victim to testify
twice.")


                                     - 56 -
See, e.g., United States v. Gonzalez-Maldonado, 115 F.3d 9, 13

(1st Cir. 1997) ("In order to give as much guidance as possible to

the district court, we also discuss some of the other claims that

are likely to resurface if there is a new trial.").     Pérez insists

that there was error in the district court's handling of the voir

dire.   We do not go that far.     But the briefing has convinced us

that the court would be well-advised to explore the issue of anti-

gay bias more thoroughly than it did in the voir dire process

reflected in the record.

           The court devoted only one question to the topic of anti-

gay bias, asking the panel: "Do you feel that you would not be

able to render a fair and impartial verdict based on the evidence

and my instructions if the defendant were homosexual or gay?"       On

remand, the court should carefully consider Pérez's argument that

this single self-assessment question "was inadequate to permit

discovery of stereotypical and pejorative notions rooted in an

extremely relevant bias."        As Pérez notes, this case raises

particular concerns about anti-gay bias not only because the

defendant is gay, but because of the graphic sexual nature of the

evidence   and   the   repugnant     but    unfortunately   widespread

prejudicial belief that gay men are likely to sexually abuse




                                   - 57 -
children.15     Questions probing prospective jurors' actual bias

against gay men -- rather than their self-assessment of their

ability to be impartial at a criminal trial where the defendant is

gay -- would be more useful in identifying jurors who could not be

fair and impartial in dealing with the difficult facts of this

case.

             Vacated and remanded.

                    - Concurring Opinion Follows -




       See Perry v. Schwarzenegger, 704 F. Supp. 2d 921, 983 (N.D.
        15

Cal. 2010) ("[S]tereotypes imagine gay men and lesbians as . . .
child molesters who recruit young children into homosexuality. No
evidence supports these stereotypes."), aff'd sub nom. Perry v.
Brown, 671 F.3d 1052 (9th Cir. 2012); Luke A. Boso, Dignity,
Inequality, and Stereotypes, 92 Wash. L. Rev. 1119, 1142-43 (2017)
(discussing manifestations of the false stereotype that gay men
are likely to be pedophiles).


                                     - 58 -
            LIPEZ, Circuit Judge, concurring.      I write separately to

urge our court in a future en banc proceeding to abandon the rigid

and outdated interpretation of Rule 30(d) of the Federal Rules of

Criminal Procedure that we had to apply in this case.          We are the

only circuit that -- without regard for the specificity or timing

of a party's initial objection to jury instructions -- deems that

objection forfeited if it is not repeated after the court instructs

the jury.    See United States v. Roberson, 459 F.3d 39, 45 (1st

Cir. 2006). That preservation requirement serves no useful purpose

in   the   administration    of   justice,   and   it   is   premised   on

practicalities that no longer exist.

            To be clear, I do not raise this issue because of any

reservations about the strength of the majority's plain error

analysis in this case.      Rather, I am concerned about the impact of

our existing rule on criminal defendants who cannot meet that

exacting standard in other instances where it is inappropriately

applied.    Pérez's case provides a helpful illustration of why the

rule requiring a pointless post-charge objection is misguided.

            Before his trial commenced, Pérez filed an ex parte

request for an entrapment jury instruction.             At the close of

evidence in the two-day trial, the parties participated in an

unrecorded charging conference.        Even without a record of the

conference, it is clear from the district court's docket entry

that Pérez renewed his request for an entrapment jury instruction.


                                    - 59 -
The district court denied the instruction, stating: "The ruling is

based on the arguments presented by the government and defendant's

response    during   the   charging    conference   in    connection     with

predisposition."16    Following the conference, the attorneys gave

their closing arguments and the court then proceeded to charge the

jury. It did not invite objections from the parties, and Pérez did

not raise an objection.

            Under our court's interpretation of Rule 30(d), Pérez

forfeited   his   claim    that   he   was   entitled    to   an   entrapment

instruction, subjecting that claim to plain-error review.                 See

Fed. R. Crim. P. 52(b).     In other words, our law faulted Pérez for

failing to reiterate an objection that had just been rejected at

the charging conference.      See United States v. Meadows, 571 F.3d

131, 146 (1st Cir. 2009) ("Objections registered during pre-charge

hearings    are   insufficient    to   preserve   the    issue."     (quoting

Roberson, 459 F.3d at 45)).

              Rule 30(d) does not require that interpretation.             It

states: "A party who objects to any portion of the instructions or

to a failure to give a requested instruction must inform the court


     16 Before instructing the jury, the court asked the parties
if there were objections to the instructions. Pérez did not object
at that time, but that lack of objection would not matter because
our precedent requires the objection to be made after the jury is
instructed.   See Roberson, 459 F.3d at 45.     Even if Pérez had
objected when invited to do so by the judge, his claim would still
be considered forfeited and subject to plain error review on
appeal. Id.


                                       - 60 -
of the specific objection and the grounds for objection before the

jury retires to deliberate." By its terms, then, the rule requires

only   that    the   party's   objection   be   specific,   explained,   and

presented before the jury deliberates.             Pérez satisfied each of

those requirements.

              Our rule insisting on a post-charge objection under Rule

30(d) has its origins in a decades-old, out-of-circuit precedent

-- authored by one of our First Circuit colleagues sitting by

designation -- that involved the similar requirement in civil cases

to timely raise instructional challenges.           See Fed. R. Civ. P. 51.

In that 1966 case, Judge Aldrich observed that "[t]he duty imposed

upon counsel of 'stating distinctly the matter to which he objects

and the grounds of his objection' cannot normally be performed

until the charge has been heard in its entirety."              Dunn v. St.

Louis-San Francisco Ry. Co., 370 F.2d 681, 684 (10th Cir. 1966)

(Aldrich,      J.    sitting   by   designation)    (quoting   then-current

language of Fed. R. Civ. P. 51).        Based on that view -- i.e., that

specificity will likely be infeasible before counsel hears the

instructions as given -- the panel in Dunn concluded that an

instructional objection ordinarily will be deemed preserved only

if it is voiced after the court charges the jury. See id.                 We

subsequently adopted that post-charge preservation rule in our

circuit, including for criminal cases governed by Rule 30(d).            See

United States v. Leach, 427 F.2d 1107, 1113 (1st Cir. 1970) (citing


                                       - 61 -
Dunn     as   precedent   for     concluding    that   a   claim       for   a   jury

instruction was forfeited where counsel requested the instruction

but did not renew his objection after the instructions were

delivered).       While Dunn allowed for limited exceptions to the

requirement that objections be made after the jury charge, see 370

F.2d at 684, the First Circuit requires a post-charge objection in

all criminal cases.17       See United States v. Coady, 809 F.2d 119,

123 (1st Cir. 1987) (rejecting an argument that a claim regarding

jury     instructions     could    be   preserved      through     a    pre-charge

objection, stating, "[t]hat counsel may have discoursed upon the

nature of his theory at some time prior to the giving of the charge

will not excuse noncompliance with the express mandates of Rule

30").

              The Dunn rationale for requiring a post-charge objection

in most cases may have been apt when it was articulated more than

a half-century ago.       The judges of that era did not routinely give

lawyers       advance   copies    of    their   proposed    instructions         for

discussion and debate at charging conferences. Indeed, even during




        In a civil proceeding, the trial court has been required
        17

since 2003 to "inform the parties of its proposed instructions and
proposed action on the requests [for instructions] before
instructing the jury and before final jury arguments," Fed. R.
Civ. P. 51(b)(1) (emphasis added), and it "must give the parties
an opportunity to object on the record and out of the jury's
hearing before the instructions and arguments are delivered," id.
at (b)(2). The rule states that an objection is timely if made
"at the opportunity provided under Rule 51(b)(2)."


                                         - 62 -
my tenure as a Maine state trial judge two decades later -- in the

late    1980s     and    early    1990s    --    most   judges     did     not    preview

instructions with counsel in their entirety before delivering

them.    Hence, the general practice supported the assumption that

parties ordinarily could not object with the specificity required

by   Rules   51    and    30(d)    until    they    heard    the    instructions         as

delivered.

             That is simply not the current reality. Today, attorneys

are well-positioned to make specific objections to assist the judge

in correcting errors before he or she charges the jury.                                  The

court's ability to distribute proposed instructions in advance and

to easily revise them on the computer means that the attorney's

obligation to object with specificity can now be -- and ordinarily

is -- performed before "the charge has been heard in its entirety."

Dunn, 370 F.2d at 684.           My experience as an appellate judge reading

trial records tells me that, as a result of this current practice,

surprises    in    the    instructions      as     given    are    rare.         Thus,   by

maintaining our rule, we impose the harsh consequence of plain-

error review without justification.

             We are an outlier in requiring a post-charge objection

in criminal cases under all circumstances.                    Every other circuit

that has considered the sufficiency of a pre-charge objection

employs a more flexible approach, in which a pre-charge objection

is evaluated for its adequacy in meeting Rule 30(d)'s requirements


                                           - 63 -
to provide the trial court with specific notice of an asserted

instructional error.     See United States v. Grote, 961 F.3d 105,

115 (2d Cir. 2020) (an objection prior to jury charge is not

forfeited if "taking further exception under the circumstances

would have been futile" (quoting United States v. Rosemond, 841

F.3d 95, 107 (2d Cir. 2016));     United States v. Russell, 134 F.3d

171, 178 (3d Cir. 1998) ("[T]he crux of Rule 30 is that the district

court be given notice of potential errors in the jury instructions,

not that a party be 'required to adhere to any formalities of

language and style to preserve his objection on the record.'"

(quoting United States v. O'Neill, 116 F.3d 245, 247 (7th Cir.

1997)); United States v. Hollinger, 553 F.2d 535, 543 (7th Cir.

1977) ("[S]pecific and distinct objections voiced in an earlier

instructions conference held in the presence of a court reporter

will be considered timely under [Rule 30(d)] . . . . [W]e shall

henceforth   allow     counsel   to     incorporate   [objections]   by

reference."); United States v. Kessi, 868 F.2d 1097, 1102 (9th

Cir. 1989) (parties need not object following the instructions if

doing so would be a "pointless formality"); United States v.

Kottwitz, 614 F.3d 1241, 1270 (11th Cir. 2010) (objection is

preserved so long as it is "sufficient to give the district court

the chance to correct errors before the case goes to the jury"),

opinion withdrawn in part on denial of reh'g on other grounds, 627

F.3d 1383 (11th Cir. 2010); see also United States v. McDonnell,


                                      - 64 -
792 F.3d 478, 504 & n.15 (4th Cir. 2015) (noting that the appellant

objected at a pre-charge conference and should have repeated his

objection     after   the   instructions   were   delivered,    but   still

applying harmless error review, rather than plain error), vacated

on other grounds, 136 S. Ct. 2355 (2016);18 United States v.

Bornfield, 184 F.3d 1144, 1146 (10th Cir. 1999) (stating that a

party is "obligated to object on the record before the jury retired

to preserve his objection for appellate review" and acknowledging

that    the   objection     might   properly   occur   at   a   pre-charge

conference).

                  That flexible approach not only fulfills the notice

purpose of Rule 30(d), but it also aligns with our forfeiture

doctrine more broadly.       Issues not raised in the trial court are

deemed forfeited, and subject to plain error review on appeal, to

prevent a party from wasting judicial resources and undermining

finality by "sandbagging" the court. See Puckett v. United States,

556 U.S. 129, 134 (2009) ("[T]he contemporaneous-objection rule



        Indeed, on further review, the Supreme Court also applied
       18

a harmless error analysis and vacated the conviction on the ground
that an error in the jury instructions was not harmless.       See
McDonnell, 136 S. Ct. at 2375. The Supreme Court did not comment
on the timing requirements of Rule 30(d) or explicitly affirm a
flexible application of the rule.      Although McDonnell is not
binding intervening precedent that would require us to abandon our
current rule, see United States v. Walker-Couvertier, 860 F.3d 1,
8 (1st Cir. 2017), it does give tacit approval to review for
harmless error rather than plain error when an appellant objected
at a pre-charge conference but not after the instructions were
delivered.


                                      - 65 -
prevents a litigant from 'sandbagging' the court -- remaining

silent about his objection and belatedly raising the error only if

the case does not conclude in his favor."); United States v.

Correa-Osorio, 784 F.3d 11, 22 (1st Cir. 2015) (stating that the

plain   error   rule   "(hopefully)   deters   unsavory   sandbagging   by

lawyers (i.e., their keeping mum about an error, pocketing it for

later just in case the jury does not acquit) and gives judges the

chance to fix things without the need for appeals and new trials").

Our obsolete interpretation of Rule 30(d) does nothing to prevent

"sandbagging." Where, as in this case, a defendant files a written

request for an instruction, and argues for that request at a

charging conference, he is not "sandbagging" when he raises that

same issue on appeal.        He has clearly brought the issue to the

trial court's attention and given the court an opportunity to

correct the instructions.

           Indeed, from a practical standpoint, an objection made

during a charging conference, before the instructions have been

delivered, should be preferred to a post-charge objection.              The

earlier notice provides more timely opportunity for the court to

correct   any    errors.      See   Hollinger,   553   F.2d   at   542-43

("Ordinarily, trial judges will derive considerable benefit from

a serious exchange of views by opposing counsel regarding the

proper formulation of the applicable rules of law before they must

charge the jury.").        In addition, when a request regarding jury


                                      - 66 -
instructions has been discussed in detail at a charging conference,

and the court has ruled, there is no advantage to anyone for

lawyers to persist with the same objection.                To the contrary, such

persistence can be awkward for counsel and off-putting for the

court.    See United States v. Toribio-Lugo, 376 F.3d 33, 41 (1st

Cir. 2004) ("To do her job, a lawyer must be forceful, but she

also must handle her relationship with the presiding judge with

care."); United States v. Kelinson, 205 F.2d 600, 601-02 (2d Cir.

1953)    ("[Rule   30(d)]   does   not    require      a   lawyer     to    become   a

chattering magpie.").

            Importantly, I am not suggesting that a party's failure

to lodge an objection after the court has delivered the jury charge

should    never    result   in   forfeiture       of   the    claim    on    appeal.

Inevitably, some pre-charge objections will be insufficiently

specific,    or    inadequately    explained,      and      will    therefore    not

fulfill the notice objective of Rule 30(d).                  But Rule 30(d) does

not require us to demand pointless repetition of objections that

were distinctly raised and decisively denied.

            In short, our court's outdated, inflexible approach to

Rule 30(d) neither advances the purpose of the rule nor serves the

interests of justice and, hence, it poses an unjustifiable barrier

to plenary appellate review of fully preserved objections.                           We

should replace our outmoded instructional-error doctrine with the

flexible approach that -- for good reason -- is now the prevailing


                                         - 67 -
view.   In    other     words,   like   our   sister    circuits,      we   should

recognize    that   a    pre-charge     objection      may    preserve      a   jury

instruction   issue     for   appellate   review    if       the   objection    was

sufficiently specific to give the trial court notice of the claimed

error and repetition of the objection post-charge would be a futile

exercise.

                      - Concurring Opinion Follows -




                                        - 68 -
           BARRON, Circuit Judge, concurring.   I share the concern

that Judge Lipez expresses about the way that our precedent

currently requires us to construe Rule 30(d) of the Federal Rules

of Criminal Procedure.     The text of the rule, his concurrence

points out, does not compel the rigid procedure for preserving

objections to jury instructions that our case law requires.   There

may often be benefits to voicing objections to instructions after

the charge to the jury has been given.    But, they are not manifest

in every case.    Indeed, the case at hand exemplifies the point.

The sole ground that the District Court gave at the charging

conference for denying the requested instruction here was that the

evidence developed at trial had failed to provide a factual basis

for giving it.   Nothing about the charge itself could have called

that ruling into question.   Yet, our precedent still requires that

we treat this defendant's failure to seek reconsideration of that

ruling as if it were a failure to have requested the instruction

at all.   See United States v. Baltas, 236 F.3d 27 (1st Cir. 2001).

                  - Dissenting Opinion Follows -




                                 - 69 -
             KAYATTA, Circuit Judge, dissenting.

             The   majority's     analysis    hinges        crucially    on   the

assertion that, as to the matter of predisposition, this case is

so   like    Hinkel   and   Gamache   that   the    need    for   an   entrapment

instruction was "clear or obvious."             Respectfully, I cannot see

how this is so in this case.

             Here is what Hinkel said when he first learned that a

15-year-old was involved:        "Sounds very naughty.            I am concerned

about her age since legally she should be 16 or older."                   It then

took a month before the continued enticement ripened into a planned

meeting. Here, by contrast, is what Pérez said upon first learning

that an eleven-year-old was involved:              "Mmmm yes."      Within three

days Pérez was messaging, "I want your boyfriend."                     And within

five days from the first message, the meet was on.

             There is more.     Hinkel offered affirmative evidence that

he had never sought a relationship with someone not of legal age.

Pérez offered no such evidence. Rather, when the agent asked Pérez

at the outset of their communications "what age do you like?,"

Pérez replied, "The younger the better.             I don't discriminate.       I

started at 8.      Hehehe.    So you tell me."        And when asked "do you

like really young guys?," he replied:               "Yes.     Age?      I started

at 8."      So while Hinkel was saying he never even looked for sex

with a minor, Pérez was highlighting a nondiscriminatory track




                                       - 70 -
record.    And he was clearly saying in context that eight years old

was not too young.

            Gamache is even further removed.               The defendant in

Gamache    initially    expressed       interest     solely    in    an     adult

relationship.     Only after "the Government's insistence and artful

manipulation" over the course of eight months did he become ready

to meet the supposed victims, and even then he was saying "this

will be a new experience for me."            United States v. Gamache, 156

F.3d 1, 6, 10 (1st Cir. 1998).         Pérez, conversely, expressed eager

interest immediately.     And unlike Hinkel and Gamache, he offered

no evidence suggesting a lack of predisposition.

            The   majority's        effort   to    avoid   the      stark      pre-

dispositional     admission    by    Pérez   at   the   very   outset     of   his

exchanges with the agent warrants particular scrutiny.                  Ignoring

Pérez's express assurance that he likes them the "younger the

better," all the majority can do is claim that there is some

ambiguity about what the agent meant when he subsequently referred

to his own age.     And the majority's claim that it is not obvious

what Pérez was saying is twice-flawed:            It certainly seems obvious

he was indeed saying he likes them "the younger the better;" and,

in any event, I do not see how it was possibly plain error for the

trial court to have read Pérez's statement exactly as I do, i.e.,

as a frank, un-coaxed profession of the precise predisposition at

issue.    And since there is zero contrary evidence, I simply cannot


                                        - 71 -
see how it was also plain error to conclude that Pérez failed to

generate a sufficient claim of entrapment to get to a jury.                     See

Gamache, 156 F.3d at 9 ("The defendant carries the initial burden

of producing some evidence of both the Government's improper

inducement, and the defendant's lack of predisposition to commit

the alleged offense, so as to 'raise a reasonable doubt as to

whether he was an unwavering innocent rather than an unwavering

criminal.'" (quoting United States v. Joost, 92 F.3d 7, 12 (1st

Cir. 1996)) (second emphasis added)); see also id. ("[T]he court's

function is to examine the evidence on the record and to draw those

inferences    as    can   reasonably    be    drawn   therefrom,       determining

whether the proof, taken in the light most favorable to the defense

can plausibly support the theory of the defense." (first emphasis

added)).

             The bottom line is that the majority significantly errs

in   comparing     Hinkel    and   Gamache    to   this    case   by   noting   the

similarities     while      ignoring   or    downplaying    the   very   material

differences.       The resulting reasoning is like saying apples and

oranges are clearly and obviously the same because they both grow




                                        - 72 -
on trees in orchards.    I would rule that it was not clear or

obvious that an entrapment instruction was required in this case.19




     19  I do agree, however, with my colleague's concurrences that
we should revisit our rule on preserving objections to jury
instructions. As ably explained, our rule is not derived from the
text of Rule 30(d), no longer fits practice, and is apt to produce
unfair results. I also agree with Part V of the majority opinion.


                                - 73 -

```

---
