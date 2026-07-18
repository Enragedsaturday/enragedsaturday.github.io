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

## GROUP: content/cases/Newman v. Underhill.md  (`case`, 5 assertions)

### content_page

```
---
title: "Newman v. Underhill"
type: case
citation: "134 F.4th 1025 (2025)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 9th Circuit"
court_level: coa
circuit: 9th
year: 2025
date_decided: 2025-04-23
docket: ""
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2025-04-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Newman v. Underhill
  varies_by_point: false
  scope_note: "Good law; recent (decided 2025-04-23). Illustrates the continuity-of-pursuit requirement — a nine-minute gap delayed but did not break a hot pursuit."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10382777/newman-v-underhill/"
  cluster_id: 10382777
  opinion_id: 10849365
  identity_checked: true
homes:
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Recent development (role-based)"
related: ["[[United States v. Santana]]", "[[Welsh v. Wisconsin]]", "[[Lange v. California]]", "[[Kentucky v. King]]"]
aliases: ["Newman v. Underhill (9th Cir. 2025)"]
tags: ["case", "fourth-amendment", "exigent-circumstances", "hot-pursuit", "fresh-pursuit", "warrantless-entry", "ninth-circuit"]
holding: "The hot-pursuit exception requires officers to be in 'immediate' and 'continuous' pursuit of a suspect from the scene of the crime at the moment of entry; a pause to wait for backup may delay but not break that continuity, and a roughly nine-minute gap — far shorter than a continuity-breaking 30-minute gap — did not break the chase where officers kept a reasonably good idea of the suspect's location and kept actively working to apprehend him."
lake:
  record_id: Newman v. Underhill
  status: verified
  projected_at: 2026-07-09
---

# Newman v. Underhill

*134 F.4th 1025 (9th Cir. 2025)* · U.S. Court of Appeals, 9th Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Deputy Underhill of the San Bernardino County Sheriff's Department tried to stop a black Chevy Silverado with an expired registration and an unilluminated license plate. The driver — later identified as Richard Delacruz — failed to yield and fled, and Underhill immediately pursued. Delacruz abandoned his truck on a dead-end street and ran on foot; Underhill followed, then lost sight of him near Michael Newman's home and decided to wait for backup before entering. Roughly nine minutes after losing sight of Delacruz, and after searching the backyard, announcing the deputies' presence, and coordinating with other officers (including a helicopter), Underhill entered Newman's home without a warrant and found Delacruz, who was Newman's roommate. Newman sued the deputies under 42 U.S.C. § 1983, alleging the warrantless entry violated the Fourth Amendment; the district court granted summary judgment to the deputies on the hot-pursuit exception.

## Issue
Whether the warrantless entry into Newman's home was justified by the hot-pursuit exception, where about nine minutes elapsed between the deputy's losing sight of the fleeing suspect and his entry into the home.

## Rule
To invoke the hot-pursuit exception, officers must show (A) probable cause to search the home and (B) [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] — the pursuit of a fleeing suspect — justifying the warrantless intrusion. The underlying principle is that "a suspect may not defeat an arrest which has been set in motion in a public place . . . by the expedient of escaping to a private place." — *[[United States v. Santana]]*, 427 U.S. 38, 43 (1976) (quoted at slip op., at 8). The exception applies "only if the 'officers [were] in 'immediate' and 'continuous' pursuit of a suspect from the scene of the crime' at the moment they made entry." — *Newman v. Underhill*, 134 F.4th 1025 (9th Cir. 2025) (slip op., at 10). ^pin-op10

Continuity is the contested element here: a decision to wait for backup "delay[s], but [does] not br[eak]," the "'continuity' of the chase." — *Id.* (slip op., at [12](https://www.courtlistener.com/opinion/10382777/newman-v-underhill/#:~:text=delay%5Bs%5D%2C%20but%20%5Bdoes%5D%20not%20br%5Beak%5D%2C)). ^pin-op12

Whether continuity breaks turns on two interrelated considerations — the degree to which officers lost track of the suspect's whereabouts, and whether they kept acting with speed to apprehend him — with the passage of time relevant to both.

## Application
Applying those principles to the undisputed facts, the panel held the continuity of the chase remained intact when Underhill entered the home. "[T]he nine-minute 'pause' identified by Plaintiff is far shorter than the 30-minute period" that had broken continuity in the circuit's controlling precedent, and during those nine minutes Underhill "had a reasonably good idea where Delacruz was hiding." — 134 F.4th 1025 (slip op., at 13). ^pin-op13

On the second consideration, "[f]ar from leaving the trail to await backup, Underhill spent most, if not all, of the nine minutes in question actively working to find and apprehend Delacruz" — searching the backyard, announcing the deputies' presence, and coordinating with other officers. Immediacy was undisputed, because Underhill gave chase as soon as Delacruz failed to yield to the traffic stop (a felony) and fled. Because the suspect's offense was a felony, the categorical hot-pursuit reasoning applied and the misdemeanor-pursuit limit of [[Lange v. California]] was not implicated.

## Conclusion
On this record there was no genuine issue of material fact that the continuity of the chase had broken before entry; the hot-pursuit exception applied, and the Ninth Circuit affirmed summary judgment for the deputies.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.** (decided April 23, 2025).
- *Newman* is a recent Ninth Circuit illustration of the **continuity-of-pursuit** (fresh-pursuit) requirement: it applies [[United States v. Santana]] and [[Welsh v. Wisconsin]] and holds that a roughly nine-minute gap delayed but did not break a [[Exigent Circumstances and Hot Pursuit|hot pursuit]], distinguishing the longer gap that broke continuity in the circuit's leading precedent. Because the underlying offense was a felony, it does not implicate the misdemeanor limit of [[Lange v. California]].

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Recent development (role-based)*

## Sources
- *Newman v. Underhill*, 134 F.4th 1025 (9th Cir. 2025) — https://www.courtlistener.com/opinion/10382777/newman-v-underhill/ — pinpoints given as slip-opinion pages (slip op., at 8, 10, 12-13); CourtListener carries the slip opinion (cluster 10382777 → opinion 10849365); opinion by Graber, J.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8acb7643ac4e4739", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "134 F.4th 1025 (2025)", "court": "U.S. Court of Appeals, 9th Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Newman v. Underhill", "year": "2025"}}
{"assertion_id": "1581ae134f8b5b4b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The hot-pursuit exception requires officers to be in 'immediate' and 'continuous' pursuit of a suspect from the scene of the crime at the moment of entry; a pause to wait for backup may delay but not break that continuity, and a roughly nine-minute gap — far shorter than a continuity-breaking 30-minute gap — did not break the chase where officers kept a reasonably good idea of the suspect's location and kept actively working to apprehend him.", "title": "Newman v. Underhill"}}
{"assertion_id": "7c02e6ee9af30bce", "dimension": "support", "kind": "home_role", "locator": {"home": "Exigent Circumstances and Hot Pursuit"}, "payload": {"home": "Exigent Circumstances and Hot Pursuit", "role": "Recent development (role-based)", "title": "Newman v. Underhill"}}
{"assertion_id": "0b3663fbe3f57103", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2025-04-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Newman v. Underhill", "field_i_validity": "good_law", "scope_note": "Good law; recent (decided 2025-04-23). Illustrates the continuity-of-pursuit requirement — a nine-minute gap delayed but did not break a hot pursuit.", "title": "Newman v. Underhill", "varies_by_point": "false"}}
{"assertion_id": "d68d436827dc364a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "Newman v. Underhill"}}
```

### lake record — Newman v. Underhill

```json
{
  "schema_version": "s2.v1",
  "record_id": "Newman v. Underhill",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Newman v. Underhill",
    "case_name_short": "Newman",
    "case_name_full": "",
    "input_case_name": "Newman v. Underhill",
    "court": "U.S. Court of Appeals, 9th Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2025-04-23",
    "year": 2025,
    "docket": null,
    "cluster_id": 10382777,
    "lead_opinion_id": 10849365,
    "sibling_ids": [
      10849365
    ],
    "absolute_url": "/opinion/10382777/newman-v-underhill/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "134 F.4th 1025",
      "volume": "134",
      "reporter": "F.4th",
      "page": "1025",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "134 F.4th 1025",
        "volume": "134",
        "reporter": "F.4th",
        "page": "1025",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "134 F.4th 1025",
    "official_selection": {
      "court_class": "coa",
      "selected": "134 F.4th 1025",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op10",
      "page": null,
      "quote": "--- # Newman v. Underhill *134 F.4th 1025 (9th Cir. 2025)* \u00b7 U.S. Court of Appeals, 9th Circuit \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Deputy Underhill of the San Bernardino County Sheriff's Department tried to stop a black Chevy Silverado with an expired registration and an unilluminated license plate. The driver \u2014 later identified as Richard Delacruz \u2014 failed to yield and fled, and Underhill immediately pursued. Delacruz abandoned his truck on a dead-end street and ran on foot; Underhill followed, then lost sight of him near Michael Newman's home and decided to wait for backup before entering. Roughly nine minutes after losing sight of Delacruz, and after searching the backyard, announcing the deputies' presence, and coordinating with other officers (including a helicopter), Underhill entered Newman's home without a warrant and found Delacruz, who was Newman's roommate. Newman sued the deputies under 42 U.S.C. \u00a7 1983, alleging the warrantless entry violated the Fourth Amendment; the district court granted summary judgment to the deputies on the hot-pursuit exception. ## Issue Whether the warrantless entry into Newman's home was justified by the hot-pursuit exception, where about nine minutes elapsed between the deputy's losing sight of the fleeing suspect and his entry into the home. ## Rule To invoke the hot-pursuit exception, officers must show (A) probable cause to search the home and (B) exigent circumstances \u2014 the pursuit of a fleeing suspect \u2014 justifying the warrantless intrusion. The underlying principle is that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op12",
      "page": null,
      "quote": "delay[s], but [does] not br[eak],",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 18222,
      "fragment": "#:~:text=delay%5Bs%5D%2C%20but%20%5Bdoes%5D%20not%20br%5Beak%5D%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-op13",
      "page": null,
      "quote": "[T]he nine-minute 'pause' identified by Plaintiff is far shorter than the 30-minute period",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2025-04-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Newman v. Underhill",
    "varies_by_point": false,
    "scope_note": "Good law; recent (decided 2025-04-23). Illustrates the continuity-of-pursuit requirement \u2014 a nine-minute gap delayed but did not break a hot pursuit.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jones v. City of North Las Vegas",
          "cluster_id": 10804885,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Newman v. Underhill:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. City of North Las Vegas",
          "cluster_id": 10667775,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Newman v. Underhill:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(10849365) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
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
        "query": "cites:(10849365)",
        "reviewed": 2,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(10849365)",
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
    "complete_query": "cites:(10849365)",
    "indexed_citing_opinions": 2,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 10849365,
        "count": 2,
        "count_source": "search"
      }
    ],
    "citation_count": 2,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/newman-v-underhill.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 2,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 10849365,
        "cited_id": 145496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 323062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 781819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 786149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 1427207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 2681571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 3031410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 4536868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 4697833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 6932793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 8897088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9407324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9426490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9427232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9429232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9429597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9441559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9494149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9498747,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9499600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9597796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10849365,
        "cited_id": 9960171,
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
    "date_created": "2026-07-05T15:52:21Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:53:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Newman v. Underhill

```
                    FOR PUBLICATION

     UNITED STATES COURT OF APPEALS
          FOR THE NINTH CIRCUIT

MICHAEL NEWMAN,                                   No. 24-1493
                                                   D.C. No.
               Plaintiff - Appellant,
                                               5:23-cv-00033-SP
    v.

TODD UNDERHILL, Deputy;
JONATHAN BARMER, Deputy;                            OPINION
LAUREN LAIDLAW; JAMES
BLANKENSHIP; COUNTY OF
SAN BERNARDINO,

               Defendants - Appellees.

         Appeal from the United States District Court
            for the Central District of California
           Sheri Pym, Magistrate Judge, Presiding
          Argued and Submitted February 12, 2025
                   Pasadena, California
                      Filed April 23, 2025
Before: Susan P. Graber, David F. Hamilton, and Patrick J.
                Bumatay, Circuit Judges. *
                   Opinion by Judge Graber


*
 The Honorable David F. Hamilton, United States Circuit Judge for the
Court of Appeals, 7th Circuit, sitting by designation.
2                      NEWMAN V. UNDERHILL


                          SUMMARY **


        Fourth Amendment/Hot Pursuit Exception

    The panel affirmed the district court’s summary
judgment for San Bernardino County Sheriff’s Department
deputies in an action brought pursuant to 42 U.S.C. § 1983
alleging Fourth Amendment violations when deputies
entered plaintiff’s home without a warrant while pursuing a
fleeing suspect.
    The district court granted summary judgment to
defendants, reasoning, in relevant part, that no Fourth
Amendment violation occurred because the hot-pursuit
exception to the warrant requirement applied.
    In affirming the district court, the panel first held that, as
a matter of law, defendants had probable cause for the
entry. Under the circumstances, a reasonable person in
Deputy Underhill’s shoes would have believed that there
was at least a fair probability that the suspect was in
plaintiff’s home. The panel next held that Underhill’s
pursuit of the suspect constituted an exigent situation
justifying the entry because the officers were in immediate
and continuous pursuit of a suspect from the scene of the
crime at the moment they made entry. Underhill gave chase
immediately after seeing the suspect fail to yield to a traffic
stop, a felony, and fleeing in his truck after being instructed
to stop. Notwithstanding the nine-minute delay between



**
  This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                    NEWMAN V. UNDERHILL                      3


Underhill losing sight of the suspect and Underhill entering
plaintiff’s home, the continuity of the chase remained intact.



                         COUNSEL

Alex Coolman (argued), Law Office of Alex Coolman, San
Diego, California, for Plaintiff-Appellant.
Daniel S. Roberts (argued), ColeHuber LLP, Ontario,
California, for Defendants-Appellees.



                         OPINION

GRABER, Circuit Judge:

    Deputy Todd Underhill of the San Bernardino County
Sheriff’s Department gave chase when the driver of a truck
feloniously failed to heed Underhill’s instruction to stop.
The suspect eventually parked near Plaintiff Michael
Newman’s home, got out of the truck, and ran. Underhill
followed on foot but lost sight of the suspect somewhere near
the rear of the house. While waiting for backup, he searched
the surrounding area but did not find the suspect. When
another officer arrived, Underhill explained that he thought
the suspect could be inside the house and that the house’s
backdoor was unlocked. Less than ten minutes later,
Underhill and other officers entered the house and
discovered Plaintiff. After questioning the legality of their
entry, Plaintiff allowed the officers to search for the suspect
(Plaintiff’s roommate), whom the officers quickly found.
4                      NEWMAN V. UNDERHILL


Plaintiff brought this action, raising both federal and state
claims predicated on an alleged violation of his Fourth
Amendment rights. The district court granted summary
judgment to Defendants, reasoning, in relevant part, that no
Fourth Amendment violation occurred because the hot-
pursuit exception to the warrant requirement applied.
Reviewing de novo, Perez v. City of Fresno, 98 F.4th 919,
924 (9th Cir. 2024), we affirm.
                        BACKGROUND
    In the early hours of July 27, 2022, Sheriff’s Deputy
Todd Underhill attempted to pull over a black Chevy
Silverado that had an expired registration and an
unilluminated license plate. The Silverado’s driver—later
identified as Richard Delacruz—fled, and Underhill
immediately pursued. Eventually, Delacruz got out of his
truck on a dead-end street and ran away on foot. Underhill
followed, also on foot, stopping briefly to “clear” the
Silverado before continuing the pursuit.
    Having lost sight of Delacruz, Underhill reported to
dispatch that Delacruz had been “[l]ast seen toward the
residence at 4083 Camellia Drive”—Plaintiff Michael
Newman’s home. The house sits on a hill, with “drop offs”
between it and adjacent properties and with fencing—which,
in some places, is only waist high—around the perimeter of
the backyard. 1
   Underhill ran toward Plaintiff’s backyard and, not seeing
Delacruz, decided to wait for backup before continuing the

1
  Underhill later declared that he saw Delacruz “open a gate and go into
the backyard” and heard “a noise consistent with a door opening and
closing,” although Underhill mentioned those details in neither his
incident report nor his probable-cause statement.
                        NEWMAN V. UNDERHILL                              5


pursuit. Deputy Jonathan Barmer arrived roughly two
minutes later. According to the transcript of the audio from
Underhill’s belt recorder, Underhill told Barmer that
Delacruz had gone “somewhere over to the rear of the
residence.” 2 Underhill also stated that he “th[ought],” but
did not “know,” that Delacruz “may” have entered Plaintiff’s
home.
    Underhill and Barmer searched the backyard for
Delacruz with their flashlights, while deputies in a Sheriff’s
Department helicopter looked for heat signatures from
overhead. The deputies neither saw any sign of Delacruz nor
heard any noises—such as the rattling of a fence—to suggest
that he had left the backyard. For their part, the deputies in
the helicopter detected heat coming from Plaintiff’s home
but could not confirm who or what was emitting it.
    During or shortly after inspecting the backyard,
Underhill noticed something about Plaintiff’s backdoor.
Underhill’s belt-recorder first captured him saying: “Yeah[,]
because he came and locked that door, dude.” It is not clear
from the record what Underhill meant by that statement.
Underhill was also recorded stating: “We got an unlocked
rear door.” Underhill later testified at his deposition that the
backdoor had been “slightly ajar[].”
    About seven minutes after Delacruz fled his truck on
foot, Underhill began announcing the Sheriff’s
Department’s presence and ordering any occupants of the
home to exit.     Underhill continued to make those
announcements for another two minutes. During that period,

2
  The record before us contains competing and somewhat inconsistent
transcripts of this recording, but not the recording itself. Because we are
reviewing a summary judgment in Defendants’ favor, we rely on
Plaintiff’s submission.
6                      NEWMAN V. UNDERHILL


Underhill heard at least one voice coming from inside the
house, and Deputy Lauren Laidlaw arrived at the scene.
    Roughly nine minutes after last seeing Delacruz,
Underhill—accompanied by Laidlaw and Barmer—entered
Plaintiff’s home through the backdoor. Hearing Plaintiff’s
voice coming from elsewhere in the house, Underhill found
Plaintiff’s room and discovered that Plaintiff is “a
quadriplegic in a wheelchair.” During their ensuing
conversation, which grew contentious at times, Plaintiff told
Underhill that his roommate drove a black Chevy Silverado.
    About eight minutes after Underhill entered the house,
Sergeant James Blankenship joined Underhill and Plaintiff.
After another four minutes of conversation, Plaintiff gave
the officers consent to look for his roommate in a different
part of the house. The officers quickly found and arrested
Delacruz, who was later convicted of a felony—evading a
peace officer with wanton disregard for safety, in violation
of California Vehicle Code section 2800.2(a).
    Plaintiff sued Defendants Underhill, Laidlaw, and
Blankenship, asserting a claim under 42 U.S.C. § 1983 for
unreasonable search in violation of the Fourth Amendment.
The operative complaint also lists two state-law causes of
action. 3 The district court entered summary judgment in
favor of Defendants on all claims. Plaintiff timely appeals.
                          DISCUSSION
    All three of Plaintiff’s claims are predicated on the
allegation that Defendants violated Plaintiff’s Fourth

3
 Additionally, Plaintiff brought a claim under Monell v. Department of
Social Services, 436 U.S. 658 (1978), against San Bernardino County.
The district court granted summary judgment to the County on that
claim, a decision that Plaintiff does not challenge in this appeal.
                        NEWMAN V. UNDERHILL                            7


Amendment rights when they entered his home without a
warrant. 4 Because the record before us does not support that
allegation, each of Plaintiff’s claims fails. 5
    Under the Fourth Amendment’s guarantee against
unreasonable searches, one’s home is “the most
constitutionally protected place on earth.” United States v.
Craighead, 539 F.3d 1073, 1083 (9th Cir. 2008); see also,
e.g., Fisher v. City of San Jose, 558 F.3d 1069, 1082 (9th
Cir. 2009) (en banc) (“[T]he home is perhaps the most
sacrosanct domain, where one’s Fourth Amendment
interests are at their zenith.”); Florida v. Jardines, 569 U.S.
1, 6 (2013) (describing “the home” as the “first among
equals”). Accordingly, the government ordinarily may not
search someone’s home without “a criminal warrant
supported by probable cause.” United States v. Grey, 959
F.3d 1166, 1177 (9th Cir. 2020).
    Nonetheless, there are a few narrow exceptions to the
warrant requirement. Sandoval v. Las Vegas Metro. Police
Dep’t, 756 F.3d 1154, 1161 (9th Cir. 2014). As relevant
here, “the exigencies of [a] situation” sometimes “make the
needs of law enforcement so compelling that [a] warrantless
search is objectively reasonable.” Lange v. California, 594
U.S. 295, 301 (2021) (second alteration in original) (quoting
Kentucky v. King, 563 U.S. 452, 460 (2011)). Situations

4
  Most of Plaintiff’s arguments are framed as critiques of the district
court’s construction of the evidence. But because our review is de novo,
we do not consider whether “the district court gave insufficient
attention” to certain aspects of the record. Tanadgusix Corp. v. Huber,
404 F.3d 1201, 1205 n.5 (9th Cir. 2005).
5
  We therefore do not address the parties’ arguments pertaining to
(1) qualified immunity’s “clearly established law” prong or
(2) secondary questions regarding Plaintiff’s state-law causes of action.
8                    NEWMAN V. UNDERHILL


involving “the hot pursuit of a fleeing suspect” can fit that
description. United States v. Struckman, 603 F.3d 731, 743
(9th Cir. 2010). Underlying the so-called hot-pursuit
exception is the principle that “a suspect may not defeat an
arrest which has been set in motion in a public place . . . by
the expedient of escaping to a private place.” United States
v. Santana, 427 U.S. 38, 43 (1976).
    To rely on the hot-pursuit exception, Defendants must
establish that (A) they had probable cause to search
Plaintiff’s home and (B) “exigent circumstances”—here, the
pursuit of a fleeing suspect—“justified the warrantless
intrusion.” United States v. Johnson, 256 F.3d 895, 905 (9th
Cir. 2001) (en banc) (per curiam). On this record, we hold
that Defendants have satisfied both requirements as a matter
of law.
    A. Probable Cause
    To establish probable cause in this case, Defendants
must show that, when Underhill entered Plaintiff’s home,
“the ‘facts and circumstances’ before [him were] sufficient
to warrant a person of reasonable caution to believe” that
Delacruz would be found therein. Id. at 905; see also United
States v. Scott, 520 F.2d 697, 700 (9th Cir. 1975) (framing
the question of probable cause, in a case about the
“exigencies of hot pursuit,” as “whether the officers . . . had,
at the time of entry, probable cause to believe that the
fugitives they sought were there”). As that description
suggests, and despite Plaintiff’s contention to the contrary,
“probable cause means ‘fair probability,’ not certainty or
even a preponderance of the evidence.” United States v.
Gourde, 440 F.3d 1065, 1069 (9th Cir. 2006) (en banc)
(emphasis added) (quoting Illinois v. Gates, 462 U.S. 213,
246 (1983)). “Whether there is a fair probability . . . is a
                        NEWMAN V. UNDERHILL                            9


‘commonsense, practical question’” that “depends upon the
totality of the circumstances, including reasonable
inferences.” United States v. Kelley, 482 F.3d 1047, 1050
(9th Cir. 2007) (quoting Gourde, 440 F.3d at 1069).
    To create a genuine factual dispute regarding probable
cause, Plaintiff relies on the purported presence of
“ambiguity” in the record as to “when and where
exactly . . . Underhill lost track of [Delacruz].” But to the
extent that any such ambiguity exists, it is immaterial. The
following facts are not in dispute: (1) Underhill saw
Delacruz running toward the back of the house;
(2) Underhill, having searched the area, knew that Delacruz
was not hiding in the backyard; (3) if Delacruz had tried to
move from the backyard to an adjacent property, he would
have been hindered by fencing and by drop-offs in the
terrain; (4) Underhill found the backdoor unlocked; and
(5) as demonstrated by his contemporaneous statements,
Underhill perceived someone interacting with the backdoor
at some point during the pursuit. 6 Faced with those
circumstances, a reasonable person in Underhill’s shoes
would have believed that there was at least a fair probability
that Delacruz was in Plaintiff’s home. We do not see, and
Plaintiff does not identify, anything in the record to dispel
such a reasonable belief.
   We therefore hold that, as a matter of law, Defendants
had probable cause to believe that Delacruz was inside


6
  We need not resolve whether a reasonable juror necessarily would
credit Underhill’s statement—made only in a declaration—that he
“heard . . . a noise consistent with a door opening and closing” after
seeing Delacruz enter Plaintiff’s backyard. Even disregarding that
statement, the undisputed evidence described in the text demonstrates the
absence of a genuine dispute of material fact regarding probable cause.
10                    NEWMAN V. UNDERHILL


Plaintiff’s home. See Johnson v. Barr, 79 F.4th 996, 1003
(9th Cir. 2023) (explaining that summary judgment on the
issue of probable clause is appropriate only “when there is
no genuine issue of fact and if ‘no reasonable jury could find
an absence of probable cause under the facts’” (quoting
Gasho v. United States, 39 F.3d 1420, 1428 (9th Cir. 1994))).
     B. Hot Pursuit
    In addition to establishing probable cause, Defendants
must show that Underhill’s pursuit of Delacruz constituted
an exigent situation justifying the entry into Plaintiff’s home.
Johnson, 256 F.3d at 907.
    In our circuit, a “hot pursuit” excuses a warrantless
intrusion into the home only if the “officers [were] in
‘immediate’ and ‘continuous’ pursuit of a suspect from the
scene of the crime” at the moment they made entry. Id.
(quoting Welsh v. Wisconsin, 466 U.S. 740, 753 (1984)).
Other relevant considerations include “the gravity of the
underlying offense for which the arrest is being made,” id. at
908 (quoting Welsh, 466 U.S. at 753), and whether “the
officers encroached on the property of a person who did not
create the exigent circumstances and was completely
unrelated to the suspect and his [crimes],” id. at 909.
    In this case, we need deal only with the exception’s
“immediacy” and “continuity” requirements. Respecting the
gravity of the offense, Plaintiff does not dispute that
Underhill observed Delacruz committing a felony.
Although the Supreme Court has not decided whether all
felonies give the police license to chase someone into their
home without a warrant, see Lange, 594 U.S. at 304–05
(assuming, but not deciding, that “fleeing-felon cases . . .
always present[] exigent circumstances”) (emphasis
omitted); Johnson, 256 F.3d at 908 n.6 (“In situations where
                    NEWMAN V. UNDERHILL                     11


an officer is truly in hot pursuit and the underlying offense
is a felony, the Fourth Amendment usually yields.”
(emphasis added)), we need not resolve that question
because Plaintiff does not argue that Delacruz’s crime fails
to qualify for the “hot pursuit” exception. And no party
discusses the effect of Plaintiff’s relationship to Delacruz, a
factor that, in general, “[v]ery few cases have considered.”
Johnson, 256 F.3d at 909.
       1. Immediacy
    We need not dwell long on the question of immediacy.
It is undisputed that Underhill gave chase “immediately”
after seeing Delacruz fail to yield to a traffic stop—thereby
committing a felony—and flee in his truck.
    Plaintiff suggests that, in this context, “immediate”
means that the warrantless search must “follow immediately,
in a temporal sense, from the underlying pursuit.” But that
interpretation would render the word “continuous”—which,
on its own, denotes that a pursuit stops being “hot” once it
ends—meaningless. More to the point, Johnson made clear
that an officer satisfies the requirement of immediacy if the
officer gives chase as soon as the suspect flees from the
scene of the crime. See id. at 907 (asking whether the
officers were in “immediate . . . pursuit of a suspect from the
scene of the crime” (emphasis added) (internal quotation
marks omitted)).
       2. Continuity
   Plaintiff argues that, because nine minutes elapsed
between Underhill’s losing sight of Delacruz and
Underhill’s entering Plaintiff’s home, a genuine dispute of
material fact exists regarding the continuity of the pursuit.
We disagree.
12                  NEWMAN V. UNDERHILL


    Johnson contains our most thorough exploration of the
continuity requirement. There, the suspect fled into the
woods, and the officer—concerned for his safety—decided
not to follow until backup arrived. Johnson, 256 F.3d at
907–08. While waiting for his colleagues, the officer
returned to the scene of his initial confrontation with the
suspect. Id. at 907. Thirty minutes passed, during which
time the suspect “was free to run,” and during which time
the police neither saw the suspect nor “received [any] new
information about where [he] had gone.” Id. at 908.
Addressing the hot-pursuit exception, we made clear that, in
certain circumstances, the decision to wait for backup
“delay[s], but [does] not br[eak],” the “‘continuity’ of the
chase.” Id. We explained, however, that because the
officers in Johnson had no clue where the suspect was for
more than 30 minutes, the chase’s continuity had been
“clearly broken.” Id.
    We discern two interrelated considerations underlying
the distinction that Johnson drew between “delayed
continuity” and “broken continuity.” First, we focused on
whether, and to what degree, the officers lost track of the
suspect’s whereabouts. On one end of the spectrum, the
continuity of the chase is more likely to survive when “police
officers always kn[o]w exactly where the suspect [is].” Id.
(emphasis added). On the other end sit cases like Johnson,
in which the officers “no longer had any idea where [the
suspect] was” by the time they resumed their search. Id.
(emphasis added). Second, we examined whether the
officers, after losing sight of the suspect, continued to act
with speed in attempting to apprehend the suspect. In
Johnson, the government’s “continuity” showing was
undermined by the fact that the officer did not “monitor [the
suspect’s] movements while waiting for his backup to
                       NEWMAN V. UNDERHILL                           13


arrive,” but instead went to retrieve an item that he had
dropped earlier. Id. Relevant to both considerations is the
question of timing. The more time passes without the
officer’s physically chasing after the suspect—whether
because the officer loses track of the suspect or because the
officer stops attempting to apprehend the suspect—the more
likely the continuity of the chase is to break. See id.
(stressing that the suspect was left “free to run for over a half
hour”). 7
    Applying those principles to the undisputed facts in the
record, we conclude that, when Underhill entered Plaintiff’s
home, the continuity of the chase remained intact.
Regarding the first consideration identified above, the nine-
minute “pause” identified by Plaintiff is far shorter than the
30-minute period at issue in Johnson. The undisputed
evidence supporting the existence of probable cause also
demonstrates that, during those nine minutes, Underhill had
a reasonably good idea where Delacruz was hiding. 8

7
   Because “the Fourth Amendment ultimately turns on the
reasonableness of the officer’s actions in light of the totality of the
circumstances,” Struckman, 603 F.3d at 743, we do not suggest that these
are the only considerations that might ever factor into a court’s
continuity-of-pursuit analysis. Still, we note that the D.C. Circuit has
taken an approach similar to ours. See United States v. Dawkins, 17 F.3d
399, 407 (D.C. Cir.) (“[S]peed and a continuous knowledge of the
alleged perpetrator’s whereabouts are the elements which underpin th[e]
[hot-pursuit] exception . . . .” (quoting United States v. Lindsay, 506
F.2d 166, 173 (D.C. Cir. 1974))), amended, 327 F.3d 1198 (D.C. Cir.
1994).
8
  The probable-cause and exigent-circumstances inquiries often overlap
to some degree. See United States v. Brooks, 367 F.3d 1128, 1135 (9th
Cir. 2004) (“Many of the same facts that showed probable cause to
suspect evidence of crime are also relevant to show Perez’s exigent need
to enter.”).
14                  NEWMAN V. UNDERHILL


Johnson’s second variable points in the same direction. Far
from leaving the trail to await backup, Underhill spent most,
if not all, of the nine minutes in question actively working to
find and apprehend Delacruz. He searched the backyard,
announced the Sheriff’s Department’s presence, and
coordinated with fellow officers—including those keeping
watch from a helicopter. Conversely, Plaintiff points to no
evidence that would allow us to infer that Defendants ceased
their pursuit of Delacruz after Underhill lost sight of him.
   In sum, on this record there is no genuine issue of
material fact suggesting that the continuity of the chase was
broken before Underhill entered Plaintiff’s home.
     AFFIRMED.

```

---

## GROUP: content/cases/Olivier v. City of Brandon.md  (`case`, 5 assertions)

### content_page

```
---
title: Olivier v. City of Brandon
type: case
citation: "No. 24-993, slip op. (U.S. 2026)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2026
date_decided: ""
docket: 24-993
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
  opinion_url: "https://www.courtlistener.com/opinion/10811625/olivier-v-city-of-brandon/"
  cluster_id: 10811625
  opinion_id: null
  identity_checked: false
lake:
  record_id: Olivier v. City of Brandon
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Heck v. Humphrey]]"
tags:
  - case
  - section-1983
  - heck-v-humphrey
  - prospective-relief
  - first-amendment
  - favorable-termination
  - supreme-court
holding: "Heck v. Humphrey does not bar a § 1983 suit seeking purely prospective relief — here an injunction against future enforcement of a protest-permit ordinance — even where the plaintiff was previously convicted of violating that same ordinance, because such a suit is not designed to annul the prior conviction and falls within § 1983's heartland."
aliases:
  - Olivier v. City of Brandon
  - "Olivier v. City of Brandon, Mississippi"
  - "Olivier v. City of Brandon (2026)"
---

# Olivier v. City of Brandon

*No. 24-993, slip op. (U.S. 2026)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10811625 → majority opinion 11278377 (No. 24-993, decided Mar. 20, 2026). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07; slip-style pin (current-Term slip opinion, no reporter cite assigned — S2 A3). S9 promotes. -->

## Background
Gabriel Olivier, a street preacher, was convicted in municipal court of violating a City of Brandon ordinance requiring protesters and demonstrators near an amphitheater to stay within a "designated protest area." He paid a fine, served no prison time, and did not appeal. Still wishing to preach near the amphitheater, he sued the City under 42 U.S.C. § 1983, seeking only prospective relief: a declaration that the ordinance violates the First Amendment and an injunction against its future enforcement. The lower courts held the suit barred by *[[Heck v. Humphrey]]*, reasoning that success would cast doubt on the validity of his prior conviction.

## Issue
Whether *[[Heck v. Humphrey]]* bars a § 1983 suit for wholly prospective relief brought by a plaintiff previously convicted under the challenged law.

## Rule
*[[Heck v. Humphrey|Heck]]* prohibits using § 1983 to obtain relief that would necessarily imply the invalidity of a conviction or sentence when the plaintiff seeks release or damages, but a suit that is "in no way designed to annul the results of a state trial" and seeks only "to be free from prosecutions for future violations" falls within § 1983's heartland (*Wooley v. Maynard*). The Court held: "Olivier's suit seeking purely prospective relief — an injunction stopping officials from enforcing an ordinance in the future — can proceed, notwithstanding Olivier's prior conviction for violating that ordinance; *Heck* does not hold otherwise." — slip op. at 1. ^pin-slip1

## Application
Olivier sought neither the reversal of his conviction nor damages for it — only forward-looking relief so he could preach without fear of future arrest. That request does not question the validity of his completed conviction; it seeks to prevent future enforcement, exactly the kind of claim *Wooley* permitted a previously convicted plaintiff to bring. Reading *[[Heck v. Humphrey|Heck]]* to bar it would trap Olivier between intentionally flouting state law and forgoing what he believes to be constitutionally protected activity.

## Conclusion
**Reversed and [[Reading and Citing Cases#on-remand|remanded]].** Justice Kagan wrote for a unanimous Court (9–0).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Olivier* cabins *[[Heck v. Humphrey|Heck]]*'s favorable-termination rule to claims that would undermine a conviction or seek release/damages, confirming that prospective injunctive relief against future enforcement remains available under § 1983 even to a previously convicted plaintiff.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Olivier v. City of Brandon*, No. 24-993, slip op. (U.S. 2026)](https://www.courtlistener.com/opinion/10811625/olivier-v-city-of-brandon/) — pinpoint: slip op. at 1 (Heck does not bar prospective-relief § 1983 suits). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07. Current-Term slip opinion; no U.S. Reports cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d4a7151d87b654a5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 24-993, slip op. (U.S. 2026)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Olivier v. City of Brandon", "year": "2026"}}
{"assertion_id": "a2edacfb5382233c", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Recent development", "title": "Olivier v. City of Brandon"}}
{"assertion_id": "db7a170b71d09934", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Heck v. Humphrey does not bar a § 1983 suit seeking purely prospective relief — here an injunction against future enforcement of a protest-permit ordinance — even where the plaintiff was previously convicted of violating that same ordinance, because such a suit is not designed to annul the prior conviction and falls within § 1983's heartland.", "title": "Olivier v. City of Brandon"}}
{"assertion_id": "070cf5bed98aed08", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Olivier v. City of Brandon"}}
{"assertion_id": "60fdbe088a324040", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Olivier v. City of Brandon", "varies_by_point": "false"}}
```

### lake record — Olivier v. City of Brandon

```json
{
  "schema_version": "s2.v1",
  "record_id": "Olivier v. City of Brandon",
  "status": "under_review",
  "identity": {
    "case_name": "Olivier v. City of Brandon",
    "case_name_short": "Olivier",
    "case_name_full": "",
    "input_case_name": "Olivier v. City of Brandon",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2026,
    "docket": "24-993",
    "cluster_id": 10811625,
    "lead_opinion_id": 11278377,
    "sibling_ids": [],
    "absolute_url": "/opinion/10811625/olivier-v-city-of-brandon/",
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
      "court_class": "scotus",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "SCOTUS No. 24-993, decided 2026-03-20 (607 U.S. ___; Kagan, 9-0). No S. Ct. page yet. (Search-floated '146 S. Ct. 916' rejected as fabricated.)",
      "legs": [
        {
          "source": "Cornell LII",
          "url": "https://www.law.cornell.edu/supremecourt/text/24-993",
          "cite": "No. 24-993, decided 2026-03-20"
        },
        {
          "source": "SCOTUSblog",
          "url": "https://www.scotusblog.com/cases/case-files/olivier-v-city-of-brandon-mississippi/",
          "cite": "No. 24-993; no reporter cite listed"
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
    "date_created": "2026-07-06T12:13:43Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "olivier-v-city-of-brandon--10811625",
      "to_record_id": "Olivier v. City of Brandon",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Olivier v. City of Brandon

```
(Slip Opinion)              OCTOBER TERM, 2025                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

        OLIVIER v. CITY OF BRANDON, MISSISSIPPI

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE FIFTH CIRCUIT

   No. 24–993.      Argued December 3, 2025—Decided March 20, 2026


Petitioner Gabriel Olivier is a street preacher in Mississippi who believes
  that sharing his religious views with fellow citizens is an important
  part of exercising his faith. His vocation sometimes took him to the
  sidewalks near an amphitheater in the City of Brandon, where he
  could find sizable audiences attending events. In 2019, the City
  adopted an ordinance requiring all individuals or groups engaging in
  “protests” or “demonstrations,” at around the time events were sched-
  uled, to stay within a “designated protest area.” In 2021, Olivier was
  arrested for violating that ordinance. He pleaded no contest in munic-
  ipal court. The court imposed a $304 fine, one year of probation, and
  10 days of imprisonment to be served only if he violated the ordinance
  during his probation. Olivier did not appeal, paid the fine, and served
  no prison time. Because he still wanted to preach near the amphithe-
  ater, Olivier filed suit against the City in federal court under 42
  U. S. C. §1983, alleging that the city ordinance violates the Free
  Speech Clause of the First Amendment by consigning him and other
  speakers to the amphitheater’s protest area. The complaint seeks, as
  a remedy, a declaration that the ordinance infringes the First Amend-
  ment and an injunction preventing city officials from enforcing the or-
  dinance in the future. In other words, the relief requested is only pro-
  spective; Olivier seeks neither the reversal of, nor compensation for,
  his prior conviction.
    The parties contested in the lower courts whether this Court’s deci-
  sion in Heck v. Humphrey, 512 U. S. 477—which prohibits the use of
  §1983 to challenge the validity of a prior conviction or sentence so as
  to obtain release from custody or monetary damages—bars the suit
  from going forward. On the City’s view of Heck, a person previously
2                    OLIVIER v. CITY OF BRANDON

                                  Syllabus

    convicted of violating a statute cannot challenge its constitutionality
    under §1983 because success in the suit would cast doubt on the prior
    conviction’s correctness. On Olivier’s contrary view, Heck does not ap-
    ply when a plaintiff seeks wholly prospective relief, rather than relief
    relating to the prior conviction. The District Court agreed with the
    City’s understanding of Heck and found Olivier’s suit barred. The
    Court of Appeals for the Fifth Circuit affirmed on the same reasoning.
Held: Olivier’s suit seeking purely prospective relief—an injunction stop-
 ping officials from enforcing an ordinance in the future—can proceed,
 notwithstanding Olivier’s prior conviction for violating that ordinance;
 Heck does not hold otherwise. Pp. 5–13.
    (a) Before the Court’s decision in Heck, the City would have had no
 plausible basis for claiming Olivier’s suit is barred. That type of suit
 falls within §1983’s heartland: Assuming a credible threat of prosecu-
 tion, a plaintiff may bring a §1983 action to challenge a local law as
 violating the Constitution and to prevent that law’s future enforce-
 ment. See, e.g., Steffel v. Thompson, 415 U. S. 452. In Wooley v.
 Maynard, 430 U. S. 705, the Court held that rule to apply even when
 the plaintiff was previously convicted under the challenged law. The
 Court explained that because the suit at issue sought “wholly prospec-
 tive” relief—“only to be free from prosecutions for future violations”—
 and was “in no way designed to annul the results of a state trial,” §1983
 provided an avenue for the plaintiff ’s claim. Id., at 711. Were it oth-
 erwise, the plaintiff would have been trapped “between the Scylla of
 intentionally flouting state law and the Charybdis of forgoing what he
 believes to be constitutionally protected activity.” Id., at 710.
    The Court’s decision in Wooley, taken alone, would defeat the City’s
 attempt to prevent Olivier’s suit from going forward, but the City ar-
 gues the Court’s later decision in Heck requires the opposite result. In
 Heck, the Court held that a state prisoner could not use §1983 to seek
 damages attributable to his allegedly unconstitutional conviction. The
 Court reasoned that such a suit in truth mounts a “collateral attack”
 on the validity of the conviction, and thus intrudes on the habeas stat-
 ute’s domain. 512 U. S., at 485. And such a suit could lead to “parallel
 litigation” and “conflicting” judgments about the same conduct, with
 the §1983 suit suggesting that the plaintiff should be released even as
 criminal or habeas proceedings found the opposite. Id., at 484. Hence
 the so-called Heck bar on “§1983 damages actions that necessarily re-
 quire the plaintiff to prove the unlawfulness of his conviction or con-
 finement.” Id., at 486. “[W]hen a state prisoner seeks damages in a
 §1983 suit,” the Court went on, “the district court must consider
 whether a judgment in favor of the plaintiff would necessarily imply
 the invalidity of his conviction or sentence.” Id., at 487.
    The Court subsequently drew a line between Heck-type claims and
                     Cite as: 607 U. S. ___ (2026)                         3

                                Syllabus

those seeking forward-looking relief. In Edwards v. Balisok, 520 U. S.
641, the Court held that while a state prisoner could not obtain dam-
ages for an alleged past violation, a claim for “prospective injunctive
relief ”—the use of fairer procedures in the future—may “properly be
brought under §1983,” because it does not depend on showing the “in-
validity of a previous” sentencing decision. Id., at 648. In Wilkinson
v. Dotson, 544 U. S. 74, the Court allowed state prisoners to bring a
§1983 suit requesting an injunction requiring the State to “comply
with constitutional” parole requirements “in the future,” determining
that such a claim for “future relief ” was “distant” from “the core of ha-
beas” and so not barred by Heck. 544 U. S., at 77, 82. Pp. 5–9.
  (b) As in Balisok and Dotson, Olivier’s suit falls outside habeas’s
core—and likewise outside Heck’s concerns. Olivier is not challenging
the “validity of [his] conviction or sentence,” for the purpose of securing
release or obtaining monetary damages. Nance v. Ward, 597 U. S. 159,
167–168. Instead, he seeks “wholly prospective” relief—“only to be free
from prosecutions for future violations” of the ordinance. Wooley, 430
U. S., at 711. Because Olivier’s suit does not, as habeas suits do, “col-
lateral[ly] attack” the old conviction, it cannot give rise to “parallel lit-
igation” respecting his prior conduct, and does not risk “conflicting”
judgments over how that conduct was prosecuted or punished. Heck,
512 U. S., at 484, 485. Unlike in Heck, Olivier’s suit merely attempts
to prevent a future prosecution, so the Heck bar does not come into
play. Pp. 9–10.
  (c) The City’s main argument to the contrary rests on one sentence
in Heck that states: “[W]hen a state prisoner seeks damages in a §1983
suit, the district court must consider whether a judgment in favor of
the plaintiff would necessarily imply the invalidity of his conviction or
sentence; if it would, the complaint must be dismissed.” 512 U. S., at
487. Strictly speaking, the “necessarily imply” language fits: If Olivier
succeeds in this suit, it would mean his prior conviction was unconsti-
tutional. But “general language in judicial opinions should be read as
referring in context to circumstances similar to [those] then before the
Court,” Turkiye Halk Bankasi A.S. v. United States, 598 U. S. 264, 278,
and the circumstances here differ from those in Heck. The Heck lan-
guage at issue was used to identify claims that were really assaults on
a prior conviction, even though involving some indirection. By con-
trast, there is no looking back in Olivier’s suit; both in the allegations
made, and in the relief sought, the suit is entirely future oriented—
even if success in it shows that something past should not have oc-
curred. The Heck Court did not consider such a suit, and the Heck
language was not meant to address it. Heck, properly understood, does
not preclude suits that only attempt to prevent future prosecutions.
4                    OLIVIER v. CITY OF BRANDON

                                  Syllabus

    Olivier’s suit to enjoin future prosecutions under the city ordinance, so
    he can return to the amphitheater, may proceed. Pp. 10–13.

    KAGAN, J., delivered the opinion for a unanimous Court.
                        Cite as: 607 U. S. ____ (2026)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     United States Reports. Readers are requested to notify the Reporter of
     Decisions, Supreme Court of the United States, Washington, D. C. 20543,
     pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 24–993
                                   _________________


     GABRIEL OLIVIER, PETITIONER v. CITY OF
             BRANDON, MISSISSIPPI
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                                [March 20, 2026]

  JUSTICE KAGAN delivered the opinion of the Court.
  Petitioner Gabriel Olivier was once convicted of violating
a city ordinance restricting expressive activity near a public
amphitheater. He now wishes to return to that venue to
voice his beliefs—but this time, without the threat of crim-
inal punishment. He therefore filed this suit, alleging that
the city ordinance infringes the First Amendment. The
suit, brought under 42 U. S. C. §1983, seeks an order de-
claring the ordinance unconstitutional and preventing its
enforcement in the future. The suit, in other words, re-
quests only forward-looking relief—nothing to do with Oliv-
ier’s prior conviction.
  The question presented here is whether this Court’s deci-
sion in Heck v. Humphrey, 512 U. S. 477 (1994), bars Oliv-
ier’s suit. The answer is no. Heck prohibits the use of §1983
to challenge the validity of a prior conviction or sentence so
as to obtain release from custody or monetary damages.
That decision has no bearing on Olivier’s suit seeking a
purely prospective remedy.
2               OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

                               I
   Olivier was convicted some five years ago for violating the
local ordinance he now challenges. Olivier is a street
preacher in Mississippi—a Christian who believes that
sharing his religious views with fellow citizens is an im-
portant part of exercising his faith. His vocation sometimes
took him to the sidewalks near an amphitheater in the City
of Brandon, where he could find sizable audiences attend-
ing events. Olivier was apparently not the only speaker at-
tracted to that area, and the activities there caused some
disruption. In 2019, the City adopted an ordinance requir-
ing all individuals or groups engaging in “protests” or
“demonstrations,” at around the time events were sched-
uled, to stay within a “designated protest area.” Supp. to
App. 70 (capitalization deleted). On his next trip to the am-
phitheater, in 2021, Olivier checked out that area, but
found it too remote for communicating his message. So he
returned, along with his signs and loudspeaker, to the side-
walk fronting the amphitheater. And there he was arrested
by the Brandon police chief for violating the city ordinance.
The next month, Olivier pleaded no contest in municipal
court. The court imposed a $304 fine; one year of probation;
and ten days of imprisonment, to be served only if, during
his probation, he again violated the ordinance. Olivier did
not appeal, paid the fine, and served no prison time.
   Because he still wanted to preach near the amphitheater,
Olivier’s next step was to file this lawsuit in federal court,
naming the City and its police chief as defendants. The suit
is brought under §1983, which authorizes claims against
state and local officials for the “deprivation of any rights”
secured by the Constitution. Olivier’s complaint alleges
that the city ordinance violates the Free Speech Clause of
the First Amendment by consigning him (and other speak-
ers) to the amphitheater’s out-of-the-way protest area. The
complaint seeks, as a remedy, a declaration that the ordi-
nance infringes his (and other speakers’) First Amendment
                     Cite as: 607 U. S. ____ (2026)                     3

                          Opinion of the Court

rights and an injunction preventing city officials from en-
forcing the ordinance in the future.1 In other words, the
relief requested is only prospective; Olivier seeks neither
the reversal of, nor compensation for, his prior conviction.
And Olivier has since made clear that he has no interest in
using a favorable judgment in this suit to later get his rec-
ord expunged or avoid his conviction’s collateral effects. See
Tr. of Oral Arg. 7. The suit is just meant to ensure that
Olivier may return to the amphitheater to speak without
fear of further punishment.
  The parties contested in the lower courts whether this
Court’s decision in Heck v. Humphrey bars the suit from go-
ing forward. On the City’s view of Heck, a person previously
convicted of violating a statute cannot challenge its consti-
tutionality under §1983 because success in the suit would
cast doubt on the prior conviction’s correctness. On Oliv-
ier’s contrary view, that rule is subject to two limitations,
either of which enables his suit to proceed. First, Olivier
contended, Heck does not preclude a suit seeking wholly
prospective relief, rather than relief relating to the prior
conviction. And second, Olivier argued, Heck does not apply
(regardless of the relief sought) when the person suing was
never in custody for his conviction, so never had a chance to
challenge it in federal habeas proceedings.2
——————
  1 Originally, Olivier also sought damages for the City’s prior enforce-

ment of the ordinance against him. But he abandoned that request as
the suit progressed, leaving only the above-described pleas for declara-
tory and injunctive relief.
  2 The premise of Olivier’s second argument is, of course, that he had

not been in custody following his conviction. That premise appears to be
wrong. Under his sentence, Olivier served a year of probation—indeed,
was still serving that time when he filed this suit. And a person on pro-
bation is generally “ ‘in custody’ for purposes of federal habeas corpus.”
Minnesota v. Murphy, 465 U. S. 420, 430 (1984); see Jones v. Cunning-
ham, 371 U. S. 236, 241–243 (1963). For whatever reason, though, the
City failed to raise that objection below, and both lower courts accepted
that Olivier was not put in custody for his conviction. See 2022 WL
4                 OLIVIER v. CITY OF BRANDON

                         Opinion of the Court

   The District Court agreed with the City’s understanding
of Heck, and the Court of Appeals for the Fifth Circuit af-
firmed on the same reasoning. If Olivier’s §1983 suit suc-
ceeded, the District Court reasoned, the judgment would
“undermine his Municipal Court conviction.” 2022 WL
15047414, *11 (SD Miss., Sept. 23, 2022). And so the suit
was categorically barred under Heck. Similarly, the Fifth
Circuit viewed Heck as precluding any §1983 claim that, if
successful, would “necessarily imply the invalidity of the
plaintiff ’s criminal conviction.” 2023 WL 5500223, *1 (Aug.
25, 2023); see Heck, 512 U. S., at 487 (using near-identical
language). Olivier’s claim, the court maintained, was of
that sort: If he showed that the city ordinance violated the
First Amendment, he also would show that his prior convic-
tion should not have happened. And that fact, the court
concluded, was dispositive. It did not matter whether Oliv-
ier’s conviction had landed him in custody. See 2023 WL
5500223, *4. Nor did it matter whether Olivier’s suit
sought only prospective relief. See ibid.
   The Fifth Circuit denied rehearing en banc, but eight (of
seventeen) judges dissented. Those judges understood Heck
to bar only the “retrospective use of [§1983] to collaterally
attack criminal convictions.” 121 F. 4th 511, 514 (2024)
(Oldham, J., dissenting) (emphasis in original). A suit like
Olivier’s for “prospective injunctive relief,” the dissenters
argued, is not precluded because granting a “forward-
looking injunction” neither “invalidate[s]” nor “impose[s]
tort liability” for a prior conviction. Id., at 514–515; see id.,
at 513 (Ho, J., dissenting) (similar). The dissenters noted
that the Court of Appeals for the Ninth Circuit had adopted
their view, which meant there was now a Circuit split about

——————
15047414, *10 (SD Miss., Sept. 23, 2022); 2023 WL 5500223, *4 (CA5,
Aug. 25, 2023). Given that the case has proceeded so far on that basis,
we treat any contrary argument as forfeited and proceed in the same
way.
                     Cite as: 607 U. S. ____ (2026)                    5

                          Opinion of the Court

Heck’s proper reach. 121 F. 4th, at 515 (Oldham, J., dis-
senting) (citing Martin v. Boise, 920 F. 3d 584, 614 (2019)).
   We granted certiorari, 606 U. S. 959 (2025), to consider
the two independent reasons Olivier offered below for why
his suit escapes the so-called Heck bar: that he was never
in custody for his prior conviction, and that he now seeks
purely prospective relief. See Pet. for Cert. i. We need not
address the former reason today because we agree with
Olivier (and the Fifth Circuit’s dissenting judges) on the lat-
ter. Given that Olivier asked for only a forward-looking
remedy—an injunction stopping officials from enforcing the
city ordinance in the future—his suit can proceed, notwith-
standing his prior conviction.3 Heck, properly understood,
does not say otherwise.
                             II
  Before our decision in Heck, the City would have had no
plausible basis for claiming Olivier’s suit is barred. That
type of suit, as no one here disputes, falls within §1983’s
heartland: Assuming a credible threat of prosecution, a
plaintiff may bring a §1983 action to challenge a local law
as violating the Constitution and to prevent that law’s fu-
ture enforcement. See, e.g., Steffel v. Thompson, 415 U. S.
452 (1974). And a half-century ago, in Wooley v. Maynard,
430 U. S. 705 (1977), this Court held that rule to apply even
when the plaintiff (like Olivier) was previously convicted
under the challenged law.

——————
   3 In reaching that holding, we do not say that every person can chal-

lenge his statute of conviction through a §1983 suit for wholly prospec-
tive relief. The Government, appearing here as amicus curiae, urges us
to reserve the issue whether a person may bring such a suit while he is
in custody for violating the statute challenged. See Tr. of Oral Arg. 41–
42, 46–47; see also Brief for United States 27 (positing why that circum-
stance might matter). We think it appropriate to do so because, as we
have explained, our assumption here is that Olivier was never in custody.
See supra, at 3–4, n. 2.
6               OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

   For anyone who has followed along this far, a description
of Wooley should strike a chord. George Maynard viewed
the “Live Free or Die” motto on his New Hampshire license
plate as “repugnant to [his] moral and religious beliefs.”
Id., at 707. So he covered those words with reflective tape,
in violation of a state statute. Maynard was convicted for
that conduct three times over in state court, receiving
(mostly suspended) sentences involving small fines and
short jail terms. After the last proceeding had concluded—
and presumably anxious that there not be a fourth—
Maynard brought a §1983 suit in federal court, seeking a
declaration that the state statute violated the First Amend-
ment and an injunction to prevent its future enforcement.
New Hampshire argued, as its front line of defense, that the
suit was precluded “because [Maynard] has already been
subjected to prosecution” under the challenged law. Id., at
712, n. 9. Our decision in Heck had not yet issued. Instead,
New Hampshire relied on “Younger principles,” which cau-
tion against federal interference with state-court proceed-
ings. Ibid.; see Younger v. Harris, 401 U. S. 37 (1971).
Those principles would be offended, New Hampshire
claimed, if a federal court were to enjoin the enforcement of
a state law at the behest of someone earlier convicted under
it in state court.
   This Court rejected New Hampshire’s argument on the
ground that Maynard’s suit sought only to prevent “further
prosecution” under the New Hampshire statute. Wooley,
430 U. S., at 711. The suit, the Court explained, was “in no
way designed to annul the results of a state trial” (as indeed
would have been troubling under Younger doctrine). 430
U. S., at 711. Maynard had “already sustained [his] convic-
tions” and “served [his] sentence[s].” Ibid. And he did “not
seek to have his record expunged, or to annul any collateral
effects” his convictions might have—for example, “upon his
driving privileges.” Ibid. Rather, Maynard sought “wholly
prospective” relief: He wanted “only to be free from
                  Cite as: 607 U. S. ____ (2026)            7

                      Opinion of the Court

prosecutions for future violations of the same” (allegedly
unconstitutional) statute. Ibid. Because that was so, the
Court held, §1983 provided an avenue to bring his claim.
See id., at 710. Were it otherwise, the Court reasoned,
Maynard would have no good way to vindicate his First
Amendment rights: He would be trapped “between the
Scylla of intentionally flouting state law and the Charybdis
of forgoing what he believes to be constitutionally protected
activity” so as to avoid yet another criminal prosecution.
Ibid.
   All of that could as easily be said of Olivier’s suit. Like
Maynard, Olivier was convicted under the statute he now
alleges to violate the First Amendment. But also like
Maynard, Olivier did not seek in his §1983 suit to upset that
conviction, or even to avert its collateral effects. Rather,
Olivier sought “wholly prospective” relief—an injunction to
preclude “further prosecution” under the law he had earlier
broken. Id., at 711. If not able to bring such a suit, Olivier
would face the same untenable choice as Maynard: violate
the law and suffer the consequences (the Scylla), or else give
up what he takes to be his First Amendment rights (the
Charybdis). See id., at 710. Our decision in Wooley, taken
alone, would thus defeat the City’s attempt to prevent Oliv-
ier’s suit from going forward.
   Some two decades later, though, the Court encountered
Heck v. Humphrey, which the City now argues requires the
opposite result. Roy Heck had been convicted in state court
of manslaughter, and was serving a fifteen-year prison sen-
tence. While his appeal was pending, he filed a §1983 suit
in federal court naming two prosecutors and a police inves-
tigator as defendants. Heck alleged that they had commit-
ted misconduct, such as destroying exculpatory evidence, to
gain his conviction. He sought as a remedy monetary “dam-
ages attributable to [his] unconstitutional conviction.” 512
U. S., at 489–490. The question raised was whether §1983
allowed the suit.
8               OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

   The Court held it did not. The Court took as settled that
Heck could not have used §1983 to “challenge[ ] the fact or
duration of his confinement and seek[ ] immediate or speed-
ier release” from custody. Id., at 481 (citing Preiser v. Ro-
driguez, 411 U. S. 475, 488–490 (1973)). A claim of that
sort, the Court noted, “must be brought in habeas corpus
proceedings.” Heck, 512 U. S., at 481. And so too, the Court
held, Heck could not use §1983 to seek damages deriving
from a conviction, unless it had already been overturned.
See id., at 486–487. To be sure, Heck could not get damages
by way of a habeas action. See id., at 481. But in suing for
them under §1983, Heck was in truth mounting a “collat-
eral attack” on the validity of his conviction, and thus in-
truding on the habeas statute’s domain. Id., at 485. Such
a suit could lead to “parallel litigation” respecting “the is-
sues of probable cause and guilt.” Id., at 484. And it could
give rise to “conflicting” judgments about the same conduct,
with the §1983 suit suggesting that Heck should be re-
leased even as criminal or habeas proceedings found the op-
posite. Ibid. Hence the Heck bar on “§1983 damages ac-
tions that necessarily require the plaintiff to prove the
unlawfulness of his conviction or confinement.” Id., at 486.
“[W]hen a state prisoner seeks damages in a §1983 suit,”
the Court went on, “the district court must consider
whether a judgment in favor of the plaintiff would neces-
sarily imply the invalidity of his conviction or sentence.”
Id., at 487. A judgment for Heck would have done so, for
his success rested on proof discrediting his conviction. His
§1983 suit therefore could not go forward.
   In two later decisions, though, the Court drew a line be-
tween Heck-type claims and those seeking forward-looking
relief. In Edwards v. Balisok, 520 U. S. 641 (1997), a state
prisoner alleged that procedures used in a disciplinary
hearing—which had deprived him of good-time credits and
thus lengthened his sentence—violated his Fourteenth
Amendment due process rights. He sought money damages
                  Cite as: 607 U. S. ____ (2026)              9

                      Opinion of the Court

for the alleged past violation; he also sought an injunction
requiring prison officials to adopt new procedures, so as to
“prevent future violations.” Id., at 643. The Court made
short work of the claim for damages. As in Heck, the Court
reasoned, the prisoner could not obtain damages without
demonstrating “the invalidity of the punishment imposed”
on him (i.e., the loss of his good-time credits), and thus im-
pinging on habeas. 520 U. S., at 648. But the claim for
“prospective injunctive relief ”—the use of fairer procedures
in the future—was a different thing. Said the Court: “Or-
dinarily, a prayer for such prospective relief ” may “properly
be brought under §1983,” because it does not depend on
showing the “invalidity of a previous” sentencing decision.
Ibid. Likewise, in Wilkinson v. Dotson, 544 U. S. 74, 77
(2005), the Court allowed state prisoners to bring a §1983
suit alleging that existing parole procedures violated the
Due Process Clause and requesting an injunction that the
State “comply with constitutional” requirements “in the fu-
ture.” That claim for “future relief,” the Court determined,
was “distant” from “the core of habeas” and so not barred by
Heck. 544 U. S., at 82 (emphasis in original).
   The same is true of Olivier’s suit. Olivier is not challeng-
ing the “validity of [his] conviction or sentence,” for the pur-
pose either of securing (or speeding) release or of obtaining
monetary damages. Nance v. Ward, 597 U. S. 159, 167–168
(2022). Instead, Olivier is seeking (in Wooley’s words)
“wholly prospective” relief—“only to be free from prosecu-
tions for future violations” of the city ordinance. 430 U. S.,
at 711. And that request, as Balisok and Dotson recognized,
falls outside habeas’s core—and likewise outside Heck’s
concerns. See 520 U. S., at 648; 544 U. S., at 82. Olivier’s
suit does not, as habeas suits do, “collateral[ly] attack” the
old conviction. Heck, 512 U. S., at 485. It thus cannot give
rise, as Heck feared, to “parallel litigation” respecting his
prior conduct. Id., at 484. Nor does it risk “conflicting”
judgments over how that conduct was prosecuted or
10              OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

punished. Ibid. The suit, after all, is not about what Olivier
did in the past, and depends on no proof addressed to his
prior conviction. Unlike in Heck, the suit merely attempts
to prevent a future prosecution. So the Heck bar does not
come into play.
  The City’s main argument to the contrary (echoing the
decisions below) rests on one sentence of our Heck opinion.
That supposedly dispositive line states: “[W]hen a state
prisoner seeks damages in a §1983 suit, the district court
must consider whether a judgment in favor of the plaintiff
would necessarily imply the invalidity of his conviction or
sentence; if it would, the complaint must be dismissed” (un-
less the conviction has already been invalidated). Id., at
487; see supra, at 8. Of course, Olivier does not “seek[ ]
damages” in his §1983 suit, but the City points out that sev-
eral post-Heck decisions dropped the sentence’s prefatory
phrase while repeating the rest. See, e.g., Dotson, 544 U. S.,
at 81–82; Skinner v. Switzer, 562 U. S. 521, 533–534 (2011).
And in the City’s view, that modified inquiry suggests that
the Heck bar should apply to Olivier’s suit. That is because,
the City says, a judgment in Olivier’s favor would “neces-
sarily imply the invalidity of [his] prior conviction[ ].” Brief
for Respondent 33. To declare the city ordinance unconsti-
tutional, as Olivier seeks, would be to imply that no one—
including Olivier—should have been convicted under that
law.
  The argument is a fair one, but hardly dispositive. We
have to agree that if Olivier succeeds in this suit, it would
mean his prior conviction was unconstitutional. So, strictly
speaking, the Heck language fits. But that could just show
that the phrasing was not quite as tailored as it should have
been. This Court has often cautioned that “general lan-
guage in judicial opinions should be read as referring in
context to circumstances similar to the circumstances then
before the Court and not referring to quite different circum-
stances that the Court was not then considering.” Turkiye
                  Cite as: 607 U. S. ____ (2026)           11

                      Opinion of the Court

Halk Bankasi A.S. v. United States, 598 U. S. 264, 278
(2023) (quoting Illinois v. Lidster, 540 U. S. 419, 424
(2004)). The City’s argument raises the question whether
that is true here.
   We think, with the benefit of hindsight, that it is—that
the sentence relied on swept a bit too broad. That language
was used in Heck to identify claims that were really as-
saults on a prior conviction, even though involving some in-
direction. One example was found in Heck itself: a claim
seeking not straightforward reversal of a conviction (and
release from custody), but damages attributable to that con-
viction, requiring proof that police misconduct made it in-
valid. Another example Heck offered was yet further atten-
uated. See 512 U. S., at 486–487, n. 6. A person convicted
of resisting arrest—defined as preventing an officer from
effecting a lawful arrest—brings a §1983 action for dam-
ages against the arresting officer for violation of his Fourth
Amendment right not to be unreasonably seized. The dam-
ages sought, unlike in Heck, are not attributable to his con-
viction (for resisting arrest); they are damages deriving only
from the underlying arrest. Still, a “§1983 action will not
lie” because the plaintiff, to prevail, “would have to negate
an element of the offense of which he has been convicted”—
i.e., that the underlying arrest was “lawful.” Ibid. Once
again, the suit requires looking back to conduct involved in
a prior conviction, and offering contradictory proof. By con-
trast, there is no looking back in Olivier’s suit. Both in the
allegations made, and in the relief sought, the suit is all
future-oriented—even if, as a kind of byproduct, success in
it shows that something past should not have occurred. The
Heck Court did not consider such a suit, and the Heck lan-
guage was not meant to address it.
   Proof positive comes from the logical—but wholly unten-
able—consequences of the City’s position. Suppose that af-
ter Olivier’s conviction, another citizen brings a §1983 suit
to enjoin the city ordinance so that he can speak outside the
12              OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

amphitheater. Let’s name this citizen Laurence and say
that he boasts a clean police record. Would Heck allow Lau-
rence’s suit to proceed? See 121 F. 4th, at 514 (Oldham, J.,
dissenting) (offering a similar hypothetical). The very ques-
tion seems ludicrous: No one would say Heck poses a bar.
But under the City’s logic, it should—because here, too,
Heck’s language fits. The hypothetical suit—no less than
Olivier’s own—would, if successful, “necessarily imply the
invalidity” of Olivier’s conviction (as well as all other con-
victions under the statute). 512 U. S., at 487. A judgment
in that suit too would demonstrate, and in just the same
way, that Olivier’s conviction was unconstitutional. The
hypothetical thus shows that the “necessarily imply” lan-
guage cannot extend as far as the City wants. Contra the
City’s logic, the Heck language does not preclude Laurence’s
§1983 suit because, rather than challenging a prior convic-
tion, that suit only attempts to prevent future ones. And
contra the City’s actual position, the language does not pre-
clude Olivier’s §1983 suit for the identical reason—because,
as explained above, it looks forward only. See supra, at 9–
10.
   With Heck thus out of the way, Wooley returns to center
stage. Recall the Court held in that case that Maynard
could sue under §1983 to prevent future enforcement of an
allegedly unconstitutional statute, despite a prior convic-
tion under that law. See supra, at 6–7. The same rule al-
lows Olivier to sue under §1983 to enjoin future prosecu-
tions under the city ordinance, despite his prior conviction.
Were that not so, Olivier would face the same dilemma as
Maynard: flout the law and risk another prosecution, or else
forgo speech he believes is constitutionally protected. See
Wooley, 430 U. S., at 710; supra, at 7. We declined to put
Maynard to that choice, and we will not put Olivier to it
either. His suit to enjoin the ordinance, so he can return to
the amphitheater, may proceed.
                Cite as: 607 U. S. ____ (2026)                 13

                    Opinion of the Court

  We accordingly reverse the judgment of the Court of Ap-
peals and remand the case for further proceedings con-
sistent with this opinion.
                                                 It is so ordered.

```

---

## GROUP: content/cases/People v. Hughes.md  (`case`, 4 assertions)

### content_page

```
---
title: "People v. Hughes"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: Michigan Supreme Court
court_level: state
circuit: ""
year: 2020
date_decided: 2020-12-28
docket: 158652
authority_weight: "Persuasive — state, illustrative"
treatment:
  field_i_validity: good_law
  as_of_content: 2020-12-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: People v. Hughes
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4843477/people-of-michigan-v-kristopher-allen-hughes/"
  cluster_id: 4843477
  opinion_id: 4647256
  identity_checked: false
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Progeny / Refinement"
related: ["[[Riley v. California]]", "[[Carpenter v. United States]]", "[[Horton v. California]]", "[[Coolidge v. New Hampshire]]"]
aliases: ["People of Michigan v. Hughes", "People v Hughes", "People v. Hughes (Mich. 2020)"]
tags: ["case", "fourth-amendment", "plain-view", "digital-search", "cell-phone", "warrant-scope", "michigan", "state-supreme"]
holding: "Declines a per se rule that an officer may always review the ENTIRE contents of digital data seized under a warrant on the mere…"
lake:
  record_id: People v. Hughes
  status: under_review
  projected_at: 2026-07-09
---

# People v. Hughes

*506 Mich. 512, 958 N.W.2d 98 (2020)* · Michigan Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Hughes's cell phone was seized and its data extracted pursuant to a warrant authorizing a search for evidence of **drug trafficking**. About a month later, the prosecutor in a separate **armed-robbery** case asked a detective to search the same data for the robbery victims' names and phone numbers; that search turned up calls and texts tying Hughes to the robbery. Convicted of armed robbery, Hughes argued the robbery evidence exceeded the drug-trafficking warrant.

## Issue
Whether officers violated the Fourth Amendment by searching lawfully seized cell-phone data for evidence of a different crime (armed robbery) than the one for which the warrant issued (drug trafficking).

## Rule
A warrant to search digital data authorizes review only to the extent reasonably consistent with the warrant's scope; there is no [[Common Legal Terms#per-se|per se]] rule permitting review of the entire contents. "We hold that, as with any other search, an officer must limit a search of digital data from a cell phone in a manner reasonably directed to uncover evidence of the criminal activity alleged in the warrant." — *People v. Hughes*, 506 Mich. 512 (slip op., at 36–37). ^pin-36

Officers must "reasonably limit the scope of their searches to evidence related to the criminal activity alleged in the warrant and not employ that authorization as a basis for seizing and searching digital data in the manner of a general warrant in search of evidence of any and all criminal activity." — *Id.* (slip op., at [35–36](https://www.courtlistener.com/opinion/4843477/people-of-michigan-v-kristopher-allen-hughes/#:~:text=reasonably%20limit%20the%20scope%20of)). ^pin-35

## Application
The warrant authorized searching Hughes's phone data only for evidence of drug trafficking. The later search — run for the robbery victims' names and phone numbers — was reasonably directed at the armed-robbery investigation, not the drug-trafficking activity alleged in the warrant, and so exceeded the warrant's scope and was a search presumptively invalid. The Court reversed the Court of Appeals and [[Reading and Citing Cases#on-remand|remanded]] (leaving the exclusionary-rule and ineffective-assistance questions to be developed below).

## Conclusion
Searching the seized cell-phone data for evidence of a crime outside the warrant's scope exceeded the warrant; the Court of Appeals was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Persuasive — state, illustrative** (Michigan Supreme Court, unanimous). A leading state application of [[Riley v. California]] to the scope of warranted cell-phone-data searches.

## Appears on
- [[Plain View Doctrine]] — *Key — Progeny / Refinement*

## Sources
- *People v. Hughes*, 506 Mich. 512, 958 N.W.2d 98 (2020) — https://www.courtlistener.com/opinion/4843477/people-of-michigan-v-kristopher-allen-hughes/ — pinpoints: slip op., at 35–37 (CL carries the slip opinion; cluster 4843477 → lead opinion 4647256).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "36cfca4fbbe903b8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Declines a per se rule that an officer may always review the ENTIRE contents of digital data seized under a warrant on the mere…", "title": "People v. Hughes"}}
{"assertion_id": "5b97e74a110fcae5", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key — Progeny / Refinement", "title": "People v. Hughes"}}
{"assertion_id": "1811ae5e7d9db97f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Persuasive — state, illustrative", "title": "People v. Hughes"}}
{"assertion_id": "dcd8645cd831104e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2020-12-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "People v. Hughes", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "People v. Hughes", "varies_by_point": "false"}}
```

### lake record — People v. Hughes

```json
{
  "schema_version": "s2.v1",
  "record_id": "People v. Hughes",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "People of Michigan v. Kristopher Allen Hughes",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "People v. Hughes",
    "court": "Michigan Supreme Court",
    "court_id": "mich",
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "2020-12-28",
    "year": 2020,
    "docket": "158652",
    "cluster_id": 4843477,
    "lead_opinion_id": 4647256,
    "sibling_ids": [
      4647256
    ],
    "absolute_url": "/opinion/4843477/people-of-michigan-v-kristopher-allen-hughes/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4765075,
        "score": 10,
        "case_name": "People of Michigan v. Howard Hughes III"
      },
      {
        "cluster_id": 4760961,
        "score": 10,
        "case_name": "People of Michigan v. Kristopher Allen Hughes"
      },
      {
        "cluster_id": 4760166,
        "score": 10,
        "case_name": "People v. Hughes"
      },
      {
        "cluster_id": 4736131,
        "score": 10,
        "case_name": "People of Michigan v. Kristopher Allen Hughes"
      },
      {
        "cluster_id": 4724607,
        "score": 10,
        "case_name": "People of Michigan v. Kristopher Allen Hughes"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
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
      "id": "pin-36",
      "page": null,
      "quote": "--- # People v. Hughes *506 Mich. 512, 958 N.W.2d 98 (2020)* \u00b7 Michigan Supreme Court \u00b7 **Persuasive \u2014 state, illustrative** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Hughes's cell phone was seized and its data extracted pursuant to a warrant authorizing a search for evidence of **drug trafficking**. About a month later, the prosecutor in a separate **armed-robbery** case asked a detective to search the same data for the robbery victims' names and phone numbers; that search turned up calls and texts tying Hughes to the robbery. Convicted of armed robbery, Hughes argued the robbery evidence exceeded the drug-trafficking warrant. ## Issue Whether officers violated the Fourth Amendment by searching lawfully seized cell-phone data for evidence of a different crime (armed robbery) than the one for which the warrant issued (drug trafficking). ## Rule A warrant to search digital data authorizes review only to the extent reasonably consistent with the warrant's scope; there is no per se rule permitting review of the entire contents.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-35",
      "page": null,
      "quote": "reasonably limit the scope of their searches to evidence related to the criminal activity alleged in the warrant and not employ that authorization as a basis for seizing and searching digital data in the manner of a general warrant in search of evidence of any and all criminal activity.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 89254,
      "fragment": "#:~:text=reasonably%20limit%20the%20scope%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2020-12-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "People v. Hughes",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4647256) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR mich OR michctapp)",
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
        "query": "cites:(4647256)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4647256)",
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
    "complete_query": "cites:(4647256)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4647256,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/people-v-hughes.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4647256,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 172097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 172511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 775977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 805906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 873669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 931473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 1030766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 1031286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 1063250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 1463336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 2338228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 2410945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 2680439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 2802125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 3182448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 3216391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 3219245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 3219311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 4152183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 4178638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 4188910,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 4243049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 4386662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 4396329,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 4398009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 4543707,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 6185132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 8137990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 8246904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 8250950,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 8698406,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9422279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9423434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9423459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9425474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9425658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9426530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9426913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9429232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9429344,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9429558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9430614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9430836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9432041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9432823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9434540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9434968,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9435359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9484912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9492053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9495475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9503043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9504435,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9504455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9504706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9514235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9524176,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9669839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9689602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9819859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9820534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9841975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9853591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9883113,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4647256,
        "cited_id": 9889094,
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
    "date_created": "2026-07-05T17:05:18Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: no_official_class_citation",
      "legacy treatment migrated: good -> good_law",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:07:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:07:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T13:38:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:07:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — People v. Hughes

```
                                                                                      Michigan Supreme Court
                                                                                            Lansing, Michigan




Syllabus
                                                             Chief Justice:               Justices:
                                                              Bridget M. McCormack        Stephen J. Markman
                                                                                          Brian K. Zahra
                                                             Chief Justice Pro Tem:
                                                                                          Richard H. Bernstein
                                                              David F. Viviano            Elizabeth T. Clement
                                                                                          Megan K. Cavanagh

This syllabus constitutes no part of the opinion of the Court but has been                Reporter of Decisions:
prepared by the Reporter of Decisions for the convenience of the reader.                  Kathryn L. Loomis



                                             PEOPLE v HUGHES

           Docket No. 158652. Argued on application for leave to appeal October 7, 2020. Decided
      December 28, 2020.

              Following a jury trial, Kristopher A. Hughes was convicted in the Oakland Circuit Court,
      Hala Jarbou, J., of armed robbery, MCL 750.529, and was sentenced as a fourth-offense habitual
      offender, MCL 769.12, to 25 to 60 years in prison. On the evening of August 6, 2016, Ronald
      Stites was at his home with Lisa Weber, whom he had met earlier that day. Weber had agreed to
      spend the night with Stites and perform sexual acts in exchange for money. At some point during
      the evening, Weber called a drug dealer known as “K-1” or “Killer” in order to obtain drugs and
      asked him to come to Stites’s residence. A man arrived at the residence, sold Stites and Weber
      crack cocaine, and departed. Later that night, the drug seller returned to Stites’s home with a gun
      and stole a safe that was located in Stites’s bedroom. Weber later identified defendant as the drug
      dealer and robber, but Stites was not able to identify the perpetrator. A detective submitted a
      warrant affidavit to search defendant’s property for evidence related to separate allegations of drug
      trafficking. The affidavit included information from a criminal informant that defendant and
      another man were dealing drugs, and the detective asserted that drug traffickers commonly use
      mobile phones and other electronic equipment in the course of their activities. The district court,
      Cynthia Thomas Walker, J., concluded that there was sufficient probable cause to support a search
      warrant and authorized a warrant to search three properties and a vehicle connected with defendant.
      While executing a search at one of the addresses identified in the warrant, the police detained
      defendant and seized a cell phone found on his person. Another detective performed a forensic
      examination of the phone and extracted all of the phone’s data. The extraction software separated
      the data into categories, including photographs, call logs, and text messages. According to the
      detective, the software also enabled police to search the data for search terms or specific phone
      numbers. About a month after the data was extracted, the prosecutor in the armed-robbery case
      against defendant asked the detective to conduct a second search of defendant’s cell-phone data
      for contacts with the phone numbers of Stites and Weber; for the names “Lisa,” “Kris,” or
      “Kristopher”; and for the word “killer.” These searches revealed several calls and text messages
      between defendant and Weber on the night that Stites was robbed, including text messages from
      Weber to defendant indicating the location of Stites’s home, that the home was unlocked, and that
      it had a flat-screen TV. After his conviction, defendant appealed, arguing that the phone records
      should have been excluded from the trial because the warrant that authorized the search of his
      phone’s data permitted officers to search for evidence of drug trafficking, not armed robbery.
      Defendant also argued that trial counsel was ineffective for failing to object to the admission of
the data on Fourth Amendment grounds. The Court of Appeals, TUKEL, P.J., and BECKERING and
SHAPIRO, JJ., rejected these arguments and affirmed defendant’s conviction in an unpublished per
curiam opinion. Defendant sought leave to appeal in the Supreme Court, which ordered oral
argument on the application. 505 Mich 855 (2019).

       In a unanimous opinion by Justice MARKMAN, the Supreme Court, in lieu of granting leave
to appeal, held:

        1. The Fourth Amendment of the United States Constitution protects against unreasonable
searches and seizures. Although a warrant is not always required before a search or seizure, there
is a strong preference for searches conducted pursuant to a warrant, and the general rule is that
police officers must obtain a warrant for a search to be reasonable under the Fourth Amendment.
Under Riley v California, 573 US 373 (2014), general Fourth Amendment principles apply with
equal force to searches of cell-phone data. In this case, the issue was whether officers violated the
Fourth Amendment when they searched defendant’s cell phone for evidence of armed robbery
without obtaining a new warrant when the phone was seized pursuant to a warrant authorizing the
search of the phone’s data for evidence of drug trafficking. The prosecutor argued that defendant
lost the reasonable expectation of privacy in his cell-phone data when the phone was seized and
the data was searched pursuant to the drug-trafficking warrant. However, under Riley, citizens
generally maintain a reasonable expectation of privacy in their cell-phone data that is not
extinguished merely because a phone is seized during a lawful arrest. Further, the seizure and
search of cell-phone data pursuant to a warrant does not extinguish an otherwise reasonable
expectation of privacy in the entirety of the seized data. Rather, a warrant authorizing the police
to seize and search cell-phone data allows officers to examine the seized data only to the extent
reasonably consistent with the scope of the warrant. In this case, the warrant authorized officers
to search defendant’s cell-phone data for evidence of drug trafficking as described by the warrant
and affidavit. Any further review of the data beyond the scope of the warrant constituted a search
that was presumptively invalid under the Fourth Amendment.

        2. In considering the Fourth Amendment’s requirements for a search of digital data
authorized by a warrant, as with any other search conducted pursuant to a warrant, a search of
digital data must be reasonably directed at uncovering evidence of the criminal activity alleged in
the warrant. Any search that is directed instead toward finding evidence of other, unrelated
criminal activity is beyond the scope of the warrant. Under the Fourth Amendment, a warrant
must state with particularity not only the items to be searched and seized, but also the alleged
criminal activity justifying the warrant. Although the prosecutor argued that the search for
evidence of armed robbery fell within the scope of the warrant because the warrant authorized
officers to review the entire report that represented the totality of defendant’s cell-phone data, the
warrant authorized a search of the data for evidence of drug trafficking, not armed robbery.
Moreover, the affidavit supporting the warrant did not even mention armed robbery, let alone seek
to establish probable cause that defendant committed that offense. While officers are not required,
when executing a search of digital data, to review only digital content that a suspect has identified
as pertaining to criminal activity, neither is it always reasonable for an officer to review the entirety
of the seized digital data on the basis that incriminating information could conceivably be found
anywhere on the device. Accordingly, an officer’s search of seized digital data must be reasonably
directed toward finding evidence of the criminal activity identified in the warrant. In this case,
about a month after officers searched defendant’s digital data for evidence of drug trafficking, the
prosecutor in the armed-robbery case asked a detective to conduct a focused search of the data for
terms pertaining to the armed-robbery case. There was no evidence that a search for these terms
would uncover evidence relating to defendant’s drug-trafficking activity, nor was there any
evidence that defendant hid or manipulated his data to conceal evidence related to drug trafficking.
Therefore, the second search of the data was not reasonably directed toward obtaining evidence of
drug trafficking and exceeded the scope of the warrant. Accordingly, the second review of the
data constituted a warrantless search that violated the Fourth Amendment, and the case had to be
remanded to the Court of Appeals for that Court to reconsider defendant’s claim of ineffective
assistance of counsel and to determine whether defendant was entitled to relief.

       Reversed and remanded.

        Justice VIVIANO, concurring, agreed with the majority that the second search of defendant’s
cell-phone data was unlawful under the Fourth Amendment but wrote separately to emphasize his
view that a law enforcement officer’s subjective intent when searching seized digital data should
be included as a potentially dispositive factor when a court considers whether a search was
reasonably directed at finding evidence of the criminal activity identified in the warrant. Justice
VIVIANO argued that if the search was purposefully conducted to obtain evidence of a crime other
than the one identified in the warrant, a court could not conclude that the search was reasonably
directed at uncovering evidence of the criminal activity alleged in the warrant. In this case, Justice
VIVIANO would find this factor dispositive since it was clear that the second search of defendant’s
cell-phone data was conducted to obtain evidence of a crime other than drug trafficking, the offense
identified in the warrant. Therefore, before conducting the second search of defendant’s cell
phone, the officer should have obtained a second search warrant directed toward obtaining
evidence of the armed-robbery offense. Because he did not, the second search was unlawful.




                                     ©2020 State of Michigan
                                                                           Michigan Supreme Court
                                                                                 Lansing, Michigan



OPINION
                                                  Chief Justice:                 Justices:
                                                   Bridget M. McCormack          Stephen J. Markman
                                                                                 Brian K. Zahra
                                                  Chief Justice Pro Tem:         Richard H. Bernstein
                                                   David F. Viviano              Elizabeth T. Clement
                                                                                 Megan K. Cavanagh


                                                               FILED December 28, 2020



                             STATE OF MICHIGAN

                                     SUPREME COURT


  PEOPLE OF THE STATE OF MICHIGAN,

               Plaintiff-Appellee,

  v                                                                No. 158652

  KRISTOPHER ALLEN HUGHES,

               Defendant-Appellant.


 BEFORE THE ENTIRE BENCH

 MARKMAN, J.
       The issue presented here is whether, when the police obtain a warrant to search

 digital data from a cell phone for evidence of a crime, they are later permitted to review

 that same data for evidence of another crime without obtaining a second warrant. We

 conclude-- in light of the particularity requirement embodied in the Fourth Amendment

 and given meaning in the United States Supreme Court’s decision in Riley v California,

 573 US 373; 134 S Ct 2473; 189 L Ed 2d 430 (2014) (addressing the “sensitive” nature of

 cell-phone data)-- that a search of digital cell-phone data pursuant to a warrant must be
reasonably directed at obtaining evidence relevant to the criminal activity alleged in that

warrant. Any search of digital cell-phone data that is not so directed, but instead is directed

at uncovering evidence of criminal activity not identified in the warrant, is effectively a

warrantless search that violates the Fourth Amendment absent some exception to the

warrant requirement.     Here, the officer’s review of defendant’s cell-phone data for

incriminating evidence relating to an armed robbery was not reasonably directed at

obtaining evidence regarding drug trafficking-- the criminal activity alleged in the warrant--

and therefore the search for that evidence was outside the purview of the warrant and thus

violative of the Fourth Amendment. Accordingly, we reverse the judgment of the Court

of Appeals and remand to that Court to determine whether defendant is entitled to relief

based upon the ineffective assistance of counsel.1

                                  I. FACTS & HISTORY

       The circumstances of this case arise from concurrent criminal prosecutions against

defendant Kristopher Hughes, one related to drug trafficking and the other related to armed

robbery. MCL 750.529. Defendant pleaded no contest to the drug-trafficking charges and




1
  Because we conclude that the Fourth Amendment was breached when officers searched
a cell phone for evidence of armed robbery without having obtained a second warrant when
the phone had been seized based upon a warrant for drug trafficking, we need not decide
(a) whether the warrant affidavit sufficiently connected defendant’s cell phone to his drug
trafficking or (b) the broader question as to what evidence set forth in an affidavit
sufficiently connects a cell phone to alleged criminal activity to support the issuance of a
warrant to search the phone’s digital contents. We only address the proper manner of
searching digital data when such data has been seized pursuant to a valid warrant.



                                              2
these pleas are not the subject of this appeal.2 Defendant went to trial on the armed-robbery

charge, and after two mistrials due to hung juries, he was convicted of the armed robbery

of Ronald Stites.

       On August 6, 2016, Stites was going for a walk when he met Lisa Weber. The two

talked, and Stites invited Weber back to his home. At Stites’s residence, Weber offered to

stay with Stites all night and to perform sexual acts in exchange for $50. Stites agreed, and

Weber followed him into his bedroom, where he opened a safe containing $4,200 in cash

and other items and pulled out a $50 bill that he agreed to give her after the night was over.

Stites then performed oral sex on Weber. Afterward, Weber went to the store to get

something to drink. Approximately 15–20 minutes later, she called a drug dealer, who

went by the name of “K-1” or “Killer,” and asked that he come over and sell drugs to her

and Stites. Sometime thereafter, a man arrived at Stites’s home, sold Weber and Stites

crack cocaine, and then departed. Weber and Stites consumed some of the drugs and

continued their sexual activities. Later in the evening, the man who had sold the drugs

returned to the home with a gun and stole Stites’s safe at gunpoint. Stites testified that

Weber assisted in the robbery and departed the home with the robber, while Weber asserted


2
  On February 2, 2017, defendant pleaded no contest to two counts of delivery and
manufacture of a controlled substance, second or subsequent offense, MCL
333.7401(2)(b)(ii), possession of marijuana, MCL 333.7403(2)(d), possession of
suboxone, MCL 333.7403(2)(b)(ii), possession of alprazolam, MCL 333.7403(2)(b)(ii),
and possession of dihydrocodeine pills, MCL 333.7403(2)(b)(ii), as a habitual fourth
offender. He was sentenced to concurrent prison terms of 36 months to 30 years, 12 to 24
months, and 24 months to 15 years. Defendant appealed and the Court of Appeals denied
his application for lack of merit. People v Hughes, unpublished order of the Court of
Appeals, entered September 28, 2017 (Docket No. 339858). Defendant did not seek leave
to appeal in this Court.


                                              3
that she did not assist in the robbery and only complied with the robber’s demands to avoid

being harmed. Weber identified defendant as the perpetrator, while Stites could not

identify defendant as the perpetrator.

       On August 11, 2016, Detective Matthew Gorman submitted a warrant affidavit to

search defendant’s property for evidence related to separate criminal allegations of drug

trafficking.   Detective Gorman’s affidavit included information from a confidential

informant that defendant and an associate named Patrick Pankey were dealing drugs. The

warrant affidavit also asserted that as a product of Detective Gorman’s experience and

training, “drug traffickers commonly use electronic equipment to aid them in their drug

trafficking activities.   This equipment includes, but is not limited to, . . . mobile

telephones . . . .” The warrant affidavit contained no information indicating that Weber

was involved in defendant’s drug trafficking and did not refer to the previous week’s armed

robbery at Stites’s residence.

       The district court judge concluded that there was probable cause for the warrant

based upon the attached affidavit and thereby issued a warrant authorizing the police to

search three residences that were connected with defendant and his vehicle for further

evidence of drug trafficking. As relevant here, the warrant provided:

       [A]ny cell phones or . . . other devices capable of digital or electronic storage
       seized by authority of this search warrant shall be permitted to be forensically
       searched and or manually searched, and any data that is able to be retrieved
       there from shall be preserved and recorded.

The warrant also contained the following limitation:

             Therein to search for, seize, secure, tabulate and make return
       according to law, the following property and things:



                                              4
              Crack Cocaine, and any other illegally possessed controlled
       substances; any raw material, product, equipment or drug paraphernalia for
       the compounding, cutting, exporting, importing, manufacturing, packaging,
       processing, storage, use or weighing of any controlled substance; proofs of
       residence, such as but not limited to, utility bills, correspondence, rent
       receipts, and keys to the premises; proofs as to the identity of unknown
       suspects such as but not limited to, photographs, certificates, and/or
       diplomas; prerecorded, illegal drug proceeds and any records pertaining to
       the receipt, possession and sale or distribution of controlled substances
       including but not limited to documents, video tapes, computer disks,
       computer hard drives, and computer peripherals; other mail receipts,
       containers or wrappers; currency, property obtained through illegal activity,
       financial instruments, safety deposit box keys, money order receipts, bank
       statements and related records; firearms, ammunition, and all occupants
       found inside. [Emphasis added.]

       On August 12, 2016, police were executing a search at one of the addresses set forth

in the warrant when they detained defendant and seized a phone that was on his person.

On August 17, 2016, defendant was arraigned on the charge of armed robbery.

       On August 23, 2016, Detective Edward Wagrowski performed a forensic

examination of the phone that was seized from defendant, and all of its data was extracted

using Cellebrite, software used for extracting digital data. Upon extraction, Cellebrite

separated and sorted the device’s data into relevant categories by, for example, placing all

of the photographs together in a single location. The extraction process resulted in a 600-

page report of defendant’s cell-phone data, which included more than 2,000 call logs, more

than 2,900 text messages, and more than 1,000 photographs. Detective Wagrowski

testified at trial that Cellebrite enabled police to enter search terms to isolate data from

specific phone numbers or that contained specific words or phrases. If there were no

contacts between a searched number and the device being searched, the searcher would

receive no results and the software would show a blank screen. It is unclear from the record



                                             5
whether and to what extent the data extracted from the cell phone was reviewed for

evidence of defendant’s drug trafficking.

       A month or so after the initial extraction, at the request of the prosecutor in

defendant’s armed-robbery case, Detective Wagrowski conducted further searches of the

cell-phone data for: (a) contacts with the phone numbers of Weber and Stites and (b) the

name “Lisa,” variations on the word “killer” (defendant’s nickname), and the name

“Kris/Kristopher” (defendant’s actual name). These searches uncovered 19 calls between

defendant and Weber on the night of the robbery and 15 text messages between defendant

and Weber between August 5, 2016 and August 10, 2016. Weber’s texts to defendant

leading up to the robbery included communications indicating where Stites’s home was

located, that the home was unlocked, and that there was a flat screen TV in the home.

Defendant sent texts to Weber on the night of the robbery asking her to “[t]ext me or call

me” and to “open the doo[r].” None of the text messages with the words “killer” or “Kris”

were from Weber’s number. The prosecutor acknowledged that the results of these

searches served as evidence at defendant’s armed-robbery trials. Defense counsel objected

to the admission of this evidence, arguing that it was “not relevant” and “stale,” but the

trial court overruled his objection.

       Defendant’s first two trials on the armed-robbery charge resulted in mistrials due to

hung juries. A juror note from the first trial explained that the jury was divided and could

not reach a verdict because “Mr. Stites was not able to positively ID Mr. Hughes” and

“Mrs. Weber’s testimony was not credible (according to some) and she was the only one

to positively identify Mr. Hughes from that night.” Similarly, a juror note from the second

trial listing the jurors’ concerns about the evidence stated that “100% of Lisa W[eber’s]


                                             6
testimony is untrue” and further noted the “d[i]screpancy of [defendant’s] description by

Ron Stites.” At defendant’s third trial, the prosecutor-- while acknowledging that the jury

might have “concerns” regarding Weber’s credibility as a “disputed accomplice” to the

armed robbery-- argued during both opening and closing statements that the text messages

and phone calls discovered on defendant’s cell phone bolstered her testimony and

established a link between defendant and the armed robbery. The jury at defendant’s third

trial convicted him of armed robbery, and he was sentenced to 25 to 60 years in prison.

         Defendant appealed his conviction, arguing in relevant part that (a) the phone

records should have been excluded from trial because the warrant supporting a search of

the data only authorized a search for evidence of drug trafficking and not armed robbery

and (b) trial counsel had been ineffective in failing to object to the data’s admission under

the Fourth Amendment. The Court of Appeals rejected these arguments and affirmed

defendant’s conviction. People v Hughes, unpublished per curiam opinion of the Court of

Appeals, issued September 25, 2018 (Docket No. 338030). Defendant then sought leave

to appeal in this Court, and we ordered oral argument on the application. People v Hughes,

505 Mich 855 (2019).3

3
    The Court asked the parties to address specifically:

         (1) whether the probable cause underlying the search warrant issued during
         the prior criminal investigation authorized police to obtain all of the
         defendant’s cell phone data; (2) whether the defendant’s reasonable
         expectation of privacy in his cell phone data was extinguished when the
         police obtained the cell phone data in a prior criminal investigation; (3) if
         not, whether the search of the cell phone data in the instant case was within
         the scope of the probable cause underlying the search warrant issued during
         the prior criminal investigation; (4) if not, whether the search of the cell
         phone data in the instant case was lawful; and (5) whether trial counsel was


                                               7
                             II. STANDARD OF REVIEW

       Questions of constitutional law are reviewed de novo. People v Hall, 499 Mich 446,

452; 884 NW2d 561 (2016). Defendant did not object to the admission of the evidence

from his cell phone under the Fourth Amendment, so this issue is unpreserved. See People

v Kimble, 470 Mich 305, 309; 684 NW2d 669 (2004). Unpreserved constitutional claims

are reviewed for plain error. People v Carines, 460 Mich 750, 764; 597 NW2d 130 (1999).4

Defendant does not argue that he is entitled to relief under this standard but rather argues

that trial counsel was ineffective for failing to object under the Fourth Amendment. The

standards for “plain error” review and ineffective assistance of counsel are distinct, and

therefore, a defendant can obtain relief for ineffective assistance of counsel even if he or

she cannot demonstrate plain error. See generally People v Randolph, 502 Mich 1; 917

NW2d 249 (2018).

                                     III. ANALYSIS

                              A. FOURTH AMENDMENT

       The Fourth Amendment of the United States Constitution provides:



       ineffective for failing to challenge the search of the cell phone data in the
       instant case on Fourth Amendment grounds. [People v Hughes, 505 Mich
       855 (2019).]
4
  “To avoid forfeiture under the ‘plain error’ rule, three requirements must be met: 1) error
must have occurred, 2) the error was plain, i.e., clear or obvious, 3) and the plain error
affected substantial rights.” Carines, 460 Mich at 763. If these requirements are satisfied,
a court must exercise its discretion and should reverse only if the “forfeited error resulted
in the conviction of an actually innocent defendant or when an error seriously affected the
fairness, integrity or public reputation of judicial proceedings independent of the
defendant’s innocence.” Id. (quotation marks and brackets omitted).



                                             8
                The right of the people to be secure in their persons, houses, papers,
         and effects, against unreasonable searches and seizures, shall not be violated,
         and no Warrants shall issue, but upon probable cause, supported by Oath or
         affirmation, and particularly describing the place to be searched, and the
         persons or things to be seized. [US Const, Am IV.][5]

As indicated by the Fourth Amendment’s text, “reasonableness is always the touchstone of

Fourth Amendment analysis.” Birchfield v North Dakota, 579 US ___, ___; 136 S Ct 2160,

2186; 195 L Ed 2d 560 (2016). Thus, a search warrant is not always required before

searching or seizing a citizen’s personal effects. See, e.g., Brigham City v Stuart, 547 US

398, 403; 126 S Ct 1943; 164 L Ed 2d 650 (2006). However, there is a “strong preference

for searches conducted pursuant to a warrant,” Illinois v Gates, 462 US 213, 236; 103 S Ct


5
    Similarly, the Michigan Constitution has provided:

                The person, houses, papers and possessions of every person shall be
         secure from unreasonable searches and seizures. No warrant to search any
         place or to seize any person or things shall issue without describing them,
         nor without probable cause, supported by oath or affirmation. . . . [Const
         1963, art 1, § 11.]

This provision was recently amended to explicitly protect “electronic data.” See Graham,
Michigan Radio, Election 2020: Michigan Voters Approve Proposal 2, Protecting
Electronic Data <https://www.michiganradio.org/post/election-2020-michigan-voters-
approve-proposal-2-protecting-electronic-data> (posted November 4, 2020) (accessed
November 6, 2020) [https://perma.cc/54KC-6XJY]; 2020 Enrolled Senate Joint Resolution G.
“In interpreting our Constitution, we are not bound by the United States Supreme Court’s
interpretation of the United States Constitution, even where the language is identical.”
People v Goldston, 470 Mich 523, 534; 682 NW2d 479 (2004). However, we have
recognized that, at least before its recent amendment, the Michigan Constitution generally
has afforded the same protections as those secured by the Fourth Amendment. People v
Slaughter, 489 Mich 302, 311; 803 NW2d 171 (2011). This is true even though the
Michigan Constitution since 1936 has contained an express limitation on the application of
the exclusionary rule to violations of Article 1, Section 11. See Goldston, 470 Mich at 535
n 8. Defendant, however, has not argued that the Michigan Constitution affords greater
protections than the Fourth Amendment in the present context, and therefore our analysis
here does not address the recent amendment.


                                               9
2317; 76 L Ed 2d 527 (1983), and the general rule is that officers must obtain a warrant for

a search to be reasonable under the Fourth Amendment. See, e.g., Riley, 573 US at 382.

       In Riley v California, the Supreme Court of the United States held that officers must

generally obtain a warrant before conducting a search of cell-phone data. Riley, 573 US at

386. In so holding, the Court rejected, with respect to cell-phone data, application of the

“search incident to a lawful arrest” exception to the warrant requirement, which generally

allows police to search and seize items (including closed containers) located on a person

during a lawful arrest. Id. at 382-386; United States v Robinson, 414 US 218, 234-236; 94

S Ct 467; 38 L Ed 2d 427 (1973). The Court reasoned that the justifications provided in

Chimel v California, 395 US 752, 762-763; 89 S Ct 2034; 23 L Ed 2d 685 (1969), for this

exception to the warrant requirement-- potential harm to officers and the destruction of

evidence-- are less compelling in the context of digital data. Riley, 573 US at 386.

       The Court also noted that a “search incident to a lawful arrest” is justified, at least

in part, by “an arrestee’s reduced privacy interests upon being taken into police custody.”

Id. at 391. However, it rejected the proposition that an arrestee loses all expectation of

privacy, asserting that “when ‘privacy-related concerns are weighty enough’ a ‘search may

require a warrant, notwithstanding the diminished expectations of privacy of the

arrestee.’ ” Id. at 392, quoting Maryland v King, 569 US 435, 463; 133 S Ct 1958; 186

L Ed 2d 1 (2013). The Court held that a warrant was required to search the contents of a

cell phone seized during a lawful arrest notwithstanding this reduced expectation of privacy

because “[c]ell phones differ in both a quantitative and a qualitative sense from other

objects that might be kept on an arrestee’s person”:




                                             10
       [I]t is no exaggeration to say that many of the more than 90% of American
       adults who own a cell phone keep on their person a digital record of nearly
       every aspect of their lives—from the mundane to the intimate. Allowing the
       police to scrutinize such records on a routine basis is quite different from
       allowing them to search a personal item or two in the occasional case.

              Although the data stored on a cell phone is distinguished from
       physical records by quantity alone, certain types of data are also qualitatively
       different. An Internet search and browsing history, for example, can be
       found on an Internet-enabled phone and could reveal an individual’s private
       interests or concerns—perhaps a search for certain symptoms of disease,
       coupled with frequent visits to WebMD. Data on a cell phone can also reveal
       where a person has been. Historic location information is a standard feature
       on many smart phones and can reconstruct someone’s specific movements
       down to the minute, not only around town but also within a particular
       building.

              Mobile application software on a cell phone, or “apps,” offer a range
       of tools for managing detailed information about all aspects of a person’s
       life. There are apps for Democratic Party news and Republican Party news;
       apps for alcohol, drug, and gambling addictions; apps for sharing prayer
       requests; apps for tracking pregnancy symptoms; apps for planning your
       budget; apps for every conceivable hobby or pastime; apps for improving
       your romantic life. There are popular apps for buying or selling just about
       anything, and the records of such transactions may be accessible on the phone
       indefinitely. There are over a million apps available in each of the two major
       app stores; the phrase “there’s an app for that” is now part of the popular
       lexicon. The average smart phone user has installed 33 apps, which together
       can form a revealing montage of the user’s life. [Riley, 573 US at 393, 395-
       396 (quotation marks and citations omitted).]

Riley makes clear that, in light of the extensive privacy interests at stake, general Fourth

Amendment principles apply with equal force to the digital contents of a cell phone. See

id. at 396-397 (“[A] cell phone search would typically expose to the government far more

than the most exhaustive search of a house: A phone not only contains in digital form many

sensitive records previously found in the home; it also contains a broad array of private

information never found in a home in any form—unless the phone is.”).




                                             11
       With this constitutional background in mind, the issue posed in this case is whether

officers violated the Fourth Amendment when they searched defendant’s cell-phone data

in pursuit of evidence that defendant committed an armed robbery when the phone was

seized pursuant to a warrant authorizing the search of this data for evidence of unrelated

drug trafficking.6 The prosecutor makes two principal arguments in support of the officer’s

search of defendant’s cell-phone data for evidence of the armed robbery: (a) the warrant to

seize and search defendant’s cell-phone data for evidence of drug trafficking extinguished

6
  Defendant also argues that the district court judge lacked probable cause to authorize the
search and seizure of his cell-phone data for evidence of drug trafficking because the
probable cause underlying the warrant failed to establish the required nexus between his
alleged criminal activity and his cell phone. See Warden, Maryland Penitentiary v Hayden,
387 US 294, 307; 87 S Ct 1642; 18 L Ed 2d 782 (1967). He contends that Detective
Gorman’s opinion, grounded in his training and expertise, that drug traffickers commonly
use cell phones to aid in their criminal enterprise was insufficient to provide probable cause
that his cell phone would contain evidence of drug trafficking. Cf. United States v Brown,
828 F3d 375, 384 (CA 6, 2016) (“[I]f the affidavit fails to include facts that directly connect
the residence with the suspected drug dealing activity, . . . it cannot be inferred that drugs
will be found in the defendant’s home—even if the defendant is a known drug dealer.”).
In light of the pervasiveness of modern cell-phone use recognized by Riley, defendant thus
raises a not-unreasonable concern as to the issuance of a warrant to search and seize cell-
phone data based solely on the nature of the crime alleged. See Riley, 573 US at 399 (“It
would be a particularly inexperienced or unimaginative law enforcement officer who could
not come up with several reasons to suppose evidence of just about any crime could be
found on a cell phone.”). On the other hand, there is caselaw to suggest that allegations of
drug trafficking are distinct from other alleged criminal activities because cell phones are
well-recognized tools of the trade for drug traffickers. See, e.g., United States v Hathorn,
920 F3d 982, 985 (CA 5, 2019) (“Cell phones, computers, and other electronic devices are
vital to the modern-day drug trade.”). Because we conclude that the officer here violated
the Fourth Amendment when he searched defendant’s cell-phone data for evidence of
armed robbery without having obtained a second warrant, we need not decide whether the
warrant affidavit provided a sufficient nexus between defendant’s drug trafficking and his
cell phone. More specifically, we need not decide whether cell phones constitute tools of
the trade for drug traffickers such that an affidavit that establishes probable cause of drug
trafficking necessarily establishes the required nexus between a suspect’s cell phone and
the alleged criminal activity.


                                              12
defendant’s reasonable expectation of privacy in all of his data and therefore no search

occurred under the Fourth Amendment and (b) the search for evidence of the armed robbery

fell within the scope of the warrant issued to search for evidence of drug trafficking because

the warrant authorized officers to review all of defendant’s data for evidence of drug

trafficking and Weber allegedly bought drugs from defendant before the armed robbery.

We respectfully find neither argument persuasive.

                           1. EXPECTATION OF PRIVACY

       The first issue is whether defendant lost the reasonable expectation of privacy in his

cell-phone data when the cell phone was seized and the data was searched pursuant to the

warrant issued in the drug-trafficking case. As this Court has explained:

       A search for Fourth Amendment purposes occurs only when “an expectation
       of privacy that society is prepared to consider reasonable is infringed.”
       United States v Jacobsen, 466 US 109, 113; 104 S Ct 1652; 80 L Ed 2d 85
       (1984). “If the inspection by police does not intrude upon a legitimate
       expectation of privacy, there is no ‘search’ subject to the Warrant Clause.”
       Illinois v Andreas, 463 US 765, 771; 103 S Ct 3319; 77 L Ed 2d 1003 (1983).
       If a person has no reasonable expectation of privacy in an object, a search of
       that object for purposes of the Fourth Amendment cannot occur. [Minnesota
       v Dickerson, 508 US 366, 375; 113 S Ct 2130; 124 L Ed 2d 334 (1993)];
       People v Brooks, 405 Mich 225, 242; 274 NW2d 430 (1979). [People v
       Custer, 465 Mich 319, 333; 630 NW2d 870 (2001).]

It is clear that under Riley, citizens maintain a reasonable expectation of privacy in their

cell-phone data and this reasonable expectation of privacy does not altogether dissipate

merely because a phone is seized during a lawful arrest. The question here is whether the

seizure and search of cell-phone data pursuant to a warrant extinguishes that otherwise

reasonable expectation of privacy in the entirety of that seized data. We conclude that it

does not. Rather, a warrant authorizing the police to seize and search cell-phone data


                                             13
allows officers to examine the seized data only to the extent reasonably consistent with the

scope of the warrant.

       The prosecutor argues the seizure of defendant’s cell-phone data pursuant to the

search warrant eliminated his reasonable expectation of privacy in that data, permitting

officers to review all such data without implicating the Fourth Amendment. This argument

“overlooks the important difference between searches and seizures.” Horton v California,

496 US 128, 133; 110 S Ct 2301, 2306; 110 L Ed 2d 112 (1990). “A search compromises

the individual interest in privacy; a seizure deprives the individual of dominion over his or

her person or property.” Id. The authority to seize an item does not necessarily eliminate

one’s expectation of privacy in that item and therefore allow the police to search that item

without limitation. See Jacobsen, 466 US at 114 (“Even when government agents may

lawfully seize . . . a package to prevent loss or destruction of suspected contraband, the

Fourth Amendment requires that they obtain a warrant before examining the contents of

such a package.”); United States v Chadwick, 433 US 1, 13 n 8; 97 S Ct 2476; 53 L Ed 2d

538 (1977) (“[T]he [lawful] seizure [of respondents’ footlocker] did not diminish

respondents’ legitimate expectation that the footlocker’s contents would remain private.”);

Custer, 465 Mich at 342 (“[W]e do not conclude that, once the police lawfully seize an

object from an individual, that individual’s reasonable expectation of privacy in that object

is altogether lost.”) (emphasis omitted). This distinction was also implicitly recognized in

Riley when the Court held that officers could seize a cell phone on a person incident to a

lawful arrest but they could not search the contents of that phone without a warrant. Riley,

573 US at 388, 401. While it may have been reasonable for officers to seize all of

defendant’s cell-phone data pursuant to the warrant to prevent the destruction of evidence


                                             14
and to isolate incriminating material from nonincriminating material, it was not necessarily

reasonable for police to review that data without limitation.

       The prosecutor’s reliance on cases holding that a suspect loses all expectation of

privacy in items seized from his person during a lawful arrest is inapt. The prosecutor cites

United States v Edwards, 415 US 800, 801-802, 806; 94 S Ct 1234; 39 L Ed 2d 771 (1974),

in which the Supreme Court held that the search and seizure of a suspect’s clothes the

morning after his arrest was reasonable. The Court recognized that officers could have

searched and seized the clothes the defendant wore at the time of his arrest immediately

after the arrest and held that a reasonable delay in doing so did not render the search and

seizure unreasonable. Id. at 805. The Court further commented, “[I]t is difficult to perceive

what is unreasonable about the police’s examining and holding as evidence those personal

effects of the accused that they already have in their lawful custody as the result of a lawful

arrest.” Id. at 806. Relying on Edwards, some courts have held that an arrestee lacks any

reasonable expectation of privacy in items seized during a lawful arrest and therefore a

later examination of those items, even for evidence of a crime other than the crime of arrest,

is not a search under the Fourth Amendment. See, e.g., Wallace v State, 373 Md 69, 90-

94; 816 A2d 883 (2003).

       These cases are inapplicable here, as Riley distinguished cell-phone data from other

items subject to a search incident to a lawful arrest in terms of the privacy interests at stake.

See Riley, 573 US at 393. Riley thus stands for the proposition that seizure of a phone and

its digital contents-- unlike a seizure of other items on a person-- does not entirely

extinguish one’s right to privacy in that data. Moreover, Edwards itself did not hold that

the mere fact an item was lawfully seized eliminated a suspect’s reasonable expectation of


                                               15
privacy; rather, it recognized that a lawful search of an item on an arrestee’s person

immediately after arrest was already reasonable under the exception to the warrant

requirement for searches incident to a lawful arrest and that a reasonable delay in

conducting that permissible search did not render the search unreasonable. Edwards, 415

US at 805. In other words, the police “did no more [at the police station] than they were

entitled to do incident to the usual custodial arrest and incarceration.” Id. Thus, assuming

that this caselaw is pertinent in the instant context, it reinforces our conclusion that the later

review of defendant’s cell-phone data for evidence of an armed robbery was only lawful if

this review was permissible in the first instance, i.e., if it was within the scope of the

warrant issued to search for evidence of drug trafficking. See State v Betterley, 191 Wis

2d 406, 418; 529 NW2d 216 (1995) (holding that, based on Edwards, “the permissible

extent of the second look [at items seized by police incident to a lawful arrest] is defined

by what the police could have lawfully done without violating the defendant’s reasonable

expectations of privacy during the first search, even if they did not do it at that time”).

       The prosecutor also argues that because the search warrant authorized officers to

search defendant’s cell-phone data for evidence of drug trafficking, defendant no longer

had a reasonable expectation of privacy in all of his data. Both the prosecutor and the Court

of Appeals relied on United States v Jacobsen for the proposition that defendant lost all

expectation of privacy in his cell-phone data when the search warrant authorized a search

of that data for drug trafficking. In Jacobsen, the employees of a private freight carrier

opened a damaged package and discovered a long tube. Jacobsen, 466 US at 111. The

employees cut open the tube and discovered plastic bags filled with a white powdery

substance. Id. The employees summoned a federal agent who, without obtaining a


                                               16
warrant, removed the bags from the tube, took a small amount of the powder out of the

bags, and tested the powder to determine whether it was cocaine. Id. at 111-112. The

Court noted that a private party’s search of an item does not implicate the Fourth

Amendment and held that “[t]he agent’s viewing of what a private party had freely made

available for his inspection did not violate the Fourth Amendment.” Id. at 119-120. The

Court explained:

       Once frustration of the original expectation of privacy occurs, the Fourth
       Amendment does not prohibit governmental use of the now nonprivate
       information. . . . The Fourth Amendment is implicated only if the authorities
       use information with respect to which the expectation of privacy has not
       already been frustrated. [Id. at 117.]

Accordingly, the Court held that “[t]he additional invasions of respondents’ privacy by the

Government agent must be tested by the degree to which they exceeded the scope of the

private search.” Id. at 115. The Court concluded that the agent’s removal of the plastic

bags from the tube and his visual inspection of the contents of the bags “infringed no

legitimate expectation of privacy and hence was not a ‘search’ within the meaning of the

Fourth Amendment” because this action did not enable the officer to learn anything that

had not previously been uncovered during the private search. Id. at 120.7


7
  Jacobsen proceeded to consider aspects of the officer’s actions that exceeded the scope
of the private search: the seizure of the plastic bags containing white powder and the testing
of the white powder to determine whether it was cocaine. The Court held that the removal
of the plastic bags from the box constituted a seizure because the officer had asserted
“dominion and control over the package and its contents,” id. at 120, but that the seizure
nonetheless was reasonable under the Fourth Amendment because “it was apparent that the
tube and plastic bags contained contraband and little else.” Id. at 121-122. It further held
that testing the powder did not constitute a search because the test “merely disclose[d]
whether or not [the] particular substance [was] cocaine.” Id. at 123. However, the Court
noted that the test of the powder involved destruction of some of that powder and that this


                                             17
       Jacobsen, in our judgment, does not advance the prosecutor’s argument. Jacobsen

addressed the degree to which a private party’s search of otherwise private items permits

the state to review those items. But there was no private search here. While Jacobsen is

consistent with the general proposition that one lacks a legitimate expectation of privacy

in items that are exposed publicly, see, e.g., Katz v United States, 389 US 347, 351; 88 S Ct

507; 19 L Ed 2d 576 (1967), it says little about the extent to which the search of an item

pursuant to a search warrant eliminates a citizen’s legitimate expectation of privacy.8 The

prosecutor cites no caselaw indicating that the issuance of a warrant eliminates entirely

one’s reasonable expectation of privacy in the place or property to be searched.9 To the

contrary, it is well established that a search warrant allows the state to examine property

only to the extent authorized by the warrant. See, e.g., Bivens v Six Unknown Named

Agents of Fed Bureau of Narcotics, 403 US 388, 394 n 7; 91 S Ct 1999; 29 L Ed 2d 619



deprivation of the defendant’s possessory interest constituted a seizure under the Fourth
Amendment. Id. at 124-125. The Court concluded that this seizure was reasonable because
it had a de minimis impact on defendant’s property interest and that “the suspicious nature
of the material made it virtually certain that the substance tested was in fact contraband.”
Id. at 125.
8
  Moreover, the other searches and seizures in Jacobsen-- specifically, the officer’s
reexamination of the contents of the package and seizure of the plastic bags, as well as the
field test to determine whether the seized substance was cocaine-- have no analogue in the
instant case. The search here did not merely duplicate the previous search, and there was
no simple test performed to determine whether the data confirmed illegal activity.
9
  Indeed, the prosecutor cites no caselaw indicating that the issuance of a search warrant
eliminates at all one’s reasonable expectation of privacy in the items to be searched rather
than merely permitting officers temporarily to compromise that reasonable expectation of
privacy. We need not resolve this semantic difference here because, regardless of how it
is framed, the result would be the same-- a warrant only permits police to review an item
or area to the extent that such review lies within the scope of the warrant.


                                             18
(1971) (“[T]he Fourth Amendment confines an officer executing a search warrant strictly

within the bounds set by the warrant.”). “If the scope of the search exceeds that permitted

by the terms of a validly issued warrant . . . , the subsequent seizure is unconstitutional

without more.” Horton, 496 US at 140. Thus, a search conducted pursuant to a search

warrant-- unlike a private search-- is necessarily limited to the scope of the warrant.

       To the extent that Jacobsen is relevant in the present context, its reasoning further

reinforces our conclusion that the issuance of a search warrant does not eliminate entirely

one’s reasonable expectation of privacy but only allows a search consistent with the scope

of the warrant. As the United States Court of Appeals for the Sixth Circuit explained in

applying Jacobsen to the search of a laptop, “[f]or the review of [the defendant’s] laptop

to be permissible, Jacobsen instructs us that [the officer’s] search had to stay within the

scope of [the] initial private search.” United States v Lichtenberger, 786 F3d 478, 488

(CA 6, 2015). The court therefore concluded that the officer’s search exceeded the scope

of the warrant because there was “no virtual certainty that [the officer’s] review [of the

defendant’s digital data] was limited to the photographs from” the earlier private search.

Id.; see also United States v Sparks, 806 F3d 1323, 1336 (CA 11, 2015) (“While [the]

private search of the cell phone might have removed certain information from the Fourth

Amendment’s protections, it did not expose every part of the information contained in the

cell phone.”), overruled on other grounds by United States v Ross, 963 F3d 1056 (CA 11,

2020); State v Terrell, 372 NC 657, 669, 670; 831 SE2d 17 (2019) (“We cannot agree that

the mere opening of a thumb drive and the viewing of as little as one file automatically

renders the entirety of the device’s contents ‘now nonprivate information’ no longer [to be]

afforded any protection by the Fourth Amendment. . . .          [T]he extent to which an


                                             19
individual’s expectation of privacy in the contents of an electronic storage device is

frustrated depends upon the extent of the private search and the nature of the device and its

contents.”).10 As applied to the instant situation, under Jacobsen, the scope of the officer’s

search of defendant’s data for evidence of armed robbery was limited to the scope of the

initial lawful intrusion, i.e., the breadth of the warrant in the drug-trafficking case.

Accordingly, Jacobsen does not support the proposition that defendant lost entirely his

expectation of privacy in all of his cell-phone data once the cell phone was seized and the

data searched pursuant to a warrant.11

10
   At least two federal courts of appeals have held that under Jacobsen, once there is a
private search of any part of a suspect’s digital data, police officers are permitted to review
all the data on that device without a warrant, comparing digital data to a closed container
that when opened loses all expectation of privacy. United States v Runyan, 275 F3d 449,
464 (CA 5, 2001); Rann v Atchison, 689 F3d 832, 836-837 (CA 7, 2012). For the reasons
stated below, we find unpersuasive, in light of the United States Supreme Court’s
subsequent decision in Riley, the analogy of a digital device to a closed container and thus
find these cases unpersuasive.
11
   While not cited by the prosecutor, we recognize that the Minnesota Court of Appeals in
State v Johnson, 831 NW2d 917, 924 (Minn App, 2013), reached the opposite conclusion
to that we reach here, holding that “the execution of the warrant ‘frustrated’ and terminated
appellant’s expectation of privacy in the hard drive and the digital contents identified in
the warrant.” Johnson relied on Illinois v Andreas, in which the United States Supreme
Court held that “the subsequent reopening of [a] container is not a ‘search’ within the
intendment of the Fourth Amendment” and that “absent a substantial likelihood that the
contents have been changed, there is no legitimate expectation of privacy in the contents
of a container previously opened under lawful authority.” Andreas, 463 US at 772-773.
However, Andreas’s holding regarding the opening of a closed container, as with those
holdings cited in note 10 of this opinion, is also inapplicable to searches of cell-phone data
in light of Riley’s subsequent recognition that privacy interests in digital data may greatly
exceed those with regard to more mundane physical objects. Riley, 573 US at 393, 397
(holding that comparing a search of physical objects to a search of digital data is “like
saying a ride on horseback is materially indistinguishable from a flight to the moon,” and
noting that “[t]reating a cell phone as a container whose contents may be searched incident
to an arrest is a bit strained”). See also Kerr, Searches and Seizures in A Digital World,


                                              20
       In summary, the search and seizure of defendant’s cell-phone data pursuant to a

warrant in the drug-trafficking case did not altogether eliminate his reasonable expectation

of privacy in that data. Rather, the police were permitted to seize and search that data, but

only to the extent authorized by the warrant. Any further review of the data beyond the

scope of that warrant constitutes a search that is presumptively invalid under the Fourth

Amendment, absent some exception to that amendment’s warrant requirement. See

Horton, 496 US at 140. The remaining question is whether the review of defendant’s data

for evidence of an armed robbery fell within the scope of the warrant issued in the drug-

trafficking case.

                             2. SCOPE OF THE WARRANT

       This Court has yet to specifically address the Fourth Amendment requirements for

a search of digital data from a cell phone authorized by a warrant. In considering this issue,

we are guided by two fundamental sources of relevant law: (a) the Fourth Amendment’s

“particularity” requirement, which limits an officer’s discretion when conducting a search

pursuant to a warrant and (b) Riley’s recognition of the extensive privacy interests in

cellular data. In light of these legal predicates, we conclude that as with any other search


119 Harv L Rev 531, 555 (2005) (arguing that “[a] computer is like a container that stores
thousands of individual containers”). Numerous courts since Riley have similarly
interpreted that decision, as we believe it must be interpreted, as rejecting an analogy
between searches of digital data and searches of closed containers. See, e.g.,
Lichtenberger, 786 F3d at 487 (“[S]earches of physical spaces and the items they contain
differ in significant ways from searches of complex electronic devices under the Fourth
Amendment.”); United States v Jenkins, 850 F3d 912, 920 n 3 (CA 7, 2017); Terrell, 372
NC at 669; United States v Lara, 815 F3d 605, 610 (CA 9, 2016). Accordingly, we
respectfully find Johnson to be unpersuasive and decline to adopt its reasoning in light of
Riley.


                                             21
conducted pursuant to a warrant, a search of digital data from a cell phone must be

“reasonably directed at uncovering” evidence of the criminal activity alleged in the warrant

and that any search that is not so directed but is directed instead toward finding evidence

of other and unrelated criminal activity is beyond the scope of the warrant. United States

v Loera, 923 F3d 907, 917, 922 (CA 10, 2019); see also Horton, 496 US at 140-141.

       The Fourth Amendment requires that search warrants “particularly describ[e] the

place to be searched, and the persons or things to be seized.” US Const, Am IV. A search

warrant thus must state with particularity not only the items to be searched and seized, but

also the alleged criminal activity justifying the warrant. See Berger v State of New York,

388 US 41, 55-56; 87 S Ct 1873; 18 L Ed 2d 1040 (1967); Andresen v Maryland, 427 US

463, 479-480; 96 S Ct 2737; 49 L Ed 2d 627 (1976); United States v Galpin, 720 F3d 436,

445 (CA 2, 2013) (“[A] warrant must identify the specific offense for which the police

have established probable cause.”). That is, some context must be supplied by the affidavit

and warrant that connects the particularized descriptions of the venue to be searched and

the objects to be seized with the criminal behavior that is suspected, for even particularized

descriptions will not always speak for themselves in evidencing criminality. See Hayden,

387 US at 307 (“There must, of course, be a nexus . . . between the item to be seized and

criminal behavior. Thus . . . , probable cause must be examined in terms of cause to believe

that the evidence sought will aid in a particular apprehension or conviction. In so doing,

consideration of police purposes will be required.”).

       The manifest purpose of this particularity requirement was to prevent general
       searches. By limiting the authorization to search to the specific areas and
       things for which there is probable cause to search, the requirement ensures
       that the search will be carefully tailored to its justifications, and will not take
       on the character of the wide-ranging exploratory searches the Framers

                                               22
       intended to prohibit. [Maryland v Garrison, 480 US 79, 84; 107 S Ct 1013;
       94 L Ed 2d 72 (1987); see also, e.g., Horton, 496 US at 139.]

       While “officers do not have to stop executing a search warrant when they run across

evidence outside the warrant’s scope, they must nevertheless reasonably direct their search

toward evidence specified in the warrant.” Loera, 923 F3d at 920; see also United States

v Ramirez, 523 US 65, 71; 118 S Ct 992; 140 L Ed 2d 191 (1998) (“The general touchstone

of reasonableness . . . governs the method of execution of the warrant.”). For example, a

warrant authorizing police to search a home for evidence of a stolen television set would

not permit officers to search desk drawers for evidence of drug possession. See Horton,

496 US at 140-141.12 This particularity requirement defines the permissible scope of a

search pursuant to a warrant, and any deviation from that scope is a warrantless search that

is unreasonable absent an exception to the warrant requirement. Id. at 140. More

specifically, in connection with the present case the state exceeds the scope of a warrant

where a search is not reasonably directed at uncovering evidence related to the criminal

activity identified in the warrant, but rather is designed to uncover evidence of criminal

activity not identified in the warrant. See, e.g., United States v Carey, 172 F3d 1268, 1272-



12
   As noted by Riley, a home and a cell phone are similarly situated, at least to the extent
that a search of either may result in a significant intrusion into an individual’s private
affairs. Riley, 573 US at 396-397 (“In 1926, [Judge] Hand observed . . . that it is ‘a totally
different thing to search a man’s pockets and use against him what they contain, [than to]
ransack[] his house for everything which may incriminate him.’ If his pockets contain a
cell phone, however, that is no longer true. Indeed, a cell-phone search would typically
expose to the government far more than the most exhaustive search of a house: A phone
not only contains in digital form many sensitive records previously found in the home; it
also contains a broad array of private information never found in a home in any form—
unless the phone is.”) (citation omitted).



                                             23
1273 (CA 10, 1999); Loera, 923 F3d at 922; United States v Nasher-Alneam, 399 F Supp

3d 579, 593-594 (SD W Va, 2019).

       In this regard, we first address the prosecutor’s argument that the search for evidence

of armed robbery fell within the scope of the warrant because the warrant authorized

officers to review the entire 600-page report containing the apparent totality of defendant’s

cell-phone data, as any segment of this data may have contained evidence of drug

trafficking and digital data can be manipulated to hide incriminating content.13 We are

cognizant that a criminal suspect will not always store or organize incriminating

information on his or her digital devices in the most obvious way or in a manner that



13
   Implicit in this argument is the assumption that an officer’s subjective intention to look
for evidence related to a crime not identified in the warrant is immaterial so long as the
search is objectively authorized by the scope of the warrant. In other words, the
prosecutor’s argument seems premised on the proposition that so long as it was objectively
reasonable to review all of defendant’s data for evidence of drug trafficking, it is irrelevant
that the genuine purpose of the search was to secure evidence of an armed robbery. The
facts that the prosecutor in the armed-robbery case asked Detective Wagrowski-- a month
or so after the initial extraction of the data-- to conduct a further search of defendant’s cell-
phone data using search terms related to the armed robbery and that this evidence was
eventually admitted in the armed-robbery trials suggests that this search was not designed
to obtain evidence related to drug trafficking, but rather to bolster the prosecutor’s case in
the armed-robbery trial. Some courts have held that an officer’s subjective intention to
find evidence of a crime not identified in the warrant constitutes a relevant factor in
determining whether a search of digital data falls outside the scope of the warrant, while
others have held that this is a purely objective inquiry. Compare Loera, 923 F3d at 919 &
n 3 (holding that the subjective intention of the officer to discern evidence of a crime not
identified in the warrant is a relevant factor in determining whether the search exceeded
the scope of the warrant), with United States v Williams, 592 F3d 511, 522 (CA 4, 2010)
(“[T]he scope of a search conducted pursuant to a warrant is defined objectively by the
terms of the warrant and the evidence sought, not by the subjective motivations of an
officer.”) (emphasis omitted). Because the search here was objectively beyond the scope
of the warrant, we need not decide whether an officer’s subjective intention is a relevant
consideration.


                                               24
facilitates the location of that information. See, e.g., United States v Mann, 592 F 3d 779,

782 (CA 7, 2010) (“Unlike a physical object that can be immediately identified as

responsive to the warrant or not, computer files may be manipulated to hide their true

contents.”). We do not hold or imply here that officers in the execution of a search of

digital data must review only digital content that a suspect deigns to identify as pertaining

to criminal activity. See United States v Burgess, 576 F3d 1078, 1093-1094 (CA 10, 2009).

Such an approach would undermine legitimate law enforcement practices and unduly

restrict officers well beyond the dictates of the Fourth Amendment.

       However, at the same time, we decline to adopt a rule that it is always reasonable

for an officer to review the entirety of the digital data seized pursuant to a warrant on the

basis of the mere possibility that evidence may conceivably be found anywhere on the

device or that evidence might be concealed, mislabeled, or manipulated. Such a per se rule

would effectively nullify the particularity requirement of the Fourth Amendment in the

context of cell-phone data and rehabilitate an impermissible general warrant that “would

in effect give ‘police officers unbridled discretion to rummage at will among a person’s

private effects.’ ” Riley, 573 US at 399, quoting Arizona v Gant, 556 US 332, 345; 129 S

Ct 1710; 173 L Ed 2d 485 (2009); see also People v Herrera, 357 P3d 1227, 1228, 1233;

2015 CO 60 (Colo, 2015) (holding that allowing a search of an entire device for evidence

of a crime based upon the possibility that evidence of the crime could be found anywhere

on the phone and that the incriminating data could be hidden or manipulated would “render

the warrant a general warrant in violation of the Fourth Amendment’s particularity

requirement”). This result would be especially problematic in light of Riley’s observations

concerning the sheer amount of information contained in cellular data and the highly


                                             25
personal character of much of that information. Riley, 573 US at 394-396; see also United

States v Otero, 563 F3d 1127, 1132 (CA 10, 2009) (“The modern development of the

personal computer and its ability to store and intermingle a huge array of one’s personal

papers in a single place increases law enforcement’s ability to conduct a wide-ranging

search into a person’s private affairs, and accordingly makes the particularity requirement

that much more important.”); Galpin, 720 F3d at 447 (“There is . . . a serious risk that every

warrant for electronic information will become, in effect, a general warrant, rendering the

Fourth Amendment irrelevant.        This threat demands a heightened sensitivity to the

particularity requirement in the context of digital searches.”) (quotation marks and citation

omitted). Accordingly, an officer’s search of seized digital data, as with any other search

conducted pursuant to a warrant, must be reasonably directed at finding evidence of the

criminal activity identified within the warrant. Loera, 923 F3d at 921-922.

       Specifically in the digital context, this requires that courts and officers consider

“whether the forensic steps of the search process were reasonably directed at uncovering

the evidence specified in the search warrant.” Id. at 917. Whether a search of seized digital

data that uncovers evidence of criminal activity not identified in the warrant was reasonably

directed at finding evidence relating to the criminal activity alleged in the warrant turns on

a number of considerations, including: (a) the nature of the criminal activity alleged and

the type of digital data likely to contain evidence relevant to the alleged activity;14 (b) the


14
   For example, in the absence of contrary case-specific information, it is unlikely that
evidence relating to tax fraud would be discovered by reviewing the images on a digital
device. See Carey, 172 F3d at 1275 n 8 (“Where a search warrant seeks only financial
records, law enforcement officers should not be allowed to search through telephone lists
or word processing files absent a showing of some reason to believe that these files contain


                                              26
evidence provided in the warrant affidavit for establishing probable cause that the alleged

criminal acts have occurred;15 (c) whether nonresponsive files are segregated from


the financial records sought.”) (quotation marks and citation omitted); Gershowitz, The
Post-Riley Search Warrant: Search Protocols on Particularity in Cell Phone Searches, 69
Vanderbilt L Rev 585, 630-638 (2016) (arguing that criminals engaged in simpler types of
street crimes, such as drug trafficking, are more likely to use cell phones and less likely to
“mislabel . . . or bury evidence” than criminals engaged in crimes like child pornography
and financial misconduct and therefore searches of cell phones for evidence of these
simpler crimes should be more limited in scope than searches of computers for evidence of
child pornography or financial misconduct).
15
   “The fact that [a warrant] application adequately described the ‘things to be seized’ does
not save [a] warrant from its facial invalidity. The Fourth Amendment by its terms requires
particularity in the warrant, not in the supporting documents.” Groh v Ramirez, 540 US
551, 557; 124 S Ct 1284; 157 L Ed 2d 1068 (2004) (emphasis omitted). However, the
particularity requirement of the Fourth Amendment can be satisfied by an affidavit that the
warrant incorporates by reference. See, e.g., United States v Hamilton, 591 F3d 1017, 1025
(CA 8, 2010). “[M]ost Courts of Appeals have held that a court may construe a warrant
with reference to a supporting application or affidavit if the warrant uses appropriate words
of incorporation, and if the supporting document accompanies the warrant.” Groh, 540 US
at 557-558. The prosecutor argues that the warrant here incorporated the warrant affidavit
by reference. The warrant stated, “THE ATTACHED AFFIDAVIT, having been sworn to
by the affiant, Detective Matthew Gorman, before me this day, based upon facts stated
therein, probable cause having been found in the name of the people of the State of
Michigan, I command that you enter the following described places and vehicles[.]” The
warrant affidavit in this case accompanied the warrant, but it is unclear whether the warrant
used “appropriate words of incorporation.” We need not resolve this issue here except to
say that regardless of whether a warrant incorporates the affidavit by reference,
consideration of the evidence provided in the warrant affidavit for establishing probable
cause is relevant to whether a search of digital data was reasonably directed at discovering
evidence of the crime alleged in the warrant. Cf. State v Goynes, 303 Neb 129, 142; 927
NW2d 346 (2019) (“[A] warrant for the search of the contents of a cell phone must be
sufficiently limited in scope to allow a search of only that content that is related to the
probable cause that justifies the search.”); Dennis, Regulating Search Warrant Execution
Procedure for Stored Electronic Communications, 86 Fordham L Rev 2993, 3012 (2018)
(noting that it is relevant to a search’s reasonableness “whether the government subjected
the materials to subsequent searches based on new information and theories developed
about the case. In these instances, courts have expressed concern about continued searches
for evidence under new theories of the case or more expansive areas not initially included


                                             27
responsive files on the device;16 (d) the timing of the search in relation to the issuance of

the warrant and the trial for the alleged criminal acts;17 (e) the technology available to allow

officers to sort data likely to contain evidence related to the criminal activity alleged in the

warrant from data not likely to contain such evidence without viewing the contents of the

unresponsive data and the limitations of this technology;18 (f) the nature of the digital


in the warrant”), citing United States v Wey, 256 F Supp 3d 355, 406 (SDNY, 2017); People
v Thompson, 28 NYS3d 237, 255 (2016).
16
     See Loera, 923 F3d at 919.
17
  See Nasher-Alneam, 399 F Supp 3d 579 (holding that a second search of digital data for
evidence of fraud 15 months after the records were seized to be searched for evidence of
distribution of a controlled substance and after the defendant had already gone to trial once
exceeded the scope of the warrant); United States v Metter, 860 F Supp 2d 205, 209, 211,
215 (EDNY, 2012) (holding that a fifteen-month delay in the government’s review of
seized devices violated the Fourth Amendment); United States v Keszthelyi, 308 F3d 557,
568-569 (CA 6, 2002) (“[A] single search warrant may authorize more than one entry into
the premises identified in the warrant, as long as the second entry is a reasonable
continuation of the original search;” “the subsequent entry must indeed be a continuation
of the original search, and not a new and separate search.”). But see United States v
Johnston, 789 F 3d 934, 941-943 (CA 9, 2015) (holding that a search of seized data five
years after the initial seizure was reasonable where the search was for evidence of the same
criminal conduct alleged in the warrant).
18
   “[L]aw enforcement officers can generally employ several methods to avoid searching
files of the type not identified in the warrant: observing files types and titles listed on the
directory, doing a key word search for relevant terms, or reading portions of each file stored
in the memory.” Carey, 172 F3d at 1276; see also Baron-Evans, When the Government
Seizes and Searches Your Client’s Computer, 18 No. 7 White-Collar Crime Rep 2 (2004);
2004 WL 635186 at 7 (“Various technical means are available to enable the government
to confine the search to the scope of probable cause, including searching by filename,
directory or subdirectory; the name of the sender or recipient of e-mail; specific key words
or phrases; particular types of files as indicated by filename extensions; and/or file date
and time.”). The availability of such methods does not necessarily foreclose a more general
search of the data. See Perldeiner, Total Recall: Computers and the Warrant Clause, 49
Conn L Rev 1757, 1777-1779 (2017) (noting four situations in which searching for and
isolating data is difficult: (a) when metadata is deleted, (b) when data is encrypted, (c)


                                              28
device being searched;19 (g) the type and breadth of the search protocol employed;20 (h)

whether there are any indications that the data has been concealed, mislabeled, or

manipulated to hide evidence relevant to the criminal activity alleged in the warrant, such

as when metadata is deleted or when data is encrypted;21 and (i) whether, after reviewing

a certain number of a particular type of data, it becomes clear that certain types of files are

not likely to contain evidence related to the criminal activity alleged in the warrant.22



when data is stored off-site, and (d) when searching for images); see also Rosa v
Commonwealth, 48 Va App 93, 101; 628 SE2d 92 (2006) (“[F]ile extensions may be
misleading and may not give accurate descriptions of the material contained in the file.”).
However, the use and availability of such technology is relevant to whether a more general
search of the data is reasonable.
19
  See Note, What Comes After “Get a Warrant”: Balancing Particularity and Practicality
in Mobile Device Search Warrants Post-Riley, 101 Cornell L Rev 187, 204-208 (2015)
(arguing that a reasonable search method of cell-phone data will differ from a reasonable
search of computer data because “(1) there are different forensic steps involved with mobile
device searches compared to computer searches and (2) mobile phones are functionally
different from computers”).
20
   “To undertake any meaningful assessment of the government’s search techniques [of
digital data], [a court] would need to understand what protocols the government used, what
alternatives might have reasonably existed, and why the latter rather than the former might
have been more appropriate.” United States v Christie, 717 F3d 1156, 1167 (CA 10, 2013).
See also Loera, 923 F3d at 920.
21
   Total Recall, 49 Conn L Rev at 1777-1779; see also Herrera, 357 P3d at 1233
(concluding that the “abstract possibility” that files could be hidden or manipulated is
insufficient to justify searching the entire phone and noting that the prosecutor “did not
present a shred of evidence to suggest, nor did [he] attempt to argue,” that the defendant in
that case hid or manipulated his files).
22
   See Carey, 172 F3d at 1274 (“[E]ach of the files containing pornographic material was
labeled ‘JPG’ and most featured a sexually suggestive title. Certainly after opening the
first file and seeing an image of child pornography, the searching officer was aware—in
advance of opening the remaining files—what the label meant. When he opened the


                                              29
       To be clear, a court will generally need to engage in such a “totality-of-

circumstances” analysis to determine whether a search of digital data was reasonably

directed toward finding evidence of the criminal activities alleged in the warrant only if,

while searching digital data pursuant to a warrant for one crime, officers discover evidence

of a different crime without having obtained a second warrant and a prosecutor seeks to

use that evidence at a subsequent criminal prosecution. Courts should also keep in mind

that in the process of ferreting out incriminating digital data it is almost inevitable that

officers will have to review some data that is unrelated to the criminal activity alleged in

the authorizing warrant. United States v Richards, 659 F3d 527, 539 (CA 6, 2011) (“[O]n

occasion in the course of a reasonable search [of digital data], investigating officers may

examine, ‘at least cursorily,’ some ‘innocuous documents . . . in order to determine

whether they are, in fact, among those papers authorized to be seized.’ ”), quoting

Andresen, 427 US at 482 n 11. The fact that some data reviewed turns out to be related to

criminal activity not alleged in the authorizing warrant does not render that search per se

outside the scope of the warrant. So long as it is reasonable under all of the circumstances

for officers to believe that a particular piece of data will contain evidence relating to the

criminal activity identified in the warrant, officers may review that data, even if that data

ultimately provides evidence of criminal activity not identified in the warrant.

       In this case, the warrant authorized officers to search defendant’s digital data for

evidence of drug trafficking, or more specifically, for evidence of “any records pertaining



subsequent files, he knew he was not going to find items related to drug activity as specified
in the warrant . . . .”).


                                             30
to the receipt, possession and sale or distribution of controlled substances including but not

limited to documents, video tapes, computer disks, computer hard drives, and computer

peripherals.” The affidavit did not even mention Weber or the armed robbery of Stites, let

alone seek to establish probable cause that defendant committed armed robbery. As a

result, the warrant did not authorize a search of defendant’s data for evidence related to the

armed robbery.

       A month or so after the initial extraction of the data, the prosecutor in the armed-

robbery case asked Detective Wagrowski to use Cellebrite to conduct a focused review of

the seized data for (a) contacts with phone numbers of Weber and Stites and (b) data

containing the words “Lisa,” “killer” (and variations thereof), and “Kristopher.” The data

obtained from this review was admitted into evidence against defendant at his trials for

armed robbery.

       There was nothing in the warrant or affidavit to suggest that either Weber or Stites

was implicated in defendant’s drug trafficking or that reviewing data with Weber’s name

or contacts with her phone number would lead to evidence regarding defendant’s drug

trafficking. Similarly, there was nothing in the warrant or affidavit to suggest that

reviewing defendant’s data for the word “killer” or defendant’s name would uncover

evidence of drug trafficking. Furthermore, there was no evidence that defendant hid or

manipulated his files to conceal evidence related to his drug trafficking or that a review of

all defendant’s data to discover evidence of drug trafficking was reasonable in light of the

use and availability of Cellebrite to isolate relevant data. Therefore, this review was not

reasonably directed toward obtaining evidence of drug trafficking and exceeded the scope

of the warrant.


                                             31
       The prosecutor argues that this review was not beyond the scope of the warrant

because defendant allegedly was selling drugs to Weber around the time of the robbery.

The prosecutor reasons that defendant’s contacts with Weber were rooted in the same illicit

activity the warrant had targeted, i.e., drug trafficking. However, any connection between

Weber and defendant’s drug trafficking was not derived from the warrant or its supportive

affidavit. Rather, probable cause that defendant was dealing drugs was based on the tip

from a confidential informant that defendant and Pankey were dealing drugs. Therefore, a

keyword search of the data for drug references, drug-related items, or contacts with Pankey

would certainly have been reasonably directed at finding evidence of drug trafficking and

would have fallen well within the scope of the warrant.23 But there was no indication in

the warrant or its affidavit that the review conducted would uncover evidence of

defendant’s drug trafficking.24     Rather, the keyword searches were directed toward


23
   This list is merely illustrative and is not intended to identify all of the potential search
terms that would have fallen within the scope of the warrant. Nor is this list intended to
imply that officers were only permitted to review defendant’s data using search terms rather
than employing different search protocols or manually searching the data using other
criteria that were reasonably directed in light of the warrant and its affidavit toward finding
evidence related to drug trafficking.
24
   We do not mean to hold or imply that police officers are categorically precluded from
reviewing cell-phone contacts with a particular person merely because that person has not
been explicitly identified in the warrant or supportive affidavit. The evidence set forth for
establishing probable cause is but one consideration in determining whether a search of
cell-phone data was “reasonably directed” at uncovering evidence related to the crime
alleged in the warrant. Therefore, other considerations may well support an officer’s
review of contacts despite the absence of an express reference to that person in the warrant
or affidavit. For example, if, while searching cell-phone data for specific drug-related
terms or references used by the defendant, an officer discovers those terms or references
within cell-phone contacts, these may of course be reviewed. Further, if an officer were to
uncover evidence that digital files containing contacts with a particular person had been


                                              32
obtaining evidence that defendant committed an armed robbery based on evidence obtained

while investigating that armed robbery. Because the warrant did not authorize a search of

defendant’s data for evidence of armed robbery, these searches fell beyond the scope of the

warrant.

       To summarize, the officer’s review of defendant’s cell-phone data for evidence

relating to the armed robbery was beyond the scope of the warrant because there was no

indication in either the warrant or the affidavit that this review, conducted well after the

initial extraction of the data, would uncover evidence of drug trafficking. Additionally, a

review of the entirety of defendant’s data was unreasonable in light of the lack of evidence

that data concerning the drug activity was somehow hidden or manipulated and in light of

the officer’s ability to conduct a more focused review of the data using Cellebrite to isolate

and separate responsive and unresponsive materials. This is not a circumstance in which

the officer was reasonably reviewing data for evidence of drug trafficking and happened to

view data implicating defendant in other criminal activity. If such were the case and the

data’s “incriminating character [was] immediately apparent,” the plain-view exception

would likely apply and permit the state to use the evidence of criminal activity not alleged

in the warrant at a subsequent criminal prosecution. People v Champion, 452 Mich 92,




hidden, manipulated, or encoded in a manner intended to conceal the contacts, the officer
might also be justified in suspecting that there was evidence of criminal activity within
those contacts regardless of whether that person was referred to in the warrant or affidavit.
However, we discern no such considerations in the instant case that would justify the
searches of Weber or Stites.



                                             33
101; 549 NW2d 849 (1996), citing Horton, 496 US 128.25 Rather, this review was directed

exclusively toward finding evidence related to the armed-robbery charge, and it was

grounded in information obtained during investigation into that crime. Accordingly, this

review constituted a warrantless search that was unlawful under the Fourth Amendment.26


25
  The exception is not implicated in this case because “an essential predicate of the plain
view doctrine is that the initial intrusion not violate the Fourth Amendment” and the
officer’s search here did violate the Fourth Amendment because it was not reasonably
directed at uncovering evidence of the criminal activities alleged in the warrant. Galpin,
720 F3d at 451 (quotation marks omitted); see also United States v Gurczynski, 76 MJ 381,
388 (2017) (“A prerequisite for the application of the plain view doctrine is that the law
enforcement officers must have been conducting a lawful search when they stumbled upon
evidence in plain view. As noted, the officers in this case were not [doing so] because the
execution of the warrant was constitutionally unreasonable.”).
26
   Defendant contends the warrant was overly broad because it allowed officers to search
his cell phone for evidence of drug trafficking without limitation. In light of the privacy
interests implicated in digital data, some magistrates have been placing more specific
limitations upon a warrant to search digital data, such as “by (1) instituting time limits on
completion [of the search], (2) mandating return or deletion of non-responsive materials,
or (3) enumerating specific search protocol to be utilized during execution.” Regulating
Search Warrant Execution, 86 Fordham L Rev at 3001-3011; see also In re Search of 3817
W West End, First Floor Chicago, Illinois 60621, 321 F Supp 2d 953, 961 (ND Ill, 2004)
(requiring the government to provide a specific search protocol of digital data to satisfy the
particularity requirement of the Fourth Amendment). There is much debate regarding the
propriety and constitutionality of ex ante limitations on the manner in which officers may
search digital data for evidence. Compare The Post-Riley Search Warrant, 69 Vanderbilt
L Rev at 638 (“Imposing restrictions on search warrants—in the form of ex ante search
protocols and geographic restrictions on the applications police can search—is the best way
to ensure that cell phone warrants do not become the reviled general warrants the Fourth
Amendment’s particularity requirement was designed to prevent.”), with Kerr, Abstract,
Ex Ante Regulation of Computer Search and Seizure, 96 Va L Rev 1241, 1242, 1265, 1267-
1268 (2010) (“[E]x ante restrictions on the execution of computer warrants are
constitutionally unauthorized and unwise.”), citing United States v Grubbs, 547 US 90, 98;
126 S Ct 1494; 164 L Ed 2d 195 (2006) (“Nothing in the language of the Constitution or
in this Court’s decisions . . . suggests that . . . search warrants . . . must include a
specification of the precise manner in which they are to be executed.”) (quotation marks
omitted). But see In re Search Warrant, 193 Vt 51, 69; 71 A3d 1158 (2012) (holding that,


                                             34
                   B. INEFFECTIVE ASSISTANCE OF COUNSEL

       The final issue is whether trial counsel was ineffective when he failed to object

under the Fourth Amendment to the admission of the evidence obtained from defendant’s

cell-phone data.    The Court of Appeals rejected out-of-hand defendant’s claim of

ineffective assistance of counsel based on its conclusion that an objection under the Fourth

Amendment would have been futile. Hughes, unpub op at 3 n 2. We find it appropriate to

remand to the Court of Appeals to reconsider defendant’s claim in light of this opinion.

When making this determination, the Court of Appeals should consider whether the

violation of defendant’s Fourth Amendment rights entitled defendant to exclusion of the

unlawfully searched data from his armed-robbery trial. See Kimmelman v Morrison, 477

US 365, 375; 106 S Ct 2574; 91 L Ed 2d 305 (1986).27

although ex ante restrictions are not required, such restrictions on searches of digital data
“are sometimes acceptable mechanisms for ensuring the particularity of a search”).
“[G]iven the unique problem encountered in computer searches, and the practical
difficulties inherent in implementing universal search methodologies, the majority of
federal courts have eschewed the use of a specific search protocol and, instead, have
employed the Fourth Amendment’s bedrock principle of reasonableness on a case-by-case
basis . . . .” Richards, 659 F3d at 538 (citations omitted). We need not decide here whether
the warrant was overly broad because “putting aside for the moment the question what
limitations the Fourth Amendment’s particularity requirement should or should not impose
on the government ex ante, the Amendment’s protection against ‘unreasonable’ searches
surely allows courts to assess the propriety of the government’s search methods . . . ex post
in light of the specific circumstances of each case.” Christie, 717 F3d at 1166, citing
Ramirez, 523 US at 71. We conclude that, regardless of whether the warrant itself was
overly broad, the search of the data pursuant to that warrant was unreasonable and therefore
violated the Fourth Amendment.
27
   The general rule is that evidence obtained in violation of the Fourth Amendment cannot
be used against a defendant at a subsequent trial. See, e.g., United States v Council, 860
F3d 604, 608-609 (CA 8, 2017); Mapp v Ohio, 367 US 643, 655; 81 S Ct 1684; 6 L Ed 2d
1081 (1961) (applying the exclusionary rule to the states). However, the exclusionary rule
is a judicially created remedy that does not apply to every Fourth Amendment violation.


                                             35
                                   IV. CONCLUSION

       The ultimate holding of this opinion is simple and straightforward-- a warrant to

search a suspect’s digital cell-phone data for evidence of one crime does not enable a search

of that same data for evidence of another crime without obtaining a second warrant.

Nothing herein should be construed to restrict an officer’s ability to conduct a reasonably

thorough search of digital cell-phone data to uncover evidence of the criminal activity

alleged in a warrant, and an officer is not required to discontinue a search when he or she

discovers evidence of other criminal activity while reasonably searching for evidence of

the criminal activity alleged in the warrant. However, respect for the Fourth Amendment’s

requirement of particularity and the extensive privacy interests implicated by cell-phone

data as delineated by the United States Supreme Court’s decision in Riley v California

requires that officers reasonably limit the scope of their searches to evidence related to the

criminal activity alleged in the warrant and not employ that authorization as a basis for

seizing and searching digital data in the manner of a general warrant in search of evidence

of any and all criminal activity. We hold that, as with any other search, an officer must

limit a search of digital data from a cell phone in a manner reasonably directed to uncover



See, e.g., Utah v Strieff, 579 US ___, ___; 136 S Ct 2056, 2061; 195 L Ed 2d 400 (2016).
The prosecutor argues in this Court that if the warrant affidavit failed to establish a
sufficient nexus between defendant’s criminal activity and his cell phone, see note 6 of this
opinion, the exclusionary rule does not apply because the officers relied in good faith on
the district court judge’s finding of probable cause. See United States v Leon, 468 US 897;
104 S Ct 3405; 82 L Ed 2d 677 (1984) (holding that the exclusionary rule does not apply
if officers rely in good faith on a magistrate’s finding of probable cause to issue a warrant).
The prosecutor does not specifically argue that if the searches at issue exceeded the scope
of the warrant any exception to the exclusionary rule applies. The parties may develop this
issue further on remand.


                                              36
evidence of the criminal activity alleged in the warrant. We hereby reverse the judgment

of the Court of Appeals and remand to that Court to address whether defendant is entitled

to relief based upon the ineffective assistance of counsel.


                                                         Stephen J. Markman
                                                         Bridget M. McCormack
                                                         Brian K. Zahra
                                                         David F. Viviano
                                                         Richard H. Bernstein
                                                         Elizabeth T. Clement
                                                         Megan K. Cavanagh




                                             37
                             STATE OF MICHIGAN

                                      SUPREME COURT


    PEOPLE OF THE STATE OF MICHIGAN,

                Plaintiff-Appellee,

    v                                                           No. 158652

    KRISTOPHER ALLEN HUGHES,

                Defendant-Appellant.


VIVIANO, J. (concurring).
        I concur in the majority’s holding but write separately because I take issue with one

aspect of its reasoning. The majority identifies several factors that a court must consider

to determine whether a police officer’s search of seized digital cell-phone data is

reasonably directed at finding evidence of the criminal activity identified in the warrant.

See ante at 26-30. I do not take issue with the factors identified by the majority, at least to

the extent that they may apply in the cases to which they might be relevant.1 But I believe

the list is incomplete without the addition of another potentially dispositive factor: the

officer’s subjective intention in conducting the search. If the search was purposefully

conducted to obtain evidence of a crime other than the one identified in the warrant, I do

not see how we can conclude that same search was “ ‘reasonably directed at uncovering’

evidence of the criminal activity alleged in the warrant.” Ante at 22.



1
  It is worth pointing out that, with the exception of Factor (h), the majority does not
reference the factors or apply them in its analysis.
       Citing conflicting caselaw from the federal circuit courts, the majority expressly

declines to address whether the officer’s subjective intention is relevant to the inquiry. See

note 13 of the majority opinion (comparing United States v Loera, 923 F3d 907 (CA 10,

2019), and United States v Williams, 592 F3d 511 (CA 4, 2010)). In Loera, the court

persuasively explained why such a restriction is needed in the context of searches of

electronic storage devices:

       The general Fourth Amendment rule is that investigators executing a warrant
       can look anywhere where evidence described in the warrant might
       conceivably be located.

                                           * * *

       This limitation works well in the physical-search context to ensure that
       searches pursuant to warrants remain narrowly tailored, but it is less effective
       in the electronic-search context where searches confront what one
       commentator has called the “needle-in-a-haystack” problem. Given the
       enormous amount of data that computers can store and the infinite places
       within a computer that electronic evidence might conceivably be located, the
       traditional rule risks allowing unlimited electronic searches.

               To deal with this problem, rather than focusing our analysis of the
       reasonableness of an electronic search on “what” a particular warrant
       permitted the government agents to search (i.e., “a computer” or “a hard
       drive”), we have focused on “how” the agents carried out the search, that is,
       the reasonableness of the search method the government employed. Our
       electronic search precedents demonstrate a shift away from considering what
       digital location was searched and toward considering whether the forensic
       steps of the search process were reasonably directed at uncovering the
       evidence specified in the search warrant. Shifting our focus in this way is
       necessary in the electronic search context because search warrants typically
       contain few—if any—restrictions on where within a computer or other
       electronic storage device the government is permitted to search. Because it
       is “unrealistic to expect a warrant prospectively [to] restrict the scope of a
       search by directory, filename or extension or to attempt to structure search
       methods,” our [ex post] assessment of the propriety of a government search
       is essential to ensuring that the Fourth Amendment’s protections are realized



                                              2
       in this context. [Loera, 923 F3d at 916-917 (citations and emphasis omitted;
       first alteration in original).]

Later, in a footnote, the court acknowledged that inadvertence was abandoned as a

necessary condition for a legitimate plain-view seizure in Horton v California, 496 US 128,

130, 139; 110 S Ct 2301; 110 L Ed 2d 112 (1990), but explained that it persisted in

“includ[ing] inadvertence as a factor to consider when deciding whether an electronic

search fell within the scope of its authorizing warrant or outside of it [because of] . . . [t]he

fundamental differences between electronic searches and physical searches, including the

fact that electronic search warrants are less likely prospectively to restrict the scope of the

search . . . .” Loera, 923 F3d at 920 n 3.

       A different approach was taken by the court in Williams, which was decided prior

to Riley v California, 573 US 373; 134 S Ct 2473; 189 L Ed 2d 430 (2014). In that case,

in examining the plain-view exception, the court held that a warrant authorizing a search

of a computer and digital storage device “impliedly authorized officers to open each file

on the computer and view its contents, at least cursorily, to determine whether the file fell

within the scope of the warrant’s authorization . . . .” Williams, 592 F3d at 521. See also

id. at 522 (“Once it is accepted that a computer search must, by implication, authorize at

least a cursory review of each file on the computer, then the criteria for applying the plain-

view exception are readily satisfied.”).           Citing Horton, the court concluded that

“[i]nadvertence focuses incorrectly on the subjective motivations of the officer in

conducting the search and not on the objective determination of whether the search is

authorized by the warrant or a valid exception to the warrant requirement.” Id. at 523. The

court made it very clear that it would not adopt new rules to govern the search and seizure



                                               3
of electronic files: “At bottom, we conclude that the sheer amount of information contained

on a computer does not distinguish the authorized search of the computer from an

analogous search of a file cabinet containing a large number of documents.” Id. at 523.

       Williams’s approach is less persuasive in light of Riley. As the majority notes,

“Riley distinguished cell-phone data from other items subject to a search incident to a

lawful arrest in terms of the privacy interests at stake.” Ante at 15, citing Riley, 573 US at

393. In Riley, the government argued that a search of all data stored on a cell phone is

“materially indistinguishable” from searches of other items found on an arrestee’s person.

Riley, 573 US at 393. Apparently not impressed with this argument, the Court responded

tartly: “That is like saying a ride on horseback is materially indistinguishable from a flight

to the moon.” Id. The Court observed that “[o]ne of the most notable distinguishing

features of modern cell phones is their immense storage capacity,” noting that “[t]he

current top-selling smart phone has a standard capacity of 16 gigabytes . . . [which]

translates to millions of pages of text, thousands of pictures, or hundreds of videos.” Id. at

393-394 (citation omitted). The rule adopted in Loera, which was decided after Riley,

accounts for the realities of modern electronic storage devices. These privacy concerns are

only heightened when it comes to the types and volume of data contained on modern smart

phones, as the majority ably explains. See ante at 10-11, quoting Riley, 573 US at 393,

395-396.

       Following the approach in Loera, I would adopt inadvertence as a factor to consider

when deciding whether an electronic search fell within the scope of its authorizing warrant.

Here, I would find that factor dispositive since it was clear that the second search of

defendant’s cell phone was conducted to obtain evidence of a crime other than the drug-


                                              4
trafficking offense identified in the warrant. At the time of the second search, the only

crime defendant was charged with arising out of the August 6 incident was armed robbery.

The prosecutor assigned to the armed-robbery case requested that the second search be

conducted to obtain evidence to support that charge. Therefore, for this separate reason, I

agree with the majority that the second search was beyond the scope of the warrant because

it was not “reasonably directed at uncovering” evidence of drug trafficking.

       Instead of relying on the lack of inadvertence, however, the majority focuses on

whether there was any indication in the warrant or affidavit that that the searches performed

would uncover evidence of defendant’s drug transactions with Weber or Stites. See ante

at 31 (“There was nothing in the warrant or affidavit to suggest that either Weber or Stites

was implicated in defendant’s drug trafficking or that reviewing data with Weber’s name

or contacts with her phone number would lead to evidence regarding defendant’s drug

trafficking.”); ante at 32 (“[A]ny connection between Weber and defendant’s drug

trafficking was not derived from the warrant or its supportive affidavit.”). But I do not

believe that a search warrant or the affidavit supporting it has to specify the participants of

each drug transaction for that evidence to be within the scope of a drug-trafficking warrant.2

2
  See United States v Castro, 881 F3d 961, 966 (CA 6, 2018) (citation omitted) (“Officers
may conduct a more detailed search of an electronic device after it was properly seized so
long as the later search does not exceed the probable cause articulated in the original
warrant and the device remained secured.”). If, for example, defendant had been charged
with or was being investigated for a drug crime arising out of the August 6 incident, in my
view, nothing would have precluded law enforcement officers from conducting a more
detailed search of the properly seized cell-phone data using the new information they
obtained concerning this additional instance of drug trafficking. See id. (“It is sometimes
the case, as it was the case here, that law enforcement officers have good reason to revisit
previously seized, and still secured, evidence as new information casts new light on the
previously seized evidence.”). As the prosecutor points out, defendant’s interactions with


                                              5
Such a requirement would go well beyond prospectively “considering whether the forensic

steps of the search process were reasonably directed at uncovering the evidence specified

in the search warrant.” Loera, 923 F3d at 917.3

       Under the circumstances of this case, before conducting another search of

defendant’s cell phone, the officer should have obtained a second search warrant directed

toward obtaining evidence of the armed-robbery offense. Because he did not, I concur with

the majority that the second search was unlawful under the Fourth Amendment.4


                                                         David F. Viviano




Weber and Stites on August 6 included the purchase and sale of illegal drugs. And once
the evidence has been properly obtained, there is nothing that would prevent it from being
used to prove a separate crime. See Williams, 592 F3d at 520, quoting United States v
Phillips, 588 F3d 218, 224 (CA 4, 2009) (“ ‘Courts have never held that a search is overly
broad merely because it results in additional criminal charges.’ ”). But we are not
confronted with that situation. Instead, it is clear that the second search was conducted to
obtain evidence of the alleged armed robbery.
3
  The majority’s reliance on this factor is perplexing for an additional reason: it is not one
of the factors identified by the majority for determining whether a search is beyond the
scope of the warrant. And I fear that it may lead to confusion about whether the absence
of such details will constitute grounds to challenge the search and seizure of any drug-
trafficking evidence that is not specifically referred to in the search warrant or affidavit.
4
  It appears that a plausible claim could be made that the government would have inevitably
discovered the evidence contained on defendant’s cell phone through lawful means given
that the cell phone was lawfully in the government’s possession. See Loera, 923 F3d at
928 (“When evidence is obtained in violation of the Fourth Amendment, that evidence
need not be suppressed if agents inevitably would have discovered it through lawful means
independent from the unconstitutional search.”). But since no such claim has been raised,
I decline to consider it further.


                                              6

```

---

## GROUP: content/cases/Perttu v. Richards.md  (`case`, 5 assertions)

### content_page

```
---
title: Perttu v. Richards
type: case
citation: "605 U.S. 460 (2025)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2025
date_decided: ""
docket: 23-1324
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
  opinion_url: "https://www.courtlistener.com/opinion/10776832/perttu-v-richards/"
  cluster_id: 10776832
  opinion_id: null
  identity_checked: true
lake:
  record_id: Perttu v. Richards
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - section-1983
  - plra
  - seventh-amendment
  - first-amendment-retaliation
holding: "When a dispute over PLRA exhaustion is intertwined with the merits of a claim carrying a Seventh Amendment jury-trial right, the parties are entitled to a jury trial on the exhaustion question rather than a bench determination by the judge."
---

# Perttu v. Richards

*605 U.S. 460 (2025)* (No. 23-1324) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10776832 → opinion 11243419; quote string-matched to the CL opinion text 2026-07-07 (CL preliminary print carries U.S. Reports pagination). S9 promotes. -->

## Background
Kyle Richards, a Michigan prisoner, sued prison employee Thomas Perttu under 42 U.S.C. § 1983, alleging that Perttu sexually abused him and other inmates and then destroyed the grievance forms Richards tried to file about the abuse and retaliated against him for filing — violating Richards's First Amendment right to file grievances. Perttu moved for summary judgment, arguing the plaintiffs had failed to exhaust available grievance procedures as the Prison Litigation Reform Act (PLRA) requires. A magistrate judge held an evidentiary hearing, found Richards's witnesses on the destruction-of-grievances issue "lacked credibility," and recommended dismissal for failure to exhaust; the district court adopted that recommendation. The same disputed fact — whether Perttu destroyed the grievances — governed both exhaustion and the First Amendment merits. The Sixth Circuit reversed.

## Issue
Whether a party has a right to a jury trial on PLRA exhaustion when that dispute is intertwined with the merits of a claim that requires a jury trial under the Seventh Amendment.

## Rule
PLRA exhaustion is an ordinary [[Common Legal Terms#affirmative-defense|affirmative defense]], and the PLRA is silent on whether a judge or a jury resolves exhaustion disputes. Congress legislates against a background of common-law adjudicatory principles under which factual disputes intertwined with jury-triable legal claims go to the jury (*Beacon Theatres*; *Smithers*), and that silence is "strong evidence that the usual practice should be followed." The Court therefore held: "For those reasons, we hold as a matter of statutory interpretation that parties have a right to a jury trial on PLRA exhaustion when that issue is intertwined with the merits of a claim that falls under the Seventh Amendment." — 605 U.S. at 468. ^pin-468

## Application
Whether Perttu destroyed Richards's grievances decided both the exhaustion defense and the First Amendment retaliation claim — a legal claim triable to a jury. Because those questions were intertwined, the district court could not resolve the shared fact at a bench hearing and then dismiss for non-exhaustion; the intertwined factual dispute had to be tried to a jury. The Court construed the PLRA to require that result and so did not reach whether the Seventh Amendment would independently compel it.

## Conclusion
The judgment of the Sixth Circuit was **affirmed**. Roberts, C.J., delivered the opinion of the Court, joined by Sotomayor, Kagan, Gorsuch, and Jackson, JJ.; Barrett, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Thomas, Alito, and Kavanaugh, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Perttu* is a procedural decision at the § 1983 prisoner-litigation gate: it keeps a jury, not the judge, as the factfinder when a PLRA exhaustion dispute and a jury-triable constitutional claim rise or fall on the same disputed fact.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Perttu v. Richards*, 605 U.S. 460 (2025)](https://www.courtlistener.com/opinion/10776832/perttu-v-richards/) — pinpoint: 468 (Opinion of the Court, holding; Roberts, C.J.); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f807754aee0726e9", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "605 U.S. 460 (2025)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Perttu v. Richards", "year": "2025"}}
{"assertion_id": "0c9ce775183e3582", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Recent development", "title": "Perttu v. Richards"}}
{"assertion_id": "8bf8211ae1dafec9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "When a dispute over PLRA exhaustion is intertwined with the merits of a claim carrying a Seventh Amendment jury-trial right, the parties are entitled to a jury trial on the exhaustion question rather than a bench determination by the judge.", "title": "Perttu v. Richards"}}
{"assertion_id": "0f35bbfb4d7787ce", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Perttu v. Richards", "varies_by_point": "false"}}
{"assertion_id": "2f57f2ad37eca932", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Perttu v. Richards"}}
```

### lake record — Perttu v. Richards

```json
{
  "schema_version": "s2.v1",
  "record_id": "Perttu v. Richards",
  "status": "under_review",
  "identity": {
    "case_name": "Perttu v. Richards",
    "case_name_short": "Perttu",
    "case_name_full": "",
    "input_case_name": "Perttu v. Richards",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2025,
    "docket": "23-1324",
    "cluster_id": 10776832,
    "lead_opinion_id": 11243419,
    "sibling_ids": [],
    "absolute_url": "/opinion/10776832/perttu-v-richards/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "605 U.S. 460",
      "volume": "605",
      "reporter": "U.S.",
      "page": "460",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "605 U.S. 460",
        "volume": "605",
        "reporter": "U.S.",
        "page": "460",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "605 U.S. 460",
    "official_selection": {
      "court_class": "scotus",
      "selected": "605 U.S. 460",
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
    "date_created": "2026-07-06T12:12:42Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:12:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:12:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "perttu-v-richards--10776832",
      "to_record_id": "Perttu v. Richards",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Perttu v. Richards

```
                   PRELIMINARY PRINT

              Volume 605 U. S. Part 2
                             Pages 460–494




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                                June 18, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
460                     OCTOBER TERM, 2024

                                Syllabus


                     PERTTU v. RICHARDS

certiorari to the united states court of appeals for
                  the sixth circuit
      No. 23–1324 Argued February 25, 2025—Decided June 18, 2025
The Prison Litigation Reform Act (PLRA) requires prisoners with com-
  plaints about prison conditions to exhaust available grievance proce-
  dures before fling suit in federal court. 42 U. S. C. § 1997e(a). But
  “exhaustion is not required” when a prison administrator “threaten[s]
  individual inmates so as to prevent their use of otherwise proper proce-
  dures.” Ross v. Blake, 578 U. S. 632, 644. “Such interference with an
  inmate's pursuit of relief renders the administrative process unavail-
  able,” so “§ 1997e(a) poses no bar” to suit. Ibid. The question pre-
  sented is whether a party has a right to a jury trial on PLRA exhaustion
  when that dispute is intertwined with the merits of the underlying suit.
    In this case, inmate Kyle Richards alleges that Thomas Perttu, a
  prison employee, sexually harassed Richards and other inmates. Rich-
  ards also alleges that, when he attempted to fle grievance documents
Page Proof Pending Publication
  about the abuse, Perttu destroyed them and “retaliated against” him for
  attempting to fle them. Richards sued Perttu under 42 U. S. C. § 1983
  for violating his constitutional rights, including his First Amendment
  right to fle grievances. Perttu moved for summary judgment, arguing
  that the plaintiffs had failed to exhaust available grievance procedures
  as required by the PLRA. The Magistrate Judge concluded that there
  was “a genuine issue of fact as to whether Plaintiffs were excused from
  properly exhausting their claims due to interference by Perttu” and that
  the issue was “appropriate for resolution during an evidentiary hear-
  ing.” App. to Pet. for Cert. 86a. At that hearing, the Magistrate
  Judge concluded that Richards's witnesses regarding Perttu's alleged
  destruction of grievance forms “lacked credibility.” The Magistrate
  Judge recommended dismissal without prejudice for failure to exhaust,
  and the District Court adopted that recommendation. The Sixth Cir-
  cuit reversed. It stated that there was “no doubt that a judge may
  otherwise resolve factual disputes regarding exhaustion under the
  PLRA,” but it held that “the Seventh Amendment requires a jury trial
  when the resolution of the exhaustion issue under the PLRA would also
  resolve a genuine dispute of material fact regarding the merits of the
  plaintiff 's substantive case.” 96 F. 4th 911, 917, 923. That decision
  conficted with Seventh Circuit precedent.
                       Cite as: 605 U. S. 460 (2025)                   461

                                 Syllabus

Held: Parties are entitled to a jury trial on PLRA exhaustion when that
 issue is intertwined with the merits of a claim that requires a jury trial
 under the Seventh Amendment. Pp. 467–479.
    (a) Before reaching Richards's arguments for why his Seventh
 Amendment right to a jury trial has been violated, the Court must frst
 determine whether a construction of the PLRA is “fairly possible” by
 which the constitutional question may be avoided. Monterey v. Del
 Monte Dunes at Monterey, Ltd., 526 U. S. 687, 707. Such a construc-
 tion is possible here. Because the Court construes the PLRA to re-
 quire a jury trial in Richards's case, the Court need not address whether
 Congress could have required otherwise in the PLRA without violating
 the Seventh Amendment.
    PLRA exhaustion is a standard affrmative defense subject to “the
 usual practice” under the Federal Rules of Civil Procedure. Jones v.
 Bock, 549 U. S. 199, 212. The usual practice is that factual disputes
 regarding legal claims go to the jury, even if that means a judge must let
 a jury decide questions he could ordinarily resolve on his own. Beacon
 Theatres, Inc. v. Westover, 359 U. S. 500, 510–511. That usual practice
 matters for interpreting the PLRA because “Congress is understood to
 legislate against a background of common-law adjudicatory principles
 . . . with an expectation that the principle[s] will apply except `when a
Page Proof Pending Publication
 statutory purpose to the contrary is evident.' ” Astoria Fed. Sav. &
 Loan Assn. v. Solimino, 501 U. S. 104, 108 (quoting Isbrandtsen Co. v.
 Johnson, 343 U. S. 779, 783). No such contrary purpose is evident in the
 PLRA. The PLRA is “silent” on whether judges or juries should resolve
 exhaustion disputes, and that silence is “strong evidence that the usual
 practice should be followed.” Jones, 549 U. S., at 212. Pp. 467–470.
    (b) At the time the PLRA was enacted, it was well established that
 factual disputes intertwined with claims that fall under the Seventh
 Amendment should go to a jury. The Court has held in various con-
 texts that, in cases of intertwinement, district courts should structure
 their order of operations to preserve the jury trial right. Pp. 470–474.
       (1) One prominent line of cases involves suits that contain both
 legal and equitable claims. Ordinarily, judges resolve equitable claims
 and juries resolve legal claims. In Beacon Theatres, this Court held
 that judges may not resolve equitable claims frst if doing so could pre-
 vent legal claims from getting to the jury. In that case, both the legal
 and equitable claims hinged on the “common issue” whether there was
 an antitrust violation. 359 U. S. 500, 503. The Court emphasized that
 in that situation, judicial “discretion is very narrowly limited and must,
 wherever possible, be exercised to preserve jury trial.” Id., at 510.
 Because resolving the equitable claims could “prevent a full jury trial”
462                     PERTTU v. RICHARDS

                                 Syllabus

 on the legal claims, the legal claims frst needed to be resolved by a jury.
 Id., at 505, 508. In this case, the parties agree that the exhaustion
 and First Amendment questions depend on common factual issues, and
 Beacon Theatres teaches that a trial court must preserve the jury trial
 in such a situation whenever possible. Nothing in the PLRA prevents
 holding a jury trial here. Pp. 471–472.
       (2) Cases involving subject matter jurisdiction are also instructive.
 Ordinarily, judges may resolve factual disputes when determining sub-
 ject matter jurisdiction. But courts may not do so when the factual
 disputes are intertwined with the merits. In Smithers v. Smith, 204
 U. S. 632, the Court held that judicial authority to dismiss for lack of
 subject matter jurisdiction “obviously is not unlimited,” for that would
 risk summarily determining the merits “without the ordinary incidents
 of a trial, including the right to a jury.” Id., at 645. In Land v. Dollar,
 330 U. S. 731, the Court found that Land was “the type of case where
 the question of jurisdiction is dependent on decision of the merits” and
 thus held the District Court should have “proceed[ed] to a decision on
 the merits.” Id., at 735, 738–739.
    In its decision below, the Sixth Circuit relied on its precedent applying
 Land, reasoning that if “certain cases [must] be heard and determined
 on the merits even when constitutionally implicated jurisdictional dis-
Page Proof Pending Publication
 putes” are at play, then “the result should be the same when the lesser
 concern of an affrmative defense, such as the PLRA's requirement to
 exhaust administrative remedies, implicates the merits of a claim.” 96
 F. 4th, at 923. The Court fnds this reasoning persuasive. After all,
 when the PLRA was enacted, many lower court decisions and treatises
 had extended the intertwinement principle to other threshold questions,
 like personal jurisdiction and venue. The Court expresses no view
 today on whether lower courts have been correct to extend the inter-
 twinement principle to these other issues, but simply notes that these
 cases—along with Beacon Theatres and Smithers—show that when the
 PLRA was enacted, the usual practice in the federal courts across a
 variety of contexts was to resolve factual disputes that are intertwined
 with the merits at the merits stage. Pp. 472–474.
    (c) Perttu's counterarguments are unpersuasive. Perttu argues that
 Beacon Theatres is inapplicable, but his argument relies on the question-
 able assumption that judicial factual fndings concerning exhaustion
 have no estoppel effect in later jury trials. Regardless, even if Perttu
 is correct about estoppel, Beacon Theatres still applies when judicial
 resolution might prevent a full jury trial for other reasons. Here, Rich-
 ards's claim is being dismissed entirely rather than just estopped, and
 it is usually impossible for prisoners to go back and exhaust then fle
 suit again, because grievance deadlines will have long since passed.
                       Cite as: 605 U. S. 460 (2025)                   463

                                 Syllabus

  Perttu's argument that jury trials confict with the PLRA's purpose of
  conserving judicial resources also fails, because the PLRA contemplates
  that merits claims will be resolved by a jury and is silent about exhaus-
  tion. The usual federal court practice in cases of intertwinement is to
  send common issues to the jury, and nothing in the PLRA suggests
  Congress intended to depart from that practice. Pp. 474–478.
96 F. 4th 911, affrmed.
   Roberts, C. J., delivered the opinion of the Court, in which Sotomayor,
Kagan, Gorsuch, and Jackson, JJ., joined. Barrett, J., fled a dissent-
ing opinion, in which Thomas, Alito, and Kavanaugh, JJ., joined, post,
p. 479.

  Ann M. Sherman, Solicitor General of Michigan, argued
the cause for petitioner. With her on the briefs were Kyla
L. Barranco, Assistant Solicitor General, and Joshua S.
Smith, Assistant Attorney General.
  Lori Alvino McGill argued the cause for respondent.
With her on the brief was J. Scott Ballenger.*
  *Briefs of amici curiae urging reversal were fled for the State of Ohio
Page
et al. by DaveProof        Pending
               Yost, Attorney                   Publication
                              General of Ohio, T. Elliot Gaiser, Solicitor
General, Zachery P. Keller, Deputy Solicitor General, and Daniel McKit-
rick and Brandon Kennedy, Assistant Attorneys General, and by the At-
torneys General for their respective jurisdictions as follows: Steve Mar-
shall of Alabama, Tim Griffn of Arkansas, William Tong of Connecticut,
Brian L. Schwalb of the District of Columbia, Ashley Moody of Florida,
Christopher M. Carr of Georgia, Raúl R. Labrador of Idaho, Theodore E.
Rokita of Indiana, Brenna Bird of Iowa, Kris Kobach of Kansas, Russell
Coleman of Kentucky, Elizabeth B. Murrill of Louisiana, Anthony G.
Brown of Maryland, Lynn Fitch of Mississippi, Austin Knudsen of Mon-
tana, Michael T. Hilgers of Nebraska, Gentner Drummond of Oklahoma,
Ellen F. Rosenblum of Oregon, Peter F. Neronha of Rhode Island, Alan
Wilson of South Carolina, Marty Jackley of South Dakota, Jonathan
Skrmetti of Tennessee, Ken Paxton of Texas, and Sean D. Reyes of Utah;
for the International Municipal Lawyers Association et al. by F. Andrew
Hessick, Richard A. Simpson, Amanda Karras, and Erich Eiselt; and for
the National Sheriffs' Association et al. by Gregory C. Champagne and
Maurice E. Bostick.
  Briefs of amici curiae urging affrmance were fled for the American
Civil Liberties Union et al. by Jennifer A. Wedekind, Cecillia D. Wang,
and Daniel S. Korobkin; for the Cato Institute by Clark M. Neily III and
Matthew Cavedon; and for Law Professors by Kevin K. Russell.
464                 PERTTU v. RICHARDS

                      Opinion of the Court

  Chief Justice Roberts delivered the opinion of the
Court.
   The Prison Litigation Reform Act of 1995 (PLRA) re-
quires prisoners with complaints about prison conditions to
exhaust available grievance procedures before bringing suit
in federal court. 42 U. S. C. § 1997e(a). In some cases the
question whether a prisoner has exhausted those procedures
is intertwined with the merits of the prisoner's lawsuit. Re-
spondent Kyle Richards is a prisoner in Michigan. He al-
leges that he was sexually abused by petitioner Thomas
Perttu, a prison employee. He also alleges that when he
tried to fle grievance forms about the abuse, Perttu de-
stroyed them and threatened to kill him if he fled more.
   Richards sued Perttu for violating his constitutional
rights, including his First Amendment right to fle griev-
ances. Perttu responded that Richards had failed to ex-
haust available grievance procedures as required by the
Page Proof Pending Publication
PLRA. The parties agree that the exhaustion and First
Amendment issues are intertwined, because both depend on
whether Perttu did in fact destroy Richards's grievances and
retaliate against him. The question presented is whether a
party has a right to a jury trial on PLRA exhaustion when
that dispute is intertwined with the merits of the underly-
ing suit.
                              I
                              A
   “Our legal system [is] committed to guaranteeing that pris-
oner claims of illegal conduct by their custodians are fairly
handled according to law.” Jones v. Bock, 549 U. S. 199, 203
(2007). “The challenge,” however, “lies in ensuring that the
food of nonmeritorious claims does not submerge and effec-
tively preclude consideration of the allegations with merit.”
Ibid. To address that challenge, Congress enacted the Prison
Litigation Reform Act of 1995, 110 Stat. 1321–71, as amended,
42 U. S. C. § 1997e, which aims to “reduce the quantity and im-
                   Cite as: 605 U. S. 460 (2025)            465

                      Opinion of the Court

prove the quality of prisoner suits.” Porter v. Nussle, 534
U. S. 516, 524 (2002).
  A “centerpiece” of the PLRA is its exhaustion provision.
Woodford v. Ngo, 548 U. S. 81, 84 (2006). It provides:
    “No action shall be brought with respect to prison condi-
    tions under [42 U. S. C. § 1983], or any other Federal law,
    by a prisoner confned in any jail, prison, or other correc-
    tional facility until such administrative remedies as are
    available are exhausted.” § 1997e(a).
We have held that this provision “requires proper exhaus-
tion” of available prison grievance procedures, meaning a
prisoner “must complete the administrative review process
in accordance with the applicable procedural rules . . . as a
precondition to bringing suit in federal court.” Woodford,
548 U. S., at 88, 93. But “exhaustion is not required” when
a prison administrator “threaten[s] individual inmates so as
to prevent their use of otherwise proper procedures.” Ross
Page Proof Pending Publication
v. Blake, 578 U. S. 632, 644 (2016). As we have explained,
“such interference with an inmate's pursuit of relief renders
the administrative process unavailable,” so “§ 1997e(a) poses
no bar” to suit. Ibid.
                              B
   In 2020, Richards and two other prisoners fled this suit
against Perttu under 42 U. S. C. § 1983. The complaint al-
leged that, over the prior year, Perttu had “engaged in a
pattern of prolifc and repetitive sexual abuse, against at
least a dozen inmates,” in violation of their constitutional
rights. App. 2–3. The complaint also alleged that the
plaintiffs had “attempted to exhaust remedies to the best of
[their] ability” but had been “threatened and retaliated
against” for doing so. Id., at 2, 13. The complaint listed
specifc incidents in which Perttu allegedly ripped up the
plaintiffs' grievance forms, threw them away, and threatened
to kill the plaintiffs if they fled more. Id., at 13–18. The
plaintiffs also alleged they were being “wrongfully held in
466                 PERTTU v. RICHARDS

                      Opinion of the Court

administrative segregation in retaliation for fling griev-
ances” and that Perttu was retaliating against them in other
ways, all in violation of their First Amendment rights. Id.,
at 18–27.
   Perttu moved for summary judgment, arguing that the
plaintiffs had failed to exhaust available grievance proce-
dures as required by the PLRA. To support his motion,
Perttu submitted an affdavit from a prison grievance coordi-
nator attesting that there was no record evidence of the
plaintiffs fling grievances about sexual abuse by Perttu in
2019 or 2020. The plaintiffs responded by reiterating that
Perttu had intercepted and destroyed those grievances and
had warned them not to fle more. The Magistrate Judge
concluded that there was “a genuine issue of fact as to
whether Plaintiffs were excused from properly exhausting
their claims due to interference by Perttu” and that the issue
was “appropriate for resolution during an evidentiary hear-
ing.” App. to Pet. for Cert. 86a.
Page Proof Pending Publication
   The Magistrate Judge held the evidentiary hearing by
video conference in November 2021. App. 88. Richards,
representing himself, conducted direct examinations of mul-
tiple witnesses who testifed that they had seen Perttu de-
stroy Richards's grievance forms and retaliate against him
for fling them. See, e.g., id., at 210–214, 230, 234–238, 250–
255. Perttu denied doing so. Id., at 339–341. The Magis-
trate Judge concluded that Richards's witnesses “lacked
credibility” because their testimony “was either substan-
tially guided by Richards's manner of questioning or wholly
conclusory.” App. to Pet. for Cert. 69a. The Magistrate
Judge therefore recommended the case be dismissed without
prejudice for failure to exhaust. Id., at 76a. The District
Court adopted the recommendation. Id., at 28a–29a.

                               C
  Richards appealed to the Sixth Circuit. Still representing
himself, he argued that resolving exhaustion through “a
                   Cite as: 605 U. S. 460 (2025)             467

                      Opinion of the Court

bench trial”—one before a judge without a jury—is “not per-
missible where it would essentially be resolving a claim it-
self.” Brief for Appellant in No. 22–1298, p. 1. After ap-
pointing counsel for Richards and requesting supplemental
briefng, the Sixth Circuit reversed. It acknowledged that,
under Circuit precedent, there was “no doubt that a judge
may otherwise resolve factual disputes regarding exhaustion
under the PLRA.” 96 F. 4th 911, 917 (2024) (citing Lee v.
Willey, 789 F. 3d 673, 677 (CA6 2015)). But the court held
that “the Seventh Amendment requires a jury trial when the
resolution of the exhaustion issue under the PLRA would
also resolve a genuine dispute of material fact regarding the
merits of the plaintiff's substantive case.” 96 F. 4th, at 923.
That decision conficted with a contrary holding on the same
question from the Seventh Circuit, see Pavey v. Conley, 544
F. 3d 739, 742 (2008), and we granted certiorari to resolve
the split. 603 U. S. 949 (2024).

Page Proof Pending
             II    Publication
   “The right to trial by jury is `of such importance and occu-
pies so frm a place in our history and jurisprudence that any
seeming curtailment of the right' has always been and
`should be scrutinized with the utmost care.' ” SEC v. Jark-
esy, 603 U. S. 109, 121 (2024) (quoting Dimick v. Schiedt, 293
U. S. 474, 486 (1935)). Richards makes two arguments for
why his Seventh Amendment right to a jury trial has been
violated here. First, he argues that the dispute over ex-
haustion in this case is intertwined with a claim that falls
squarely under the Seventh Amendment—his First Amend-
ment retaliation claim for damages under § 1983—and that
factual questions related to that claim must be resolved by
a jury. See Monterey v. Del Monte Dunes at Monterey,
Ltd., 526 U. S. 687, 709, 720–721 (1999) (holding that “a § 1983
suit seeking legal relief is an action at law within the mean-
ing of the Seventh Amendment” and that a “predominantly
factual question” in such an action is “for the jury”). Sec-
468                 PERTTU v. RICHARDS

                      Opinion of the Court

ond, Richards makes a broader argument that, based on the
historical test in Markman v. Westview Instruments, Inc.,
517 U. S. 370 (1996), the Seventh Amendment requires a jury
trial for all factual disputes related to PLRA exhaustion,
even those not intertwined with the merits.
   Our precedents make clear that “[b]efore inquiring into
the applicability of the Seventh Amendment, we must `frst
ascertain whether a construction of the statute is fairly
possible by which the [constitutional] question may be
avoided.' ” Del Monte Dunes, 526 U. S., at 707 (quoting Felt-
ner v. Columbia Pictures Television, Inc., 523 U. S. 340, 345
(1998)). Such a construction is possible here. PLRA ex-
haustion is an affrmative defense subject to “the usual prac-
tice under the Federal Rules [of Civil Procedure].” Jones,
549 U. S., at 212. The usual practice is that factual disputes
regarding the merits of a legal claim go to the jury, even if
that means a judge must let a jury decide questions he could
Page Proof Pending Publication
ordinarily decide on his own. See Beacon Theatres, Inc. v.
Westover, 359 U. S. 500, 510–511 (1959). That usual practice
matters for interpreting the statute because “Congress is un-
derstood to legislate against a background of common-law
adjudicatory principles . . . with an expectation that the prin-
ciple[s] will apply except `when a statutory purpose to the
contrary is evident.' ” Astoria Fed. Sav. & Loan Assn. v.
Solimino, 501 U. S. 104, 108 (1991) (quoting Isbrandtsen Co.
v. Johnson, 343 U. S. 779, 783 (1952)). No such contrary pur-
pose is evident in the PLRA.
   For those reasons, we hold as a matter of statutory inter-
pretation that parties have a right to a jury trial on PLRA
exhaustion when that issue is intertwined with the merits of
a claim that falls under the Seventh Amendment. In light
of this holding, we express no view today on whether Con-
gress could have required otherwise in the PLRA without
violating a party's Seventh Amendment right to a jury trial.
See Byrd v. Blue Ridge Rural Elec. Cooperative, Inc., 356
U. S. 525, 537, and n. 10 (1958) (holding that affrmative de-
                       Cite as: 605 U. S. 460 (2025)                    469

                           Opinion of the Court

fense should go to jury due to “the manner in which [the
federal system] distributes trial functions between judge and
jury,” making it “unnecessary” to consider “the constitu-
tional question”).1
                               A
   We begin with a settled premise: PLRA exhaustion is a
standard affrmative defense. Jones, 549 U. S., at 216. As
we said in Woodford, 548 U. S., at 101, PLRA exhaustion is
“not jurisdictional,” which is why “a district court [is al-
lowed] to dismiss plainly meritless claims without frst ad-
dressing” the often “more complex question” of exhaustion.
And as we said in Jones, 549 U. S., at 216, PLRA exhaustion
is not a “pleading requirement,” which is why “inmates are
not required to specially plead or demonstrate exhaustion in
their complaints.” Rather, PLRA exhaustion is an “affrm-
ative defense” subject to “the usual practice under the Fed-
eral Rules.” Id., at 212. And that usual practice applies,
Page Proof Pending Publication
Jones explained, even though the PLRA is “silent on the
issue,” because that silence is itself “strong evidence that the
usual practice should be followed.” Ibid.
   The PLRA is similarly “silent on the issue” whether
judges or juries should resolve factual disputes related to
exhaustion. The exhaustion provision states simply that
“[n]o action shall be brought with respect to prison condi-
   1
     The dissent criticizes us for asking whether we can avoid the constitu-
tional question by answering the statutory one. Post, at 484–486, and
n. 3 (Barrett, J., dissenting). But we have described doing exactly that
as a “cardinal principle.” Tull v. United States, 481 U. S. 412, 417, n. 3
(1987). The dissent suggests the principle does not apply here because
the parties did not raise it and the courts below did not address it. But
the same was true in Tull, yet we still began by asking whether it was
possible to read the statute to avoid the constitutional question, and moved
on only after concluding the answer was no. Surely we should not deviate
from that principle simply because our answer this time is yes. And in
this case, the statutory question has been fully briefed by amici and in-
volves the same precedents relied on by the parties. See Brief for Law
Professors as Amici Curiae 8–15.
470                     PERTTU v. RICHARDS

                          Opinion of the Court

tions . . . until such administrative remedies as are available
are exhausted.” 42 U. S. C. § 1997e(a). Perttu does not
argue that this provision requires that exhaustion disputes
be resolved by judges. And rightly so. As we noted in
Jones, the phrase “[n]o action shall be brought” is “boiler-
plate language” often used for other affrmative defenses,
like statutes of limitations, 549 U. S., at 220, that routinely
go to the jury. And “failure to exhaust was notably not
added” to the PLRA's screening provisions, which require
judges to dismiss cases on specifed grounds. Id., at 214.
   Just like in Jones, then, the statutory silence on the ques-
tion before us “is strong evidence that the usual practice
should be followed.” Id., at 212; see also Dixon v. United
States, 548 U. S. 1, 17 (2006) (“In light of Congress' silence
on the issue . . . it is up to the federal courts to effectuate
the affrmative defense . . . as Congress may have contem-
plated it . . . given the long-established common-law rule.”
(internal quotation marks omitted)). We therefore look to
Page Proof Pending Publication
the usual practice for resolving factual disputes intertwined
with the merits.2
                                B
  The PLRA was enacted in 1996. By that time, it was well
established that when a factual dispute is intertwined with
the merits of a claim that falls under the Seventh Amend-
ment, that dispute should go to a jury, even if that requires
judges to defer determinations they would ordinarily make
on their own. We have accordingly held in various contexts

   2
     The dissent thinks this should be an even “easier case” than Tull and
others where we concluded that a statute did not confer a jury trial right.
Post, at 488. But our analysis in this case is that “the usual practice
should be followed,” Jones v. Bock, 549 U. S. 199, 212 (2007), and that the
usual practice in cases of intertwinement is to send the question to the
jury, see Beacon Theatres, Inc. v. Westover, 359 U. S. 500, 510–511 (1959);
see also post, at 490 (recognizing that Beacon Theatres establishes a “gen-
eral prudential rule”). Tull and the other cases did not implicate a prac-
tice or rule like Beacon Theatres that itself calls for a jury trial.
                   Cite as: 605 U. S. 460 (2025)             471

                      Opinion of the Court

that, in cases of intertwinement, district courts should struc-
ture their order of operations to preserve the jury trial right.

                                1
   One prominent line of cases involves suits that contain
both legal and equitable claims. Ordinarily, judges resolve
equitable claims and juries resolve legal claims. But in Bea-
con Theatres, 359 U. S., at 510–511, we held that judges may
not resolve equitable claims frst if doing so could prevent
legal claims from getting to the jury.
   Beacon Theatres involved an antitrust dispute between
two movie theater companies. One company brought an eq-
uitable claim for a declaratory judgment that it had not vio-
lated antitrust laws. The other company brought a legal
claim for money damages alleging that the frst company had
violated antitrust laws. Both the equitable and legal claims
therefore hinged on the “common issue” whether there was
Page Proof Pending Publication
an antitrust violation. Id., at 503. Faced with this di-
lemma, we emphasized that, while judges ordinarily have
“discretion in deciding whether the legal or equitable cause
should be tried frst,” “that discretion is very narrowly lim-
ited and must, wherever possible, be exercised to preserve
jury trial.” Id., at 510; see also id., at 510–511 (“[O]nly
under the most imperative circumstances, circumstances
which in view of the fexible procedures of the Federal Rules
we cannot now anticipate, can the right to a jury trial of
legal issues be lost through prior determination of equitable
claims.” (footnote omitted)). The consequence in that case
was clear: Because resolving the equitable claims could “pre-
vent a full jury trial” on the legal claims, the legal claims
needed to be resolved by a jury frst. Id., at 505, 508. The
district court's decision to instead resolve the equitable
claims frst was therefore “not permissible.” Id., at 508.
   Later cases confrm that Beacon Theatres should be read
“expansively,” applying to any claim triable by a jury even
“in a suit in which the basic relief sought is equitable.” 9 C.
472                 PERTTU v. RICHARDS

                      Opinion of the Court

Wright & A. Miller, Federal Practice and Procedure § 2302.1,
pp. 33–34 (4th ed. 2020). For example, in Dairy Queen, Inc.
v. Wood, 369 U. S. 469, 473, 475 (1962), the plaintiff alleged
that the defendant had breached a contract for use of the
trademark “Dairy Queen,” and the plaintiff sought both legal
and equitable relief. We observed that the legal and equita-
ble claims therefore depended on “common” “factual issues
related to the question of whether there [had] been a breach
of contract.” Id., at 479. For that reason, the consequence
was again clear: “[T]he district judge erred in refusing to
grant petitioner's demand for a trial by jury.” Ibid.
   In this case, the parties agree that the exhaustion and
First Amendment questions depend on common factual is-
sues. And Beacon Theatres teaches that a trial court's dis-
cretion in such a situation is “very narrowly limited and
must, wherever possible, be exercised to preserve jury trial.”
359 U. S., at 510. Nothing in the PLRA prevents holding a
jury trial here.
Page Proof Pending Publication2
  Our cases involving subject matter jurisdiction are also
instructive. Ordinarily, judges may resolve factual disputes
in the course of determining whether subject matter juris-
diction is proper. See Wetmore v. Rymer, 169 U. S. 115,
120–121 (1898). But we have long held that a court may
not do so when the factual disputes are intertwined with
the merits.
  For example, in Smithers v. Smith, 204 U. S. 632, 641–642
(1907), the district court concluded that it lacked subject
matter jurisdiction because the case did not meet the $2,000
amount-in-controversy requirement. The district court did
so, however, by fnding that even if the defendants had each
taken a part of the plaintiff 's land—as the plaintiff alleged—
the defendants had not acted jointly, and so the aggregate
amount in controversy did not exceed $2,000. Id., at 645–
646. We reversed because we found that, in arriving at this
conclusion, the district court had decided a factual question
that was “an essential element of the merits of the dispute”—
                    Cite as: 605 U. S. 460 (2025)             473

                       Opinion of the Court

whether the defendants had acted jointly—and so had “in
effect, decided the controversy between the parties upon the
merits.” Id., at 646. We acknowledged that judges ordi-
narily have “the authority to dismiss [an] action [for lack of
subject matter jurisdiction] without trial by jury.” Id., at
644–645. But we held that this authority “obviously is not
unlimited,” “lest under the guise of determining jurisdiction
the merits of the controversy between the parties be sum-
marily decided without the ordinary incidents of a trial, in-
cluding the right to a jury.” Id., at 645.
   We applied similar analysis in Land v. Dollar, 330 U. S.
731 (1947). There the district court concluded that it lacked
subject matter jurisdiction due to sovereign immunity, be-
cause the suit for unlawful possession of stock shares by fed-
eral offcials was in fact a suit “against the United States.”
Id., at 734. We recognized that “as a general rule the Dis-
trict Court would have authority to consider questions of
jurisdiction.” Id., at 735. But we found that Land was
Page Proof Pending Publication
“the type of case where the question of jurisdiction is de-
pendent on decision of the merits,” because both questions
hinged on the plaintiffs' claims that “the shares of stock
never were property of the United States.” Id., at 735, 738.
We therefore held that the district court should have “pro-
ceed[ed] to a decision on the merits” rather than resolve the
jurisdictional issue at a preliminary stage. Id., at 739. See
Gulf Oil Corp. v. Copp Paving Co., 419 U. S. 186, 203, n. 19
(1974) (acknowledging practice of “reserving the jurisdic-
tional issues” when there is “an identity between the `juris-
dictional' issues and certain issues on the merits”); see also
8 J. Moore, D. Coquillette, G. Joseph, G. Vairo, & C. Varner,
Moore's Federal Practice § 38.34[1][c][i], p. 38–154 (3d ed.
2024) (Moore); 5B C. Wright, A. Miller, & A. Spencer, Fed-
eral Practice and Procedure § 1350, pp. 224–226 (4th ed.
2024).
   In its decision below, the Sixth Circuit relied on its Circuit
precedent applying Land, reasoning that if “certain cases
[must] be heard and determined on the merits even when
474                  PERTTU v. RICHARDS

                       Opinion of the Court

constitutionally implicated jurisdictional disputes” are at
play, then “the result should be the same when the lesser
concern of an affrmative defense, such as the PLRA's re-
quirement to exhaust administrative remedies, implicates
the merits of a claim.” 96 F. 4th, at 923 (citing Fireman's
Fund Ins. Co. v. Railway Express Agency, Inc., 253 F. 2d
780, 784 (CA6 1958)). We fnd that reasoning persuasive.
After all, when the PLRA was enacted, many lower court
decisions and treatises had extended the intertwinement
principle to other threshold questions, including personal ju-
risdiction, venue, choice of law, and forum non conveniens.
See, e. g., 5 J. Moore et al., Moore's Federal Practice ¶38.36[3],
p. 38–341 (2d ed. 1996) (“[T]o determine that the alleged acts
did not take place . . . on motion to dismiss for want of proper
venue would be to deny the plaintiff a jury trial on the mer-
its.”); see also 8 Moore §§ 38.34[1][e], [2], [3] (3d ed. 2024).
We express no view today on whether lower courts have
been correct to extend the intertwinement principle to these
Page Proof Pending Publication
other issues. We simply note that these cases—along with
Beacon Theatres and Smithers—show that when the PLRA
was enacted, the usual practice in the federal courts across
a variety of contexts was to resolve factual disputes that are
intertwined with the merits at the merits stage. The
PLRA's complete silence on that question is therefore
“strong evidence” that this “usual practice should be fol-
lowed.” Jones, 549 U. S., at 212.

                                C
   Perttu offers important counterarguments, but we are ul-
timately not persuaded. First, Perttu argues that Beacon
Theatres is inapplicable here. According to Perttu, the con-
cern in Beacon Theatres was that judicial resolution of the
equitable claims would have had collateral estoppel effect on
the legal claims. But here, Perttu says, the judge's factual
fndings related to exhaustion would have no such effect in a
later jury trial.
                        Cite as: 605 U. S. 460 (2025)                      475

                            Opinion of the Court

   Two Circuits have suggested they agree with Perttu that
factual fndings related to exhaustion have no estoppel effect,
but with little analysis and in cases that did not squarely
present an estoppel issue. See Pavey, 544 F. 3d, at 742; Al-
bino v. Baca, 747 F. 3d 1162, 1171 (CA9 2014). Legal trea-
tises, on the other hand, provide support for the proposition
that factual determinations in a frst action can have direct
estoppel effect in a second action on the same claim. See
Restatement (Second) of Judgments § 27, Comment b, Illus-
tration 3, Comment d, pp. 251–255 (1980); 18 C. Wright, A.
Miller, & E. Cooper, Federal Practice and Procedure § 4418,
pp. 505–506 (3d ed. 2016). The Restatement gives an exam-
ple analogous to the situation before us: If a court dismisses
a case for lack of personal jurisdiction based on a particular
factual fnding, that factual fnding has preclusive effect in a
subsequent action on issues beyond just personal jurisdic-
tion. Restatement (Second) of Judgments § 27, Illustration
Page Proof Pending Publication
3, p. 252.3 Perttu also overlooks the fact that, if the judge
below had ruled that Perttu did destroy Richards's griev-
ances, then Perttu himself may have been precluded from
relitigating that issue before the jury under law of the case.
See 18B C. Wright, A. Miller, & E. Cooper, Federal Practice
and Procedure § 4478.5, p. 773 (3d ed. 2019).
   We therefore cannot reject the possibility that a judicial
ruling on PLRA exhaustion might have estoppel effect in a
later jury trial. And Beacon Theatres shows that the
proper path in that situation is to hold the jury trial, not to
change the estoppel rules. See Parklane Hosiery Co. v.
Shore, 439 U. S. 322, 333 (1979) (“Recognition that an equita-
ble determination could have collateral-estoppel effect in a

   3
     See also, e. g., Carr v. Tillery, 591 F. 3d 909, 917 (CA7 2010) (“[A] dis-
missal can be without prejudice yet have preclusive effect.”); Deutsch v.
Flannery, 823 F. 2d 1361, 1364 (CA9 1987) (“It matters not that the prior
action resulted in a dismissal without prejudice, so long as the determina-
tion being accorded preclusive effect was essential to the dismissal.”).
476                     PERTTU v. RICHARDS

                          Opinion of the Court

subsequent legal action was the major premise of this
Court's decision in Beacon Theatres.”).4
   Regardless, even if Perttu is right that factual fndings
concerning exhaustion have no estoppel effect in a later jury
trial, we decline to limit Beacon Theatres artifcially to cases
involving estoppel. The problem in Beacon Theatres was
that judicial resolution of a “common issue” might have “pre-
vent[ed] a full jury trial” on the legal claims. 359 U. S., at
503, 505, 508. Estoppel was simply the reason why a “full
jury trial” might have been “prevent[ed]” in that case. Id.,
at 505 (“[T]o try the equitable cause frst . . . might, through
collateral estoppel, prevent a full jury trial.” (emphasis
added)). The principle of Beacon Theatres still applies
when judicial resolution of a common issue might “prevent a
full jury trial” for some reason other than estoppel. And
here, that other reason is clear. Instead of just being es-
topped, Richards's claim is being dismissed entirely. We
therefore agree with the Sixth Circuit's reasoning: Even as-
Page Proof Pending Publication
suming Perttu is right that a jury may “reexamine the
judge's factual fndings,” that “rationale” “rings hollow if the
prisoner's case is dismissed for failure to exhaust,” because
“[i]n such an instance, a jury would never be assembled to
resolve the factual disputes.” 96 F. 4th, at 921.
   It is no answer, in our view, to say that a prisoner might
someday get a jury by starting over, exhausting the griev-
ance procedures, then refling his lawsuit. After all, that
path is impossible in most cases. As Perttu acknowledged
at oral argument, “the time frames for . . . grievances are
very short”— on the order of days. Tr. of Oral Arg. 35; see,

  4
   The dissent reads this “major premise” language from Parklane as
suggesting that Beacon Theatres is all about estoppel. Post, at 491. But
the question in Parklane was whether a prior equitable ruling could have
estoppel effect in a subsequent legal action, and Parklane simply pointed
out that Beacon Theatres believed it could—i.e., that Beacon Theatres
took that fact as a “major premise” then reasoned from there. That logic
does not imply that Beacon Theatres is limited to cases involving estoppel.
                         Cite as: 605 U. S. 460 (2025)                     477

                            Opinion of the Court

e. g., Jones, 549 U. S., at 207 (grievance deadlines of 2 to 5
days); Woodford, 548 U. S., at 95–96 (grievance deadlines of
14 to 30 days). By the time a case is dismissed for failure
to exhaust, grievance deadlines will have long since passed.
But Perttu makes no argument that such deadlines are tolled
in these situations. Instead, he points to the fact that prison
administrators in some (but not all) jurisdictions have discre-
tion to excuse missed grievance deadlines, with no evidence
of how often administrators actually exercise that discretion,
let alone in cases where—as here—doing so would foresee-
ably set up a second lawsuit. And though Perttu makes a
different argument for why Richards could exhaust and refle
in this case,5 he does not argue that courts should treat indi-
vidual cases of intertwinement differently based on whether
a particular party in a given case might one day get to a
jury. See Beacon Theatres, 359 U. S., at 504 (concern at
  5
      Perttu argues that Richards remains able to exhaust because his alle-
Page          Proof
gations fall under  the PrisonPending
                                Rape Elimination ActPublication
                                                        of 2003 (PREA), 117
Stat. 972, 34 U. S. C. § 30301 et seq., and federal regulations prevent pris-
ons from imposing deadlines on PREA grievances regarding sexual abuse.
Reply Brief 14 (citing 28 CFR § 115.52(b)(1) (2024)). Accordingly, Perttu
says, the PREA policy applicable in the State of Michigan when Richards
fled suit did not bar him from fling new grievances. See App. 75 (“A
prisoner may fle a PREA grievance at any time.”). Richards, however,
says “[t]his is the frst time in this fve years of litigation that [Perttu] has
represented that . . . all of [Richards's] claims might be able to be ex-
hausted.” Tr. of Oral Arg. 51. Richards also says that his “First Amend-
ment claim . . . is not protected by the PREA policy.” Id., at 51–52;
see also App. 76 (“Any PREA grievance containing multiple issues, which
include sexual abuse and non-sexual abuse issues, shall be processed . . .
to address the allegations of sexual abuse only.”). We take no position on
this dispute.
  Perttu also notes that the Michigan Department of Corrections has since
amended its PREA policy to “eliminat[e] the administrative grievance pro-
cedure for addressing prisoner grievances regarding sexual abuse.”
Reply Brief 14, n. 3. We take no position on whether this new policy
covers Richards's First Amendment claim or whether there are other ad-
ministrative remedies that Richards would need to exhaust before fling a
subsequent action.
478                 PERTTU v. RICHARDS

                      Opinion of the Court

issue arises when prior determination by judge “might” de-
prive party of jury trial); id., at 505 (same).
   Finally, Perttu argues that requiring a jury trial here
would confict with the purpose of PLRA exhaustion, which
is to conserve judicial resources by preventing unexhausted
claims from going to trial. For support, Perttu cites our
decision in Katchen v. Landy, 382 U. S. 323 (1966). There
we held that a bankruptcy court could proceed to decide an
equitable claim—even if similar issues might one day arise
before a jury on a legal claim—because to prevent the equita-
ble claim from being “tried in the bankruptcy court in the
normal manner” would be “to dismember a scheme which
Congress has prescribed.” Id., at 339.
   But Katchen is clearly far afeld. That case involved
a “specifc statutory scheme”—bankruptcy—“contemplating
the prompt trial of a disputed claim without the intervention
of a jury” in a special set of courts created for that purpose.
Page Proof Pending Publication
Ibid. The equivalent “statutory scheme” here—the
PLRA—contemplates that Richards's First Amendment
claim will be resolved by a jury and is silent about whether
a jury should resolve exhaustion.
   Perttu responds that holding a jury trial on exhaustion
nonetheless conficts with congressional intent because the
point of PLRA exhaustion is to ensure that only exhausted
claims go to trial. But that objection would apply with even
greater force in Smithers and Land, because—by the same
logic—holding a trial on subject matter jurisdiction would
confict with the purpose of ensuring that trials happen only
where jurisdiction is proper. See Ex parte McCardle, 7
Wall. 506, 514 (1869) (“Without jurisdiction the court cannot
proceed at all in any cause.”). Yet Smithers and Land show
that, in cases of intertwinement, the proper practice is in-
deed to go to trial. We therefore cannot agree with Perttu
that the PLRA's general interest in conserving judicial re-
sources shows that Congress clearly intended for judges to
resolve exhaustion disputes in this unique circumstance.
                   Cite as: 605 U. S. 460 (2025)            479

                     Barrett, J., dissenting

                         *      *      *
   If Congress had expressly provided in the PLRA that ex-
haustion disputes must be resolved by judges, then we would
have been required to consider today whether such a provi-
sion violates the Seventh Amendment. But it is a “cardinal
principle” that we not address such a constitutional question
unless necessary. Tull v. United States, 481 U. S. 412, 417,
n. 3 (1987). Meanwhile, as we have shown, the usual prac-
tice of the federal courts in cases of intertwinement is to
send common issues to the jury. Because nothing in the
PLRA suggests Congress intended to depart from that prac-
tice here, we hold that parties are entitled to a jury trial on
PLRA exhaustion when that issue is intertwined with the
merits of a claim protected by the Seventh Amendment.
   The judgment of the United States Court of Appeals for
the Sixth Circuit is affrmed.
                                              It is so ordered.
Page
 Justice Proof    Pending
         Barrett, with            Publication
                       whom Justice Thomas, Justice
Alito, and Justice Kavanaugh join, dissenting.
  The Prison Litigation Reform Act of 1995 (PLRA) re-
quires prisoners suing under 42 U. S. C. § 1983 to frst ex-
haust the administrative remedies that are “available” to
them. § 1997e(a). In the decision below, the Sixth Circuit
held that even if prisoners are not ordinarily entitled to a
jury trial to resolve this threshold question, the Seventh
Amendment requires a jury when exhaustion is intertwined
with the merits. I would reverse. The jury right con-
ferred by the Seventh Amendment does not depend on the
degree of factual overlap between a threshold issue and the
merits of the plaintiff's claim.
  The Court takes a different path. Instead of resolving
the constitutional question that the parties brought to us,
the Court holds that the PLRA itself requires a jury trial
whenever an issue is common to exhaustion and the merits.
No matter, the Court says, that the PLRA is silent on the
480                 PERTTU v. RICHARDS

                     Barrett, J., dissenting

subject. No matter that this statutory argument was not
briefed before us. And no matter that it was not passed on
by the courts below.
  Having taken this detour, the Court ends up in the wrong
place. Reading the PLRA's silence to implicitly confer a
right to a jury trial contravenes not only basic principles
of statutory interpretation, but also several of this Court's
precedents. I respectfully dissent.

                               I
   Kyle Richards, a state prisoner, sued Thomas Perttu, a
prison employee, for damages under § 1983. Richards al-
leged two bases for relief: First, he alleged that Perttu had
sexually harassed several inmates, including Richards. And
second, Richards alleged that when he had attempted to fle
grievances reporting the harassment, Perttu had retaliated
in several ways, including by destroying Richards's griev-
Page Proof Pending Publication
ance forms. See ante, at 465–466. Richards claimed that
Perttu's initial harassment and subsequent retaliation vio-
lated the Eighth and First Amendments, respectively. See
App. 18.
   Because a damages suit under § 1983 is a “Sui[t] at common
law,” all agree that the Seventh Amendment entitles Rich-
ards to a jury trial on the merits of his claims. U. S. Const.,
Amdt. 7 (“In Suits at common law, where the value in contro-
versy shall exceed twenty dollars, the right of trial by jury
shall be preserved”); see Monterey v. Del Monte Dunes at
Monterey, Ltd., 526 U. S. 687, 720–721 (1999). To litigate
the merits, however, the PLRA requires Richards to estab-
lish that he exhausted “such administrative remedies as are
available” to him. § 1997e(a). Whether Richards did so
turns on a factual dispute about the availability of his admin-
istrative remedies. According to Richards, Perttu's de-
struction of Richards's grievances rendered the prison griev-
ance system “unavailable” for purposes of the PLRA. Ross
v. Blake, 578 U. S. 632, 644 (2016). Perttu, for his part, in-
                      Cite as: 605 U. S. 460 (2025)                  481

                        Barrett, J., dissenting

sists that he did not destroy Richards's grievances; thus, he
says, the system was available to Richards and Richards's
failure to fle grievances dooms his § 1983 claims. See
§ 1997e(a).
   This dispute about the facts engendered another about the
law—and more specifcally, about the role of the jury. The
PLRA itself says nothing about the right to a jury trial on
the question of exhaustion. And all the circuits to have con-
sidered the question hold that the Seventh Amendment does
not require one. So the consensus rule in the courts of ap-
peals has been that PLRA exhaustion can be resolved
through a bench trial.1
   Although the Sixth Circuit has long embraced this rule,
see Lee v. Willey, 789 F. 3d 673, 678 (2015), Richards argued
that his case was special—and the Sixth Circuit agreed. An
exception applies, it held, “when the resolution of the exhaus-
tion issue . . . would also resolve a genuine dispute of mate-
rial fact regarding the merits of the plaintiff's substantive
Page Proof Pending Publication
case.” 96 F. 4th 911, 923 (2024). In such cases, the Sixth
Circuit held, the Seventh Amendment entitles the parties to
a jury. That holding broke with the decisions of the Seventh
and Ninth Circuits, both of which have rejected a factual-
overlap exception. See Pavey v. Conley, 544 F. 3d 739, 742
(CA7 2008); Albino v. Baca, 747 F. 3d 1162, 1171 (CA9 2014)
(en banc) (agreeing with Pavey in dicta).

                                   II
  Having granted certiorari to resolve this split, I would re-
verse. The jury-trial right conferred by the Seventh
Amendment does not turn on the degree of factual overlap
  1
    See Messa v. Goord, 652 F. 3d 305, 308–310 (CA2 2011) (per curiam);
Small v. Camden Cty., 728 F. 3d 265, 269–271 (CA3 2013); Dillon v. Rog-
ers, 596 F. 3d 260, 271 (CA5 2010); Lee v. Willey, 789 F. 3d 673, 677–678
(CA6 2015); Pavey v. Conley, 544 F. 3d 739, 741–742 (CA7 2008); Albino v.
Baca, 747 F. 3d 1162, 1170–1171 (CA9 2014) (en banc); Bryant v. Rich, 530
F. 3d 1368, 1373–1377 (CA11 2008).
482                      PERTTU v. RICHARDS

                          Barrett, J., dissenting

between a threshold question and the merits of the plain-
tiff 's claim.
   Because the Seventh Amendment provides that the “ `right
of trial by jury shall be preserved,' ” it protects “ `the right
which existed under the English common law when the
Amendment was adopted.' ” Markman v. Westview Instru-
ments, Inc., 517 U. S. 370, 376 (1996). In actions that would
have been tried at law at the founding, such as this one, the
question is whether the “particular trial decision” at issue
“must fall to the jury in order to preserve the substance of
the common-law right as it existed in 1791.” Ibid.
   The parties devote much of their time to debating the best
founding-era analogue to the exhaustion defense. Accord-
ing to Richards, exhaustion is analogous to common-law de-
fenses that would have been raised through a plea in bar.2
Under the common-law pleading system, Richards argues,
the parties' dueling pleas would isolate disputed points of
law and fact, with the former allocated to a judge and the
Page Proof Pending Publication
latter allocated to a jury. See H. Stephen, Principles of
Pleading in Civil Actions 59–61 (1882); B. Shipman, Hand-
book of Common-Law Pleading § 15, p. 32 (3d ed. 1923).
Perttu, on the other hand, grounds exhaustion in traditional
equitable practice. In his view, an exhaustion defense most
closely resembles a defensive equitable action to enjoin a
lawsuit—an action that would have been heard by the chan-
cellor, not a jury. Liberty Oil Co. v. Condon Nat. Bank, 260
U. S. 235, 242–243 (1922).
   The Court does not get into this back-and-forth—and here,
I agree with the Court. We did not take this case to deter-
mine whether the Seventh Amendment requires jury trials
for all disputes about exhaustion. There is no circuit split
on that question, and the court below did not address it.
   2
     Richards relies primarily on the plea in discharge, a type of plea in bar
that applies when the plaintiff 's cause of action has been “discharged by
some matter subsequent, either of fact or of law.” B. Shipman, Handbook
of Common-Law Pleading § 198b, p. 348 (3d ed. 1923).
                   Cite as: 605 U. S. 460 (2025)            483

                     Barrett, J., dissenting

(Recall that under binding Sixth Circuit precedent, there is
generally no Seventh Amendment right to a jury trial for
exhaustion disputes. See Lee, 789 F. 3d, at 678.) The ques-
tion, moreover, might be very diffcult. Neither party iden-
tifes an obvious analogue to exhaustion, a defense that de-
veloped long after the founding. See R. Berger, Exhaustion
of Administrative Remedies, 48 Yale L. J. 981, and n. 1 (1939).
Resolving the dispute would therefore require us to confront
challenging historical and methodological questions: Did the
Seventh Amendment constitutionalize common-law pleading
rules? Does Congress have the authority, after the merger
of law and equity, to fashion novel defenses as “equitable”?
What presumption applies when the historical evidence is
ambiguous? It would be unwise to address these questions
before the lower courts have seriously considered them.
   Answering the question presented, however, would not
have required us to resolve these knotty issues. We granted
Page Proof Pending Publication
certiorari to decide the same limited issue that the Sixth
Circuit decided: whether a special Seventh Amendment rule
applies when a factual dispute about exhaustion is inter-
twined with the merits. And on this question, the historical
record is much clearer. Richards has presented no evidence
that intertwinement with the merits was relevant to the
jury-trial right. Instead, he simply repeats his broader his-
torical argument: that factual disputes raised through pleas
were heard by juries. But this was true regardless of
whether the dispute overlapped with the merits. See, e. g.,
Wetmore v. Rymer, 169 U. S. 115, 120–123 (1898) (describing
“trial[s] had with a jury” over subject-matter jurisdiction).
Likewise, Perttu's account does not implicate intertwine-
ment. All equitable defenses were heard by “the judge as
a chancellor” because they were freestanding equitable ac-
tions. Liberty Oil, 260 U. S., at 242–243; see W. Cook, Equi-
table Defenses, 32 Yale L. J. 645, 650–652 (1922–1923).
   The upshot is that there is no historical support for a spe-
cial intertwinement rule. Mere factual overlap with the
484                      PERTTU v. RICHARDS

                          Barrett, J., dissenting

merits does not transform a collateral issue ordinarily re-
solved by a court into one necessarily resolved by a jury.
We could have corrected that constitutional error and saved
the broader, more complicated debate for another day.
                              III
   Remarkably, in this Seventh Amendment case, the Court
has nothing to say about the Seventh Amendment. In fact,
the Court sets the Constitution entirely aside, “express[ing]
no view” on how or when it demands that a jury resolve
intertwined factual disputes. Ante, at 468–469. Left with
nothing else to interpret, the Court pivots to the PLRA.
True, the Court acknowledges, the PLRA says nothing about
the role of the jury—and certainly nothing about the role of
the jury in resolving disputes about exhaustion. But as a
matter of statutory interpretation and “ `common-law adjudi-
catory principles,' ” the Court holds that the PLRA nonethe-
less requires a jury trial when a dispute about exhaustion is
Page Proof Pending Publication
“intertwined with the merits” of the plaintiff 's claim. Ante,
at 468.
   This is wrong several times over. Richards did not pres-
ent this statutory theory to us or any other court; the PLRA
does not confer a jury right through its silence; and the
Court plucks its purported “common-law adjudicatory princi-
ple” out of thin air. I take each point in turn.
                             A
  To begin, the Court spins a statutory theory that Richards
has never even mentioned, much less developed.3 Before us,
   3
     The avoidance canon permits a court to choose a less plausible interpre-
tation of a statute when the most natural one would provoke a “ `serious' ”
constitutional question. Zadvydas v. Davis, 533 U. S. 678, 689 (2001).
Though the Court invokes the canon in this case, it is unwilling to say that
interpreting the PLRA to permit a court to resolve Richards's exhaustion
defense would pose a “serious” constitutional question. This reticence
is presumably attributable to the scant historical support for Richards's
proposed intertwinement rule. Even if the canon applied, moreover, the
                     Cite as: 605 U. S. 460 (2025)               485

                       Barrett, J., dissenting

Richards argues only that he has a constitutional right to a
jury trial. Both his Brief in Opposition and his merits brief
focus exclusively on the Seventh Amendment. See Brief for
Respondent 3 (“[T]he Seventh Amendment clearly protects
Respondent's right to jury resolution of disputed historical
facts central to the merits of his legal claim”); Brief in Oppo-
sition 1 (“The Sixth Circuit correctly held that [the District
Court's] process violated the Seventh Amendment”). The
same was true below. In the District Court, Richards's ar-
gument turned on the proper application of circuit prece-
dent—precedent that has everything to do with the Seventh
Amendment and nothing to do with the PLRA. See Objec-
tions and Request for Review in No. 2:20–cv–00076 (WD
Mich., Aug. 6, 2021), ECF Doc. 102, p. 2; Lee, 789 F. 3d, at
678. Following Richards's lead, the District Court likewise
focused on the Seventh Amendment. 2021 WL 3508384, *2
(WD Mich., Aug. 10, 2021) (“[T]he Seventh Amendment right
to a jury trial [does] not extend to the exhaustion question”).
Page Proof Pending Publication
On appeal in the Sixth Circuit, Richards continued to press
the same Seventh Amendment argument. Brief for Appel-
lant in No. 22–1298, p. 2; see generally Supplemental Brief
for Appellant in No. 22–1289. So, no surprise, the Sixth Cir-
cuit addressed only the Seventh Amendment. See 96 F. 4th,
at 923 (“[T]he Seventh Amendment requires a jury trial
when the resolution of the exhaustion issue under the PLRA
would also resolve a genuine dispute of material fact regard-
ing the merits of the plaintiff 's substantive case”).
   In light of this procedural history, the Court's path is per-
plexing. We typically refuse to consider arguments that the
parties failed to make before us. See Reno v. American
Civil Liberties Union, 521 U. S. 844, 863, n. 30 (1997). Like-
wise, “we normally decline to entertain . . . arguments” that
a party “failed to raise . . . in the courts below.” Kingdom-
ware Technologies, Inc. v. United States, 579 U. S. 162, 173
chosen interpretation must be plausible—and, as I explain in the next
Part, the Court's interpretation most certainly is not.
486                   PERTTU v. RICHARDS

                      Barrett, J., dissenting

(2016). And we regularly emphasize that “we are a court of
review, not of frst view,” so we generally do not address
issues that the court of appeals did not analyze frst. Cutter
v. Wilkinson, 544 U. S. 709, 718, n. 7 (2005). (Making mat-
ters worse, it is not clear that any court has considered the
statutory question the Court resolves today.) Apparently,
these party-presentation principles have no purchase here.
Without any prompting from the parties, the Court devises
and embraces a theory that Richards himself never raised—
all, ironically enough, to save his case from dismissal for an
alleged failure to exhaust.
                               B
   Nor does the Court depart from party presentation in
service of a sound result. Its analysis goes wrong at every
turn, beginning with its choice to venture beyond statutory
text into the realm of statutory silence.
   As the Court recognizes, the PLRA is “ `silent on the issue'
Page Proof Pending Publication
whether judges or juries should resolve factual disputes re-
lated to exhaustion.” Ante, at 469. Indeed, a search of the
exhaustion provision yields nothing remotely related to a
jury trial:
      “No action shall be brought with respect to prison condi-
      tions under [42 U. S. C. § 1983], or any other Federal law,
      by a prisoner confned in any jail, prison, or other correc-
      tional facility until such administrative remedies as are
      available are exhausted.” § 1997e(a).
Notwithstanding this silence, the Court says that the PLRA
guarantees the plaintiff “a right to a jury trial on PLRA
exhaustion when that issue is intertwined with the merits of
a claim that falls under the Seventh Amendment.” Ante, at
468. According to the Court, this “intertwinement” rule is
so well established that Congress expected courts to apply
it even when the statute says nothing about it. Ibid. Sup-
posedly, the rule is a “ `common-law adjudicatory principl[e]' ”
against which Congress legislates. Ibid.
                   Cite as: 605 U. S. 460 (2025)            487

                     Barrett, J., dissenting

   It is true that Congress sometimes legislates against the
backdrop of a well-established principle. For example, rely-
ing on the “strength of the traditional rule” that criminal
offenses require mens rea, we interpret statutes to incorpo-
rate that requirement “ `even where the statutory defnition
did not in terms include it.' ” Staples v. United States, 511
U. S. 600, 605–606 (1994) (quoting United States v. Balint,
258 U. S. 250, 251–252 (1922)). Section 1997e(a), however,
implicates no such “traditional rule.” (Note that while the
Court treats the “intertwinement” rule as bedrock, it is ap-
parently not confdent enough in the rule's historical roots to
call it constitutionally required.) Even beyond that, how-
ever, the Court does not cite precedent applying this sup-
posed rule—or anything like it—as a background principle
of statutory interpretation. And so far as I can tell, there
is no such precedent. On the contrary, when we have con-
sidered whether a statute confers the right to a jury trial,
Page Proof Pending Publication
we have understood silence to mean what you would ex-
pect—that Congress did not affrmatively confer such a
right.
   Consider Tull v. Uni ted States, 481 U. S. 412 (1987).
There, we considered whether a civil action under the Clean
Water Act required the jury's involvement. We asked the
same question that the Court asks today: Was a “ `construc-
tion of the statute . . . fairly possible by which the [Seventh
Amendment] question may be avoided' ”? Id., at 417, n. 3.
No, we said: “Nothing in the language of the Clean Water
Act or its legislative history implies any congressional intent
to grant defendants the right to a jury trial.” Ibid. “Given
this statutory silence,” there was no statutory basis for a
jury-trial right. Ibid. (emphasis added). That was so even
though the traditional role of the jury in this context meant
that the Seventh Amendment required one. Id., at 418–419.
   Our decision in Feltner v. Columbia Pictures Television,
Inc., is similar. 523 U. S. 340 (1998). Faced with the ques-
tion whether a copyright owner was entitled to a jury trial
488                  PERTTU v. RICHARDS

                      Barrett, J., dissenting

in a suit for damages, we observed that the statute was “si-
lent on the point.” Id., at 342. The “entire statutory provi-
sion” made “no mention of a right to a jury trial or, for that
matter, to juries at all.” Id., at 346. As in Tull, that si-
lence was dispositive: We “discern[ed] no statutory right to
a jury trial.” 523 U. S., at 347. And again, that was so even
though the Seventh Amendment demanded a jury. Id., at
348–355.
   Finally, in Monterey, we held that § 1983 “does not itself
confer the jury right.” 526 U. S., at 707. This was true, we
explained, even though § 1983 authorizes a party to proceed
through an “ `action at law.' ” Ibid. We declined to inter-
pret the phrase as a “term of art implying a right to a jury
trial,” and, as a result, we declined “to fnd a statutory jury
right under § 1983.” Id., at 707–708.
   This should have been an easier case than Tull, Feltner,
or Monterey. In each of those cases, the statute invoked
terms traditionally associated with the jury-trial right. See
Page Proof Pending Publication
Monterey, 526 U. S., at 707 (“ `action[s] at law' ”); Feltner, 523
U. S., at 352–353 (“statutory damages”); Tull, 481 U. S., at
422 (“civil penalty”). Indeed, in all three cases, we ulti-
mately held that the Seventh Amendment required a jury
trial. Monterey, 526 U. S., at 720–721; Feltner, 523 U. S., at
355; Tull, 481 U. S., at 427. It would have been easy to read
into a phrase such as “action at law” an implicit instruction
to require jury trials, but we did not do so; instead, we read
the statute to mean what it actually said. Monterey, 526
U. S., at 708. Here, the statute contains no term tradition-
ally associated with the jury-trial right, and the claim to a
statutory backdrop is even weaker. That is perhaps why
Richards never attempted to make the statutory argument
that the Court advances now.

                                C
  The Court's approach to statutory interpretation is not only
adventuresome—it also rests on an illusion. Neither history,
nor logic, nor precedent supports its “intertwinement” rule.
                   Cite as: 605 U. S. 460 (2025)             489

                     Barrett, J., dissenting

   I covered the lack of historical support for the rule in my
discussion of the Seventh Amendment. On, then, to logic:
The Court's proposed rule is both manifestly unfair and in-
herently arbitrary. Under the Court's approach, similarly
situated plaintiffs are entitled to a jury (or not) based on
immaterial distinctions in the claims they choose to bring.
To see why, imagine that another inmate (say, Smith) sues
Perttu based on the very same facts that Richards alleges
here. Like Richards, Smith claims that Perttu sexually har-
assed him. And, like Richards, Smith contends that Perttu
destroyed his grievances, thus excusing his failure to exhaust
his available administrative remedies. But suppose that,
unlike Richards, Smith brings only an Eighth Amendment
claim. Because the destruction of grievance forms does not
implicate the Eighth Amendment, Richards's proposed rule
would not entitle Smith to a jury trial on exhaustion.
   As this example illustrates, the Court's rule makes little
sense. There is no question that both Richards and Smith
Page Proof Pending Publication
would be entitled to a jury trial on the merits of their § 1983
claims. For both Richards and Smith, an adverse ruling on
administrative exhaustion would require dismissal. For
both Richards and Smith, the exhaustion question would de-
pend on the same set of facts and credibility determinations.
And for both Richards and Smith, an exhaustion-related dis-
missal would not preclude a subsequent suit once they have
adequately exhausted their claims. So why should Richards
get a jury trial, but not Smith? The Court does not say.
   Instead, the Court relies on three cases holding (it says)
that an issue triggers the jury-trial right if it is intertwined
with the merits, even if it could ordinarily be resolved by the
court. None of the cited cases stands for this proposition.

                                1
   The Court leads with Beacon Theatres, Inc. v. Westover,
359 U. S. 500 (1959). See ante, at 471–472. In that case, the
District Court had two actions before it: (1) an equitable ac-
tion by the plaintiff (Fox Theatres); and (2) a countersuit by
490                 PERTTU v. RICHARDS

                     Barrett, J., dissenting

the defendant (Beacon Theatres) for damages. See 359
U. S., at 502–503. Both actions involved a common issue re-
lated to the reasonableness of the plaintiff's underlying con-
tracts. But only the latter action—a suit at law—implicated
the right to a jury trial. That teed up the question: Which
should the trial court resolve frst?
   The answer, we held, is that courts ultimately have “dis-
cretion in deciding whether the legal or equitable cause
should be tried frst.” Id., at 510. But this discretion
should, “wherever possible, be exercised” such that the legal
claims would be heard before the equitable ones. Ibid.
Resolving the equitable claim frst, we explained, might inad-
vertently “ `operate either by way of res judicata or collateral
estoppel' ” so as to limit the “ `opportunity fully to try to a
jury every issue which has a bearing upon' ” the legal claim.
Id., at 504 (quoting Beacon Theatres, Inc. v. Westover, 252
F. 2d 864, 874 (CA9 1958)).
Page Proof Pending Publication
   Beacon Theatres does not hold, however, that the Seventh
Amendment compels legal-then-equitable sequencing. Nor
does it “construc[t]” statutory silence to require such a rule.
Ante, at 468. Instead, as our later cases confrm, Beacon
Theatres “enunciate[s] no more than a general prudential
rule” governing the trial court's “discretion in determining
the sequence of trial” when legal and equitable claims are
joined in the same action. Parklane Hosiery Co. v. Shore,
439 U. S. 322, 334 (1979). As a rule of discretion, it is not
hard and fast: We have observed that “there might be situa-
tions” in which a court may “resolve the equitable claim frst
even though the results might be dispositive of the issues
involved in the legal claim.” Katchen v. Landy, 382 U. S.
323, 339–340 (1966). Congress, too, has fexibility: It may
devise “a specifc statutory scheme” that contemplates “the
prompt trial of a disputed claim without the intervention of
a jury.” Id., at 339.
   With that understanding of Beacon Theatres in mind, the
differences with this case are hard to miss. Beacon The-
                       Cite as: 605 U. S. 460 (2025)                    491

                         Barrett, J., dissenting

atres involved a court's discretion in judicial administra-
tion—discretion that Congress is always free to override.
See Katchen, 382 U. S., at 339–340 (emphasizing that the
Beacon Theatres rule can be displaced “[t]o implement con-
gressional intent”). The Court's analysis here, by contrast,
turns on whether Congress affrmatively conferred a jury-
trial right on prisoners when it enacted the PLRA.
   Besides, the problem that drove the Court's decision in
Beacon Theatres is absent here. Recall the concern: that
Fox's equitable claim would proceed to fnal judgment before
Beacon Theatres's legal claim and thus preclusively resolve
“the issues involved” in that claim. Katchen, 382 U. S., at
339–340. Indeed, as we later explained in Parklane Ho-
siery, “[r]ecognition that an equitable determination could
have collateral-estoppel effect in a subsequent legal action
was the major premise” of Beacon Theatres. 439 U. S., at
333 (emphasis added). The holding of Beacon Theatres, we
Page Proof Pending Publication
underscored, was specifcally intended to avoid foreclosing,
“by res judicata or collateral estoppel,” the “relitigation” of
an “issue common to both legal and equitable claims.” 439
U. S., at 334.
   No such concern is present in this case. Both courts to
have considered the issue have concluded, consistent with
principles of collateral estoppel, that the resolution of facts
relating to administrative exhaustion does not bind the jury
in a subsequent trial. See Pavey, 544 F. 3d, at 742; Albino,
747 F. 3d, at 1171. This makes sense: Because collateral es-
toppel requires a “fnal judgment,” it should have no force
when the resolution of a threshold issue (like exhaustion)
results in a without-prejudice dismissal. Restatement (Sec-
ond) of Judgments § 27 (1980).4

  4
    While Richards does not dispute that collateral estoppel is inapplicable
here, the Court suggests that it may apply. To support this contention,
however, the Court simply relies on the hornbook principle that “factual
determinations in a frst action can have direct estoppel effect in a second
492                     PERTTU v. RICHARDS

                         Barrett, J., dissenting

  For reasons I do not understand, the Court recasts Beacon
Theatres as having little to do with collateral estoppel.
Without any hesitation, it turns Beacon Theatres's “major
premise” into a minor corollary, announcing that the case will
not be “artifcially” limited “to cases involving estoppel.”
Ante, at 476. But the reasoning of Beacon Theatres ex-
pressly turned on estoppel, and we have subsequently identi-
fed this principle as the animating force behind its holding.
Parklane Hosiery, 439 U. S., at 333; Katchen, 382 U. S., at
339–340. And estoppel is the one circumstance where inter-
twinement with the merits has practical relevance to the
jury-trial right. Without fanfare, citation, or explanation,
the Court thus transforms our 40-year understanding of a
seminal case on equity.
                              2
  The Court's reliance on Smithers v. Smith and Land v.
Dollar is even more of a stretch: Neither has anything to do
Page Proof Pending Publication
with the question presented here.

action on the same claim.” Ante, at 475. To be sure, the resolution of a
threshold issue precludes relitigation of that same threshold issue in a
subsequent suit. See 18A C. Wright, A. Miller, & E. Cooper, Federal
Practice and Procedure § 4436, p. 143 (3d ed. 2017). For that reason, if a
court rules against a plaintiff on exhaustion and dismisses her case, she
cannot relitigate whether she exhausted her administrative remedies.
But if she prevails on exhaustion and proceeds to the merits, collateral
estoppel should not preclude revisiting the facts that informed the court's
ruling on exhaustion. Indeed, the cases cited by the majority, see ante,
at 475, n. 3, are consistent with this principle. See Carr v. Tillery, 591
F. 3d 909, 916–917 (CA7 2010) (a determination that a federal court lacks
subject-matter jurisdiction over a suit would bar a federal court from as-
serting jurisdiction in a subsequent suit); Deutsch v. Flannery, 823 F. 2d
1361, 1364 (CA9 1987) (a determination that a complaint fails to allege
fraud with particularity could preclude the refling of an identical com-
plaint). The law-of-the-case doctrine would be similarly inapplicable.
See 18B C. Wright, A. Miller, & E. Cooper, Federal Practice & Procedure
§ 4478.5, p. 774 (3d ed. 2019) (“Reconsideration of a fact issue may be ap-
propriate . . . if a change of procedural posture changes the nature of
the issue”).
                   Cite as: 605 U. S. 460 (2025)             493

                     Barrett, J., dissenting

   Start with Smithers, in which the plaintiff asserted that
the defendants had stolen his land. 204 U. S. 632, 640 (1907).
The land, the plaintiff claimed, was worth more than $2,000,
the amount-in-controversy requirement then in effect. See
id., at 639–641. After holding a bench trial, the District
Court dismissed the case for lack of jurisdiction; according
to the court, each defendant had taken a parcel worth less
than $2,000, and the defendants had not acted jointly. Id.,
at 641–642. In so holding, the court violated the black-letter
rule that a plaintiff's declaration generally establishes the
amount in controversy. Id., at 642. Because it was “legally
possible for the plaintiff to recover the full amount of all the
land and the full amount of the damages claimed,” we held
that the District Court had erred in dismissing the case.
Id., at 644.
   In other words, the District Court simply misapplied long-
standing jurisdictional principles. The plaintiff 's pleadings
were suffcient to establish jurisdiction, notwithstanding any
Page Proof Pending Publication
factual disputes that might limit the plaintiff 's potential re-
covery down the line. But these disputes implicated the
merits—damages, in particular—not jurisdiction. Smith-
ers's rule is therefore unremarkable. A trial court may not
prematurely resolve a merits question by framing it as a ju-
risdictional question, thereby depriving the plaintiff of a
jury. Smithers says nothing about whether a threshold
question requires a jury simply because of factual overlap
with the merits.
   Land v. Dollar, 330 U. S. 731 (1947), is even further afeld.
There, stockholders sued members of the U. S. Maritime
Commission to recover stock previously delivered to the
Commission. Id., at 733–734. The District Court dis-
missed the case, reasoning that because the stock was federal
property, sovereign immunity barred the plaintiff's suit.
Id., at 734–735. That was an error, we held: Ownership of
the stock implicated the merits of the stockholders' claim, so
the court should not have decided that issue at the outset of
the case. Id., at 739.
494                 PERTTU v. RICHARDS

                     Barrett, J., dissenting

   Nothing in Land turned on the Seventh Amendment; in-
deed, the word “jury” does not appear in our opinion or the
opinion of the court below. See Dollar v. Land, 154 F. 2d
307 (CADC 1946). This may be because Land was a suit for
injunctive relief and mandamus, not damages. See 330
U. S., at 740 (Reed, J., concurring); Dollar, 154 F. 2d, at 308
(“The complaint prayed for relief by way of injunction and
mandamus against the defendant”). In fact, in the end “a
lengthy trial was had before the court without a jury.” Dol-
lar v. Land, 184 F. 2d 245, 247 (CADC 1950). Sensibly, then,
we have never understood Land to inform the scope of the
right to a jury trial. It stands for the more limited proposi-
tion that when there is “an identity between the `jurisdic-
tional' issues and certain issues on the merits,” there is “no
objection to reserving the jurisdictional issues until a hear-
ing on the merits.” Gulf Oil Corp. v. Copp Paving Co., 419
U. S. 186, 203, n. 19 (1974). This rule is just a principle of
judicial administration—addressing circumstances in which
Page Proof Pending Publication
it makes sense to defer ruling on a potentially jurisdictional
issue until the merits—and not a holding on the jury-trial
right.
                          *    *     *
  The Court reads the PLRA to say what it does not. It
does so for reasons that the parties did not brief; that have
no basis in our doctrine; and that are contrary to well-
established principles of statutory interpretation. In so
doing, the Court creates a regime under which an exhaustion
requirement designed to “reduce the quantity and improve
the quality of prisoner suits” just generates more litigation
of its own. Porter v. Nussle, 534 U. S. 516, 524 (2002).
Now, any prisoner can potentially obtain full jury review of
the very threshold question that was designed to streamline
prisoner litigation. All he has to do is fnd a way to trans-
form his inability to use the prison system into a claim for
relief. Congress did not devise such a rule, and we have
never adopted one. I respectfully dissent.
                            Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
Page Proof Pending Publication
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

p. 464, line 2 from bottom: “94 Stat. 352” is changed to “110 Stat. 1321–71,
   as amended,”

```

---
