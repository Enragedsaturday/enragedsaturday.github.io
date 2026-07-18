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

## GROUP: content/cases/Griffin v. Wisconsin.md  (`case`, 5 assertions)

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
{"assertion_id": "6787fb52897a4f3a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "483 U.S. 868 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 2897", "official_citation_present": true, "parallel_cite": "107 S. Ct. 3164; 97 L. Ed. 2d 709; 55 U.S.L.W. 5156", "title": "Griffin v. Wisconsin", "year": "1987"}}
{"assertion_id": "47f00af2364d21c8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless search of a probationer's home pursuant to a valid regulation is reasonable when supported by \\\"reasonable grounds\\\";…", "title": "Griffin v. Wisconsin"}}
{"assertion_id": "5dfa9956cb6b935a", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Progeny / Refinement", "title": "Griffin v. Wisconsin"}}
{"assertion_id": "08c6675f6e2ff19f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-06-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Griffin v. Wisconsin", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Griffin v. Wisconsin", "varies_by_point": "false"}}
{"assertion_id": "f519fbf1e54f9cb9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Griffin v. Wisconsin"}}
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

## GROUP: content/cases/Groh v. Ramirez.md  (`case`, 5 assertions)

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
{"assertion_id": "94767cf8266796a7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "540 U.S. 551 (2004)", "court": "U.S. Supreme Court", "neutral_cite": "2004 U.S. LEXIS 1624; 2004 WL 330057", "official_citation_present": true, "parallel_cite": "124 S. Ct. 1284; 157 L. Ed. 2d 1068", "title": "Groh v. Ramirez", "year": "2004"}}
{"assertion_id": "72cc06264a043b65", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrant that utterly **fails to describe the persons or things to be seized** is facially invalid under the Particularity Clause —…", "title": "Groh v. Ramirez"}}
{"assertion_id": "9c2838653e0f1b79", "dimension": "support", "kind": "home_role", "locator": {"home": "Particularity"}, "payload": {"home": "Particularity", "role": "Key — Progeny / Refinement", "title": "Groh v. Ramirez"}}
{"assertion_id": "1c85639dcffbacc7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Groh v. Ramirez"}}
{"assertion_id": "20af7391d8232866", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2004-02-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Groh v. Ramirez", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Groh v. Ramirez", "varies_by_point": "false"}}
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

## GROUP: content/cases/Hampton v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Hampton v. United States"
type: case
citation: "425 U.S. 484 (1976)"
parallel_cite: "96 S. Ct. 1646; 48 L. Ed. 2d 113"
neutral_cite: 1976 U.S. LEXIS 49
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-04-27
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-04-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hampton v. United States
  varies_by_point: false
  scope_note: "Plurality opinion (Rehnquist, J.); Powell & Blackmun concurred in the judgment on narrower grounds."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109437/hampton-v-united-states/"
  cluster_id: 109437
  opinion_id: 9426380
  identity_checked: true
homes:
  - page: "[[Entrapment]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Russell]]", "[[Sorrells v. United States]]", "[[Sherman v. United States]]"]
aliases: ["Hampton v. US"]
tags: ["case", "entrapment", "due-process", "predisposition", "outrageous-government-conduct"]
holding: "Neither the entrapment defense nor the Due Process Clause bars conviction of a PREDISPOSED defendant even where a government agent…"
lake:
  record_id: Hampton v. United States
  status: verified
  projected_at: 2026-07-06
---

# Hampton v. United States

*425 U.S. 484 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Hampton was convicted of selling heroin to undercover federal agents. He claimed that a government informant had supplied him the very heroin he then sold, and argued that the Government's furnishing the contraband barred his conviction. The jury was instructed that predisposition defeated entrapment, and Hampton's predisposition to commit the offense was established.

## Issue
Whether the Government's supplying the contraband that a predisposed defendant then sells bars his conviction — either under the entrapment defense or under the Due Process Clause.

## Rule
No. A predisposed defendant cannot claim entrapment, and — in the plurality's view — due process does not bar his conviction even where a government agent supplied the contraband. "The remedy of the criminal defendant with respect to the acts of Government agents, which, far from being resisted, are encouraged by him, lies solely in the defense of entrapment." — 425 U.S. at 490. ^pin-490

"If the police engage in illegal activity in concert with a defendant beyond the scope of their duties the remedy lies, not in freeing the equally culpable defendant, but in prosecuting the police under the applicable provisions of state or federal law." — *Id.* ^pin-490a

## Application
Hampton's predisposition to sell heroin was established, so the entrapment defense was unavailable to him. And although the informant allegedly supplied the drug, the police, the informant, and Hampton acted in concert, and that conduct deprived him of no constitutional right — so neither entrapment nor due process freed him. (Justices Powell and Blackmun concurred in the judgment but declined to hold that government supply of contraband can never violate due process.)

## Conclusion
The conviction was affirmed; the defendant's predisposition foreclosed the entrapment defense, and the Government's role in supplying the contraband did not bar the conviction.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hampton* is a plurality decision; its judgment forecloses entrapment for a predisposed defendant, while the broader due-process holding (no bar even when the Government supplies contraband) commanded only three votes, with Powell and Blackmun reserving the possibility of an outrageous-government-conduct due-process defense in a future case.

## Appears on
- [[Entrapment]] — *Key — Progeny / Refinement*

## Sources
- *Hampton v. United States*, 425 U.S. 484 (1976) — https://www.courtlistener.com/opinion/109437/hampton-v-united-states/ — pinpoint: 490.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "87be3abaaedffe56", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "425 U.S. 484 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 49", "official_citation_present": true, "parallel_cite": "96 S. Ct. 1646; 48 L. Ed. 2d 113", "title": "Hampton v. United States", "year": "1976"}}
{"assertion_id": "a05ccaac612edf7e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Neither the entrapment defense nor the Due Process Clause bars conviction of a PREDISPOSED defendant even where a government agent…", "title": "Hampton v. United States"}}
{"assertion_id": "c578970dd3f925d1", "dimension": "support", "kind": "home_role", "locator": {"home": "Entrapment"}, "payload": {"home": "Entrapment", "role": "Key — Progeny / Refinement", "title": "Hampton v. United States"}}
{"assertion_id": "7180aef29e6c24ea", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hampton v. United States"}}
{"assertion_id": "aa850af4693f59a7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-04-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hampton v. United States", "field_i_validity": "good_law", "scope_note": "Plurality opinion (Rehnquist, J.); Powell & Blackmun concurred in the judgment on narrower grounds.", "title": "Hampton v. United States", "varies_by_point": "false"}}
```

### lake record — Hampton v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hampton v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hampton v. United States",
    "case_name_short": "Hampton",
    "case_name_full": "HAMPTON, AKA BYERS v. UNITED STATES",
    "input_case_name": "Hampton v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-04-27",
    "year": 1976,
    "docket": null,
    "cluster_id": 109437,
    "lead_opinion_id": 9426380,
    "sibling_ids": [
      109437,
      9426380,
      9426381,
      9426382
    ],
    "absolute_url": "/opinion/109437/hampton-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9010580,
        "score": 20,
        "case_name": "Hampton v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "425 U.S. 484",
      "volume": "425",
      "reporter": "U.S.",
      "page": "484",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 1646",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1646",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 113",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "113",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 49",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "49",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "425 U.S. 484",
        "volume": "425",
        "reporter": "U.S.",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 1646",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1646",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 113",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "113",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 49",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "49",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "425 U.S. 484",
    "official_selection": {
      "court_class": "scotus",
      "selected": "425 U.S. 484",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-490",
      "page": null,
      "quote": "--- # Hampton v. United States *425 U.S. 484 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Hampton was convicted of selling heroin to undercover federal agents. He claimed that a government informant had supplied him the very heroin he then sold, and argued that the Government's furnishing the contraband barred his conviction. The jury was instructed that predisposition defeated entrapment, and Hampton's predisposition to commit the offense was established. ## Issue Whether the Government's supplying the contraband that a predisposed defendant then sells bars his conviction \u2014 either under the entrapment defense or under the Due Process Clause. ## Rule No. A predisposed defendant cannot claim entrapment, and \u2014 in the plurality's view \u2014 due process does not bar his conviction even where a government agent supplied the contraband.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-490a",
      "page": null,
      "quote": "If the police engage in illegal activity in concert with a defendant beyond the scope of their duties the remedy lies, not in freeing the equally culpable defendant, but in prosecuting the police under the applicable provisions of state or federal law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-04-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hampton v. United States",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (Rehnquist, J.); Powell & Blackmun concurred in the judgment on narrower grounds.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Washington",
          "cluster_id": 7315755,
          "cite": [
            "131 F. Supp. 3d 1007",
            "2015 U.S. Dist. LEXIS 124545",
            "2015 WL 5522286"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rich",
          "cluster_id": 7311690,
          "cite": [
            "83 F. Supp. 3d 424",
            "2015 U.S. Dist. LEXIS 12347",
            "2015 WL 452190"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Delaine and Malisa Fitzpat",
          "cluster_id": 889950,
          "cite": [
            "2012 MT 300",
            "367 Mont. 385",
            "291 P.3d 1106",
            "2012 Mont. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Uribe",
          "cluster_id": 5810602,
          "cite": [
            "199 Cal. App. 4th 836",
            "132 Cal. Rptr. 3d 102",
            "2011 Cal. App. LEXIS 1253"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert A. Burke",
          "cluster_id": 792103,
          "cite": [
            "425 F.3d 400",
            "68 Fed. R. Serv. 437",
            "2005 U.S. App. LEXIS 21013",
            "2005 WL 2373934"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cunningham",
          "cluster_id": 3952337,
          "cite": [
            "808 N.E.2d 488",
            "156 Ohio App. 3d 714",
            "2004 Ohio 1935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Maffett",
          "cluster_id": 1986216,
          "cite": [
            "633 N.W.2d 339",
            "464 Mich. 878"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sanchez",
          "cluster_id": 72803,
          "cite": [
            "138 F.3d 1410",
            "1998 U.S. App. LEXIS 7487",
            "1998 WL 176673"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Greer",
          "cluster_id": 9050105,
          "cite": [
            "178 F.R.D. 418",
            "1998 U.S. Dist. LEXIS 3360",
            "1998 WL 128483"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Sandoval",
          "cluster_id": 603895,
          "cite": [
            "990 F.2d 481",
            "93 Daily Journal DAR 4205",
            "93 Cal. Daily Op. Serv. 2475",
            "1993 U.S. App. LEXIS 6759",
            "1993 WL 94342"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, Appellant/cross-Appellee v. Jack Pardue, Michel Pardue, Appellee/cross-Appellant",
          "cluster_id": 597867,
          "cite": [
            "983 F.2d 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Barrera-Moreno",
          "cluster_id": 9003836,
          "cite": [
            "951 F.2d 1089",
            "1991 WL 263160"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Douglas Floyd Osborne, Jr.",
          "cluster_id": 562325,
          "cite": [
            "935 F.2d 32"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas R. Marino, United States of America v. Peter R. Chabot",
          "cluster_id": 563220,
          "cite": [
            "936 F.2d 23",
            "1991 U.S. App. LEXIS 12662",
            "1991 WL 104191"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Gonzales, A/K/A Jose Menas, United States of America v. Ruiz, Wilson",
          "cluster_id": 556660,
          "cite": [
            "927 F.2d 139",
            "1991 U.S. App. LEXIS 3577",
            "1991 WL 28353"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Brent Eugene Smith, United States of America v. Roberto Osegueya Martinez, United States of America v. Richard Leroy Popp, Jr.",
          "cluster_id": 555136,
          "cite": [
            "924 F.2d 889",
            "91 Cal. Daily Op. Serv. 682",
            "91 Daily Journal DAR 1029",
            "1991 U.S. App. LEXIS 915"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hasting",
          "cluster_id": 110933,
          "cite": [
            "76 L. Ed. 2d 96",
            "103 S. Ct. 1974",
            "461 U.S. 499",
            "1983 U.S. LEXIS 31",
            "51 U.S.L.W. 4572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scott",
          "cluster_id": 109895,
          "cite": [
            "57 L. Ed. 2d 65",
            "98 S. Ct. 2187",
            "437 U.S. 82",
            "1978 U.S. LEXIS 109"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mathews v. United States",
          "cluster_id": 112012,
          "cite": [
            "99 L. Ed. 2d 54",
            "108 S. Ct. 883",
            "485 U.S. 58",
            "1988 U.S. LEXIS 943"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Payner",
          "cluster_id": 110317,
          "cite": [
            "65 L. Ed. 2d 468",
            "100 S. Ct. 2439",
            "447 U.S. 727",
            "1980 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Voigt",
          "cluster_id": 722380,
          "cite": [
            "89 F.3d 1050",
            "78 A.F.T.R.2d (RIA) 5577",
            "1996 U.S. App. LEXIS 16287",
            "1996 WL 380609"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Christopher Twigg, Iii, United States of America v. Henry Alfred Neville",
          "cluster_id": 361264,
          "cite": [
            "588 F.2d 373"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John M. Murphy",
          "cluster_id": 456168,
          "cite": [
            "768 F.2d 1518"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sonya Evette Singleton",
          "cluster_id": 754623,
          "cite": [
            "144 F.3d 1343",
            "1998 U.S. App. LEXIS 15451",
            "1998 WL 350507"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Bagnariol, United States of America v. Gordon L. Walgren, United States of America v. Patrick Gallagher",
          "cluster_id": 397437,
          "cite": [
            "665 F.2d 877",
            "1981 U.S. App. LEXIS 15028"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, in No. 81-1020 v. Jannotti, Harry P. United States of America, in No. 81-1021 v. Schwartz, George X",
          "cluster_id": 401021,
          "cite": [
            "673 F.2d 578",
            "1982 WL 602723"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Zavaras",
          "cluster_id": 158747,
          "cite": [
            "195 F.3d 573",
            "1999 Colo. J. C.A.R. 6110",
            "1999 U.S. App. LEXIS 26874",
            "1999 WL 973608"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stokes v. Gann",
          "cluster_id": 51572,
          "cite": [
            "498 F.3d 483",
            "2007 U.S. App. LEXIS 20735",
            "2007 WL 2430109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Rey",
          "cluster_id": 483372,
          "cite": [
            "811 F.2d 1453",
            "1987 U.S. App. LEXIS 3116"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rafael Santana and Francis Fuentes",
          "cluster_id": 654192,
          "cite": [
            "6 F.3d 1",
            "1993 U.S. App. LEXIS 23810",
            "1993 WL 345746"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gendron",
          "cluster_id": 195225,
          "cite": [
            "18 F.3d 955",
            "1994 WL 50975"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hilario Mendoza-Salgado, United States of America v. Ramon Edwardo Garcia",
          "cluster_id": 583725,
          "cite": [
            "964 F.2d 993",
            "35 Fed. R. Serv. 1029",
            "1992 U.S. App. LEXIS 10413",
            "1992 WL 101352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kojo Sababu, Jaime Delgado, and Dora Garcia",
          "cluster_id": 533826,
          "cite": [
            "891 F.2d 1308",
            "1989 U.S. App. LEXIS 19420"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. F. Thomas Little, United States of America v. Peter Chernik, United States of America v. Harold Grutchfield",
          "cluster_id": 447563,
          "cite": [
            "753 F.2d 1420"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul C. Porter, United States v. Walter G. Baker, United States v. Frederick L. Hearn, United States v. Larry Reservitz",
          "cluster_id": 453326,
          "cite": [
            "764 F.2d 1",
            "1985 U.S. App. LEXIS 20706"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Humberto Barbosa",
          "cluster_id": 775561,
          "cite": [
            "271 F.3d 438",
            "2001 U.S. App. LEXIS 24350",
            "2001 WL 1382027"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Angela Nolan-Cooper",
          "cluster_id": 757749,
          "cite": [
            "155 F.3d 221",
            "1998 U.S. App. LEXIS 21403"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Roy Moreno Ramirez, United States of America v. Robert H. Reynolds",
          "cluster_id": 420788,
          "cite": [
            "710 F.2d 535",
            "13 Fed. R. Serv. 1310",
            "1983 U.S. App. LEXIS 25876"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Darrel Paterson Simpson, Robert MacRiner Anderson, and James Roy Freeman",
          "cluster_id": 484907,
          "cite": [
            "813 F.2d 1462",
            "1987 U.S. App. LEXIS 4561"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lilly Schmidt",
          "cluster_id": 733396,
          "cite": [
            "105 F.3d 82",
            "1997 U.S. App. LEXIS 705",
            "1997 WL 31579"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109437 OR 9426380 OR 9426381 OR 9426382) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MzY2ODE2MDAwMDAmcz0xOTU1NDYyJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109437+OR+9426380+OR+9426381+OR+9426382%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 18,
        "triage_snippet_classified": 182
      },
      "lane2_top_cited": {
        "query": "cites:(109437 OR 9426380 OR 9426381 OR 9426382)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjgmcz0zODA0ODAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109437+OR+9426380+OR+9426381+OR+9426382%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109437 OR 9426380 OR 9426381 OR 9426382)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109437 OR 9426380 OR 9426381 OR 9426382)",
    "indexed_citing_opinions": 628,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109437,
        "count": 585,
        "count_source": "search"
      },
      {
        "opinion_id": 9426380,
        "count": 57,
        "count_source": "search"
      },
      {
        "opinion_id": 9426381,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426382,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 911,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hampton-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQyMjc5OTcmcz0yNzE1MDU1JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109437+OR+9426380+OR+9426381+OR+9426382%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109437,
        "cited_id": 101251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 101997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 108662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 108768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 108906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 109387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 298766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 306412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 314188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 316284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 318238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 319175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 325618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 1270730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 2136075,
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
    "date_created": "2026-07-05T06:03:22Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:03:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:03:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:11:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:03:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hampton v. United States

```
<opinion type="majority">
<author id="b555-6">Mr. Justice Kehnquist</author>
<p id="A0d">announced the judgment of the Court in an opinion in which The Chief Justice and Mr. Justice White join.</p>
<p id="b555-7">This case presents the question of whether a defendant may be convicted for the sale of contraband which he procured from a Government informant or agent. The Court of Appeals for the Eighth Circuit held he could be, and we agree.</p>
<p id="b555-8">I</p>
<p id="b555-9">Petitioner was convicted of two counts of distributing heroin in violation of <span class="citation no-link">21 U. S. C. §841</span> (a)(1) in the United States District Court for the Eastern District of Missouri and sentenced to concurrent terms of five years’ imprisonment (suspended).<footnotemark>1</footnotemark> The case arose from two sales of heroin by petitioner to agents of the Federal Drug Enforcement Administration (DEA) in St. Louis on February 25 and 26, 1974. The sales were arranged by one Hutton, who was a pool-playing acquaintance of petitioner at the Pud bar in St. Louis and also a DEA informant.</p>
<p id="b555-10">According to the Government’s witnesses, in late February 1974, Hutton and petitioner were shooting pool <page-number citation-index="1" label="486">*486</page-number>at the Pud when petitioner, after observing “track” (needle) marks on Hutton's arms told Hutton that he needed money and knew where he could get some heroin. Hutton responded that he could find a buyer and petitioner suggested that he “get in touch with those people.” Hutton then called DEA Agent Terry Sawyer and arranged a sale for 10 p. m. on February 25.<footnotemark>2</footnotemark></p>
<p id="b556-4">At the appointed time, Hutton and petitioner went to a prearranged meetingplace and were met by Agent Sawyer and DEA Agent McDowell, posing as narcotics dealers. Petitioner produced a tinfoil packet from his cap and turned it over to the agents who tested it, pronounced it “okay,” and negotiated a price of $145 which was paid to petitioner. Before they parted, petitioner told Sawyer that he could obtain larger quantities of heroin and gave Sawyer a phone number where he could be reached.</p>
<p id="b556-5">The next day Sawyer called petitioner and arranged for another “buy” that afternoon. Petitioner got Hutton to go along and they met the agents again near where they had been the previous night.</p>
<p id="b556-6">They all entered the agents’ car, and petitioner again produced a tinfoil packet from his cap. The agents again field-tested it and pronounced it satisfactory. Petitioner then asked for $500 which Agent Sawyer said he would get from the trunk. Sawyer got out and opened the trunk which was a signal to other agents to move in and arrest petitioner, which they did.</p>
<p id="b556-7">Petitioner’s version of events was quite different. According to him, in response to his statement that he was short of cash, Hutton said that he had a <page-number citation-index="1" label="487">*487</page-number>friend who was a pharmacist who could produce a nonnarcotic counterfeit drug which would give the same reaction as heroin. Hutton proposed selling this drug to gullible acquaintances who would be led to believe they were buying heroin. Petitioner testified that they successfully duped one buyer with this fake drug and that the sales which led to the arrest were solicited by petitioner<footnotemark>3</footnotemark> in an effort to profit further from this ploy.</p>
<p id="b557-5">Petitioner contended that he neither intended to sell, nor knew that he was dealing in heroin and that all of the drugs he sold were supplied by Hutton. His account was at least partially disbelieved by the jury which was instructed that in order to convict petitioner they had to find that the Government proved “that the defendant knowingly did an act which the law forbids, purposely intending to violate the law.” Thus the guilty verdict necessarily implies that the jury rejected petitioner's claim that he did not know the substance was heroin, and petitioner himself admitted both soliciting and carrying out sales. The only relevance of his version of the facts, then, lies in his having requested an instruction embodying that version.<footnotemark>4</footnotemark> He did not request a standard entrapment instruction but he did request the following:</p>
<blockquote id="b557-6">“The defendant asserts that he was the victim of entrapment as to the crimes charged in the indictment.</blockquote>
<blockquote id="b558-4"><page-number citation-index="1" label="488">*488</page-number>“If you find that the defendant’s sales of narcotics were sales of narcotics supplied to him by an informer in the employ of or acting on behalf of the government, then you must acquit the defendant because the law as a matter of policy forbids his conviction in such a case.</blockquote>
<blockquote id="b558-5">“Furthermore, under this particular defense, you need not consider the predisposition of the defendant to commit the offense charged, because if the governmental involvement through its informer reached the point that I have just defined in your own minds, then the predisposition of the defendant would not matter.” Brief for Petitioner 9.</blockquote>
<p id="b558-6">The trial court refused the instruction and petitioner was found guilty. He appealed to the United States Court of Appeals for the Eighth Circuit, claiming that if the jury had believed that the drug was supplied by Hutton he should have been acquitted. The Court of Appeals rejected this argument and affirmed the conviction, relying on our opinion in <em>United States </em>v. <em>Russell, </em><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/" aria-description="Citation for case: United States v. Russell">411 U. S. 423</a></span> (1973). <span class="citation" data-id="9461293"><a href="/opinion/323851/united-states-v-charles-hampton-also-known-as-michael-byers/" aria-description="Citation for case: United States v. Charles Hampton, Also Known as Michael...">507 F. 2d 832</a></span> (1974).</p>
<p id="b558-7">II</p>
<p id="b558-8">In <em>Russell </em>we held that the statutory defense of entrapment was not available where it was conceded that a Government agent supplied a necessary ingredient in the manufacture of an illicit drug. We reaffirmed the principle of <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span> (1932), and <em>Sherman </em>v. <em>United States, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">356 U. S. 369</a></span> (1958), that the entrapment defense “focus[es] on the intent or predisposition of the defendant to commit the crime,” <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#429" aria-description="Citation for case: United States v. Russell"><em>Russell, supra, at </em>429</a></span>, rather than upon the conduct of the Government’s agents. We ruled out the possibility that the defense of entrapment could ever be <page-number citation-index="1" label="489">*489</page-number>based upon governmental misconduct in a case, such as this one, where the predisposition of the defendant to commit the crime was established.</p>
<p id="b559-5">In holding that “[i]t is only when the Government’s deception actually implants the criminal design in the mind of the defendant that the defense of entrapment comes into play,” <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#436" aria-description="Citation for case: United States v. Russell">411 U. S., at 436</a></span>, we, of course, rejected the contrary view of the dissents in that case and the concurrences in <em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span> </em>and <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Sherman</a></span>. </em>In view of these holdings, petitioner correctly recognizes that his case does not qualify as one involving “entrapment” at all. He instead relies on the language in <em>Russell </em>that “we may some day be presented with a situation in which the conduct of law enforcement agents is so outrageous that due process principles would absolutely bar the government from invoking judicial processes to obtain a conviction, cf. <em>Rochin </em>v. California, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952) . . . .” <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#431" aria-description="Citation for case: United States v. Russell">411 U. S., at 431-432</a></span>.</p>
<p id="b559-6">In urging that this case involves a violation of his due process rights, petitioner misapprehends the meaning of the quoted language in <em><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/" aria-description="Citation for case: United States v. Russell">Russell, supra.</a></span> </em>Admittedly petitioner’s case is different from Russell’s but the difference is one of degree, not of kind. In <em>Russell </em>the ingredient supplied by the Government agent was a legal drug which the defendants demonstrably could have obtained from other sources besides the Government. Here the drug which the Government informant allegedly supplied to petitioner both was illegal and constituted the <em>corpus delicti </em>for the sale of which the petitioner was convicted. The Government obviously played a more significant role in enabling petitioner to sell contraband in this case than it did in <em>Russell.</em></p>
<p id="b559-7">But in each case the Government agents were acting in concert with the defendant, and in each case either the jury found or the defendant conceded that he was <page-number citation-index="1" label="490">*490</page-number>predisposed to commit the crime for which he was convicted. The remedy of the criminal defendant with respect to the acts of Government agents, which, far from being resisted, are encouraged by him, lies solely in the defense of entrapment. But, as noted, petitioner's conceded predisposition rendered this defense unavailable to him.</p>
<p id="b560-5">To sustain petitioner’s contention here wo Id run directly contrary to our statement in <em>Russell </em>that the defense of entrapment is not intended “to give the federal judiciary a ‘chancellor’s foot’ veto over law enforcement practices of which it did not approve. The execution of the federal laws under our Constitution is confided primarily to the Executive Branch of the Government, subject to applicable constitutional and statutory limitations and to judicially fashioned rules to enforce those limitations.” <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#435" aria-description="Citation for case: United States v. Russell">411 U. S., at 435</a></span>.</p>
<p id="b560-6">The limitations of the Due Process Clause of the Fifth Amendment come into play only when the Government activity in question violates some protected right of the <em>defendant. </em>Here, as we have noted, the police, the Government informant, and the defendant acted in concert with one another. If the result of the governmental activity is to “implant in the mind of an innocent person the disposition to commit the alleged offense and induce its commission . . . ,” <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States"><em>Sorrells, supra, </em>at 442</a></span>, the defendant is protected by the defense of entrapment. If the police engage in illegal activity in concert with a defendant beyond the scope of their duties the remedy lies, not in freeing the equally culpable defendant, but in prosecuting the police under' the applicable provisions of state or federal law. See <em>O’Shea </em>v. <em>Littleton, </em><span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/#503" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U. S. 488, 503</a></span> (1974); <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#428" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 428-429</a></span> (1976). But the police conduct here no more deprived defendant of any right <page-number citation-index="1" label="491">*491</page-number>secured to him by the United States Constitution than did the police conduct in <em>Bussell </em>deprive Russell of any rights.</p>
<p id="b561-5">
<em>Affirmed.</em>
</p>
<p id="b561-6">Mr. Justice Stevens took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b555-11"> Petitioner was placed on five years’ probation which, was to run concurrently with the remainder of a 28- to 30-year. state armed robbery sentence from which petitioner had escaped.</p>
</footnote>
<footnote label="2">
<p id="b556-8"> The testimony of Hutton is confused as to the dates. At one point he indicated that the initial conversation and the sale both occurred on February 25. At another point he testified that they occurred on two separate days.</p>
</footnote>
<footnote label="3">
<p id="b557-7"> On appeal, petitioner’s counsel, who was also his counsel at trial, conceded that petitioner was predisposed to commit this offense. <span class="citation" data-id="9461293"><a href="/opinion/323851/united-states-v-charles-hampton-also-known-as-michael-byers/" aria-description="Citation for case: United States v. Charles Hampton, Also Known as Michael...">507 F. 2d 832</a></span>, 836 n. 5 (CA8 1974).</p>
</footnote>
<footnote label="4">
<p id="b557-8"> The Court of Appeals treated the proffered instruction on its merits, rather than inquiring as to whether its refusal, in light of the other instructions given and of the jury’s verdict, may have been harmless error. We therefore do likewise.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Hanlon v. Berger.md  (`case`, 5 assertions)

### content_page

```
---
title: "Hanlon v. Berger"
type: case
citation: "526 U.S. 808 (1999)"
parallel_cite: "119 S. Ct. 1706; 143 L. Ed. 2d 978"
neutral_cite: 1999 U.S. LEXIS 3634
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-05-24
docket: 97-1927
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-05-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hanlon v. Berger
  varies_by_point: false
  scope_note: "Per curiam companion to Wilson v. Layne; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/1087699/hanlon-v-berger/"
  cluster_id: 1087699
  opinion_id: 1087699
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Wilson v. Layne]]", "[[Bivens v. Six Unknown Named Agents]]", "[[Harlow v. Fitzgerald]]"]
aliases: []
tags: ["case", "section-1983", "bivens", "qualified-immunity", "media-ride-along", "per-curiam"]
holding: "A media ride-along during the execution of a search warrant violated the Fourth Amendment under Wilson v. Layne, but the officers were entitled to qualified immunity."
lake:
  record_id: Hanlon v. Berger
  status: verified
  projected_at: 2026-07-06
---

# Hanlon v. Berger

*526 U.S. 808 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Paul and Erma Berger lived on a 75,000-acre ranch near Jordan, Montana. In 1993 a magistrate issued a warrant to search the ranch and outbuildings (excluding the residence) for evidence of unlawful taking of wildlife. When U.S. Fish and Wildlife Service agents executed the warrant, a CNN photo-and-reporting crew accompanied them, observing and recording the search. The Bergers sued the agents and an assistant U.S. attorney for damages under [[Bivens v. Six Unknown Named Agents]], alleging a Fourth Amendment violation.

## Issue
Whether the media's accompaniment during execution of the warrant stated a Fourth Amendment violation, and whether the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Rule
The case is governed by its same-day companion, [[Wilson v. Layne]]. The Court treated the allegations as stating a Fourth Amendment violation under *[[Wilson v. Layne|Wilson]]* — "respondents alleged a Fourth Amendment violation under our decision today in *Wilson v. Layne.*" — 526 U.S. at 810. ^pin-810

But the officers were entitled to [[Qualified Immunity|qualified immunity]]: "Petitioners maintain that even though they may have violated the Fourth Amendment rights of respondents, they are entitled to the defense of qualified immunity. We agree. Our holding in *Wilson* makes clear that this right was not clearly established in 1992." — *Id.* ^pin-810b

## Application
*[[Wilson v. Layne|Wilson]]* held that letting the media into a home during a warrant's execution violates the Fourth Amendment, and that the right was not clearly established before that 1999 decision. Because the 1993 ranch search here predated *[[Wilson v. Layne|Wilson]]* and no intervening decision had made the law any clearer, the agents could not have known their conduct was unlawful and were entitled to [[Qualified Immunity|qualified immunity]], just as in *[[Wilson v. Layne|Wilson]]*.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]] (per curiam). The media ride-along stated a Fourth Amendment violation under *[[Wilson v. Layne]]*, but the officers received [[Qualified Immunity|qualified immunity]] because the right was not clearly established at the time of the search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- A [[Common Legal Terms#per-curiam|per curiam]] companion decided the same day as [[Wilson v. Layne]], applying that decision's Fourth Amendment holding and qualified-immunity analysis to a media ride-along onto a ranch under a *[[Bivens v. Six Unknown Named Agents|Bivens]]* claim. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Hanlon v. Berger*, 526 U.S. 808 (1999) (per curiam) — https://www.courtlistener.com/opinion/1087699/hanlon-v-berger/ — pinpoint: 810.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3c4aef5b65e82a6c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "526 U.S. 808 (1999)", "court": "U.S. Supreme Court", "neutral_cite": "1999 U.S. LEXIS 3634", "official_citation_present": true, "parallel_cite": "119 S. Ct. 1706; 143 L. Ed. 2d 978", "title": "Hanlon v. Berger", "year": "1999"}}
{"assertion_id": "08c2ac50f857bf50", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Hanlon v. Berger"}}
{"assertion_id": "38713ac50198069a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A media ride-along during the execution of a search warrant violated the Fourth Amendment under Wilson v. Layne, but the officers were entitled to qualified immunity.", "title": "Hanlon v. Berger"}}
{"assertion_id": "78a787168290b284", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hanlon v. Berger"}}
{"assertion_id": "df4e3f0b8fe94910", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1999-05-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hanlon v. Berger", "field_i_validity": "good_law", "scope_note": "Per curiam companion to Wilson v. Layne; good law.", "title": "Hanlon v. Berger", "varies_by_point": "false"}}
```

### lake record — Hanlon v. Berger

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hanlon v. Berger",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hanlon v. Berger",
    "case_name_short": "Hanlon",
    "case_name_full": "HANLON Et Al. v. BERGER Et Ux.",
    "input_case_name": "Hanlon v. Berger",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-05-24",
    "year": 1999,
    "docket": "97-1927",
    "cluster_id": 1087699,
    "lead_opinion_id": 1087699,
    "sibling_ids": [
      1087699,
      9526990,
      9526991
    ],
    "absolute_url": "/opinion/1087699/hanlon-v-berger/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9183869,
        "score": 20,
        "case_name": "Hanlon v. Berger"
      },
      {
        "cluster_id": 9183868,
        "score": 20,
        "case_name": "Hanlon v. Berger"
      },
      {
        "cluster_id": 9182880,
        "score": 20,
        "case_name": "Hanlon v. Berger"
      },
      {
        "cluster_id": 9182879,
        "score": 20,
        "case_name": "Hanlon v. Berger"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "526 U.S. 808",
      "volume": "526",
      "reporter": "U.S.",
      "page": "808",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 1706",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1706",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 978",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "978",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 3634",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3634",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "526 U.S. 808",
        "volume": "526",
        "reporter": "U.S.",
        "page": "808",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 1706",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1706",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 978",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "978",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 3634",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3634",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "526 U.S. 808",
    "official_selection": {
      "court_class": "scotus",
      "selected": "526 U.S. 808",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-810",
      "page": null,
      "quote": "--- # Hanlon v. Berger *526 U.S. 808 (1999)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Paul and Erma Berger lived on a 75,000-acre ranch near Jordan, Montana. In 1993 a magistrate issued a warrant to search the ranch and outbuildings (excluding the residence) for evidence of unlawful taking of wildlife. When U.S. Fish and Wildlife Service agents executed the warrant, a CNN photo-and-reporting crew accompanied them, observing and recording the search. The Bergers sued the agents and an assistant U.S. attorney for damages under [[Bivens v. Six Unknown Named Agents]], alleging a Fourth Amendment violation. ## Issue Whether the media's accompaniment during execution of the warrant stated a Fourth Amendment violation, and whether the officers were entitled to qualified immunity. ## Rule The case is governed by its same-day companion, [[Wilson v. Layne]]. The Court treated the allegations as stating a Fourth Amendment violation under *Wilson* \u2014",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-810b",
      "page": null,
      "quote": "Petitioners maintain that even though they may have violated the Fourth Amendment rights of respondents, they are entitled to the defense of qualified immunity. We agree. Our holding in *Wilson* makes clear that this right was not clearly established in 1992.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-05-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hanlon v. Berger",
    "varies_by_point": false,
    "scope_note": "Per curiam companion to Wilson v. Layne; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Detroy v. City & County of Honolulu",
          "cluster_id": 8653044,
          "cite": [
            "271 F. App'x 554"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brokers' Choice of America, Inc. v. NBC Universal, Inc.",
          "cluster_id": 2682361,
          "cite": [
            "757 F.3d 1125",
            "2014 WL 3307834"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Suiters",
          "cluster_id": 169685,
          "cite": [
            "499 F.3d 1228",
            "35 Media L. Rep. (BNA) 2409",
            "2007 U.S. App. LEXIS 20686",
            "2007 WL 2421765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villegas v. Gilroy Garlic Festival Ass'n",
          "cluster_id": 1441350,
          "cite": [
            "541 F.3d 950",
            "2008 U.S. App. LEXIS 18801",
            "2008 WL 4058566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re DoubleClick Inc. Privacy Litigation",
          "cluster_id": 2429654,
          "cite": [
            "154 F. Supp. 2d 497",
            "2001 WL 303744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brunette v. Humane Society Of Ventura County",
          "cluster_id": 778168,
          "cite": [
            "294 F.3d 1205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Theofel v. Farey-Jones",
          "cluster_id": 8438109,
          "cite": [
            "359 F.3d 1066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George Theofel Howard Teig David Kelley Integrated Capital Associates, Inc., a Delaware Corporation Nancy Rilett Ryan Tam Claudia English Teresa Patterson Tanya Young Roberto Marsella Regina Ovenden Emil Pesiri Eric Sullivan Douglas H. Wolf Richard Buckingham v. Alwyn Farey-Jones Iryna A. Kwasny, George Theofel Howard Teig David Kelley Integrated Capital Associates, Inc., a Delaware Corporation Nancy Rilett Ryan Tam Claudia English Teresa Patterson Tanya Young Roberto Marsella Regina Ovenden Emil Pesiri Eric Sullivan Douglas H. Wolf Richard Buckingham v. Alwyn Farey-Jones Iryna A. Kwasny",
          "cluster_id": 785281,
          "cite": [
            "359 F.3d 1066",
            "2003 U.S. App. LEXIS 26896"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. Butte-Silver Bow County",
          "cluster_id": 778595,
          "cite": [
            "298 F.3d 1022",
            "2002 Cal. Daily Op. Serv. 6645",
            "2002 Daily Journal DAR 8361",
            "2002 U.S. App. LEXIS 14911",
            "2002 WL 1677990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Artis v. United States",
          "cluster_id": 2159070,
          "cite": [
            "802 A.2d 959",
            "2002 D.C. App. LEXIS 380",
            "2002 WL 1575751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George Theofel Howard Teig David Kelley Integrated Capital Associates, Inc., a Delaware Corporation Nancy Rilett Ryan Tam Claudia English Teresa Patterson Tanya Young Roberto Marsella Regina Ovenden Emil Pesiri Eric Sullivan Douglas H. Wolf Richard Buckingham v. Alwyn Farey-Jones Iryna A. Kwasny, George Theofel Howard Teig David Kelley Integrated Capital Associates, Inc., a Delaware Corporation Nancy Rilett Ryan Tam Claudia English Teresa Patterson Tanya Young Roberto Marsella Regina Ovenden Emil Pesiri Eric Sullivan Douglas H. Wolf Richard Buckingham v. Alwyn Farey-Jones Iryna A. Kwasny",
          "cluster_id": 783378,
          "cite": [
            "341 F.3d 978",
            "2003 Daily Journal DAR 9849",
            "2003 Cal. Daily Op. Serv. 7848",
            "2003 U.S. App. LEXIS 17963"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Theofel v. Farey-Jones",
          "cluster_id": 8437727,
          "cite": [
            "341 F.3d 978",
            "2003 WL 22020268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Conradt Ex Rel. Conradt v. NBC Universal, Inc.",
          "cluster_id": 2009416,
          "cite": [
            "536 F. Supp. 2d 380",
            "36 Media L. Rep. (BNA) 1490",
            "2008 U.S. Dist. LEXIS 14112",
            "2008 WL 501361"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. Butte-Silver Bow County",
          "cluster_id": 7103940,
          "cite": [
            "283 F.3d 985"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph R. Ramirez Julia L. Ramirez Joshua Ramirez Regina Ramirez v. Butte-Silver Bow County John McPherson Sheriff of Butte-Silver Bow County Joe Lee, Undersheriff of Butte-Silver Bow County John Does 1-50, in Their Individual And/or Official Capacities, and Jeff Groh, Special Agent With the Bureau of Alcohol, Tobacco, and Firearms, Joseph R. Ramirez Julia L. Ramirez Joshua Ramirez Regina Ramirez v. Butte Silver Bow County John McPherson Sheriff of Butte-Silver Bow County Joe Lee, Undersheriff of Butte-Silver Bow County Jeff Groh, Special Agent With the Bureau of Alcohol, Tobacco, and Firearms John Does 1-50, in Their Individual And/or Official Capacities",
          "cluster_id": 776951,
          "cite": [
            "283 F.3d 985",
            "2002 Daily Journal DAR 2872",
            "2002 Cal. Daily Op. Serv. 2343",
            "2002 U.S. App. LEXIS 3893"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brunette v. Humane Society",
          "cluster_id": 7105844,
          "cite": [
            "294 F.3d 1205",
            "2002 WL 1396511"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. Butte-Silver Bow County",
          "cluster_id": 7106653,
          "cite": [
            "298 F.3d 1022"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brokers' Choice of America v. NBC Universal, Inc.",
          "cluster_id": 3062233,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villegas v. City of Gilroy",
          "cluster_id": 3052856,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frederick v. BIOGRAPHY CHANNEL",
          "cluster_id": 2350172,
          "cite": [
            "683 F. Supp. 2d 798",
            "38 Media L. Rep. (BNA) 1362",
            "2010 U.S. Dist. LEXIS 9743",
            "2010 WL 431502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(1087699 OR 9526990 OR 9526991) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 2,
        "triage_snippet_classified": 20
      },
      "lane2_top_cited": {
        "query": "cites:(1087699 OR 9526990 OR 9526991)",
        "reviewed": 23,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 20,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(1087699 OR 9526990 OR 9526991)",
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
    "complete_query": "cites:(1087699 OR 9526990 OR 9526991)",
    "indexed_citing_opinions": 23,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 1087699,
        "count": 22,
        "count_source": "search"
      },
      {
        "opinion_id": 9526990,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9526991,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 34,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hanlon-v-berger.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjAyMjYxNzcmcz03NzY5NTEmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%281087699+OR+9526990+OR+9526991%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 1087699,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1087699,
        "cited_id": 748210,
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
    "date_created": "2026-07-05T06:11:33Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:15:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hanlon v. Berger

```
<div>
<center><b><span class="citation" data-id="9526990"><a href="/opinion/1087699/hanlon-v-berger/" aria-description="Citation for case: Hanlon v. Berger">526 U.S. 808</a></span> (1999)</b></center>
<center><h1>HANLON et al.<br>
v.<br>
BERGER et ux.</h1></center>
<center>No. 97-1927.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued March 24, 1999.</center>
<center>Decided May 24, 1999.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><i>Richard A. Cordray</i> argued the cause for petitioners. With him on the briefs was <i>James A. Anzelmo.</i> </p>
<p><i>Henry H. Rossbacher</i> argued the cause for respondents. With him on the brief for respondents Berger et al. were <i>Nanci E. Nishimura</i> and <i>Jay F. Lansing. P. Cameron DeVore, Jessica L. Goldman,</i> and <i>David C. Kohler</i> filed briefs for respondents Cable News Network, Inc., et al.<sup>[*]</sup></p>
<p><span class="star-pagination">*809</span> Per Curiam.</p>
<p>Respondents Paul and Erma Berger sued petitioners special agents of the United States Fish and Wildlife Service and an assistant United States attorneyfor damages under <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971). They alleged that the conduct of petitioners had violated their rights under the Fourth Amendment to the United States Constitution. <span class="citation" data-id="748210"><a href="/opinion/748210/paul-w-berger-and-erma-r-berger-v-rodney-c-hanlon-joel-scrafford/" aria-description="Citation for case: Paul W. Berger and Erma R. Berger v. Rodney C. Hanlon...">129 F. 3d 505</a></span> (CA9 1997). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./525/981/">525 U. S. 981</a></span> (1998).</p>
<p>Respondents live on a 75,000-acre ranch near Jordan, Montana. In 1993, a Magistrate Judge issued a warrant authorizing the search of "The Paul W. Berger ranch with appurtenant structures, excluding the residence" for evidence of "the taking of wildlife in violation of Federal laws." App. 17. About a week later, a multiple-vehicle caravan consisting of Government agents and a crew of photographers and reporters from Cable News Network, Inc. (CNN), proceeded to a point near the ranch. The agents executed the warrant and explained: "Over the course of the day, the officers searched the ranch and its outbuildings pursuant to the authority conferred by the search warrant. The CNN media crew . . . accompanied and observed the officers, and the media crew recorded the officers' conduct in executing the warrant." Brief for Petitioners 5.</p>
<p>Review of the complaint's much more detailed allegations to the same effect satisfies us that respondents alleged a Fourth Amendment violation under our decision today in <span class="star-pagination">*810</span> <i>Wilson</i> v. <i>Layne, ante,</i> p. 603. There we hold that police violate the Fourth Amendment rights of homeowners when they allow members of the media to accompany them during the execution of a warrant in their home. We also hold there that because the law on this question before today's decision was not clearly established, the police in that case were entitled to the defense of qualified immunity. <i>Ante,</i>  at 605-606.</p>
<p>Petitioners maintain that even though they may have violated the Fourth Amendment rights of respondents, they are entitled to the defense of qualified immunity. We agree. Our holding in <i>Wilson</i> makes clear that this right was not clearly established in 1992. The parties have not called our attention to any decisions which would have made the state of the law any clearer a year laterat the time of the search in this case. We therefore vacate the judgment of the Court of Appeals for the Ninth Circuit and remand the case for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Stevens, concurring in part and dissenting in part.</p>
<p>As I explain in my dissent in <i>Wilson</i> v. <i>Layne, ante,</i> p. 618, I am convinced that the constitutional rule recognized in that case had been clearly established long before 1992. I therefore respectfully dissent from the Court's disposition of this case on qualified immunity grounds.</p>
<h2>NOTES</h2>
<p>[*]   A brief of <i>amici curiae</i> urging reversal was filed for ABC, Inc., et al. by <i>Lee Levine, James E. Grossberg, Jay Ward Brown, Henry S. Hoberman, Richard M. Schmidt, Jr., Susanna M. Lowy, Harold W. Fuson, Jr., Barbara Wartelle Wall, Ralph E. Goldberg, Karlene W. Goller, Jerry S.</i>  <i>Birenz, Slade R. Metcalf, Jack N. Goodman, David S. J. Brown, René P. Milam, George Freeman,</i> and <i>Jane E. Kirtley.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the National Association of Criminal Defense Lawyers by <i>Joshua L. Dratel;</i> and for the National Association of Securities and Commercial Law Attorneys by <i>Kevin P. Roddy.</i> </p>
<p><i>M. Reed Hopper</i> and <i>Robin L. Rivett</i> filed a brief for the Pacific Legal Foundation as <i>amicus curiae.</i> </p>

</div>
```

---
