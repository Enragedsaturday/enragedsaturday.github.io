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

## GROUP: _overhaul2/lake/cases/United States v. Morley.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Morley"
type: case
citation: "99 F.4th 1328 (2024)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Eleventh Circuit"
court_level: coa
circuit: 11th
year: 2024
date_decided: 2024-04-30
docket: 22-12988
authority_weight: "Binding in-circuit — 11th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2024-04-30
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Morley
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/9498175/united-states-v-derrick-alfondso-morley/"
  cluster_id: 9498175
  opinion_id: 9964788
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Recent development (role-based)"
related: ["[[Carroll v. United States]]", "[[United States v. Ross]]", "[[California v. Carney]]"]
aliases: ["United States v. Morley (11th Cir. 2024)"]
tags: ["case", "fourth-amendment", "automobile-exception", "vehicle-search", "probable-cause", "eleventh-circuit"]
holding: "Recites the modern two-element formulation of the automobile exception: a warrantless vehicle search is permitted if (1) the vehicle is…"
lake:
  record_id: United States v. Morley
  status: verified
  projected_at: 2026-07-09
---

# United States v. Morley

*99 F.4th 1328 (11th Cir. 2024)* · U.S. Court of Appeals, Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Morley was convicted of drug offenses arising from a controlled transaction. At an associate's direction, a cooperating individual (Fred) retrieved a briefcase containing cocaine from the passenger seat of Morley's car without a warrant. Morley moved to suppress the cocaine as the fruit of an unlawful search. The district court denied the motion, finding that the automobile exception (and apparent-authority consent) justified the warrantless search; Morley was convicted and appealed.

## Issue
Whether the warrantless retrieval of the briefcase from the passenger compartment of Morley's car was justified under the automobile exception to the Fourth Amendment's warrant requirement.

## Rule
The automobile exception permits a warrantless vehicle search on two elements. The court restated the circuit's formulation: "The automobile exception allows law enforcement to conduct a warrantless search of a vehicle if (1) the vehicle is readily mobile and (2) law enforcement has probable cause to search it." — *United States v. Morley*, 99 F.4th 1328 (11th Cir. 2024) (slip op., at 15). ^pin-op15

The first element is satisfied by mere operability: "All that is necessary to satisfy the first element is that the automobile is operational." — [*Id.*](https://www.courtlistener.com/opinion/9498175/united-states-v-derrick-alfondso-morley/#:~:text=All%20that%20is%20necessary%20to) ^pin-op15a

## Application
Both elements were satisfied here. Morley drove the car to the scene and did not dispute that it was readily mobile, so the first element was met. As to probable cause, Morley's associate had negotiated an $84,000 drug deal, Morley arrived and parked close to the associate's and the cooperating individual's cars, and the associate then directed the cooperating individual to retrieve the drugs from the passenger seat of Morley's car — facts the court held were more than enough to establish probable cause to search. Because both elements were met, law enforcement was authorized to conduct the warrantless search of Morley's car.

## Conclusion
Both elements of the automobile exception were satisfied, so the warrantless search of Morley's car was constitutionally permissible; the Eleventh Circuit affirmed the denial of Morley's suppression motion.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 11th Cir.**
- No negative treatment. *Morley* is a recent published Eleventh Circuit decision restating the circuit's two-element automobile-exception test (ready mobility + probable cause) and applying it to a vehicle driven to the scene of a drug transaction.

## Appears on
- [[Automobile Exception]] — *Recent development (role-based)*

## Sources
- *United States v. Morley*, 99 F.4th 1328 (11th Cir. 2024) — https://www.courtlistener.com/opinion/9498175/united-states-v-derrick-alfondso-morley/ — pinpoints given as slip-opinion pages (CourtListener carries the slip opinion; cluster 9498175 → opinion 9964788).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "aa87aa240b8fb8b1", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Morley"}, "payload": {"all": [{"cite": "99 F.4th 1328", "page": "1328", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}], "display": "99 F.4th 1328", "official": {"cite": "99 F.4th 1328", "page": "1328", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "99"}, "official_selection_present": true, "record_id": "United States v. Morley"}}
{"assertion_id": "9318dcb065a4425a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op15a", "record_id": "United States v. Morley"}, "payload": {"fragment": "#:~:text=All%20that%20is%20necessary%20to", "page": null, "pin_id": "pin-op15a", "pinpoint_status": "slip-only", "quote": "All that is necessary to satisfy the first element is that the automobile is operational.", "quote_fidelity": "matched", "record_id": "United States v. Morley", "star_marker": null}}
{"assertion_id": "ac24822611ac43db", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op15", "record_id": "United States v. Morley"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op15", "pinpoint_status": "slip-only", "quote": "--- # United States v. Morley *99 F.4th 1328 (11th Cir. 2024)* · U.S. Court of Appeals, Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Morley was convicted of drug offenses arising from a controlled transaction. At an associate's direction, a cooperating individual (Fred) retrieved a briefcase containing cocaine from the passenger seat of Morley's car without a warrant. Morley moved to suppress the cocaine as the fruit of an unlawful search. The district court denied the motion, finding that the automobile exception (and apparent-authority consent) justified the warrantless search; Morley was convicted and appealed. ## Issue Whether the warrantless retrieval of the briefcase from the passenger compartment of Morley's car was justified under the automobile exception to the Fourth Amendment's warrant requirement. ## Rule The automobile exception permits a warrantless vehicle search on two elements. The court restated the circuit's formulation:", "quote_fidelity": "mismatch", "record_id": "United States v. Morley", "star_marker": null}}
{"assertion_id": "8f6d822572288570", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Morley"}, "payload": {"as_of_content": "2024-04-30", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Morley", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Morley

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Morley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Derrick Alfondso Morley",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Morley",
    "court": "U.S. Court of Appeals, Eleventh Circuit",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "11th",
    "state": null,
    "date_decided": "2024-04-30",
    "year": 2024,
    "docket": "22-12988",
    "cluster_id": 9498175,
    "lead_opinion_id": 9964788,
    "sibling_ids": [
      9964788
    ],
    "absolute_url": "/opinion/9498175/united-states-v-derrick-alfondso-morley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "99 F.4th 1328",
      "volume": "99",
      "reporter": "F.4th",
      "page": "1328",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "99 F.4th 1328",
        "volume": "99",
        "reporter": "F.4th",
        "page": "1328",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "99 F.4th 1328",
    "official_selection": {
      "court_class": "coa",
      "selected": "99 F.4th 1328",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op15",
      "page": null,
      "quote": "--- # United States v. Morley *99 F.4th 1328 (11th Cir. 2024)* \u00b7 U.S. Court of Appeals, Eleventh Circuit \u00b7 **Binding in-circuit \u2014 11th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Morley was convicted of drug offenses arising from a controlled transaction. At an associate's direction, a cooperating individual (Fred) retrieved a briefcase containing cocaine from the passenger seat of Morley's car without a warrant. Morley moved to suppress the cocaine as the fruit of an unlawful search. The district court denied the motion, finding that the automobile exception (and apparent-authority consent) justified the warrantless search; Morley was convicted and appealed. ## Issue Whether the warrantless retrieval of the briefcase from the passenger compartment of Morley's car was justified under the automobile exception to the Fourth Amendment's warrant requirement. ## Rule The automobile exception permits a warrantless vehicle search on two elements. The court restated the circuit's formulation:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op15a",
      "page": null,
      "quote": "All that is necessary to satisfy the first element is that the automobile is operational.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 22722,
      "fragment": "#:~:text=All%20that%20is%20necessary%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2024-04-30",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Morley",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Lawrence Alexander",
          "cluster_id": 10814315,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Morley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9964788) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca11)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      },
      "lane2_top_cited": {
        "query": "cites:(9964788)",
        "reviewed": 1,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(9964788)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(9964788)",
    "indexed_citing_opinions": 1,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9964788,
        "count": 1,
        "count_source": "search"
      }
    ],
    "citation_count": 10,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-morley.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 1,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9964788,
        "cited_id": 70414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 72529,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 76193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 77108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 77161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 77608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 78102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 78192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 78506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 216166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 453288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 458882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 499145,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 551365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 568540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 657263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 676156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 679522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 770221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 773384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 820615,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 2648815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 2766686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4184984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4234128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4283480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4301605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4703255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 9323286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 9427680,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 9433305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 9477172,
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
    "date_created": "2026-07-06T01:51:28Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:51:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:51:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:52:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:51:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Morley

```
USCA11 Case: 22-12988    Document: 50-1      Date Filed: 04/30/2024   Page: 1 of 30




                                                            [PUBLISH]
                                    In the
                 United States Court of Appeals
                         For the Eleventh Circuit

                           ____________________

                                 No. 22-12988
                           ____________________

        UNITED STATES OF AMERICA,
                                                       Plaintiﬀ-Appellee,
        versus
        DERRICK ALFONDSO MORLEY,


                                                    Defendant-Appellant.


                           ____________________

                  Appeal from the United States District Court
                      for the Southern District of Florida
                     D.C. Docket No. 1:21-cr-20519-DPG-2
                           ____________________
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 2 of 30




        2                       Opinion of the Court                22-12988

        Before WILSON, LUCK, and LAGOA, Circuit Judges.
        LAGOA, Circuit Judge:
                A jury convicted Derrick Morley of conspiracy to possess
        with intent to distribute five hundred grams or more of cocaine, in
        violation of 21 U.S.C. § 846, and possession with intent to distribute
        five hundred grams or more of cocaine, in violation of 21 U.S.C.
        § 841(a)(1). For each count, Morley was sentenced to a term of 60
        months’ imprisonment, to be served concurrently. Morley now
        appeals his convictions and sentence, arguing that: (1) the district
        court erred in denying his motion to suppress evidence that was
        the fruit of an unlawful search; (2) the trial evidence was insuffi-
        cient to support his convictions; (3) the district court erred in
        providing a deliberate ignorance jury instruction; and (4) the dis-
        trict court erred in denying him a safety valve sentence reduction
        under 18 U.S.C. § 3553(f). After carefully considering the parties’
        arguments and with the benefit of oral argument, we affirm Mor-
        ley’s convictions and sentence.
             I.     FACTUAL & PROCEDURAL BACKGROUND
               We begin with the government’s trial evidence as to two
        separate cocaine deals that led to Morley’s arrest. The first deal
        took place on August 6, 2021, when Morley’s associate and code-
        fendant, Valentino Edgecombe, sold half a kilogram of cocaine to
        a paid FBI confidential informant (“Fred”). The FBI learned, in
        early August 2021, that Edgecombe, a Bahamian national, had been
        in South Florida “looking to try to get off some dope.” Based on
        this information, Fred, at the FBI’s direction, arranged to meet
USCA11 Case: 22-12988       Document: 50-1      Date Filed: 04/30/2024      Page: 3 of 30




        22-12988                Opinion of the Court                          3

        Edgecombe in the parking lot of a Miami shopping mall, outside of
        a Bass Pro Shops. With law enforcement officers surveilling, Fred
        bought half a kilogram of cocaine from Edgecombe for $14,000.
                Following the first cocaine deal, Fred tried to negotiate a big-
        ger deal for six kilograms of cocaine. On September 22, 2021, on a
        recorded phone call, Fred told Edgecombe that he had the money
        ready to buy more cocaine. About ten minutes later, on a second
        recorded phone call, Edgecombe offered to send Fred “straight to
        the person” with the cocaine. Edgecombe explained, however,
        that the person would only relinquish the cocaine if Edgecombe
        first cleared his debt, which he’d previously said he owed to “the
        guy who was holding the dope.”
               About an hour after the second recorded phone call, law en-
        forcement observed Edgecombe meet up with Morley in the park-
        ing lot of a Fort Lauderdale hotel where Edgecombe was staying.
        Morley arrived in a maroon BMW, which law enforcement later
        confirmed that he owned. Morley parked near Edgecombe, en-
        tered Edgecombe’s car, and they drove off together. Expecting a
        deal to occur, law enforcement tracked Edgecombe and Morley
        from the hotel, first to a car parts store and then to a Sam’s Club.
        However, no deal took place that day.
               Instead, the second deal happened six days later on Septem-
        ber 28, 2021. The day prior, in a recorded phone call, Edgecombe
        again told Fred that he had to take him straight to his cocaine
        source to clear his debt and make the deal. Fred agreed to pay
        $28,000 per kilogram of cocaine, and the two decided they would
USCA11 Case: 22-12988      Document: 50-1     Date Filed: 04/30/2024     Page: 4 of 30




        4                      Opinion of the Court                22-12988

        meet up the next day and go together to the cocaine source. On
        the morning of the deal, Edgecombe sent a WhatsApp message to
        Fred indicating that he could sell him three kilograms of cocaine.
               Later that evening, before meeting Edgecombe, Fred met
        with law enforcement to prepare for a “controlled evidence pur-
        chase arrest operation.” Law enforcement gave Fred a hat
        equipped with a covert videorecording device and a backpack con-
        taining money for the deal. Law enforcement also told Fred to per-
        suade Edgecombe to meet him in “a specific part” of a parking lot
        of a Home Depot rather than going with Edgecombe to his source.
               Fred arrived at the Home Depot and, to coax Edgecombe
        into meeting him there, told Edgecombe that his car battery “was
        dead” and that his key “won’t crank.” Edgecombe ultimately
        agreed over the phone to meet Fred at the Home Depot to com-
        plete the deal. So, Fred sent a text message to Edgecombe with the
        address of the Home Depot.
               Edgecombe arrived at the Home Depot at around 8:30 p.m.
        and parked his car next to Fred’s car. Fred asked whether
        Edgecombe had the cocaine with him, and Edgecombe responded,
        “Yeah someone is right there” and promised “[i]t’s coming.”
        Edgecombe then tried to persuade Fred to get in the car with him,
        but Fred refused, stating “I can’t get in the car with you. I got too
        much money. I don’t got no gun.” Fred told Edgecombe to “tell
        [his] peoples” he can only get in Edgecombe’s car if he sees the co-
        caine first.
USCA11 Case: 22-12988      Document: 50-1     Date Filed: 04/30/2024     Page: 5 of 30




        22-12988               Opinion of the Court                        5

               Minutes later, Morley arrived in his maroon BMW and
        “trolled through the parking lot.” He parked his car, got out, and
        quickly walked toward a nearby Wendy’s restaurant. Edgecombe
        instructed Fred to “[g]o get it” from Morley’s passenger seat. Fred
        retrieved a “small briefcase” from Morley’s car and brought it to
        his car, confirming that it contained three kilograms of cocaine.
                  In the meantime, Morley tried to enter the Wendy’s, but the
        door was locked, so he paced back and forth outside. All the while,
        Morley kept looking back toward the Home Depot parking lot:
        “[H]e just kept looking over his shoulder and then he walked into
        . . . [t]he driveway area of Wendy’s, and he just kind of lingered in
        the area kind of like looking at the BMW, just watching it.” After
        several minutes, Morley walked across the street to help a family
        with a broken-down car.
              After Fred gave Edgecombe $84,000 for the cocaine, law en-
        forcement arrested Edgecombe. Law enforcement then arrested
        Morley across the street.
               Incident to his arrest, agents seized Morley’s cellphone, got
        a search warrant, and accessed his phone. The search revealed ex-
        tensive communications between Morley and Edgecombe leading
        up to the second cocaine deal, as well as evidence that Morley had
        acted on that communication. For instance, Morley and
        Edgecombe called each other fifteen times on the night of Septem-
        ber 28. Edgecombe also sent the address of the Home Depot to
        Morley in a text message, which came two minutes after Fred had
        sent the same address to Edgecombe. Data from Morley’s phone
USCA11 Case: 22-12988     Document: 50-1     Date Filed: 04/30/2024   Page: 6 of 30




        6                     Opinion of the Court               22-12988

        showed that he looked up directions from his home in Fort Lauder-
        dale to the Home Depot two minutes after Edgecombe had sent
        him the address.
               Edgecombe and Morley had also communicated in the lead-
        up to the first cocaine deal. On August 3, 2021, Edgecombe texted
        Morley, “i want you ride with me to deal with something also make
        yourself available” and “whenever i call you i want ride with me.”
        Then, on the day of the first deal, Edgecombe sent Morley a mes-
        sage with the address of the same Bass Pro Shops where Fred met
        Edgecombe.
             A grand jury returned a three-count indictment charging
        Morley with conspiring to possess with intent to distribute five
        hundred grams or more of cocaine in violation of 21 U.S.C. § 846
        (Count 1) and possessing with intent to distribute five hundred
        grams or more of cocaine in violation of 21 U.S.C. § 841(a)(1)
        (Count 3).
               Morley moved to suppress the cocaine that Fred, at
        Edgecombe’s direction, took from Morley’s vehicle without a war-
        rant. The government opposed Morley’s suppression motion. The
        government argued that the automobile exception to the Fourth
        Amendment’s warrant requirement applied because there was a
        fair probability that Fred would find contraband in Morley’s car.
        The government noted that Fred and Edgecombe “had negotiated
        an $84,000 drug deal, and Edgecombe—who had previously sold
        [Fred] half a kilogram of cocaine—told [Fred] where to find the
        drugs.” Thus, the government concluded, Fred reasonably
USCA11 Case: 22-12988       Document: 50-1       Date Filed: 04/30/2024     Page: 7 of 30




        22-12988                Opinion of the Court                           7

        believed he would find drugs in Morley’s car. In any event, the
        government added, the consent exception applied because Fred
        reasonably believed Edgecombe had the authority to direct him to
        search Morley’s car. Morley argued that neither of the two rele-
        vant exceptions to the Fourth Amendment’s warrant requirement
        applied to Fred’s search of his car.
                The district court held an evidentiary hearing at which Mi-
        ami-Dade Detective and FBI Organized Crime Task Force Officer
        Wendell Johnson testified. After hearing the officer’s testimony,
        the district court denied Morley’s motion. First, the district court
        found that there was probable cause to believe Morley’s car con-
        tained contraband or evidence of a crime because Edgecombe and
        Fred “picked specific remote locations” for their drug deals, and
        “it’s really hard to believe that . . . [Morley] pulled up in close prox-
        imity” by happenstance. And second, the district court found that
        apparent authority existed under the circumstances because “the
        drugs were retrieved exactly where Mr. Edgecombe said that they
        would be.”
               Morley proceeded to a four-day jury trial. The govern-
        ment’s proposed jury instructions included the pattern instruction
        on deliberate ignorance. At the charge conference, Morley ob-
        jected to the government’s proposed deliberate ignorance instruc-
        tion. He contended that the record did not support the instruction
        because “[t]here ha[d] been no proof of any evidence in reference
        to fingerprints or . . . DNA” and “the testimony on exactly where
        the bag was located and how it was taken out of the car is extremely
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 8 of 30




        8                      Opinion of the Court                 22-12988

        wishy-washy.” In response, the government argued that deliberate
        ignorance was “an alternative proof,” which was “consistent with
        the evidence that Edgecombe had him drive a bag to the Home
        Depot, and he never made any attempt to ask Edgecombe what
        was in that bag, despite the multiple calls they had.” The district
        court deferred ruling on Morley’s objection.
                After the close of the evidence, the district court decided to
        give the jury instruction because the evidence “equally could be
        consistent with actual knowledge or deliberate ignorance.” The
        district court pointed to Morley’s actions, like walking away from
        the car, and the way the drugs were packaged. The instruction
        mirrored the government’s proposed instruction.
               During trial, Morley twice moved for a judgment of acquit-
        tal under Federal Rule of Criminal Procedure 29(a). The district
        court denied both of his motions. The jury ultimately found him
        guilty as charged in the indictment. Afterward, Morley moved for
        a judgment of acquittal notwithstanding the verdict under Rule
        29(c). The district court denied his motion in a paperless order.
               Before sentencing, the United States Probation Office pre-
        pared a Presentence Investigation Report (“PSI”) using the 2021
        Sentencing Guidelines Manual. The PSI held Morley accountable
        for 3.518 kilograms of cocaine (about half a kilogram for the August
        6 deal and three kilograms for the September 28 deal), resulting in
        a total offense level of 28. It also assessed three criminal history
        points based on Morley’s prior 37-month sentence for conspiracy
        to import 100 kilograms or more of marijuana. With three criminal
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024      Page: 9 of 30




        22-12988               Opinion of the Court                          9

        history points, Morley fell into criminal history category II. To-
        gether, Morley’s total offense level and criminal history category
        produced a guideline range of 87 to 108 months’ imprisonment.
               Through his trial attorney, Morley filed several objections to
        the PSI’s description of his offense conduct. Despite the jury’s ver-
        dict, Morley maintained his innocence and “denied all knowledge”
        of Edgecombe’s sale of cocaine to Fred. In support, Morley at-
        tached a post-trial polygraph examination report, which claimed
        Morley “was truthful” in denying his knowledge of the conspiracy
        and the cocaine. Morley attached the full version of the polygraph
        examiner’s report to a motion for a downward variance filed a cou-
        ple of weeks later.
                A new attorney later entered his appearance to represent
        Morley for sentencing. Through his sentencing attorney, Morley
        filed additional objections to the PSI in which, among other things,
        he argued for a base offense level of 26, because the evidence only
        supported his responsibility for the September 28 deal, and a role
        reduction under U.S.S.G. § 3B1.2. Morley also moved to continue
        his sentencing hearing because his sentencing attorney, unlike his
        trial attorney, believed that he might qualify for relief from the
        mandatory minimum sentence under 18 U.S.C. § 3553(f). Known
        as the safety valve, that statute allows the district court to impose
        a sentence below the mandatory minimum sentence for drug
        crimes if the defendant meets five criteria. § 3553(f)(1)–(5). Two
        of the statutory criteria are relevant here. First, under § 3553(f)(1),
        the district court must find that:
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024      Page: 10 of 30




        10                      Opinion of the Court                  22-12988

               (1) the defendant does not have—
                  (A) more than 4 criminal history points, ex-
                  cluding any criminal history points resulting
                  from a 1-point offense, as determined under
                  the sentencing guidelines;
                  (B) a prior 3-point offense, as determined un-
                  der the sentencing guidelines; and
                  (C) a prior 2-point offense, as determined un-
                  der the sentencing guidelines[.]
               Second, under § 3553(f)(5), the district court must find that
        the defendant truthfully provided to the government “all infor-
        mation and evidence the defendant has concerning the offense or
        offenses that were part of the same course of conduct or of a com-
        mon scheme or plan.”
               As for § 3553(f)(1), Morley argued that his prior three-point
        offense for conspiracy to import marijuana did not preclude him
        from relief because the safety valve’s criminal- history-point provi-
        sion is “conjunctive.” The safety valve, he argued, only excludes
        defendants who have all three things: (A) more than four criminal
        history points, excluding any points from one-point offenses, (B) a
        prior three-point offense, and (C) a prior two-point violent offense.
        And because he did not have more than four criminal history points
        or a prior two-point violent offense, he could qualify for relief if the
        court gave him time to submit a truthful statement to the govern-
        ment.
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 11 of 30




        22-12988               Opinion of the Court                         11

                After the district court continued Morley’s sentencing hear-
        ing, he submitted a written safety valve statement in an attempt to
        comply with § 3553(f)(5). In his statement, Morley again claimed
        he did not know he had delivered cocaine to a drug deal. He ex-
        plained that, when he arrived at the Home Depot, he “walked to a
        nearby Wendy’s for something to eat” and left his car unlocked
        “because the locks did not work (as shown in the trial) in an at-
        tempt to buy some food.” He pointed to his post-arrest statements
        and the polygraph test for corroboration of his lack of knowledge.
        But in the end, he admitted, whether it “was naïve, stupid or com-
        pletely negligent,” he “did bring the bag which contained cocaine
        in this case to the parking lot of the Home Depot,” and he accepted
        full responsibility for it.
               At sentencing, the district court granted two of Morley’s ob-
        jections to the PSI’s offense-level calculation. First, it found Morley
        responsible for 3, rather than 3.518, kilograms of cocaine, which
        reduced his base offense level to 26 under U.S.S.G. § 2D1.1(c)(7).
        Second, it awarded Morley a two-level minor role reduction under
        U.S.S.G. § 3B1.2, producing a new total offense level of 24.
                The district court then found Morley did not qualify for
        safety-valve relief both because of his criminal history and his fail-
        ure to truthfully provide the government with all the information
        he had concerning his offenses. As to his criminal history, the dis-
        trict court interpreted § 3553(f)(1) as “disjunctive,” meaning a de-
        fendant must not have any of (1) more than four criminal history
        points, (2) a prior three-point offense, or (3) a prior two-point
USCA11 Case: 22-12988         Document: 50-1   Date Filed: 04/30/2024     Page: 12 of 30




        12                       Opinion of the Court                22-12988

        violent offense to qualify for relief. And because Morley had a prior
        three-point offense, the court found that he was not safety-valve
        eligible. As to his statement, the district court agreed with Morley’s
        contention that the government’s “belief regarding truthfulness”
        and noted that “perhaps” even “the jury’s findings” did not prevent
        it from finding his statement truthful. Still, the district court disa-
        greed that Morley provided a truthful and complete statement un-
        der § 3553(f)(5), particularly considering the government’s “strong
        circumstantial case.”
               The district court found that Morley’s total offense level of
        24 and his criminal history category of II produced a guideline
        range of 57 to 71 months. Because the mandatory minimum sen-
        tence for his offenses was 60 months, however, the district court
        calculated the guideline range as 60 to 71 months. The govern-
        ment advocated for a 65-month term of imprisonment, citing Mor-
        ley’s prior 37-month sentence for his federal drug conviction and
        the need to promote deterrence, respect for the law, “and send a
        message that the defendant should not be dealing with drugs.”
        Morley asked for the mandatory minimum sentence of 60 months.
        Before the district court imposed its sentence, it allowed Morley to
        provide a statement.
              The district court sentenced Morley to two concurrent
        terms of 60 months’ imprisonment on both counts, the mandatory
        minimum sentence for each count under § 841(b)(1)(B)(ii). This
        timely appeal followed.
                        II.      STANDARDS OF REVIEW
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024      Page: 13 of 30




        22-12988                Opinion of the Court                         13

               A district court’s denial of a motion to suppress evidence is
        reviewed under a mixed standard. United States v. Jiminez, 224 F.3d
        1243, 1247 (11th Cir. 2000). We review the district court’s findings
        of fact under the clearly erroneous standard and its application of
        law to those facts de novo. Id. We also give “due weight” to the
        inferences that the district court and law enforcement officers draw
        from the facts. Ornelas v. United States, 517 U.S. 690, 699 (1996).
        When considering a ruling on a motion to suppress, we must con-
        strue all facts in the light most favorable to the party prevailing in
        the district court. United States v. Behety, 32 F.3d 503, 510 (11th Cir.
        1994).
                “We review de novo a [d]istrict [c]ourt’s denial of judgment
        of acquittal on sufficiency of evidence grounds, considering the ev-
        idence in the light most favorable to the [g]overnment, and draw-
        ing all reasonable inferences and credibility choices in the [g]overn-
        ment’s favor.” United States v. Capers, 708 F.3d 1286, 1296 (11th Cir.
        2013) (emphasis omitted). We must affirm if “after viewing the ev-
        idence in the light most favorable to the prosecution, any rational
        trier of fact could have found the essential elements of the crime[s]
        beyond a reasonable doubt.” United States v. Hernandez, 433 F.3d
        1328, 1335 (11th Cir. 2005) (emphasis omitted) (quoting Jackson v.
        Virginia, 443 U.S. 307, 319 (1979)).
               We also review de novo whether the circumstances of a par-
        ticular case rendered it appropriate to instruct the jury on deliber-
        ate ignorance. United States v. Stone, 9 F.3d 934, 937 (11th Cir. 1993).
        But our review of jury instructions is deferential, and we will
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 14 of 30




        14                     Opinion of the Court                  22-12988

        reverse only “if we are left with a substantial and eradicable doubt
        as to whether the jury was properly guided in its deliberations.”
        United States v. Crabtree, 878 F.3d 1274, 1289 (11th Cir. 2018) (quot-
        ing United States v. Steed, 548 F.3d 961, 977 (11th Cir. 2008)).
                                 III.   ANALYSIS
                On appeal, Morley argues that: (1) the district court erred in
        denying his motion to suppress the evidence of the briefcase as the
        fruit of an unlawful search; (2) the evidence at trial was insufficient
        to support his convictions; (3) the district court erred in providing
        a deliberate ignorance jury instruction; and (4) the district court
        erred in denying him a safety valve sentence reduction. We ad-
        dress each of his challenges in turn.
                             A. The Motion to Suppress
                Morley argues that Fred’s retrieval of the briefcase from the
        passenger seat of Morley’s car was an unconstitutional search in
        violation of the Fourth Amendment. It is undisputed that Fred’s
        actions amounted to a warrantless search that implicated the
        Fourth Amendment’s protections. We must determine, however,
        whether any exception to the Fourth Amendment’s warrant re-
        quirement rendered the search constitutionally permissible. The
        district court specifically found that two exceptions applied: the au-
        tomobile exception and the consent exception by way of apparent
        authority.
              As an initial matter, Morley mischaracterizes the automobile
        and apparent authority doctrines as requirements that must be met
        for a valid search. Those doctrines, however, are separate
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 15 of 30




        22-12988               Opinion of the Court                         15

        exceptions to the Fourth Amendment’s warrant requirement, and
        either of which may provide an independent basis for us to affirm
        the denial of Morley’s suppression motion. Here, we conclude that
        the district court did not abuse its discretion in finding that the au-
        tomobile exception applied.
                The automobile exception allows law enforcement to con-
        duct a warrantless search of a vehicle if (1) the vehicle is readily
        mobile and (2) law enforcement has probable cause to search it.
        United States v. Lindsey, 482 F.3d 1285, 1293 (11th Cir. 2007). All
        that is necessary to satisfy the first element is that the automobile
        is operational. United States v. Watts, 329 F.3d 1282, 1286 (11th Cir.
        2003). In United States v. Nixon, 918 F.2d 895 (11th Cir. 1990), this
        Court explained that “ready mobility” is “inherent in all automo-
        biles that reasonably appear to be capable of functioning.” Id. at
        903 (emphasis in original); see also United States v. Alexander, 835
        F.2d 1406, 1409 (11th Cir. 1988) (stating that the vehicle need not
        be moving at the moment when police obtain probable cause to
        search and that the ability of a vehicle to become mobile is suffi-
        cient). That requirement is met here because Morley drove the car
        to the scene, nor does Morley challenge that his vehicle was readily
        mobile. See Sapuppo v. Allstate Floridian Ins. Co., 739 F.3d 678, 680
        (11th Cir. 2014) (noting that a party abandons an issue by not rais-
        ing it on appeal).
              Turning to the second element, probable cause exists when,
        “under the totality of the circumstances, there is a fair probability
        that contraband or evidence of a crime will be found in the
USCA11 Case: 22-12988     Document: 50-1     Date Filed: 04/30/2024    Page: 16 of 30




        16                    Opinion of the Court                22-12988

        vehicle.” Lindsey, 482 F.3d at 1293 (citation omitted). For example,
        in United States v. Lanzon, 639 F.3d 1293 (11th Cir. 2011), we held
        that the district court did not err in denying Lanzon’s motion to
        suppress because officers had probable cause to search Lanzon’s
        truck pursuant to the automobile exception. Id. at 1300. In that
        case, Lanzon participated in instant message conversations with an
        undercover agent posing as “Tom.” Id. Lanzon described to
        “Tom” his intent to have sex with a minor, and he agreed to meet
        “Tom” and the minor at a specific time and place and to bring col-
        ored condoms with him. Id. After driving his truck to the desig-
        nated meeting place at the agreed-upon time, Lanzon approached
        the officers who were posing as “Tom” and the minor and said,
        “Tom, Tom.” Id. Lanzon was then arrested, and a search of his
        person yielded no condoms. Id. The officers sought Lanzon’s con-
        sent to search his truck, but he refused. Id. at 1297. The officers
        then searched the truck anyway—using Lanzon’s keys to open it—
        and found the colored condoms, along with flavored lubricant and
        a receipt for the purchase of those items. Id. During his criminal
        proceedings, Lanzon filed to suppress the evidence seized from his
        truck, which the district court denied. Id. at 1299. On appeal, we
        held that, under the totality of the circumstances, there was a fair
        probability that evidence of a crime would be found in Lanzon’s
        vehicle. Id. at 1300.
               The facts and circumstances known to law enforcement
        here are similar to those in Lanzon. As in Lanzon, law enforcement
        here, via a confidential informant, engaged in conversations with
        Edgecombe that led to an agreement to meet at a specific time and
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024     Page: 17 of 30




        22-12988               Opinion of the Court                        17

        place for an illicit act. The only significant difference here is the
        involvement of a third party, Morley. But Morley arrived at the
        designated meeting place at the agreed upon time, minutes after
        Edgecombe had texted him to come, and after Edgecombe told
        Fred that the cocaine was on its way. When Morley arrived, it was
        clear that Edgecombe recognized him. Indeed, Edgecombe explic-
        itly directed Fred to retrieve the cocaine from Morley’s car. There
        was more than a reasonable probability that Fred would find con-
        traband in the exact place that Edgecombe told him to look.
               Morley’s argument against probable cause relies heavily on
        one unpublished case, United States v. Smith, 596 F. App’x 804 (11th
        Cir. 2015), in which this Court affirmed a district court’s finding
        that probable cause existed. Id. at 807. In Smith, this Court held
        that a police officer’s credible belief that “he smelled marijuana
        coming from the car” of the defendant, whom he had just arrested
        for marijuana possession, sufficed to show probable cause to con-
        duct a warrantless search of the vehicle. Id. Morley’s argument
        largely consists of a recitation of the facts in Smith in an effort to
        distinguish it from the facts here. But there are multiple problems
        with Morley’s approach. For starters, Morley fails to explain how
        an unpublished case in which this Court found that law enforce-
        ment acted reasonably establishes that law enforcement acted un-
        reasonably here. Additionally, unlike the officer in Smith, Fred did
        not have to logically deduce that there might be contraband in the
        car based on smell or any other subjective factor. Fred searched
        Morley’s car after Edgecombe first told Fred that the cocaine was
        on its way and then specifically directed him to “[g]o get” the
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 18 of 30




        18                     Opinion of the Court                  22-12988

        cocaine from Morley’s passenger seat. Thus, the probability that
        Fred would find contraband in Morley’s car was no less than it was
        in Smith.
               Morley also misconstrues both the standard of review and
        the legal test for probable cause. Regarding the standard of review,
        he argues that it “is not improbable that no reasonable fact finder
        could accept” an alternative explanation. Our review, however,
        does not ask whether there is some possible alternative explanation
        that a reasonable factfinder could have accepted. Rather, we re-
        view the district court’s findings of fact only for clear error, and we
        must give due weight to the inferences that the district court and
        law enforcement officers draw from those facts. Ornelas, 517 U.S.
        at 699. And when considering a ruling on a motion to suppress, we
        must construe all facts in the light most favorable to the party pre-
        vailing in the district court—here, the government. See Behety, 32
        F.3d at 510.
                As to the proper legal test, Morley argues that he was merely
        used by Edgecombe as a pawn to unwittingly facilitate the Septem-
        ber 28 deal. This conclusion, he contends, is supported by the fact
        that Edgecombe unilaterally involved an innocent decoy for the
        prior August 6 drug deal. But Morley’s knowledge, or lack thereof,
        is irrelevant to the probable cause inquiry. Instead, it is “the facts
        and circumstances within [law enforcement’s] knowledge” that
        matter. Rankin v. Evans, 133 F.3d 1425, 1435 (11th Cir. 1998) (quot-
        ing Williamson v. Mills, 65 F.3d 155, 158 (11th Cir. 1995)). Even if
        Morley were “unwittingly duped” into bringing the cocaine to the
USCA11 Case: 22-12988     Document: 50-1     Date Filed: 04/30/2024   Page: 19 of 30




        22-12988              Opinion of the Court                      19

        deal, his supposed lack of knowledge has no bearing on law en-
        forcement’s knowledge as to the probability that Morley’s car con-
        tained cocaine.
               Under the totality of the circumstances, the facts and cir-
        cumstances that were known to law enforcement at the relevant
        time supported a fair probability that cocaine would be found in
        Morley’s vehicle. Edgecombe had previously sold Fred half a kilo-
        gram of cocaine, and Fred and Edgecombe had no other relation-
        ship besides that of customer and drug dealer. Turning to the night
        of September 28, Fred and Edgecombe had negotiated an $84,000
        drug deal, and Edgecombe made it clear to Fred that he was not
        working alone. Edgecombe consistently asked Fred to go straight
        to “the guy who was holding the dope.” And on the night of the
        deal, Edgecombe asked Fred to drive with him to a different loca-
        tion to get the cocaine from another person. After Fred refused,
        Edgecombe told Fred that his associate was bringing it to them at
        the Home Depot. Shortly afterward, Morley arrived, and parked
        his vehicle close to Edgecombe and Fred’s cars. Edgecombe then
        directed Fred to retrieve the drugs from the passenger seat of Mor-
        ley’s car. This was more than enough to establish probable cause
        under the automobile exception.
                Because both elements of the automobile exception were
        satisfied, law enforcement was authorized to conduct a warrantless
        search of Morley’s car. Watts, 329 F.3d at 1286. We therefore af-
        firm the district court’s denial of Morley’s motion to suppress.
USCA11 Case: 22-12988        Document: 50-1   Date Filed: 04/30/2024     Page: 20 of 30




        20                      Opinion of the Court                22-12988

                        B.      Sufficiency of the Evidence
                Morley next challenges the sufficiency of the evidence sup-
        porting his convictions for conspiracy to possess with intent to dis-
        tribute cocaine in violation of 21 U.S.C. § 846 and possession of co-
        caine with intent to distribute in violation of 21 U.S.C. § 841(a)(1).
        Morley argues that the evidence here was solely circumstantial and
        that it was insufficient for a reasonable jury to find him guilty be-
        yond a reasonable doubt. Specifically, Morley argues that the pros-
        ecution failed to prove that he was a willing participant in the con-
        spiracy and that he knew that the briefcase contained cocaine.
                Both of the offenses for which Morley was convicted have a
        guilty knowledge element. The conspiracy charge under § 846 re-
        quired the government to prove: (1) the existence of an illegal
        agreement between two or more people to distribute cocaine; (2)
        that Morley knew of the agreement and its goal; and (3) that Mor-
        ley knowingly joined or participated in the agreement. See United
        States v. Brown, 587 F.3d 1082, 1089 (11th Cir. 2009). And the sub-
        stantive possession charge under § 841(a)(1) required the govern-
        ment to prove that Morley knowingly possessed cocaine and in-
        tended to distribute it. United States v. Mercer, 541 F.3d 1070, 1076
        (11th Cir. 2008). Because guilty knowledge can rarely be estab-
        lished directly, however, “a jury may infer knowledge and criminal
        intent from circumstantial evidence alone.” United States v. Duenas,
        891 F.3d 1330, 1334 (11th Cir. 2018).
             Morley argues that the circumstantial evidence here is not
        enough to support an inference of knowledge. He contends that
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024     Page: 21 of 30




        22-12988               Opinion of the Court                        21

        this is a case of “guilt by association,” and that close association
        with a co-conspirator or mere presence at the scene of the crime is
        insufficient evidence to prove knowing participation in a conspir-
        acy. Morley is correct that “[n]either association with a co-con-
        spirator nor presence at the scene of a crime, standing alone, will
        support a finding of specific knowledge.” Id. (citing United States v.
        Louis, 861 F.3d 1330, 1333 (11th Cir. 2017)). But “presence none-
        theless is a probative factor which the jury may consider in deter-
        mining whether a defendant was a knowing and intentional partic-
        ipant in a criminal scheme.” United States v. Miranda, 425 F.3d 953,
        959 (11th Cir. 2005) (quoting United States v. McDowell, 250 F.3d
        1354, 1365 (11th Cir. 2001)).
                Relying mainly on our decision in United States v. Sullivan,
        763 F.2d 1215 (11th Cir. 1985), Morley argues that his association
        with Edgecombe along with his presence at the scene is insufficient
        to support his convictions. In Sullivan, six codefendants were con-
        victed of conspiring to import marijuana from Columbia and dis-
        tribute it in the United States. Id. at 1216. The plan was to fly the
        marijuana to Florida, and then at the airport landing strip, to of-
        fload that marijuana into vans. Id. at 1216–17. Those vans would
        then deliver the marijuana to other drivers who would be waiting
        at a nearby hotel and would keep distributing the marijuana. Id.
        All six codefendants appealed the sufficiency of the evidence sup-
        porting their conspiracy convictions, but this Court found that only
        one codefendant, Martos, raised a legitimate challenge. Id. at 1218.
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024    Page: 22 of 30




        22                     Opinion of the Court                22-12988

               This Court summarized the evidence related to Martos as
        follows. Drug Enforcement Administration agents saw Martos in
        a hotel parking lot near a red van. Id. at 1219. A codefendant, Mar-
        tinez, arrived in a blue van and walked over to Martos. Id. Martos
        and Martinez then walked over to two other codefendants, and all
        four walked around the parking lot for about five minutes. Id.
        Martos and Martinez went to the blue van and one of them, though
        it was never established who, removed a small bag from the van.
        Id. The two then went into the hotel lounge. Id. All four of them
        were later arrested, including Martos. Id. When Martos was ar-
        rested, he was with Martinez who was carrying the small handbag,
        which was found to contain a pistol. Id. There was no marijuana
        found at the scene of arrest because the plan was for other conspira-
        tors to offload the marijuana from the planes and transport it to the
        hotel to meet separate drivers who would distribute it to various
        other points. Id. at 1217. Therefore, though the police knew that
        some alleged conspirators would be drivers in the hotel parking lot
        awaiting other conspirators delivering marijuana from the airport,
        there was no evidence as to who the drivers at the hotel would be.
        Id.
               We reversed Martos’s conviction because there was no evi-
        dence that Martos knew of the existence of the conspiracy or that
        he knew that the van was intended to transport marijuana. Id. His
        conviction, rather, was seemingly based only “on his presence at
        the scene in the [hotel] parking lot.” Id. He was never “observed
        doing anything from which the jury could draw an inference that
        he was a member of the conspiracy.” Id.
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024     Page: 23 of 30




        22-12988               Opinion of the Court                        23

               Morley contends that this case is similar to Martos’s in Sulli-
        van because there was no evidence that Morley knew Edgecombe
        was planning to sell cocaine on August 6 or September 22 or that
        Morley knew Edgecombe’s briefcase contained cocaine that
        Edgecombe would instruct Fred to retrieve from Morley’s car. In-
        stead, Morley argues, he merely believed that he was meeting his
        friend, Edgecombe, after they scheduled a meeting at Home Depot
        for Morley to return the case left in his car. Morley points out that
        neither his DNA nor latent fingerprints were found on the cocaine
        or briefcase, so there was insufficient proof that he knew that he
        was transporting cocaine.
                The circumstantial evidence here, however, is far greater
        than it was in Sullivan and was more than sufficient for the jury to
        infer Morley’s knowledge. For starters, no marijuana was recov-
        ered at the scene of arrest in Sullivan, so it was much more attenu-
        ated to impute, to Martos, knowledge of a conspiracy to distribute
        drugs that Martos never physically possessed. In this case, it is un-
        disputed that Morley was in physical possession of the three kilo-
        grams of cocaine and that he transported the cocaine to the scene
        of the drug deal at the time it was supposed to occur. The only
        issue is whether a reasonable jury could have inferred that Morley
        knowingly agreed to do so despite his contention that he was an
        unsuspecting pawn. While knowledge requirements may vary
        widely based on the individual facts of each case, a jury can infer
        knowledge using certain guideposts, such as whether “a defendant
        was instrumental to a plan’s success, had ample opportunities to
        discover the critical fact, and was in frequent contact with someone
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 24 of 30




        24                     Opinion of the Court                  22-12988

        who knew that fact.” United States v. Colston, 4 F.4th 1179, 1190
        (11th Cir. 2021). Viewed in the light most favorable to the verdict,
        a reasonable jury could have found that Morley knew of the plan
        to deliver cocaine to a drug deal.
                Morley played an instrumental role in the plan’s success.
        Edgecombe relied on Morley to deliver $84,000 worth of cocaine
        to a drug deal that Edgecombe had been discussing with Fred for
        over a month. And a prudent drug dealer is not likely to entrust
        the delivery of costly amounts of drugs to unwitting participants.
        In fact, we have repeatedly held that because “‘a prudent smuggler
        is not likely to suffer the presence of unaffiliated bystanders,’ when
        the orchestrator of a conspiracy vests substantial trust in an associ-
        ate to contribute to the scheme, a jury may infer the associate’s
        knowing participation.” Duenas, 891 F.3d at 1334 (quoting United
        States v. Cruz-Valdez, 773 F.2d 1541, 1547 (11th Cir. 1985) (en banc)).
        The deal’s success depended on Morley delivering the cocaine. He
        did so, arriving at the designated meeting site, at the designated
        meeting time, minutes after Edgecombe directed him to show up.
               Morley’s communications with Edgecombe further support
        the inference of knowledge. On the day of the drug deal, Morley
        was in consistent contact with Edgecombe, who had brokered the
        cocaine deal with Fred. Morley’s phone records showed that he
        and Edgecombe called each other fifteen times, including multiple
        phone calls after Edgecombe had sent Morley the Home Depot ad-
        dress. The communications leading up to the September 28 deal
        suggested Morley’s knowledge, too. On September 22, Fred and
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024     Page: 25 of 30




        22-12988               Opinion of the Court                        25

        Edgecombe had a conversation at 10:01 a.m. about a deal for six
        kilograms of cocaine. During that call, Edgecombe told Fred that
        “it still isn’t really in place yet.” Fred explained that he wanted to
        know when it would be ready because he had “business” in Or-
        lando. After that call, Edgecombe and Morley spoke twice on the
        phone, once at 10:06 a.m. and again at 10:13 a.m. A minute after
        Edgecombe’s second call with Morley, Edgecombe called Fred
        again and told him he would send him “straight” and “directly” to
        the person with the cocaine.
                On the day of the August 6 deal, Edgecombe shared with
        Morley the address of the Bass Pro Shops. In addition, a few days
        before the August 6 drug deal, Edgecombe sent Morley two cryptic
        text messages: “I want you ride with me to deal with something
        also make yourself available,” and “whenever i call you i want ride
        with me.” In Duenas, we found similar messages to be a relevant
        indicator of the defendant’s knowledge. 891 F.3d at 1335. Specifi-
        cally, the defendant in Duenas texted his girlfriend two days before
        the transaction “that he was ‘going to do a special work,’ which he
        suggested would be lucrative for him.” Id. His girlfriend “re-
        sponded, ‘Good luck. God protect you and guide you,’” which this
        Court found to be an indicator of the defendant’s “knowing as-
        sumption of a palpable risk.” Id. The August 6 messages here are
        similar to those in Duenas. Edgecombe urging Morley to make
        himself available to ride with Edgecombe to deal with something
        whenever Edgecombe called, a few days before the first drug deal,
        could support an inference of Morley’s knowledge of the circum-
        stances. When paired with the communications leading up to, and
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 26 of 30




        26                     Opinion of the Court                  22-12988

        on the date of, the September 28 drug deal, the frequency and the
        timing of the calls suggested Morley was a knowing participant.
               Despite Morley’s arguments to the contrary, the circum-
        stantial evidence here went far beyond Morley’s mere presence at
        the scene or his close association with Edgecombe. Morley showed
        up at the designated meeting site, at the designated meeting time,
        minutes after Edgecombe directed him to come. He was entrusted
        with delivering the cocaine, so he was instrumental to the deal. His
        communications with Edgecombe, a knowing participant, were
        frequent and suspiciously timed. In totality, a jury could reasona-
        bly infer Morley’s knowing involvement in the cocaine conspiracy
        on these facts. The trial evidence was thus sufficient to support his
        convictions, and we affirm as to this issue.
                     C.     Deliberate Ignorance Instruction
               Morley also challenges the district court’s decision to pro-
        vide a jury instruction on deliberate ignorance. The district court
        instructed the jury on both actual knowledge and deliberate igno-
        rance because the evidence “equally could be consistent with ac-
        tual knowledge or deliberate ignorance.” The district court
        pointed to Morley’s actions, such as his walking away from the car,
        and the way the drugs were packaged.
                A deliberate ignorance instruction is appropriate when the
        facts “support the inference that the defendant was aware of a high
        probability of the existence of the fact in question and purposely
        contrived to avoid learning all of the facts in order to have a defense
        in the event of a subsequent prosecution.” United States v. Rivera,
USCA11 Case: 22-12988     Document: 50-1     Date Filed: 04/30/2024    Page: 27 of 30




        22-12988              Opinion of the Court                       27

        944 F.2d 1563, 1571 (11th Cir. 1991) (quoting United States v. Al-
        varado, 838 F.2d 311, 314 (9th Cir. 1987)). We have cautioned the
        district courts against instructing juries on deliberate ignorance
        when the evidence only points to either actual knowledge or no
        knowledge on the part of the defendant. Stone, 9 F.3d at 937 (citing
        Rivera, 944 F.2d at 1570–71). But it is not error “when the evidence
        could support both actual knowledge or deliberate ignorance and
        the jury was instructed on both.” United States v. Maitre, 898 F.3d
        1151, 1157 (11th Cir. 2018).
                Morley argues that the evidence only supported an actual-
        knowledge theory and points to our decision in United States v. Pe-
        rez-Tosta, 36 F.3d 1552 (11th Cir. 1994) for support. There, the de-
        fendant had driven a “cocaine-laden” truck to a house and “was
        present while seventy kilograms of cocaine were taken off the truck
        and placed in the bedroom of the house.” Id. at 1565. Because the
        only inference a jury could draw from this evidence was that the
        defendant’s presence during such a large movement of cocaine
        meant that he “had to have been aware of it,” we held that the dis-
        trict court erroneously gave a deliberate ignorance instruction. Id.
               But the facts here are different from Perez-Tosta. Unlike the
        defendant in Perez-Tosta, Morley attempted to distance himself
        from the deal as it took place. Morley received a text message from
        Edgecombe with the address of the Home Depot and, within
        minutes, left his house and drove there with a briefcase containing
        three kilograms of cocaine on his passenger seat. When Morley
        arrived, however, he did not attempt to find Edgecombe. Instead,
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024      Page: 28 of 30




        28                      Opinion of the Court                  22-12988

        he quickly exited his vehicle and walked across the street to a
        Wendy’s restaurant. After realizing that the Wendy’s was closed,
        Morley paced around outside and eventually made his way across
        the street to help a family with car troubles. Consequently, Morley
        was not present when Fred retrieved the three kilograms of cocaine
        from Morley’s car, or when Fred gave Edgecombe the $84,000 for
        that cocaine. These facts supported the alternative inference that
        Morley was aware of a high probability that he had delivered co-
        caine to a drug deal and had been trying to avoid learning all the
        facts in order to have a defense in a subsequent prosecution. Mor-
        ley’s actions therefore warranted the deliberate ignorance instruc-
        tion.
                In any event, the district court instructed the jury that it
        could convict if Morley had actual knowledge or deliberate igno-
        rance. If, as Morley contends, there was insufficient evidence that
        he was deliberately ignorant of the contents of the briefcase, then
        our precedent is clear that the jury must have convicted on the al-
        ternative theory—actual knowledge. See Colston, 4 F.4th at 1192
        (citing Stone, 9 F.3d at 938). Thus, even if the district court erred in
        giving the deliberate ignorance instruction, it was harmless. See id.
        In any event, Morley’s challenge to the jury instruction fails.
                          D.      Safety Valve Reduction
              Finally, Morley argues that the district court erred in its de-
        termination that he was ineligible for a safety valve sentence reduc-
        tion under the First Step Act. See 18 U.S.C. § 3553(f). The district
        court denied Morley a safety valve reduction on two grounds: (1)
USCA11 Case: 22-12988        Document: 50-1        Date Filed: 04/30/2024        Page: 29 of 30




        22-12988                  Opinion of the Court                              29

        Morley did not satisfy § 3553(f)(1) because he had a prior 3-point
        offense and (2) Morley did not satisfy § 3553(f)(5) because his safety
        valve statement was insufficiently truthful and complete. 1 In light
        of the Supreme Court’s recent decision in Pulsifer v. United States,
        144 S. Ct. 718 (2024), the district court’s first basis for denying safety
        valve relief was correct.
                At the time of sentencing, there were competing interpreta-
        tions as to whether § 3553(f)(1) was conjunctive or disjunctive. Af-
        ter noting that the issue was “still not settled by the Eleventh Cir-
        cuit,” the district court landed on the disjunctive side of the debate
        and based its first ground for denying safety valve relief on that
        finding. Shortly after Morley was sentenced, this Court released its
        en banc decision in United States v. Garcon, 54 F.4th 1274 (11th Cir.
        2022) (en banc), abrogated by Pulsifer, 144 S. Ct. 718. Vacating a prior
        panel decision that reached the opposite conclusion, our en banc
        Court determined that § 3553(f)(1) was “conjunctive” such that de-
        fendants were only disqualified from safety valve relief due to prior
        convictions if they had all of the criminal history features under
        subsection (f)(1). Id. at 1276.
                On appeal, Morley argued that Garcon invalidated the dis-
        trict court’s first basis for denying safety valve relief and, as to the
        second basis, that the district court clearly erred in finding that he
        failed to satisfy § 3553(f)(5). The government conceded that, after

        1 The relevant statutory provisions, along with the conjunctive versus disjunc-

        tive interpretative divide, are detailed in the Factual & Procedural Back-
        ground.
USCA11 Case: 22-12988      Document: 50-1       Date Filed: 04/30/2024      Page: 30 of 30




        30                      Opinion of the Court                   22-12988

        Garcon, the district court’s first basis for denying safety valve relief
        would have been incorrect. However, the government argued that
        we should affirm on the district court’s alternative rationale that
        Morley’s safety-valve statement was insufficient under § 3553(f)(5).
        Therefore, the only issue that we would have needed to consider
        is whether the district court erred in its § 3553(f)(5) determination.
        We only needed to reach that argument, however, if Morley was
        otherwise eligible for the safety valve reduction. But the Supreme
        Court’s recent decision in Pulsifer expressly abrogated our decision
        in Garcon and held that a defendant who has any of the three crim-
        inal-history components under § 3553(f)(1) is disqualified from
        safety valve sentencing relief. 144 S. Ct. at 737.
               It is undisputed in this appeal that Morley fails to satisfy §
        3553(f)(1)(B) because he has a prior three-point offense—conspir-
        acy to import 100 kilograms or more of marijuana. Therefore,
        Morley is ineligible for the safety valve reduction in light of Pulsifer.
        We thus affirm the district court’s denial of Morley’s request for a
        reduced sentence.
                                 IV.     CONCLUSION
                 For these reasons, we affirm Morley’s convictions and sen-
        tence.
                 AFFIRMED.

```

---

## GROUP: _overhaul2/lake/cases/United States v. Morton.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Morton"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Fifth Circuit"
court_level: coa
circuit: 5th
year: 2022
date_decided: 2022-08-23
docket: 19-10842
authority_weight: "Binding in-circuit — 5th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2022-08-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Morton
  varies_by_point: false
  scope_note: "En banc; resolved on the good-faith exception."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7859188/united-states-v-morton/"
  cluster_id: 7859188
  opinion_id: 7803054
  identity_checked: false
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Recent development (role-based)"
related: ["[[Riley v. California]]", "[[Carpenter v. United States]]", "[[United States v. Leon]]"]
aliases: ["United States v. Morton (5th Cir. 2022)", "United States v. Morton (en banc)"]
tags: ["case", "fourth-amendment", "plain-view", "digital-searches", "cell-phone", "good-faith-exception", "fifth-circuit"]
holding: "En banc 5th Circuit (resolving on good-faith grounds) discusses the digital general-warrant problem and flags, in concurrence, that the…"
lake:
  record_id: United States v. Morton
  status: under_review
  projected_at: 2026-07-09
---

# United States v. Morton

*46 F.4th 331 (5th Cir. 2022)* · U.S. Court of Appeals, Fifth Circuit (en banc) · **Binding in-circuit — 5th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating Morton, officers obtained warrants to search his cell phones in a drug case. While executing the warrants on the phones' photographs, they found images that appeared to be child pornography. Morton moved to suppress the images, arguing the affidavits did not establish probable cause to search his photographs. Sitting [[Reading and Citing Cases#en-banc|en banc]], the Fifth Circuit resolved the case on the [[The Good-Faith Exception|good-faith exception]] to the exclusionary rule.

## Issue
Whether the images recovered from Morton's phones must be suppressed, or whether the officers' good-faith reliance on the issuing judge's warrants brought the evidence within the [[The Good-Faith Exception|good-faith exception]].

## Rule
The [[Reading and Citing Cases#en-banc|en banc]] court resolved the case on good faith and expressly declined to reach the underlying Fourth Amendment question: "We do not decide if the state judge should have authorized full searches of the phones based on these affidavits. We decide only that the officers acted in good faith when relying on the judge's decision to issue the warrants." — *United States v. Morton*, 46 F.4th 331 (5th Cir. 2022) (en banc) (slip op., at 13). ^pin-op13

Judges concurring in the judgment wrote separately to flag the unresolved digital-search problem the majority left open — that the [[Plain View Doctrine|plain-view doctrine]] may need adaptation for data outside a warrant's scope: it "would be unsurprising if the Court, again acknowledging the need to adapt rules constructed for the physical world to the reality of the digital world, recognized an exception to another longstanding Fourth Amendment doctrine, this time plain view." — *Id.* (slip op., at [16](https://www.courtlistener.com/opinion/7859188/united-states-v-morton/#:~:text=would%20be%20unsurprising%20if%20the)) (opinion concurring in the judgment). ^pin-op16

## Application
The [[Reading and Citing Cases#en-banc|en banc]] court concluded that the warrant affidavits were borderline rather than bare bones, so the officers' reliance on the judge's warrants was objectively reasonable and the [[The Good-Faith Exception|good-faith exception]] applied. The court therefore affirmed admission of the images without deciding whether the warrants in fact established probable cause to search Morton's photographs. The separate opinion concurring in the judgment used the case to identify — but not resolve — whether the [[Plain View Doctrine|plain-view doctrine]] should be limited for nonresponsive digital data, the reason this decision is tracked on the plain-view page.

## Conclusion
Sitting [[Reading and Citing Cases#en-banc|en banc]], the Fifth Circuit held the [[The Good-Faith Exception|good-faith exception]] applied and affirmed the denial of suppression; it expressly declined to decide whether the warrants were overbroad as to the phones' photographs.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 5th Cir.** (en banc).
- No negative treatment. *Morton*'s holding rests on the [[The Good-Faith Exception|good-faith exception]] ([[United States v. Leon]]); its relevance to the [[Plain View Doctrine|plain-view doctrine]] lies in the separate opinion flagging the open digital-search question after [[Riley v. California]] and [[Carpenter v. United States]].

## Appears on
- [[Plain View Doctrine]] — *Recent development (role-based)*

## Sources
- *United States v. Morton*, 46 F.4th 331 (5th Cir. 2022) (en banc) — https://www.courtlistener.com/opinion/7859188/united-states-v-morton/ — pinpoints given as slip-opinion pages (CourtListener carries the slip opinion; cluster 7859188 → opinion 7803054).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "540ddeae83c244ee", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op13", "record_id": "United States v. Morton"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op13", "pinpoint_status": "slip-only", "quote": "--- # United States v. Morton *46 F.4th 331 (5th Cir. 2022)* · U.S. Court of Appeals, Fifth Circuit (en banc) · **Binding in-circuit — 5th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating Morton, officers obtained warrants to search his cell phones in a drug case. While executing the warrants on the phones' photographs, they found images that appeared to be child pornography. Morton moved to suppress the images, arguing the affidavits did not establish probable cause to search his photographs. Sitting en banc, the Fifth Circuit resolved the case on the good-faith exception to the exclusionary rule. ## Issue Whether the images recovered from Morton's phones must be suppressed, or whether the officers' good-faith reliance on the issuing judge's warrants brought the evidence within the good-faith exception. ## Rule The en banc court resolved the case on good faith and expressly declined to reach the underlying Fourth Amendment question:", "quote_fidelity": "mismatch", "record_id": "United States v. Morton", "star_marker": null}}
{"assertion_id": "ff5d39c2f5186445", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op16", "record_id": "United States v. Morton"}, "payload": {"fragment": "#:~:text=would%20be%20unsurprising%20if%20the", "page": null, "pin_id": "pin-op16", "pinpoint_status": "star-verified", "quote": "would be unsurprising if the Court, again acknowledging the need to adapt rules constructed for the physical world to the reality of the digital world, recognized an exception to another longstanding Fourth Amendment doctrine, this time plain view.", "quote_fidelity": "matched", "record_id": "United States v. Morton", "star_marker": "11"}}
{"assertion_id": "35221def06364d07", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Morton"}, "payload": {"as_of_content": "2022-08-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Morton", "scope_note": "En banc; resolved on the good-faith exception.", "varies_by_point": false}}
```

### lake record — United States v. Morton

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Morton",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Morton",
    "case_name_short": "Morton",
    "case_name_full": "",
    "input_case_name": "United States v. Morton",
    "court": "U.S. Court of Appeals, Fifth Circuit",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "5th",
    "state": null,
    "date_decided": "2022-08-23",
    "year": 2022,
    "docket": "19-10842",
    "cluster_id": 7859188,
    "lead_opinion_id": 7803054,
    "sibling_ids": [
      7803054
    ],
    "absolute_url": "/opinion/7859188/united-states-v-morton/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
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
    }
  },
  "pinpoints": [
    {
      "id": "pin-op13",
      "page": null,
      "quote": "--- # United States v. Morton *46 F.4th 331 (5th Cir. 2022)* \u00b7 U.S. Court of Appeals, Fifth Circuit (en banc) \u00b7 **Binding in-circuit \u2014 5th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating Morton, officers obtained warrants to search his cell phones in a drug case. While executing the warrants on the phones' photographs, they found images that appeared to be child pornography. Morton moved to suppress the images, arguing the affidavits did not establish probable cause to search his photographs. Sitting en banc, the Fifth Circuit resolved the case on the good-faith exception to the exclusionary rule. ## Issue Whether the images recovered from Morton's phones must be suppressed, or whether the officers' good-faith reliance on the issuing judge's warrants brought the evidence within the good-faith exception. ## Rule The en banc court resolved the case on good faith and expressly declined to reach the underlying Fourth Amendment question:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op16",
      "page": null,
      "quote": "would be unsurprising if the Court, again acknowledging the need to adapt rules constructed for the physical world to the reality of the digital world, recognized an exception to another longstanding Fourth Amendment doctrine, this time plain view.",
      "star_marker": "11",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 30555,
      "fragment": "#:~:text=would%20be%20unsurprising%20if%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2022-08-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Morton",
    "varies_by_point": false,
    "scope_note": "En banc; resolved on the good-faith exception.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7803054) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca5)",
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
        "query": "cites:(7803054)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(7803054)",
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
    "complete_query": "cites:(7803054)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7803054,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-morton.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 7803054,
        "cited_id": 6544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 8255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 46216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 47945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 50941,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 172511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 183984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 450602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 480195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 595515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 765254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 802237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 1189236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 2310827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 2673989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4251099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4649311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4693288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4699658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 6454865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 6534035,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 7263677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9417418,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9421690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9422845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9422971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9423434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9423895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9424493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9426173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9428782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9429232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9434104,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9469573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9498985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9499327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9876158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9889044,
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
    "date_created": "2026-07-06T01:52:16Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: no_official_class_citation",
      "legacy treatment migrated: good -> good_law",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T13:39:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Morton

```
Case: 19-10842        Document: 00516443952             Page: 1      Date Filed: 08/23/2022




               United States Court of Appeals
                    for the Fifth Circuit                                         United States Court of Appeals
                                                                                           Fifth Circuit

                                                                                         FILED
                                                                                   August 22, 2022
                                        No. 19-10842
                                                                                    Lyle W. Cayce
                                                                                         Clerk
   United States of America,

                                                                      Plaintiff—Appellee,

                                            versus

   Brian Matthew Morton,

                                                                  Defendant—Appellant.


                     Appeal from the United States District Court
                         for the Northern District of Texas
                               USDC No. 4:19-CR-17-1


   Before Richman, Chief Judge, and Jolly, Jones, Smith, Stewart,
   Dennis, Elrod, Southwick, Haynes, Graves, Higginson,
   Costa, Willett, Ho, Duncan, Engelhardt, Oldham and
   Wilson, Circuit Judges.*
   Gregg Costa, Circuit Judge, joined by Richman, Chief Judge, and
   Jones, Smith, Stewart, Southwick, Haynes, Ho, Duncan,
   Engelhardt, Oldham, and Wilson, Circuit Judges:
           State troopers arrested Brian Morton after finding drugs in his car
   during a traffic stop. Morton also had three cellphones in the car. A state


           *
             Judge Jolly chooses not to dissent or to join Judge Graves’s dissent. He chooses
   to stand by the initial panel opinion.
Case: 19-10842      Document: 00516443952           Page: 2   Date Filed: 08/23/2022




                                     No. 19-10842


   judge later signed warrants authorizing searches of the phones for evidence
   of drug crime. The warrants allowed law enforcement to look at photos on
   the phones. When doing so, troopers discovered photos that appeared to be
   child pornography. This discovery led to a second set of search warrants.
   The ensuing forensic examination of the phones revealed almost 20,000
   images of child pornography. This federal prosecution for receipt of child
   pornography followed.
          Even though search warrants authorized everything law enforcement
   did when searching the cell phones, Morton argues the evidence discovered
   during those searches should be suppressed. We disagree because law
   enforcement is usually entitled to rely on warrants, and none of the
   exceptions that undermine good-faith reliance on a judge’s authorization
   applies.
                                          I
          Shortly after midnight, state trooper Burt Blue pulled over Morton’s
   van on Interstate 20 about fifty miles west of Fort Worth. After approaching
   the driver’s side door, Blue smelled marijuana. Morton eventually admitted
   he had marijuana in the van. Blue then searched Morton and found an Advil
   bottle in his right pocket. The bottle contained several different colored pills
   that Morton admitted were ecstasy. Morton was arrested.
          Blue and another trooper searched the van. Inside a plastic container
   wrapped in tape they discovered two plastic bags, one of which contained a
   small amount of marijuana. They also found a glass pipe with marijuana. In
   addition to the drug evidence, the troopers discovered approximately 100
   pairs of women’s underwear, a number of sex toys, and lubricant. A backpack
   with children’s school supplies was also inside the van. A lollipop was inside
   a cupholder. Based on what they found in the van, the troopers were
   concerned Morton was a sexual predator.




                                          2
Case: 19-10842      Document: 00516443952           Page: 3   Date Filed: 08/23/2022




                                     No. 19-10842


          The troopers also seized three cellphones during the search of the van.
   A few days after Morton’s arrest, Blue applied for search warrants for the
   three phones. The search warrants sought evidence of drug possession and
   dealing.
          In the affidavits he submitted in support of the warrants, Blue
   recounted the traffic stop and the drug evidence discovered in the van and on
   Morton. He also explained why, based on his experience, he believed it likely
   that the cellphones contained evidence of illegal drug activity. People often
   communicate via cellphone to arrange drug transactions. And “criminals
   often take photographs of co-conspirators as well as illicit drugs and currency
   derived from the sale of illicit drugs.”
          A state district judge concluded that probable cause existed for the
   searches and signed the three warrants. Each warrant allowed troopers to
   search for various items on the phones including “photographs, digital
   images, or multimedia files in furtherance of narcotics trafficking or
   possession.”
          While searching the phones, Blue and a Department of Public Safety
   agent saw images they believed were child pornography. They stopped
   searching and sought new warrants seeking evidence of child pornography.
   The same state district judge issued the new warrants. The forensic search
   of the phones that followed located 19,270 images of child pornography on
   the three phones.
          A federal grand jury charged Morton with receipt of child
   pornography. Morton moved to suppress the pornographic images found on
   the phones. He argued that probable cause did not support the initial
   warrants allowing the phone searches. The good-faith doctrine did not apply,
   he continued, because the affidavits were too “general in nature” to tie the
   phones to drug activity. He also briefly contended that the search of the




                                          3
Case: 19-10842     Document: 00516443952            Page: 4    Date Filed: 08/23/2022




                                     No. 19-10842


   phone for drug evidence was pretextual because the troopers were really
   concerned that Morton might have committed sex crimes.
          The district court refused to suppress the evidence. It concluded that
   the good-faith exception to the suppression rule applied.
          After losing his suppression motion, Morton entered a conditional
   guilty plea that allowed him to challenge the searches on appeal.
          Morton’s appeal initially succeeded. A panel of our court concluded
   that, although the “affidavits successfully establish probable cause to search
   Morton’s contacts, call logs, and text messages for evidence of drug
   possession,” United States v. Morton, 984 F.3d 421, 427 (5th Cir. 2021), they
   do not establish probable cause “that the photographs on Morton’s phones
   would contain evidence pertinent to [that] crime,” id. at 428. The panel also
   held that the good-faith exception did not apply because reasonable officers
   should “have been aware that searching the digital images on Morton’s
   phone—allegedly for drug-trafficking-related evidence—was unsupported
   by probable cause.” Id. at 430.
          Our full court vacated that decision and agreed to hear this case en
   banc. See United States v. Morton, 996 F.3d 754 (5th Cir. 2021).
                                          II
          Riley v. California, one of the recent Supreme Court cases applying the
   Fourth Amendment to modern technology, held that the search of a
   cellphone incident to arrest requires a warrant. 574 U.S. 373 (2014). Morton
   and supporting amici view this case as a follow-on that allows us to flesh out
   when probable cause exists to believe that certain applications on a cellphone
   contain incriminating evidence. They argue that Riley’s warrant requirement
   will be a mere formality if officers can search an entire phone based on




                                          4
Case: 19-10842        Document: 00516443952              Page: 5      Date Filed: 08/23/2022




                                         No. 19-10842


   nothing more than the fact that criminals sometimes use phones to conduct
   their illicit activity.
           Despite the invitation to treat this as another difficult case addressing
   how “the degree of privacy secured to citizens by the Fourth Amendment”
   is affected “by the advance of modern technology,” Kyllo v. United States,
   533 U.S. 27, 33–34 (2001), a longstanding rule resolves the case: Evidence
   should not be suppressed when law enforcement obtained it in good-faith
   reliance on a warrant. See United States v. Leon, 468 U.S. 897 (1984).1
           The good-faith rule flows from two central features of modern Fourth
   Amendment jurisprudence: the warrant requirement and the suppression
   remedy. The Supreme Court has held that a warrant is generally required for
   certain searches, most notably searches of the home and most recently
   searches of cellphones incident to arrest. See Riley, 574 U.S. at 403; Brigham
   City v. Stuart, 547 U.S. 398, 403 (2006) (noting that “searches and seizures
   inside a home without a warrant are presumptively unreasonable” (internal
   quotation omitted)). Behind the warrant requirement is the idea that the
   “inferences which reasonable men draw from evidence” to decide if probable
   cause exists should “be drawn by a neutral and detached magistrate instead
   of being judged by the officer engaged in the often competitive enterprise of
   ferreting out crime.” Johnson v. United States, 333 U.S. 10, 14 (1948)
   (Jackson, J.). Although obtaining a warrant from that neutral judge may



           1
             We recognize that it will “stunt the development of Fourth Amendment law” if
   courts too often avoid the underlying constitutional question and deny suppression motions
   based on the good-faith rule. See Davis v. United States, 564 U.S. 229, 245–46 (2011)
   (summarizing this argument the defendant advanced); cf. Pearson v. Callahan, 555 U.S. 223
   236 (2009) (giving courts discretion to rule only on the “clearly established” inquiry for
   qualified immunity but recognizing that deciding the underlying constitutional question is
   “often beneficial”). In this instance, however, we conclude that the good-faith rule offers
   the most appropriate resolution by the full court.




                                               5
Case: 19-10842      Document: 00516443952           Page: 6    Date Filed: 08/23/2022




                                     No. 19-10842


   burden law enforcement before it conducts the search, the police obtain a
   benefit after the search. When a court reviews an after-the-fact challenge to
   the search, “the resolution of doubtful or marginal cases . . . should be largely
   determined by the preference to be accorded to warrants.” United States v.
   Ventresca, 380 U.S. 102, 109 (1965). As a result, “[s]earches pursuant to a
   warrant will rarely require any deep inquiry into reasonableness.” Leon, 468
   U.S. at 922 (quoting Illinois v. Gates, 462 U.S. 213, 267 (1983) (White, J.,
   concurring in judgment)).
          To this unwillingness to second guess the magistrate who authorized
   the warrant, the exclusionary rule adds another component. As a judicially-
   created remedy rather than a constitutional requirement, the exclusionary
   rule is justified by the deterrent effect of suppressing evidence when it was
   obtained unlawfully. Id. at 906. A key consideration in deciding when
   suppression will deter is whether “law enforcement officers have acted in
   objective good faith.” Id. at 908. The need to punish police conduct and
   thus deter future violations via suppression “assumes that the police have
   engaged in willful, or at the very least negligent, conduct.” Id. at 919 (quoting
   United States v. Peltier, 422 U.S. 531, 539 (1975)). The exclusionary rule is
   not aimed at “punish[ing] the errors of judges and magistrates” who issue
   warrants. Id. at 916.
          Deference to the judge issuing the warrant and the exclusionary rule’s
   focus on deterring police misconduct results in the good-faith exception to
   the suppression remedy: A “‘warrant issued by a magistrate normally
   suffices to establish’ that a law enforcement officer has ‘acted in good faith
   in conducting a search.’” Id. at 922 (quoting United States v. Ross, 456 U.S.
   798, 832 n.32 (1982)).
          Normally, but not always.        The Supreme Court identified four
   situations when “a reasonably well trained officer would have known that the




                                          6
Case: 19-10842         Document: 00516443952               Page: 7      Date Filed: 08/23/2022




                                          No. 19-10842


   search was illegal despite the magistrate’s authorization.” Id. at 922 n.23.
   Reliance on a warrant is unreasonable when: 1) the magistrate issued it based
   on information the affiant knew was false or should have known was false but
   for reckless disregard of the truth; 2) the magistrate wholly abandoned the
   judicial role; 3) the warrant is based on an affidavit so lacking in probable
   cause as to render belief in its existence unreasonable; and 4) the warrant is
   facially deficient in particularizing the place to be searched or things to be
   seized. Id. at 923; see also United States v. Triplett, 684 F.3d 500, 504 (5th Cir.
   2012).
                                                III
            Morton principally tries to defeat good faith by invoking the third
   exception, which involves what are commonly known as “bare bones”
   affidavits.2 “‘Bare bones’ affidavits contain wholly conclusory statements,
   which lack the facts and circumstances from which a magistrate can
   independently determine probable cause.” United States v. Satterwhite, 980
   F.2d 317, 321 (5th Cir. 1992).




            2
             Morton also invokes the first exception that applies when law enforcement
   misleads the magistrate with false information in the affidavit. We succinctly address this
   argument because the full court is unanimous in rejecting it and Morton may not have
   adequately raised it in district court.
           The alleged falsehood is keeping from the magistrate that the affiant’s motive was
   not obtaining evidence of drug crime but investigating suspicions that Morton was a sexual
   predator. In other words, Morton is arguing that the reason for obtaining the warrant was
   pretextual. Even if Morton could prove this motive, it would not matter. The Supreme
   Court has repeatedly held that the Fourth Amendment inquiry, including the existence of
   probable cause, is objective. See, e.g., Brigham City, 547 U.S. at 404–05 (2006); Whren v.
   United States, 517 U.S. 806, 813 (1996); see also United States v. McKinnon, 681 F.3d 203,
   210 (5th Cir. 2012) (explaining that the officer’s motive in searching a vehicle did not
   matter). It is telling that Morton’s primary authority on this issue is a vacated opinion. See
   United States v. Pope, 452 F.3d 338, vacated by 467 F.3d 912 (5th Cir. 2006).




                                                 7
Case: 19-10842      Document: 00516443952            Page: 8   Date Filed: 08/23/2022




                                     No. 19-10842


          A look at some bare-bones affidavits from Supreme Court cases shows
   just how bare they are. One affidavit, from the Prohibition Era, said nothing
   more than that the agent “has cause to suspect and does believe that certain
   merchandise . . . has otherwise been brought into the United States contrary
   to law, and that said merchandise is now deposited and contained within”
   the defendant’s home. Nathanson v. United States, 290 U.S. 41, 44 (1933).
   Another affidavit, this one supporting an arrest warrant, said only that, on a
   certain day, the defendant “did receive, conceal, etc., narcotic drugs, to-wit:
   heroin hydrochloride with knowledge of unlawful importation” and that the
   affiant “believes” certain people “are material witnesses in relation to this
   charge.” Giordenello v. United States, 357 U.S. 480, 481 (1958). Similarly,
   the allegations supporting an arrest warrant were bare bones when the only
   information was that “defendants did then and there unlawfully break and
   enter a locked and sealed building.” Whiteley v. Warden, 401 U.S. 560, 563
   (1971). Lastly, Houston police officers obtained a search warrant based only
   on their statement that they “received reliable information from a credible
   person and do believe that [drugs] are being kept at the above described
   premises for the purpose of sale and use contrary to the provisions of the
   law.” Aguilar v. Texas, 378 U.S. 108, 109 (1964). These affidavits do not
   detail any facts, they allege only conclusions.
          Also consider affidavits we have found to be bare-boned. In what we
   described as a “textbook example of a facially invalid, ‘barebones’ affidavit,”
   the officer listed just the defendant’s “biographical and contact information”
   and then stated “nothing more than the charged offense, accompanied by a
   conclusory statement” that the defendant committed that crime. Spencer v.
   Staton, 489 F.3d 658, 661–62 (5th Cir. 2007), withdrawn in part on reh’g (July
   26, 2007). In another case, an officer obtained a warrant to search a motel
   room based on an affidavit stating nothing more than that the officer
   “received information from a confidential informant” who was known to him




                                          8
Case: 19-10842      Document: 00516443952           Page: 9    Date Filed: 08/23/2022




                                     No. 19-10842


   and who had “provided information in the past that ha[d] led to arrest and
   convictions.” United States v. Barrington, 806 F.2d 529, 531 (5th Cir. 1986).
   As these cases illustrate, bare-bones affidavits contain “wholly conclusory”
   statements such as “the affiant ‘has cause to suspect and does believe’ or
   ‘[has] received reliable information from a credible person and [does]
   believe.’” United States v. Pope, 467 F.3d 912, 920 (5th Cir. 2006) (internal
   quotations omitted).
          The affidavits used to search Morton’s phones are not of this genre;
   they have some meat on the bones. Each is over three pages and fully details
   the facts surrounding Morton’s arrest and the discovery of drugs and his
   phones. They explain where the marijuana and glass pipe were discovered,
   the number (16) and location of the ecstasy pills, and the affiant’s knowledge
   that cellphones are used for receipt and delivery of illegal narcotics. In
   support of the request to search for photos on the phones, the affiant explains
   he “knows through training and experience that criminals often take
   photographs of co-conspirators as well as illicit drugs and currency derived
   the sale of illicit drugs.” Whatever one might conclude in hindsight about
   the strength of the evidence it recounts, the affidavit is not “wholly
   conclusory.” Satterwhite, 980 F.2d at 321.
          The affidavits, then, put all the relevant “facts and circumstances”
   before the state judge, allowing him to “independently determine” if the
   notoriously fuzzy probable-cause standard had been met. See id.; see also
   Gates, 462 U.S. at 232 (“[P]robable cause is a fluid concept—turning on the
   assessment of probabilities in particular factual contexts—not readily, or
   even usefully, reduced to a neat set of legal rules.”). In other words, the judge
   made a judgment call. Judgment calls in close cases are precisely when the
   good-faith rule prevents suppression based on after-the-fact reassessment of
   a probable-cause determination. Leon, 468 U.S. at 914 (“Reasonable minds
   frequently may differ on the question whether a particular affidavit



                                          9
Case: 19-10842        Document: 00516443952              Page: 10       Date Filed: 08/23/2022




                                          No. 19-10842


   establishes probable cause, and we have thus concluded that the preference
   for warrants is most appropriately effectuated by according ‘great deference’
   to a magistrate’s determination.” (quoting Spinelli v. United States, 393 U.S.
   410, 419 (1969))).
           Although he invokes the bare-bones exception, Morton does not
   confront the caselaw showing it applies to affidavits that are wholly
   conclusory. He instead mostly challenges the probable-cause determination
   assessment itself, contending that the facts “merely establish[ed] probable
   cause for a user-quantity drug possession arrest and not probable cause to
   search the entire communication and photographic contents of [his]
   phones.” Drug possessors, he points out, are less likely to use phones for
   drug activity than are dealers. He contends it would gut Riley if the linking of
   criminal activity to cellphones can be based on nothing more than an officer’s
   experience that certain offenders often use cellphones in connection with
   their crimes. But this is not such a case. Morton had multiple phones in his
   car along with the drugs, which our court and others have recognized can
   indicate that the phones are being used for criminal activity.3 See United
   States v. Bams, 858 F.3d 937, 945 (5th Cir. 2017); United States v. Lindsay, 3
   F.4th 32, 40 (1st Cir. 2021); United States v. Peterson, 2019 WL 1793138, at
   *11–12 (E.D. Va. Apr. 24, 2019); see also United States v. Eggerson, 999 F.3d
   1121, 1127 (8th Cir. 2021) (“It would be unreasonable and impractical to
   demand that judges evaluating probable cause must turn a blind eye to the
   virtual certainty that drug dealers use cell phones.”).




           3
            The concurring opinion points out that the affidavits did not identify the existence
   of three phones as a reason why the troopers suspected Morton of dealing drugs. But
   together the affidavits placed the fact of Morton’s multiple phones before the state judge,
   who is charged with making an objective evaluation of probable cause.




                                                10
Case: 19-10842        Document: 00516443952           Page: 11    Date Filed: 08/23/2022




                                       No. 19-10842


          It is a close call whether the evidence recounted in the affidavits
   established probable cause for drug trafficking as opposed to drug possession.
   And if the evidence indicated only possession, then it is another close call
   whether there was probable cause to believe that evidence of drug possession
   would be found on the phones. But as we have emphasized, on close calls
   second guessing the issuing judge is not a basis for excluding evidence.
          Viewed in their entirety, the affidavits supporting the warrants are far
   from bare bones. It thus was reasonable to rely on the warrants and search
   the phones.
          For most of this case, Morton’s argument was the one we have just
   addressed: that searching any part of his phones was unjustified because the
   affidavits establish probable cause only for drug possession and not the
   trafficking that is more logically tied to phones. But even the panel originally
   hearing this appeal did not accept that argument despite holding that the
   photos should have been suppressed. The panel recognized probable cause
   existed to “search Morton’s contacts, call logs, and text messages” on his
   phone, just not the photos. 984 F.3d at 427–28; id. at 431 (concluding that
   “the magistrate did not have a substantial basis for determining that probable
   cause existed to extend the search to the photographs on the cellphones”).
   Morton now runs with this theory that good-faith should be “analyzed
   separately” for each area to be searched. Because he did not make this claim
   in the district court or in his original appellate brief, it is forfeited, and we are
   not deciding it.
          Even if we could consider Morton’s new argument advocating a
   piecemeal analysis, it would not change our holding that the good-faith rule
   applies. At least one other court has taken the approach of the original panel
   in this case and analyzed whether an affidavit is bare bones for particular
   items to be searched. See Burns v. United States, 235 A.3d 758, 774 (D.C.




                                            11
Case: 19-10842     Document: 00516443952            Page: 12   Date Filed: 08/23/2022




                                     No. 19-10842


   2020) (“The affidavits were thus classic ‘bare bones’ statements as to
   everything on Mr. Burns’s phones for which Detective Littlejohn made a
   claim of probable cause beyond three narrow categories of data for which the
   affidavits made proper factual showings.”). Our precedent takes a different
   approach. When a defendant moved to suppress evidence obtained under a
   warrant that authorized the seizure of “twenty-six categories of evidence,
   primarily written and electronic documents,” our good-faith inquiry did not
   parse probable cause for each category. See United States v. Cherna, 184 F.3d
   403, 406 (5th Cir. 1999). We instead focused on whether the affidavit as a
   whole was bare bones, while “keep[ing] in mind that it is more difficult to
   demonstrate probable cause for an ‘all records’ search of a residence than for
   other searches.” Id. at 409. That is, the scope of a warrant may influence
   whether it is bare bones. An affidavit that is not bare bones for a limited
   search could be bare when supporting a broader search. Keeping the focus
   on the entirety of the affidavit as Cherna does is the traditional bare-bones
   inquiry, see, e.g, Leon, 468 U.S. at 926 (referring to a “‘bare bones’ affidavit”
   not parts of an affidavit), and consistent with the ultimate question whether
   an officer would know the affidavit is “so lacking in probable cause as to
   render belief in its existence unreasonable” despite a judge’s finding that
   probable cause existed, id. at 923.
          Viewing the entire affidavit against the broad phone search it
   authorized, it is borderline rather than bare bones. And even if our caselaw
   allowed a photographs-only inquiry and Morton preserved that argument, we
   would still not characterize the evidence supporting that request as “wholly
   conclusory.” Cf. United States v. Burgess, 576 F.3d 1078 (10th Cir. 2009)
   (recognizing that it was reasonable to search a computer for “trophy photos”
   of drug activity based on not much more evidence than exists here).
          The officers relied in good faith on the warrants the state judge issued.
   On finding images that appeared to be child pornography, they went back to



                                          12
Case: 19-10842       Document: 00516443952              Page: 13      Date Filed: 08/23/2022




                                         No. 19-10842


   the judge for additional warrants (Morton does not challenge how the
   searches were conducted).           We see no unreasonable law enforcement
   conduct that warrants suppression of the evidence the searches discovered.
                                             ***
           We do not decide if the state judge should have authorized full
   searches of the phones based on these affidavits. We decide only that the
   officers acted in good faith when relying on the judge’s decision to issue the
   warrants. This ruling hardly nullifies Riley as Morton, amici, and the dissent
   suggest. Before Riley, police could have searched Morton’s phones on the
   spot after arresting him. See United States v. Finley, 477 F.3d 250, 259–60
   (5th Cir. 2007), overruled by Riley, 573 U.S. at 373. Because of Riley, the
   officers had to obtain warrants. For better or worse, the warrant requirement
   and good-faith rule make the judge presented with the warrant application
   the central guardian of Fourth Amendment rights.4 That has long been true
   when officers seek to search a home; Riley makes it true for searches of
   cellphones incident to arrest.
           The judgment is AFFIRMED.




           4
            The role of the judge who must authorize a warrant is absent from the dissent’s
   recounting of how officers might be able to search cellphones after “find[ing] evidence of
   small quantities of illicit drugs for personal use during an automobile stop.” Dissenting
   Op. 4–5.




                                              13
Case: 19-10842        Document: 00516443952         Page: 14    Date Filed: 08/23/2022




                                     No. 19-10842


   Stephen A. Higginson, Circuit Judge, with whom Elrod and
   Willett, Circuit Judges, join, and with whom Ho and Wilson, Circuit
   Judges, join as to Part II, concurring in the judgment:
          I agree with the majority that the affidavit supporting the warrants in
   this case was “borderline rather than bare bones,” and, therefore, that the
   good faith exception applies. United States v. Satterwhite, 980 F.2d 317, 321
   (5th Cir. 1992).
                                           I.
          Because we can decide this case on the good faith exception, the
   majority opinion appropriately declines to address whether there was
   probable cause to search Morton’s cell phone. I write separately to address
   the majority’s response to Morton’s argument that a finding of probable
   cause here would conflict with the reasoning, though not necessarily the
   holding, of Riley v. California, 573 U.S. 373 (2014), in which the Supreme
   Court held that police officers must obtain a warrant before searching the
   contents of an arrestee’s cell phone, rather than conducting a search of the
   cell phone incident to arrest.
          The only facts in the affidavit to support probable cause for a search
   of Morton’s cell phone were that: (1) he possessed a user-quantity of drugs,
   (2) he simultaneously possessed a cell phone, and (3) the officer “kn[ew]
   through training and experience” that individuals, including those
   possessing illicit drugs, use their cell phones to communicate. If these three
   facts are sufficient to support probable cause for the search here, then any
   time an officer finds drugs (or other contraband for that matter) on a person
   or in a vehicle, there is probable cause to search the entire contents of a nearby
   cell phone.
          Of course, Riley requires that officers first get a warrant, 573 U.S. at
   403, but if the fact that the arrestee was carrying a cell phone at the time of




                                          14
Case: 19-10842        Document: 00516443952              Page: 15       Date Filed: 08/23/2022




                                          No. 19-10842


   arrest is sufficient to support probable cause for a search, then the warrant
   requirement is merely a paperwork requirement. It cannot be that Riley’s
   holding is so hollow.1
                                               II.
           The heightened privacy interest that Riley recognized an arrestee has
   in the contents of their cell phone stems in part from the quantitative and
   qualitative differences between the data stored on a cell phone and any
   “other objects that might be kept on an arrestee’s person.” Id. at 393. Cell
   phones contain an enormous amount of personal information dating back
   months or years, including data that has no physical equivalent, like browser
   history or geolocation information. Id. at 394-96. Therein lies the problem
   with a cell phone search premised solely on the simultaneous possession of
   drugs and a phone. It is not merely the lack of probable cause that evidence
   of drug possession or trafficking would be found on the phone, but also that
   with such a meager showing, officers would gain unfettered access to all of
   “the privacies of life.” Id. at 403 (quoting Boyd v. United States, 116 U.S. 616,
   630 (1886)).
           The original panel opinion in this case presented one potential
   solution to this problem by requiring probable cause for each category of data
   to be searched. United States v. Morton, 984 F.3d 421, 425-26 (5th Cir. 2021).
   This approach runs into practical problems, including the fact that



           1
             The majority’s response to the contention that “it would gut Riley if the linking
   of criminal activity to cellphones can be based on nothing more than an officer’s experience
   that certain offenders often use cellphones in connection with their crimes” is that, here,
   there was something more—namely, the presence of multiple cellphones. It is true that we
   have recognized that the presence of multiple phones in a car—when combined with other
   strong evidence—can support a conviction for drug trafficking, United States v. Bams, 858
   F.3d 937, 945 (5th Cir. 2017). But the affidavits here did not mention that multiple phones
   were found in the car, let alone rely on that fact to support probable cause.




                                               15
Case: 19-10842     Document: 00516443952            Page: 16    Date Filed: 08/23/2022




                                     No. 19-10842


   “criminals can—and often do—hide, mislabel, or manipulate files to conceal
   criminal activity.” United States v. Stabile, 633 F.3d 219, 237 (3d Cir. 2011).
          Another approach, proposed by a leading Fourth Amendment
   scholar, would impose “use restrictions” on data that is outside the scope of
   the warrant, possibly by limiting application of the plain view doctrine in the
   context of digital searches. See Orin S. Kerr, Executing Warrants for Digital
   Evidence: The Case for Use Restrictions on Nonresponsive Data, 48 Tex. Tech
   L. Rev. 1, 9, 19-20 (2015). At least one state supreme court has adopted a
   use restriction approach, see State v. Mansor, 421 P.3d 323, 344 (Or. 2018),
   and another has suggested that it might do so in the future, Preventative Med.
   Assocs. v. Commonwealth, 992 N.E.2d 257, 274 (Mass. 2013). After Riley and
   Carpenter v. United States, 138 S. Ct. 2206, 2220 (2018), in which the
   Supreme Court held that the third-party doctrine does not apply to cell-site
   location information, it would be unsurprising if the Court, again
   acknowledging the need to adapt rules constructed for the physical world to
   the reality of the digital world, recognized an exception to another
   longstanding Fourth Amendment doctrine, this time plain view. See Kerr,
   supra, at 20; see generally Kyllo v. United States, 533 U.S. 27, 33-34 (2001).
          And there may be still other solutions that have yet to be identified.
   State courts face these dilemmas much more often than we do, and their
   continued innovation in this area—along with the valuable insights of Fourth
   Amendment scholars and those with the necessary technological expertise—
   will undoubtedly aid the lower federal courts and the Supreme Court in
   reaching a solution that protects privacy and the Framers’ conception of
   reasonableness. To my eye, that conception is unlikely to approve plain view
   full access to, and use of, what the Supreme Court has observed is more
   private information than would be contained in an entire home, where plain
   view access has obvious and significant limits. Riley, 573 U.S. at 396-97.




                                          16
Case: 19-10842     Document: 00516443952           Page: 17    Date Filed: 08/23/2022




                                    No. 19-10842


   James E. Graves, Jr., Circuit Judge, joined by Dennis, Circuit Judge,
   dissenting:
          Despite cautionary case law from this court that we “should resist the
   temptation to frequently rest [our] Fourth Amendment decisions on the safe
   haven of the good-faith exception, lest [we] fail to give law enforcement and
   the public the guidance needed to regulate their frequent interactions,” the
   majority avoids dealing with the “close call” question of probable cause.
   United States v. Molina-Isidoro, 884 F.3d 287, 293 (5th Cir. 2018) (Costa, J.,
   specially concurring). We should not fall into this “inflexible practice” that
   the Supreme Court warned against in Leon “of always deciding whether the
   officers’ conduct manifested objective good faith before turning to the
   question whether the Fourth Amendment has been violated.” United States
   v. Leon, 468 U.S. 897, 923 (1984). In failing to analyze this case for probable
   cause, the majority condones the government’s extensive and intrusive
   search of cell phones and its failure to provide any explanation of how those
   particular phones relate to the charged crime. In essence, it insulates officers
   from having to connect the dots between their general knowledge and
   experience—as detailed in a probable cause affidavit—and the basis for that
   specific search warrant. See United States v. Pope, 467 F.3d 912, 920 (5th Cir.
   2006) (disavowing affidavits based on an officer’s general suspicions or
   beliefs as “bare bones”). I dissent.
          First, this case must be viewed against the proper backdrop. Searching
   a cellphone is much more invasive than a self-contained search of a pocket,
   compartment, or bag. As Learned Hand noted, it is “a totally different thing
   to search a man’s pockets and use against him what they contain, from
   ransacking his house for everything which may incriminate him.” Riley v.
   California, 573 U.S. 373, 396 (2014) (citation omitted). “A phone not only
   contains in digital form many sensitive records previously found in the home;
   it also contains a broad array of private information never found in a home in



                                          17
Case: 19-10842     Document: 00516443952            Page: 18   Date Filed: 08/23/2022




                                     No. 19-10842


   any form—unless the phone is.” Id. at 396-97. Here, law enforcement
   conducted a traffic stop that produced evidence of a marginal offense. Then,
   they used this evidence as an excuse to gain unfettered access to a device
   saturated with personal, private information.
          Probable cause exists when “there is a fair probability that contraband
   or evidence of a crime will be found in a particular place.” Illinois v. Gates,
   462 U.S. 213, 238 (1983). We require a “nexus between the [place] to be
   searched and the evidence sought.” United States v. Freeman, 685 F.2d 942,
   949 (5th Cir. 1982) (collecting cases). Here, Morton was charged with simple
   possession based on 16 ecstasy pills, a small bag of marijuana, and a glass pipe.
   Trooper Blue’s affidavit stated that he believed Morton’s phones contained
   evidence of possession of ecstasy and marijuana “and other criminal
   activity.” Notably, Trooper Blue’s affidavit indicates that he already had
   firsthand evidence of Morton’s possession offense. One, he found the drugs
   on Morton. And two, Morton “admitted to . . . the possession of marijuana
   and [e]cstasy.” Morton did not have a large quantity of drugs, a large sum of
   cash, or anything else that would have indicated he was anything more than
   an admitted drug possessor, not a drug dealer.
          However, in an attempt to gain access to Morton’s phones, Trooper
   Blue made sweeping generalizations about “other criminal activity” and cell
   phone use, yet not once did he mention why such evidence could or would
   be on Morton’s phone. Nor did he connect his suspicions to Morton’s simple
   possession offense. Not even in passing. He instead hinged his affidavit on
   general conclusions about cellphones and criminals. As the Supreme Court
   has noted, “[i]t would be a particularly inexperienced or unimaginative law
   enforcement officer who could not come up with several reasons to suppose
   evidence of just about any crime could be found on a cell phone.” Riley, 573
   U.S. at 399. However, such speculation cannot be used to allow “police
   officers unbridled discretion to rummage at will among a person’s private



                                          18
Case: 19-10842     Document: 00516443952            Page: 19   Date Filed: 08/23/2022




                                     No. 19-10842


   effects.” Id. (citation omitted). Trooper Blue’s generalizations lack a nexus
   to the crime of simple possession, and there was no probable cause for the
   warrant to issue.
          For this same reason, the good faith exception does not apply. This
   court has repeatedly held that a nexus is necessary to claim the protection of
   the good faith exception. See, e.g., United States v. Garcia, 27 F.3d 1009, 1014
   (5th Cir. 1994) (noting in the discussion on the officer’s good faith reliance
   that “[t]he affidavit must tend to show some nexus between the [area] to be
   searched and the evidence sought.”); United States v. Brown, 567 F. App’x
   272, 284 (5th Cir. 2014) (unpublished) (including the lack of nexus “between
   [defendant’s] trafficking activities and his residence” among the deficiencies
   in the warrant’s supporting affidavit); United States v. Triplett, 684 F.3d 500,
   506–07 (5th Cir. 2012); United States v. Fields, 72 F.3d 1200, 1214 (5th Cir.
   1996); United States v. Gant, 759 F.2d 484, 488 (5th Cir. 1985); cf. Warden,
   Md. Penitentiary v. Hayden, 387 U.S. 294, 307 (1967) (indicating in the
   context of a seizure of “mere evidence” that “[t]here must, of course, be a
   nexus . . . between the item to be seized and criminal behavior.”).
          Where the affiant claims—without explaining why—he “has cause to
   suspect and does believe” or—without explaining how—he “[has] received
   reliable information from a credible person and [does] believe” that the
   search will result in the discovery of illegal activity, we deem such affidavits
   “bare bones.” Pope, 467 F.3d at 920 (internal quotations omitted). And the
   root issue with “bare bones” affidavits is that they do not explain how or why
   the affiant’s attested knowledge and the specific facts connect.
          Under Leon, the Supreme Court noted that the critical inquiry in this
   analysis is whether the affidavit “provide[s] evidence sufficient to”—at a
   minimum—“create disagreement among thoughtful and competent judges
   as to the existence of probable cause.” 468 U.S. at 926; see also U.S. v. Bosyk,




                                          19
Case: 19-10842      Document: 00516443952            Page: 20    Date Filed: 08/23/2022




                                      No. 19-10842


   933 F.3d 319, 333 (4th Cir. 2019); U.S. v. Davis, 530 F.3d 1069, 1083 n.3 (9th
   Cir. 2008); U.S. v. Luong, 470 F.3d 898, 903 (9th Cir. 2006). Cramming facts
   into a supporting affidavit does not make reliance on the resulting warrant
   more objectively reasonable unless those facts are probative as to probable
   cause. But the majority departs from this approach and exalts quantity over
   quality. For instance, the majority lauds the fact that the supporting affidavit
   in this case was “over three pages” long; specified the locations where the
   marijuana, ecstasy, and glass pipe were found; and stated the quantity of
   ecstasy pills recovered (namely, sixteen). Ante, at 9. But the search of
   Defendant’s phone was justified only on the basis that people who sell drugs,
   and other “criminals,” might have inculpatory photographs on their phones.
   And none of these facts indicate that Morton sold drugs or otherwise
   possessed them for anything other than personal use.
          In short, Trooper Blue makes sweeping generalizations about criminal
   activity and cell phone use, yet not once does he mention why such evidence
   could or would be on Morton’s phone or how it relates to simple possession.
   No reasonable officer could have perceived the facts alleged in the supporting
   affidavit to be “indicia of probable cause” to support a search of Defendant’s
   phone. Leon, 468 U.S. at 923.
          Lastly, I fear that the incentive for law enforcement to imitate Trooper
   Blue’s conduct in this case will be both strong and widespread. It is routine
   for officers to find evidence of small quantities of illicit drugs for personal use
   during an automobile stop. If the officer then wishes to gain access to such
   person’s phone—and, with it, “[t]he sum of [his or her] private life,” Riley,
   573 U.S. at 394—the majority’s approach imposes virtually no costs against
   doing so. All the officer needs to do is state what drugs they found, where
   they found it, and provide boilerplate language about how “cellphones are
   used for receipt and delivery of illegal narcotics.” Ante, at 9. The officer can




                                           20
Case: 19-10842     Document: 00516443952           Page: 21   Date Filed: 08/23/2022




                                    No. 19-10842


   then take refuge in the majority’s holding that he is protected by the good
   faith exception. This is unjust, unfair, and unconstitutional.
          I respectfully dissent.




                                         21

```

---

## GROUP: _overhaul2/lake/cases/United States v. Neugin.json  (`lake-record`, 5 assertions)

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
{"assertion_id": "e03503dce5417d03", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Neugin"}, "payload": {"all": [{"cite": "958 F.3d 924", "page": "924", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "958"}], "display": "958 F.3d 924", "official": {"cite": "958 F.3d 924", "page": "924", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "958"}, "official_selection_present": true, "record_id": "United States v. Neugin"}}
{"assertion_id": "36046261a528e45f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op15a", "record_id": "United States v. Neugin"}, "payload": {"fragment": "#:~:text=Without%20the%20violation%2C%20therefore%2C%20Mr.", "page": null, "pin_id": "pin-op15a", "pinpoint_status": "slip-only", "quote": "Without the violation, therefore, Mr. Neugin would not inevitably have been arrested. And without the arrest, the truck would not inevitably have been impounded and searched.", "quote_fidelity": "matched", "record_id": "United States v. Neugin", "star_marker": null}}
{"assertion_id": "8f1e9090fe42bf2e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op17", "record_id": "United States v. Neugin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op17", "pinpoint_status": "slip-only", "quote": "the police would not have inevitably discovered the evidence absent the Fourth Amendment violation . . . that evidence is fruit of the poisonous tree and should have been suppressed.", "quote_fidelity": "mismatch", "record_id": "United States v. Neugin", "star_marker": null}}
{"assertion_id": "c5eb508c160b2a86", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op15", "record_id": "United States v. Neugin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op15", "pinpoint_status": "slip-only", "quote": "--- # United States v. Neugin *958 F.3d 924 (10th Cir. 2020)* · U.S. Court of Appeals, Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a domestic-dispute stop, officers let Neugin's wife retrieve her belongings from a truck. Deputy Clinton opened the camper shell on the back of the truck and looked inside without consent, saw a bucket of ammunition, and arrested Neugin, a felon. The truck was later impounded and a shotgun was found. Neugin moved to suppress the ammunition and firearm. The district court denied the motion under the community-caretaking exception, and Neugin appealed. ## Issue Whether the warrantless opening of the camper was justified by the community-caretaking exception, and, if not, whether the evidence was admissible under the inevitable-discovery exception to the exclusionary rule. ## Rule The inevitable-discovery exception lets the government avoid suppression only by showing the evidence would have been discovered by lawful means independent of the violation; it cannot rest on speculation. The court reiterated that", "quote_fidelity": "mismatch", "record_id": "United States v. Neugin", "star_marker": null}}
{"assertion_id": "1dc6eecf90642907", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Neugin"}, "payload": {"as_of_content": "2020-05-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Neugin", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/United States v. Nora.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Nora
type: case
citation: "765 F.3d 1049 (2014)"
parallel_cite: ""
neutral_cite: "2014 U.S. App. LEXIS 16677; 2014 WL 4235955"
court: 9th Cir.
court_level: coa
circuit: ca9
year: 2014
date_decided: 2014-08-28
docket: 12-50485
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
  opinion_url: "https://www.courtlistener.com/opinion/2722177/united-states-v-johnny-casel-nora/"
  cluster_id: 2722177
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Nora
  status: under_review
  projected_at: 2026-07-08
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — Anchor (SACO spine: perimeter-defeats-flight-exigency, 765 F.3d at 1055; containment-vs-exit-command line)"
  - page: "[[Arrest in the Home]]"
    role: "Related — cross-doctrine (constructive-entry consequence of Payton)"
---

# United States v. Nora

*765 F.3d 1049 (9th Cir. 2014)* (No. 12-50485) · U.S. Court of Appeals, 9th Cir. · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 2722177 → 765 F.3d 1049, No. 12-50485, decided 2014-08-28 (Watford, J.). Rule/Application quotes string-matched to the CL opinion text 2026-07-08. -->

## Background
On a night in January 2008, two uniformed officers patrolling South Central Los Angeles saw Johnny Nora and two other men on the street; when Nora saw the officers he fled into his house. Officers detained a companion in the front yard while another ran to cover the back door, and then called for backup: "some 20 to 30 officers arrived and surrounded the house with weapons drawn," aided by a police helicopter. After a 20-to-30-minute standoff, "the officers used a public address system to order the occupants of the house to come out," and Nora complied and was arrested in front of the house. Officers then obtained a warrant and searched the home, seizing narcotics and firearms that formed the basis of the federal charges. Nora moved to suppress; the district court denied the motion, and he entered a conditional guilty plea.

## Issue
Whether officers who surround a suspect's home with an overwhelming show of force and summon him out over a public-address system effect a warrantless arrest "in violation of *Payton v. New York*," and whether any [[Exigent Circumstances and Hot Pursuit|exigency]] excused the failure to obtain an arrest warrant.

## Rule
*[[Payton v. New York|Payton]]* supplies the baseline: "The Court held in *Payton* that the Fourth Amendment forbids arresting a suspect inside his home unless the police first obtain an arrest warrant or an exception to the warrant requirement applies." 765 F.3d at 1054 (citing *Payton v. New York*, 445 U.S. 573, 590 (1980)). ^pin-1054

A suspect summoned out of a surrounded home is treated as arrested inside it unless he voluntarily exposed himself; the government must then justify the warrantless in-home arrest by an exception such as [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]. <!-- pin-1054 star-page CONFIRMED at orchestrator finalization 2026-07-08: quote at doc position 15602, between star markers *1054 (pos 14213) and *1055 (pos 22131) — MCP search_document, opinion 2722177. -->

The perimeter itself defeats the flight-and-danger [[Exigent Circumstances and Hot Pursuit|exigency]] the government invoked. The court found no basis to believe anyone else was endangered, and "[n]or had Nora given any other indication that he was in 'an agitated and violent state,'" *[[United States v. Al-Azzawy]]*, 784 F.2d 890, 894 (9th Cir. 1986); "[f]inally, the officers had no reason to believe Nora might pose a danger to the public by attempting to flee, since they had the house completely surrounded and could monitor all exit points." — 765 F.3d at 1055. ^pin-1055

## Application
Because the officers had probable cause but no warrant, and because a complete perimeter with monitored exits eliminated any risk of flight or escape, no [[Exigent Circumstances and Hot Pursuit|exigency]] excused the warrant requirement. The surround-and-summon tactic was therefore a warrantless arrest that *[[Payton v. New York|Payton]]* forbids: the officers "could monitor all exit points," so the very containment the government offered as justification is what negated the claimed [[Exigent Circumstances and Hot Pursuit|exigency]]. 765 F.3d at 1055. ^pin-1055b

The evidence derived from the ensuing search was fruit of the unlawful arrest and should have been suppressed.

## Conclusion
The Ninth Circuit reversed the denial of suppression and [[Reading and Citing Cases#on-remand|remanded]]. Officers who surround a home and order a suspect out cannot rely on flight-based [[Exigent Circumstances and Hot Pursuit|exigency]] to avoid the warrant requirement when the perimeter already forecloses escape.

## Treatment & subsequent history
- **Status:** ⚪ unverified (frontier stub) — **Binding in-circuit — 9th Cir.** Treatment/progeny not machine-certified until S9 promotion.
- *Nora* is the modern Ninth-Circuit spine of the surround-and-call-out (SACO) line: it applies the containment-vs-exit-command rule of *[[United States v. Al-Azzawy]]* (coerced emergence from a surrounded home is an in-home arrest) and marks the outer boundary of the flight-[[Exigent Circumstances and Hot Pursuit|exigency]] exception (perimeter defeats flight). It contrasts with the voluntary-exposure holding of *[[United States v. Vaneaton]]*, 49 F.3d 1423 (9th Cir. 1995), and with the armed-standoff [[Exigent Circumstances and Hot Pursuit|exigency]] of *Fisher v. City of San Jose*, 558 F.3d 1069 (9th Cir. 2009) (en banc).

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 2722177 + 765 F.3d 1049); renders under the ⚪ banner until S9 promotion.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Key*

## Sources
- [*United States v. Nora*, 765 F.3d 1049 (9th Cir. 2014)](https://www.courtlistener.com/opinion/2722177/united-states-v-nora/) — pinpoints: 1054 (*Payton* rule), 1055 (perimeter defeats flight/danger exigency; distinguishing *Al-Azzawy* at 894); quotes string-matched to the CL opinion text 2026-07-08.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "715fa8a46445a3dd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Nora"}, "payload": {"all": [{"cite": "765 F.3d 1049", "page": "1049", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "765"}, {"cite": "2014 U.S. App. LEXIS 16677", "page": "16677", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2014"}, {"cite": "2014 WL 4235955", "page": "4235955", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2014"}], "display": "765 F.3d 1049", "official": {"cite": "765 F.3d 1049", "page": "1049", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "765"}, "official_selection_present": true, "record_id": "United States v. Nora"}}
{"assertion_id": "0c82e38eb66c1490", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Nora"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Nora", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Nora

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Nora",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Johnny Casel Nora",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Johnny Casel NORA, AKA John Carter, AKA John Nora, AKA Johnny Nora, AKA Johnny Carl Nora, Defendant-Appellant",
    "input_case_name": "United States v. Nora",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2014-08-28",
    "year": 2014,
    "docket": "12-50485",
    "cluster_id": 2722177,
    "lead_opinion_id": 2722177,
    "sibling_ids": [],
    "absolute_url": "/opinion/2722177/united-states-v-johnny-casel-nora/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "765 F.3d 1049",
      "volume": "765",
      "reporter": "F.3d",
      "page": "1049",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. App. LEXIS 16677",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "16677",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 4235955",
        "volume": "2014",
        "reporter": "WL",
        "page": "4235955",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "765 F.3d 1049",
        "volume": "765",
        "reporter": "F.3d",
        "page": "1049",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. App. LEXIS 16677",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "16677",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 4235955",
        "volume": "2014",
        "reporter": "WL",
        "page": "4235955",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "765 F.3d 1049",
    "official_selection": {
      "court_class": "coa",
      "selected": "765 F.3d 1049",
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
    "date_created": "2026-07-08T16:52:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T16:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T16:52:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-nora--2722177",
      "to_record_id": "United States v. Nora",
      "as_of": "2026-07-08T22:30:00Z",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Nora

```
                FOR PUBLICATION

  UNITED STATES COURT OF APPEALS
       FOR THE NINTH CIRCUIT


UNITED STATES OF AMERICA,                No. 12-50485
                Plaintiff-Appellee,
                                            D.C. No.
                 v.                      2:09-cr-00092-
                                            SVW-1
JOHNNY CASEL NORA, AKA John
Carter, AKA John Nora, AKA
Johnny Nora, AKA Johnny Carl               OPINION
Nora,
              Defendant-Appellant.


      Appeal from the United States District Court
          for the Central District of California
      Stephen V. Wilson, District Judge, Presiding

                Argued and Submitted
        January 8, 2014—Pasadena, California

                 Filed August 28, 2014

   Before: William A. Fletcher, Milan D. Smith, Jr.,
         and Paul J. Watford, Circuit Judges.

              Opinion by Judge Watford
2                   UNITED STATES V. NORA

                           SUMMARY*


                          Criminal Law

    The panel reversed the district court’s denial of a motion
to suppress evidence seized from the defendant’s home, and
remanded for further proceedings, in a case in which the
defendant entered a conditional guilty plea to possession of
cocaine base with intent to distribute.

    The panel held that although the defendant’s arrest was
supported by probable cause, the arrest violated Payton v.
New York, 445 U.S. 573 (1980), and violated the Fourth
Amendment, where the officers physically took the defendant
into custody outside his home in the front yard only by
surrounding his house and ordering him to come out at
gunpoint, and no exigency existed.

    The panel held that evidence seized during a pat-down
search incident to an arrest made in violation of Payton must
be suppressed, whether the search occurs inside the home or,
as in the case of the cash and marijuana here, outside the
home. The panel held that the defendant’s post-arrest
statements are subject to suppression as well, as fruit of the
unlawful search of his person. The panel held that
suppression of this evidence renders the portions of the
warrant authorizing a search for narcotics-related evidence
and evidence of gang membership invalid. The panel held
that the remaining untainted evidence did not establish
probable cause to search the defendant’s home for the broad

  *
    This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                 UNITED STATES V. NORA                     3

range of firearms described in the warrant, and that as a
consequence, the entire warrant was invalid and all evidence
seized pursuant to it must be suppressed.


                        COUNSEL

Michael J. Treman (argued), Santa Barbara, California, for
Defendant-Appellant.

André Birotte Jr., United States Attorney, Robert E. Dugdale,
Chief, Criminal Division, Cheryl L. O’Connor (argued) and
Max B. Shiner, Assistant United States Attorneys, Los
Angeles, California, for Plaintiff-Appellee.


                        OPINION

WATFORD, Circuit Judge:

    The issue raised by this appeal is whether the police
violated Johnny Nora’s Fourth Amendment rights when they
searched his home. The search yielded narcotics and
firearms, which formed the basis for the federal charges
brought against him. After the district court denied Nora’s
motion to suppress the evidence seized from his home, Nora
entered a conditional guilty plea pending the outcome of this
appeal.

    Nora contends that, although the officers obtained a
search warrant, all of the evidence discovered during the
search must be suppressed because the warrant was invalid.
The warrant was invalid, Nora argues, because it was based
on information acquired as a result of his unlawful arrest.
4                 UNITED STATES V. NORA

And his arrest was unlawful, Nora urges, because the officers
either lacked probable cause to arrest him or, alternatively,
arrested him in violation of Payton v. New York, 445 U.S. 573
(1980).

                               I

    The events relevant here occurred on a single night in
January 2008. Two uniformed police officers were patrolling
Nora’s neighborhood in South Central Los Angeles in an
unmarked car. As they drove down Nora’s street, the officers
saw three men they didn’t know standing on the sidewalk in
front of Nora’s two-bedroom house, about 75 yards away.
The officers lost sight of the men for a few seconds. By the
time the officers pulled up in front of the house and got out of
the car, two of the three men (Nora and Andre Davis) were
standing on the porch, while the third (Patrick Hodges) stood
in the front yard, which was enclosed by a metal fence. See
Appendix (photograph of front yard and porch). The officers
stood on the sidewalk and attempted to engage in casual
conversation with the men.

    According to the officers, whose testimony the district
court credited over Nora’s conflicting testimony, Nora
appeared nervous and stood stiffly with his right side
obscured from the officers’ view. Seconds into the
conversation, Nora abruptly spun toward the front door and
pushed past Davis to get into the house. As he did so, the
officers could see that Nora was holding a blue-steel semi-
automatic handgun in his right hand. One of the officers
shouted “Stop! Police!” but Nora and Davis ignored the
command, rushed into the house, and shut the door behind
them.
                  UNITED STATES V. NORA                     5

    After Nora and Davis fled into the house, one of the
officers detained Hodges, who was still standing in the front
yard, while the other officer ran around the side of the house
to watch the back door. Someone inside the house turned off
the only light that had been on, leaving the house completely
dark. The officers then called for backup. Within minutes,
some 20 to 30 officers arrived and surrounded the house with
weapons drawn. They were aided by a police helicopter
hovering above whose lights, Nora’s wife testified, lit up the
house “like the daytime.”

    A standoff ensued for the next 20 to 30 minutes, which
ended when the officers used a public address system to order
the occupants of the house to come out. Nora and Davis
complied, followed a few minutes later by Nora’s wife and
children.

    Officers immediately handcuffed Nora and searched him.
They found a small amount of marijuana and more than
$1,000 in cash on his person. One of the officers read Nora
the warnings required by Miranda v. Arizona, 384 U.S. 436
(1966), and then briefly questioned him. Nora made several
incriminating statements in response to those questions.
Specifically, Nora admitted that he had personal use
quantities of methamphetamine and heroin in a dresser
drawer, that he lived at the house, and that he belonged to a
particular street gang. After determining Nora’s identity, the
officers ran a criminal background check, which revealed that
Nora had a prior conviction for carrying a loaded firearm and
two prior convictions for being a felon in possession of a
firearm.

   The officers sought and obtained a warrant to search
Nora’s home for the following items: marijuana,
6                 UNITED STATES V. NORA

methamphetamine, heroin, and related paraphernalia;
evidence relating to the sale of narcotics; firearms,
magazines, and ammunition; and evidence of gang
membership. The affidavit supporting the warrant relied on
the officers’ observations of Nora outside his home, as well
as the evidence obtained as a result of Nora’s arrest—namely,
the marijuana and cash found on his person, his post-arrest
statements, and the record of his prior convictions. Among
other things, the search of Nora’s home resulted in seizure of
the following:

    •   From an ironing-board closet hidden behind the
        refrigerator: quantities of cocaine, cocaine base,
        marijuana, over $9,000 in cash, and four semi-
        automatic handguns.

    •   From a bedroom dresser drawer: quantities of heroin
        and methamphetamine.

    •   From the detached garage: quantities of cocaine base,
        one handgun, one rifle, two shotguns, two electronic
        scales, handgun magazines, and ammunition.

    A federal grand jury charged Nora with possession with
intent to distribute controlled substances, possession of
firearms in furtherance of a drug trafficking offense,
possession of an unregistered firearm, and one count of being
a felon in possession of a firearm. Nora entered a conditional
guilty plea to possession of cocaine base with intent to
distribute, reserving his right to appeal the district court’s
denial of his suppression motion. The court ultimately
sentenced Nora to 122 months in prison.
                      UNITED STATES V. NORA                               7

                                     II

    Nora first contends that the officers lacked probable cause
to arrest him. The government counters that the officers had
probable cause to arrest Nora for violating California Penal
Code § 25850(a) (formerly § 12031(a)). That statute, as
relevant here, makes it a misdemeanor to carry a loaded
firearm “while in any public place or on any public street.”
§ 25850(a).1

    The officers’ firsthand observations of Nora on the porch
undoubtedly gave them probable cause to believe he was
carrying a firearm. But for purposes of § 25850(a), Nora’s
front porch is not a “public place.” See People v. Strider,
100 Cal. Rptr. 3d 66, 74 (Ct. App. 2009). The question, then,
is whether the officers had probable cause to believe both that
Nora had been carrying the firearm while standing on the
sidewalk (which is a public place), and that the firearm was
loaded.

    The officers’ observations gave rise to a “fair probability”
that Nora had been carrying the handgun while standing on
the sidewalk. Illinois v. Gates, 462 U.S. 213, 238 (1983).
That’s where the officers first saw him, and they lost sight of
him for only a few seconds before they next saw him standing
on the porch with the gun in his hand. They did not see him
pick up anything or accept anything from Davis or Hodges
while on the porch. Given the short interval during which the


  1
     “A person is guilty of carrying a loaded firearm when the person
carries a loaded firearm on the person or in a vehicle while in any public
place or on any public street in an incorporated city or in any public place
or on any public street in a prohibited area of unincorporated territory.”
Cal. Penal Code § 25850(a).
8                 UNITED STATES V. NORA

officers lost sight of Nora, they had reasonable grounds to
believe that the firearm they saw him holding on the porch
had been in his hand just moments earlier on the sidewalk as
well. See Maryland v. Pringle, 540 U.S. 366, 371 (2003).

    The facts known to the officers also established a fair
probability that the firearm was loaded. The particular
firearm involved here—a semi-automatic handgun—is
principally used for self-defense and protection of the home,
see District of Columbia v. Heller, 554 U.S. 570, 628 (2008),
purposes served most effectively if the weapon is loaded.
The officers saw Nora carrying the handgun at night outside
a home in which he later sought refuge, suggesting he was in
fact carrying the handgun for those purposes. As the district
court noted, the fact that Nora carried the handgun in his hand
“at the ready” strengthened the inference it was loaded; it
wasn’t stored in a gun case or left unattended in a vehicle,
circumstances in which a firearm might more plausibly be
unloaded. And Nora’s unprovoked flight into the house upon
seeing the officers added further weight to the inference that
criminal wrongdoing might be afoot. See Illinois v. Wardlow,
528 U.S. 119, 124–25 (2000); Sibron v. New York, 392 U.S.
40, 66–67 (1968). These facts, taken together, provided a
reasonable basis for believing Nora had violated § 25850(a).

   Nora argues that it’s possible he picked up the handgun
between the time he was standing on the sidewalk and the
time he reached the porch, and that the gun could have been
unloaded. But the concept of probable cause requires us to
deal in probabilities, not certainties, and for that reason it
doesn’t demand “the same type of specific evidence of each
element of the offense as would be needed to support a
conviction.” Adams v. Williams, 407 U.S. 143, 149 (1972).
Taking into account the totality of the circumstances, the
                  UNITED STATES V. NORA                        9

officers needed to have only a “reasonable ground” for
believing Nora had violated § 25850(a). Pringle, 540 U.S. at
371. Here, they did.

                               III

    Nora next contends that, even if the officers had probable
cause to arrest him, they arrested him in violation of Payton
v. New York, 445 U.S. 573 (1980). The Court held in Payton
that the Fourth Amendment forbids arresting a suspect inside
his home unless the police first obtain an arrest warrant or an
exception to the warrant requirement applies. Id. at 590.
That rule is designed to protect “the privacy and the sanctity
of the home,” id. at 588, and stems from “the overriding
respect for the sanctity of the home that has been embedded
in our traditions since the origins of the Republic.” Id. at 601.

    The government properly concedes that the police
arrested Nora “inside” his home for purposes of the Payton
rule. Although officers physically took Nora into custody
outside his home in the front yard, they accomplished that
feat only by surrounding his house and ordering him to come
out at gunpoint. We’ve held that forcing a suspect to exit his
home in those circumstances constitutes an in-home arrest
under Payton. See, e.g., Fisher v. City of San Jose, 558 F.3d
1069, 1074–75 (9th Cir. 2009) (en banc); United States v. Al-
Azzawy, 784 F.2d 890, 893 (9th Cir. 1985). Since the officers
didn’t obtain an arrest warrant, Nora’s arrest violated the
Fourth Amendment unless an exception to the warrant
requirement applies.

   The government argues, and the district court found, that
the “exigent circumstances” exception to the warrant
requirement applies. That exception permits a warrantless in-
10                UNITED STATES V. NORA

home arrest in certain narrowly defined circumstances. See
United States v. Struckman, 603 F.3d 731, 743 (9th Cir.
2010). One such circumstance is where the government can
show that the delay necessary to secure a warrant would
create “a substantial risk of harm to the persons involved or
to the law enforcement process.” Al-Azzawy, 784 F.2d at 894
(internal quotation marks omitted).

    Nora didn’t present the kind of immediate threat to the
safety of officers or others necessary to justify a disregard of
the warrant requirement. Our decision in Al-Azzawy provides
a useful contrast. In that case the defendant refused
commands to exit his home a short time after he threatened to
shoot his neighbor, to light his neighbor’s trailer on fire, and
to “blow up” the entire trailer park in which the two lived if
the neighbor bothered the defendant’s family again. Id.
at 891, 894. Officers were told that the defendant had also
threatened the neighbor with a pistol the day before and had
been seen in possession of hand grenades and automatic
weapons a few days earlier. Id. at 891. We held that exigent
circumstances justified the defendant’s warrantless in-home
arrest because the officers reasonably believed that he
“possessed illegal explosives and was in an agitated and
violent state.” Id. at 894. Even on those facts, we said the
exigency question was close. Id.

    The facts of this case are decidedly less compelling from
an exigency standpoint than those in Al-Azzawy. True, the
officers saw Nora in possession of a handgun. But Nora
never aimed the weapon at the officers or anyone else, and
the officers had no evidence that he had used or threatened to
use it. Cf. Fisher, 558 F.3d at 1072–73 (suspect aimed rifle
at officers and threatened to shoot). The officers had no
reason to believe that illegal weapons such as explosives were
                    UNITED STATES V. NORA                         11

present inside Nora’s home, or that anyone else to whom
Nora may have posed a danger was inside. Nor had Nora
given any other indication that he was in “an agitated and
violent state.” Al-Azzawy, 784 F.2d at 894. Finally, the
officers had no reason to believe Nora might pose a danger to
the public by attempting to flee, since they had the house
completely surrounded and could monitor all exit points. See
United States v. Gooch, 6 F.3d 673, 679 (9th Cir. 1993)
(defendant resting in closed tent posed no present danger to
officers or other campers, despite having discharged firearm
in crowded campground hours earlier).

    Our conclusion that no exigency existed is buttressed by
the fact that the offense involved here was a misdemeanor.
At the time the officers ordered Nora to exit his home, they
had probable cause to believe he had committed only a
misdemeanor violation of California Penal Code § 25850(a).2
The Supreme Court has said we should be hesitant to find
exigent circumstances “when the underlying offense for
which there is probable cause to arrest is relatively minor.”
Welsh v. Wisconsin, 466 U.S. 740, 750 (1984). Reflecting
that hesitancy, we’ve held that “an exigency related to a
misdemeanor will seldom, if ever, justify a warrantless entry
into the home.” Hopkins v. Bonvicino, 573 F.3d 752, 769
(9th Cir. 2009) (internal quotation marks omitted). In our
view, this isn’t one of the rare cases in which exigent
circumstances can be found notwithstanding the relatively
minor nature of the offense involved.




  2
    The officers were not yet aware of Nora’s criminal history, which
would have elevated the offense to a felony. See Cal. Penal Code
§ 25850(c)(1).
12                UNITED STATES V. NORA

                              IV

    Having concluded that the officers had probable cause to
arrest Nora but made the arrest in violation of Payton, we
must next decide whether the evidence obtained as a result of
Nora’s unlawful arrest should be suppressed. See Wong Sun
v. United States, 371 U.S. 471, 484–88 (1963). That evidence
falls into three categories: (1) the cash and marijuana found
on Nora during the pat-down search incident to his arrest;
(2) Nora’s post-arrest statements admitting gang membership
and the presence of personal use quantities of narcotics in the
house; and (3) information relating to Nora’s identity—in
particular, the record of his past convictions.

                              A

    As to the cash and marijuana found on Nora’s person, our
analysis is guided first and foremost by New York v. Harris,
495 U.S. 14 (1990), which established the scope of the
exclusionary rule’s application following a Payton violation.
In Harris, police had probable cause to arrest the defendant
but arrested him in his home without a warrant or exigent
circumstances. The defendant made incriminating statements
while still inside his home, and later signed a written
confession incriminating himself at the police station. The
Court noted that the statements made inside the home were
properly suppressed. Id. at 20. But the Court held that the
written statement made at the police station was not subject
to suppression, reasoning that “where the police have
probable cause to arrest a suspect, the exclusionary rule does
not bar the State’s use of a statement made by the defendant
outside of his home, even though the statement is taken after
an arrest made in the home in violation of Payton.” Id. at 21.
                  UNITED STATES V. NORA                      13

    The Court refused to suppress the statement made outside
the home because doing so would not have advanced the
deterrent purpose the exclusionary rule is designed to serve.
That purpose is served, the Court held, only by suppressing
evidence that “is in some sense the product of illegal
governmental activity.” Id. at 19 (internal quotation marks
omitted). In the context of a Payton violation, the illegality
doesn’t consist of gaining custody of the defendant; the
existence of probable cause to arrest provides a lawful basis
for that intrusion upon the defendant’s liberty. Id. at 18.
Instead, the illegality consists of the officers’ intrusion into
the privacy and sanctity of the home without prior judicial
authorization. Id. at 17. Only evidence that the police
discover as a result of having made the arrest “in the home
rather than someplace else” can be deemed the product of a
Payton violation. Id. at 19.

    Both the Supreme Court and our court have held that we
must suppress evidence seized during a pat-down search of
the defendant’s person following a Payton violation. See
Kirk v. Louisiana, 536 U.S. 635, 637–38 (2002) (per curiam);
United States v. Blake, 632 F.2d 731, 733, 736 (9th Cir.
1980). Those cases involved Payton violations in which the
police physically intruded into the home and conducted the
pat-down search while still inside. The question before us is
whether the rule of Kirk and Blake should be applied to
Payton violations involving a suspect who, like Nora, is
forced to exit his home in response to police coercion, such
that the pat-down search takes place outside the physical
confines of the home. The Sixth Circuit appears to have
applied the rule in these circumstances, albeit without
analysis. See United States v. Saari, 272 F.3d 804, 807, 812
(6th Cir. 2001) (upholding suppression of handgun found in
14                UNITED STATES V. NORA

defendant’s waistband after police ordered him to exit his
home).

    Deciding whether to apply a rule to a new factual scenario
requires knowing something of the rule’s rationale. Although
the exact rationale underlying the rule established in Kirk and
Blake wasn’t articulated, each of the potential rationales
supports extending the exclusionary rule to the scenario at
issue here. On the one hand, the rule could be based simply
on the notion that a Payton violation renders an arrest
unlawful, and a search incident to an unlawful arrest is itself
always unlawful, wherever it happens to occur. If Kirk and
Blake rest on that rationale, then deciding the suppression
issue before us is easy: The cash and marijuana found during
the search incident to Nora’s unlawful arrest must be
suppressed, even though the search occurred outside his home
in the front yard.

     On the other hand, Kirk and Blake could rest on the notion
that, when the police arrest a suspect by physically intruding
into his home without a warrant, any personal effects found
on his person must be suppressed in order to protect the
privacy and sanctity of the home. An individual might wear
or carry things on his person within the confines of his home
that he wouldn’t take with him when venturing out in public,
so items discovered during a pat-down search conducted
inside the home could well be “the fruit of having been
arrested in the home rather than someplace else.” Harris,
495 U.S. at 19. Viewed in that light, Payton’s protection of
the privacy and sanctity of the home would be incomplete if
it didn’t extend to the person of a suspect arrested inside his
home.
                  UNITED STATES V. NORA                      15

    That same rationale applies when the police violate
Payton by ordering a suspect to exit his home at gunpoint.
The home receives special constitutional protection in part
because “at the very core of the Fourth Amendment stands
the right of a man to retreat into his own home and there be
free from unreasonable governmental intrusion.” Payton,
445 U.S. at 589–90 (internal quotation marks and alterations
omitted). When the police unreasonably intrude upon that
interest by ordering a suspect to exit his home at gunpoint, the
suspect’s opportunity to collect himself before venturing out
in public is certainly diminished, if not eliminated altogether.
In this context, too, Payton’s protection of the privacy and
sanctity of the home would be incomplete if it didn’t extend
to the person of a suspect forced to abandon the refuge of his
home involuntarily.

    For these reasons, evidence seized during a pat-down
search incident to an arrest made in violation of Payton must
be suppressed, whether the search occurs inside the home, as
in Kirk and Blake, or outside the home, as in this case. In
either scenario, evidence found on the suspect’s person
should be regarded as “the fruit of having been arrested in the
home rather than someplace else.” Harris, 495 U.S. at 19.
Accordingly, the cash and marijuana seized during the search
incident to Nora’s arrest must be suppressed.

                               B

    We conclude that Nora’s post-arrest statements are
subject to suppression as well. Under our decision in United
States v. Shetler, 665 F.3d 1150 (9th Cir. 2011), Nora’s
statements must be deemed the fruit of the unlawful search of
his person.
16                UNITED STATES V. NORA

     In Shetler, the police conducted an extensive illegal
search of the defendant’s home while the defendant was
detained outside, watching as the search progressed. Id. at
1154. Officers found evidence of methamphetamine
production in the house and garage. When questioned by the
police 36 hours later, the defendant confessed to having
engaged in methamphetamine production. We held that the
defendant’s confession was the product of the illegal search
and had to be suppressed. We noted that in these
circumstances officers will likely use evidence gleaned from
the illegal search in questioning the suspect, and the suspect’s
answers “may be influenced by his knowledge that the
officials had already seized certain evidence.” Id. at 1158.
Because the government bore the burden of proving that the
defendant’s confession was not “fruit of the poisonous tree,”
id. at 1157, the government was required to produce evidence
demonstrating that the defendant’s answers “were not
induced or influenced by the illegal search.” Id. at 1158. The
government failed to do so.

    The same is true here. Nora’s incriminating statements
followed immediately on the heels of the unlawful search of
his person, which yielded marijuana and a large amount of
cash. Whether the police questioned Nora about that
evidence or not, his answers were likely influenced by his
knowledge that the police had already discovered it. As in
Shetler, the government produced no evidence to the
contrary. Nor has the government shown that intervening
circumstances rendered the connection between Nora’s
statements and the illegal search “so attenuated as to dissipate
the taint.” Id. at 1159 (internal quotation marks omitted).
Nora’s post-arrest statements must therefore be suppressed.
                    UNITED STATES V. NORA                          17

                                  C

    As to Nora’s identity—in particular, the record of his
prior convictions—we need not decide whether that evidence
is admissible. We will assume that it is, resolving any doubts
on that score in the government’s favor. As will become
clear, even on that assumption, we conclude that the
government cannot prevail.

                                 V

    In light of what we’ve said above, some of the evidence
included in the search warrant affidavit was admissible and
some of it wasn’t. The remaining question is whether that
fact renders the search warrant invalid in whole or in part.

     A search warrant isn’t rendered invalid merely because
some of the evidence included in the affidavit is tainted.
United States v. Reed, 15 F.3d 928, 933 (9th Cir. 1994). The
warrant remains valid if, after excising the tainted evidence,
the affidavit’s “remaining untainted evidence would provide
a neutral magistrate with probable cause to issue a warrant.”
Id. (internal quotation marks omitted); see also United States
v. Grandstaff, 813 F.2d 1353, 1355 (9th Cir. 1987). Thus,
after excising the cash and marijuana found on Nora’s person
and his post-arrest statements, we must determine whether the
remaining untainted evidence was sufficient to support
issuance of the warrant.3 We make that determination
without the usual deference owed to the magistrate’s initial


  3
     The government doesn’t challenge the district court’s decision to
suppress evidence discovered during a protective sweep of Nora’s home,
which officers conducted before obtaining the warrant, so we will
disregard that evidence as well.
18                UNITED STATES V. NORA

finding of probable cause. United States v. Kelley, 482 F.3d
1047, 1051 (9th Cir. 2007).

    Two principal pieces of evidence remain after excising
the tainted evidence from the affidavit: (1) the officers’
observation of Nora with a handgun under circumstances
establishing probable cause to believe he had violated
California Penal Code § 25850(a); and (2) the officers’
knowledge of Nora’s criminal history, in particular his prior
conviction for carrying a loaded firearm and his two prior
convictions for being a felon in possession of a firearm.

    This remaining, untainted evidence did not provide
probable cause to search Nora’s home for marijuana, heroin,
and methamphetamine, or for evidence of gang membership,
all of which were listed in the warrant as items subject to
seizure. Those portions of the warrant are therefore invalid.
That leaves the portion of the warrant authorizing the seizure
of “[f]irearms, assault rifles, handguns of any caliber and
shotguns of any caliber,” as well as ammunition for such
firearms. We must decide whether that portion of the warrant
is valid; if it is, the severance doctrine might apply. See
United States v. Gomez-Soto, 723 F.2d 649, 654 (9th Cir.
1984) (noting that, if applicable, the severance doctrine
“allows us to strike from a warrant those portions that are
invalid and preserve those portions that satisfy the fourth
amendment”).

    To satisfy the Fourth Amendment, the warrant’s firearms
clause must be supported by probable cause and describe with
particularity the items to be seized. United States v. Sells,
463 F.3d 1148, 1156 (10th Cir. 2006); In re Grand Jury
Subpoenas Dated Dec. 10, 1987, 926 F.2d 847, 857 (9th Cir.
1991). Because we conclude that the firearms clause was not
                  UNITED STATES V. NORA                    19

supported by probable cause, we need not decide whether the
clause satisfies the particularity requirement.

    The untainted evidence unquestionably provided probable
cause to search Nora’s home for the blue-steel semi-
automatic handgun the officers saw him carrying. Nora ran
into the house with the gun in his hand but exited without it,
giving the officers reason to believe it was still inside. The
gun was of course evidence of the crime for which the
officers had probable cause to arrest him and would therefore
have been subject to seizure on that basis alone. But without
more, the officers’ firsthand observations of Nora with a gun
in his hand did not give them reasonable grounds to believe
that any additional firearms would be found in the house. See
Millender v. Cnty. of Los Angeles, 620 F.3d 1016, 1025 (9th
Cir. 2010) (en banc), rev’d on other grounds sub nom.
Messerschmidt v. Millender, 132 S. Ct. 1235 (2012).

    The only other arguably untainted evidence the officers
had was knowledge of Nora’s criminal history. We have
stated that criminal history “can be helpful in establishing
probable cause, especially where the previous arrest or
conviction involves a crime of the same general nature as the
one the warrant is seeking to uncover.” Greenstreet v. Cnty.
of San Bernardino, 41 F.3d 1306, 1309 (9th Cir. 1994); see
also 2 Wayne R. LaFave, Search & Seizure: A Treatise on the
Fourth Amendment § 3.2(d), at 72 & n.147 (5th ed. 2012).
For example, in Hart v. Parks, 450 F.3d 1059 (9th Cir. 2006),
we noted that the suspect’s prior theft convictions were
“particularly relevant” (when combined with other evidence)
to determining whether the police had probable cause to
arrest him for another theft. Id. at 1066.
20                 UNITED STATES V. NORA

    By the same logic, Nora’s prior firearms convictions
might have been relevant if the officers had observed Nora
holding an object that appeared to be a firearm, and the issue
was whether the officers had probable cause to believe the
object was in fact a firearm. But here, the officers didn’t need
the prior convictions to support the inference that Nora in fact
possessed a firearm; they already had probable cause to
believe that. Rather, at issue is whether a fair probability
existed that Nora owned other firearms, in addition to the
single firearm the officers had observed. Nora’s prior
firearms convictions don’t speak to that issue and thus are of
marginal relevance to the probable cause issue before us.

    Our decision in United States v. Weber, 923 F.2d 1338
(9th Cir. 1991), illustrates the shortcoming here. In Weber,
the defendant ordered four photographs of children engaged
in sexually explicit acts from a fictitious distributor created as
part of a government-orchestrated sting operation. Id. at
1340. The agents planned to deliver the photographs to the
defendant’s home through a mail courier. They then sought
an anticipatory warrant to search the defendant’s home, not
just for the four photographs he had ordered, but for any other
photographs, books, magazines, and videotapes depicting
child pornography. Id. at 1340–41. To justify this much
broader search for child pornography, the warrant affidavit
contained an officer’s expert opinion regarding three classes
of suspects likely to keep such materials at home (“child
molesters,” “pedophiles,” and “child pornography
collectors”). Id. at 1341. We found the evidence insufficient
to establish probable cause to search for materials beyond the
four photographs involved in the sting. Although the expert’s
opinion described three classes of suspects likely to possess
the broad range of child pornography materials described in
                  UNITED STATES V. NORA                     21

the warrant, the government failed to demonstrate that the
defendant belonged to one of those classes. Id. at 1341, 1345.

    Here, the government’s evidence is insufficient for the
opposite reason: The affidavit established that Nora belonged
to a class of suspects with prior firearms convictions, but
didn’t show why that class of suspects would tend to own
multiple firearms. Nor did the affidavit contain other facts
tying Nora himself to firearms beyond the one he had been
observed carrying. Were we to hold that this evidence
suffices for probable cause, officers would have free rein to
search a suspect’s home anytime the suspect had prior
firearms convictions and was spotted with a single gun,
whether near his home or not. While the police in those
circumstances might have probable cause to search for the
specific firearm they observed, they would need evidence
tending to show that the suspect in question—or the class of
people to which the suspect belonged—possessed additional
firearms to justify a more expansive search. As we stated in
Weber, “probable cause to believe that some incriminating
evidence will be present at a particular place does not
necessarily mean there is probable cause to believe that there
will be more of the same.” Id. at 1344.

    We are thus left with no portion of the warrant that
satisfies the Fourth Amendment’s requirements. The officers
had probable cause to search for the blue-steel semi-
automatic handgun they saw Nora carrying, but the only
clause of the warrant addressing firearms did not specifically
describe that weapon. It instead purported to authorize the
seizure of firearms of any stripe, expanding the scope of the
search to include firearms for which the officers did not have
probable cause. Since a warrant must “be no broader than the
probable cause on which it is based,” id. at 1342, the firearms
22                UNITED STATES V. NORA

clause must be stricken as well. With no valid portion of the
warrant that could even potentially be saved, the severance
doctrine cannot apply.

    Because the entire warrant was invalid, the government’s
plain view argument also fails. In order for the plain view
doctrine to apply, “the officer must lawfully have been in the
place from which the object could be seen in plain view.”
United States v. Galpin, 720 F.3d 436, 451 (2d Cir. 2013); see
Minnesota v. Dickerson, 508 U.S. 366, 375 (1993). The
officers’ entry into Nora’s home was not authorized by a
valid warrant or an exception to the warrant requirement,
which means they were not lawfully present in the home in
the first place. The plain view doctrine is therefore
inapplicable. See United States v. Spilotro, 800 F.2d 959, 968
(9th Cir. 1986).

                      *       *       *

    Although Nora’s arrest was supported by probable cause,
the manner in which officers made the arrest violated Payton.
Evidence obtained as a result of Nora’s unlawful arrest must
be suppressed, which renders the portions of the warrant
authorizing a search for narcotics-related evidence and
evidence of gang membership invalid. The remaining
untainted evidence did not establish probable cause to search
Nora’s home for the broad range of firearms described in the
warrant. As a consequence, the entire warrant was invalid
and all evidence seized pursuant to it must be suppressed.
We reverse the district court’s order denying Nora’s
suppression motion and remand for further proceedings.

     REVERSED and REMANDED.
UNITED STATES V. NORA   23




     APPENDIX
                        24   UNITED STATES V. NORA




                                        Case 2:09-cr-00092-SVW Document ID: 862538211/02/09 Page 2 of Page: 31 ID #:189
                                         Case: 12-50485 05/10/2013      36-7 Filed    DktEntry: 10-2 3 Page of 257




                                  PAGE 23




United States v. Nora                                                         28                                          Excerpts of Record
CA # 12-50485                                                                                                             Volume II

```

---
