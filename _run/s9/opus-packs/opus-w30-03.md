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

## GROUP: content/cases/Cooper v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Cooper v. California"
type: case
citation: "386 U.S. 58 (1967)"
parallel_cite: "87 S. Ct. 788; 17 L. Ed. 2d 730"
neutral_cite: 1967 U.S. LEXIS 2199
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-02-20
docket: 103
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-02-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Cooper v. California
  varies_by_point: false
  scope_note: "Pre-dates the modern inventory line (Opperman/Bertine) and the articulated automobile exception, but remains good law as a reasonableness-of-custodial-search holding; no negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107360/cooper-v-california/"
  cluster_id: 107360
  opinion_id: 9423351
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[South Dakota v. Opperman]]", "[[Colorado v. Bertine]]", "[[Florida v. White]]", "[[Cardwell v. Lewis]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "impound", "forfeiture", "custodial-search", "reasonableness"]
holding: "A warrantless search of a car the police lawfully hold in custody for forfeiture is reasonable where the search is closely related to the reason the car was seized and is being retained; reasonableness, not state-law authorization, is the Fourth Amendment test."
lake:
  record_id: Cooper v. California
  status: verified
  projected_at: 2026-07-09
---

# Cooper v. California

*386 U.S. 58 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Cooper's arrest for a narcotics offense, officers impounded his car under a California statute requiring that a vehicle used in narcotics activity be seized and held "as evidence until a forfeiture has been declared or a release ordered." A week later, without a warrant, an officer searched the impounded car and found a piece of a brown paper sack used to wrap heroin; forfeiture was not declared until over four months after seizure. The state appellate court, reading *[[Preston v. United States]]*, held the search unreasonable.

## Issue
Whether a warrantless search of an automobile that the police are required by state law to seize and hold in custody pending forfeiture is reasonable under the Fourth Amendment.

## Rule
Reasonableness — not state-law authorization — is the test, and it turns on the facts: "whether a search and seizure is unreasonable within the meaning of the Fourth Amendment depends upon the facts and circumstances of each case." — 386 U.S. at 59. ^pin-59

A custodial search tied to the reason for the impoundment is reasonable: the "subsequent search of the car — whether the State had 'legal title' to it or not — was closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained." — *Id.* at 61. ^pin-61

Thus: "Under the circumstances of this case, we cannot hold unreasonable under the Fourth Amendment the examination or search of a car validly held by officers for use as evidence in a forfeiture proceeding." — [*Id.* at 62](https://www.courtlistener.com/opinion/107360/cooper-v-california/#:~:text=Under%20the%20circumstances%20of%20this). ^pin-62

## Application
Unlike *[[Preston v. United States|Preston]]* — where the car's custody (after a vagrancy arrest) was "totally unrelated" to the charge — here the statute required officers to seize and retain Cooper's car as evidence pending forfeiture, and they had to keep it for months. The search was closely connected to the reason for that custody, and "[i]t would be unreasonable to hold that the police, having to retain the car in their custody for such a length of time, had no right, even for their own protection, to search it." That the police could have obtained a warrant was no answer, because the test is whether the search was reasonable, not whether a warrant could have been procured.

## Conclusion
Affirmed. The warrantless search of a car lawfully held in police custody for forfeiture, closely related to the reason for that custody, was reasonable under the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Cooper* is an early custodial/forfeiture-search holding later joined by the inventory line ([[South Dakota v. Opperman]], [[Colorado v. Bertine]]) and the forfeiture-seizure rule of [[Florida v. White]].

## Appears on
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Cooper v. California*, 386 U.S. 58 (1967) — https://www.courtlistener.com/opinion/107360/cooper-v-california/ — pinpoints: 59, 61, 62.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a601ce6583675b79", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "386 U.S. 58 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 2199", "official_citation_present": true, "parallel_cite": "87 S. Ct. 788; 17 L. Ed. 2d 730", "title": "Cooper v. California", "year": "1967"}}
{"assertion_id": "154af159ecdc3cdf", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless search of a car the police lawfully hold in custody for forfeiture is reasonable where the search is closely related to the reason the car was seized and is being retained; reasonableness, not state-law authorization, is the Fourth Amendment test.", "title": "Cooper v. California"}}
{"assertion_id": "2fbe39f7d3743308", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Related (cross-doctrine)", "title": "Cooper v. California"}}
{"assertion_id": "39a7295c2fa7b564", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Cooper v. California"}}
{"assertion_id": "49c090ae91b66374", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-02-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Cooper v. California", "field_i_validity": "good_law", "scope_note": "Pre-dates the modern inventory line (Opperman/Bertine) and the articulated automobile exception, but remains good law as a reasonableness-of-custodial-search holding; no negative treatment.", "title": "Cooper v. California", "varies_by_point": "false"}}
```

### lake record — Cooper v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Cooper v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Cooper v. California",
    "case_name_short": "Cooper",
    "case_name_full": "Cooper v. California",
    "input_case_name": "Cooper v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-02-20",
    "year": 1967,
    "docket": "103",
    "cluster_id": 107360,
    "lead_opinion_id": 9423351,
    "sibling_ids": [
      107360,
      9423351,
      9423352
    ],
    "absolute_url": "/opinion/107360/cooper-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8967442,
        "score": 20,
        "case_name": "Cooper v. California"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "386 U.S. 58",
      "volume": "386",
      "reporter": "U.S.",
      "page": "58",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 788",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "788",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 730",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "730",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 2199",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2199",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "386 U.S. 58",
        "volume": "386",
        "reporter": "U.S.",
        "page": "58",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 788",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "788",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 730",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "730",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 2199",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2199",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "386 U.S. 58",
    "official_selection": {
      "court_class": "scotus",
      "selected": "386 U.S. 58",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-59",
      "page": null,
      "quote": "A week later, without a warrant, an officer searched the impounded car and found a piece of a brown paper sack used to wrap heroin; forfeiture was not declared until over four months after seizure. The state appellate court, reading *Preston v. United States*, held the search unreasonable. ## Issue Whether a warrantless search of an automobile that the police are required by state law to seize and hold in custody pending forfeiture is reasonable under the Fourth Amendment. ## Rule Reasonableness \u2014 not state-law authorization \u2014 is the test, and it turns on the facts:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-61",
      "page": null,
      "quote": "subsequent search of the car \u2014 whether the State had 'legal title' to it or not \u2014 was closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-62",
      "page": null,
      "quote": "Under the circumstances of this case, we cannot hold unreasonable under the Fourth Amendment the examination or search of a car validly held by officers for use as evidence in a forfeiture proceeding.",
      "star_marker": "62",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8973,
      "fragment": "#:~:text=Under%20the%20circumstances%20of%20this",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-02-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Cooper v. California",
    "varies_by_point": false,
    "scope_note": "Pre-dates the modern inventory line (Opperman/Bertine) and the articulated automobile exception, but remains good law as a reasonableness-of-custodial-search holding; no negative treatment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Clarence E. Johnson",
          "cluster_id": 4343883,
          "cite": [
            "208 So. 3d 843",
            "2017 Fla. App. LEXIS 995"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Jordan Heath Dentler",
          "cluster_id": 4472853,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
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
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Yarborough v. State",
          "cluster_id": 5268654,
          "cite": [
            "981 S.W.2d 846",
            "1998 Tex. App. LEXIS 6575",
            "1998 WL 734396"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex Parte Bowers",
          "cluster_id": 1529526,
          "cite": [
            "886 S.W.2d 346",
            "1994 WL 456838"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 2425299,
          "cite": [
            "867 S.W.2d 63",
            "1993 WL 461699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bassano",
          "cluster_id": 2428155,
          "cite": [
            "827 S.W.2d 557",
            "1992 WL 51165"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Walter Bryan Roberson",
          "cluster_id": 537703,
          "cite": [
            "897 F.2d 1092",
            "1990 U.S. App. LEXIS 4639",
            "1990 WL 27247"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coolidge v. New Hampshire",
          "cluster_id": 108377,
          "cite": [
            "29 L. Ed. 2d 564",
            "91 S. Ct. 2022",
            "403 U.S. 443",
            "1971 U.S. LEXIS 25"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Maroney",
          "cluster_id": 108184,
          "cite": [
            "26 L. Ed. 2d 419",
            "90 S. Ct. 1975",
            "399 U.S. 42",
            "1970 U.S. LEXIS 19"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sibron v. New York",
          "cluster_id": 107730,
          "cite": [
            "20 L. Ed. 2d 917",
            "88 S. Ct. 1889",
            "392 U.S. 40",
            "1968 U.S. LEXIS 1346",
            "44 Ohio Op. 2d 402"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ross",
          "cluster_id": 110719,
          "cite": [
            "72 L. Ed. 2d 572",
            "102 S. Ct. 2157",
            "456 U.S. 798",
            "1982 U.S. LEXIS 18",
            "50 U.S.L.W. 4580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Mosley",
          "cluster_id": 109336,
          "cite": [
            "46 L. Ed. 2d 313",
            "96 S. Ct. 321",
            "423 U.S. 96",
            "1975 U.S. LEXIS 100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
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
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. DeFillippo",
          "cluster_id": 110127,
          "cite": [
            "61 L. Ed. 2d 343",
            "99 S. Ct. 2627",
            "443 U.S. 31",
            "1979 U.S. LEXIS 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 2424950,
          "cite": [
            "988 S.W.2d 770",
            "1999 Tex. Crim. App. LEXIS 33",
            "1999 WL 212791"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Breverman",
          "cluster_id": 1198942,
          "cite": [
            "960 P.2d 1094",
            "77 Cal. Rptr. 2d 870",
            "19 Cal. 4th 142",
            "98 Cal. Daily Op. Serv. 6812",
            "98 Daily Journal DAR 9358",
            "1998 Cal. LEXIS 5589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Hass",
          "cluster_id": 109221,
          "cite": [
            "43 L. Ed. 2d 570",
            "95 S. Ct. 1215",
            "420 U.S. 714",
            "1975 U.S. LEXIS 5"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lafayette",
          "cluster_id": 110976,
          "cite": [
            "77 L. Ed. 2d 65",
            "103 S. Ct. 2605",
            "462 U.S. 640",
            "1983 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berger v. New York",
          "cluster_id": 107483,
          "cite": [
            "18 L. Ed. 2d 1040",
            "87 S. Ct. 1873",
            "388 U.S. 41",
            "1967 U.S. LEXIS 2964"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "PruneYard Shopping Center v. Robins",
          "cluster_id": 110292,
          "cite": [
            "64 L. Ed. 2d 741",
            "100 S. Ct. 2035",
            "447 U.S. 74",
            "1980 U.S. LEXIS 129",
            "6 Media L. Rep. (BNA) 1311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gunwall",
          "cluster_id": 1390131,
          "cite": [
            "720 P.2d 808",
            "106 Wash. 2d 54"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heitman v. State",
          "cluster_id": 2461257,
          "cite": [
            "815 S.W.2d 681",
            "60 U.S.L.W. 2074",
            "1991 Tex. Crim. App. LEXIS 160",
            "1991 WL 111761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cardwell v. Lewis",
          "cluster_id": 109069,
          "cite": [
            "41 L. Ed. 2d 325",
            "94 S. Ct. 2464",
            "417 U.S. 583",
            "1974 U.S. LEXIS 75",
            "69 Ohio Op. 2d 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edwards",
          "cluster_id": 108995,
          "cite": [
            "39 L. Ed. 2d 771",
            "94 S. Ct. 1234",
            "415 U.S. 800",
            "1974 U.S. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hendrickson",
          "cluster_id": 1135960,
          "cite": [
            "917 P.2d 563"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107360 OR 9423351 OR 9423352) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MDA1NjY0MDAwMDAmcz0xOTkyMDA3JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107360+OR+9423351+OR+9423352%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(107360 OR 9423351 OR 9423352)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzQmcz0xMzQ5MjU4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107360+OR+9423351+OR+9423352%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107360 OR 9423351 OR 9423352)",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 0,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107360 OR 9423351 OR 9423352)",
    "indexed_citing_opinions": 993,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107360,
        "count": 935,
        "count_source": "search"
      },
      {
        "opinion_id": 9423351,
        "count": 97,
        "count_source": "search"
      },
      {
        "opinion_id": 9423352,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1583,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/cooper-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3MzQ1NDgmcz02NDY0NTgwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107360+OR+9423351+OR+9423352%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107360,
        "cited_id": 102004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107360,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107360,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107360,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107360,
        "cited_id": 106862,
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
    "date_created": "2026-07-05T01:14:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:20:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Cooper v. California

```
<opinion type="majority">
<author id="b136-11">Mr. Justice Black</author>
<p id="A4A">delivered the opinion of the Court.</p>
<p id="Aiq">Petitioner was convicted in a California state court of selling heroin to a police informer. The conviction rested in part on the introduction in evidence of a small piece of a brown paper sack seized by police without a warrant from the glove compartment of an automobile which police, upon petitioner’s arrest, had impounded and were holding in a garage. The search occurred a week after the arrest of petitioner. Petitioner appealed his convic<page-number citation-index="1" label="59">*59</page-number>tion to the California District Court of Appeal which, considering itself bound by our holding and opinion in <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>, held that the search and seizure violated the Fourth Amendment’s ban of unreasonable searches and seizures. That court went on, however, to determine that this was harmless error under Art. VI, § 4½, of California’s Constitution which provides that judgments should not be set aside or reversed unless the court is of the opinion that the error “resulted in a miscarriage of justice.” <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/" aria-description="Citation for case: People v. Cooper">234 Cal. App. 2d 587</a></span>, <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/" aria-description="Citation for case: People v. Cooper">44 Cal. Rptr. 483</a></span>. The California Supreme Court declined to hear the case. We granted certiorari along with <em>Chapman </em>v. <em>California, ante, </em>p. 18, to consider whether the California harmless-error constitutional provision could' be used in this way to ignore the alleged federal constitutional error. <span class="citation multiple-matches"><a href="/c/U.%20S./384/904/">384 U. S. 904</a></span>. We have today passed upon the question in <em>Chapman, </em>but do not reach it in this case because we are satisfied that the lower court erroneously decided that our <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>case required that this, search be held- an unreasonable one within the meaning of the Fourth Amendment.</p>
<p id="b137-5">We made it clear in <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>that whether a search and seizure is unreasonable within the meaning of the Fourth Amendment depends upon the facts and circumstances of each case and pointed out, in particular, that searches of cars that are constantly movable may make the search of a car without a warrant a reasonable one although the result might be the opposite in a search of a home, a store, or other fixed piece of property. <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#366" aria-description="Citation for case: Preston v. United States">376 U. S., at 366-367</a></span>. In <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>the search was sought to be justified primarily on the ground that it was incidental to and part of a lawful arrest. There we said that “[o]nce an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest.” <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Id.,</a></span> </em>at -367. In the <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>case, it was alternatively argued that the warrantless <page-number citation-index="1" label="60">*60</page-number>search, after the arrest was over and while Preston’s car was being held for him by the police, was justified because the officers had probable cause to believe the car was stolen. But the police arrested Preston for vagrancy, not theft, and no claim was made that the police had Authority to hold his car on that charge. The search was therefore to be treated as though his car was in his own or his agent’s possession, safe from intrusions by the police or anyone else. The situation involving petitioner’s car is quite different.</p>
<p id="b138-4">Here, California’s Attorney General concedes that the search was not incident to an arrest. It is argued, however, that the search was reasonable on other grounds. Section 11611 of the California Health &amp; Safety Code provides that any officer making an arrest for ⅝ narcotics violation shall seize and deliver to the State Division of Narcotic Enforcement any vehicle used to store, conceal, transport, sell or facilitate the possession of. narcotics, such vehicle “to be <em>held as evidence </em>until a forfeiture has been declared or a release ordered.” <footnotemark>1</footnotemark> (Emphasis supplied.) Petitioner’s vehicle, which evidence showed had been used to carry oh his narcotics possession and transportation, was impounded by the officers and their duty required that it be kept “as evidence” until forfeiture proceedings were carried to a conclusion. The lower court concluded, as a matter of state law, that the state forfeiture statute did not by “clear and express language” <page-number citation-index="1" label="61">*61</page-number>authorize the officers to search petitioner’s car. <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/#598" aria-description="Citation for case: People v. Cooper">234 Cal. App. 2d, at 598</a></span>, <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/#491" aria-description="Citation for case: People v. Cooper">44 Cal. Rptr., at 491</a></span>. But the question here is not whether the search was authorized by state "law. The question is rather whether the search was reasonable under the Fourth Amendment. Just as a search authorized by state law may be an unreasonable one under that amendment, so may a search not expressly authorized by state law be justified as a constitutionally reasonable one. While it is true, as the lower court said, that “lawful custody of an automobile does not of itself dispense with constitutional requirements of searches thereafter made of it,” <em>ibid., </em>the reason for and nature of the custody may constitutionally justify the search. Preston was arrested for vagrancy. An arresting officer took his car to the station rather than just leaving it on the street. It was not suggested that this was done other than for Preston’s convenience or that the police had any right to impound the car and keep it from Preston or whomever he might send for it. The fact that the police had custody of Preston’s car was totally'unrelated to the vagrancy charge for which they arrested him. So was their subsequent search of the car.* This case is not <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span>, </em>nor is it controlled by it. Here the officers seized petitioner’s car because they were required, to do so by state law. They seized it because of the crime for which they arrested petitioner. They seized it to impound it' and they had to keep it until forfeiture proceedings were concluded. Their subsequent search of the car — whether the State had “legal title” to it or not— was closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained. The forfeiture of petitioner’s car did not take place until over four months after it was lawfully seized. It would be unreasonable to hold that the police, having to retain the car in their custody for such a length of time, had no right, even for their own <page-number citation-index="1" label="62">*62</page-number>protection, to search it. It is rio answer to say that the police could have obtained a search warrant, for “[t]he relevant test is not whether it is reasonable to procure a search warrant, but whether the search was reasonable.” <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66</a></span>. Under the circumstances of this case, we cannot hold unreasonable under the Fourth Amendment the examination or search of a car validly held by officers for use as evidence in a forfeiture proceeding.</p>
<p id="b140-5">Our holding, of course, does not affect the State’s power to impose higher standards on searches and seizures than required by the Federal Constitution if it chooses to do so. And when such state standards alone have been violated, the State is free, without review by us, to apply its own state harmless-error rule to such errors of state law. There being no federal constitutional error her.e, there is no need for us to determine whether the lower court properly applied its state harmless-error rule.<footnotemark>2</footnotemark></p>
<p id="AvO">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b138-5"> Cal. Health &amp;'Safety Code §11610 provides:</p>
<blockquote id="b138-6">"The interest of any registered owner of a vehicle used to unlawfully transport or facilitate the unlawful transportation of any narcotic, or in which any narcotic is unlawfully kept, deposited, or concealed or which is used to facilitate the unlawful keeping, depositing or concealment of any narcotic, or in which any narcotic is unlawfully possessed -by ah occupant thereof or which is used to facilitate the unlawful possession of any narcotic by an occupant thereof, shall be forfeited to the State.”</blockquote>
</footnote>
<footnote label="2">
<p id="b140-8">Petitioner also presents the contention here that he was unconstitutionally deprived of the right to confront a witness against him, because, the State did not produce the informant to testify against him. This contention we consider absolutely devoid of merit.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Corley v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Corley v. United States"
type: case
citation: "556 U.S. 303 (2009)"
parallel_cite: "129 S. Ct. 1558; 173 L. Ed. 2d 443"
neutral_cite: 2009 U.S. LEXIS 2512
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-04-06
docket: 07-10441
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-04-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Corley v. United States
  varies_by_point: false
  scope_note: "Good law; the controlling modern statement of the federal McNabb-Mallory prompt-presentment rule as modified by 18 U.S.C. §3501. A federal-court rule (Rule 5(a)/§3501), not a constitutional rule binding the States."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145888/corley-v-united-states/"
  cluster_id: 145888
  opinion_id: 145888
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Related (cross-doctrine)"
related: ["[[McNabb v. United States]]", "[[Mallory v. United States]]", "[[Miranda v. Arizona]]", "[[Dickerson v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "confessions", "mcnabb-mallory", "prompt-presentment", "section-3501", "voluntariness"]
holding: "18 U.S.C. §3501 modified but did not supplant the McNabb-Mallory rule: a federal confession made before presentment and more than six hours after arrest must be suppressed if the presentment delay was unreasonable or unnecessary."
lake:
  record_id: Corley v. United States
  status: verified
  projected_at: 2026-07-06
---

# Corley v. United States

*556 U.S. 303 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Johnnie Corley was suspected of a bank robbery. Federal agents arrested him about 8 a.m. on an unrelated state warrant after he fled and assaulted an officer. The FBI held him at a local station, took him to a hospital for a minor cut, and then to the Philadelphia FBI office. Although the nearest magistrate judges' chambers were in the same building, the agents did not present Corley but questioned him, and about 9.5 hours after arrest he began an oral confession to the robbery, followed later by a written one. He moved to suppress the confessions under the McNabb-Mallory rule for unreasonable delay in presentment.

## Issue
Whether 18 U.S.C. §3501 abolished the McNabb-Mallory rule entirely, or whether §3501(c) merely creates a six-hour safe harbor — leaving McNabb-Mallory to exclude a federal confession made during an unreasonable presentment delay beyond that window.

## Rule
Section 3501 modified, but did not supplant, McNabb-Mallory. The Court restated the rule it preserved: "the rule known simply as *McNabb-Mallory* 'generally render[s] inadmissible confessions made during periods of detention that violat[e] the prompt presentment requirement of Rule 5(a).'" — 556 U.S. at 309 (quoting *United States v. Alvarez-Sanchez*, 511 U.S. 350, 354 (1994)). ^pin-309

"We hold that §3501 modified *McNabb-Mallory* without supplanting it. Under the rule as revised by §3501(c), a district court with a suppression claim must find whether the defendant confessed within six hours of arrest . . . . If the confession occurred before presentment and beyond six hours, however, the court must decide whether delaying that long was unreasonable or unnecessary under the *McNabb-Mallory* cases, and if it was, the confession is to be suppressed." — *Id.* at 322. ^pin-322

## Application
Corley's oral confession came roughly 9.5 hours after his arrest, before he was presented to a magistrate. Because that placed the statement potentially outside §3501(c)'s six-hour window, the courts below had to determine whether the confession should be treated as made within six hours and, if not, whether the additional delay was unreasonable or unnecessary under McNabb-Mallory — and to make the same inquiry as to the written confession. The Third Circuit had instead held that §3501 abrogated McNabb-Mallory altogether and so never made those findings; that was error.

## Conclusion
Section 3501 modified McNabb-Mallory without supplanting it. The judgment of the Court of Appeals was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]] to determine whether Corley's confessions fell within the six-hour safe harbor and, if not, whether the presentment delay was unreasonable or unnecessary.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Corley* is the controlling modern statement of the federal prompt-presentment rule, applying [[McNabb v. United States]] and [[Mallory v. United States]] as modified by 18 U.S.C. §3501. It is a **federal-court** evidentiary rule (Federal Rule of Criminal Procedure 5(a) / §3501), not a constitutional rule binding the States. It draws on [[Dickerson v. United States]] for the background that §3501 was Congress's response to [[Miranda v. Arizona]] and McNabb-Mallory.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*
- [[Miranda and Custodial Interrogation]] — *Related (cross-doctrine)*

## Sources
- *Corley v. United States*, 556 U.S. 303 (2009) — https://www.courtlistener.com/opinion/145888/corley-v-united-states/ — pinpoints: 309, 322.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d69737473c348777", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "556 U.S. 303 (2009)", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 2512", "official_citation_present": true, "parallel_cite": "129 S. Ct. 1558; 173 L. Ed. 2d 443", "title": "Corley v. United States", "year": "2009"}}
{"assertion_id": "2f669e3d75175ff8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "18 U.S.C. §3501 modified but did not supplant the McNabb-Mallory rule: a federal confession made before presentment and more than six hours after arrest must be suppressed if the presentment delay was unreasonable or unnecessary.", "title": "Corley v. United States"}}
{"assertion_id": "677661b560ed072f", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Related (cross-doctrine)", "title": "Corley v. United States"}}
{"assertion_id": "a9059ec215a2a3a0", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Corley v. United States"}}
{"assertion_id": "741ee7de07ee2ad6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Corley v. United States"}}
{"assertion_id": "afc80d39c9f869a1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2009-04-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Corley v. United States", "field_i_validity": "good_law", "scope_note": "Good law; the controlling modern statement of the federal McNabb-Mallory prompt-presentment rule as modified by 18 U.S.C. §3501. A federal-court rule (Rule 5(a)/§3501), not a constitutional rule binding the States.", "title": "Corley v. United States", "varies_by_point": "false"}}
```

### lake record — Corley v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Corley v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Corley v. United States",
    "case_name_short": "Corley",
    "case_name_full": "Corley v. United States",
    "input_case_name": "Corley v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-04-06",
    "year": 2009,
    "docket": "07-10441",
    "cluster_id": 145888,
    "lead_opinion_id": 145888,
    "sibling_ids": [
      145888
    ],
    "absolute_url": "/opinion/145888/corley-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "556 U.S. 303",
      "volume": "556",
      "reporter": "U.S.",
      "page": "303",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 1558",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1558",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 443",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 2512",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "2512",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "556 U.S. 303",
        "volume": "556",
        "reporter": "U.S.",
        "page": "303",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 1558",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1558",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 443",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 2512",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "2512",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "556 U.S. 303",
    "official_selection": {
      "court_class": "scotus",
      "selected": "556 U.S. 303",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-309",
      "page": null,
      "quote": "--- # Corley v. United States *556 U.S. 303 (2009)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Johnnie Corley was suspected of a bank robbery. Federal agents arrested him about 8 a.m. on an unrelated state warrant after he fled and assaulted an officer. The FBI held him at a local station, took him to a hospital for a minor cut, and then to the Philadelphia FBI office. Although the nearest magistrate judges' chambers were in the same building, the agents did not present Corley but questioned him, and about 9.5 hours after arrest he began an oral confession to the robbery, followed later by a written one. He moved to suppress the confessions under the McNabb-Mallory rule for unreasonable delay in presentment. ## Issue Whether 18 U.S.C. \u00a73501 abolished the McNabb-Mallory rule entirely, or whether \u00a73501(c) merely creates a six-hour safe harbor \u2014 leaving McNabb-Mallory to exclude a federal confession made during an unreasonable presentment delay beyond that window. ## Rule Section 3501 modified, but did not supplant, McNabb-Mallory. The Court restated the rule it preserved:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-322",
      "page": null,
      "quote": "We hold that \u00a73501 modified *McNabb-Mallory* without supplanting it. Under the rule as revised by \u00a73501(c), a district court with a suppression claim must find whether the defendant confessed within six hours of arrest . . . . If the confession occurred before presentment and beyond six hours, however, the court must decide whether delaying that long was unreasonable or unnecessary under the *McNabb-Mallory* cases, and if it was, the confession is to be suppressed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-04-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Corley v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; the controlling modern statement of the federal McNabb-Mallory prompt-presentment rule as modified by 18 U.S.C. \u00a73501. A federal-court rule (Rule 5(a)/\u00a73501), not a constitutional rule binding the States.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Pharmaceutical Care Management Ass'n v. Gerhart",
          "cluster_id": 4337608,
          "cite": [
            "852 F.3d 722",
            "63 Employee Benefits Cas. (BNA) 1085",
            "2017 WL 104467",
            "2017 U.S. App. LEXIS 476"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "MSPA Claims 1, LLC v. Infinity Auto Insurance Company",
          "cluster_id": 4252384,
          "cite": [
            "835 F.3d 1351",
            "2016 U.S. App. LEXIS 15984"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Doscher v. Sea Port Group Securities, LLC",
          "cluster_id": 4246233,
          "cite": [
            "832 F.3d 372",
            "2016 U.S. App. LEXIS 14767",
            "2016 WL 4245427"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Natural Resources Defense Council, Inc. v. Pritzker",
          "cluster_id": 4238897,
          "cite": [
            "828 F.3d 1125",
            "2016 D.A.R. 7241",
            "82 ERC (BNA) 1979",
            "2016 U.S. App. LEXIS 13021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marx v. General Revenue Corp.",
          "cluster_id": 821305,
          "cite": [
            "185 L. Ed. 2d 242",
            "133 S. Ct. 1166",
            "568 U.S. 371",
            "2013 U.S. LEXIS 1859",
            "81 U.S.L.W. 4135",
            "84 Fed. R. Serv. 3d 1486",
            "24 Fla. L. Weekly Fed. S 60"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Erickson Meko Campbell",
          "cluster_id": 6357475,
          "cite": [
            "26 F.4th 860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Forest Grove School District v. T. A.",
          "cluster_id": 145855,
          "cite": [
            "174 L. Ed. 2d 168",
            "129 S. Ct. 2484",
            "557 U.S. 230",
            "2009 U.S. LEXIS 4645",
            "77 U.S.L.W. 4550",
            "21 Fla. L. Weekly Fed. S 983"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walter Shuker v. Smith & Nephew PLC",
          "cluster_id": 4473712,
          "cite": [
            "885 F.3d 760"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mary Jo C. v. New York State and Local Retirement System et ano.",
          "cluster_id": 816224,
          "cite": [
            "707 F.3d 144",
            "2013 WL 322879",
            "2013 U.S. App. LEXIS 2013"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthew Alexander v. Verizon Wireless Services, LL",
          "cluster_id": 4442643,
          "cite": [
            "875 F.3d 243"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bloch v. Frischholz",
          "cluster_id": 1345471,
          "cite": [
            "587 F.3d 771",
            "2009 U.S. App. LEXIS 24917",
            "2009 WL 3789996"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ward v. Chavez",
          "cluster_id": 799476,
          "cite": [
            "678 F.3d 1042",
            "2012 WL 1592171",
            "2012 U.S. App. LEXIS 9316"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jane Doe v. Mercy Catholic Medical Center",
          "cluster_id": 4373438,
          "cite": [
            "850 F.3d 545",
            "2017 WL 894455",
            "2017 U.S. App. LEXIS 4004",
            "101 Empl. Prac. Dec. (CCH) 45,757"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Latiolais v. Eagle, Incorporated",
          "cluster_id": 4729521,
          "cite": [
            "951 F.3d 286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Landstar Express America, Inc. v. Federal Maritime Commission",
          "cluster_id": 187384,
          "cite": [
            "569 F.3d 493",
            "386 U.S. App. D.C. 336",
            "2009 U.S. App. LEXIS 13940",
            "2009 WL 1812746"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glaser v. Wound Care Consultants, Inc.",
          "cluster_id": 1196972,
          "cite": [
            "570 F.3d 907",
            "2009 U.S. App. LEXIS 14394",
            "2009 WL 1885500"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guedes v. Bureau of Alcohol, Tobacco, Firearms",
          "cluster_id": 4605646,
          "cite": [
            "920 F.3d 1"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kawashima v. Holder",
          "cluster_id": 623145,
          "cite": [
            "182 L. Ed. 2d 1",
            "132 S. Ct. 1166",
            "565 U.S. 478",
            "2012 U.S. LEXIS 1084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Khadidja Issa v. Lancaster School District",
          "cluster_id": 4343616,
          "cite": [
            "847 F.3d 121",
            "2017 WL 393164",
            "2017 U.S. App. LEXIS 1595",
            "339 Educ. L. Rep. 630"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G.G. v. Salesforce.com, Inc.",
          "cluster_id": 9417992,
          "cite": [
            "76 F.4th 544"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sioux Honey Ass'n v. Hartford Fire Insurance",
          "cluster_id": 624415,
          "cite": [
            "672 F.3d 1041",
            "2012 WL 379626",
            "33 I.T.R.D. (BNA) 1929",
            "2012 U.S. App. LEXIS 2399"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barnes v. Belice (In Re Belice)",
          "cluster_id": 2195918,
          "cite": [
            "461 B.R. 564",
            "2011 WL 6942900"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barton v. Barr",
          "cluster_id": 4747781,
          "cite": [
            "590 U.S. 222",
            "140 S. Ct. 1442",
            "206 L. Ed. 2d 682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dane Gillis",
          "cluster_id": 4660754,
          "cite": [
            "938 F.3d 1181"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Trinity Rolando Cabezas-Montano",
          "cluster_id": 4722792,
          "cite": [
            "949 F.3d 567"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rubin v. Islamic Republic of Iran",
          "cluster_id": 4469600,
          "cite": [
            "583 U.S. 202",
            "138 S. Ct. 816",
            "200 L. Ed. 2d 58",
            "2018 U.S. LEXIS 1376"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Lehman Bros. Mortgage-Backed Securities",
          "cluster_id": 216493,
          "cite": [
            "650 F.3d 167"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Clenney",
          "cluster_id": 184207,
          "cite": [
            "631 F.3d 658",
            "2011 U.S. App. LEXIS 2117",
            "2011 WL 322640"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Redlightning",
          "cluster_id": 177836,
          "cite": [
            "624 F.3d 1090",
            "2010 U.S. App. LEXIS 21957",
            "2010 WL 4158583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145888) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDMyNTk4NDAwMDAwJnM9MjgwMzQwOCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145888%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(145888)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01OCZzPTg0NDEyMjcmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145888%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145888)",
        "reviewed": 47,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 47,
        "triage_read": 0,
        "triage_snippet_classified": 47
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145888)",
    "indexed_citing_opinions": 458,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145888,
        "count": 458,
        "count_source": "search"
      }
    ],
    "citation_count": 914,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/corley-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MzY5MjQmcz0xMDAzOTI2NyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145888%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145888,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 104603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 110077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 110079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 110258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 111043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 111487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 112310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 112585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 112670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 112706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 117863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 117887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 117955,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 118324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 118347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 136987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 145646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 287662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 307188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 350606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 411243,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 435237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 577700,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 604116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 733387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 779209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 1087948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 1193367,
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
    "date_created": "2026-07-05T01:20:16Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:21:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:21:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:27:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:21:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Corley v. United States

```
(Slip Opinion)              OCTOBER TERM, 2008                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                     CORLEY v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE THIRD CIRCUIT

    No. 07–10441.       Argued January 21, 2009—Decided April 6, 2009
McNabb v. United States, 318 U. S. 332, and Mallory v. United States,
 354 U. S. 449, “generally rende[r] inadmissible confessions made dur
 ing periods of detention that violat[e] the prompt presentment re
 quirement of [Federal Rule of Criminal Procedure] 5(a).” United
 States v. Alvarez-Sanchez, 511 U. S. 350, 354. Rule 5(a), in turn, pro
 vides that a “person making an arrest . . . must take the defendant
 without unnecessary delay before a magistrate judge . . . .” Congress
 enacted 18 U. S. C. §3501 in response to Miranda v. Arizona, 384
 U. S. 436, and some applications of the McNabb-Mallory rule. In an
 attempt to eliminate Miranda, §3501(a) provides that “a confession
 . . . shall be admissible in evidence if it is voluntarily given,” and
 §3501(b) lists several considerations for courts to address in assess
 ing voluntariness. Subsection (c), which focuses on McNabb-Mallory,
 provides that “a confession made . . . by . . . a defendant . . . , while
 . . . under arrest . . . , shall not be inadmissible solely because of delay
 in bringing such person before a magistrate judge . . . if such confes
 sion is found by the trial judge to have been made voluntarily and . . .
 within six hours [of arrest]”; it extends that time limit when further
 delay is “reasonable considering the means of transportation and the
 distance to . . . the nearest available [magistrate].”
     Petitioner Corley was arrested for assaulting a federal officer at
 about 8 a.m. Around 11:45 FBI agents took him to a Philadelphia
 hospital to treat a minor injury. At 3:30 p.m. he was taken from the
 hospital to the local FBI office and told that he was a suspect in a
 bank robbery. Though the office was in the same building as the
 nearest magistrate judges, the agents did not bring him before a
 magistrate judge, but questioned him, hoping for a confession. At
 5:27 p.m., some 9.5 hours after his arrest, Corley began an oral con
2                      CORLEY v. UNITED STATES

                                  Syllabus

    fession that he robbed the bank. He asked for a break at 6:30 and
    was held overnight. The interrogation resumed the next morning,
    ending with his signed written confession. He was finally presented
    to a Magistrate Judge at 1:30 p.m., 29.5 hours after his arrest, and
    charged with armed bank robbery and related charges. The District
    Court denied his motion to suppress his confessions under Rule 5(a)
    and McNabb-Mallory. It reasoned that the oral confession occurred
    within §3501(c)’s six-hour window because the time of Corley’s medi
    cal treatment should be excluded from the delay. It also found the
    written confession admissible, explaining there was no unreasonable
    delay under Rule 5(a) because Corley had requested the break. He
    was convicted of conspiracy and bank robbery. The Third Circuit af
    firmed. Relying on Circuit precedent to the effect that §3501 abro
    gated McNabb-Mallory and replaced it with a pure voluntariness
    test, it concluded that if a district court found a confession voluntary
    after considering the points listed in §3501(b), it would be admissible,
    even if the presentment delay was unreasonable.
Held: Section 3501 modified McNabb-Mallory but did not supplant it.
 Pp. 8–18.
    (a) The Government claims that because §3501(a) makes a confes
 sion “admissible” “if it is voluntarily given,” it entirely eliminates
 McNabb-Mallory with its bar to admitting even a voluntary confes
 sion if given during an unreasonable presentment delay. Corley ar
 gues that §3501(a) was only meant to overrule Miranda, and notes
 that only §3501(c) touches on McNabb-Mallory, making the rule in
 applicable to confessions given within six hours of an arrest. He has
 the better argument. Pp. 8–16.
      (1) The Government’s reading renders §3501(c) nonsensical and
 superfluous. If subsection (a) really meant that any voluntary con
 fession was admissible, then subsection (c) would add nothing; if a
 confession was “made voluntarily” it would be admissible, period, and
 never “inadmissible solely because of delay,” even a delay beyond six
 hours. The Government’s reading is thus at odds with the basic in
 terpretive canon that “ ‘[a] statute should be construed [to give effect]
 to all its provisions, so that no part will be inoperative or superfluous,
 void or insignificant.’ ” Hibbs v. Winn, 542 U. S. 88, 101. The Gov
 ernment claims that in providing that a confession “shall not be ad
 missible,” Congress meant that a confession “shall not be [involun
 tary].” Thus read, (c) would specify a bright-line rule applying (a) to
 cases of delay: it would tell courts that delay alone does not make a
 confession involuntary unless the delay exceeds six hours. But
 “ ‘Congress did not write the statute that way.’ ” Russello v. United
 States, 464 U. S. 16, 23. The terms “inadmissible” and “involuntary”
 are not synonymous. Congress used both in (c), and this Court
                   Cite as: 556 U. S. ____ (2009)                     3

                              Syllabus

“would not presume to ascribe this difference to a simple mistake in
draftsmanship.” Ibid. There is also every reason to believe that
Congress used the distinct terms deliberately, specifying two criteria
that must be satisfied to prevent a confession from being “inadmissi
ble solely because of delay”: the confession must be “[1] made volun
tarily and . . . [2] within six hours [of arrest].” Moreover, under the
McNabb-Mallory rule, “inadmissible” and “involuntary” mean differ
ent things. Corley’s position, in contrast, gives effect to both (c) and
(a), by reading (a) as overruling Miranda and (c) as qualifying
McNabb-Mallory.          The Government’s counterargument—that
Corley’s reading would also create a conflict, since (a) makes all vol
untary confessions admissible while (c) would leave some voluntary
confessions inadmissible—falls short. First, (a) is a broad directive
while (c) aims only at McNabb-Mallory, and “a more specific statute
[is] given precedence over a more general one.” Busic v. United
States, 446 U. S. 398, 406. Second, reading (a) to create a conflict
with (c) not only would make (c) superfluous, but would also create
conflicts with so many other Rules of Evidence that the subsection
cannot possibly be given its literal scope. Pp. 8–12.
     (2) The legislative history strongly favors Corley’s reading. The
Government points to nothing in this history supporting its contrary
view. Pp. 13–15.
     (3) The Government’s position would leave the Rule 5 present
ment requirement without teeth, for if there is no McNabb-Mallory
there is no apparent remedy for a presentment delay. The prompt
presentment requirement is not just an administrative nicety. It
dates back to the common law. Under Rule 5, presentment is the
point at which the judge must take several key steps to foreclose
Government overreaching: e.g., informing the defendant of the
charges against him and giving the defendant a chance to consult
with counsel. Without McNabb-Mallory, federal agents would be free
to question suspects for extended periods before bringing them out in
the open, even though “custodial police interrogation, by its very na
ture, isolates and pressures the individual,” Dickerson v. United
States, 530 U. S. 428, 435, inducing people to confess to crimes they
never committed. Pp. 15–16.
   (b) There is no merit to the Government’s fallback claim that even
if §3501 preserved a limited version of McNabb-Mallory, Congress cut
it out by enacting Federal Rule of Evidence 402, which provides that
“[a]ll relevant evidence is admissible, except as otherwise provided by
the Constitution of the United States, by Act of Congress, by these
rules, or by other rules prescribed by the Supreme Court . . . .” The
Advisory Committee’s Notes expressly identified McNabb-Mallory as
a statutorily authorized rule that would survive Rule 402, and the
4                    CORLEY v. UNITED STATES

                               Syllabus

    Government has previously conceded before this Court that Rule 402
    preserved McNabb-Mallory. Pp. 16–18.
500 F. 3d 210, vacated and remanded.

   SOUTER, J., delivered the opinion of the Court, in which STEVENS,
KENNEDY, GINSBURG, and BREYER, JJ., joined. ALITO, J., filed a dissent
ing opinion, in which ROBERTS, C. J., and SCALIA and THOMAS, JJ.,
joined.
                       Cite as: 556 U. S. ____ (2009)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                 No. 07–10441
                                  _________________


     JOHNNIE CORLEY, PETITIONER v. UNITED 

                  STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE THIRD CIRCUIT

                                [April 6, 2009]


  JUSTICE SOUTER delivered the opinion of the Court.
  The question here is whether Congress intended 18
U. S. C. §3501 to discard, or merely to narrow, the rule in
McNabb v. United States, 318 U. S. 332 (1943), and Mal
lory v. United States, 354 U. S. 449 (1957), under which an
arrested person’s confession is inadmissible if given after
an unreasonable delay in bringing him before a judge. We
hold that Congress meant to limit, not eliminate, McNabb-
Mallory.
                             I

                             A

   The common law obliged an arresting officer to bring his
prisoner before a magistrate as soon as he reasonably
could. See County of Riverside v. McLaughlin, 500 U. S.
44, 61–62 (1991) (SCALIA, J., dissenting). This “present
ment” requirement tended to prevent secret detention and
served to inform a suspect of the charges against him, and
it was the law in nearly every American State and the
National Government. See id., at 60–61; McNabb, supra,
at 342, and n. 7.
   McNabb v. United States raised the question of how to
2                CORLEY v. UNITED STATES

                      Opinion of the Court

enforce a number of federal statutes codifying the pre
sentment rule. 318 U. S., at 342 (citing, among others, 18
U. S. C. §595 (1940 ed.), which provided that “ ‘[i]t shall be
the duty of the marshal . . . who may arrest a person . . . to
take the defendant before the nearest . . . judicial officer
. . . for a hearing’ ”). There, federal agents flouted the
requirement by interrogating several murder suspects for
days before bringing them before a magistrate, and then
only after they had given the confessions that convicted
them. 318 U. S., at 334–338, 344–345.
    On the defendants’ motions to exclude the confessions
from evidence, we saw no need to reach any constitutional
issue. Instead we invoked the supervisory power to estab
lish and maintain “civilized standards of procedure and
evidence” in federal courts, id., at 340, which we exercised
for the sake of making good on the traditional obligation
embodied in the federal presentment legislation. We saw
both the statutes and the traditional rule as aimed not
only at checking the likelihood of resort to the third degree
but meant generally to “avoid all the evil implications of
secret interrogation of persons accused of crime.” Id., at
344. We acknowledged that “Congress ha[d] not explicitly
forbidden the use of evidence . . . procured” in derogation
of the presentment obligation, id., at 345, but we realized
that “permit[ting] such evidence to be made the basis of a
conviction in the federal courts would stultify the policy
which Congress ha[d] enacted into law,” ibid., and in the
exercise of supervisory authority we held confessions
inadmissible when obtained during unreasonable pre
sentment delay.
    Shortly after McNabb, the combined action of the Judi
cial Conference of the United States and Congress pro
duced Federal Rule of Criminal Procedure 5(a), which
pulled the several statutory presentment provisions to
gether in one place. See Mallory, supra, at 452 (describing
Rule 5(a) as “a compendious restatement, without sub
                 Cite as: 556 U. S. ____ (2009)           3

                     Opinion of the Court

stantive change, of several prior specific federal statutory
provisions”). As first enacted, the rule told “[a]n officer
making an arrest under a warrant issued upon a com
plaint or any person making an arrest without a warrant
[to] take the arrested person without unnecessary delay
before the nearest available commissioner or before any
other nearby officer empowered to commit persons
charged with offenses against the laws of the United
States.” Fed. Rule Crim. Proc. 5(a) (1946). The rule re
mains much the same today: “A person making an arrest
within the United States must take the defendant without
unnecessary delay before a magistrate judge . . . .” Fed.
Rule Crim. Proc. 5(a)(1)(A) (2007).
   A case for applying McNabb and Rule 5(a) together soon
arose in Upshaw v. United States, 335 U. S. 410 (1948).
Despite the Government’s confession of error, the D. C.
Circuit had thought McNabb’s exclusionary rule applied
only to involuntary confessions obtained by coercion dur
ing the period of delay, 335 U. S., at 411–412, and so held
the defendant’s voluntary confession admissible into evi
dence. This was error, and we reiterated the reasoning of
a few years earlier. “In the McNabb case we held that the
plain purpose of the requirement that prisoners should
promptly be taken before committing magistrates was to
check resort by officers to ‘secret interrogation of persons
accused of crime.’ ” Id., at 412 (quoting McNabb, supra, at
344). Upshaw consequently emphasized that even volun
tary confessions are inadmissible if given after an unrea
sonable delay in presentment. 335 U. S., at 413.
   We applied Rule 5(a) again in Mallory v. United States,
holding a confession given seven hours after arrest inad
missible for “unnecessary delay” in presenting the suspect
to a magistrate, where the police questioned the suspect
for hours “within the vicinity of numerous committing
magistrates.” 354 U. S., at 455. Again, we repeated the
reasons for the rule and explained, as we had before and
4                    CORLEY v. UNITED STATES

                          Opinion of the Court

have since, that delay for the purpose of interrogation is
the epitome of “unnecessary delay.” Id., at 455–456; see
also McLaughlin, 500 U. S., at 61 (SCALIA, J., dissenting)
(“It was clear” at common law “that the only element
bearing upon the reasonableness of delay was not such
circumstances as the pressing need to conduct further
investigation, but the arresting officer’s ability, once the
prisoner had been secured, to reach a magistrate”); Up
shaw, supra, at 414. Thus, the rule known simply as
McNabb-Mallory “generally render[s] inadmissible confes
sions made during periods of detention that violat[e] the
prompt presentment requirement of Rule 5(a).” United
States v. Alvarez-Sanchez, 511 U. S. 350, 354 (1994).
   There the law remained until 1968, when Congress
enacted 18 U. S. C. §3501 in response to Miranda v. Ari
zona, 384 U. S. 436 (1966), and to the application of
McNabb-Mallory in some federal courts. Subsections (a)
and (b) of §3501 were meant to eliminate Miranda.1 See
Dickerson v. United States, 530 U. S. 428, 435–437 (2000);
infra, at 13–14. Subsection (a) provides that “[i]n any
criminal prosecution brought by the United States . . . , a
confession . . . shall be admissible in evidence if it is volun
tarily given,” while subsection (b) lists several considera
tions for courts to address in assessing voluntariness.2
——————
   1 We rejected this attempt to overrule Miranda in Dickerson v. United

States, 530 U. S. 428 (2000).
   2 In full, subsections (a) and (b) provide:

   “(a) In any criminal prosecution brought by the United States or by
the District of Columbia, a confession, as defined in subsection (e)
hereof, shall be admissible in evidence if it is voluntarily given. Before
such confession is received in evidence, the trial judge shall, out of the
presence of the jury, determine any issue as to voluntariness. If the
trial judge determines that the confession was voluntarily made it shall
be admitted in evidence and the trial judge shall permit the jury to
hear relevant evidence on the issue of voluntariness and shall instruct
the jury to give such weight to the confession as the jury feels it de
serves under all the circumstances.
                    Cite as: 556 U. S. ____ (2009)                   5

                         Opinion of the Court

Subsection (c), which focused on McNabb-Mallory, see
infra, at 13–14, provides that in any federal prosecution,
“a confession made . . . by . . . a defendant therein, while
such person was under arrest . . . , shall not be inadmissi
ble solely because of delay in bringing such person before a
magistrate judge . . . if such confession is found by the
trial judge to have been made voluntarily . . . and if such
confession was made . . . within six hours [of arrest]”;
the six-hour time limit is extended when further delay
is “reasonable considering the means of transportation
and the distance to be traveled to the nearest available
[magistrate].”3
——————
   “(b) The trial judge in determining the issue of voluntariness shall
take into consideration all the circumstances surrounding the giving of
the confession, including (1) the time elapsing between arrest and
arraignment of the defendant making the confession, if it was made
after arrest and before arraignment, (2) whether such defendant knew
the nature of the offense with which he was charged or of which he was
suspected at the time of making the confession, (3) whether or not such
defendant was advised or knew that he was not required to make any
statement and that any such statement could be used against him, (4)
whether or not such defendant had been advised prior to questioning of
his right to the assistance of counsel; and (5) whether or not such
defendant was without the assistance of counsel when questioned and
when giving such confession.
   “The presence or absence of any of the above-mentioned factors to be
taken into consideration by the judge need not be conclusive on the
issue of voluntariness of the confession.”
   3 In full, subsection (c) provides:

   “In any criminal prosecution by the United States or by the District
of Columbia, a confession made or given by a person who is a defendant
therein, while such person was under arrest or other detention in the
custody of any law-enforcement officer or law-enforcement agency, shall
not be inadmissible solely because of delay in bringing such person
before a magistrate judge or other officer empowered to commit persons
charged with offenses against the laws of the United States or of the
District of Columbia if such confession is found by the trial judge to
have been made voluntarily and if the weight to be given the confession
is left to the jury and if such confession was made or given by such
person within six hours immediately following his arrest or other
6                   CORLEY v. UNITED STATES

                         Opinion of the Court

  The issue in this case is whether Congress intended
§3501(a) to sweep McNabb-Mallory’s exclusionary rule
aside entirely, or merely meant §3501(c) to provide immu
nization to voluntary confessions given within six hours of
a suspect’s arrest.
                              B
  Petitioner Johnnie Corley was suspected of robbing a
bank in Norristown, Pennsylvania. After federal agents
learned that Corley was subject to arrest on an unrelated
local matter, some federal and state officers went together
to execute the state warrant on September 17, 2003, and
found him just as he was pulling out of a driveway in his
car. Corley nearly ran over one officer, then jumped out of
the car, pushed the officer down, and ran. The agents
gave chase and caught and arrested him for assaulting a
federal officer. The arrest occurred about 8 a.m. 500 F. 3d
210, 212 (CA3 2007).
  FBI agents first kept Corley at a local police station
while they questioned residents near the place he was
captured. Around 11:45 a.m. they took him to a Philadel
phia hospital to treat a minor cut on his hand that he got
during the chase. At 3:30 p.m. the agents took him from
the hospital to the Philadelphia FBI office and told him
that he was a suspect in the Norristown bank robbery.
Though the office was in the same building as the cham
bers of the nearest magistrate judges, the agents did not
bring Corley before a magistrate, but questioned him
instead, in hopes of getting a confession. App. 68–69, 83,
138–139.
——————
detention: Provided, That the time limitation contained in this subsec
tion shall not apply in any case in which the delay in bringing such
person before such magistrate judge or other officer beyond such six
hour period is found by the trial judge to be reasonable considering the
means of transportation and the distance to be traveled to the nearest
available such magistrate judge or other officer.”
                 Cite as: 556 U. S. ____ (2009)          7

                     Opinion of the Court

   The agents’ repeated arguments sold Corley on the
benefits of cooperating with the Government, and he
signed a form waiving his Miranda rights. At 5:27 p.m.,
some 9.5 hours after his arrest, Corley began an oral
confession that he robbed the bank, id., at 62, and spoke
on in this vein until about 6:30, when agents asked him to
put it all in writing. Corley said he was tired and wanted
a break, so the agents decided to hold him overnight and
take the written statement the next morning. At 10:30
a.m. on September 18 they began the interrogation again,
which ended when Corley signed a written confession. He
was finally presented to a magistrate at 1:30 p.m. that
day, 29.5 hours after his arrest. 500 F. 3d, at 212.
   Corley was charged with armed bank robbery, 18
U. S. C. §2113(a), (d), conspiracy to commit armed bank
robbery, §371, and using a firearm in furtherance of a
crime of violence, §924(c). When he moved to suppress his
oral and written confessions under Rule 5(a) and McNabb-
Mallory, the District Court denied the motion, with the
explanation that the time Corley was receiving medical
treatment should be excluded from the delay, and that the
oral confession was thus given within the six-hour window
of §3501(c). Crim. No. 03–775 (ED Pa., May 10, 2004),
App. 97. The District Court also held Corley’s written
confession admissible, reasoning that “a break from inter
rogation requested by an arrestee who has already begun
his confession does not constitute unreasonable delay
under Rule 5(a).” Id., at 97–98. Corley was convicted of
conspiracy and armed robbery but acquitted of using a
firearm during a crime of violence. 500 F. 3d, at 212–213.
   A divided panel of the Court of Appeals for the Third
Circuit affirmed the conviction, though its rationale for
rejecting Corley’s Rule 5(a) argument was different from
the District Court’s. The panel majority considered itself
bound by Circuit precedent to the effect that §3501 en
tirely abrogated the McNabb-Mallory rule and replaced it
8                   CORLEY v. UNITED STATES

                          Opinion of the Court

with a pure voluntariness test. See 500 F. 3d, at 212
(citing Government of the Virgin Islands v. Gereau, 502
F. 2d 914 (CA3 1974)). As the majority saw it, if a district
court found a confession voluntary after considering the
points listed in §3501(b), it would be admissible, regard
less of whether delay in presentment was unnecessary or
unreasonable. 500 F. 3d, at 217. Judge Sloviter read
Gereau differently and dissented with an opinion that
“§3501 does not displace Rule 5(a)” or abrogate McNabb-
Mallory for presentment delays beyond six hours. 500
F. 3d, at 236.
   We granted certiorari to resolve a division in the Circuit
Courts on the reach of §3501. 554 U. S. ___ (2008). Com
pare United States v. Glover, 104 F. 3d 1570, 1583 (CA10
1997) (§3501 entirely supplanted McNabb-Mallory);
United States v. Christopher, 956 F. 2d 536, 538–539 (CA6
1991) (same), with United States v. Mansoori, 304 F. 3d
635, 660 (CA7 2002) (§3501 limited the McNabb-Mallory
rule to periods more than six hours after arrest); United
States v. Perez, 733 F. 2d 1026, 1031–1032 (CA2 1984)
(same).4 We now vacate and remand.
                              II
  The Government’s argument focuses on §3501(a), which
provides that any confession “shall be admissible in evi
dence” in federal court “if it is voluntarily given.” To the
Government, subsection (a) means that once a district
court looks to the considerations in §3501(b) and finds a
confession voluntary, in it comes; (a) entirely eliminates
McNabb-Mallory with its bar to admitting even a volun
tary confession if given during an unreasonable delay in
presentment.
  Corley argues that §3501(a) was meant to overrule
——————
  4 We granted certiorari to resolve this question once before, in United

States v. Alvarez-Sanchez, 511 U. S. 350 (1994), but ultimately resolved
that case on a different ground, id., at 355–360.
                     Cite as: 556 U. S. ____ (2009)                   9

                         Opinion of the Court

Miranda and nothing more, with no effect on McNabb-
Mallory, which §3501 touches only in subsection (c). By
providing that a confession “shall not be inadmissible
solely because of delay” in presentment if “made voluntar
ily and . . . within six hours [of arrest],” subsection (c)
leaves McNabb-Mallory inapplicable to confessions given
within the six hours, but when a confession comes even
later, the exclusionary rule applies and courts have to see
whether the delay was unnecessary or unreasonable.
   Corley has the better argument.
                                 A
  The fundamental problem with the Government’s read
ing of §3501 is that it renders §3501(c) nonsensical and
superfluous. Subsection (c) provides that a confession
“shall not be inadmissible solely because of delay” in pre
sentment if the confession is “made voluntarily and . . .
within six hours [of arrest].” If (a) really meant that any
voluntary confession was admissible, as the Government
contends, then (c) would add nothing; if a confession was
“made voluntarily” it would be admissible, period, and
never “inadmissible solely because of delay,” no matter
whether the delay went beyond six hours. There is no way
out of this, and the Government concedes it. Tr. of Oral
Arg. 33 (“Congress never needed (c); (c) in the [G]overn
ment’s view was always superfluous”).
  The Government’s reading is thus at odds with one of
the most basic interpretive canons, that “ ‘[a] statute
should be construed so that effect is given to all its provi
sions, so that no part will be inoperative or superfluous,
void or insignificant . . . .’ ” Hibbs v. Winn, 542 U. S. 88,
101 (2004) (quoting 2A N. Singer, Statutes and Statutory
Construction §46.06, pp.181–186 (rev. 6th ed. 2000)).5 The
——————
  5 The dissent says that the antisuperfluousness canon has no place

here because “there is nothing ambiguous about the language of
§3501(a).” Post, at 2 (opinion of ALITO, J.). But this response violates
10                   CORLEY v. UNITED STATES

                           Opinion of the Court

Government attempts to mitigate its problem by rewriting
(c) into a clarifying, if not strictly necessary, provision:
although Congress wrote that a confession “shall not be
inadmissible solely because of delay” if the confession is
“made voluntarily and . . . within six hours [of arrest],” the
Government tells us that Congress actually meant that a
confession “shall not be [involuntary] solely because of
delay” if the confession is “[otherwise voluntary] and . . .
[made] within six hours [of arrest].” Thus rewritten, (c)
would coexist peacefully (albeit inelegantly) with (a), with
(c) simply specifying a bright-line rule applying (a) to
cases of delay: it would tell courts that delay alone does
not make a confession involuntary unless the delay ex
ceeds six hours.
    To this proposal, “ ‘[t]he short answer is that Congress
did not write the statute that way.’ ” Russello v. United
States, 464 U. S. 16, 23 (1983) (quoting United States v.
Naftalin, 441 U. S. 768, 773 (1979)). The Government
may say that we can sensibly read “inadmissible” as “in
voluntary” because the words are “virtually synonymous
. . . in this statutory context,” Brief for United States 23,
but this is simply not so. To begin with, Congress used

——————
“the cardinal rule that a statute is to be read as a whole,” King v. St.
Vincent’s Hospital, 502 U. S. 215, 221 (1991). Subsection 3501(a) seems
clear only if one ignores the absurd results of a literal reading, infra, at
11–12, and only until one reads §3501(c) and recognizes that if (a)
means what it literally says, (c) serves no purpose. Even the dissent
concedes that when (a) and (c) are read together, “[t]here is simply no
perfect solution to the problem before us.” Post, at 4. Thus, the dis
sent’s point that subsection (a) seems clear when read in isolation
proves nothing, for “[t]he meaning—or ambiguity—of certain words or
phrases may only become evident when placed in context.” FDA v.
Brown & Williamson Tobacco Corp., 529 U. S. 120, 132 (2000). When
subsection (a) is read in context, there is no avoiding the question,
“What could Congress have been getting at with both (a) and (c)?” The
better answer is that Congress meant to do just what Members explic
itly said in the legislative record. See infra, at 13–15.
                  Cite as: 556 U. S. ____ (2009)            11

                      Opinion of the Court

both terms in (c) itself, and “[w]e would not presume to
ascribe this difference to a simple mistake in draftsman
ship.” Russello, supra, at 23. And there is, in fact, every
reason to believe that Congress used the distinct terms
very deliberately. Subsection (c) specifies two criteria that
must be satisfied to prevent a confession from being “in
admissible solely because of delay”: the confession must be
“[1] made voluntarily and . . . [2] within six hours [of
arrest].” Because voluntariness is thus only one of several
criteria for admissibility under (c), “involuntary” and
“inadmissible” plainly cannot be synonymous. What is
more, the Government’s argument ignores the fact that
under the McNabb-Mallory rule, which we presume Con
gress was aware of, Cannon v. University of Chicago, 441
U. S. 677, 699 (1979), “inadmissible” and “involuntary”
mean different things. As we explained before and as the
Government concedes, McNabb-Mallory makes even vol
untary confessions inadmissible if given after an unrea
sonable delay in presentment, Upshaw, 335 U. S., at 413;
Tr. of Oral Arg. 33 (“[I]t was well understood that
McNabb-Mallory . . . excluded totally voluntary confes
sions”). So we cannot accept the Government’s attempt to
confuse the critically distinct terms “involuntary” and
“inadmissible” by rewriting (c) into a bright-line rule doing
nothing more than applying (a).
  Corley’s position, in contrast, gives effect to both (c) and
(a), by reading (a) as overruling Miranda and (c) as quali
fying McNabb-Mallory. The Government answers, how
ever, that accepting Corley’s argument would result in a
different problem: it would create a conflict between (c)
and (a), since (a) provides that all voluntary confessions
are admissible while Corley’s reading of (c) leaves some
voluntary confessions inadmissible. But the Government’s
counterargument falls short for two reasons. First, even if
(a) is read to be at odds with (c), the conflict is resolved by
recognizing that (a) is a broad directive while (c) aims only
12                  CORLEY v. UNITED STATES

                         Opinion of the Court

at McNabb-Mallory, and “a more specific statute will be
given precedence over a more general one . . . .” Busic v.
United States, 446 U. S. 398, 406 (1980). Second, and
more fundamentally, (a) cannot prudently be read to
create a conflict with (c), not only because it would make
(c) superfluous, as explained, but simply because reading
(a) that way would create conflicts with so many other
rules that the subsection cannot possibly be given its
literal scope. Subsection (a) provides that “[i]n any crimi
nal prosecution brought by the United States . . . , a con
fession . . . shall be admissible in evidence if it is voluntar
ily given,” and §3501(e) defines “confession” as “any
confession of guilt of any criminal offense or any self
incriminating statement made or given orally or in writ
ing.” Thus, if the Government seriously urged a literal
reading, (a) would mean that “in any criminal prosecution
brought by the United States . . . , [‘any self-incriminating
statement’ with respect to ‘any criminal offense’] . . . shall
be admissible in evidence if it is voluntarily given.” Thus
would many a Rule of Evidence be overridden in case after
case: a defendant’s self-incriminating statement to his
lawyer would be admissible despite his insistence on
attorney-client privilege; a fourth-hand hearsay statement
the defendant allegedly made would come in; and a defen
dant’s confession to an entirely unrelated crime committed
years earlier would be admissible without more. These
are some of the absurdities of literalism that show that
Congress could not have been writing in a literalistic
frame of mind.6
——————
   6 The dissent seeks to avoid these absurd results by claiming that

“§3501(a) does not supersede ordinary evidence Rules,” post, at 10, but
its only argument for this conclusion is that “there is no reason to
suppose that Congress meant any such thing,” post, at 9. The dissent is
certainly correct that there is no reason to suppose that Congress
meant any such thing; that is what our reductio ad absurdum shows.
But that leaves the dissent saying, “§3501(a) must be read literally”
                      Cite as: 556 U. S. ____ (2009)                    13

                          Opinion of the Court

                               B
  As it turns out, there is more than reductio ad absur
dum and the antisuperfluousness canon to confirm that
subsection (a) leaves McNabb-Mallory alone, for that is
what legislative history says. In fact, the Government
concedes that subsections (a) and (b) were aimed at
Miranda, while subsection (c) was meant to modify the
presentment exclusionary rule. Tr. of Oral Arg. 38 (“I will
concede to you . . . that section (a) was considered to over
rule Miranda, and subsection (c) was addressed to
McNabb-Mallory”). The concession is unavoidable. The
Senate, where §3501 originated, split the provision into
two parts: Division 1 contained subsections (a) and (b),
and Division 2 contained subsection (c). 114 Cong. Rec.
14171 (1968). In the debate on the Senate floor immedi
ately before voting on these proposals, several Senators,
including the section’s prime sponsor, Senator McClellan,
explained that Division 1 “has to do with the Miranda
decision,” while Division 2 related to Mallory. 114 Cong.
Rec. 14171–14172. This distinct intent was confirmed by
the separate Senate votes adopting the two measures,
Division 1 by 55 to 29 and Division 2 by 58 to 26, id., at
14171–14172, 14174–14175; if (a) did abrogate McNabb-
Mallory, as the Government claims, then voting for Divi
sion 2 would have been entirely superfluous, for the Divi
sion 1 vote would already have done the job. That aside, a
sponsor’s statement to the full Senate carries considerable
weight, and Senator McClellan’s explanation that Division
1 was specifically addressed to Miranda confirms that (a)
and (b) were never meant to reach far enough to abrogate
——————
(rendering §3501(c) superfluous), “but not too literally” (so that it would
override other Rules of Evidence). The dissent cannot have it both
ways. If it means to profess literalism it will have to take the absurdity
that literalism brings with it; “credo quia absurdum” (as Tertullian
may have said). If it will not take the absurd, then its literalism is no
alternative to our reading of the statute.
14                  CORLEY v. UNITED STATES

                          Opinion of the Court

other background evidentiary rules including McNabb-
Mallory.
   Further legislative history not only drives that point
home, but conclusively shows an intent that subsection (c)
limit McNabb-Mallory, not replace it. In its original draft,
subsection (c) would indeed have done away with McNabb-
Mallory completely, for the bill as first written would have
provided that “[i]n any criminal prosecution by the United
States . . . , a confession made or given by a person who is
a defendant therein . . . shall not be inadmissible solely
because of delay in bringing such person before a [magis
trate] if such confession is . . . made voluntarily.” S. 917,
90th Cong., 2d Sess., 44–45 (1968) (as reported by Senate
Committee on the Judiciary); 114 Cong. Rec. 14172. The
provision so conceived was resisted, however, by a number
of Senators worried about allowing indefinite presentment
delays. See, e.g., id., at 11740, 13990 (Sen. Tydings) (the
provision would “permit Federal criminal suspects to be
questioned indefinitely before they are presented to a
committing magistrate”); id., at 12290 (Sen. Fong) (the
provision “would open the doors to such practices as hold
ing suspects incommunicado for an indefinite period”).
After Senator Tydings proposed striking (c) from the bill
altogether, id., at 13651 (Amendment No. 788), Senator
Scott introduced the compromise of qualifying (c) with the
words: “ ‘and if such confession was made or given by such
person within six hours following his arrest or other de
tention.’ ” Id., at 14184–14185 (Amendment No. 805).7
The amendment was intended to confine McNabb-Mallory
to excluding only confessions given after more than six
hours of delay, see 114 Cong. Rec. 14184 (remarks of Sen.
Scott) (“My amendment provides that the period during
——————
  7 The proviso at the end of (c) relating to reasonable delays caused by

the means of transportation and distance to be traveled came later by
separate amendment. 114 Cong. Rec. 14787.
                 Cite as: 556 U. S. ____ (2009)           15

                     Opinion of the Court

which confessions may be received . . . shall in no case
exceed 6 hours”), and it was explicitly modeled on the
provision Congress had passed just months earlier to
govern presentment practice in the District of Columbia,
Title III of An Act Relating to Crime and Criminal Proce
dure in the District of Columbia (D. C. Crime Act),
§301(b), 81 Stat. 735–736, see, e.g., 114 Cong. Rec. 14184
(remarks of Sen. Scott) (“My amendment is an attempt to
conform, as nearly as practicable, to Title III of [the D. C.
Crime Act]”). By the terms of that Act, “[a]ny statement,
admission, or confession made by an arrested person
within three hours immediately following his arrest shall
not be excluded from evidence in the courts of the District
of Columbia solely because of delay in presentment.”
§301(b), 81 Stat. 735–736. Given the clear intent that
Title III modify but not eliminate McNabb-Mallory in the
District of Columbia, see, e.g., S. Rep. No. 912, 90th Cong.,
1st Sess., 17–18 (1967), using it as a model plainly shows
how Congress meant as much but no more in §3501(c).
  In sum, the legislative history strongly favors Corley’s
reading. The Government points to nothing in this history
supporting its view that (c) created a bright-line rule for
applying (a) in cases with a presentment issue.
                              C
   It also counts heavily against the position of the United
States that it would leave the Rule 5 presentment re
quirement without any teeth, for as the Government again
is forced to admit, if there is no McNabb-Mallory there is
no apparent remedy for delay in presentment. Tr. of Oral
Arg. 25. One might not care if the prompt presentment
requirement were just some administrative nicety, but in
fact the rule has always mattered in very practical ways
and still does. As we said, it stretches back to the common
law, when it was “one of the most important” protections
“against unlawful arrest.” McLaughlin, 500 U. S., at 60–
16                CORLEY v. UNITED STATES

                      Opinion of the Court

61 (SCALIA, J., dissenting). Today presentment is the
point at which the judge is required to take several key
steps to foreclose Government overreaching: informing the
defendant of the charges against him, his right to remain
silent, his right to counsel, the availability of bail, and any
right to a preliminary hearing; giving the defendant a
chance to consult with counsel; and deciding between
detention or release. Fed. Rule Crim. Proc. 5(d); see also
Rule 58(b)(2).
   In a world without McNabb-Mallory, federal agents
would be free to question suspects for extended periods
before bringing them out in the open, and we have always
known what custodial secrecy leads to. See McNabb, 318
U. S. 332. No one with any smattering of the history of
20th-century dictatorships needs a lecture on the subject,
and we understand the need even within our own system
to take care against going too far. “[C]ustodial police
interrogation, by its very nature, isolates and pressures
the individual,” Dickerson, 530 U. S., at 435, and there is
mounting empirical evidence that these pressures can
induce a frighteningly high percentage of people to confess
to crimes they never committed, see, e.g., Drizin & Leo,
The Problem of False Confessions in the Post-DNA World,
82 N. C. L. Rev. 891, 906–907 (2004).
   Justice Frankfurter’s point in McNabb is as fresh as
ever: “The history of liberty has largely been the history of
observance of procedural safeguards.” 318 U. S., at 347.
McNabb-Mallory is one of them, and neither the text nor
the history of §3501 makes out a case that Congress
meant to do away with it.
                           III
  The Government’s fallback claim is that even if §3501
preserved a limited version of McNabb-Mallory, Congress
cut out the rule altogether by enacting Federal Rule of
Evidence 402 in 1975. Act of Jan. 2, Pub. L. 93–595, 88
                  Cite as: 556 U. S. ____ (2009)           17

                      Opinion of the Court

Stat. 1926. So far as it might matter here, that rule pro
vides that “[a]ll relevant evidence is admissible, except as
otherwise provided by the Constitution of the United
States, by Act of Congress, by these rules, or by other
rules prescribed by the Supreme Court pursuant to statu
tory authority.” The Government says that McNabb-
Mallory excludes relevant evidence in a way not “other
wise provided by” any of these four authorities, and so has
fallen to the scythe.
   The Government never raised this argument in the
Third Circuit or the District Court, which would justify
refusing to consider it here, but in any event it has no
merit. The Advisory Committee’s Notes on Rule 402,
which were before Congress when it enacted the Rules of
Evidence and which we have relied on in the past to inter
pret the rules, Tome v. United States, 513 U. S. 150, 160
(1995) (plurality opinion), expressly identified McNabb-
Mallory as a statutorily authorized rule that would sur
vive Rule 402: “The Rules of Civil and Criminal Procedure
in some instances require the exclusion of relevant evi
dence. For example, . . . the effective enforcement of . . .
Rule 5(a) . . . is held to require the exclusion of statements
elicited during detention in violation thereof.” 28 U. S. C.
App., pp. 325–326 (citing Mallory, 354 U. S. 449, and 18
U. S. C. §3501(c)); see also Mallory, supra, at 451 (“Th[is]
case calls for a proper application of Rule 5(a) of the Fed
eral Rules of Criminal Procedure . . .”). Indeed, the Gov
ernment has previously conceded before this Court that
Rule 402 preserved McNabb-Mallory. Brief for United
States in United States v. Payner, O. T. 1979, No. 78–
1729, p. 32, and n. 13 (1979) (saying that Rule 402 “left to
the courts . . . questions concerning the propriety of ex
cluding relevant evidence as a method of implementing
the Constitution, a federal statute, or a statutorily author
ized rule,” and citing McNabb-Mallory as an example).
The Government was right the first time, and it would be
18               CORLEY v. UNITED STATES

                     Opinion of the Court

bizarre to hold that Congress adopted Rule 402 with a
purpose exactly opposite to what the Advisory Committee
Notes said the rule would do.
                              IV
   We hold that §3501 modified McNabb-Mallory without
supplanting it. Under the rule as revised by §3501(c), a
district court with a suppression claim must find whether
the defendant confessed within six hours of arrest (unless
a longer delay was “reasonable considering the means of
transportation and the distance to be traveled to the near
est available [magistrate]”). If the confession came within
that period, it is admissible, subject to the other Rules of
Evidence, so long as it was “made voluntarily and . . . the
weight to be given [it] is left to the jury.” Ibid. If the
confession occurred before presentment and beyond six
hours, however, the court must decide whether delaying
that long was unreasonable or unnecessary under the
McNabb-Mallory cases, and if it was, the confession is to
be suppressed.
   In this case, the Third Circuit did not apply this rule
and in consequence never conclusively determined
whether Corley’s oral confession “should be treated as
having been made within six hours of arrest,” as the Dis
trict Court held. 500 F. 3d, at 220, n. 7. Nor did the Cir
cuit consider the justifiability of any delay beyond six
hours if the oral confession should be treated as given
outside the six-hour window; and it did not make this
enquiry with respect to Corley’s written confession. We
therefore vacate the judgment of the Court of Appeals and
remand the case for consideration of those issues in the
first instance, consistent with this opinion.

                                            It is so ordered.
                      Cite as: 556 U. S. ____ (2009)         1

                           ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
                               _________________

                              No. 07–10441
                               _________________


     JOHNNIE CORLEY, PETITIONER v. UNITED 

                  STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE THIRD CIRCUIT

                              [April 6, 2009]


   JUSTICE ALITO, with whom THE CHIEF JUSTICE, JUSTICE
SCALIA, and JUSTICE THOMAS join, dissenting.
   Section 3501(a) of Title 18, United States Code, directly
and unequivocally answers the question presented in this
case. After petitioner was arrested by federal agents, he
twice waived his Miranda1 rights and voluntarily con
fessed, first orally and later in writing, that he had par
ticipated in an armed bank robbery. He was then taken
before a Magistrate Judge for an initial appearance. The
question that we must decide is whether this voluntary
confession may be suppressed on the ground that there
was unnecessary delay in bringing petitioner before the
Magistrate Judge. Unless the unambiguous language of
§3501(a) is ignored, petitioner’s confession may not be
suppressed.
                               I
  Section 3501(a) states: “In any criminal prosecution
brought by the United States . . ., a confession . . . shall be
admissible in evidence if it is voluntarily given.”
  Applying “settled principles of statutory construction,”
“we must first determine whether the statutory text is
plain and unambiguous,” and “[i]f it is, we must apply the

——————
 1 See   Miranda v. Arizona, 384 U. S. 436 (1966).
2                  CORLEY v. UNITED STATES

                        ALITO, J., dissenting

statute according to its terms.” Carcieri v. Salazar, 555
U. S. ___, ___ (2009) (slip op., at 7). Here, there is nothing
ambiguous about the language of §3501(a), and the Court
does not claim otherwise. Although we normally presume
that Congress “means in a statute what it says there,”
Connecticut Nat. Bank v. Germain, 503 U. S. 249, 253–254
(1992), the Court today concludes that §3501(a) does not
mean what it says and that a voluntary confession may be
suppressed under the McNabb-Mallory rule.2 This super
visory rule, which requires the suppression of a confession
where there was unnecessary delay in bringing a federal
criminal defendant before a judicial officer after arrest,
was announced long before 18 U. S. C. §3501(a) was
adopted. According to the Court, this rule survived the
enactment of §3501(a) because Congress adopted that
provision for the sole purpose of abrogating Miranda and
apparently never realized that the provision’s broad lan
guage would also do away with the McNabb-Mallory rule.
I disagree with the Court’s analysis and therefore respect
fully dissent.
                             II 

                             A

  The Court’s first and most substantial argument in
vokes “the antisuperfluousness canon,” ante, at 12, under
which a statute should be read, if possible, so that all of its
provisions are given effect and none is superfluous. Ante,
at 9–12. Section 3501(c) provides that a voluntary confes
sion “shall not be inadmissible solely because of the delay”
in bringing the defendant before a judicial officer if the
defendant is brought before a judicial officer within six
hours of arrest. If §3501(a) means that a voluntary con
fession may never be excluded due to delay in bringing the

——————
 2 See McNabb v. United States, 318 U. S. 332 (1943), and Mallory v.

United States, 354 U. S. 449 (1957).
                 Cite as: 556 U. S. ____ (2009)           3

                     ALITO, J., dissenting

defendant before a judicial officer, the Court reasons, then
§3501(c), which provides a safe harbor for a subset of
voluntary confessions (those made in cases in which the
initial appearance occurs within six hours of arrest), is
superfluous.
   Canons of interpretation “are quite often useful in close
cases, or when statutory language is ambiguous. But we
have observed before that such ‘interpretative canon[s are]
not a license for the judiciary to rewrite language enacted
by the legislature.’ ” United States v. Monsanto, 491 U. S.
600, 611 (1989) (quoting United States v. Albertini, 472
U. S. 675, 680 (1985)). Like other canons, the antisuper
fluousness canon is merely an interpretive aid, not an
absolute rule. See Connecticut Nat. Bank, 503 U. S., at
254 (“When the words of a statute are unambiguous, then,
this first canon is also the last: ‘judicial inquiry is com
plete’ ”). There are times when Congress enacts provisions
that are superfluous, and this may be such an instance.
Cf. id., at 253 (noting that “[r]edundancies across statutes
are not unusual events in drafting”); Gutierrez de Martinez
v. Lamagno, 515 U. S. 417, 445–446 (1995) (SOUTER, J.,
dissenting) (noting that, although Congress “indulged in a
little redundancy,” the “inelegance may be forgiven” be
cause “Congress could sensibly have seen some practical
value in the redundancy”).
   Moreover, any superfluity created by giving subsection
(a) its plain meaning may be minimized by interpreting
subsection (c) to apply to confessions that are otherwise
voluntary.     The Government contends that §3501(c),
though inartfully drafted, is not superfluous because what
the provision means is that a confession is admissible if it
is given within six hours of arrest and it is otherwise vol
untary—that is, if there is no basis other than prepre
sentment delay for concluding that the confession was
coerced. Read in this way, §3501(c) is not superfluous.
   The Court rejects this argument on the ground that
4                 CORLEY v. UNITED STATES

                      ALITO, J., dissenting

“ ‘Congress did not write the statute that way,’ ” ante, at
10, and thus, in order to adhere to a narrow reading of
§3501(c), the Court entirely disregards the unambiguous
language of §3501(a). Although §3501(a) says that a
confession is admissible if it is “voluntarily given,” the
Court reads that provision to mean that a voluntary con
fession may not be excluded on the ground that the confes
sion was obtained in violation of Miranda. To this read
ing, the short answer is that Congress really did not write
the statute that way.
   As is true with most of the statutory interpretation
questions that come before this Court, the question in this
case is not like a jigsaw puzzle. There is simply no perfect
solution to the problem before us.
   Instead, we must choose between two imperfect solu
tions. The first (the one adopted by the Court) entirely
disregards the clear and simple language of §3501(a), rests
on the proposition that Congress did not understand the
plain import of the language it used in subsection (a), but
adheres to a strictly literal interpretation of §3501(c). The
second option respects the clear language of subsection (a),
but either accepts some statutory surplusage or interprets
§3501(c)’s reference to a voluntary confession to mean an
otherwise voluntary confession. To my mind, the latter
choice is far preferable.
                              B
  In addition to the antisuperfluousness canon, the Court
relies on the canon that favors a specific statutory provi
sion over a conflicting provision cast in more general
terms, ante, at 11, but that canon is inapplicable here. For
one thing, §3501(a) is quite specific; it specifically provides
that if a confession is voluntary, it is admissible. More
important, there is no other provision, specific or general,
that conflicts with §3501(a). See National Cable & Tele
communications Assn., Inc. v. Gulf Power Co., 534 U. S.
                 Cite as: 556 U. S. ____ (2009)           5

                     ALITO, J., dissenting

327, 335–336 (2002) (“It is true that specific statutory
language should control more general language when there
is a conflict between the two. Here, however, there is no
conflict” (emphasis added)). Subsection (c) is not conflict
ing because it does not authorize the suppression of any
voluntary confession. What the Court identifies is not a
conflict between two statutory provisions but a conflict
between the express language of one provision (§3501(a))
and the “negative implication” that the Court draws from
another (§3501(c)). United States v. Alvarez-Sanchez, 511
U. S. 350, 355 (1994). Because §3501(c) precludes the
suppression of a voluntary confession based solely on a
delay of less than six hours, the Court infers that Con
gress must have contemplated that a voluntary confession
could be suppressed based solely on a delay of more than
six hours. The Court cites no authority for a canon of
interpretation that favors a “negative implication” of this
sort over clear and express statutory language.
                               C
   The Court contends that a literal interpretation of
§3501(a) would leave the prompt presentment require
ment set out in Federal Rule of Criminal Procedure 5(a)(1)
“without any teeth, for . . . if there is no McNabb-Mallory
there is no apparent remedy for delay in presentment.”
Ante, at 15. There is nothing strange, however, about a
prompt presentment requirement that is not enforced by a
rule excluding voluntary confessions made during a period
of excessive prepresentment delay. As the Court notes,
“[t]he common law obliged an arresting officer to bring his
prisoner before a magistrate as soon as he reasonably
could,” ante, at 1, but the McNabb-Mallory supervisory
rule was not adopted until the middle of the 20th century.
To this day, while the States are required by the Fourth
Amendment to bring an arrestee promptly before a judi
cial officer, see, e.g., County of Riverside v. McLaughlin,
6                CORLEY v. UNITED STATES

                      ALITO, J., dissenting

500 U. S. 44, 56 (1991), we have never held that this con
stitutional requirement is backed by an automatic exclu
sionary sanction, see, e.g., Hudson v. Michigan, 547 U. S.
586, 592 (2006). And although the prompt presentment
requirement serves interests in addition to the prevention
of coerced confessions, the McNabb-Mallory rule provides
no sanction for excessive prepresentment delay in those
instances in which no confession is sought or obtained.
   Moreover, the need for the McNabb-Mallory exclusion
ary rule is no longer clear. That rule, which was adopted
long before Miranda, originally served a purpose that is
now addressed by the giving of Miranda warnings upon
arrest. As Miranda recognized, McNabb and Mallory
were “responsive to the same considerations of Fifth
Amendment policy” that the Miranda rule was devised to
address. Miranda v. Arizona, 384 U. S. 436, 463 (1966).
   In the pre-Miranda era, the requirement of prompt
presentment ensured that persons taken into custody
would, within a relatively short period, receive advice
about their rights. See McNabb v. United States, 318
U. S. 332, 344 (1943). Now, however, Miranda ensures
that arrestees receive such advice at an even earlier point,
within moments of being taken into custody. Of course,
arrestees, after receiving Miranda warnings, may waive
their rights and submit to questioning by law enforcement
officers, see, e.g., Davis v. United States, 512 U. S. 452,
458 (1994), and arrestees may likewise waive the prompt
presentment requirement, see, e.g., New York v. Hill, 528
U. S. 110, 114 (2000) (“We have . . . ‘in the context of a
broad array of constitutional and statutory provisions,’
articulated a general rule that presumes the availability of
waiver, . . . and we have recognized that ‘the most basic
rights of criminal defendants are . . . subject to waiver’ ”).
It seems unlikely that many arrestees who are willing to
waive the right to remain silent and the right to the assis
tance of counsel during questioning would balk at waiving
                   Cite as: 556 U. S. ____ (2009)                 7

                        ALITO, J., dissenting

the right to prompt presentment. More than a few courts
of appeals have gone as far as to hold that a waiver of
Miranda rights also constitutes a waiver under McNabb-
Mallory. See, e.g., United States v. Salamanca, 990 F. 2d
629, 634 (CADC), cert. denied, 510 U. S. 928 (1993);
United States v. Barlow, 693 F. 2d 954, 959 (CA6 1982),
cert. denied, 461 U. S. 945 (1983); United States v. Indian
Boy X, 565 F. 2d 585, 591 (CA9 1977), cert. denied, 439
U. S. 841 (1978); United States v. Duvall, 537 F. 2d 15, 23–
24, n. 9 (CA2), cert. denied, 426 U. S. 950 (1976); United
States v. Howell, 470 F. 2d 1064, 1067, n. 1 (CA9 1972);
Pettyjohn v. United States, 419 F. 2d 651, 656 (CADC
1969), cert. denied, 397 U. S. 1058 (1970); O’Neal v. United
States, 411 F. 2d 131, 136–137 (CA5), cert. denied, 396
U. S. 827 (1969). Whether or not those decisions are
correct, it is certainly not clear that the McNabb-Mallory
rule adds much protection beyond that provided by
Miranda.
                             D
  The Court contends that the legislative history of §3501
supports its interpretation, but the legislative history
proves nothing that is not evident from the terms of the
statute. With respect to §3501(a), the legislative history
certainly shows that the provision’s chief backers meant to
do away with Miranda,3 but the Court cites no evidence
that this was all that §3501(a) was intended to accom
plish. To the contrary, the Senate Report clearly says that
§3501(a) was meant to reinstate the traditional rule that a

——————
  3 At argument, the Government conceded “that section (a) was con

sidered to overrule Miranda and subsection (c) was addressed to
McNabb-Mallory.” See Tr. of Oral Arg. 38. It is apparent that the
attorney for the Government chose his words carefully and did not
concede, as the Court seems to suggest, that subsection (a) was in
tended to do no more than to overrule Miranda or that subsection (c)
was the only part of §3501 that affected the McNabb-Mallory rule.
8                CORLEY v. UNITED STATES

                     ALITO, J., dissenting

confession should be excluded only if involuntary, see
S. Rep. No. 1097, 90th Cong., 2d Sess., 38 (1968) (Senate
Report), a step that obviously has consequences beyond
the elimination of Miranda. And the Senate Report re
peatedly cited Escobedo v. Illinois, 378 U. S. 478 (1964), as
an example of an unsound limitation on the admission of
voluntary confessions, see Senate Report 41–51, thus
illustrating that §3501(a) was not understood as simply an
anti-Miranda provision. Whether a majority of the Mem
bers of the House and Senate had the McNabb-Mallory
rule specifically in mind when they voted for §3501(a) is
immaterial. Statutory provisions may often have a reach
that is broader than the specific targets that the lawmak
ers might have had in mind at the time of enactment.
   The legislative history relating to §3501(c) suggests
nothing more than that some Members of Congress may
mistakenly have thought that the version of §3501 that
was finally adopted would not displace the McNabb-
Mallory rule. As the Court relates, the version of §3501(c)
that emerged from the Senate Judiciary Committee would
have completely eliminated that rule. See ante, at 12–13.
Some Senators opposed this, and the version of this provi
sion that was eventually passed simply trimmed the rule.
It is possible to identify a few Senators who spoke out in
opposition to the earlier version of subsection (c) and then
voted in favor of the version that eventually passed, and it
is fair to infer that these Senators likely thought that the
amendment of subsection (c) had saved the rule. See 114
Cong. Rec. 14172–14175, 14798 (1968). But there is no
evidence that a majority of the House and Senate shared
that view, and any Member who took a few moments to
read subsections (a) and (c) must readily have understood
that subsection (a) would wipe away all non-constitution
ally based rules barring the admission of voluntary confes
sions, not just Miranda, and that subsection (c) did not
authorize the suppression of any voluntary confessions.
                     Cite as: 556 U. S. ____ (2009)                   9

                         ALITO, J., dissenting

The Court unjustifiably attributes to a majority of the
House and Senate a mistake that, the legislative history
suggests, may have been made by only a few.
                                E
  Finally, the Court argues that under a literal reading of
§3501(a), “many a rule of evidence [would] be overridden
in case after case.” Ante, at 12. In order to avoid this
absurd result, the Court says, it is necessary to read
§3501(a) as merely abrogating Miranda and not
the McNabb-Mallory rule. There is no merit to this
argument.4
  The language that Congress used in §3501(a)—a confes
sion is “admissible” if “voluntarily given”—is virtually a
verbatim quotation of the language used by this Court in
describing the traditional rule regarding the admission of
confessions. See, e.g., Haynes v. Washington, 373 U. S.
503, 513 (1963) (“ ‘ In short, the true test of admissibility is
that the confession is made freely, voluntarily and without
compulsion or inducement of any sort.’ ” (quoting Wilson v.
United States, 162 U. S. 613, 623 (1896))); Lyons v. Okla
homa, 322 U. S. 596, 602 (1944); Ziang Sung Wan v.
United States, 266 U. S. 1, 15 (1924); Bram v. United
States, 168 U. S. 532, 545 (1897). In making these state
ments, this Court certainly did not mean to suggest that a
voluntary confession must be admitted in those instances
in which a standard rule of evidence would preclude ad
mission, and there is no reason to suppose that Congress
meant any such thing either. In any event, the Federal

——————
   4 Contrary to the Court’s suggestion, cases in which one of the stan

dard Rules of Evidence might block the admission of a voluntary
confession would seem quite rare, and the Court cites no real-world
examples. The Court thus justifies its reading of §3501, which totally
disregards the clear language of subsection (a), based on a few essen
tially fanciful hypothetical cases that, in any event, have been covered
since 1975 by the Federal Rules of Evidence.
10               CORLEY v. UNITED STATES

                     ALITO, J., dissenting

Rules of Evidence now make it clear that §3501(a) does
not supersede ordinary evidence Rules, including Rules
regarding privilege (Rule 501), hearsay (Rule 802), and
restrictions on the use of character evidence (Rule 404).
Thus, it is not necessary to disregard the plain language of
§3501(a), as the Court does, in order to avoid the sort of
absurd results to which the Court refers.
  For all these reasons, I would affirm the decision of the
Court of Appeals, and I therefore respectfully dissent.

```

---

## GROUP: content/cases/County of Los Angeles v. Mendez.md  (`case`, 5 assertions)

### content_page

```
---
title: County of Los Angeles v. Mendez
type: case
citation: "581 U.S. 420 (2017)"
parallel_cite: "137 S. Ct. 1539; 198 L. Ed. 2d 52; 26 Fla. L. Weekly Fed. S 604; 85 U.S.L.W. 4292"
neutral_cite: "2017 U.S. LEXIS 3396; 2017 WL 2322832"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2017
date_decided: 2017-05-30
docket: No. 16-369
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
  opinion_url: "https://www.courtlistener.com/opinion/4395246/county-of-los-angeles-v-mendez/"
  cluster_id: 4395246
  opinion_id: null
  identity_checked: true
lake:
  record_id: County of Los Angeles v. Mendez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Use of Force]]"
    role: Anchor
related:
  - "[[Use of Force]]"
  - "[[Graham v. Connor]]"
tags:
  - case
  - fourth-amendment
  - excessive-force
  - provocation-rule
  - graham-v-connor
  - proximate-cause
holding: "The Fourth Amendment provides no basis for the Ninth Circuit's 'provocation rule'; an officer's objectively reasonable use of force cannot be rendered an unreasonable seizure by an earlier, separate Fourth Amendment violation (such as a warrantless entry) that provoked the confrontation, though that distinct violation may support its own claim and proximate-cause damages."
aliases:
  - County of Los Angeles v. Mendez
  - "County of Los Angeles v. Mendez (2017)"
---

# County of Los Angeles v. Mendez

*581 U.S. 420 (2017)* (No. 16-369) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4395246 → lead opinion 4172499 (Alito, J.; 581 U.S. 420, decided May 30, 2017). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text carries S. Ct. star-pagination (parallel 137 S. Ct. 1539), so the pin is to 137 S. Ct. at 1544 (page-label `*1544`) — the official U.S. Reports pagination is not present in the CL text. S9 promotes. -->

## Background
Los Angeles County sheriff's deputies searching for a wanted parolee entered the property where Angel Mendez and Jennifer Garcia were living and, without a warrant and without knocking or announcing, opened the door of a wooden shack in the backyard where the couple was resting. Mendez kept a BB gun to shoot pests; as he rose, he moved the BB gun, and the deputies — seeing the silhouette of what looked like a rifle — opened fire, seriously wounding both Mendez and Garcia. The district court found the shooting itself reasonable under *[[Graham v. Connor]]* but held the deputies liable under the Ninth Circuit's "provocation rule," reasoning that their unconstitutional warrantless entry had provoked the confrontation. The Ninth Circuit affirmed.

## Issue
Whether officers who use force that is objectively reasonable under *[[Graham v. Connor|Graham]]* may nonetheless be held liable for excessive force on the theory that a separate, earlier Fourth Amendment violation provoked the need to use force.

## Rule
The Court rejected the provocation rule root and branch: "We hold that the Fourth Amendment provides no basis for such a rule. A different Fourth Amendment violation cannot transform a later, reasonable use of force into an unreasonable seizure." — 137 S. Ct. at 1544. ^pin-1544

## Application
An excessive-force claim is governed solely by whether the force used was objectively reasonable under *[[Graham v. Connor|Graham]]*, judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] at the moment force is applied. The provocation rule instead conjured an excessive-force violation out of a distinct, antecedent wrong — the warrantless entry — and so permitted liability even where the force was reasonable. If the force was reasonable, there is no excessive-force claim at all; any separate constitutional violation must be litigated as its own claim, with its foreseeable harms recoverable under ordinary proximate-cause principles. The Court also held the Ninth Circuit's alternative proximate-cause theory was infected by the same error and [[Reading and Citing Cases#on-remand|remanded]].

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. Alito, J., delivered the opinion of a unanimous Court; Gorsuch, J., took no part in the consideration or decision of the case.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Mendez* keeps excessive-force analysis anchored to *[[Graham v. Connor|Graham]]*'s moment-of-force reasonableness and eliminates the provocation rule as a route to liability. It preserves, rather than forecloses, recovery for a distinct antecedent violation such as an unlawful entry — through a separate claim and ordinary proximate cause. Teach it as reinforcing that the "reasonableness" inquiry is not to be diluted by folding in earlier, independent Fourth Amendment wrongs.

## Appears on
- [[Use of Force]] — *Anchor*

## Sources
- [*County of Los Angeles v. Mendez*, 581 U.S. 420 (2017)](https://www.courtlistener.com/opinion/4395246/county-of-los-angeles-v-mendez/) — pinpoint: 137 S. Ct. 1539, 1544 (Alito, J., for the Court; the CL opinion text is paginated to the parallel S. Ct. reporter, carrying the page-label `*1544` at the holding — the U.S. Reports star-pagination is not present in the CL text). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "762720762d599619", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "581 U.S. 420 (2017)", "court": "U.S. Supreme Court", "neutral_cite": "2017 U.S. LEXIS 3396; 2017 WL 2322832", "official_citation_present": true, "parallel_cite": "137 S. Ct. 1539; 198 L. Ed. 2d 52; 26 Fla. L. Weekly Fed. S 604; 85 U.S.L.W. 4292", "title": "County of Los Angeles v. Mendez", "year": "2017"}}
{"assertion_id": "07d4aa0d66e23229", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Anchor", "title": "County of Los Angeles v. Mendez"}}
{"assertion_id": "3dc3983aa41a564d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Amendment provides no basis for the Ninth Circuit's 'provocation rule'; an officer's objectively reasonable use of force cannot be rendered an unreasonable seizure by an earlier, separate Fourth Amendment violation (such as a warrantless entry) that provoked the confrontation, though that distinct violation may support its own claim and proximate-cause damages.", "title": "County of Los Angeles v. Mendez"}}
{"assertion_id": "05c738a037b6de2d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "County of Los Angeles v. Mendez", "varies_by_point": "false"}}
{"assertion_id": "db7f92a234a253f8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "County of Los Angeles v. Mendez"}}
```

### lake record — County of Los Angeles v. Mendez

```json
{
  "schema_version": "s2.v1",
  "record_id": "County of Los Angeles v. Mendez",
  "status": "under_review",
  "identity": {
    "case_name": "County of Los Angeles v. Mendez",
    "case_name_short": "Mendez",
    "case_name_full": "COUNTY OF LOS ANGELES, CALIFORNIA, Et Al., Petitioners v. Angel MENDEZ, Et Al.",
    "input_case_name": "County of Los Angeles v. Mendez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2017-05-30",
    "year": 2017,
    "docket": "No. 16-369",
    "cluster_id": 4395246,
    "lead_opinion_id": 4172499,
    "sibling_ids": [],
    "absolute_url": "/opinion/4395246/county-of-los-angeles-v-mendez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "581 U.S. 420",
      "volume": "581",
      "reporter": "U.S.",
      "page": "420",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "137 S. Ct. 1539",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "1539",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "198 L. Ed. 2d 52",
        "volume": "198",
        "reporter": "L. Ed. 2d",
        "page": "52",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 604",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4292",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4292",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2017 U.S. LEXIS 3396",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "3396",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 2322832",
        "volume": "2017",
        "reporter": "WL",
        "page": "2322832",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "581 U.S. 420",
        "volume": "581",
        "reporter": "U.S.",
        "page": "420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 1539",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "1539",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "198 L. Ed. 2d 52",
        "volume": "198",
        "reporter": "L. Ed. 2d",
        "page": "52",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. LEXIS 3396",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "3396",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 604",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4292",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4292",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 2322832",
        "volume": "2017",
        "reporter": "WL",
        "page": "2322832",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "581 U.S. 420",
    "official_selection": {
      "court_class": "scotus",
      "selected": "581 U.S. 420",
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
    "date_created": "2026-07-06T13:14:37Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:14:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:14:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "county-of-los-angeles-v-mendez--4395246",
      "to_record_id": "County of Los Angeles v. Mendez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — County of Los Angeles v. Mendez

```
(Slip Opinion)              OCTOBER TERM, 2016                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

  COUNTY OF LOS ANGELES, CALIFORNIA, ET AL. v. 

                MENDEZ ET AL. 


CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

      No. 16–369.      Argued March 22, 2017—Decided May 30, 2017
The Los Angeles County Sheriff’s Department received word from a
  confidential informant that a potentially armed and dangerous parol-
  ee-at-large had been seen at a certain residence. While other officers
  searched the main house, Deputies Conley and Pederson searched
  the back of the property where, unbeknownst to the deputies, re-
  spondents Mendez and Garcia were napping inside a shack where
  they lived. Without a search warrant and without announcing their
  presence, the deputies opened the door of the shack. Mendez rose
  from the bed, holding a BB gun that he used to kill pests. Deputy
  Conley yelled, “Gun!” and the deputies immediately opened fire,
  shooting Mendez and Garcia multiple times. Officers did not find the
  parolee in the shack or elsewhere on the property.
     Mendez and Garcia sued Deputies Conley and Pederson and the
  County under 42 U. S. C. §1983, pressing three Fourth Amendment
  claims: a warrantless entry claim, a knock-and-announce claim, and
  an excessive force claim. On the first two claims, the District Court
  awarded Mendez and Garcia nominal damages. On the excessive
  force claim, the court found that the deputies’ use of force was rea-
  sonable under Graham v. Connor, 490 U. S. 386, but held them liable
  nonetheless under the Ninth Circuit’s provocation rule, which makes
  an officer’s otherwise reasonable use of force unreasonable if (1) the
  officer “intentionally or recklessly provokes a violent confrontation”
  and (2) “the provocation is an independent Fourth Amendment viola-
  tion,” Billington v. Smith, 292 F. 3d 1177, 1189. On appeal, the
  Ninth Circuit held that the officers were entitled to qualified immun-
  ity on the knock-and-announce claim and that the warrantless entry
  violated clearly established law. It also affirmed the District Court’s
2               COUNTY OF LOS ANGELES v. MENDEZ

                                  Syllabus

    application of the provocation rule, and held, in the alternative, that
    basic notions of proximate cause would support liability even without
    the provocation rule.
Held: The Fourth Amendment provides no basis for the Ninth Circuit’s
 “provocation rule.” Pp. 5–10.
    (a) The provocation rule is incompatible with this Court’s excessive
 force jurisprudence, which sets forth a settled and exclusive frame-
 work for analyzing whether the force used in making a seizure com-
 plies with the Fourth Amendment. See Graham, supra, at 395. The
 operative question in such cases is “whether the totality of the cir-
 cumstances justifie[s] a particular sort of search or seizure.” Tennes-
 see v. Garner, 471 U. S. 1, 8–9. When an officer carries out a seizure
 that is reasonable, taking into account all relevant circumstances,
 there is no valid excessive force claim. The provocation rule, howev-
 er, instructs courts to look back in time to see if a different Fourth
 Amendment violation was somehow tied to the eventual use of force,
 an approach that mistakenly conflates distinct Fourth Amendment
 claims. The proper framework is set out in Graham. To the extent
 that a plaintiff has other Fourth Amendment claims, they should be
 analyzed separately.
    The Ninth Circuit attempts to cabin the provocation rule by defin-
 ing a two-prong test: First, the separate constitutional violation must
 “creat[e] a situation which led to” the use of force; and second, the
 separate constitutional violation must be committed recklessly or in-
 tentionally. 815 F. 3d 1178, 1193. Neither limitation, however,
 solves the fundamental problem: namely, that the provocation rule is
 an unwarranted and illogical expansion of Graham. In addition, each
 limitation creates problems of its own. First, the rule relies on a
 vague causal standard. Second, while the reasonableness of a search
 or seizure is almost always based on objective factors, the provocation
 rule looks to the subjective intent of the officers who carried out the
 seizure.
    There is no need to distort the excessive force inquiry in this way in
 order to hold law enforcement officers liable for the foreseeable con-
 sequences of all their constitutional torts. Plaintiffs can, subject to
 qualified immunity, generally recover damages that are proximately
 caused by any Fourth Amendment violation. See, e.g., Heck v.
 Humphrey, 512 U. S. 477, 483. Here, if respondents cannot recover
 on their excessive force claim, that will not foreclose recovery for in-
 juries proximately caused by the warrantless entry. Pp. 5–10.
    (b) The Ninth Circuit’s proximate-cause holding is similarly taint-
 ed. Its analysis appears to focus solely on the risks foreseeably asso-
 ciated with the failure to knock and announce—the claim on which
 the court concluded that the deputies had qualified immunity—
                     Cite as: 581 U. S. ____ (2017)                   3

                               Syllabus

  rather than the warrantless entry. On remand, the court should re-
  visit the question whether proximate cause permits respondents to
  recover damages for their injuries based on the deputies’ failure to
  secure a warrant at the outset. Pp. 10–11.
815 F. 3d 1178, vacated and remanded.

  ALITO, J., delivered the opinion of the Court, in which all other Mem-
bers joined, except GORSUCH, J., who took no part in the consideration
or decision of the case.
                       Cite as: 581 U. S. ____ (2017)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 16–369
                                  _________________


  COUNTY OF LOS ANGELES, CALIFORNIA, ET AL., 

     PETITIONERS v. ANGEL MENDEZ, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                                [May 30, 2017]


  JUSTICE ALITO delivered the opinion of the Court.
  If law enforcement officers make a “seizure” of a person
using force that is judged to be reasonable based on a
consideration of the circumstances relevant to that deter-
mination, may the officers nevertheless be held liable for
injuries caused by the seizure on the ground that they
committed a separate Fourth Amendment violation that
contributed to their need to use force? The Ninth Circuit
has adopted a “provocation rule” that imposes liability in
such a situation.
  We hold that the Fourth Amendment provides no basis
for such a rule. A different Fourth Amendment violation
cannot transform a later, reasonable use of force into an
unreasonable seizure.
                            I

                            A

  In October 2010, deputies from the Los Angeles County
Sheriff ’s Department were searching for a parolee-at-large
named Ronnie O’Dell. A felony arrest warrant had been
issued for O’Dell, who was believed to be armed and dan-
gerous and had previously evaded capture. Findings of
2           COUNTY OF LOS ANGELES v. MENDEZ

                     Opinion of the Court

Fact and Conclusions of Law, No. 2:11–cv–04771 (CD
Cal.), App. to Pet. for Cert. 56a, 64a. Deputies Christo-
pher Conley and Jennifer Pederson were assigned to assist
the task force searching for O’Dell. Id., at 57a–58a. The
task force received word from a confidential informant
that O’Dell had been seen on a bicycle at a home in Lan-
caster, California, owned by Paula Hughes, and the offic-
ers then mapped out a plan for apprehending O’Dell. Id.,
at 58a. Some officers would approach the front door of the
Hughes residence, while Deputies Conley and Pederson
would search the rear of the property and cover the back
door of the residence. Id., at 59a. During this briefing, it
was announced that a man named Angel Mendez lived in
the backyard of the Hughes home with a pregnant woman
named Jennifer Garcia (now Mrs. Jennifer Mendez). Ibid.
Deputy Pederson heard this announcement, but at trial
Deputy Conley testified that he did not remember it. Ibid.
  When the officers reached the Hughes residence around
midday, three of them knocked on the front door while
Deputies Conley and Pederson went to the back of the
property. Id., at 63a. At the front door, Hughes asked if
the officers had a warrant. Ibid. A sergeant responded
that they did not but were searching for O’Dell and had a
warrant for his arrest. Ibid. One of the officers heard
what he thought were sounds of someone running inside
the house. Id., at 64a. As the officers prepared to open
the door by force, Hughes opened the door and informed
them that O’Dell was not in the house. Ibid. She was
placed under arrest, and the house was searched, but
O’Dell was not found. Ibid.
  Meanwhile, Deputies Conley and Pederson, with guns
drawn, searched the rear of the residence, which was
cluttered with debris and abandoned automobiles. Id., at
60a, 65a. The property included three metal storage sheds
and a one-room shack made of wood and plywood. Id., at
60a. Mendez had built the shack, and he and Garcia had
                 Cite as: 581 U. S. ____ (2017)           3

                     Opinion of the Court

lived inside for about 10 months. Id., at 61a. The shack
had a single doorway covered by a blue blanket. Ibid.
Amid the debris on the ground, an electrical cord ran into
the shack, and an air conditioner was mounted on the
side. Id., at 62a. A gym storage locker and clothes and
other possessions were nearby. Id., at 61a. Mendez kept a
BB rifle in the shack for use on rats and other pests. Id.,
at 62a. The BB gun “closely resembled a small caliber
rifle.” Ibid.
   Deputies Conley and Pederson first checked the three
metal sheds and found no one inside. Id., at 65a. They
then approached the door of the shack. Id., at 66a. Unbe-
knownst to the officers, Mendez and Garcia were in the
shack and were napping on a futon. Id., at 67a. The
deputies did not have a search warrant and did not knock
and announce their presence. Id., at 66a. When Deputy
Conley opened the wooden door and pulled back the blan-
ket, Mendez thought it was Ms. Hughes and rose from the
bed, picking up the BB gun so he could stand up and place
it on the floor. Id., at 68a. As a result, when the deputies
entered, he was holding the BB gun, and it was “point[ing]
somewhat south towards Deputy Conley.” Id., at 69a.
Deputy Conley yelled, “Gun!” and the deputies immediately
opened fire, discharging a total of 15 rounds. Id., at 69a–
70a. Mendez and Garcia “were shot multiple times and
suffered severe injuries,” and Mendez’s right leg was later
amputated below the knee. Id., at 70a. O’Dell was not in
the shack or anywhere on the property. Ibid.
                           B
  Mendez and his wife (respondents here) filed suit under
Rev. Stat. §1976, 42 U. S. C. §1983, against petitioners,
the County of Los Angeles and Deputies Conley and Ped-
erson. As relevant here, they pressed three Fourth
Amendment claims. First, they claimed that the deputies
executed an unreasonable search by entering the shack
4           COUNTY OF LOS ANGELES v. MENDEZ

                     Opinion of the Court

without a warrant (the “warrantless entry claim”); second,
they asserted that the deputies performed an unreason-
able search because they failed to announce their presence
before entering the shack (the “knock-and-announce
claim”); and third, they claimed that the deputies effected
an unreasonable seizure by deploying excessive force in
opening fire after entering the shack (the “excessive force
claim”).
  After a bench trial, the District Court ruled largely in
favor of respondents. App. to Pet. for Cert. 135a–136a.
The court found Deputy Conley liable on the warrantless
entry claim, and the court also found both deputies liable
on the knock-and-announce claim. But the court awarded
nominal damages for these violations because “the act of
pointing the BB gun” was a superseding cause “as far as
damage [from the shooting was] concerned.” App. 238.
  The District Court then addressed respondents’ exces-
sive force claim. App. to Pet. for Cert. 105a–127a. The
court began by evaluating whether the deputies used
excessive force under Graham v. Connor, 490 U. S. 386
(1989). The court held that, under Graham, the deputies’
use of force was reasonable “given their belief that a man
was holding a firearm rifle threatening their lives.” App.
to Pet. for Cert. 108a. But the court did not end its exces-
sive force analysis at this point. Instead, the court turned
to the Ninth Circuit’s provocation rule, which holds that
“an officer’s otherwise reasonable (and lawful) defensive
use of force is unreasonable as a matter of law, if (1) the
officer intentionally or recklessly provoked a violent re-
sponse, and (2) that provocation is an independent consti-
tutional violation.” Id., at 111a. Based on this rule, the
District Court held the deputies liable for excessive force
and awarded respondents around $4 million in damages.
Id., at 135a–136a.
  The Court of Appeals affirmed in part and reversed in
part. 815 F. 3d 1178 (CA9 2016). Contrary to the District
                 Cite as: 581 U. S. ____ (2017)           5

                     Opinion of the Court

Court, the Court of Appeals held that the officers were
entitled to qualified immunity on the knock-and-announce
claim. Id., at 1191–1193. But the court concluded that
the warrantless entry of the shack violated clearly estab-
lished law and was attributable to both deputies. Id., at
1191, 1195. Finally, and most important for present
purposes, the court affirmed the application of the provo-
cation rule. The Court of Appeals did not disagree with
the conclusion that the shooting was reasonable under
Graham; instead, like the District Court, the Court of
Appeals applied the provocation rule and held the depu-
ties liable for the use of force on the theory that they had
intentionally and recklessly brought about the shooting by
entering the shack without a warrant in violation of clearly
established law. 815 F. 3d, at 1193.
   The Court of Appeals also adopted an alternative ra-
tionale for its judgment. It held that “basic notions of
proximate cause” would support liability even without the
provocation rule because it was “reasonably foreseeable”
that the officers would meet an armed homeowner when
they “barged into the shack unannounced.” Id., at 1194–
1195.
   We granted certiorari. 580 U. S. ___ (2016).
                             II
  The Ninth Circuit’s provocation rule permits an exces-
sive force claim under the Fourth Amendment “where an
officer intentionally or recklessly provokes a violent con-
frontation, if the provocation is an independent Fourth
Amendment violation.” Billington v. Smith, 292 F. 3d
1177, 1189 (CA9 2002). The rule comes into play after a
forceful seizure has been judged to be reasonable under
Graham. Once a court has made that determination, the
rule instructs the court to ask whether the law enforce-
ment officer violated the Fourth Amendment in some
other way in the course of events leading up to the seizure.
6           COUNTY OF LOS ANGELES v. MENDEZ

                     Opinion of the Court

If so, that separate Fourth Amendment violation may
“render the officer’s otherwise reasonable defensive use of
force unreasonable as a matter of law.” Id., at 1190–1191.
   The provocation rule, which has been “sharply ques-
tioned” outside the Ninth Circuit, City and County of San
Francisco v. Sheehan, 575 U. S. ___, ___, n. 4 (2015) (slip
op., at 14, n. 4), is incompatible with our excessive force
jurisprudence. The rule’s fundamental flaw is that it uses
another constitutional violation to manufacture an exces-
sive force claim where one would not otherwise exist.
   The Fourth Amendment prohibits “unreasonable
searches and seizures.” “[R]easonableness is always the
touchstone of Fourth Amendment analysis,” Birchfield v.
North Dakota, 579 U. S. ___, ___ (2016) (slip op., at 37),
and reasonableness is generally assessed by carefully
weighing “the nature and quality of the intrusion on the
individual’s Fourth Amendment interests against the
importance of the governmental interests alleged to justify
the intrusion.” Tennessee v. Garner, 471 U. S. 1, 8 (1985)
(internal quotation marks omitted).
   Our case law sets forth a settled and exclusive frame-
work for analyzing whether the force used in making a
seizure complies with the Fourth Amendment. See Gra-
ham, 490 U. S., at 395. As in other areas of our Fourth
Amendment jurisprudence, “[d]etermining whether the
force used to effect a particular seizure is ‘reasonable’ ”
requires balancing of the individual’s Fourth Amendment
interests against the relevant government interests. Id.,
at 396. The operative question in excessive force cases is
“whether the totality of the circumstances justifie[s] a
particular sort of search or seizure.” Garner, supra, at 8–9.
   The reasonableness of the use of force is evaluated
under an “objective” inquiry that pays “careful attention to
the facts and circumstances of each particular case.”
Graham, supra, at 396. And “[t]he ‘reasonableness’ of a
particular use of force must be judged from the perspective
                  Cite as: 581 U. S. ____ (2017)            7

                      Opinion of the Court

of a reasonable officer on the scene, rather than with the
20/20 vision of hindsight.” Ibid. “Excessive force claims
. . . are evaluated for objective reasonableness based upon
the information the officers had when the conduct oc-
curred.” Saucier v. Katz, 533 U. S. 194, 207 (2001). That
inquiry is dispositive: When an officer carries out a seizure
that is reasonable, taking into account all relevant cir-
cumstances, there is no valid excessive force claim.
    The basic problem with the provocation rule is that it
fails to stop there. Instead, the rule provides a novel and
unsupported path to liability in cases in which the use of
force was reasonable. Specifically, it instructs courts to
look back in time to see if there was a different Fourth
Amendment violation that is somehow tied to the eventual
use of force. That distinct violation, rather than the force-
ful seizure itself, may then serve as the foundation of the
plaintiff ’s excessive force claim. Billington, supra, at 1190
(“The basis of liability for the subsequent use of force is
the initial constitutional violation . . . ”).
    This approach mistakenly conflates distinct Fourth
Amendment claims. Contrary to this approach, the objec-
tive reasonableness analysis must be conducted separately
for each search or seizure that is alleged to be unconstitu-
tional. An excessive force claim is a claim that a law
enforcement officer carried out an unreasonable seizure
through a use of force that was not justified under the
relevant circumstances. It is not a claim that an officer
used reasonable force after committing a distinct Fourth
Amendment violation such as an unreasonable entry.
    By conflating excessive force claims with other Fourth
Amendment claims, the provocation rule permits excessive
force claims that cannot succeed on their own terms. That
is precisely how the rule operated in this case. The Dis-
trict Court found (and the Ninth Circuit did not dispute)
that the use of force by the deputies was reasonable under
Graham. However, respondents were still able to recover
8             COUNTY OF LOS ANGELES v. MENDEZ

                          Opinion of the Court

damages because the deputies committed a separate
constitutional violation (the warrantless entry into the
shack) that in some sense set the table for the use of force.
That is wrong. The framework for analyzing excessive
force claims is set out in Graham. If there is no excessive
force claim under Graham, there is no excessive force
claim at all. To the extent that a plaintiff has other
Fourth Amendment claims, they should be analyzed
separately.*
  The Ninth Circuit’s efforts to cabin the provocation rule
only undermine it further. The Ninth Circuit appears to
recognize that it would be going entirely too far to suggest
that any Fourth Amendment violation that is connected to
a reasonable use of force should create a valid excessive
force claim. See, e.g., Beier v. Lewiston, 354 F. 3d 1058,
1064 (CA9 2004) (“Because the excessive force and false
arrest factual inquiries are distinct, establishing a lack of
probable cause to make an arrest does not establish an
excessive force claim, and vice-versa”). Instead, that court
has endeavored to limit the rule to only those distinct
Fourth Amendment violations that in some sense “pro-
voked” the need to use force. The concept of provocation,
——————
  * Respondents do not attempt to defend the provocation rule. In-
stead, they argue that the judgment below should be affirmed under
Graham itself. Graham commands that an officer’s use of force be
assessed for reasonableness under the “totality of the circumstances.”
490 U. S., at 396 (internal quotation marks omitted). On respondents’
view, that means taking into account unreasonable police conduct prior
to the use of force that foreseeably created the need to use it. Brief for
Respondents 42–43. We did not grant certiorari on that question, and
the decision below did not address it. Accordingly, we decline to ad-
dress it here. See, e.g., McLane Co. v. EEOC, ante, at 11 (“[W]e are a
court of review, not of first view” (internal quotation marks omitted)).
All we hold today is that once a use of force is deemed reasonable under
Graham, it may not be found unreasonable by reference to some sepa-
rate constitutional violation. Any argument regarding the District
Court’s application of Graham in this case should be addressed to the
Ninth Circuit on remand.
                 Cite as: 581 U. S. ____ (2017)           9

                     Opinion of the Court

in turn, has been defined using a two-prong test. First,
the separate constitutional violation must “creat[e] a
situation which led to” the use of force; second, the sepa-
rate constitutional violation must be committed recklessly
or intentionally. 815 F. 3d, at 1193 (internal quotation
marks omitted).
   Neither of these limitations solves the fundamental
problem of the provocation rule: namely, that it is an
unwarranted and illogical expansion of Graham. But in
addition, each of the limitations creates problems of its
own. First, the rule includes a vague causal standard. It
applies when a prior constitutional violation “created a
situation which led to” the use of force. The rule does not
incorporate the familiar proximate cause standard. In-
deed, it is not clear what causal standard is being applied.
Second, while the reasonableness of a search or seizure is
almost always based on objective factors, see Whren v.
United States, 517 U. S. 806, 814 (1996), the provocation
rule looks to the subjective intent of the officers who car-
ried out the seizure. As noted, under the Ninth Circuit’s
rule, a prior Fourth Amendment violation may be held to
have provoked a later, reasonable use of force only if the
prior violation was intentional or reckless.
   The provocation rule may be motivated by the notion
that it is important to hold law enforcement officers liable
for the foreseeable consequences of all of their constitu-
tional torts. See Billington, 292 F. 3d, at 1190 (“[I]f an
officer’s provocative actions are objectively unreasonable
under the Fourth Amendment, . . . liability is established,
and the question becomes . . . what harms the constitu-
tional violation proximately caused”). However, there is
no need to distort the excessive force inquiry in order to
accomplish this objective. To the contrary, both parties
accept the principle that plaintiffs can—subject to quali-
fied immunity—generally recover damages that are prox-
imately caused by any Fourth Amendment violation. See,
10          COUNTY OF LOS ANGELES v. MENDEZ

                      Opinion of the Court

e.g., Heck v. Humphrey, 512 U. S. 477, 483 (1994) (§1983
“creates a species of tort liability” informed by tort princi-
ples regarding “damages and the prerequisites for their
recovery” (internal quotation marks omitted)); Memphis
Community School Dist. v. Stachura, 477 U. S. 299, 306
(1986) (“[W]hen §1983 plaintiffs seek damages for viola-
tions of constitutional rights, the level of damages is ordi-
narily determined according to principles derived from the
common law of torts”). Thus, there is no need to dress up
every Fourth Amendment claim as an excessive force
claim. For example, if the plaintiffs in this case cannot
recover on their excessive force claim, that will not fore-
close recovery for injuries proximately caused by the war-
rantless entry. The harm proximately caused by these
two torts may overlap, but the two claims should not be
confused.
                             III
  The Court of Appeals also held that “even without rely-
ing on [the] provocation theory, the deputies are liable for
the shooting under basic notions of proximate cause.” 815
F. 3d, at 1194. In other words, the court apparently con-
cluded that the shooting was proximately caused by the
deputies’ warrantless entry of the shack. Proper analysis
of this proximate cause question required consideration of
the “foreseeability or the scope of the risk created by the
predicate conduct,” and required the court to conclude that
there was “some direct relation between the injury asserted
and the injurious conduct alleged.” Paroline v. United
States, 572 U. S. ___, ___ (2014) (slip op., at 7) (internal
quotation marks omitted).
  Unfortunately, the Court of Appeals’ proximate cause
analysis appears to have been tainted by the same errors
that cause us to reject the provocation rule. The court
reasoned that when officers make a “startling entry” by
“barg[ing] into” a home “unannounced,” it is reasonably
                 Cite as: 581 U. S. ____ (2017)           11

                     Opinion of the Court

foreseeable that violence may result. 815 F. 3d, at 1194–
1195 (internal quotation marks omitted). But this ap-
pears to focus solely on the risks foreseeably associated
with the failure to knock and announce, which could not
serve as the basis for liability since the Court of Appeals
concluded that the officers had qualified immunity on that
claim. By contrast, the Court of Appeals did not identify
the foreseeable risks associated with the relevant constitu-
tional violation (the warrantless entry); nor did it explain
how, on these facts, respondents’ injuries were proximately
caused by the warrantless entry. In other words, the
Court of Appeals’ proximate cause analysis, like the provo-
cation rule, conflated distinct Fourth Amendment claims
and required only a murky causal link between the war-
rantless entry and the injuries attributed to it. On re-
mand, the court should revisit the question whether prox-
imate cause permits respondents to recover damages for
their shooting injuries based on the deputies’ failure to
secure a warrant at the outset. See Bank of America Corp.
v. Miami, ante, at 12 (declining to “draw the precise
boundaries of proximate cause” in the first instance). The
arguments made on this point by the parties and by the
United States as amicus provide a useful starting point for
this inquiry. See Brief for Petitioners 42–56; Brief for
Respondents 20–31, 51–59; Reply Brief 17–24; Brief for
United States as Amicus Curiae 26–32.
                        *     *    *
   For these reasons, the judgment of the Court of Appeals
is vacated, and the case is remanded for further proceed-
ings consistent with this opinion.
                                           It is so ordered.

  JUSTICE GORSUCH took no part in the consideration or
decision of this case.

```

---

## GROUP: content/cases/County of Riverside v. McLaughlin.md  (`case`, 6 assertions)

### content_page

```
---
title: "County of Riverside v. McLaughlin"
type: case
citation: "500 U.S. 44 (1991)"
parallel_cite: "111 S. Ct. 1661; 114 L. Ed. 2d 49"
neutral_cite: 1991 U.S. LEXIS 2528
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-05-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: County of Riverside v. McLaughlin
  varies_by_point: false
  scope_note: "Good law. Implements Gerstein v. Pugh: a judicial probable-cause determination within 48 hours of a warrantless arrest is presumptively prompt; beyond 48 hours the burden shifts to the government to show a bona fide emergency or other extraordinary circumstance, and intervening weekends/holidays do not excuse delay. (date_decided omitted — CL dateFiled 1991-05-20 differs from the announced May 13, 1991; year certain.)"
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112585/county-of-riverside-v-mclaughlin/"
  cluster_id: 112585
  opinion_id: 112585
  identity_checked: true
homes:
  - page: "[[Prompt Probable-Cause Determination]]"
    role: "Key — the 48-hour presumption implementing Gerstein"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[Gerstein v. Pugh]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest", "probable-cause", "pretrial-detention", "gerstein-hearing"]
holding: "A judicial probable-cause determination provided within 48 hours of a warrantless arrest is presumptively prompt under Gerstein; if it comes later, the burden shifts to the government to show a bona fide emergency or extraordinary circumstance (intervening weekends do not qualify)."
lake:
  record_id: County of Riverside v. McLaughlin
  status: verified
  projected_at: 2026-07-06
---

# County of Riverside v. McLaughlin

*500 U.S. 44 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Riverside County, California, combined the *[[Gerstein v. Pugh|Gerstein]]* probable-cause determination for warrantless arrestees with its arraignment proceedings, which were provided within two days of arrest but excluding weekends and holidays. As a result, a person arrested late in the week (for example, on a Thursday) could be held until the following Monday — longer with an intervening holiday — before any judicial probable-cause determination. McLaughlin and others brought a class action challenging the practice as a violation of the promptness requirement of *[[Gerstein v. Pugh]]*.

## Issue
What time period satisfies *[[Gerstein v. Pugh|Gerstein]]*'s requirement that a warrantless arrestee receive a "prompt" judicial determination of probable cause — and whether Riverside County's weekend- and holiday-excluding schedule met it.

## Rule
A 48-hour window is presumptively prompt. "[A] jurisdiction that provides judicial determinations of probable cause within 48 hours of arrest will, as a general matter, comply with the promptness requirement of *Gerstein*." — 500 U.S. at 56. ^pin-56

But timeliness within 48 hours is not automatically sufficient: "This is not to say that the probable cause determination in a particular case passes constitutional muster simply because it is provided within 48 hours. Such a hearing may nonetheless violate *Gerstein* if the arrested individual can prove that his or her probable cause determination was delayed unreasonably." — *Id.* ^pin-56b

Past 48 hours, the burden flips: "Where an arrested individual does not receive a probable cause determination within 48 hours, the calculus changes. . . . [T]he burden shifts to the government to demonstrate the existence of a bona fide emergency or other extraordinary circumstance. . . . Nor, for that matter, do intervening weekends [qualify as such a circumstance]." — *Id.* at 57. ^pin-57

## Application
Riverside's practice — combined probable-cause/arraignment proceedings within two days but excluding Saturdays, Sundays, and holidays — meant a Thursday arrestee might wait until Monday, exceeding the 48-hour period the Court deemed presumptively permissible. Because its regular practice ran past 48 hours, the County was not immune from a systemic (class-action) challenge. The Court left to the lower courts [[Reading and Citing Cases#on-remand|on remand]] whether the County's habit of holding arraignments on "the last day" possible reflected legitimate reasons or impermissible "delay for delay's sake."

## Conclusion
A judicial probable-cause determination within 48 hours of a warrantless arrest is presumptively prompt under *[[Gerstein v. Pugh|Gerstein]]*; delay beyond that shifts the burden to the government, and weekends and holidays do not excuse it. Riverside's schedule exceeded the window, so the judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *McLaughlin* implements the "promptly after arrest" requirement of [[Gerstein v. Pugh]] with the operative 48-hour benchmark (and the over-48-hour burden shift) that governs post-arrest detention timing.

## Appears on
- [[Prompt Probable-Cause Determination]] — *Key*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *County of Riverside v. McLaughlin*, 500 U.S. 44 (1991) — https://www.courtlistener.com/opinion/112585/county-of-riverside-v-mclaughlin/ — pinpoints: 56, 57.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "51eb34b1d940c8e6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "500 U.S. 44 (1991)", "court": "U.S. Supreme Court", "neutral_cite": "1991 U.S. LEXIS 2528", "official_citation_present": true, "parallel_cite": "111 S. Ct. 1661; 114 L. Ed. 2d 49", "title": "County of Riverside v. McLaughlin", "year": "1991"}}
{"assertion_id": "0a1b2e6affe3bc73", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A judicial probable-cause determination provided within 48 hours of a warrantless arrest is presumptively prompt under Gerstein; if it comes later, the burden shifts to the government to show a bona fide emergency or extraordinary circumstance (intervening weekends do not qualify).", "title": "County of Riverside v. McLaughlin"}}
{"assertion_id": "40a31f6a9f7b9898", "dimension": "support", "kind": "home_role", "locator": {"home": "Prompt Probable-Cause Determination"}, "payload": {"home": "Prompt Probable-Cause Determination", "role": "Key — the 48-hour presumption implementing Gerstein", "title": "County of Riverside v. McLaughlin"}}
{"assertion_id": "8f329002f7232718", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Related (cross-doctrine)", "title": "County of Riverside v. McLaughlin"}}
{"assertion_id": "0ccce9afbbb7fbb7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "County of Riverside v. McLaughlin"}}
{"assertion_id": "eb9a35d213ad5054", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "County of Riverside v. McLaughlin", "field_i_validity": "good_law", "scope_note": "Good law. Implements Gerstein v. Pugh: a judicial probable-cause determination within 48 hours of a warrantless arrest is presumptively prompt; beyond 48 hours the burden shifts to the government to show a bona fide emergency or other extraordinary circumstance, and intervening weekends/holidays do not excuse delay. (date_decided omitted — CL dateFiled 1991-05-20 differs from the announced May 13, 1991; year certain.)", "title": "County of Riverside v. McLaughlin", "varies_by_point": "false"}}
```

### lake record — County of Riverside v. McLaughlin

```json
{
  "schema_version": "s2.v1",
  "record_id": "County of Riverside v. McLaughlin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "County of Riverside v. McLaughlin",
    "case_name_short": "McLaughlin",
    "case_name_full": "COUNTY OF RIVERSIDE Et Al. v. McLAUGHLIN Et Al.",
    "input_case_name": "County of Riverside v. McLaughlin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-05-20",
    "year": 1991,
    "docket": null,
    "cluster_id": 112585,
    "lead_opinion_id": 112585,
    "sibling_ids": [
      112585,
      9432264,
      9432265,
      9432266
    ],
    "absolute_url": "/opinion/112585/county-of-riverside-v-mclaughlin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9104127,
        "score": 20,
        "case_name": "County of Riverside v. McLaughlin"
      },
      {
        "cluster_id": 9104126,
        "score": 20,
        "case_name": "County of Riverside v. McLaughlin"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "500 U.S. 44",
      "volume": "500",
      "reporter": "U.S.",
      "page": "44",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 1661",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1661",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 L. Ed. 2d 49",
        "volume": "114",
        "reporter": "L. Ed. 2d",
        "page": "49",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 2528",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "2528",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "500 U.S. 44",
        "volume": "500",
        "reporter": "U.S.",
        "page": "44",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 1661",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1661",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 L. Ed. 2d 49",
        "volume": "114",
        "reporter": "L. Ed. 2d",
        "page": "49",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 2528",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "2528",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "500 U.S. 44",
    "official_selection": {
      "court_class": "scotus",
      "selected": "500 U.S. 44",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-56",
      "page": null,
      "quote": "judicial determination of probable cause \u2014 and whether Riverside County's weekend- and holiday-excluding schedule met it. ## Rule A 48-hour window is presumptively prompt.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-56b",
      "page": null,
      "quote": "This is not to say that the probable cause determination in a particular case passes constitutional muster simply because it is provided within 48 hours. Such a hearing may nonetheless violate *Gerstein* if the arrested individual can prove that his or her probable cause determination was delayed unreasonably.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-57",
      "page": null,
      "quote": "Where an arrested individual does not receive a probable cause determination within 48 hours, the calculus changes. . . . [T]he burden shifts to the government to demonstrate the existence of a bona fide emergency or other extraordinary circumstance. . . . Nor, for that matter, do intervening weekends [qualify as such a circumstance].",
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
    "composite_basis_ref": "County of Riverside v. McLaughlin",
    "varies_by_point": false,
    "scope_note": "Good law. Implements Gerstein v. Pugh: a judicial probable-cause determination within 48 hours of a warrantless arrest is presumptively prompt; beyond 48 hours the burden shifts to the government to show a bona fide emergency or other extraordinary circumstance, and intervening weekends/holidays do not excuse delay. (date_decided omitted \u2014 CL dateFiled 1991-05-20 differs from the announced May 13, 1991; year certain.)",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Foster v. Commissioner of Correction (No. 1)",
          "cluster_id": 4758096,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morehouse v. Jackson",
          "cluster_id": 8694856,
          "cite": [
            "614 F. App'x 159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jeffrey M. Stein D.D.S. M.S.D. P.A. v. Buccaneers Limited Partnership",
          "cluster_id": 2756228,
          "cite": [
            "772 F.3d 698",
            "2014 WL 6734819"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. County of Monterey",
          "cluster_id": 7310798,
          "cite": [
            "70 F. Supp. 3d 963",
            "2014 U.S. Dist. LEXIS 138247",
            "2014 WL 4843945"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Courtney Bishop",
          "cluster_id": 2655823,
          "cite": [
            "431 S.W.3d 22",
            "2014 WL 888198",
            "2014 Tenn. LEXIS 189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilson v. Montano",
          "cluster_id": 866546,
          "cite": [
            "715 F.3d 847",
            "2013 U.S. App. LEXIS 9055",
            "2013 WL 1848138"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane1_negative"
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
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zadvydas v. Davis",
          "cluster_id": 1269289,
          "cite": [
            "150 L. Ed. 2d 653",
            "121 S. Ct. 2491",
            "533 U.S. 678",
            "2001 U.S. LEXIS 4912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Devenpeck v. Alford",
          "cluster_id": 137733,
          "cite": [
            "160 L. Ed. 2d 537",
            "125 S. Ct. 588",
            "543 U.S. 146",
            "2004 U.S. LEXIS 8272"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hamdi v. Rumsfeld",
          "cluster_id": 137001,
          "cite": [
            "159 L. Ed. 2d 578",
            "124 S. Ct. 2633",
            "542 U.S. 507",
            "2004 U.S. LEXIS 4761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
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
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Genesis HealthCare Corp. v. Symczyk",
          "cluster_id": 858086,
          "cite": [
            "185 L. Ed. 2d 636",
            "133 S. Ct. 1523",
            "569 U.S. 66",
            "2013 U.S. LEXIS 3157",
            "24 Fla. L. Weekly Fed. S 133",
            "81 U.S.L.W. 4229",
            "20 Wage & Hour Cas.2d (BNA) 801",
            "2013 WL 1567370"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lloyd D. Alkire v. Judge Jane Irving",
          "cluster_id": 782133,
          "cite": [
            "330 F.3d 802",
            "55 Fed. R. Serv. 3d 1023",
            "2003 U.S. App. LEXIS 10834",
            "2003 WL 21251540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kerry Heckman, on Behalf of Themselves and All Other Persons Similarly Situated v. Williamson County",
          "cluster_id": 895412,
          "cite": [
            "369 S.W.3d 137",
            "55 Tex. Sup. Ct. J. 803",
            "2012 WL 2052813",
            "2012 Tex. LEXIS 462"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manuel v. City of Joliet",
          "cluster_id": 4376986,
          "cite": [
            "580 U.S. 357",
            "137 S. Ct. 911",
            "197 L. Ed. 2d 312",
            "2017 U.S. LEXIS 2021",
            "26 Fla. L. Weekly Fed. S 476",
            "85 U.S.L.W. 4130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corley v. United States",
          "cluster_id": 145888,
          "cite": [
            "173 L. Ed. 2d 443",
            "129 S. Ct. 1558",
            "556 U.S. 303",
            "2009 U.S. LEXIS 2512"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cantu v. State",
          "cluster_id": 2431347,
          "cite": [
            "842 S.W.2d 667",
            "1992 Tex. Crim. App. LEXIS 138",
            "1992 WL 116290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florence v. Board of Chosen Freeholders of County of Burlington",
          "cluster_id": 626454,
          "cite": [
            "182 L. Ed. 2d 566",
            "132 S. Ct. 1510",
            "566 U.S. 318",
            "2012 U.S. LEXIS 2712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hughes",
          "cluster_id": 2581420,
          "cite": [
            "39 P.3d 432",
            "116 Cal. Rptr. 2d 401",
            "27 Cal. 4th 287"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. King",
          "cluster_id": 873669,
          "cite": [
            "186 L. Ed. 2d 1",
            "133 S. Ct. 1958",
            "2013 U.S. LEXIS 4165",
            "569 U.S. 435",
            "24 Fla. L. Weekly Fed. S 234",
            "81 U.S.L.W. 4343",
            "2013 WL 2371466"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1801669,
          "cite": [
            "49 Cal. 4th 405",
            "2010 D.A.R. 10",
            "111 Cal. Rptr. 3d 589",
            "233 P.3d 1000",
            "2010 Cal. LEXIS 5970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hansen v. State",
          "cluster_id": 1829968,
          "cite": [
            "592 So. 2d 114",
            "1991 WL 280025"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nielsen v. Preap",
          "cluster_id": 4601079,
          "cite": [
            "586 U.S. 392",
            "139 S. Ct. 954",
            "203 L. Ed. 2d 333",
            "2019 U.S. LEXIS 2088"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Rodriguez",
          "cluster_id": 11663,
          "cite": [
            "110 F.3d 299",
            "1997 WL 163525"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Abu Ali",
          "cluster_id": 1025840,
          "cite": [
            "528 F.3d 210",
            "2008 U.S. App. LEXIS 12122",
            "2008 WL 2315664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robidoux v. Celani",
          "cluster_id": 9014146,
          "cite": [
            "987 F.2d 931",
            "25 Fed. R. Serv. 3d 86",
            "1993 U.S. App. LEXIS 4332",
            "1993 WL 64467"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shane Holloway v. Delaware County S",
          "cluster_id": 812189,
          "cite": [
            "700 F.3d 1063",
            "2012 U.S. App. LEXIS 23823",
            "2012 WL 5846289"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robidoux v. Celani",
          "cluster_id": 601791,
          "cite": [
            "987 F.2d 931"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Turner",
          "cluster_id": 1188941,
          "cite": [
            "878 P.2d 521",
            "8 Cal. 4th 137",
            "32 Cal. Rptr. 2d 762",
            "94 Daily Journal DAR 11425",
            "94 Cal. Daily Op. Serv. 6238",
            "1994 Cal. LEXIS 4151"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Case v. Eslinger",
          "cluster_id": 78223,
          "cite": [
            "555 F.3d 1317",
            "2009 U.S. App. LEXIS 2141",
            "2009 WL 196842"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "County of Riverside v. McLaughlin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112585 OR 9432264 OR 9432265 OR 9432266) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzY2MDcwNDAwMDAwJnM9ODU4MDg2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112585+OR+9432264+OR+9432265+OR+9432266%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(112585 OR 9432264 OR 9432265 OR 9432266)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzMmcz0xNTU4OTE0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112585+OR+9432264+OR+9432265+OR+9432266%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112585 OR 9432264 OR 9432265 OR 9432266)",
        "reviewed": 42,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 42,
        "triage_read": 0,
        "triage_snippet_classified": 42
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112585 OR 9432264 OR 9432265 OR 9432266)",
    "indexed_citing_opinions": 862,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112585,
        "count": 740,
        "count_source": "search"
      },
      {
        "opinion_id": 9432264,
        "count": 136,
        "count_source": "search"
      },
      {
        "opinion_id": 9432265,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432266,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1552,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/county-of-riverside-v-mclaughlin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NjUzOCZzPTEwNjAwMDU2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112585+OR+9432264+OR+9432265+OR+9432266%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112585,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 108713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 109128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 109928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 110228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 110599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 110916,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 111198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 111258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 112188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 112489,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 334165,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 392118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 409611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 414211,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 453324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 474259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 504865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 531392,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 1398635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 1460908,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112585,
        "cited_id": 1897137,
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
    "date_created": "2026-07-05T01:27:02Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:46:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — County of Riverside v. McLaughlin

```
<div>
<center><b><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U.S. 44</a></span> (1991)</b></center>
<center><h1>COUNTY OF RIVERSIDE ET AL.<br>
v.<br>
McLAUGHLIN ET AL.</h1></center>
<center>No. 89-1817.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 7, 1991.</center>
<center>Decided May 13, 1991.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*46</span> <i>Timothy T. Coates</i> argued the cause for petitioners. With him on the briefs were <i>Peter J. Ferguson, Michael A. Bell,</i> and <i>Martin Stein.</i></p>
<p><i>Dan Stormer</i> argued the cause for respondents. With him on the brief were <i>Richard P. Herman, Ben Margolis,</i> and <i>Elizabeth Spector.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*47</span> JUSTICE O'CONNOR delivered the opinion of the Court.</p>
<p>In <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975), this Court held that the Fourth Amendment requires a prompt judicial determination of probable cause as a prerequisite to an extended pretrial detention following a warrantless arrest. This case requires us to define what is "prompt" under <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>.</i></p>
<p></p>
<h2>I</h2>
<p>This is a class action brought under <span class="citation no-link">42 U. S. C. § 1983</span> challenging the manner in which the County of Riverside, California (County), provides probable cause determinations to persons arrested without a warrant. At issue is the County's policy of combining probable cause determinations with its arraignment procedures. Under County policy, which tracks closely the provisions of Cal. Penal Code Ann. § 825 (West 1985), arraignments must be conducted without unnecessary delay and, in any event, within two days of arrest. This 2-day requirement excludes from computation weekends and holidays. Thus, an individual arrested without a warrant late in the week may in some cases be held for as long as five days before receiving a probable cause determination. Over the Thanksgiving holiday, a 7-day delay is possible.</p>
<p>The parties dispute whether the combined probable cause/arraignment procedure is available to <i>all</i> warrantless arrestees. Testimony by Riverside County District Attorney Grover Trask suggests that individuals arrested without <span class="star-pagination">*48</span> warrants for felonies do not receive a probable cause determination until the preliminary hearing, which may not occur until 10 days after arraignment. <span class="citation" data-id="6672116"><a href="/opinion/6787847/taylor-v-niles/" aria-description="Citation for case: Taylor v. Niles">2 App. 298</a></span>-299. Before this Court, however, the County represents that its policy is to provide probable cause determinations at arraignment for all persons arrested without a warrant, regardless of the nature of the charges against them. <i><span class="citation" data-id="6672116"><a href="/opinion/6787847/taylor-v-niles/" aria-description="Citation for case: Taylor v. Niles">Ibid.</a></span></i> See also Tr. of Oral Arg. 13. We need not resolve the factual inconsistency here. For present purposes, we accept the County's representation.</p>
<p>In August 1987, Donald Lee McLaughlin filed a complaint in the United States District Court for the Central District of California, seeking injunctive and declaratory relief on behalf of himself and "`all others similarly situated.'" The complaint alleged that McLaughlin was then currently incarcerated in the Riverside County Jail and had not received a probable cause determination. He requested "`an order and judgment requiring that the defendants and the County of Riverside provide in-custody arrestees, arrested without warrants, prompt probable cause, bail and arraignment hearings.'" Pet. for Cert. 6. Shortly thereafter, McLaughlin moved for class certification. The County moved to dismiss the complaint, asserting that McLaughlin lacked standing to bring the suit because he had failed to show, as required by <i>Los Angeles</i> v. <i>Lyons,</i> <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">461 U. S. 95</a></span> (1983), that he would again be subject to the allegedly unconstitutional conduct  <i>i. e.,</i> a warrantless detention without a probable cause determination.</p>
<p>In light of the pending motion to dismiss, the District Court continued the hearing on the motion to certify the class. Various papers were submitted; then, in July 1988, the District Court accepted for filing a second amended complaint, which is the operative pleading here. From the record it appears that the District Court never explicitly ruled on defendants' motion to dismiss, but rather took it off the court's calendar in August 1988.</p>
<p><span class="star-pagination">*49</span> The second amended complaint named three additional plaintiffs  Johnny E. James, Diana Ray Simon, and Michael Scott Hyde  individually and as class representatives. The amended complaint alleged that each of the named plaintiffs had been arrested without a warrant, had received neither a prompt probable cause nor a bail hearing, and was still in custody. <span class="citation" data-id="6671984"><a href="/opinion/6787716/betts-v-state/" aria-description="Citation for case: Betts v. State">1 App. 3</a></span>. In November 1988, the District Court certified a class comprising "all present and future prisoners in the Riverside County Jail including those pretrial detainees arrested without warrants and held in the Riverside County Jail from August 1, 1987 to the present, and all such future detainees who have been or may be denied prompt probable cause, bail or arraignment hearings." <span class="citation" data-id="6671984"><a href="/opinion/6787716/betts-v-state/" aria-description="Citation for case: Betts v. State">1 App. 7</a></span>.</p>
<p>In March 1989, plaintiffs asked the District Court to issue a preliminary injunction requiring the County to provide all persons arrested without a warrant a judicial determination of probable cause within 36 hours of arrest. <span class="citation" data-id="6671986"><a href="/opinion/6787718/tippie-v-state/" aria-description="Citation for case: Tippie v. State">1 App. 21</a></span>. The District Court issued the injunction, holding that the County's existing practice violated this Court's decision in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>.</i> Without discussion, the District Court adopted a rule that the County provide probable cause determinations within 36 hours of arrest, except in exigent circumstances. The court "retained jurisdiction indefinitely" to ensure that the County established new procedures that complied with the injunction. <span class="citation" data-id="6672123"><a href="/opinion/6787854/neave-building-co-v-roudebush/" aria-description="Citation for case: Neave Building Co. v. Roudebush">2 App. 333</a></span>-334.</p>
<p>The United States Court of Appeals for the Ninth Circuit consolidated this case with another challenging an identical preliminary injunction issued against the County of San Bernardino. See <i>McGregor</i> v. <i>County of San Bernardino,</i> decided with <i>McLaughlin</i> v. <i>County of Riverside,</i> <span class="citation" data-id="8975120"><a href="/opinion/8983199/mclaughlin-v-county-of-riverside/" aria-description="Citation for case: McLaughlin v. County of Riverside">888 F. 2d 1276</a></span> (1989).</p>
<p>On November 8, 1989, the Court of Appeals affirmed the order granting the preliminary injunction against Riverside County. One aspect of the injunction against San Bernardino County was reversed by the Court of Appeals; that determination is not before us.</p>
<p><span class="star-pagination">*50</span> The Court of Appeals rejected Riverside County's <i><span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span></i>-based standing argument, holding that the named plaintiffs had Article III standing to bring the class action for injunctive relief. <span class="citation" data-id="8975120"><a href="/opinion/8983199/mclaughlin-v-county-of-riverside/#1277" aria-description="Citation for case: McLaughlin v. County of Riverside">888 F. 2d, at 1277</a></span>. It reasoned that, at the time plaintiffs filed their complaint, they were in custody and suffering injury as a result of defendants' allegedly unconstitutional action. The court then proceeded to the merits and determined that the County's policy of providing probable cause determinations at arraignment within 48 hours was "not in accord with <i>Gerstein's</i> requirement of a determination `promptly after arrest'" because no more than 36 hours were needed "to complete the administrative steps incident to arrest." <span class="citation" data-id="8975120"><a href="/opinion/8983199/mclaughlin-v-county-of-riverside/#1278" aria-description="Citation for case: McLaughlin v. County of Riverside"><i>Id.,</i> at 1278</a></span>.</p>
<p>The Ninth Circuit thus joined the Fourth and Seventh Circuits in interpreting <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> as requiring a probable cause determination immediately following completion of the administrative procedures incident to arrest. <i>Llaguno</i> v. <i>Mingey,</i> <span class="citation" data-id="9473571"><a href="/opinion/453324/gloria-llaguno-v-edward-mingey/#1567" aria-description="Citation for case: Gloria Llaguno v. Edward Mingey">763 F. 2d 1560, 1567-1568</a></span> (CA7 1985) (en banc); <i>Fisher</i> v. <i>Washington Metropolitan Area Transit Authority,</i> <span class="citation" data-id="8915910"><a href="/opinion/8926233/fisher-v-washington-metropolitan-area-transit-authority/#1139" aria-description="Citation for case: Fisher v. Washington Metropolitan Area Transit Authority">690 F. 2d 1133, 1139-1141</a></span> (CA4 1982). By contrast, the Second Circuit understands <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> to "stres[s] the need for flexibility" and to permit States to combine probable cause determinations with other pretrial proceedings. <i>Williams</i> v. <i>Ward,</i> <span class="citation" data-id="8959859"><a href="/opinion/8968443/williams-v-ward/#386" aria-description="Citation for case: Williams v. Ward">845 F. 2d 374, 386</a></span> (1988), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./488/1020/">488 U. S. 1020</a></span> (1989). We granted certiorari to resolve this conflict among the Circuits as to what constitutes a "prompt" probable cause determination under <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>.</i></p>
<p></p>
<h2>II</h2>
<p>As an initial matter, the County renews its claim that plaintiffs lack standing. It explains that the main thrust of plaintiffs' suit is that they are entitled to "prompt" probable cause determinations and insists that this is, by definition, a time-limited violation. Once sufficient time has passed, the County argues, the constitutional violation is complete because a probable cause determination made after that point <span class="star-pagination">*51</span> would no longer be "prompt." Thus, at least as to the named plaintiffs, there is no standing because it is too late for them to receive a prompt hearing and, under <i><span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>,</i> they cannot show that they are likely to be subjected again to the unconstitutional conduct.</p>
<p>We reject the County's argument. At the core of the standing doctrine is the requirement that a plaintiff "allege personal injury fairly traceable to the defendant's allegedly unlawful conduct and likely to be redressed by the requested relief." <i>Allen</i> v. <i>Wright,</i> <span class="citation" data-id="9429754"><a href="/opinion/111258/allen-v-wright/#751" aria-description="Citation for case: Allen v. Wright">468 U. S. 737, 751</a></span> (1984), citing <i>Valley Forge Christian College,</i> v. <i>Americans United for Separation of Church and State, Inc.,</i> <span class="citation" data-id="9428574"><a href="/opinion/110599/valley-forge-christian-college-v-americans-united-for-separation-of-church/#472" aria-description="Citation for case: Valley Forge Christian College v. Americans United for...">454 U. S. 464, 472</a></span> (1982). The County does not dispute that, at the time the second amended complaint was filed, plaintiffs James, Simon, and Hyde had been arrested without warrants and were being held in custody without having received a probable cause determination, prompt or otherwise. Plaintiffs alleged in their complaint that they were suffering a direct and current injury as a result of this detention, and would continue to suffer that injury until they received the probable cause determination to which they were entitled. Plainly, plaintiffs' injury was at that moment capable of being redressed through injunctive relief. The County's argument that the constitutional violation had already been "completed" relies on a crabbed reading of the complaint. This case is easily distinguished from <i><span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>,</i> in which the constitutionally objectionable practice ceased altogether before the plaintiff filed his complaint.</p>
<p>It is true, of course, that the claims of the named plaintiffs have since been rendered moot; eventually, they either received probable cause determinations or were released. Our cases leave no doubt, however, that by obtaining class certification, plaintiffs preserved the merits of the controversy for our review. In factually similar cases we have held that "the termination of a class representative's claim does not moot the claims of the unnamed members of the class." See, <i>e. g.,</i> <span class="star-pagination">*52</span> <i>Gerstein,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#110" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 110-111, n. 11</a></span>, citing <i>Sosna</i> v. <i>Iowa,</i> <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">419 U. S. 393</a></span> (1975); <i>Schall</i> v. <i>Martin,</i> <span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/#256" aria-description="Citation for case: Schall v. Martin">467 U. S. 253, 256, n. 3</a></span> (1984). That the class was not certified until after the named plaintiffs' claims had become moot does not deprive us of jurisdiction. We recognized in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> that "[s]ome claims are so inherently transitory that the trial court will not have even enough time to rule on a motion for class certification before the proposed representative's individual interest expires." <i>United States Parole Comm'n</i> v. <i>Geraghty,</i> <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#399" aria-description="Citation for case: United States Parole Commission v. Geraghty">445 U. S. 388, 399</a></span> (1980), citing <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#110" aria-description="Citation for case: Gerstein v. Pugh"><i>Gerstein, supra,</i> at 110, n. 11</a></span>. In such cases, the "relation back" doctrine is properly invoked to preserve the merits of the case for judicial resolution. See <i>Swisher</i> v. <i>Brady,</i> <span class="citation" data-id="9427327"><a href="/opinion/109928/swisher-v-brady/#213" aria-description="Citation for case: Swisher v. Brady">438 U. S. 204, 213-214, n. 11</a></span> (1978); <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#402" aria-description="Citation for case: Sosna v. Iowa"><i>Sosna, supra,</i> at 402, n. 11</a></span>. Accordingly, we proceed to the merits.</p>
<p></p>
<h2>III</h2>
<p></p>
<h2>A</h2>
<p>In <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</i> this Court held unconstitutional Florida procedures under which persons arrested without a warrant could remain in police custody for 30 days or more without a judicial determination of probable cause. In reaching this conclusion we attempted to reconcile important competing interests. On the one hand, States have a strong interest in protecting public safety by taking into custody those persons who are reasonably suspected of having engaged in criminal activity, even where there has been no opportunity for a prior judicial determination of probable cause. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#112" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 112</a></span>. On the other hand, prolonged detention based on incorrect or unfounded suspicion may unjustly "imperil [a] suspect's job, interrupt his source of income, and impair his family relationships." <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 114</a></span>. We sought to balance these competing concerns by holding that States "must provide a fair and reliable determination of probable cause as a condition for any significant pretrial restraint of liberty, and this determination must be made by a judicial officer either before <i>or promptly after</i> arrest." <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#125" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 125</a></span> (emphasis added).</p>
<p><span class="star-pagination">*53</span> The Court thus established a "practical compromise" between the rights of individuals and the realities of law enforcement. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 113</a></span>. Under <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</i> warrantless arrests are permitted but persons arrested without a warrant must promptly be brought before a neutral magistrate for a judicial determination of probable cause. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 114</a></span>. Significantly, the Court stopped short of holding that jurisdictions were constitutionally compelled to provide a probable cause hearing immediately upon taking a suspect into custody and completing booking procedures. We acknowledged the burden that proliferation of pretrial proceedings places on the criminal justice system and recognized that the interests of everyone involved, including those persons who are arrested, might be disserved by introducing further procedural complexity into an already intricate system. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#119" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 119-123</a></span>. Accordingly, we left it to the individual States to integrate prompt probable cause determinations into their differing systems of pretrial procedures. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#123" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 123-124</a></span>.</p>
<p>In so doing, we gave proper deference to the demands of federalism. We recognized that "state systems of criminal procedure vary widely" in the nature and number of pretrial procedures they provide, and we noted that there is no single "preferred" approach. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#123" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 123</a></span>. We explained further that "flexibility and experimentation by the States" with respect to integrating probable cause determinations was desirable and that each State should settle upon an approach "to accord with [the] State's pretrial procedure viewed as a whole." <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Ibid.</a></span></i> Our purpose in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> was to make clear that the Fourth Amendment requires every State to provide prompt determinations of probable cause, but that the Constitution does not impose on the States a rigid procedural framework. Rather, individual States may choose to comply in different ways.</p>
<p>Inherent in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i>'s invitation to the States to experiment and adapt was the recognition that the Fourth Amendment does not compel an immediate determination of probable <span class="star-pagination">*54</span> cause upon completing the administrative steps incident to arrest. Plainly, if a probable cause hearing is constitutionally compelled the moment a suspect is finished being "booked," there is no room whatsoever for "flexibility and experimentation by the States." <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Ibid.</a></span></i> Incorporating probable cause determinations "into the procedure for setting bail or fixing other conditions of pretrial release" which <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> explicitly contemplated, <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">id.,</a></span></i> at 124would be impossible. Waiting even a few hours so that a bail hearing or arraignment could take place at the same time as the probable cause determination would amount to a constitutional violation. Clearly, <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> is not that inflexible.</p>
<p>Notwithstanding <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i>'s discussion of flexibility, the Court of Appeals for the Ninth Circuit held that no flexibility was permitted. It construed <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> as "requir[ing] a probable cause determination to be made <i>as soon as the administrative steps incident to arrest were completed,</i> and that such steps should require only a brief period." <span class="citation" data-id="8975120"><a href="/opinion/8983199/mclaughlin-v-county-of-riverside/#1278" aria-description="Citation for case: McLaughlin v. County of Riverside">888 F. 2d, at 1278</a></span> (emphasis added) (internal quotation marks omitted). This same reading is advanced by the dissents. See <i>post,</i> at 59 (opinion of MARSHALL, J.); <i>post,</i> at 61-63, 65 (opinion of SCALIA, J.). The foregoing discussion readily demonstrates the error of this approach. <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> held that probable cause determinations must be prompt  not immediate. The Court explained that "flexibility and experimentation" were "desirab[le]"; that"[t]here is no single preferred pretrial procedure"; and that "the nature of the probable cause determination usually will be shaped to accord with a State's pretrial procedure viewed as a whole." <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#123" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 123</a></span>. The Court of Appeals and JUSTICE SCALIA disregard these statements, relying instead on selective quotations from the Court's opinion. As we have explained, <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> struck a balance between competing interests; a proper understanding of the decision is possible only if one takes into account both sides of the equation.</p>
<p>JUSTICE SCALIA claims to find support for his approach in the common law. He points to several statements from the <span class="star-pagination">*55</span> early 1800's to the effect that an arresting officer must bring a person arrested without a warrant before a judicial officer "`as soon as he <i>reasonably</i> can.'" <i>Post,</i> at 61 (emphasis in original). This vague admonition offers no more support for the dissent's inflexible standard than does <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i>'s statement that a hearing follow "promptly after arrest." <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#125" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 125</a></span>. As mentioned at the outset, the question before us today is what is "prompt" under <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>.</i> We answer that question by recognizing that <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> struck a balance between competing interests.</p>
<p></p>
<h2>B</h2>
<p>Given that <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> permits jurisdictions to incorporate probable cause determinations into other pretrial procedures, some delays are inevitable. For example, where, as in Riverside County, the probable cause determination is combined with arraignment, there will be delays caused by paperwork and logistical problems. Records will have to be reviewed, charging documents drafted, appearance of counsel arranged, and appropriate bail determined. On weekends, when the number of arrests is often higher and available resources tend to be limited, arraignments may get pushed back even further. In our view, the Fourth Amendment permits a reasonable postponement of a probable cause determination while the police cope with the everyday problems of processing suspects through an overly burdened criminal justice system.</p>
<p>But flexibility has its limits; <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> is not a blank check. A State has no legitimate interest in detaining for extended periods individuals who have been arrested without probable cause. The Court recognized in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> that a person arrested without a warrant is entitled to a fair and reliable determination of probable cause and that this determination must be made promptly.</p>
<p>Unfortunately, as lower court decisions applying <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> have demonstrated, it is not enough to say that probable <span class="star-pagination">*56</span> cause determinations must be "prompt." This vague standard simply has not provided sufficient guidance. Instead, it has led to a flurry of systemic challenges to city and county practices, putting federal judges in the role of making legislative judgments and overseeing local jailhouse operations. See, <i>e. g., McGregor</i> v. <i>County of San Bernardino,</i> decided with <i>McLaughlin</i> v. <i>County of Riverside,</i> <span class="citation" data-id="8975120"><a href="/opinion/8983199/mclaughlin-v-county-of-riverside/" aria-description="Citation for case: McLaughlin v. County of Riverside">888 F. 2d 1276</a></span> (CA9 1989); <i>Scott</i> v. <i>Gates,</i> Civ. No. 84-8647 (CD Cal., Oct. 3, 1988); see also <i>Bernard</i> v. <i>Palo Alto,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/699/1023/">699 F. 2d 1023</a></span> (CA9 1983); <i>Sanders</i> v. <i>Houston,</i> <span class="citation" data-id="1460908"><a href="/opinion/1460908/sanders-v-city-of-houston/" aria-description="Citation for case: Sanders v. City of Houston">543 F. Supp. 694</a></span> (SD Tex. 1982), aff'd, <span class="citation multiple-matches"><a href="/c/F.%202d/741/1379/">741 F. 2d 1379</a></span> (CA5 1984); <i>Lively</i> v. <i>Cullinane,</i> <span class="citation" data-id="1897137"><a href="/opinion/1897137/lively-v-cullinane/" aria-description="Citation for case: Lively v. Cullinane">451 F. Supp. 1000</a></span> (DC 1978).</p>
<p>Our task in this case is to articulate more clearly the boundaries of what is permissible under the Fourth Amendment. Although we hesitate to announce that the Constitution compels a specific time limit, it is important to provide some degree of certainty so that States and counties may establish procedures with confidence that they fall within constitutional bounds. Taking into account the competing interests articulated in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</i> we believe that a jurisdiction that provides judicial determinations of probable cause within 48 hours of arrest will, as a general matter, comply with the promptness requirement of <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>.</i> For this reason, such jurisdictions will be immune from systemic challenges.</p>
<p>This is not to say that the probable cause determination in a particular case passes constitutional muster simply because it is provided within 48 hours. Such a hearing may nonetheless violate <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> if the arrested individual can prove that his or her probable cause determination was delayed unreasonably. Examples of unreasonable delay are delays for the purpose of gathering additional evidence to justify the arrest, a delay motivated by ill will against the arrested individual, or delay for delay's sake. In evaluating whether the delay in a particular case is unreasonable, however, courts must allow a substantial degree of flexibility. Courts cannot ignore the <span class="star-pagination">*57</span> often unavoidable delays in transporting arrested persons from one facility to another, handling late-night bookings where no magistrate is readily available, obtaining the presence of an arresting officer who may be busy processing other suspects or securing the premises of an arrest, and other practical realities.</p>
<p>Where an arrested individual does not receive a probable cause determination within 48 hours, the calculus changes. In such a case, the arrested individual does not bear the burden of proving an unreasonable delay. Rather, the burden shifts to the government to demonstrate the existence of a bona fide emergency or other extraordinary circumstance. The fact that in a particular case it may take longer than 48 hours to consolidate pretrial proceedings does not qualify as an extraordinary circumstance. Nor, for that matter, do intervening weekends. A jurisdiction that chooses to offer combined proceedings must do so as soon as is reasonably feasible, but in no event later than 48 hours after arrest.</p>
<p>JUSTICE SCALIA urges that 24 hours is a more appropriate outer boundary for providing probable cause determinations. See <i>post,</i> at 68. In arguing that any delay in probable cause hearings beyond completing the administrative steps incident to arrest and arranging for a magistrate is unconstitutional, JUSTICE SCALIA, in effect, adopts the view of the Court of Appeals. Yet he ignores entirely the Court of Appeals' determination of the time required to complete those procedures. That court, better situated than this one, concluded that it takes 36 hours to process arrested persons in Riverside County. <span class="citation" data-id="8975120"><a href="/opinion/8983199/mclaughlin-v-county-of-riverside/#1278" aria-description="Citation for case: McLaughlin v. County of Riverside">888 F. 2d, at 1278</a></span>. In advocating a 24-hour rule, JUSTICE SCALIA would compel Riverside County  and countless others across the Nation  to speed up its criminal justice mechanisms substantially, presumably by allotting local tax dollars to hire additional police officers and magistrates. There may be times when the Constitution compels such direct interference with local control, but this is not one. As we have explained, <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> clearly contemplated a reasonable <span class="star-pagination">*58</span> accommodation between legitimate competing concerns. We do no more than recognize that such accommodation can take place without running afoul of the Fourth Amendment.</p>
<p>Everyone agrees that the police should make every attempt to minimize the time a presumptively innocent individual spends in jail. One way to do so is to provide a judicial determination of probable cause immediately upon completing the administrative steps incident to arrest<i>i. e.,</i> as soon as the suspect has been booked, photographed, and fingerprinted. As JUSTICE SCALIA explains, several States, laudably, have adopted this approach. The Constitution does not compel so rigid a schedule, however. Under <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</i> jurisdictions may choose to combine probable cause determinations with other pretrial proceedings, so long as they do so promptly. This necessarily means that only certain proceedings are candidates for combination. Only those proceedings that arise very early in the pretrial processsuch as bail hearings and arraignments  may be chosen. Even then, every effort must be made to expedite the combined proceedings. See <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#124" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 124</a></span>.</p>
<p></p>
<h2>IV</h2>
<p>For the reasons we have articulated, we conclude that Riverside County is entitled to combine probable cause determinations with arraignments. The record indicates, however, that the County's current policy and practice do not comport fully with the principles we have outlined. The County's current policy is to offer combined proceedings within two days, exclusive of Saturdays, Sundays, or holidays. As a result, persons arrested on Thursdays may have to wait until the following Monday before they receive a probable cause determination. The delay is even longer if there is an intervening holiday. Thus, the County's regular practice exceeds the 48-hour period we deem constitutionally <span class="star-pagination">*59</span> permissible, meaning that the County is not immune from systemic challenges, such as this class action.</p>
<p>As to arrests that occur early in the week, the County's practice is that "arraignment[s] usually tak[e] place on the last day" possible. <span class="citation" data-id="6671997"><a href="/opinion/6787728/standard-oil-co-v-hopkins/" aria-description="Citation for case: Standard Oil Co. v. Hopkins">1 App. 82</a></span>. There may well be legitimate reasons for this practice; alternatively, this may constitute delay for delay's sake. We leave it to the Court of Appeals and the District Court, on remand, to make this determination.</p>
<p>The judgment of the Court of Appeals is vacated, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE MARSHALL, with whom JUSTICE BLACKMUN and JUSTICE STEVENS join, dissenting.</p>
<p>In <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975), this Court held that an individual detained following a warrantless arrest is entitled to a "prompt" judicial determination of probable cause as a prerequisite to any further restraint on his liberty. See <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh"><i>id.,</i> at 114-116, 125</a></span>. I agree with JUSTICE SCALIA that a probable-cause hearing is sufficiently "prompt" under <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> only when provided immediately upon completion of the "administrative steps incident to arrest," <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh"><i>id.,</i> at 114</a></span>. See <i>post,</i> at 62-63. Because the Court of Appeals correctly held that the County of Riverside must provide probable-cause hearings as soon as it completes the administrative steps incident to arrest, see <span class="citation multiple-matches"><a href="/c/F.%202d/888/1276/">888 F. 2d 1276</a></span>, 1278 (CA9 1989), I would affirm the judgment of the Court of Appeals. Accordingly, I dissent.</p>
<p>JUSTICE SCALIA, dissenting.</p>
<p>The story is told of the elderly judge who, looking back over a long career, observes with satisfaction that "when I was young, I probably let stand some convictions that should have been overturned, and when I was old, I probably set aside some that should have stood; so overall, justice was <span class="star-pagination">*60</span> done." I sometimes think that is an appropriate analog to this Court's constitutional jurisprudence, which alternately creates rights that the Constitution does not contain and denies rights that it does. Compare <i>Roe</i> v. <i>Wade,</i> <span class="citation" data-id="9425157"><a href="/opinion/108713/roe-v-wade/" aria-description="Citation for case: Roe v. Wade">410 U. S. 113</a></span> (1973) (right to abortion does exist), with <i>Maryland</i> v. <i>Craig,</i> <span class="citation" data-id="9842114"><a href="/opinion/112489/maryland-v-craig/" aria-description="Citation for case: Maryland v. Craig">497 U. S. 836</a></span> (1990) (right to be confronted with witnesses, U. S. Const., Amdt. 6, does not). Thinking that neither the one course nor the other is correct, nor the two combined, I dissent from today's decision, which eliminates a very old right indeed.</p>
<p></p>
<h2>I</h2>
<p>The Court views the task before it as one of "balanc[ing] [the] competing concerns" of "protecting public safety," on the one hand, and avoiding "prolonged detention based on incorrect or unfounded suspicion," on the other hand, <i>ante,</i> at 52. It purports to reaffirm the "`practical compromise'" between these concerns struck in <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975), <i>ante,</i> at 53. There is assuredly room for such an approach in resolving novel questions of search and seizure under the "reasonableness" standard that the Fourth Amendment sets forth. But not, I think, in resolving those questions on which a clear answer already existed in 1791 and has been generally adhered to by the traditions of our society ever since. As to those matters, the "balance" has already been struck, the "practical compromise" reachedand it is the function of the Bill of Rights to <i>preserve</i> that judgment, not only against the changing views of Presidents and Members of Congress, but also against the changing views of Justices whom Presidents appoint and Members of Congress confirm to this Court.</p>
<p>The issue before us today is of precisely that sort. As we have recently had occasion to explain, the Fourth Amendment's prohibition of "unreasonable seizures," insofar as it applies to seizure of the person, preserves for our citizens the traditional protections against unlawful arrest afforded by the common law. See <i>California</i> v. <i>Hodari D.,</i> 499 U. S. <span class="star-pagination">*61</span> 621 (1991). One of thoseone of the most important of thosewas that a person arresting a suspect without a warrant must deliver the arrestee to a magistrate "as soon as he reasonably can." 2 M. Hale, Pleas of the Crown 95, n. 13 (1st Am. ed. 1847). See also 4 W. Blackstone, Commentaries *289, *293; <i>Wright</i> v. <i>Court,</i> 107 Eng. Rep. 1182 (K. B. 1825) ("[I]t is the duty of a person arresting any one on suspicion of felony to take him before a justice as soon as he reasonably can"); 1 R. Burn, Justice of the Peace 276-277 (1837) ("When a constable arrests a party for treason or felony, he must take him before a magistrate to be examined as soon as he <i>reasonably</i> can") (emphasis omitted). The practice in the United States was the same. See, <i>e. g.,</i> 5 Am. Jur. 2d, Arrest §§ 76, 77 (1962); <i>Venable</i> v. <i>Huddy,</i> 77 N. J. L. 351, <span class="citation" data-id="8063376"><a href="/opinion/8102806/venable-v-huddy/#11" aria-description="Citation for case: Venable v. Huddy">72 A. 10, 11</a></span> (1909); <i>Atchison, T. &amp; S. F. R. Co.</i> v. <i>Hinsdell,</i> <span class="citation" data-id="7897287"><a href="/opinion/7946415/atchison-topeka-santa-fe-railway-co-v-hinsdell/#76" aria-description="Citation for case: Atchison, Topeka &amp; Santa Fe Railway Co. v. Hinsdell">76 Kan. 74, 76</a></span>, <span class="citation" data-id="7897287"><a href="/opinion/7946415/atchison-topeka-santa-fe-railway-co-v-hinsdell/#801" aria-description="Citation for case: Atchison, Topeka &amp; Santa Fe Railway Co. v. Hinsdell">90 P. 800, 801</a></span> (1907); <i>Ocean S. S. Co.</i> v. <i>Williams,</i> <span class="citation" data-id="5560588"><a href="/opinion/5710587/ocean-steamship-co-v-williams/#262" aria-description="Citation for case: Ocean Steamship Co. v. Williams">69 Ga. 251, 262</a></span> (1883); <i>Johnson</i> v. <i>Mayor and City Council of Americus,</i> <span class="citation" data-id="5556139"><a href="/opinion/5706294/johnson-v-mayor-of-americus/#86" aria-description="Citation for case: Johnson v. Mayor of Americus">46 Ga. 80, 86-87</a></span> (1872); <i>Low</i> v. <i>Evans,</i> <span class="citation" data-id="7035354"><a href="/opinion/7127998/low-v-evans/#489" aria-description="Citation for case: Low v. Evans">16 Ind. 486, 489</a></span> (1861); <i>Tubbs</i> v. <i>Tukey,</i> <span class="citation" data-id="6409182"><a href="/opinion/6535463/tubbs-v-tukey/#440" aria-description="Citation for case: Tubbs v. Tukey">57 Mass. 438, 440</a></span> (1849) (warrant); Perkins, The Law of Arrest, <span class="citation no-link">25 Iowa L. Rev. 201</span>, 254 (1940). Cf. <i>Pepper</i> v. <i>Mayes,</i> <span class="citation" data-id="7131493"><a href="/opinion/7219422/pepper-v-mayes/" aria-description="Citation for case: Pepper v. Mayes">81 Ky. 673</a></span> (1884). It was clear, moreover, that the only element bearing upon the reasonableness of delay was not such circumstances as the pressing need to conduct further investigation, but the arresting officer's ability, once the prisoner had been secured, to reach a magistrate who could issue the needed warrant for further detention. 5 Am. Jur. 2d, Arrest, <i>supra,</i> §§ 76, 77; 1 Restatement of Torts § 134, Comment <i>b</i> (1934); <i>Keefe</i> v. <i>Hart,</i> <span class="citation" data-id="6432068"><a href="/opinion/6558320/keefe-v-hart/#482" aria-description="Citation for case: Keefe v. Hart">213 Mass. 476, 482</a></span>, <span class="citation no-link">100 N. E. 558</span>, 559 (1913); <i>Leger</i> v. <i>Warren,</i> <span class="citation no-link">57 N. E. 506</span>, 508 (Ohio 1900); <i>Burk</i> v. <i>Howley,</i> <span class="citation" data-id="6244102"><a href="/opinion/6375147/burk-v-howley/#551" aria-description="Citation for case: Burk v. Howley">179 Pa. 539, 551</a></span>, <span class="citation" data-id="6244102"><a href="/opinion/6375147/burk-v-howley/#329" aria-description="Citation for case: Burk v. Howley">36 A. 327, 329</a></span> (1897); <i>Kirk &amp; Son</i> v. <i>Garrett,</i> <span class="citation" data-id="7899815"><a href="/opinion/7948804/samuel-kirk-son-v-garrett/#405" aria-description="Citation for case: Samuel Kirk &amp; Son v. Garrett">84 Md. 383, 405</a></span>, <span class="citation" data-id="7899815"><a href="/opinion/7948804/samuel-kirk-son-v-garrett/#1091" aria-description="Citation for case: Samuel Kirk &amp; Son v. Garrett">35 A. 1089, 1091</a></span> (1896); <i>Simmons</i> v. <i>Vandyke,</i> <span class="citation" data-id="7052128"><a href="/opinion/7144005/simmons-v-vandyke/#384" aria-description="Citation for case: Simmons v. Vandyke">138 Ind. 380, 384</a></span>, <span class="citation" data-id="7052128"><a href="/opinion/7144005/simmons-v-vandyke/#974" aria-description="Citation for case: Simmons v. Vandyke">37 N. E. 973, 974</a></span> (1894) (dictum); <i>Ocean S. S. Co.</i> v. <i>Williams, supra,</i> at 263; <i>Hayes</i> v. <i>Mitchell,</i> <span class="citation" data-id="6511173"><a href="/opinion/6634615/hayes-v-mitchell/#455" aria-description="Citation for case: Hayes v. Mitchell">69 Ala. 452, 455</a></span> (1881); <i>Kenerson</i> v. <i>Bacon,</i> <span class="citation" data-id="6578751"><a href="/opinion/6698748/kenerson-v-bacon/#577" aria-description="Citation for case: Kenerson v. Bacon">41 Vt. 573, 577</a></span> (1869); <i>Green</i> v. <i>Kennedy,</i> 48 N. Y. <span class="star-pagination">*62</span> 653, 654 (1871); <i>Schneider</i> v. <i>McLane,</i> <span class="citation" data-id="5649143"><a href="/opinion/5794247/schneider-v-mclane/" aria-description="Citation for case: Schneider v. McLane">3 Keyes 568</a></span> (NY App. 1867); Annot., 51 L. R. A. 216 (1901). Cf. <i>Wheeler</i> v. <i>Nesbitt,</i> <span class="citation" data-id="87431"><a href="/opinion/87431/wheeler-v-nesbitt/#552" aria-description="Citation for case: Wheeler v. Nesbitt">24 How. 544, 552</a></span> (1860). Any detention beyond the period within which a warrant could have been obtained rendered the officer liable for false imprisonment. See, <i>e. g., </i><i>Twilley</i> v. <i>Perkins,</i> <span class="citation" data-id="7898815"><a href="/opinion/7947840/twilley-v-perkins/#265" aria-description="Citation for case: Twilley v. Perkins">77 Md. 252, 265</a></span>, <span class="citation no-link">26 A. 286</span>, 289 (1893); <i>Wiggins</i> v. <i>Norton,</i> <span class="citation" data-id="5563430"><a href="/opinion/5713393/wiggins-v-norton/#152" aria-description="Citation for case: Wiggins v. Norton">83 Ga. 148, 152</a></span>, <span class="citation" data-id="5563430"><a href="/opinion/5713393/wiggins-v-norton/#608" aria-description="Citation for case: Wiggins v. Norton">9 S. E. 607, 608-609</a></span> (1889); <i>Brock</i> v. <i>Stimson,</i> <span class="citation" data-id="6416703"><a href="/opinion/6542977/brock-v-stimson/" aria-description="Citation for case: Brock v. Stimson">108 Mass. 520</a></span> (1871); Annot., 98 A. L. R. 2d 966 (1964).<sup>[1]</sup></p>
<p>We discussed and relied upon this common-law understanding in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</i> see <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 114-116</a></span>, holding that the period of warrantless detention must be limited to the time necessary to complete the arrest and obtain the magistrate's review.</p>
<blockquote>"[A] policeman's on-the-scene assessment of probable cause provides legal justification for arresting a person suspected of crime, and for a <i>brief period of detention to take the administrative steps incident to arrest.</i> Once the suspect is in custody . . . the reasons that justify dispensing <span class="star-pagination">*63</span> with the magistrate's neutral judgment <i>evaporate.</i>" <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 113-114</a></span> (emphasis added).</blockquote>
<p>We said that "the Fourth Amendment requires a judicial determination of probable cause as a prerequisite to extended restraint of liberty," <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh"><i>id.,</i> at 114</a></span>, "either before or promptly after arrest," <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#125" aria-description="Citation for case: Gerstein v. Pugh"><i>id.,</i> at 125</a></span>. Though <i>how</i> "promptly" we did not say, it was plain enough that the requirement left no room for intentional delay unrelated to the completion of "the administrative steps incident to arrest." Plain enough, at least, that all but one federal court considering the question understood <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> that way. See, <i>e. g., </i><i>Gramenos</i> v. <i>Jewel Companies, Inc.,</i> <span class="citation" data-id="474259"><a href="/opinion/474259/james-n-gramenos-v-jewel-companies-inc/#437" aria-description="Citation for case: James N. Gramenos v. Jewel Companies, Inc.">797 F. 2d 432, 437</a></span> (CA7 1986), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./481/1028/">481 U. S. 1028</a></span> (1987); <i>Bernard</i> v. <i>Palo Alto,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/699/1023/">699 F. 2d 1023</a></span>, 1025 (CA9 1983) <i>(per curiam)</i><i>; </i><i>Fisher</i> v. <i>Washington Metropolitan Area Transit Authority,</i> <span class="citation" data-id="8915910"><a href="/opinion/8926233/fisher-v-washington-metropolitan-area-transit-authority/#1140" aria-description="Citation for case: Fisher v. Washington Metropolitan Area Transit Authority">690 F. 2d 1133, 1140</a></span> (CA4 1982); <i>Mabry</i> v. <i>County of Kalamazoo,</i> <span class="citation" data-id="1398635"><a href="/opinion/1398635/mabry-v-county-of-kalamazoo/#914" aria-description="Citation for case: Mabry v. County of Kalamazoo">626 F. Supp. 912, 914</a></span> (WD Mich. 1986); <i>Sanders</i> v. <i>Houston,</i> <span class="citation" data-id="1460908"><a href="/opinion/1460908/sanders-v-city-of-houston/#699" aria-description="Citation for case: Sanders v. City of Houston">543 F. Supp. 694, 699-701</a></span> (SD Tex. 1982), aff'd, <span class="citation multiple-matches"><a href="/c/F.%202d/741/1379/">741 F. 2d 1379</a></span> (CA5 1984); <i>Lively</i> v. <i>Cullinane,</i> <span class="citation" data-id="1897137"><a href="/opinion/1897137/lively-v-cullinane/#1004" aria-description="Citation for case: Lively v. Cullinane">451 F. Supp. 1000, 1004</a></span> (DC 1978). See also <i>People ex rel. Maxian</i> v. <i>Brown,</i> 164 App. Div. 2d 56, 62-64, 561 N. Y. S. 2d 418, 421-422 (1990), aff'd, 77 N. Y. 2d 422 (1991); Note, <i>Williams</i> v. <i><span class="citation" data-id="8959859"><a href="/opinion/8968443/williams-v-ward/" aria-description="Citation for case: Williams v. Ward">Ward</a></span>:</i> Compromising the Constitutional Right to Prompt Determination of Probable Cause Upon Arrest, <span class="citation no-link">74 Minn. L. Rev. 196</span>, 204 (1989). But see <i>Williams</i> v. <i>Ward,</i> <span class="citation" data-id="8959859"><a href="/opinion/8968443/williams-v-ward/" aria-description="Citation for case: Williams v. Ward">845 F. 2d 374</a></span> (CA2 1988), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./488/1020/">488 U. S. 1020</a></span> (1989).</p>
<p>Today, however, the Court discerns something quite different in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>.</i> It finds that the plain statements set forth above (not to mention the common-law tradition of liberty upon which they were based) were trumped by the <i>implication</i> of a later dictum in the case which, according to the Court, manifests a "recognition that the Fourth Amendment does <i>not</i> compel an immediate determination of probable cause upon completing the administrative steps incident to arrest." <i>Ante,</i> at 53-54 (emphasis added). Of course <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> did not say, nor do <i>I</i> contend, that an "immediate" determination <span class="star-pagination">*64</span> is required. But what the Court today means by "not immediate" is that the delay can be attributable to something other than completing the administrative steps incident to arrest and arranging for the magistratenamely, to the administrative convenience of combining the probable-cause determination with other state proceedings. The result, we learn later in the opinion, is that what <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> meant by "a brief period of detention to take the administrative steps incident to arrest" is two full days. I think it is clear that the case neither said nor meant any such thing.</p>
<p>Since the Court's opinion hangs so much upon <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</i> it is worth quoting the allegedly relevant passage in its entirety.</p>
<blockquote>"Although we conclude that the Constitution does not require an adversary determination of probable cause, we recognize that state systems of criminal procedure vary widely. There is no single preferred pretrial procedure, and the nature of the probable cause determination usually will be shaped to accord with a State's pretrial procedure viewed as a whole. While we limit our holding to the precise requirement of the Fourth Amendment, we recognize the desirability of flexibility and experimentation by the States. It may be found desirable, for example, to make the probable cause determination at the suspect's first appearance before a judicial officer,. . . or the determination may be incorporated into the procedure for setting bail or fixing other conditions of pretrial release. In some States, existing procedures may satisfy the requirement of the Fourth Amendment. Others may require only minor adjustment, <i>such as acceleration of existing preliminary hearings.</i> Current proposals for criminal procedure reform suggest other ways of testing probable cause for detention. Whatever procedure a State may adopt, it must provide a fair and reliable determination of probable cause as a condition for any significant pretrial restraint of liberty, and this <span class="star-pagination">*65</span> determination must be made by a judicial officer <i>either before or promptly after arrest.</i>" <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#123" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 123-125</a></span> (footnotes omitted; emphasis added).</blockquote>
<p>The Court's holding today rests upon the statement that "we recognize the desirability of flexibility and experimentation." But in its context that statement plainly refers to the <i>nature</i> of the hearing and not to its <i>timing.</i> That the timing is a given and a constant is plain from the italicized phrases, especially that which concludes the relevant passage. The timing <i>is</i> specifically addressed in the previously quoted passage of the opinion, which makes clear that "promptly after arrest" means upon completion of the "administrative steps incident to arrest." It is not apparent to me, as it is to the Court, that on these terms "[i]ncorporating probable cause determinations `into the procedure for setting bail or fixing other conditions of pretrial release' . . . would be impossible," <i>ante,</i> at 54; but it is clear that, if and when it is impossible, <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> envisioned that the procedural "experimentation," rather than the Fourth Amendment's requirement of prompt presentation to a magistrate, would have to yield.</p>
<p>Of course even if the implication of the dictum in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> were what the Court says, that would be poor reason for keeping a wrongfully arrested citizen in jail contrary to the clear dictates of the Fourth Amendment. What is most revealing of the frailty of today's opinion is that it relies upon <i>nothing</i> but that implication from a dictum, plus its own (quite irrefutable because entirely value laden) "balancing" of the competing demands of the individual and the State. With respect to the point at issue here, different times and different placeseven highly liberal times and placeshave struck that balance in different ways. Some Western democracies currently permit the executive a period of detention without impartially adjudicated cause. In England, for example, the Prevention of Terrorism Act 1989, §§ 14(4), 5, permits suspects to be held without presentation and without charge for seven days. 12 Halsbury's Stat. 1294 (4th <span class="star-pagination">*66</span> ed. 1989). It was the purpose of the Fourth Amendment to put this matter beyond time, place, and judicial predilection, incorporating the traditional common-law guarantees against unlawful arrest. The Court says not a word about these guarantees, and they are determinative. <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i>'s approval of a "brief period" of delay to accomplish "administrative steps incident to an arrest" is already a questionable extension of the traditional formulation, though it probably has little practical effect and can perhaps be justified on <i>de minimis</i> grounds.<sup>[2]</sup> To expand <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</i> however, into an authorization for 48-hour detention related neither to the obtaining of a magistrate nor the administrative "completion" of the arrest seems to me utterly unjustified. Mr. McLaughlin was entitled to have a <i>prompt</i> impartial determination that there was reason to deprive him of his libertynot according to a schedule that suits the State's convenience in piggybacking various proceedings, but as soon as his arrest was completed and the magistrate could be procured.</p>
<p></p>
<h2>II</h2>
<p>I have finished discussing what I consider the principal question in this case, which is what factors determine whether the postarrest determination of probable cause has been (as the Fourth Amendment requires) "reasonably prompt." The Court and I both accept two of those factors, completion of the administrative steps incident to arrest and arranging for a magistrate's probable-cause determination. Since we disagree, however, upon a third factorthe Court <span class="star-pagination">*67</span> believing, as I do not, that "combining" the determination with other proceedings justifies a delaywe necessarily disagree as well on the subsequent question, which can be described as the question of the absolute time limit. Any determinant of "reasonable promptness" that is within the control of the State (as the availability of the magistrate, the personnel and facilities for completing administrative procedures incident to arrest, and the timing of "combined procedures" all are) must be restricted by some outer time limit, or else the promptness guarantee would be worthless. If, for example, it took a full year to obtain a probable-cause determination in California because only a single magistrate had been authorized to perform that function throughout the State, the hearing would assuredly not qualify as "reasonably prompt." At some point, legitimate reasons for delay become illegitimate.</p>
<p>I do not know how the Court calculated its outer limit of 48 hours. I must confess, however, that I do not know how I would do so either, if I thought that one justification for delay could be the State's "desire to combine." There are no standards for "combination," and as we acknowledged in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> the various procedures that might be combined "vary widely" from State to State. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#123" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 123</a></span>. So as far as I can discern (though I cannot pretend to be able to do better), the Court simply decided that, given the administrative convenience of "combining," it is not so bad for an utterly innocent person to wait 48 hours in jail before being released.</p>
<p>If one eliminates (as one should) that novel justification for delay, determining the outer boundary of reasonableness is a more objective and more manageable task. We were asked to undertake it in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</i> but declinedwisely, I think, since we had before us little data to support any figure we might choose. As the Court notes, however, <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> has engendered a number of cases addressing not only the scope of the procedures "incident to arrest," but also their duration. <span class="star-pagination">*68</span> The conclusions reached by the judges in those cases, and by others who have addressed the question, are surprisingly similar. I frankly would prefer even more information, and for that purpose would have supported reargument on the single question of an outer time limit. The data available are enough to convince me, however, that certainly no more than 24 hours is needed.<sup>[3]</sup></p>
<p>With one exception, no federal court considering the question has regarded 24 hours as an inadequate amount of time to complete arrest procedures, and with the same exception every court actually setting a limit for a probable-cause determination based on those procedures has selected 24 <span class="star-pagination">*69</span> hours. (The exception would not count Sunday within the 24-hour limit.) See <i>Bernard</i> v. <i>Palo Alto,</i> 699 F. 2d, at 1025; <i>McGill</i> v. <i>Parsons,</i> <span class="citation" data-id="334165"><a href="/opinion/334165/frederick-mcgill-v-james-c-parsons/#485" aria-description="Citation for case: Frederick McGill v. James C. Parsons">532 F. 2d 484, 485</a></span> (CA5 1976); <i>Sanders</i> v. <i>Houston,</i> <span class="citation" data-id="1460908"><a href="/opinion/1460908/sanders-v-city-of-houston/#701" aria-description="Citation for case: Sanders v. City of Houston">543 F. Supp., at 701-703</a></span>; <i>Lively</i> v. <i>Cullinane,</i> <span class="citation" data-id="1897137"><a href="/opinion/1897137/lively-v-cullinane/#1003" aria-description="Citation for case: Lively v. Cullinane">451 F. Supp., at 1003-1004</a></span>. Cf. <i>Dommer</i> v. <i>Hatcher,</i> <span class="citation" data-id="1482406"><a href="/opinion/1482406/dommer-v-hatcher/#1046" aria-description="Citation for case: Dommer v. Hatcher">427 F. Supp. 1040, 1046</a></span> (ND Ind. 1975) (24-hour maximum; 48 if Sunday included), rev'd in part, <span class="citation multiple-matches"><a href="/c/F.%202d/653/289/">653 F. 2d 289</a></span> (CA7 1981). See also <i>Gramenos</i> v. <i>Jewel Companies, Inc.,</i> <span class="citation" data-id="474259"><a href="/opinion/474259/james-n-gramenos-v-jewel-companies-inc/#437" aria-description="Citation for case: James N. Gramenos v. Jewel Companies, Inc.">797 F. 2d, at 437</a></span> (four hours "requires explanation"); Brandes, Post-Arrest Detention and the Fourth Amendment: Refining the Standard of <i>Gerstein</i> v. <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Pugh</a></span>,</i> 22 Colum. J. L. &amp; Soc. Prob. 445, 474-475 (1989). Federal courts have reached a similar conclusion in applying Federal Rule of Criminal Procedure 5(a), which requires presentment before a federal magistrate "without unnecessary delay." See, <i>e. g.,</i> Thomas, The Poisoned Fruit of Pretrial Detention, 61 N. Y. U. L. Rev. 413, 450, n. 238 (1986) (citing cases). And state courts have similarly applied a 24-hour limit under state statutes requiring presentment without "unreasonable delay." New York, for example, has concluded that no more than 24 hours is necessary from arrest to <i>arraignment, People ex rel. Maxian</i> v. <i>Brown,</i> 164 App. Div. 2d, at 62-64, 561 N. Y. S. 2d, at 421-422. Twenty-nine States have statutes similar to New York's, which require either presentment or arraignment "without unnecessary delay" or "forthwith"; eight States explicitly require presentment or arraignment within 24 hours; and only seven States have statutes explicitly permitting a period longer than 24 hours. Brandes, <i>supra,</i> at 478, n. 230. Since the States requiring a probable-cause hearing within 24 hours include both New York and Alaska, it is unlikely that circumstances of population or geography demand a longer period. Twenty-four hours is consistent with the American Law Institute's Model Code. ALI, Model Code of Pre-Arraignment Procedure § 310.1 (1975). And while the American Bar Association in its proposed rules of criminal procedure initially required that presentment simply be <span class="star-pagination">*70</span> made "without unnecessary delay," it has recently concluded that no more than six hours should be required, except at night. Uniform Rules of Criminal Procedure, 10 U. L. A. App., Criminal Justice Standard 10-4.1 (Spec. Pamph. 1987). Finally, the conclusions of these commissions and judges, both state and federal, are supported by commentators who have examined the question. See, <i>e. g.,</i> Brandes, <i>supra,</i> at 478-485 (discussing national 24-hour rule); Note, 74 Minn. L. Rev., at 207-209.</p>
<p>In my view, absent extraordinary circumstances, it is an "unreasonable seizure" within the meaning of the Fourth Amendment for the police, having arrested a suspect without a warrant, to delay a determination of probable cause for the arrest either (1) for reasons unrelated to arrangement of the probable-cause determination or completion of the steps incident to arrest, or (2) beyond 24 hours after the arrest. Like the Court, I would treat the time limit as a presumption; when the 24 hours are exceeded the burden shifts to the police to adduce unforeseeable circumstances justifying the additional delay.</p>
<p></p>
<h2>* * *</h2>
<p>A few weeks before issuance of today's opinion there appeared in the Washington Post the story of protracted litigation arising from the arrest of a student who entered a restaurant in Charlottesville, Virginia, one evening, to look for some friends. Failing to find them, he tried to leavebut refused to pay a $5 fee (required by the restaurant's posted rules) for failing to return a red tab he had been issued to keep track of his orders. According to the story, he "was taken by police to the Charlottesville jail" at the restaurant's request. "There, a magistrate refused to issue an arrest warrant," and he was released. Washington Post, Apr. 29, 1991, p. 1. That is how it used to be; but not, according to today's decision, how it must be in the future. If the Fourth Amendment meant then what the Court says it does now, the student could lawfully have been held for as long as it would <span class="star-pagination">*71</span> have taken to arrange for his arraignment, up to a maximum of 48 hours.</p>
<p>Justice Story wrote that the Fourth Amendment "is little more than the affirmance of a great constitutional doctrine of the common law." 3 J. Story, Commentaries on the Constitution 748 (1833). It should not become less than that. One hears the complaint, nowadays, that the Fourth Amendment has become constitutional law for the guilty; that it benefits the career criminal (through the exclusionary rule) often and directly, but the ordinary citizen remotely if at all. By failing to protect the innocent arrestee, today's opinion reinforces that view. The common-law rule of <i>prompt</i> hearing had as its primary beneficiaries the innocentnot those whose fully justified convictions must be overturned to scold the police; nor those who avoid conviction because the evidence, while convincing, does not establish guilt beyond a reasonable doubt; but those so blameless that there was not even good reason to arrest them. While in recent years we have invented novel applications of the Fourth Amendment to release the unquestionably guilty, we today repudiate one of its core applications so that the presumptively innocent may be left in jail. Hereafter a law-abiding citizen wrongfully arrested may be compelled to await the grace of a Dickensian bureaucratic machine, as it churns its cycle for up to two daysnever once given the opportunity to show a judge that there is absolutely no reason to hold him, that a mistake has been made. In my view, this is the image of a system of justice that has lost its ancient sense of priority, a system that few Americans would recoguize as our own.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the State of California by <i>John K. Van de Kamp,</i> Attorney General, <i>Richard B. Iglehart,</i> Chief Assistant Attorney General, <i>Harley D. Mayfield,</i> Senior Assistant Attorney General, and <i>Robert M. Foster</i> and <i>Frederick R. Millar, Jr.,</i> Supervising Deputy Attorneys General; and for the District Attorney, County of Riverside, California, by <i>Grover C. Trask II, pro se.</i>
</p>
<p><i>Robert M. Rotstein, John A. Powell, Paul L. Hoffman,</i> and <i>Judith Resnik</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging affirmance.</p>
<p>Briefs of <i>amici curiae</i> were filed for the State of Hawaii et al. by <i>Warren Price III,</i> Attorney General of Hawaii, and <i>Steven S. Michaels,</i> Deputy Attorney General, <i>Don Siegelman,</i> Attorney General of Alabama, <i>Ron Fields,</i> Attorney General of Arkansas, <i>John J. Kelly,</i> Chief State's Attorney of Connecticut, <i>Charles M. Oberly III,</i> Attorney General of Delaware, <i>James T. Jones,</i> Attorney General of Idaho, <i>Neil F. Hartigan,</i> Attorney General of Illinois, <i>Linley E. Pearson,</i> Attorney General of Indiana, <i>James E. Tierney,</i> Attorney General of Maine, <i>Frank J. Kelley,</i> Attorney General of Michigan, <i>Mike Moore,</i> Attorney General of Mississippi, <i>Marc Racicot,</i> Attorney General of Montana, <i>Robert M. Spire,</i> Attorney General of Nebraska, <i>Robert J. Del Tufo,</i> Attorney General of New Jersey, <i>John</i> <i>P. Arnold,</i> Attorney General of New Hampshire, <i>Hal Stratton,</i> Attorney General of New Mexico, <i>Brian McKay,</i> Attorney General of Nevada, <i>Lacy H. Thornburg,</i> Attorney General of North Carolina, <i>Robert H. Henry,</i> Attorney General of Oklahoma, <i>T. Travis Medlock,</i> Attorney General of South Carolina, <i>Roger A. Tellinghuisen,</i> Attorney General of South Dakota, <i>Jeffrey L. Amestoy,</i> Attorney General of Vermont, and <i>Joseph P. Meyer,</i> Attorney General of Wyoming; for the County of Los Angeles et al. by <i>De Witt W. Clinton</i> and <i>Dixon M. Holston;</i> for the California District Attorneys Association by <i>Michael R. Capizzi;</i> and for the Youth Law Center by <i>Mark I. Soler</i> and <i>Loren M. Warboys.</i></p>
<p>[1]  The Court dismisses reliance upon the common law on the ground that its "vague admonition" to the effect that "an arresting officer must bring a person arrested without a warrant before a judicial officer `as soon as he <i>reasonably</i> can'" provides no more support than does <i>Gerstein</i> v. <i>Pugh</i>'s, <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975), "promptly after arrest" language for the "inflexible standard" that I propose. <i>Ante,</i> at 55. This response totally confuses the present portion of my opinion, which addresses the constitutionally permissible <i>reasons</i> for delay, with Part II below, which addresses (no more inflexibly, I may say, than the Court's 48-hour rule) the question of an outer time limit. The latterhow much time, <i>given the functions the officer is permitted to complete beforehand,</i> constitutes "as soon as he reasonably can" or "promptly after arrest"is obviously a function not of the common law but of helicopters and telephones. But what those delay-legitimating functions arewhether, for example, they include further investigation of the alleged crime or (as the Court says) "mixing" the probable-cause hearing with other proceedingsis assuredly governed by the common law, whose admonition on the point is not at all "vague": Only the function of arranging for the magistrate qualifies. The Court really has no response to this. It simply rescinds the common-law guarantee.</p>
<p>[2]  Ordinarily, I think, there would be plenty of time for "administrative steps" while the arrangements for a hearing are being made. But if, for example, a magistrate is present in the precinct and entertaining probable-cause hearings at the very moment a wrongfully arrested person is brought in, I see no basis for intentionally delaying the hearing in order to subject the person to a cataloging of his personal effects, fingerprinting, photographing, etc. He ought not be exposed to those indignities if there is no proper basis for constraining his freedom of movement, and if that can immediately be determined.</p>
<p>[3]  The Court claims that the Court of Appeals "concluded that it takes 36 hours to process arrested persons in Riverside County." <i>Ante,</i> at 57. The court concluded no such thing. It concluded that 36 hours (the time limit imposed by the District Court) was "ample" time to complete the arrest, <span class="citation multiple-matches"><a href="/c/F.%202d/888/1276/">888 F. 2d 1276</a></span>, 1278 (CA9 1989), and that the county had provided no evidence to demonstrate the contrary. The District Court, in turn, had not made any evidentiary finding to the effect that 36 hours was necessary, but for unexplained reasons said that it "declines to adopt the 24 hour standard [generally applied by other courts], but adopts a 36 hour limit, except in exigent circumstances." <i>McLaughlin</i> v. <i>County of Riverside,</i> No. CV87-5597 RG (CD Cal., Apr. 19, 1989). <span class="citation" data-id="6672123"><a href="/opinion/6787854/neave-building-co-v-roudebush/" aria-description="Citation for case: Neave Building Co. v. Roudebush">2 App. 332</a></span>. Before this Court, moreover, the county has acknowledged that "nearly 90 percent of all cases . . . can be completed in 24 hours or less," Brief for District Attorney, County of Riverside, as <i>Amicus Curiae</i> 16, and the examples given to explain the other 10 percent are entirely unpersuasive (heavy traffic on the southern California freeways; the need to wait for arrestees who are properly detainable because they are visibly under the influence of drugs to come out of that influence before they can be questioned about <i>other</i> crimes; the need to take blood and urine samples promptly in drug cases) with one exception: awaiting completion of investigations and filing of investigation reports by various state and federal agencies. <i>Id.,</i> at 16-17. We have long held, of course, that delaying a probable-cause determination for the latter reasoneffecting what Judge Posner has aptly called "imprisonment on suspicion, while the police look for evidence to confirm their suspicion," <i>Llaguno</i> v. <i>Mingey,</i> <span class="citation" data-id="9473571"><a href="/opinion/453324/gloria-llaguno-v-edward-mingey/#1568" aria-description="Citation for case: Gloria Llaguno v. Edward Mingey">763 F. 2d 1560, 1568</a></span> (CA7 1985)is improper. See <i>Gerstein,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#120" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 120, n. 21</a></span>, citing <i>Mallory</i> v. <i>United States,</i> <span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/#456" aria-description="Citation for case: Mallory v. United States">354 U. S. 449, 456</a></span> (1957).</p>

</div>
```

---
