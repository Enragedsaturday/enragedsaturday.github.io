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

## GROUP: content/cases/Donovan v. Dewey.md  (`case`, 5 assertions)

### content_page

```
---
title: "Donovan v. Dewey"
type: case
citation: "452 U.S. 594 (1981)"
parallel_cite: "101 S. Ct. 2534; 69 L. Ed. 2d 262"
neutral_cite: 1980 U.S. LEXIS 58
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-06-17
docket: 80-901
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Donovan v. Dewey
  varies_by_point: false
  scope_note: "Good law; part of the Colonnade-Biswell pervasively-regulated-industry line, later refined into the three-part test of New York v. Burger (1987)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110530/donovan-v-dewey/"
  cluster_id: 110530
  opinion_id: 9428427
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Progeny (pervasively-regulated industry)"
related: ["[[United States v. Biswell]]", "[[Marshall v. Barlow's Inc.]]", "[[See v. City of Seattle]]"]
aliases: []
tags: ["case", "fourth-amendment", "administrative-search", "inspections", "pervasively-regulated", "mines", "warrant"]
holding: "Warrantless inspections of a pervasively regulated industry (mines) are reasonable where a comprehensive statutory scheme — defining the certainty, regularity, frequency, and scope of inspection — provides a constitutionally adequate substitute for a warrant."
lake:
  record_id: Donovan v. Dewey
  status: under_review
  projected_at: 2026-07-06
---

# Donovan v. Dewey

*452 U.S. 594 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Under § 103(a) of the Federal Mine Safety and Health Act of 1977, a federal inspector sought to inspect a stone quarry operated by Dewey without a warrant. The Act authorizes mandatory, unannounced inspections of all mines at specified frequencies. Dewey refused entry and challenged the warrantless-inspection scheme under the Fourth Amendment; the District Court held it unconstitutional under *[[Marshall v. Barlow's Inc|Marshall v. Barlow's, Inc.]]*

## Issue
Whether the Fourth Amendment permits warrantless inspections of mines under a comprehensive federal regulatory scheme that does not require a warrant.

## Rule
Yes. Commercial premises in a pervasively regulated business enjoy reduced privacy. "The greater latitude to conduct warrantless inspections of commercial property reflects the fact that the expectation of privacy that the owner of commercial property enjoys in such property differs significantly from the sanctity accorded an individual's home, and that this privacy interest may, in certain circumstances, be adequately protected by regulatory schemes authorizing warrantless inspections." — 452 U.S. at 598–599. ^pin-598

"Applying this analysis … we conclude that the warrantless inspections required by the Mine Safety and Health Act do not offend the Fourth Amendment." — *Id.* at 602. ^pin-602

"[T]he only real issue before us is whether the statute's inspection program, in terms of the certainty and regularity of its application, provides a constitutionally adequate substitute for a warrant. We believe that it does." — *Id.* at 603. ^pin-603

## Application
Mining is "among the most hazardous" industries, giving Congress a substantial interest in unannounced inspections that a warrant requirement could frustrate. The Act supplied a constitutionally adequate warrant substitute: it mandates inspection of all mines at defined frequencies (surface mines at least twice yearly, underground at least four times), sets the standards in statute and regulation, and constrains inspector discretion — so the operator "is not left to wonder about the purposes of the inspector or the limits of his task." The certainty and regularity of the scheme made the warrantless inspections reasonable.

## Conclusion
The warrantless mine inspections under the Act were constitutional; the judgment for Dewey was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Donovan v. Dewey* applies and extends the *Colonnade-Biswell* pervasively-regulated-industry exception preserved in [[Marshall v. Barlow's Inc.]]; the line was later organized into a three-part test in *[[New York v. Burger]]* (1987). It remains good law.

## Appears on
- [[Special Needs and Administrative Searches]] — *Progeny (pervasively-regulated industry)*

## Sources
- *Donovan v. Dewey*, 452 U.S. 594 (1981) — https://www.courtlistener.com/opinion/110530/donovan-v-dewey/ — pinpoints: 598–599, 602, 603.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5db3c7612d54947a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "452 U.S. 594 (1981)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 58", "official_citation_present": true, "parallel_cite": "101 S. Ct. 2534; 69 L. Ed. 2d 262", "title": "Donovan v. Dewey", "year": "1981"}}
{"assertion_id": "00188b5e69045b1b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Warrantless inspections of a pervasively regulated industry (mines) are reasonable where a comprehensive statutory scheme — defining the certainty, regularity, frequency, and scope of inspection — provides a constitutionally adequate substitute for a warrant.", "title": "Donovan v. Dewey"}}
{"assertion_id": "eb4be7399eea1451", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Progeny (pervasively-regulated industry)", "title": "Donovan v. Dewey"}}
{"assertion_id": "37560856cfb5ac9d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Donovan v. Dewey"}}
{"assertion_id": "447187fbbb4d19a4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1981-06-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Donovan v. Dewey", "field_i_validity": "good_law", "scope_note": "Good law; part of the Colonnade-Biswell pervasively-regulated-industry line, later refined into the three-part test of New York v. Burger (1987).", "title": "Donovan v. Dewey", "varies_by_point": "false"}}
```

### lake record — Donovan v. Dewey

```json
{
  "schema_version": "s2.v1",
  "record_id": "Donovan v. Dewey",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Donovan v. Dewey",
    "case_name_short": "Donovan",
    "case_name_full": "DONOVAN, SECRETARY OF LABOR v. DEWEY Et Al.",
    "input_case_name": "Donovan v. Dewey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-06-17",
    "year": 1981,
    "docket": "80-901",
    "cluster_id": 110530,
    "lead_opinion_id": 9428427,
    "sibling_ids": [
      110530,
      9428427,
      9428428,
      9428429,
      9428430
    ],
    "absolute_url": "/opinion/110530/donovan-v-dewey/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9032957,
        "score": 20,
        "case_name": "Donovan v. Dewey"
      },
      {
        "cluster_id": 9031727,
        "score": 20,
        "case_name": "Donovan v. Dewey"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "452 U.S. 594",
      "volume": "452",
      "reporter": "U.S.",
      "page": "594",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 2534",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2534",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 262",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "262",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 58",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "58",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "452 U.S. 594",
        "volume": "452",
        "reporter": "U.S.",
        "page": "594",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 2534",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2534",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 262",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "262",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 58",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "58",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "452 U.S. 594",
    "official_selection": {
      "court_class": "scotus",
      "selected": "452 U.S. 594",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-598",
      "page": null,
      "quote": "--- # Donovan v. Dewey *452 U.S. 594 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Under \u00a7 103(a) of the Federal Mine Safety and Health Act of 1977, a federal inspector sought to inspect a stone quarry operated by Dewey without a warrant. The Act authorizes mandatory, unannounced inspections of all mines at specified frequencies. Dewey refused entry and challenged the warrantless-inspection scheme under the Fourth Amendment; the District Court held it unconstitutional under *Marshall v. Barlow's, Inc.* ## Issue Whether the Fourth Amendment permits warrantless inspections of mines under a comprehensive federal regulatory scheme that does not require a warrant. ## Rule Yes. Commercial premises in a pervasively regulated business enjoy reduced privacy.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-602",
      "page": null,
      "quote": "Applying this analysis \u2026 we conclude that the warrantless inspections required by the Mine Safety and Health Act do not offend the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-603",
      "page": null,
      "quote": "[T]he only real issue before us is whether the statute's inspection program, in terms of the certainty and regularity of its application, provides a constitutionally adequate substitute for a warrant. We believe that it does.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Donovan v. Dewey",
    "varies_by_point": false,
    "scope_note": "Good law; part of the Colonnade-Biswell pervasively-regulated-industry line, later refined into the three-part test of New York v. Burger (1987).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Phillips v. State",
          "cluster_id": 1747319,
          "cite": [
            "109 S.W.3d 562",
            "2003 WL 1923487"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane1_negative"
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
        "journal_ref": "Donovan v. Dewey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Crosby v. Paulk",
          "cluster_id": 74072,
          "cite": [
            "187 F.3d 1339",
            "1999 U.S. App. LEXIS 21641",
            "1999 WL 703193"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perry G. Blocker",
          "cluster_id": 733272,
          "cite": [
            "104 F.3d 720",
            "1997 U.S. App. LEXIS 712",
            "1997 WL 14762"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane1_negative"
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
        "journal_ref": "Donovan v. Dewey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leon",
          "cluster_id": 111262,
          "cite": [
            "82 L. Ed. 2d 677",
            "104 S. Ct. 3405",
            "468 U.S. 897",
            "1984 U.S. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aaron Lindh v. James P. Murphy, Warden",
          "cluster_id": 726705,
          "cite": [
            "96 F.3d 856",
            "1996 U.S. App. LEXIS 24136",
            "1996 WL 517290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thunder Basin Coal Co. v. Reich",
          "cluster_id": 112921,
          "cite": [
            "127 L. Ed. 2d 29",
            "114 S. Ct. 771",
            "510 U.S. 200",
            "1994 U.S. LEXIS 1136",
            "94 Daily Journal DAR 619",
            "7 Fla. L. Weekly Fed. S 695",
            "94 Cal. Daily Op. Serv. 373",
            "62 U.S.L.W. 4058",
            "1994 CCH OSHD 30,312",
            "16 OSHC (BNA) 1553"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dow Chemical Co. v. United States Ex Rel. Administrator",
          "cluster_id": 111667,
          "cite": [
            "90 L. Ed. 2d 226",
            "106 S. Ct. 1819",
            "476 U.S. 227",
            "1986 U.S. LEXIS 155",
            "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679",
            "54 U.S.L.W. 4464",
            "24 ERC (BNA) 1385"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Menotti v. City of Seattle",
          "cluster_id": 3032002,
          "cite": [
            "409 F.3d 1113",
            "2005 WL 1300994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thompson",
          "cluster_id": 1836924,
          "cite": [
            "842 So. 2d 330",
            "2003 WL 1826561"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Santikos v. State",
          "cluster_id": 1653416,
          "cite": [
            "836 S.W.2d 631",
            "1992 Tex. Crim. App. LEXIS 131",
            "1992 WL 116096"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 5607944,
          "cite": [
            "21 Cal. 4th 668",
            "99 Cal. Daily Op. Serv. 6990",
            "99 Daily Journal DAR 8867",
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "1999 Cal. LEXIS 5534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of L. A. v. Patel",
          "cluster_id": 2811846,
          "cite": [
            "576 U.S. 409",
            "135 S. Ct. 2443",
            "192 L. Ed. 2d 435",
            "2015 U.S. LEXIS 4065",
            "83 U.S.L.W. 4520",
            "25 Fla. L. Weekly Fed. S 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald P. Rohrig",
          "cluster_id": 728738,
          "cite": [
            "98 F.3d 1506",
            "1996 U.S. App. LEXIS 28274",
            "1996 WL 627521"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 1160907,
          "cite": [
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "21 Cal. 4th 668"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph J. O'Brien v. City of Grand Rapids William Hegarty Daniel Ostapowicz",
          "cluster_id": 669698,
          "cite": [
            "23 F.3d 990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Swint v. City Of Wadley",
          "cluster_id": 693042,
          "cite": [
            "51 F.3d 988",
            "1995 U.S. App. LEXIS 10481"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vaughn Neita v. City of Chicago",
          "cluster_id": 4239934,
          "cite": [
            "830 F.3d 494",
            "2016 U.S. App. LEXIS 13191",
            "2016 WL 3905604"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Free Speech Coalition, Inc. v. Attorney General of the United States",
          "cluster_id": 676451,
          "cite": [
            "677 F.3d 519",
            "2012 WL 1255056",
            "2012 U.S. App. LEXIS 7543"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110530 OR 9428427 OR 9428428 OR 9428429 OR 9428430) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDgyMjA4MDAwMDAmcz00OTI5JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110530+OR+9428427+OR+9428428+OR+9428429+OR+9428430%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110530 OR 9428427 OR 9428428 OR 9428429 OR 9428430)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NSZzPTEyMTU1MzQmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110530+OR+9428427+OR+9428428+OR+9428429+OR+9428430%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110530 OR 9428427 OR 9428428 OR 9428429 OR 9428430)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 1,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110530 OR 9428427 OR 9428428 OR 9428429 OR 9428430)",
    "indexed_citing_opinions": 458,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110530,
        "count": 397,
        "count_source": "search"
      },
      {
        "opinion_id": 9428427,
        "count": 69,
        "count_source": "search"
      },
      {
        "opinion_id": 9428428,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428429,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428430,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 689,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/donovan-v-dewey.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjczMjc3OCZzPTQ4OTgzOTUmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28110530+OR+9428427+OR+9428428+OR+9428429+OR+9428430%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110530,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 110420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 368292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 370334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 373443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 381457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 1557646,
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
    "date_created": "2026-07-05T02:40:01Z",
    "date_modified": "2026-07-06T07:40:38Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:40:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:40:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:44:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:40:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Donovan v. Dewey

```
<opinion type="majority">
<author id="b642-4"><page-number citation-index="1" label="596">*596</page-number>Justice Marshall</author>
<p id="Ah4">delivered the opinion of the Court.</p>
<p id="b642-5">In this case we consider whether § 103 (a) of the Federal Mine Safety and Health Act of 1977, <span class="citation no-link">30 U. S. C. § 813</span> (a) (1976 ed., Supp. Ill), which authorizes warrantless inspections of underground and surface mines, violates the Fourth Amendment. Concluding that searches conducted pursuant to this provision are reasonable within the meaning of the Fourth Amendment, we reverse the judgment of the District Court for the Eastern District of Wisconsin invalidating the statute.</p>
<p id="b642-6">I</p>
<p id="b642-7">The Federal Mine Safety and Health Act of 1977, <span class="citation no-link">91 Stat. 1290</span>, <span class="citation no-link">30 U. S. C. § 801</span> <em>et seq. </em>(1976 ed. and Supp. Ill), requires the Secretary of Labor to develop detailed mandatory health and safety standards to govern the operation of the Nation’s mines. 30 XJ. S. C. §811 (1976 ed., Supp. III).<footnotemark>1</footnotemark> Section 103 (a) of the Act, <span class="citation no-link">30 U. S. C. § 813</span> (a) (1976 ed., Supp. HI), provides that federal mine inspectors are to inspect underground mines at least four times per year and surface mines at least twice a year to insure compliance with these standards, and to make followup inspections to determine whether previously discovered violations have been corrected. This section also grants mine inspectors “a right of entry to, upon, or through any coal or other mine” <footnotemark>2</footnotemark> and states that “no advance notice of an inspection shall be provided to any person.” If a mine operator refuses to allow a warrant-less inspection conducted pursuant to § 103 (a), the Secretary <page-number citation-index="1" label="597">*597</page-number>is authorized to institute a civil action to obtain injunctive or other appropriate relief. <span class="citation no-link">30 U. S. C. § 818</span> (a)(1)(C) (1976 ed., Supp. III).</p>
<p id="b643-5">In July 1978, a federal mine inspector attempted to inspect quarries owned by appellee Waukesha Lime and Stone Co. in order to determine whether all 25 safety and health violations uncovered during a prior inspection had been corrected. After the inspector had been on the site for about an hour, Waukesha’s president, appellee Douglas Dewey, refused to allow the inspection to continue unless the inspector first obtain a search warrant. The inspector issued a citation to Waukesha for terminating the inspection,<footnotemark>3</footnotemark> and the Secretary subsequently filed this civil action in the District Court for the Eastern District of Wisconsin seeking to enjoin appellees from refusing to permit warrantless searches of the Waukesha facility.</p>
<p id="b643-6">The District Court granted summary judgment in favor of appellees on the ground that the Fourth Amendment prohibited the warrantless searches of stone quarries authorized by § 103 (a) of the Act.<footnotemark>4</footnotemark> <span class="citation" data-id="1557646"><a href="/opinion/1557646/marshall-v-dewey/" aria-description="Citation for case: Marshall v. Dewey">493 F. Supp. 963</a></span> (1980). The <page-number citation-index="1" label="598">*598</page-number>Secretary appealed directly to this Court pursuant to <span class="citation no-link">28 U. S. C. § 1252</span>. Because the District Court’s ruling invalidated an important prqvision of the Mine Safety and Health Act, we noted probable jurisdiction.<footnotemark>5</footnotemark> <em>Sub nom. Marshall </em>v. <em>Dewey, </em><span class="citation" data-id="9023790"><a href="/opinion/9030506/marshall-v-dewey/" aria-description="Citation for case: Marshall v. Dewey">449 U. S. 1122</a></span> (1981).</p>
<p id="b644-5">II</p>
<p id="b644-6">Our prior cases have established that the Fourth Amendment’s prohibition against unreasonable searches applies to administrative inspections of private commercial property. <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978); <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967). However, unlike searches of private homes, which generally must be conducted pursuant to a warrant in order to be reasonable under the Fourth Amendment,<footnotemark>6</footnotemark> legislative schemes authorizing warrantless administrative searches of commercial property do not necessarily violate the Fourth Amendment. See, <em>e. g., United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972); <em>Colonnade Catering Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970). The greater latitude to conduct warrantless inspections of commercial property reflects the fact that the expectation of privacy that the owner of commercial property enjoys in such property differs significantly from the sanctity accorded an <page-number citation-index="1" label="599">*599</page-number>individual's home, and that this privacy interest may, in certain circumstances, be adequately protected by regulatory schemes authorizing warrantless inspections. <em>United States </em>v. <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Biswell, supra, </em>at 316</a></span>.</p>
<p id="b645-5">The interest of the owner of commercial property is not one in being free from any inspections. Congress has broad authority to regulate commercial enterprises engaged in or affecting interstate commerce, and an inspection program may in some cases be a necessary component of federal regulation. Rather, the Fourth Amendment protects the interest of the owner of property in being free from <em>unreasonable </em>intrusions onto his property by agents of the government. Inspections of commercial property may be unreasonable if they are not authorized by law or are unnecessary for the furtherance of federal interests. <em>Colonnade Catering Corp. </em>v. <em>United States, supra, </em>at 77. Similarly, warrantless inspections of commercial property may be constitutionally objectionable if their occurrence is so random, infrequent, or unpredictable that the owner, for all practical purposes, has no real expectation that his property will from time to time be inspected by government officials. <em>Marshall </em>v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Barlow’s, Inc., supra, at </em>323</a></span>. “Where Congress has authorized inspection but made no rules governing the procedures that inspectors must follow, the Fourth Amendment and its various restrictive rules apply.” <em>Colonnade Corp. </em>v. <em>United States, supra, </em>at 77. In such cases, a warrant may be necessary to protect the owner from the “unbridled discretion [of] executive and administrative officers,” <em>Marshall </em>v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Barlow’s, Inc., supra, </em>at 323</a></span>, by assuring him that “reasonable legislative or administrative standards for conducting an . . . inspection are satisfied with respect to a particular [establishment].” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 538</a></span> (1967).</p>
<p id="b645-6">However, the assurance of regularity provided by a warrant may be unnecessary under certain inspection schemes. Thus, in <em>Colonnade Corp. </em>v. <em>United States, </em>we recognized that because the alcoholic beverage industry had long been <page-number citation-index="1" label="600">*600</page-number>“subject to close supervision and inspection,” Congress enjoyed “broad power to design such powers of inspection ... as it deems necessary to meet the evils at hand.” <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#76" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 76-77</a></span>. Similarly, in <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>this Court-concluded that the Gun Control Act of 1968, <span class="citation no-link">18 U. S. C. § 921</span> <em>et seq., </em>provided a sufficiently comprehensive and predictable inspection scheme that the warrantless inspections mandated under the statute did not violate the Fourth Amendment. After describing the strong federal interest in conducting unannounced, warrantless inspections, we noted:</p>
<blockquote id="b646-5">“It is also plain that inspections for compliance with the Gun Control Act pose only limited threats to the dealer’s justifiable expectations of privacy. When a dealer chooses to engage in this pervasively regulated business ... , he does so with the knowledge that his records, firearms, and ammunition will be subject to effective inspection. . . . The dealer is not left to wonder about the purposes of the inspector or the limits of his task.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</blockquote>
<p id="b646-6">These decisions make clear that a warrant may not be constitutionally required when Congress has reasonably determined that warrantless searches are necessary to further a regulatory scheme and the federal regulatory presence is sufficiently comprehensive and defined that the owner of commercial property cannot help but be aware that his property will be subject to periodic inspections undertaken for specific purposes.</p>
<p id="b646-7">We re-emphasized this exception to the warrant requirement most recently in <em>Marshall </em>v. <em>Barlow’s, Inc. </em>In that case, we held that absent consent a warrant was constitutionally required in order to conduct administrative inspections under § 8 (a) of the Occupational Safety and Health Act of 1970, <span class="citation no-link">29 U. S. C. §657</span> (a). That statute imposes health and safety standards on all businesses engaged in or affecting interstate commerce that have employees, <span class="citation no-link">29 U. S. C. <page-number citation-index="1" label="601">*601</page-number>§ 652</span> (5), and authorizes representatives of the Secretary to conduct inspections to ensure compliance with the Act. <span class="citation no-link">29 U. S. C. § 657</span> (a). However, the Act fails to tailor the scope and frequency of such administrative inspections to the particular health and safety concerns posed by the numerous and varied businesses regulated by the statute. Instead, the Act flatly authorizes administrative inspections of “any factory, plant, establishment, construction site, or other area, workplace, or environment where work is performed by an employee of an employer” and empowers inspectors conducting such searches to investigate “any such place of employment and all pertinent conditions, structures, machines, apparatus, devices, equipment, and materials therein, and to question privately any such employer, owner, operator, agent, or employee.” <em><span class="citation no-link">Ibid.</span> </em>Similarly, the Act does not provide any standards to guide inspectors either in their selection of establishments to be searched or in the exercise of their authority to search. The statute instead simply provides that such searches must be performed “at . . . reasonable times, and within reasonable limits and in a reasonable manner.” <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b647-5">In assessing this regulatory scheme, this Court found that the provision authorizing administrative searches “devolves almost unbridled discretion upon executive and administrative officers, particularly those in the field, as to when to search and whom to search.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 323</a></span>. Accordingly, we concluded that a warrant was constitutionally required to assure a nonconsenting owner, who may have little real expectation that his business will be subject to inspection, that the contemplated search was “authorized by statute, and . . . pursuant to an administrative plan containing specific neutral criteria.” <em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">Ibid.</a></span> </em>However, we expressly limited our holding to the inspection provisions of the Occupational Safety and Health Act, noting that the “reasonableness of a warrantless search . . . will depend upon the specific enforcement needs and privacy guarantees of each statute” and that some statutes “apply only to a single industry, where <page-number citation-index="1" label="602">*602</page-number>regulations might already be so pervasive that a <em>Colonnade-Biswell </em>exception to the warrant requirement could apply.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#321" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Id., </em>at 321</a></span>.</p>
<p id="b648-4">Applying this analysis to the case before us, we conclude that the warrantless inspections required by the Mine Safety and Health Act do not offend the Fourth Amendment. As an initial matter, it is undisputed that there is a substantial federal interest in improving the health and safety conditions in the Nation’s underground and surface mines. In enacting the statute, Congress was plainly aware that the mining industry is among the most hazardous in the country and that the poor health and safety record of this industry has significant deleterious effects on interstate commerce.<footnotemark>7</footnotemark> Nor is it seriously contested that Congress in this case could reasonably determine, as it did with respect to the Gun Control Act in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>that a system of warrantless inspections was <page-number citation-index="1" label="603">*603</page-number>necessary “if the law is to be properly enforced and inspection made effective.” <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>. In designing an inspection program. Congress expressly recognized that a warrant requirement could significantly frustrate effective enforcement of the Act. Thus, it provided in § 103 (a) of the Act that “no advance notice of an inspection shall be provided to any person.” In explaining this provision, the Senate Report notes:</p>
<blockquote id="b649-5">“[I]n [light] of the notorious ease with which many safety or health hazards may be concealed if advance warning of inspection is obtained, a warrant requirement would seriously undercut this Act’s objectives.” S. Rep. No. 95-181, p. 27 (1977).</blockquote>
<p id="b649-6">We see no reason not to defer to this legislative determination. Here, as in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>Congress could properly conclude: “[I]f inspection is to be effective and serve as a credible deterrent, unannounced, even frequent, inspections are essential. In this context, the prerequisite of a warrant could easily frustrate inspection.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</p>
<p id="b649-7">Because a warrant requirement clearly might impede the “specific enforcement needs” of the Act, <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#321" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 321</a></span>, the only real issue before us is whether the statute’s inspection program, in terms of the certainty and regularity of its application, provides a constitutionally adequate substitute for a warrant. We believe that it does. Unlike the statute at issue in <em>Barlow’s, </em>the Mine Safety and Health Act applies to industrial activity with a notorious history of serious accidents and unhealthful working conditions. The Act is specifically tailored to address those concerns,<footnotemark>8</footnotemark> and the regulation of mines it imposes is sufficiently pervasive and defined that the owner of such a facility cannot help but be aware that he “will be subject to effective inspection.” <em>United States </em>v. <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Biswell, supra, </em>at 316</a></span>. First, the Act re<page-number citation-index="1" label="604">*604</page-number>quires inspection of <em>all </em>mines and specifically defines the frequency of inspection. Representatives of the Secretary must inspect all surface mines at least twice annually and all underground mines at least four times annually. <span class="citation no-link">30 U. S. C. § 813</span> (a) (1976 ed., Supp. III). Similarly, all mining operations that generate explosive gases must be inspected at irregular 5-, 10-, or 15-day intervals. § 813 (i). Moreover, the Secretary must conduct followup inspections of mines where violations of the Act have previously been discovered, § 813 (a), and must inspect a mine immediately if notified by a miner or a miner’s representative that a violation of the Act or an imminently dangerous condition exists. § 813 (g).<footnotemark>9</footnotemark> Second, the standards with which a mine operator is required to comply are all specifically set forth in the Act or in Title 30 of the Code of Federal Regulations. Indeed, the Act requires that the Secretary inform mine operators of all standards proposed pursuant to the Act. § 811 (e). Thus, rather than leaving the frequency and purpose of inspections to the unchecked discretion of Government officers, the Act establishes a predictable and guided federal regulatory presence. Like the gun dealer in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>the operator of a mine “is not left to wonder about the purposes of the inspector or the limits of his task.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</p>
<p id="b650-5">Finally, the Act provides a specific mechanism for accommodating any special privacy concerns that a specific mine operator might have. The Act prohibits forcible entries, and instead requires the Secretary, when refused entry onto a mining facility, to file a civil action in federal court to obtain an injunction against future refusals. <span class="citation no-link">30 U. S. C. § 818</span> (a) (1976 ed., Supp. III). This proceeding provides an <page-number citation-index="1" label="605">*605</page-number>adequate forum for the mineowner to show that a specific search is outside the federal regulatory authority, or to seek from the district court an order accommodating any unusual privacy interests that the mineowner might have. See, <em>e. g., Marshall </em>v. <em>Stoudt’s Ferry Preparation Co., </em><span class="citation" data-id="368292"><a href="/opinion/368292/ray-marshall-secretary-of-labor-united-states-department-of-labor-v/#594" aria-description="Citation for case: Ray Marshall, Secretary of Labor, United States...">602 F. 2d 589, 594</a></span> (CA3 1979) (inspectors ordered to keep confidential mine's trade secrets), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/1015/">444 U. S. 1015</a></span> (1980).</p>
<p id="b651-5">Under these circumstances, it is difficult to see what additional protection a warrant requirement would provide. The Act itself clearly notifies the operator that inspections will be performed on a regular basis. Moreover, the Act and the regulations issued pursuant to it inform the operator of what health and safety standards must be met in order to be in compliance with the statute. The discretion of Government officials to determine what facilities to search and what violations to search for is thus directly curtailed by the regulatory scheme. In addition, the statute itself embodies a means by which any special Fourth Amendment interests can be accommodated. Accordingly, we conclude that the general program of warrantless inspections authorized by § 103 (a) of the Act does not violate the Fourth Amendment.</p>
<p id="b651-6">Appellees contend, however, that even if § 103 (a) is constitutional as applied to most segments of the mining industry, it nonetheless violates the Fourth Amendment as applied to authorize warrantless inspections of stone quarries. Appel-lees’ argument essentially tracks the reasoning of the court below. That court, while expressly acknowledging our decisions in <em>Colonnade </em>and <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>found the exception to the warrant requirement defined in those cases to be inapplicable solely because surface quarries, which came under federal regulation in 1966,<footnotemark>10</footnotemark> do “not have a long tradition of government regulation.” <span class="citation" data-id="1557646"><a href="/opinion/1557646/marshall-v-dewey/#964" aria-description="Citation for case: Marshall v. Dewey">493 F. Supp., at 964</a></span>. To be sure, in <em>Colonnade </em>this Court referred to “the long history of the <page-number citation-index="1" label="606">*606</page-number>regulation of the liquor industry,” <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#75" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 75</a></span>, and more recently in <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 313</a></span>, we noted that a “long tradition of close government supervision” militated against imposition of a warrant requirement. However, as previously noted, see <em>supra, </em>at 599, it is the pervasiveness and regularity of the federal regulation that ultimately determines whether a warrant is necessary to render an inspection program reasonable under the Fourth Amendment. Thus in <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>this Court upheld the warrantless search provisions of the Gun Control Act of 1968 despite the fact that “[f]ederal regulation of the interstate traffic in firearms is not as deeply rooted in history as is governmental control of the liquor industry.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>. Of course, the duration of a particular regulatory Scheme will often be an important factor in determining whether it is sufficiently pervasive to make the imposition of a warrant requirement unnecessary. But if the length of regulation were the only criterion, absurd results would occur. Under appellees’ view, new or emerging industries, including ones such as the nuclear power industry that pose enormous potential safety and health problems, could never be subject to warrantless searches even under the most carefully structured inspection program simply because of the recent vintage of regulation.</p>
<p id="b652-5">The Fourth Amendment’s central concept of reasonableness will not tolerate such arbitrary results, and we therefore conclude that warrantless inspection of stone quarries, like similar inspections of other mines covered by the Act, are constitutionally permissible. The judgment of the District Court is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b652-6">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b642-8"> The Act supersedes the Federal Coal Mine Health and Safety Act of 1969, formerly <span class="citation no-link">30 U. S. C. § 801</span> <em>et seq., </em>and repeals and replaces the Federal Metal and Nonmetallic Mine Safety Act of 1966, formerly <span class="citation no-link">30 U. S. C. § 721</span> <em>et seq.</em></p>
</footnote>
<footnote label="2">
<p id="b642-9"> The Act defines “coal or other mine” to include “an area of land from which minerals are extracted in nonliquid form or, if in liquid form, are extracted with workers underground.” <span class="citation no-link">30 U. S. C. § 802</span> (h) (1) (1976 ed., Supp. III). It is undisputed that the quarry operated by appellee company falls within this definition.</p>
</footnote>
<footnote label="3">
<p id="b643-7"> The Act provides that the Secretary shall issue citations and propose civil penalties for violations of the Act or standards promulgated under the Act. <span class="citation no-link">30 U. S. C. §§ 814</span> (a), 820 (a) (1976 ed., Supp. III). The Secretary’s regulations call for issuance of a citation and the assessment of a civil penalty for denial of entry. <span class="citation no-link">30 CFR § 100.4</span> (1980). The Act also allows a mine operator to contest any citation in a hearing before an administrative law judge, whose decision is subject to discretionary review by the Mine Safety and Health Review Commission. <span class="citation no-link">30 U. S. C. §§ 815</span> (d), 823 (d) (1976 ed., Supp. III). The operator thereafter is entitled to review of a final administrative ruling in the appropriate court of appeals. <span class="citation no-link">30 U. S. C. §816</span> (1976 ed., Supp. III).</p>
<p id="b643-8">In this case, the Administrative Law Judge upheld a $1,000 civil penalty proposed by the Secretary. This decision is currently under review by the Mine Safety and Health Review Commission.</p>
</footnote>
<footnote label="4">
<p id="b643-9"> Although the District Court limited its holding to the constitutionality of § 103 (a) as applied to warrantless inspections of stone quarries, the Act makes no distinction as to the type of mine to be inspected, and our <page-number citation-index="1" label="598">*598</page-number>conclusions here apply equally to all warrantless inspections authorized by the Act.</p>
</footnote>
<footnote label="5">
<p id="b644-9"> Three Courts of Appeals have upheld the warrantless inspection provisions of the Act as they apply to quarry operations similar to appellees’ facility. See <em>Marshall </em>v. <em>Texoline Co., </em><span class="citation" data-id="8910771"><a href="/opinion/8921866/marshall-v-texoline-co/" aria-description="Citation for case: Marshall v. Texoline Co.">612 F. 2d 935</a></span> (CA5 1980); <em>Marshall </em>v. <em>Nolichuckey Sand Co., </em><span class="citation" data-id="370334"><a href="/opinion/370334/ray-marshall-secretary-of-labor-united-states-department-of-labor-v/" aria-description="Citation for case: Ray Marshall, Secretary of Labor, United States...">606 F. 2d 693</a></span> (CA6 1979), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./446/908/">446 U. S. 908</a></span> (1980); <em>Marshall </em>v. <em>Stoudt’s Ferry Preparation Co., </em><span class="citation" data-id="368292"><a href="/opinion/368292/ray-marshall-secretary-of-labor-united-states-department-of-labor-v/" aria-description="Citation for case: Ray Marshall, Secretary of Labor, United States...">602 F. 2d 589</a></span> (CA3 1979), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/1015/">444 U. S. 1015</a></span> (1980).</p>
</footnote>
<footnote label="6">
<p id="b644-10"> Absent consent or exigent circumstances, a private home may not be entered to conduct a search or effect an arrest without a warrant. <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U. S. 204</a></span> (1981); <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948). Of course, these same restrictions pertain when commercial property is searched for contraband or evidence of crime. <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#352" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 352-359</a></span> (1977).</p>
</footnote>
<footnote label="7">
<p id="b648-5"> In the preamble to the Act, Congress declared:</p>
<blockquote id="b648-6">“[T]here is an urgent need to provide more effective means and measures for improving the working conditions and practices in the Nation’s coal or other mines in order to prevent death and serious physical harm, and in order to prevent occupational diseases originating in such mines. . . .</blockquote>
<blockquote id="b648-7">“[T]he existence of unsafe and unhealthful conditions and practices in the Nation’s coal or other mines is a serious impediment to the future growth of the coal and other mining industry and cannot be tolerated. . . .</blockquote>
<blockquote id="b648-8">“[T]he disruption of production and the loss of income to operators and miners as a result of coal or other mine accidents or occupationally caused diseases unduly impedes and burdens commerce.” <span class="citation no-link">30 U. S. C. §§ 801</span> (c), (d), (f).</blockquote>
<p id="b648-9">These congressional findings were based on extensive evidence showing that the mining industry was among the most hazardous of the Nation’s industries. See S. Rep. No. 95-181 (1977); H. R. Rep. No. 95-312 (1977). Although Congress did not make explicit reference to stone quarries in these findings, stone quarries were deliberately included within the scope of the statute. Since the Mine Safety and Health Act, unlike the Occupational Safety and Health Act, is narrowly and explicitly directed at inherently dangerous industrial activity, the inclusion of stone quarries in the statute is presumptively equivalent to a finding that the stone quarrying industry is inherently dangerous.</p>
</footnote>
<footnote label="8">
<p id="b649-8"> Cf. H. R. Rep. No. 95-312, <em>supra, </em>at 1 (mining operations are “so unique, so complex, and so hazardous as to not fit neatly under the Occupational Safety and Health Act”).</p>
</footnote>
<footnote label="9">
<p id="b650-6"> In contrast, the inspection scheme considered in <em>Barlow’s </em>did not require the periodic inspection of businesses covered by the Occupational Safety and Health Act, and instead left the decision to inspect within the broad discretion of agency officials. Thus, when a Government official attempted to inspect the facility in that case, the owner had no indication of “why an inspection of [his] establishment was within the program.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 323, n. 20</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b651-7"> Stone quarries were first subjected to federal health and safety inspections under the Federal Metal and Nonmetallie Mine Safety Act of 1966, 30 TJ. S. C. §§ 723, 724.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Dow Chemical Co. v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Dow Chemical Co. v. United States"
type: case
citation: "476 U.S. 227 (1986)"
parallel_cite: "106 S. Ct. 1819; 90 L. Ed. 2d 226; 16 Envtl. L. Rep. (Envtl. Law Inst.) 20679; 54 U.S.L.W. 4464; 24 ERC (BNA) 1385"
neutral_cite: 1986 U.S. LEXIS 155
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-05-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-05-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Dow Chemical Co. v. United States
  varies_by_point: false
  scope_note: "Good law; the open-areas-as-open-fields/navigable-airspace holding remains the governing rule for aerial observation of commercial and industrial premises."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/"
  cluster_id: 111667
  opinion_id: 9430504
  identity_checked: true
homes:
  - page: "[[Aerial and Enhanced Surveillance]]"
    role: "Key — Anchor"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[California v. Ciraolo]]", "[[Florida v. Riley]]", "[[Oliver v. United States]]", "[[Kyllo v. United States]]"]
aliases: ["Dow Chemical Co. v. United States Ex Rel. Administrator"]
tags: ["case", "fourth-amendment", "search", "aerial-surveillance", "open-fields", "curtilage", "commercial-premises"]
holding: "Precision aerial photography of the open areas of an industrial complex from navigable airspace is not a Fourth Amendment search; such open areas are more like open fields than the curtilage of a home."
lake:
  record_id: Dow Chemical Co. v. United States
  status: verified
  projected_at: 2026-07-09
---

# Dow Chemical Co. v. United States

*476 U.S. 227 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Dow refused a follow-up EPA inspection of its 2,000-acre chemical-manufacturing complex, the EPA hired a commercial aerial photographer who used a precision aerial mapping camera to photograph the plant's open areas from lawful navigable airspace. Dow sued, claiming the overflight photography was a Fourth Amendment search of an "industrial curtilage" in which it had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Issue
Whether the EPA's warrantless taking of aerial photographs of the open areas of an industrial plant complex, from navigable airspace, constitutes a "search" under the Fourth Amendment.

## Rule
No. The open areas of a large industrial complex are not the constitutional equivalent of the [[Curtilage|curtilage]] of a home; "such an industrial complex is more comparable to an open field and as such it is open to the view and observation of persons in aircraft lawfully in the public airspace immediately above or sufficiently near the area for the reach of cameras." — 476 U.S. at 239. ^pin-239

Accordingly, "the taking of aerial photographs of an industrial plant complex from navigable airspace is not a search prohibited by the Fourth Amendment." — [*Id.*](https://www.courtlistener.com/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/#:~:text=the%20taking%20of%20aerial%20photographs) ^pin-239a

## Application
Dow's exposed manufacturing facilities, though enclosed against ground-level intrusion, were open to observation from the air. Because the photographs were taken from lawful navigable airspace using a conventional (if precise) mapping camera, and because the open areas of the complex resembled open fields rather than the intimate [[Curtilage|curtilage]] of a dwelling, Dow had no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] against the overflight. The Court noted only that surveillance revealing intimate, enclosed details — or use of highly sophisticated equipment not generally available — might raise different questions, but the mapping photography here did not.

## Conclusion
The aerial photography was not a Fourth Amendment search. The judgment for the United States was affirmed on the constitutional question.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Decided the same day as [[California v. Ciraolo]] (naked-eye aerial view of a home's [[Curtilage|curtilage]]) and reinforced by [[Florida v. Riley]] (helicopter observation). [[Kyllo v. United States]] (2001) later cabined *sense-enhancing technology* directed at the *home's* interior, distinguishing the open-area/commercial setting here.

## Appears on
- [[Aerial and Enhanced Surveillance]] — *Key — Anchor*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *Dow Chemical Co. v. United States*, 476 U.S. 227 (1986) — https://www.courtlistener.com/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/ — pinpoint: 239.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "041136740b890f16", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "476 U.S. 227 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 155", "official_citation_present": true, "parallel_cite": "106 S. Ct. 1819; 90 L. Ed. 2d 226; 16 Envtl. L. Rep. (Envtl. Law Inst.) 20679; 54 U.S.L.W. 4464; 24 ERC (BNA) 1385", "title": "Dow Chemical Co. v. United States", "year": "1986"}}
{"assertion_id": "248775b6a5a63be8", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "Dow Chemical Co. v. United States"}}
{"assertion_id": "bfea93984a9972df", "dimension": "support", "kind": "home_role", "locator": {"home": "Aerial and Enhanced Surveillance"}, "payload": {"home": "Aerial and Enhanced Surveillance", "role": "Key — Anchor", "title": "Dow Chemical Co. v. United States"}}
{"assertion_id": "e508b1c24f40464e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Precision aerial photography of the open areas of an industrial complex from navigable airspace is not a Fourth Amendment search; such open areas are more like open fields than the curtilage of a home.", "title": "Dow Chemical Co. v. United States"}}
{"assertion_id": "79ce59f3d9ab1532", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Dow Chemical Co. v. United States"}}
{"assertion_id": "d37f3e137c91943f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1986-05-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Dow Chemical Co. v. United States", "field_i_validity": "good_law", "scope_note": "Good law; the open-areas-as-open-fields/navigable-airspace holding remains the governing rule for aerial observation of commercial and industrial premises.", "title": "Dow Chemical Co. v. United States", "varies_by_point": "false"}}
```

### lake record — Dow Chemical Co. v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Dow Chemical Co. v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Dow Chemical Co. v. United States Ex Rel. Administrator",
    "case_name_short": "",
    "case_name_full": "DOW CHEMICAL CO. v. UNITED STATES, by and Through ADMINISTRATOR, ENVIRONMENTAL PROTECTION AGENCY",
    "input_case_name": "Dow Chemical Co. v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-05-19",
    "year": 1986,
    "docket": null,
    "cluster_id": 111667,
    "lead_opinion_id": 9430504,
    "sibling_ids": [
      111667,
      9430504,
      9430505
    ],
    "absolute_url": "/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "476 U.S. 227",
      "volume": "476",
      "reporter": "U.S.",
      "page": "227",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 1819",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 L. Ed. 2d 226",
        "volume": "90",
        "reporter": "L. Ed. 2d",
        "page": "226",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679",
        "volume": "16",
        "reporter": "Envtl. L. Rep. (Envtl. Law Inst.)",
        "page": "20679",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4464",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4464",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 ERC (BNA) 1385",
        "volume": "24",
        "reporter": "ERC (BNA)",
        "page": "1385",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 155",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "155",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "476 U.S. 227",
        "volume": "476",
        "reporter": "U.S.",
        "page": "227",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1819",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 L. Ed. 2d 226",
        "volume": "90",
        "reporter": "L. Ed. 2d",
        "page": "226",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 155",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "155",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679",
        "volume": "16",
        "reporter": "Envtl. L. Rep. (Envtl. Law Inst.)",
        "page": "20679",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4464",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4464",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 ERC (BNA) 1385",
        "volume": "24",
        "reporter": "ERC (BNA)",
        "page": "1385",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "476 U.S. 227",
    "official_selection": {
      "court_class": "scotus",
      "selected": "476 U.S. 227",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-239",
      "page": null,
      "quote": "under the Fourth Amendment. ## Rule No. The open areas of a large industrial complex are not the constitutional equivalent of the curtilage of a home;",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-239a",
      "page": null,
      "quote": "the taking of aerial photographs of an industrial plant complex from navigable airspace is not a search prohibited by the Fourth Amendment.",
      "star_marker": "239",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26872,
      "fragment": "#:~:text=the%20taking%20of%20aerial%20photographs",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-05-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Dow Chemical Co. v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; the open-areas-as-open-fields/navigable-airspace holding remains the governing rule for aerial observation of commercial and industrial premises.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. McCarthy",
          "cluster_id": 4746120,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Martin",
          "cluster_id": 1978636,
          "cite": [
            "2008 VT 53",
            "955 A.2d 1144",
            "184 Vt. 23",
            "2008 Vt. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Opinion Piedad Barajas-Avaslos",
          "cluster_id": 785295,
          "cite": [
            "359 F.3d 1204",
            "2004 U.S. App. LEXIS 4569",
            "2004 D.A.R. 3084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terry James Pierre and Otis Harris, III",
          "cluster_id": 560501,
          "cite": [
            "932 F.2d 377",
            "1991 U.S. App. LEXIS 10296",
            "1991 WL 82423"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane1_negative"
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
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dunn",
          "cluster_id": 111833,
          "cite": [
            "94 L. Ed. 2d 326",
            "107 S. Ct. 1134",
            "480 U.S. 294",
            "1987 U.S. LEXIS 1057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oles v. State",
          "cluster_id": 1762668,
          "cite": [
            "993 S.W.2d 103",
            "1999 Tex. Crim. App. LEXIS 53",
            "1999 WL 330266"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Riley",
          "cluster_id": 112175,
          "cite": [
            "102 L. Ed. 2d 835",
            "109 S. Ct. 693",
            "488 U.S. 445",
            "1989 U.S. LEXIS 580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hector Vega-Rodriguez v. Puerto Rico Telephone Company",
          "cluster_id": 739069,
          "cite": [
            "110 F.3d 174",
            "12 I.E.R. Cas. (BNA) 1253",
            "1997 U.S. App. LEXIS 6517",
            "1997 WL 154362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio Civil Service Employees Association v. Richard P. Seiter",
          "cluster_id": 512622,
          "cite": [
            "858 F.2d 1171",
            "3 I.E.R. Cas. (BNA) 1623",
            "1988 U.S. App. LEXIS 13585",
            "1988 WL 100808"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hector Hernan Hoyos",
          "cluster_id": 534551,
          "cite": [
            "892 F.2d 1387"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Elkins Carol Elkins, United States of America v. Carol Elkins James Elkins",
          "cluster_id": 778775,
          "cite": [
            "300 F.3d 638"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darlie Kee Darin Routier v. City of Rowlett Texas Jimmy Ray Patterson Chris Frosch Greg Davis, Assistant District Attorney for Dallas County",
          "cluster_id": 772922,
          "cite": [
            "247 F.3d 206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vaughn Neita v. City of Chicago",
          "cluster_id": 4239934,
          "cite": [
            "830 F.3d 494",
            "2016 U.S. App. LEXIS 13191",
            "2016 WL 3905604"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Betts, Tony",
          "cluster_id": 2948317,
          "cite": [
            "397 S.W.3d 198",
            "2013 WL 1628963",
            "2013 Tex. Crim. App. LEXIS 705"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Palmieri v. Pamela Lynch, AKA Pam Lynch, John Doe 1",
          "cluster_id": 788624,
          "cite": [
            "392 F.3d 73",
            "2004 U.S. App. LEXIS 25468",
            "2004 WL 2827676"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tom Wilkinson Eastland, and Cullen Reed Harris",
          "cluster_id": 603530,
          "cite": [
            "989 F.2d 760",
            "1993 U.S. App. LEXIS 7723",
            "1993 WL 112732"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wabun-Inini, AKA Vernon Bellecourt v. William Sessions, Director, Federal Bureau of Investigation, Washington, D.C. Jeffrey J. Jamar, Agent-In-Charge, Minneapolis Office of the Fbi, Minneapolis, Minnesota Peter Cunningham, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota William Clifford, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota John Doe Jane Doe, and Other Presently Unknown Officials of the United States Government, Wabun-Inini, AKA Vernon Bellecourt v. William Sessions, Director, Federal Bureau of Investigation, Washington, D.C. Jeffrey J. Jamar, Agent-In-Charge, Minneapolis Office of the Fbi, Minneapolis, Minnesota Peter Cunningham, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota William Clifford, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota John Doe Jane Doe, and Other Presently Unknown Officials of the United States Government",
          "cluster_id": 539907,
          "cite": [
            "900 F.2d 1234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Connolly",
          "cluster_id": 6580040,
          "cite": [
            "454 Mass. 808",
            "913 N.E.2d 356",
            "2009 Mass. LEXIS 642"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Norris",
          "cluster_id": 1079931,
          "cite": [
            "47 S.W.3d 457",
            "2000 Tenn. Crim. App. LEXIS 437",
            "2000 WL 710506"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wacker",
          "cluster_id": 1364515,
          "cite": [
            "856 P.2d 1029",
            "317 Or. 419",
            "1993 Ore. LEXIS 130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Noel C. Jenkins (96-5338) Linda L. Jenkins (96-5346)",
          "cluster_id": 746252,
          "cite": [
            "124 F.3d 768"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ainsworth",
          "cluster_id": 1442371,
          "cite": [
            "801 P.2d 749",
            "310 Or. 613",
            "1990 Ore. LEXIS 361"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson, Lamar v. Quander, Paul A.",
          "cluster_id": 186640,
          "cite": [
            "440 F.3d 489",
            "370 U.S. App. D.C. 167",
            "2006 U.S. App. LEXIS 6601",
            "2006 WL 662748"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111667 OR 9430504 OR 9430505) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 145,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 145,
        "triage_read": 4,
        "triage_snippet_classified": 141
      },
      "lane2_top_cited": {
        "query": "cites:(111667 OR 9430504 OR 9430505)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MyZzPTc1MjM1OSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111667+OR+9430504+OR+9430505%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111667 OR 9430504 OR 9430505)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111667 OR 9430504 OR 9430505)",
    "indexed_citing_opinions": 210,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111667,
        "count": 180,
        "count_source": "search"
      },
      {
        "opinion_id": 9430504,
        "count": 39,
        "count_source": "search"
      },
      {
        "opinion_id": 9430505,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 342,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/dow-chemical-co-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3MzQwMSZzPTQ3NDYxMjAmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111667+OR+9430504+OR+9430505%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111667,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 110062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 404175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 445066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 2009668,
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
    "date_created": "2026-07-05T02:44:19Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:44:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:44:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:48:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:44:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Dow Chemical Co. v. United States

```
<opinion type="majority">
<author id="b293-4"><page-number citation-index="1" label="229">*229</page-number>Chief Justice Burger</author>
<p id="ALr">delivered the opinion of the Court.</p>
<p id="b293-5">We granted certiorari to review the holding of the Court of Appeals (a) that the Environmental Protection Agency’s aerial observation of petitioner’s plant complex did not exceed EPA’s statutory investigatory authority, and (b) that EPA’s aerial photography of petitioner’s 2,000-acre plant complex without a warrant was not a search under the Fourth Amendment.</p>
<p id="b293-6">I</p>
<p id="b293-7">Petitioner Dow Chemical Co. operates a 2,000-acre facility manufacturing chemicals at Midland, Michigan. The facility consists of numerous covered buildings, with manufacturing equipment and piping conduits located between the various buildings exposed to visual observation from the air. At all times, Dow has maintained elaborate security around the perimeter of the complex barring ground-level public views of these areas. It also investigates any low-level flights by aircraft over the facility. Dow has not undertaken, however, to conceal all manufacturing equipment within the complex from aerial views. Dow maintains that the cost of covering its exposed equipment would be prohibitive.</p>
<p id="b293-8">In early 1978, enforcement officials of EPA, with Dow’s consent, made an on-site inspection of two powerplants in this complex. A subsequent EPA request for a second inspection, however, was denied, and EPA did not thereafter seek an administrative search warrant. Instead, EPA employed a commercial aerial photographer, using a standard floor-mounted, precision aerial mapping camera, to take photographs of the facility from altitudes of 12,000, 3,000, and 1,200 feet. At all times the aircraft was lawfully within navigable airspace. See 49 U. S. C. App. § 1304; <span class="citation no-link">14 CFR § 91.79</span> (1985).</p>
<p id="b294-4"><page-number citation-index="1" label="230">*230</page-number>EPA did not inform Dow of this aerial photography, but when Dow became aware of it, Dow brought suit in the District Court alleging that EPA’s action violated the Fourth Amendment and was beyond EPA’s statutory investigative authority. The District Court granted Dow’s motion for summary judgment on the ground that EPA had no authority to take aerial photographs and that doing so was a search violating the Fourth Amendment. EPA was permanently enjoined from taking aerial photographs of Dow’s premises and from disseminating, releasing, or copying the photographs already taken. <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch">536 F. Supp. 1355</a></span> (ED Mich. 1982).</p>
<p id="b294-5">The District Court accepted the parties’ concession that EPA’s “‘quest for evidence’” was a “search,” <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/#1358" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch"><em>id., </em>at 1358</a></span>, and limited its analysis to whether the search was unreasonable under <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). Proceeding on the assumption that a search in Fourth Amendment terms had been conducted, the court found that Dow manifested an expectation of privacy in its exposed plant areas because it intentionally surrounded them with buildings and other enclosures. <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/#1364" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch">536 F. Supp., at 1364-1366</a></span>.</p>
<p id="b294-6">The District Court held that this expectation of privacy was reasonable, as reflected in part by trade secret protections restricting Dow’s commercial competitors from aerial photography of these exposed areas. <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/#1366" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch"><em>Id., </em>at 1366-1369</a></span>. The court emphasized that use of “the finest precision aerial camera available” permitted EPA to capture on film “a great deal more than the human eye could ever see.” <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/#1367" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch"><em>Id., </em>at 1367</a></span>.</p>
<p id="b294-7">The Court of Appeals reversed. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and...">749 F. 2d 307</a></span> (CA6 1984). It recognized that Dow indeed had a subjective expectation of privacy in certain areas from ground-level intrusions, but the court was not persuaded that Dow had a subjective expectation of being free from <em>aerial </em>surveillance since Dow had taken no precautions against such observation, in contrast to its elaborate ground-level precautions. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#313" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 313</a></span>. The court rejected the argument that it was not feasible to shield any of the critical parts of the exposed plant areas from aerial surveys. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#312" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 312-313</a></span>. The Court of Appeals, <page-number citation-index="1" label="231">*231</page-number>however, did not explicitly reject the District Court’s factual finding as to Dow’s subjective expectations.</p>
<p id="b295-5">Accepting the District Court finding of Dow’s privacy expectation, the Court of Appeals held that it was not a reasonable expectation “[w]hen the entity observed is a multibuilding complex, and the area observed is the outside of these buildings and the spaces in between the buildings.” <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#313" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 313</a></span>. Viewing Dow’s facility to be more like the “open field” in <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984), than a home or an office, it held that the common-law curtilage doctrine did not apply to a large industrial complex of closed buildings connected by pipes, conduits, and other exposed manufacturing equipment. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#313" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and...">749 F. 2d, at 313-314</a></span>. The Court of Appeals looked to “the peculiarly strong concepts of intimacy, personal autonomy and privacy associated with the home” as the basis for the curtilage protection. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#314" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 314</a></span>. The court did not view the use of sophisticated photographic equipment by EPA as controlling.</p>
<p id="Abd">The Court of Appeals then held that EPA clearly acted within its statutory powers even absent express authorization for aerial surveillance, concluding that the delegation of general investigative authority to EPA, similar to that of other law enforcement agencies, was sufficient to support the use of aerial photography. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#315" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 315</a></span>.</p>
<p id="b295-7">II</p>
<p id="b295-8">The photographs at issue in this case are essentially like those commonly used in mapmaking. Any person with an airplane and an aerial camera could readily duplicate them. In common with much else, the technology of photography has changed in this century. These developments have enhanced industrial processes, and indeed all areas of life; they have also enhanced law enforcement techniques. Whether they may be employed by competitors to penetrate trade secrets is not a question presented in this case. Governments do not generally seek to appropriate trade secrets of the pri<page-number citation-index="1" label="232">*232</page-number>vate sector, and the right to be free of appropriation of trade secrets is protected by law.</p>
<p id="b296-5">Dow nevertheless relies heavily on its claim that trade secret laws protect it from any aerial photography of this industrial complex by its competitors, and that this protection is relevant to our analysis of such photography under the Fourth Amendment. That such photography might be barred by state law with regard to competitors, however, is irrelevant to the questions presented here. State tort law governing unfair competition does not define the limits of the Fourth Amendment. Cf. <em>Oliver </em>v. <em>United States, supra </em>(trespass law does not necessarily define limits of Fourth Amendment). The Government is seeking these photographs in order to regulate, not to compete with, Dow. If the Government were to use the photographs to compete with Dow, Dow might have a Fifth Amendment “taking” claim. Indeed, Dow alleged such a claim in its complaint, but the District Court dismissed it without prejudice. But even trade secret laws would not bar all forms of photography of this industrial complex; rather, only photography with an intent to use any trade secrets revealed by the photographs may be proscribed. Hence, there is no prohibition of photographs taken by a casual passenger on an airliner, or those taken by a company producing maps for its mapmaking purposes.</p>
<p id="b296-6">Dow claims first that EPA has no authority to use aerial photography to implement its statutory authority for “site inspection” under § 114(a) of the Clean Air Act, <span class="citation no-link">42 U. S. C. § 7414</span>(a);<footnotemark>1</footnotemark> second, Dow claims EPA’s use of aerial photogra<page-number citation-index="1" label="233">*233</page-number>phy was a “search” of an area that, notwithstanding the large size of the plant, was within an “industrial curtilage” rather than an “open field,” and that it had a reasonable expectation of privacy from such photography protected by the Fourth Amendment.</p>
<p id="b297-4">Ill</p>
<p id="b297-5">Congress has vested in EPA certain investigatory and enforcement authority, without spelling out precisely how this authority was to be exercised in all the myriad circumstances that might arise in monitoring matters relating to clean air and water standards. When Congress invests an agency with enforcement and investigatory authority, it is not necessary to identify explicitly each and every technique that may be used in the course of executing the statutory mission. Aerial observation authority, for example, is not usually expressly extended to police for traffic control, but it could hardly be thought necessary for a legislative body to tell police that aerial observation could be employed for traffic control of a metropolitan area, or to expressly authorize police to send messages to ground highway patrols that a particular over-the-road truck was traveling in excess of 55 miles per hour. Common sense and ordinary human experience teach that traffic violators are apprehended by observation.</p>
<p id="b297-6">Regulatory or enforcement authority generally carries with it all the modes of inquiry and investigation traditionally employed or useful to execute the authority granted. Environmental standards such as clean air and clean water cannot be enforced only in libraries and laboratories, helpful as those institutions may be.</p>
<p id="b297-7">Under § 114(a)(2), the Clean Air Act provides that “upon presentation of. . . credentials,” EPA has a “right of entry to, upon, or through any premises.” <span class="citation no-link">42 U. S. C. § 7414</span>(a)(2)(A). Dow argues this limited grant of authority to enter does not <page-number citation-index="1" label="234">*234</page-number>authorize any aerial observation. In particular, Dow argues that unannounced aerial observation deprives Dow of its right to be informed that an inspection will be made or has occurred, and its right to claim confidentiality of the information contained in the places to be photographed, as provided in §§ 114(a) and (c), <span class="citation no-link">42 U. S. C. §§ 7414</span>(a) and (c). It is not claimed that EPA has disclosed any of the photographs outside the agency.</p>
<p id="b298-5">Section 114(a), however, appears to expand, not restrict, EPA’s general powers to investigate. Nor is there any suggestion in the statute that the powers conferred by this section are intended to be exclusive. There is no claim that EPA is prohibited from taking photographs from a ground-level location accessible to the general public. EPA, as a regulatory and enforcement agency, needs no explicit statutory provision to employ methods of observation commonly available to the public at large: we hold that the use of aerial observation and photography is within EPA’s statutory authority.<footnotemark>2</footnotemark></p>
<p id="b298-6">IV</p>
<p id="b298-7">We turn now to Dow’s contention that taking aerial photographs constituted a search without a warrant, thereby violating Dow’s rights under the Fourth Amendment. In making this contention, however, Dow concedes that a simple flyover with naked-eye observation, or the taking of a photograph from a nearby hillside overlooking such a facility, would give rise to no Fourth Amendment problem.</p>
<p id="b298-8">In <em>California </em>v. <em>Ciraolo, ante, </em>p. 207, decided today, we hold that naked-eye aerial observation from an altitude of <page-number citation-index="1" label="235">*235</page-number>1,000 feet of a backyard within the curtilage of a home does not constitute a search under the Fourth Amendment.</p>
<p id="b299-5">In the instant case, two additional Fourth Amendment claims are presented: whether the common-law “curtilage” doctrine encompasses a large industrial complex such as Dow’s, and whether photography employing an aerial mapping camera is permissible in this context. Dow argues that an industrial plant, even one occupying 2,000 acres, does not fall within the “open fields” doctrine of <em>Oliver </em>v. <em>United States </em>but rather is an “industrial curtilage” having constitutional protection equivalent to that of the curtilage of a private home. Dow farther contends that any aerial photography of this “industrial curtilage” intrudes upon its reasonable expectations of privacy. Plainly a business establishment or an industrial or commercial facility enjoys certain protections under the Fourth Amendment. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978); <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967).</p>
<p id="b299-6">Two lines of cases are relevant to the inquiry: the curtilage doctrine and the “open fields” doctrine. The curtilage area immediately surrounding a private house has long been given protection as a place where the occupants have a reasonable and legitimate expectation of privacy that society is prepared to accept. See <em>Ciraolo, supra.</em></p>
<p id="b299-7">As the curtilage doctrine evolved to protect much the same kind of privacy as that covering the interior of a structure, the contrasting “open fields” doctrine evolved as well. From <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924), to <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984), the Court has drawn a fine as to what expectations are reasonable in the open areas beyond the curtilage of a dwelling: “open fields do not provide the setting for those intimate activities that the [Fourth] Amendment is intended to shelter from governmental interference or surveillance.” <em>Oliver, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#179" aria-description="Citation for case: Oliver v. United States">466 U. S., at 179</a></span>. In <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span>, </em>we held that “an individual may not legitimately demand privacy for activities out of doors in fields, except in the area <page-number citation-index="1" label="236">*236</page-number>immediately surrounding the home.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#178" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 178</a></span>. To fall within the “open fields” doctrine the area “need be neither ‘open’ nor a ‘field’ as those terms are used in common speech.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#180" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 180, n. 11</a></span>.</p>
<p id="b300-5">Dow plainly has a reasonable, legitimate, and objective expectation of privacy within the interior of its covered buildings, and it is equally clear that expectation is one society is prepared to observe. <em>E. g., See </em>v. <em>City of <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">Seattle, supra.</a></span> </em>Moreover, it could hardly be expected that Dow would erect a huge cover over a 2,000-acre tract. In contending that its entire enclosed plant complex is an “industrial curtilage,” Dow argues that its exposed manufacturing facilities are analogous to the curtilage surrounding a home because it has taken every possible step to bar access from ground level.</p>
<p id="b300-6">The Court of Appeals held that whatever the limits of an “industrial curtilage” barring ground-level intrusions into Dow’s private areas, the open areas exposed here were more analogous to “open fields” than to a curtilage for purposes of aerial observation. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#312" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and...">749 F. 2d, at 312-314</a></span>. In <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span>, </em>the Court described the curtilage of a dwelling as “the area to which extends the intimate activity associated with the ‘sanctity of a man’s home and the privacies of life.’” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S., at 180</a></span> (quoting <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886)). See <em>California </em>v. <em>Ciraolo, supra. </em>The intimate activities associated with family privacy and the home and its curtilage simply do not reach the outdoor areas or spaces between structures and buildings of a manufacturing plant.</p>
<p id="b300-7">Admittedly, Dow’s enclosed plant complex, like the area in <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span>, </em>does not fall precisely within the “open fields” doctrine. The area at issue here can perhaps be seen as falling somewhere between “open fields” and curtilage, but lacking some of the critical characteristics of both.<footnotemark>3</footnotemark> Dow’s inner <page-number citation-index="1" label="237">*237</page-number>manufacturing areas are elaborately secured to ensure they are not open or exposed to the public from the ground. Any actual physical entry by EPA into any enclosed area would raise significantly different questions, because “[t]he businessman, like the occupant of a residence, has a constitutional right to go about his business free from unreasonable official entries upon his private commercial property.” <em>See </em>v. <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle"><em>City of Seattle, supra, </em>at 543</a></span>. The narrow issue raised by Dow’s claim of search and seizure, however, concerns aerial observation of a 2,000-acre outdoor manufacturing facility <em>without </em>physical entry.<footnotemark>4</footnotemark></p>
<p id="b301-5">We pointed out in <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#598" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 598-599</a></span> (1981), that the Government has “greater latitude to conduct warrantless inspections of commercial property” because “the expectation of privacy that the owner of commercial property enjoys.in such property differs significantly <page-number citation-index="1" label="238">*238</page-number>from the sanctity accorded an individual’s home.” We emphasized that unlike a homeowner’s interest in his dwelling, “[t]he interest of the owner of commercial property is not one in being free from any inspections.” <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#599" aria-description="Citation for case: Donovan v. Dewey"><em>Id., </em>at 599</a></span>. And with regard to regulatory inspections, we have held that “[w]hat is observable by the public is observable without a warrant, by the Government inspector as well.” <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#315" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 315</a></span> (footnote omitted).</p>
<p id="b302-5"><em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span> </em>recognized that in the open field context, “the public and police lawfully may survey lands from the air.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#179" aria-description="Citation for case: Oliver v. United States">466 U. S., at 179</a></span> (footnote omitted). Here, EPA was not employing some unique sensory device that, for example, could penetrate the walls of buildings and record conversations in Dow’s plants, offices, or laboratories, but rather a conventional, albeit precise, commercial camera commonly used in mapmaking. The Government asserts it has not yet enlarged the photographs to any significant degree, but Dow points out that simple magnification permits identification of objects such as wires as small as inch in diameter.</p>
<p id="b302-6">It may well be, as the Government concedes, that surveillance of private property by using highly sophisticated surveillance equipment not generally available to the public, such as satellite technology, might be constitutionally proscribed absent a warrant. But the photographs here are not so revealing of intimate details as to raise constitutional concerns. Although they undoubtedly give EPA more detailed information than naked-eye views, they remain limited to an outline of the facility’s buildings and equipment. The mere fact that human vision is enhanced somewhat, at least to the degree here, does not give rise to constitutional problems.<footnotemark>5</footnotemark> <page-number citation-index="1" label="239">*239</page-number>An electronic device to penetrate walls or windows so as to hear and record confidential discussions of chemical formulae or other trade secrets would raise very different and far more serious questions; other protections such as trade secret laws are available to protect commercial activities from private surveillance by competitors.<footnotemark>6</footnotemark></p>
<p id="b303-5">We conclude that the open areas of an industrial plant complex with numerous plant structures spread over an area of 2,000 acres are not analogous to the “curtilage” of a dwelling for purposes of aerial surveillance;<footnotemark>7</footnotemark> such an industrial complex is more comparable to an open field and as such it is open to the view and observation of persons in aircraft lawfully in the public airspace immediately above or sufficiently near the area for the reach of cameras.</p>
<p id="b303-6">We hold that the taking of aerial photographs of an industrial plant complex from navigable airspace is not a search prohibited by the Fourth Amendment.</p>
<p id="b303-7">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b296-7"> Section 114(a)(2) provides:</p>
<blockquote id="b296-8">“(2) the Administrator or his authorized representative, upon presentation of his credentials —</blockquote>
<blockquote id="b296-9">“(A) shall have a right of entry to, upon, or through any premises of such person or in which any records required to be maintained under paragraph (1) of this section are located, and</blockquote>
<blockquote id="b296-10">“(B) may at reasonable times have access to and copy any records, inspect any monitoring equipment or method required under paragraph (1), <page-number citation-index="1" label="233">*233</page-number>and sample any emissions which such person is required to sample under paragraph (1).”</blockquote>
</footnote>
<footnote label="2">
<p id="b298-9"> Assuming the Clean Air Act’s explicit provisions for protecting trade secrets obtained by EPA as the result of its investigative efforts is somehow deemed inapplicable to the information obtained here, see <span class="citation no-link">42 U. S. C. § 7414</span>(e), Dow’s fear that EPA might disclose trade secrets revealed in these photographs appears adequately addressed by federal law prohibiting such disclosure generally under the Trade Secrets Act, <span class="citation no-link">18 U. S. C. § 1905</span>, and the Freedom of Information Act, <span class="citation no-link">5 U. S. C. § 552</span>(b)(4). See <em>Chrysler Corp. </em>v. <em>Brown, </em><span class="citation" data-id="9427540"><a href="/opinion/110062/chrysler-corp-v-brown/" aria-description="Citation for case: Chrysler Corp. v. Brown">441 U. S. 281</a></span> (1979).</p>
</footnote>
<footnote label="3">
<p id="b300-8"> In <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span>, </em>we observed that “for most homes, the boundaries of the curtilage will be clearly marked; and the conception defining the curtilage — as the area around the home to which the activity of home life extends — is a familiar one easily understood from our daily experience.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States">466 <page-number citation-index="1" label="237">*237</page-number>U. S., at 182, n. 12</a></span>. While we did not attempt to definitively mark the boundaries of what constitutes an open field, we noted that “[i]t is clear . . . that the term ‘open fields’ may include any unoccupied or undeveloped area outside of the curtilage.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#180" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 180, n. 11</a></span>. As <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span> </em>recognized, the curtilage surrounding a home is generally a well-defined, limited area. In stark contrast, the areas for which Dow claims enhanced protection cover the equivalent of a half dozen family farms.</p>
</footnote>
<footnote label="4">
<p id="b301-9"> We find it important that this is <em>not </em>an area immediately adjacent to a private home, where privacy expectations are most heightened. Nor is this an area where Dow has made any effort to protect against aerial surveillance. Contrary to the partial dissent’s understanding, <em>post, </em>at 241-242, the Court of Appeals emphasized:</p>
<blockquote id="b301-10">“Dow did not take <em>any </em>precautions against aerial intrusions, even though the plant was near an airport and within the pattern of planes landing and taking off. If elaborate and expensive measures for ground security show that Dow has an actual expectation of privacy in ground security, as Dow argues, then taking <em>no </em>measure for aerial security should say something about its actual privacy expectation in being free from aerial observation.” <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#312" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and...">749 F. 2d 307, 312</a></span> (CA6 1984) (emphasis added).</blockquote>
<p id="AS2">Simply keeping track of the identification numbers of any planes flying overhead, with a later followup to see if photographs were taken, does not constitute a “procedur[e] designed to protect the facility from aerial photography.” <em>Post, </em>at 241.</p>
</footnote>
<footnote label="5">
<p id="b302-7"> The partial dissent emphasizes Dow’s claim that under magnification power lines as small as Vz-ineh in diameter can be observed. <em>Post, </em>at 243. But a glance at the photographs in issue shows that those power lines are observable only because of their stark contrast with the snow-white background. No objects as small as 72-inch in diameter such as a class ring, for example, are recognizable, nor are there any identifiable human faces or <page-number citation-index="1" label="239">*239</page-number>secret documents captured in such a fashion as to implicate more serious privacy concerns. Fourth Amendment eases must be decided on the facts of each case, not by extravagant generalizations. “[W]e have never held that potential, as opposed to actual, invasions of privacy constitute searches for purposes of the Fourth Amendment.” <em>United States </em>v. <em>Karo, </em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#712" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 712</a></span> (1984). On these facts, nothing in these photographs suggests that any reasonable expectations of privacy have been infringed.</p>
</footnote>
<footnote label="6">
<p id="b303-13"> The partial dissent relies heavily on Dow’s claim that aerial photography of its facility is proscribed by trade secret laws. <em>Post, </em>at 248-249, and n. 11. While such laws may protect against use of photography by competitors in the same trade to advance their commercial interests, in no manner do “those laws constitute society’s express determination” that <em>all </em>photography of Dow’s facility violates reasonable expectations of privacy. <em>Post, </em>at 249. No trade secret law cited to us by Dow proscribes the use of aerial photography of Dow’s facilities for law enforcement purposes, let alone photography for private purposes unrelated to competition such as map-making or simple amateur snapshots. See <em>swpra, </em>at 232.</p>
</footnote>
<footnote label="7">
<p id="b303-14"> Our holding here does not reach the issues raised by the Court of Appeals for the Seventh Circuit’s holding regarding a “business curtilage” in <em>United States </em>v. <em>Swart, </em><span class="citation" data-id="404175"><a href="/opinion/404175/united-states-v-dale-a-swart/" aria-description="Citation for case: United States v. Dale A. Swart">679 F. 2d 698</a></span> (CA7 1982); that case involved actual physical entry onto the business premises.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Doyle v. Ohio.md  (`case`, 5 assertions)

### content_page

```
---
title: "Doyle v. Ohio"
type: case
citation: "426 U.S. 610 (1976)"
parallel_cite: "96 S. Ct. 2240; 49 L. Ed. 2d 91"
neutral_cite: 1976 U.S. LEXIS 66
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-06-17
docket: 75-5014
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Doyle v. Ohio
  varies_by_point: false
  scope_note: "Good law; cabined to post-Miranda silence (see Jenkins v. Anderson, Fletcher v. Weir, Salinas) but the core Doyle rule is intact."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109491/doyle-v-ohio/"
  cluster_id: 109491
  opinion_id: 109491
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Harris v. New York]]", "[[Miranda v. Arizona]]", "[[Salinas v. Texas]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "miranda", "silence", "impeachment", "due-process"]
holding: "Using a defendant's post-arrest, post-Miranda silence to impeach his exculpatory trial testimony violates the Due Process Clause, because the Miranda warnings carry an implicit assurance that silence will carry no penalty."
lake:
  record_id: Doyle v. Ohio
  status: verified
  projected_at: 2026-07-06
---

# Doyle v. Ohio

*426 U.S. 610 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Doyle and a codefendant were arrested for selling marijuana and given [[Miranda and Custodial Interrogation|Miranda warnings]]. They said nothing at arrest. At trial each testified to an [[Brady and Giglio|exculpatory]] story (that they had been framed). On cross-examination the prosecutor impeached them by asking why, if their story were true, they had not told it to the arresting officer at the time of arrest.

## Issue
Whether a state prosecutor may use a defendant's silence at the time of arrest, after [[Miranda and Custodial Interrogation|Miranda warnings]] were given, to impeach an [[Brady and Giglio|exculpatory]] account the defendant offers for the first time at trial.

## Rule
No. Using post-arrest, post-*[[Miranda v. Arizona|Miranda]]* silence to impeach violates due process. Post-arrest silence following [[Miranda and Custodial Interrogation|Miranda warnings]] is "insolubly ambiguous" because it may be nothing more than the arrestee's exercise of his *[[Miranda v. Arizona|Miranda]]* rights. — 426 U.S. at 617. ^pin-617

"[W]hile it is true that the *Miranda* warnings contain no express assurance that silence will carry no penalty, such assurance is implicit to any person who receives the warnings. In such circumstances, it would be fundamentally unfair and a deprivation of due process to allow the arrested person's silence to be used to impeach an explanation subsequently offered at trial." — *Id.* at 618. ^pin-618

## Application
Doyle and his codefendant were given [[Miranda and Custodial Interrogation|Miranda warnings]] and then stayed silent at arrest. The State used that silence on cross-examination to suggest their trial testimony was a recent fabrication. Because the warnings implicitly assured them that silence carried no penalty, using that silence against them was fundamentally unfair and violated the Fourteenth Amendment's Due Process Clause.

## Conclusion
The impeachment use of post-arrest, post-*[[Miranda v. Arizona|Miranda]]* silence violated due process; the convictions were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Doyle* is cabined to silence after [[Miranda and Custodial Interrogation|Miranda warnings]]: impeachment with **pre-arrest** silence (Jenkins v. Anderson) and with **post-arrest but pre-Miranda** silence (Fletcher v. Weir) does not offend *Doyle*; see also [[Salinas v. Texas]] (pre-custody silence). The core *Doyle* rule remains good law.
- Contrast [[Harris v. New York]]: a voluntary statement taken in violation of Miranda may impeach, but *Doyle* bars impeachment by the silence itself.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Doyle v. Ohio*, 426 U.S. 610 (1976) — https://www.courtlistener.com/opinion/109491/doyle-v-ohio/ — pinpoints: 617, 618.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c3796cfe2813e711", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "426 U.S. 610 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 66", "official_citation_present": true, "parallel_cite": "96 S. Ct. 2240; 49 L. Ed. 2d 91", "title": "Doyle v. Ohio", "year": "1976"}}
{"assertion_id": "5fdf8099723fcff6", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny", "title": "Doyle v. Ohio"}}
{"assertion_id": "74a1ba1ac1656ed0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Using a defendant's post-arrest, post-Miranda silence to impeach his exculpatory trial testimony violates the Due Process Clause, because the Miranda warnings carry an implicit assurance that silence will carry no penalty.", "title": "Doyle v. Ohio"}}
{"assertion_id": "244ed81b9e77efd2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-06-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Doyle v. Ohio", "field_i_validity": "good_law", "scope_note": "Good law; cabined to post-Miranda silence (see Jenkins v. Anderson, Fletcher v. Weir, Salinas) but the core Doyle rule is intact.", "title": "Doyle v. Ohio", "varies_by_point": "false"}}
{"assertion_id": "a8a9da88e0e44fde", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Doyle v. Ohio"}}
```

### lake record — Doyle v. Ohio

```json
{
  "schema_version": "s2.v1",
  "record_id": "Doyle v. Ohio",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Doyle v. Ohio",
    "case_name_short": "Doyle",
    "case_name_full": "Doyle v. Ohio",
    "input_case_name": "Doyle v. Ohio",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-06-17",
    "year": 1976,
    "docket": "75-5014",
    "cluster_id": 109491,
    "lead_opinion_id": 109491,
    "sibling_ids": [
      109491,
      9426459,
      9426460
    ],
    "absolute_url": "/opinion/109491/doyle-v-ohio/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "426 U.S. 610",
      "volume": "426",
      "reporter": "U.S.",
      "page": "610",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 2240",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2240",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 91",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "91",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 66",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "426 U.S. 610",
        "volume": "426",
        "reporter": "U.S.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 2240",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2240",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 91",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "91",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 66",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "426 U.S. 610",
    "official_selection": {
      "court_class": "scotus",
      "selected": "426 U.S. 610",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-617",
      "page": null,
      "quote": "--- # Doyle v. Ohio *426 U.S. 610 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Doyle and a codefendant were arrested for selling marijuana and given Miranda warnings. They said nothing at arrest. At trial each testified to an exculpatory story (that they had been framed). On cross-examination the prosecutor impeached them by asking why, if their story were true, they had not told it to the arresting officer at the time of arrest. ## Issue Whether a state prosecutor may use a defendant's silence at the time of arrest, after Miranda warnings were given, to impeach an exculpatory account the defendant offers for the first time at trial. ## Rule No. Using post-arrest, post-*Miranda* silence to impeach violates due process. Post-arrest silence following Miranda warnings is",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-618",
      "page": null,
      "quote": "[W]hile it is true that the *Miranda* warnings contain no express assurance that silence will carry no penalty, such assurance is implicit to any person who receives the warnings. In such circumstances, it would be fundamentally unfair and a deprivation of due process to allow the arrested person's silence to be used to impeach an explanation subsequently offered at trial.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Doyle v. Ohio",
    "varies_by_point": false,
    "scope_note": "Good law; cabined to post-Miranda silence (see Jenkins v. Anderson, Fletcher v. Weir, Salinas) but the core Doyle rule is intact.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. Sharrieff M. Kent",
          "cluster_id": 9487155,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Morris",
          "cluster_id": 9415465,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tappia Green",
          "cluster_id": 9409950,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Rivera",
          "cluster_id": 4743993,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sesmas",
          "cluster_id": 4735753,
          "cite": [
            "459 P.3d 1265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Orr",
          "cluster_id": 10367163,
          "cite": [
            "305 Ga. 729"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Randle",
          "cluster_id": 4523033,
          "cite": [
            "2018 SD 61",
            "916 N.W.2d 461"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brecht v. Abrahamson",
          "cluster_id": 112845,
          "cite": [
            "123 L. Ed. 2d 353",
            "113 S. Ct. 1710",
            "507 U.S. 619",
            "1993 U.S. LEXIS 2981"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": [
            "89 L. Ed. 2d 410",
            "106 S. Ct. 1135",
            "475 U.S. 412",
            "1986 U.S. LEXIS 32",
            "54 U.S.L.W. 4265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson v. United States",
          "cluster_id": 118380,
          "cite": [
            "147 L. Ed. 2d 405",
            "120 S. Ct. 2326",
            "530 U.S. 428",
            "2000 U.S. LEXIS 4305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dinkins v. State",
          "cluster_id": 1688238,
          "cite": [
            "894 S.W.2d 330",
            "1995 Tex. Crim. App. LEXIS 9",
            "1995 WL 40331"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Anderson",
          "cluster_id": 110298,
          "cite": [
            "65 L. Ed. 2d 86",
            "100 S. Ct. 2124",
            "447 U.S. 231",
            "1980 U.S. LEXIS 131"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Neville",
          "cluster_id": 110832,
          "cite": [
            "74 L. Ed. 2d 748",
            "103 S. Ct. 916",
            "459 U.S. 553",
            "1983 U.S. LEXIS 129",
            "51 U.S.L.W. 4148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Greer v. Miller",
          "cluster_id": 111956,
          "cite": [
            "97 L. Ed. 2d 618",
            "107 S. Ct. 3102",
            "483 U.S. 756",
            "1987 U.S. LEXIS 2930"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Orange Jell Beechum",
          "cluster_id": 358983,
          "cite": [
            "582 F.2d 898",
            "1978 U.S. App. LEXIS 8198",
            "3 Fed. R. Serv. 1185"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Osband",
          "cluster_id": 5607850,
          "cite": [
            "13 Cal. 4th 622",
            "919 P.2d 640",
            "96 Daily Journal DAR 9137",
            "96 Cal. Daily Op. Serv. 5583",
            "55 Cal. Rptr. 2d 26",
            "1996 Cal. LEXIS 3814"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Charles",
          "cluster_id": 110306,
          "cite": [
            "65 L. Ed. 2d 222",
            "100 S. Ct. 2180",
            "447 U.S. 404",
            "1980 U.S. LEXIS 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coffman",
          "cluster_id": 2623595,
          "cite": [
            "96 P.3d 30",
            "17 Cal. Rptr. 3d 710",
            "34 Cal. 4th 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 844247,
          "cite": [
            "52 Cal. 4th 856",
            "261 P.3d 243",
            "131 Cal. Rptr. 3d 225",
            "2011 Cal. LEXIS 8769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Greenfield",
          "cluster_id": 111553,
          "cite": [
            "88 L. Ed. 2d 623",
            "106 S. Ct. 634",
            "474 U.S. 284",
            "1986 U.S. LEXIS 41",
            "54 U.S.L.W. 4077"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fletcher v. Weir",
          "cluster_id": 110668,
          "cite": [
            "71 L. Ed. 2d 490",
            "102 S. Ct. 1309",
            "455 U.S. 603",
            "1982 U.S. LEXIS 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roberts v. United States",
          "cluster_id": 110234,
          "cite": [
            "63 L. Ed. 2d 622",
            "100 S. Ct. 1358",
            "445 U.S. 552",
            "1980 U.S. LEXIS 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Crittenden",
          "cluster_id": 2614001,
          "cite": [
            "885 P.2d 887",
            "9 Cal. 4th 83",
            "36 Cal. Rptr. 2d 474",
            "94 Daily Journal DAR 18013",
            "94 Cal. Daily Op. Serv. 9702",
            "1994 Cal. LEXIS 6570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
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
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duckworth v. Eagan",
          "cluster_id": 112322,
          "cite": [
            "106 L. Ed. 2d 166",
            "109 S. Ct. 2875",
            "492 U.S. 195",
            "1989 U.S. LEXIS 3196",
            "57 U.S.L.W. 4942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marvin Baker",
          "cluster_id": 77176,
          "cite": [
            "432 F.3d 1189",
            "2005 WL 3369204"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Antwine",
          "cluster_id": 2364064,
          "cite": [
            "743 S.W.2d 51",
            "1987 Mo. LEXIS 374",
            "1987 WL 2721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Rundle",
          "cluster_id": 2633881,
          "cite": [
            "180 P.3d 224",
            "74 Cal. Rptr. 3d 454",
            "43 Cal. 4th 76",
            "2008 Cal. LEXIS 3795"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Monroe",
          "cluster_id": 4764609,
          "cite": [
            "468 P.3d 1273",
            "2020 CO 67"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heidelberg v. State",
          "cluster_id": 2120437,
          "cite": [
            "144 S.W.3d 535",
            "2004 Tex. Crim. App. LEXIS 1479",
            "2004 WL 2109065"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Glasper",
          "cluster_id": 2027353,
          "cite": [
            "917 N.E.2d 401",
            "234 Ill. 2d 173",
            "334 Ill. Dec. 575",
            "2009 Ill. LEXIS 933"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109491 OR 9426459 OR 9426460) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMyMDQ0ODAwMDAwJnM9NDUxOTA2MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109491+OR+9426459+OR+9426460%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(109491 OR 9426459 OR 9426460)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMzkmcz0yODQ1OCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109491+OR+9426459+OR+9426460%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109491 OR 9426459 OR 9426460)",
        "reviewed": 64,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 64,
        "triage_read": 2,
        "triage_snippet_classified": 62
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109491 OR 9426459 OR 9426460)",
    "indexed_citing_opinions": 2961,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109491,
        "count": 2633,
        "count_source": "search"
      },
      {
        "opinion_id": 9426459,
        "count": 386,
        "count_source": "search"
      },
      {
        "opinion_id": 9426460,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4773,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/doyle-v-ohio.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyMjQ2MjUmcz0xMDMzNjQxOCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109491+OR+9426459+OR+9426460%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109491,
        "cited_id": 95301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 100906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 103779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 105508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 105661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 105925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 106219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 109101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 109289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 279002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 323043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 2499246,
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
    "date_created": "2026-07-05T02:48:28Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:48:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:48:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:53:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:48:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Doyle v. Ohio

```
<div>
<center><b><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">426 U.S. 610</a></span> (1976)</b></center>
<center><h1>DOYLE<br>
v.<br>
OHIO.</h1></center>
<center>No. 75-5014.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 23, 1976.</center>
<center>Decided June 17, 1976.<sup>[*]</sup></center>
CERTIORARI TO THE COURT OF APPEALS OF OHIO, TUSCARAWAS COUNTY.
<p><i>James R. Willis</i> argued the cause for petitioners and filed briefs in both cases.</p>
<p><i>Ronald L. Collins</i> argued the cause <i>pro hac vice</i> and filed a brief for respondent in both cases.<sup>[]</sup></p>
<p><span class="star-pagination">*611</span> MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>The question in these consolidated cases is whether a state prosecutor may seek to impeach a defendant's exculpatory story, told for the first time at trial, by cross-examining the defendant about his failure to have told the story after receiving <i>Miranda</i> warnings<sup>[1]</sup> at the time of his arrest. We conclude that use of the defendant's post-arrest silence in this manner violates due process, and therefore reverse the convictions of both petitioners.</p>
<p></p>
<h2>I</h2>
<p>Petitioners Doyle and Wood were arrested together and charged with selling 10 pounds of marihuana to a local narcotics bureau informant. They were convicted in the Common Pleas Court of Tuscarawas County, Ohio, in separate trials held about one week apart. The evidence at their trials was identical in all material respects.</p>
<p>The State's witnesses sketched a picture of a routine marihuana transaction. William Bonnell, a well-known "street person" with a long criminal record, offered to assist the local narcotics investigation unit in setting up drug "pushers" in return for support in his efforts to receive lenient treatment in his latest legal problems. The narcotics agents agreed. A short time later, Bonnell advised the unit that he had arranged a "buy" of 10 pounds of marihuana and needed $1,750 to pay for it. Since the banks were closed and time was short, the agents were able to collect only $1,320. Bonnell took this money and left for the rendezvous, under surveillance by four narcotics agents in two cars. As planned, he met petitioners in a bar in Dover, Ohio. From there, he and petitioner Wood drove in Bonnell's <span class="star-pagination">*612</span> pickup truck to the nearby town of New Philadelphia, Ohio, while petitioner Doyle drove off to obtain the marihuana and then meet them at a prearranged location in New Philadelphia. The narcotics agents followed the Bonnell truck. When Doyle arrived at Bonnell's waiting truck in New Philadelphia, the two vehicles proceeded to a parking lot where the transaction took place. Bonnell left in his truck, and Doyle and Wood departed in Doyle's car. They quickly discovered that they had been paid $430 less than the agreed-upon price, and began circling the neighborhood looking for Bonnell. They were stopped within minutes by New Philadelphia police acting on radioed instructions from the narcotics agents. One of those agents, Kenneth Beamer, arrived on the scene promptly, arrested petitioners, and gave them <i>Miranda</i> warnings. A search of the car, authorized by warrant, uncovered the $1,320.</p>
<p>At both trials, defense counsel's cross-examination of the participating narcotics agents was aimed primarily at establishing that, due to a limited view of the parking lot, none of them had seen the actual transaction but had seen only Bonnell standing next to Doyle's car with a package under his arm, presumably after the transaction.<sup>[2]</sup> Each petitioner took the stand at his trial and admitted practically everything about the State's case except the most crucial point: who was <span class="star-pagination">*613</span> selling marihuana to whom. According to petitioners, Bonnell had framed them. The arrangement had been for Bonnell to sell Doyle 10 pounds of marihuana. Doyle had left the Dover bar for the purpose of borrowing the necessary money, but while driving by himself had decided that he only wanted one or two pounds instead of the agreed-upon 10 pounds. When Bonnell reached Doyle's car in the New Philadelphia parking lot, with the marihuana under his arm, Doyle tried to explain his change of mind. Bonnell grew angry, threw the $1,320 into Doyle's car, and took all 10 pounds of the marihuana back to his truck. The ensuing chase was the effort of Wood and Doyle to catch Bonnell to find out what the $1,320 was all about.</p>
<p>Petitioners' explanation of the events presented some difficulty for the prosecution, as it was not entirely implausible and there was little if any direct evidence to contradict it.<sup>[3]</sup> As part of a wide-ranging cross-examination for impeachment purposes, and in an effort to undercut the explanation, the prosecutor asked each petitioner at his respective trial why he had not told the frameup story to Agent Beamer when he arrested petitioners. In the first trial, that of petitioner Wood, the following colloquy occurred:<sup>[4]</sup></p>
<blockquote>"Q. [By the prosecutor.] Mr. Beamer did arrive on the scene?</blockquote>
<blockquote>"A. [By Wood.] Yes, he did.</blockquote>
<blockquote>"Q. And I assume you told him all about what happened to you?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. No.</blockquote>
<blockquote>
<span class="star-pagination">*614</span> "Q. You didn't tell Mr. Beamer?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. No.</blockquote>
<blockquote>"Q. You didn't tell Mr. Beamer this guy put $1,300 in your car?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. No, sir.</blockquote>
<blockquote>"Q. And we can't understand any reason why anyone would put money in your car and you were chasing him around town and trying to give it back?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. I didn't understand that.</blockquote>
<blockquote>"Q. You mean you didn't tell him that?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. Tell him what?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Mr. Wood, if that is all you had to do with this and you are innocent, when Mr. Beamer arrived on the scene why didn't you tell him?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. But in any event you didn't bother to tell Mr. Beamer anything about this?</blockquote>
<blockquote>"A. No, sir."</blockquote>
<p>Defense counsel's timely objections to the above questions of the prosecutor were overruled. The cross-examination of petitioner Doyle at his trial contained a similar exchange, and again defense counsel's timely objections were overruled.<sup>[5]</sup></p>
<p><span class="star-pagination">*615</span> Each petitioner appealed to the Court of Appeals, Fifth District, Tuscarawas County, alleging, <i>inter alia,</i> that the trial court erred in allowing the prosecutor to cross-examine the petitioner at his trial about his post-arrest silence. The Court of Appeals affirmed the convictions, stating as to the contentions about the post-arrest silence:</p>
<blockquote>"This was not evidence offered by the state in its case in chief as confession by silence or as substantive evidence of guilt but rather cross examination <span class="star-pagination">*616</span> of a witness as to why he had not told the same story earlier at his first opportunity.</blockquote>
<blockquote>"We find no error in this. It goes to credibility of the witness."</blockquote>
<p>The Supreme Court of Ohio denied further review. We granted certiorari to decide whether impeachment use of a defendant's post-arrest silence violates any provision of the Constitution,<sup>[6]</sup> a question left open last Term in <i>United States</i> v. <i>Hale,</i> <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">422 U. S. 171</a></span> (1975), and on which the Federal Courts of Appeals are in conflict. See <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">id.,</a></span></i> at 173 n. 2.</p>
<p></p>
<h2>II</h2>
<p>The State pleads necessity as justification for the prosecutor's action in these cases. It argues that the discrepancy between an exculpatory story at trial and silence at time of arrest gives rise to an inference that the story was fabricated somewhere along the way, perhaps to fit within the seams of the State's case as it was developed at pretrial hearings. Noting that the prosecution usually has little else with which to counter such an exculpatory story, the State seeks only the right to cross-examine a defendant as to post-arrest silence for the limited purpose of impeachment. In support of its position the State emphasizes the importance of cross-examination <span class="star-pagination">*617</span> in general, see <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="9421572"><a href="/opinion/105661/brown-v-united-states/#154" aria-description="Citation for case: Brown v. United States">356 U. S. 148, 154-155</a></span> (1958), and relies upon those cases in which this Court has permitted use for impeachment purposes of post-arrest statements that were inadmissible as evidence of guilt because of an officer's failure to follow <i>Miranda</i>'s dictates. <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971); <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975); see also <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954). Thus, although the State does not suggest petitioners' silence could be used as evidence of guilt, it contends that the need to present to the jury all information relevant to the truth of petitioners' exculpatory story fully justifies the cross-examination that is at issue.</p>
<p>Despite the importance of cross-examination,<sup>[7]</sup> we have concluded that the <i>Miranda</i> decision compels rejection of the State's position. The warnings mandated by that case, as a prophylactic means of safeguarding Fifth Amendment rights, see <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#443" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 443-444</a></span> (1974), require that a person taken into custody be advised immediately that he has the right to remain silent, that anything he says may be used against him, and that he has a right to retained or appointed counsel before submitting to interrogation. Silence in the wake of these warnings may be nothing more than the arrestee's exercise of these <i>Miranda</i> rights. Thus, every post-arrest silence is insolubly ambiguous because of what the State is required to advise the person arrested.<sup>[8]</sup> See <i>United States</i> v. <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale, supra,</a></span></i> <span class="star-pagination">*618</span> at 177. Moreover, while it is true that the <i>Miranda</i> warnings contain no express assurance that silence will carry no penalty, such assurance is implicit to any person who receives the warnings. In such circumstances, it would be fundamentally unfair and a deprivation of due process to allow the arrested person's silence to be used to impeach an explanation subsequently offered at trial.<sup>[9]</sup></p>
<p><span class="star-pagination">*619</span> MR. JUSTICE WHITE, concurring in the judgment in <i>United States</i> v. <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/#182" aria-description="Citation for case: United States v. Hale"><i>Hale, supra,</i> at 182-183</a></span>, put it very well:</p>
<blockquote>"[W]hen a person under arrest is informed, as <i>Miranda</i> requires, that he may remain silent, that anything he says may be used against him, and that he may have an attorney if he wishes, it seems to me that it does not comport with due process to permit the prosecution during the trial to call attention to his silence at the time of arrest and to insist that because he did not speak about the facts of the case at that time, as he was told he need not do, an unfavorable inference might be drawn as to the truth of his trial testimony. . . . Surely Hale was not informed here that his silence, as well as his words, could be used against him at trial. Indeed, anyone would reasonably conclude from <i>Miranda</i> warnings that this would not be the case."<sup>[10]</sup></blockquote>
<p>We hold that the use for impeachment purposes of petitioners' silence, at the time of arrest and after receiving <i>Miranda</i> warnings, violated the Due Process Clause of the Fourteenth Amendment.<sup>[11]</sup> The State has not <span class="star-pagination">*620</span> claimed that such use in the circumstances of this case might have been harmless error. Accordingly, petitioners' convictions are reversed and their causes remanded to the state courts for further proceedings not inconsistent with this opinion.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE STEVENS, with whom MR. JUSTICE BLACKMUN and MR. JUSTICE REHNQUIST join, dissenting.</p>
<p>Petitioners assert that the prosecutor's cross-examination about their failure to mention the purported "frame" until they testified at trial violated their constitutional right to due process and also their constitutional privilege against self-incrimination. I am not persuaded by the first argument; though there is merit in a portion of the second, I do not believe it warrants reversal of these state convictions.</p>
<p></p>
<h2>I</h2>
<p>The Court's due process rationale has some of the characteristics of an estoppel theory. If (a) the defendant is advised that he may remain silent, and (b) he does remain silent, then we (c) presume that his decision was made in reliance on the advice, and (d) conclude that it is unfair in certain cases, though not others,<sup>[1]</sup> to use his silence to impeach his trial testimony. The key to the Court's analysis is apparently a concern that the <i>Miranda</i> warning, which is intended to increase the probability <span class="star-pagination">*621</span> that a person's response to police questioning will be intelligent and voluntary, will actually be deceptive unless we require the State to honor an unstated promise not to use the accused's silence against him.</p>
<p>In my judgment there is nothing deceptive or prejudicial to the defendant in the <i>Miranda</i> warning.<sup>[2]</sup> Nor do I believe that the fact that such advice was given to the defendant lessens the probative value of his silence, or makes the prosecutor's cross-examination about his silence any more unfair than if he had received no such warning.</p>
<p>This is a case in which the defendants' silence at the time of their arrest was graphically inconsistent with their trial testimony that they were the unwitting victims of a "frameup" in which the police did not participate. If defendants had been framed, their failure to mention that fact at the time of their arrest is almost <span class="star-pagination">*622</span> inexplicable; for that reason, under accepted rules of evidence, their silence is tantamount to a prior inconsistent statement and admissible for purposes of impeachment.<sup>[3]</sup></p>
<p>Indeed, there is irony in the fact that the <i>Miranda</i> warning provides the only plausible explanation for their silence. If it were the true explanation, I should think that they would have responded to the questions on cross-examination about why they had remained silent by stating that they relied on their understanding of the advice given by the arresting officers. Instead, however, they gave quite a different jumble of responses.<sup>[4]</sup> Those <span class="star-pagination">*623</span> responses negate the Court's presumption that their silence was induced by reliance on deceptive advice.</p>
<p>Since the record requires us to put to one side the <span class="star-pagination">*624</span> Court's presumption that the defendants' silence was the product of reliance on the <i>Miranda</i> warning, the Court's entire due process rationale collapses. For without reliance <span class="star-pagination">*625</span> on the waiver, the case is no different than if no warning had been given, and nothing in the Court's opinion suggests that there would be any unfairness in <span class="star-pagination">*626</span> using petitioners' prior inconsistent silence for impeachment purposes in such a case.</p>
<p>Indeed, as a general proposition, if we assume the defendant's silence would be admissible for impeachment purposes if no <i>Miranda</i> warning had been given, I should think that the warning would have a tendency to salvage the defendant's credibility as a witness. If the defendant is a truthful witness, and if his silence is the consequence of his understanding of the <i>Miranda</i> warning, he may explain that fact when he is on the stand. Even if he is untruthful, the availability of that explanation puts him in a better position than if he had received no warning. In may judgment, the risk that a truthful defendant will be deceived by the <i>Miranda</i> warning and also will be unable to explain his honest misunderstanding is so much less than the risk that exclusion of the evidence will merely provide a shield for perjury that I cannot accept the Court's due process rationale.</p>
<p>Accordingly, if we assume that the use of a defendant's silence for impeachment purposes would be otherwise unobjectionable, I find no merit in the notion that he is denied due process of law because he received a <i>Miranda</i> warning.</p>
<p></p>
<h2>II</h2>
<p>Petitioners argue that the State violated their Fifth Amendment privilege against self-incrimination by asking the jury to draw an inference of guilt from their constitutionally protected silence. They challenge both the prosecutor's cross-examination and his closing argument.</p>
<p></p>
<h2>A</h2>
<p>Petitioners claim that the cross-examination was improper because it referred to their silence at the time of <span class="star-pagination">*627</span> their arrest, to their failure to testify at the preliminary hearing, and to their failure to reveal the "frame" prior to trial. Their claim applies to the testimony of each defendant at his own trial, and also to the testimony each gave as a witness at the trial of the other. Since I think it quite clear that a defendant may not object to the violation of another person's privilege,<sup>[5]</sup> I shall only discuss the argument that a defendant may not be cross-examined about his own prior inconsistent silence.</p>
<p>In support of their objections to the cross-examination about their silence at the time of arrest, petitioners primarily rely on the statement in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, that the prosecution may not use at trial the fact that the defendant stood mute or claimed the privilege in the face of accusations during custodial interrogation.<sup>[6]</sup> There are two reasons why that statement does not adequately support petitioners' argument.</p>
<p>First, it is not accurate to say that the petitioners "stood mute or claimed the privilege in the face of accusations." Neither petitioner claimed the privilege and <span class="star-pagination">*628</span> petitioner Doyle did not even remain silent.<sup>[7]</sup> The case is not one in which a description of the actual conversation between the defendants and the police would give rise to any inference of guilt if it were not so flagrantly inconsistent with their trial testimony. Rather than a claim of privilege, we simply have a failure to advise the police of a "frame" at a time when it most surely would have been mentioned if petitioners' trial testimony were true. That failure gave rise to an inference of guilt only because it belied their trial testimony.</p>
<p>Second, the dictum in the footnote in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> relies primarily upon <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span>, which held that the Fifth Amendment, as incorporated in the Fourteenth, prohibited the prosecution's use of the defendant's silence in its case in chief. But as long ago as <i>Raffel</i> v. <i>United States,</i> <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">271 U. S. 494</a></span>, this Court recognized the distinction between the prosecution's affirmative use of the defendant's prior silence and the use of prior silence for impeachment purposes. <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> expressly held that the defendant's silence at a prior trial was admissible for purposes of impeachment despite the application in federal prosecutions of the prohibition that <i><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span></i> found in the Fifth Amendment. <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/#496" aria-description="Citation for case: Raffel v. United States"><i>Raffel, supra,</i> at 496-497</a></span>.</p>
<p>Moreover, Mr. Chief Justice Warren, the author of the Court's opinion in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> joined the opinion in <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span>, which squarely held that a valid constitutional objection to the admissibility of evidence as part of the Government's case in chief did not bar the use of that evidence to impeach the defendant's trial testimony. The availability of an objection to the affirmative use of improper evidence does not provide the defendant "with a shield against contradiction of his untruths." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States"><i>Id.,</i> at 65</a></span>. The need to ensure the integrity <span class="star-pagination">*629</span> of the truth-determining function of the adversary trial process has provided the predicate for an unbroken line of decisions so holding.<sup>[8]</sup></p>
<p><span class="star-pagination">*630</span> Although I have no doubt concerning the propriety of the cross-examination about petitioners' failure to mention the purported "frame" at the time of their arrest, a more difficult question is presented by their objection to the questioning about their failure to testify at the preliminary hearing and their failure generally to mention the "frame" before trial.<sup>[9]</sup> Unlike the failure <span class="star-pagination">*631</span> to make the kind of spontaneous comment that discovery of a "frame" would be expected to prompt, there is no significant inconsistency between petitioners' trial testimony <span class="star-pagination">*632</span> and their adherence to counsel's advice not to take the stand at the preliminary hearing; moreover, the decision not to divulge their defense prior to trial is probably attributable to counsel rather than to petitioners.<sup>[10]</sup> Nevertheless, unless and until this Court overrules <i>Raffel</i> v. <i>United States,</i> <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">271 U. S. 494</a></span>,<sup>[11]</sup> I think a state court is <span class="star-pagination">*633</span> free to regard the defendant's decision to take the stand as a waiver of his objection to the use of his failure to testify at an earlier proceeding or his failure to offer his version of the events prior to trial.</p>
<p></p>
<h2>B</h2>
<p>In my judgment portions of the prosecutor's argument to the jury overstepped permissible bounds. In each trial, he commented upon the defendant's silence not only as inconsistent with his testimony that he had been "framed," <span class="star-pagination">*634</span> but also as inconsistent with the defendant's innocence.<sup>[12]</sup> Comment on the lack of credibility of the defendant is plainly proper; it is not proper, however, for the prosecutor <span class="star-pagination">*635</span> to ask the jury to draw a direct inference of guilt from silenceto argue, in effect, that silence is inconsistent with innocence. But since the two inferencesperjury <span class="star-pagination">*636</span> and guiltare inextricably intertwined because they have a common source, it would be unrealistic to permit comment on the former but to find reversible error in the slightest reference to the latter. In the context of the entire argument and the entire trial, I am not persuaded that the rather sophisticated distinction between permissible comment on credibility and impermissible comment on an inference of guilt justifies a reversal of these state convictions.<sup>[13]</sup></p>
<p>Accordingly, although I have some doubt concerning the propriety of the cross-examination about the preliminary hearing and consider a portion of the closing argument improper, I would affirm these convictions.</p>
<h2>NOTES</h2>
<p>[*]  Together with No. 75-5015, <i>Wood</i> v. <i>Ohio,</i> also on certiorari to the same court.</p>
<p>[]  <i>Solicitor General Bork</i> filed a brief for the United States as <i>amicus curiae.</i></p>
<p>[1]  <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467-473</a></span> (1966).</p>
<p>[2]  Defense counsel's efforts were not totally successful. One of the four narcotics agents testified at both trials that he had seen the package passed through the window of Doyle's car to Bonnell. In an effort to impeach that testimony, defense counsel played a tape of the preliminary hearing at which the same agent had testified only to seeing the package under Bonnell's arm. The agent did not retract his trial testimony, and both he and the prosecutor explained the apparent inconsistency by noting that the examination at the preliminary hearing had not focused upon whether anyone had seen the package pass to Bonnell.</p>
<p>[3]  See n. 2. <i>supra.</i></p>
<p>[4]  Trial transcript in <i>Ohio</i> v. <i>Wood.</i> No. 10657. Common Pleas Court, Tuscarawas County, Ohio (hereafter Wood Tr.), 465-470.</p>
<p>[5]  Trial transcript in <i>Ohio</i> v. <i>Doyle,</i> No. 10656, Common Pleas Court, Tuscarawas County, Ohio (hereafter Doyle Tr.), 504-507:
</p>
<p>"Q. [By the prosecutor.] . . . You are innocent?</p>
<p>"A. [By Doyle.] I am innocent. Yes Sir.</p>
<p>"Q. That's why you told the police department and Kenneth Beamer when they arrived</p>
<p>.....</p>
<p>"(Continuing.)about your innocence?</p>
<p>.....</p>
<p>"A. . . . I didn't tell them about my innocence. No.</p>
<p>"Q. You said nothing at all about how you had been set up?</p>
<p>.....</p>
<p>"Q. Did Mr. Wood?</p>
<p>"A. Not that I recall, Sir.</p>
<p>.....</p>
<p>"Q. As a matter of fact, if I recall your testimony correctly, you said instead of protesting your innocence, as you do today, you said in response to a question of Mr. Beamer,`I don't know what you are talking about.'</p>
<p>"A. I believe what I said,`What's this all about?' If I remember, that's the only thing I said.</p>
<p>.....</p>
<p>"A. I was questioning, you know, what it was about. That's what I didn't know. I knew that I was trying to buy, which was wrong, but I didn't know what was going on. I didn't know that Bill Bonnell was trying to frame me, or what-have-you.</p>
<p>.....</p>
<p>"Q. All right,But you didn't protest your innocence at that time?</p>
<p>.....</p>
<p>"A. Not until I knew what was going on."</p>
<p>In addition, the court in both trials permitted the prosecutor, over more objections, to argue petitioners' post-arrest silence to the jury. Closing Argument of Prosecutor 13-14, supplementing Wood Tr.; Doyle Tr. 515, 526.</p>
<p>[6]  Petitioners also claim constitutional error because each of them was cross-examined by the prosecutor as to why he had not told the exculpatory story at the preliminary hearing or any other time prior to the trials. In addition, error of constitutional dimension is asserted because each petitioner was cross-examined as to post-arrest, preliminary hearing, and general pretrial silence when he testified as a <i>defense witness</i> at the other petitioner's trial. These averments of error present different considerations from those implicated by cross-examining petitioners as defendants as to their silence after receiving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings at the time of arrest. In view of our disposition of this case we find it unnecessary to reach these additional issues.</p>
<p>[7]  We recognize, of course, that unless prosecutors are allowed wide leeway in the scope of impeachment cross-examination some defendants would be able to frustrate the truth-seeking function of a trial by presenting tailored defenses insulated from effective challenge. See generally <i>Fitzpatrick</i> v. <i>United States,</i> <span class="citation" data-id="95301"><a href="/opinion/95301/fitzpatrick-v-united-states/#315" aria-description="Citation for case: Fitzpatrick v. United States">178 U. S. 304, 315</a></span> (1900).</p>
<p>[8]  The dissent by MR. JUSTICE STEVENS expresses the view that the giving of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings does not lessen the "probative value of [a defendant's] silence . . . ." <i>Post,</i> at 621. But in <i>United States</i> v. <i>Hale,</i> <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/#177" aria-description="Citation for case: United States v. Hale">422 U. S. 171, 177</a></span> (1975), we noted that silence at the time of arrest may be inherently ambiguous even apart from the effect of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, for in a given case there may be several explanations for the silence that are consistent with the existence of an exculpatory explanation. In <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale</a></span></i> we exercised our supervisory powers over federal courts. The instant cases, unlike <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale</a></span>,</i> come to us from a state court and thus provide no occasion for the exercise of our supervisory powers. Nor is it necessary, in view of our holding above, to express an opinion on the probative value for impeachment purposes of petitioners' silence. We note only that the <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale</a></span></i> court considered silence at the time of arrest likely to be ambiguous and thus of dubious probative value.</p>
<p>[9]  A somewhat analogous situation was presented in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">318 U. S. 189</a></span> (1943). A defendant who testified at his trial was permitted by the trial judge to invoke the Fifth Amendment privilege against self-incrimination in response to certain questions on cross-examination. This Court assumed that it would not have been error for the trial court to have denied the privilege in the circumstances, see <span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/#196" aria-description="Citation for case: Johnson v. United States"><i>id.,</i> at 196</a></span>, in which case a failure to answer would have been a proper basis for adverse inferences and a proper subject for prosecutorial comment. But because the privilege had been granted, even if erroneously, "the requirements of fair trial" made it error for the trial court to permit comment upon the defendant's silence. <i><span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Ibid.</a></span></i>
</p>
<p>"An accused having the assurance of the court that his claim of privilege would be granted might well be entrapped if his assertion of the privilege could then be used against him. His real choice might then be quite different from his apparent one. . . . Elementary fairness requires that an accused should not be misled on that score." <span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/#197" aria-description="Citation for case: Johnson v. United States"><i>Id.,</i> at 197</a></span>.</p>
<p><i>Johnson</i> was decided under this Court's supervisory powers over the federal courts. But the necessity for elementary fairness is not unique to the federal criminal system. Cf. <i>Raley</i> v. <i>Ohio,</i> <span class="citation" data-id="105925"><a href="/opinion/105925/raley-v-ohio/#437" aria-description="Citation for case: Raley v. Ohio">360 U. S. 423, 437-440</a></span> (1959).</p>
<p>[10]  The dissenting opinion relies on the fact that petitioners in this case, when cross-examined about their silence, did not offer reliance on <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings as a justification. But the error we perceive lies in the cross-examination on this question, thereby implying an inconsistency that the jury might construe as evidence of guilt. After an arrested person is formally advised by an officer of the law that he has a right to remain silent, the unfairness occurs when the prosecution, in the presence of the jury, is allowed to undertake impeachment on the basis of what may be the exercise of that right.</p>
<p>[11]  It goes almost without saying that the fact of post-arrest silence could be used by the prosecution to contradict a defendant who testifies to an exculpatory version of events and claims to have told the police the same version upon arrest. In that situation the fact of earlier silence would not be used to impeach the exculpatory story, but rather to challenge the defendant's testimony as to his behavior following arrest. Cf. <i>United States</i> v. <i>Fairchild,</i> <span class="citation" data-id="323043"><a href="/opinion/323043/united-states-v-alton-r-fairchild/#1383" aria-description="Citation for case: United States v. Alton R. Fairchild">505 F. 2d 1378, 1383</a></span> (CA5 1975).</p>
<p>[1]  As the Court acknowledges, the "fact of post-arrest silence could be used by the prosecution to contradict a defendant who testifies to an exculpatory version of events and claims to have told the police the same version upon arrest." <i>Ante,</i> at 619 and this page, n. 11.</p>
<p>[2]  At Wood's trial, the arresting officer described the warning he gave petitioners:
</p>
<p>"I told Mr. Wood and Mr. Doyle of the Miranda warning rights they had the right to remain silent, anything they said could and would be used against them in a court of law, and they had the right to an attorney and didn't have to say anything without an attorney being present and if they couldn't afford one, the court would appoint them one at the proper time." Trial transcript in <i>Ohio</i> v. <i>Wood,</i> No. 10657, Common Pleas Court, Tuscarawas County, Ohio (hereafter Wood Tr.), 126. At the Doyle trial, he testified that he "gave them their rights" and gave them a " `Miranda Warning.' " Trial transcript in <i>Ohio</i> v. <i>Doyle,</i> No. 10656, Common Pleas Court, Tuscarawas County, Ohio (hereafter Doyle Tr.), 269. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, requires the following warning:</p>
<p>"[The suspect] must be warned prior to any questioning that he has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him prior to any questioning if he so desires." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 479</a></span>.</p>
<p>[3]  3A J. Wigmore, Evidence § 1042 (Chadbourn rev. 1970).</p>
<p>[4]  Petitioner Doyle gave the following testimony on direct and cross-examination at his trial:
</p>
<p>"Q. [By defense counsel.] And you were placed under arrest at that time?</p>
<p>"A. [By Doyle.] Yes. I asked what for and he said,`For the sale of marijuana.' I told him,I didn't know what he was talking about.</p>
<p>.....</p>
<p>"Q. [By the prosecutor.] As a matter of fact, if I recall your testimony correctly, you said instead of protesting your innocence, as you do today, you said in response to a question of Mr. Beamer,`I don't know what you are talking about.'</p>
<p>"A. [By Doyle.] I believe what I said,`What's this all about?' If I remember, that's the only thing I said.</p>
<p>"Q. You testified on direct.</p>
<p>"A. If I did, then I didn't understand.</p>
<p>". . . I was questioning, you know, what it was about. That's what I didn't know. I knew that I was trying to buy, which was wrong, but I didn't know what was going on. I didn't know that Bill Bonnell was trying to frame me, or what-have-you.</p>
<p>.....</p>
<p>"Q. All right,But you didn't protest your innocence at that time?</p>
<p>.....</p>
<p>"A. Not until I knew what was going on." Doyle Tr. 479, 506-507.</p>
<p>At Wood's trial, Doyle gave a somewhat different explanation of his silence at the time of arrest:</p>
<p>"Q. [By the prosecutor.] Why didn't [Wood] tell [the police officers] about Mr. Bonnell?</p>
<p>"A. [By Doyle.] Because we didn't know what was going on and wanted to find out.</p>
<p>"Q. So he hid the money under the mat?</p>
<p>"A. The police officers said they stopped us for a red light. I wanted to get my hands on Bill Bonnell.</p>
<p>"Q. It wasn't because you were guilty, was it?</p>
<p>"A. Because I wanted to get my hands on Bill Bonnell because</p>
<p>I suspected he was trying . . .</p>
<p>"Q. Why didn't you tell the police that Bill Bonnell just set you up?</p>
<p>"A. Because I would rather have my own hands on him.</p>
<p>.....</p>
<p>"Q. When Mr. Beamer arrived?</p>
<p>"A. . . . [W]hen Mr. Beamer got there I said to Mr. Beamer what the hell is all this about and he said you are under arrest for the suspicion of selling marijuana and I said you got to be crazy. I was pretty upset.</p>
<p>.....</p>
<p>"Q. So on the night of April 29 you felt that you were being framed like you are being framed today?</p>
<p>"A. I was so confused that night, the night of the arrest.</p>
<p>"Q. How about Mr. Wood?</p>
<p>"A. Mr. Wood didn't know what was going on.</p>
<p>.....</p>
<p>"Q. . . . Are you as mad and upset today as you were that night?</p>
<p>"A. I can't answer that question.</p>
<p>"Q. Did you feel the same way about what happened to you?</p>
<p>"A. That night I felt like I couldn't believe what was happening.</p>
<p>"Q. You didn't like being framed?</p>
<p>"A. That is right. I didn't like some one putting me in a spot like that.</p>
<p>"Q. Didn't it occur to you to try to protect yourself?</p>
<p>"A. Yes, at this time I felt like I wasn't talking to nobody but John James who was the attorney at that time.</p>
<p>"Q. But you felt . . .</p>
<p>"A. The man walked up and didn't ask me anything.</p>
<p>"Q. You didn't talk to a soul about how rotten it was because you were framed?</p>
<p>.....</p>
<p>"A. I will answer the question, sir, the best I can. I didn't know what to say. I was stunned about what was going on and I was asked questions and I answered the questions as simply as I could because I didn't have nobody there to help me answer the questions.</p>
<p>"Q. Wouldn't that have been a marvelous time to protest your innocence?</p>
<p>.....</p>
<p>"A. I don't know if it would or not.</p>
<p>"Q. Do you remember having a conversation with Kenneth Beamer?</p>
<p>"A. Yes, sir.</p>
<p>"Q. What was said?</p>
<p>.....</p>
<p>"A. Kenneth Beamer said I want to know where you stash where your hide out is, where you are keeping the dope and I said I don't know what you are talking about. I believe the question was asked in front of you.</p>
<p>"Q. Where did this conversation take place?</p>
<p>"A. Took place during the search.</p>
<p>.....</p>
<p>"Q. So any way you didn't tell anyone how angry you were that night?</p>
<p>.....</p>
<p>"A. I was very angry.</p>
<p>"Q. But you didn't tell anyone?</p>
<p>"A. That is right. If I started I don't know where I would have stopped. I was upset." Wood Tr. 424-430.</p>
<p>Petitioner Wood testified on cross-examination at his trial as follows:</p>
<p>"Q. [By the prosecutor.] Jefferson Doyle said he was confused, angry and upset [at the time of the arrest]. Were you confused, angry and upset?</p>
<p>.....</p>
<p>"A. [By Wood.] Upset and confused.</p>
<p>"Q. Why were you upset?</p>
<p>"A. Because I didn't know what was going on most of the time.</p>
<p>"Q. Why would you be upset? Because you found $1300 in your back seat?</p>
<p>"A. Mainly because the person that was in the car Jeff [Doyle] was upset confused and angry and . . .</p>
<p>"Q. What has that to do with you?</p>
<p>"A. I am in the car. That is what it has to do with me.</p>
<p>.....</p>
<p>"Q. You are innocent?</p>
<p>"A. Yes.</p>
<p>"Q. Of anything?</p>
<p>"A. I don't know about anything.</p>
<p>"Q. This particular incident, you were placed under arrest, weren't you?</p>
<p>"A. Yes, innocent of this incident.</p>
<p>"Q. Innocent of the entire transaction?</p>
<p>"A. Yes, sir.</p>
<p>"Q. Or even any knowledge of the entire transaction?</p>
<p>"A. Up to a point, sir.</p>
<p>.....</p>
<p>"Q. Mr. Wood, if that is all you had to do with this and you are innocent, when Mr. Beamer arrived on the scene why didn't you tell him?</p>
<p>.....</p>
<p>"A. Mr. Cunningham, in the last eight months to a year there has been so many implications, etc. in the paper and law enforcement that are setting people up and busting them for narcotics and stuff." Wood Tr. 467-469.</p>
<p>[5]  See <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#206" aria-description="Citation for case: Massiah v. United States">377 U. S. 201, 206-207</a></span>; 8 J. Wigmore, Evidence § 2270, pp. 416-417 (McNaughton rev. 1961); cf. <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174</a></span>. Cross-examination and comment upon a witness' prior silence does not raise any inference prejudicial to the defendant, and indeed, does not even raise any inference that the defendant remained silent.</p>
<p>[6]  "In accord with our decision today, it is impermissible to penalize an individual for exercising his Fifth Amendment privilege when he is under police custodial interrogation. The prosecution may not, therefore, use at trial the fact that he stood mute or claimed his privilege in the face of accusation. Cf. <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965); <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span> (1964); Comment, <span class="citation no-link">31 U. Chi. L. Rev. 556</span> (1964); Developments in the LawConfessions, <span class="citation no-link">79 Harv. L. Rev. 935</span>, 1041-1044 (1966). See also <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#562" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 562</a></span> (1897)." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 468</a></span> n. 37.</p>
<p>[7]  See n. 4, <i>supra.</i></p>
<p>[8]  As the Court recently recognized in a most carefully considered opinion, an adversary system can maintain neither the reality nor the appearance of efficacy without the assurance that its judgments rest upon a complete illumination of a case rather than upon "a partial or speculative presentation of the facts." <i>United States</i> v. <i>Nixon,</i> <span class="citation" data-id="109101"><a href="/opinion/109101/united-states-v-nixon/#709" aria-description="Citation for case: United States v. Nixon">418 U. S. 683, 709</a></span>. The necessity of insuring a complete presentation of all relevant evidence has led to the rule that a criminal defendant who voluntarily forgoes his privilege not to testify, and presents exculpatory or mitigating evidence, thereby subjects himself to relevant cross-examination without the right to reclaim Fifth Amendment protection on a selective basis. <i>Fitzpatrick</i> v. <i>United States,</i> <span class="citation" data-id="95301"><a href="/opinion/95301/fitzpatrick-v-united-states/#315" aria-description="Citation for case: Fitzpatrick v. United States">178 U. S. 304, 315</a></span>.
</p>
<p>"If he takes the stand and testifies in his own defense, his credibility may be impeached and his testimony assailed like that of any other witness, and the breadth of his waiver is determined by the scope of relevant cross-examination. `[H]e has no right to set forth to the jury all the facts which tend in his favor without laying himself open to a cross-examination upon those facts.' " <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="9421572"><a href="/opinion/105661/brown-v-united-states/#154" aria-description="Citation for case: Brown v. United States">356 U. S. 148, 154-155</a></span> (citation omitted).</p>
<p>One need not impute perjury to an entire class to acknowledge that a testifying defendant has more to gain and less to lose than an ordinary witness from fabrications upon the witness stand. Cf. <i>Reagan</i> v. <i>United States,</i> <span class="citation" data-id="94162"><a href="/opinion/94162/reagan-v-united-states/#304" aria-description="Citation for case: Reagan v. United States">157 U. S. 301, 304-311</a></span>; <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="279002"><a href="/opinion/279002/calvin-j-taylor-v-united-states/#284" aria-description="Citation for case: Calvin J. Taylor v. United States">390 F. 2d 278, 284-285</a></span> (CA8 1968) (Blackmun, J.). As the Court notes today: "Unless prosecutors are allowed wide leeway in the scope of impeachment cross-examination some defendants would be able to frustrate the truth-seeking function of a trial by presenting tailored defenses insulated from effective challenge." <i>Ante,</i> at 617 n. 7. In recognition of this fact, this Court has allowed evidence to be used for impeachment purposes that would be inadmissible as evidence of guilt. In <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span>, evidence of narcotics unlawfully seized in connection with an aborted earlier case against a defendant was held admissible for the limited purpose of impeaching the defendant's testimony that he never had been associated with narcotics, although such evidence clearly was inadmissible for any purpose in the prosecution's case in chief. In <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span>, the Court held admissible for the purpose of impeaching a defendant's testimony certain partially inconsistent post-arrest statements which, although voluntary, were unavailable for the prosecution's case because they had been given by the defendant without benefit of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. And last Term, in a decision closely analogous to <i><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span>,</i> the Court held admissible for impeachment purposes post-arrest statements of a defendant made after he had received <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and exercised his right to request a lawyer, but before he had been furnished with counsel as <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires in such circumstances. <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span>.</p>
<p>In each of these cases involving impeachment cross-examination, the need to insure the integrity of the trial by the "traditional truth-testing devices of the adversary process," <i>Harris</i> v. <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York"><i>New York, supra,</i> at 225</a></span>, was deemed to outweigh the policies underlying the relevant exclusionary rules.</p>
<p>[9]  Petitioner Doyle was cross-examined as follows at his trial:
</p>
<p>"Q. [By the prosecutor.] All right. Do you remember the Preliminary Hearing in this case?</p>
<p>"A. [By Doyle.] Yes Sir. I remember it.</p>
<p>"Q. And that was prior to your indictment for this offense, was it not?</p>
<p>"A. Yes sir. I believe,Yes Sir, it was before I was indicted.</p>
<p>"Q. Arraignment. Is that what you mean?</p>
<p>"A. Yes. The next day after the arrest.</p>
<p>"Q. Yes, when evidence was presented and you had the opportunity to hear the testimony of the witnesses against you. Remember that?</p>
<p>"A. Yes Sir.</p>
<p>"Q. Mr. Bonnell testified; Captain Griffin testified; Deputy Chief Deputy White testified?</p>
<p>"A. Yes Sir.</p>
<p>"Q. Kenneth Beamer testified?</p>
<p>"A. Yes Sir.</p>
<p>"Q. You were there, weren't you?</p>
<p>"A. Yes Sir.</p>
<p>"Q. And your lawyer was there,Mr. James?</p>
<p>"A. Yes Sir.</p>
<p>"Q. Tape recording was made of the transcript?</p>
<p>"A. Yes Sir.</p>
<p>"Q. Did you protest your innocence at that proceeding?</p>
<p>.....</p>
<p>"A. I didn'teverything that was done with that was done with my attorney. My attorney did it.</p>
<p>"Q. All right. The first time that you gave this version of the fact was in the trial of Richard Wood,was it not?</p>
<p>.....</p>
<p>"A. Yes Sir. It was the first time I was asked.</p>
<p>"Q. All the time, you being innocent?</p>
<p>"A. Yes Sir." Doyle Tr. 507-508.</p>
<p>Petitioner Wood was subjected to similar cross-examination at his trial:</p>
<p>"Q. [By the prosecutor.] As a matter of fact you never told anyone that you had been set up until today?</p>
<p>.....</p>
<p>"A. [By Wood.] Yes, I believe I did, sir.</p>
<p>"Q. I assume you discussed it with your lawyer?</p>
<p>"A. Yes, I discussed it with my lawyer.</p>
<p>"Q. And you heard the testimony and witnesses against you?</p>
<p>"A. Yes, sir.</p>
<p>"Q. And were you aware Mr. James was able to obtain a tape transcript of the proceedings?</p>
<p>"A. Yes.</p>
<p>"Q. And you no doubt listened to those?</p>
<p>"A. Parts and portions of themsome of it.</p>
<p>"Q. But you never communicated your innocence?</p>
<p>"A. I believe I did one time to Mr. Beamer.</p>
<p>"Q. When might that have been?</p>
<p>"A. When in the jail house.</p>
<p>"Q. So you protested your innocence?</p>
<p>"A. In a little room. I believe he asked us how do you let people get away with people setting up friends like this. He said Bill Bonnell is not your friend and I said no, but I figured he was a good enough acquaintance he would do that.</p>
<p>"Q. Where was that?</p>
<p>"A. Little room there.</p>
<p>"Q. Ever been there before?</p>
<p>"A. Yes, sir.</p>
<p>"Q. When?</p>
<p>.....</p>
<p>"Q. Did you see me there?</p>
<p>"A. I didn't know who you were at the time. I believe you were in and out of there.</p>
<p>"Q. You didn't say anything to me, did you?</p>
<p>"A. No, I didn't know who you were then." Wood Tr. 470-472.</p>
<p>[10]  Under Ohio law, the preliminary hearing determines only whether the defendant should be held for trial. The prosecution need establish, at most, that a crime has been committed and that there is "probable and reasonable cause" to hold the defendant for trial, and the court need only find "substantial credible evidence" of the charge against the defendant. <span class="citation no-link">Ohio Rev. Code Ann. §§ 2937.12</span>, 2937.13 (Supp. 1973). Indeed, if a defendant has been indicted, no hearing need be held. <i>State</i> v. <i>Morris,</i> <span class="citation" data-id="6755494"><a href="/opinion/6865449/state-v-morris/#326" aria-description="Citation for case: State v. Morris">42 Ohio St. 2d 307, 326</a></span>, <span class="citation" data-id="6755494"><a href="/opinion/6865449/state-v-morris/#97" aria-description="Citation for case: State v. Morris">329 N. E. 2d 85, 97</a></span> (1975). Defense counsel thus will have no incentive to divulge the defendant's case at the preliminary hearing if the prosecution has presented substantial evidence of guilt. Since that was the case here, no significant impeaching inference may be drawn from petitioners' silence at that proceeding.
</p>
<p>Petitioners' failure to refer to the "frame" at any time between arrest and trial is somewhat more probative; for if the "frame" story were true, one would have expected counsel to try to persuade the prosecution to dismiss the charges in advance of trial.</p>
<p>[11]  <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> was the last decision of this Court to address the constitutionality of admitting evidence of a defendant's prior silence to impeach his testimony upon direct examination. Raffel had been charged with conspiracy to violate the National Prohibition Act. An agent testified at his first trial that he had admitted ownership of a drinking place; Raffel did not take the stand. The trial ended in a hung jury, and upon retrial, the agent testified as before. Raffel elected to testify and denied making the statement, but he was cross-examined on his failure to testify in the first trial. This Court held that the evidence was admissible because Raffel had completely waived the privilege against self-incrimination by deciding to testify. <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/#499" aria-description="Citation for case: Raffel v. United States">271 U. S., at 499</a></span>.
</p>
<p>Subsequent cases, decided in the exercise of this Court's supervisory powers, have diminished the force of <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> in the federal courts. <i>United States</i> v. <i>Hale,</i> <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">422 U. S. 171</a></span>; <i>Stewart</i> v. <i>United States,</i> <span class="citation" data-id="9422185"><a href="/opinion/106219/stewart-v-united-states/" aria-description="Citation for case: Stewart v. United States">366 U. S. 1</a></span>; <i>Grunewald</i> v. <i>United States,</i> <span class="citation" data-id="9421440"><a href="/opinion/105508/grunewald-v-united-states/" aria-description="Citation for case: Grunewald v. United States">353 U. S. 391</a></span>. All three of these cases held that the defendant's prior silence or prior claim of the privilege was inadmissible for purposes of impeachment; all three distinguished <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> on the ground that the Court there assumed that the defendant's prior silence was significantly inconsistent with his testimony on direct examination. <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/#175" aria-description="Citation for case: United States v. Hale"><i>Hale, supra,</i> at 175-176</a></span>; <span class="citation" data-id="9422185"><a href="/opinion/106219/stewart-v-united-states/#5" aria-description="Citation for case: Stewart v. United States"><i>Stewart, supra,</i> at 5-7</a></span>; <span class="citation" data-id="9421440"><a href="/opinion/105508/grunewald-v-united-states/#418" aria-description="Citation for case: Grunewald v. United States"><i>Grunewald, supra,</i> at 418-424</a></span>. Two of the three cases relied upon the need to protect the defendant's exercise of the privilege against self-incrimination from unwarranted inferences of guilt, a rationale that is not easily reconciled with the reasoning in <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> that the decision to testify constitutes a complete waiver of the protection afforded by the privilege. Compare <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale, supra,</a></span></i> at 180 and n. 7, and <span class="citation" data-id="9421440"><a href="/opinion/105508/grunewald-v-united-states/#423" aria-description="Citation for case: Grunewald v. United States"><i>Grunewald, supra,</i> at 423-424</a></span>, with <i>Raffel,</i> <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/#499" aria-description="Citation for case: Raffel v. United States">271 U. S., at 499</a></span>.</p>
<p>[12]  At Doyle's trial, the prosecutor made the following arguments to the jury:
</p>
<p>"Diffuse what the true facts are; obscure the facts and prosecute the prosecution.</p>
<p>"A typical and classic defense, but keep in mind, when you are considering the testimony of the law enforcement officers involved, that not until, Ladies and Gentlemen, not until the trial of this case and prior to this case, the trial of Richard Wood's case, that anybody connected with the prosecution in this case had any idea what stories would be told by Jefferson Doyle and Richard Wood. Not the foggiest idea. Both of them told you on the witness stand that neither one of them said a word to the law enforcement officials on the scene</p>
<p>.....</p>
<p>"(continuing) on the scene at the point of their arrest, at the Preliminary Hearing before Indictment in this case. Not a word that they were innocent; that this was their position; that somehow, they had been `set-up.'</p>
<p>"So, when you evaluate the testimony of the Law Enforcement Officials, consider</p>
<p>.....</p>
<p>"(continuing)what they had to deal with on the night in question and the months subsequent to that.</p>
<p>.....</p>
<p>"Then they decide that they have been `had' somehow. They have been framed.</p>
<p>"Now, remember, this fits with the facts as observed by the law enforcement officers except the basic, crucial facts. Somehow, they have been framed. So, if you can believe this, Ladies and Gentlemen, they take off, chase Bill Bonnell around to give his money back to him or ask him what he did to them, yet they don't bother to tell the Law Enforcement Officers.</p>
<p>"It is unbelievable. I think, when you go to the Jury Room, Ladies and Gentlemen, you are going to decide what really happened.</p>
<p>.....</p>
<p>"We have the Fifth Amendment. I agree with it. It is fundamental to our sense and system of fairness, but if you are innocent</p>
<p>.....</p>
<p>"(continuing)if you are innocent, Ladies and Gentlemen, if you have been framed, if you have been set-on, etc. etc. etc., as we heard in Court these last days, you don't say, when the law enforcement officer says,`You are under arrest,'you don't say,`I don't know what you are talking about.' You tell the truth. You tell them what happened and you go from there. You don't say, `I don't know what you are talking about,'and demand to see your lawyer and refuse to permit a search of your vehicle, forcing the law enforcement agents to get a search warrant.</p>
<p>"If you're innocent, you just don't do it." Doyle Tr. 515-516, 519, 526.</p>
<p>At Wood's trial, he made similar arguments:</p>
<p>"The defense in this case was very careful to make no statements at all until they had the benefit of hearing all the evidence against them and had time to ascertain what they would admit and what they would deny and how they could fit their version of the story with the state's case. During none of this time did we ever hear any business about a set up or frame or anything else. All right.</p>
<p>"Yes, it is the law of our land, and rightfully so, ladies and gentlemen, that nobody must be compelled to incriminate themselves. It is the 5th Amendment. No one can be forced to give testimony against themselves where criminal action charges are pending. It is a very fundamental right and I am glad we have it.</p>
<p>"The idea was nobody can convict himself out of his own mouth and it grew out of the days when they used to whip and beat and extract statements from the defendants and get them to convict themselves out of their own mouth, and I am glad we have that right.</p>
<p>"But ladies and gentlemen, there is one statement I am going to make. If you are innocent, if you are innocent, if you have been framed, if you have been set up as claimed in this case, when do you tell it? When do you tell the policemen that?</p>
<p>.....</p>
<p>"Think about it. After monthsafter various proceedings and for the first time? I am not going to say any more about that but I want you to think about it." Closing Argument of the Prosecutor 12-14, supplementing Wood Tr.</p>
<p>[13]  Petitioner Doyle also argues that he was erroneously cross-examined at his trial on his failure to consent to a search of the car he was driving at the time of the arrest. Petitioner Wood appears to raise the similar claim that testimony of other witnesses that he failed to consent to a search of the car was erroneously admitted at his trial. The parties have not argued these issues separately from the questions whether prior silence in various circumstances may be admitted to impeach a defendant or a defense witness. It is apparent, however, that these questions implicate Fourth Amendment issues that merit independent examination. Accordingly, like the Court, I do not address them.</p>

</div>
```

---

## GROUP: content/cases/Draper v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Draper v. United States"
type: case
citation: "358 U.S. 307 (1959)"
parallel_cite: "79 S. Ct. 329; 3 L. Ed. 2d 327"
neutral_cite: 1959 U.S. LEXIS 1607
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1959
date_decided: 1959-01-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1959-01-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Draper v. United States
  varies_by_point: false
  scope_note: "Good law. A reliable informant's detailed tip whose innocent details police personally corroborate furnishes probable cause to arrest, even though the corroborated facts are themselves innocent. Folded into the totality-of-circumstances test of Illinois v. Gates."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105820/draper-v-united-states/"
  cluster_id: 105820
  opinion_id: 105820
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Progeny"
related: ["[[Brinegar v. United States]]", "[[Illinois v. Gates]]", "[[Aguilar v. Texas]]", "[[Spinelli v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "informant", "corroboration", "warrantless-arrest"]
holding: "A reliable informant's detailed tip, the innocent details of which police personally corroborate, establishes probable cause to arrest even though the corroborated facts are themselves innocent."
lake:
  record_id: Draper v. United States
  status: verified
  projected_at: 2026-07-09
---

# Draper v. United States

*358 U.S. 307 (1959)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A reliable paid informant, Hereford, told federal narcotics agent Marsh that James Draper had gone to Chicago and would return by train on one of two specified mornings carrying three ounces of heroin. Hereford described Draper's exact physical appearance, the precise clothing he would wear, the tan zipper bag he would carry, and his habit of walking fast. On the second morning Marsh watched a man matching every detail alight from the Chicago train and walk quickly toward the exit. Marsh arrested him without a warrant; a search incident to the arrest produced heroin and a syringe. Draper moved to suppress, arguing the agents lacked probable cause.

## Issue
Whether a reliable informant's detailed tip — the innocent details of which police personally corroborate before acting — furnishes probable cause for a warrantless arrest, even though the corroborated facts are innocent and the informant's information was hearsay to the arresting officer.

## Rule
Yes. Where police corroborate the verifiable details of a reliable informant's tip, they may reasonably infer that the remaining, incriminating detail is also true. "[W]ith every other bit of Hereford's information being thus personally verified, Marsh had 'reasonable grounds' to believe that the remaining unverified bit of Hereford's information — that Draper would have the heroin with him — was likewise true." — 358 U.S. at 313. ^pin-313

Probable cause is a practical, non-technical standard: "In dealing with probable cause, . . . as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act." — [*Id.* at 313](https://www.courtlistener.com/opinion/105820/draper-v-united-states/#:~:text=In%20dealing%20with%20probable%20cause%2C) (quoting *Brinegar v. United States*). ^pin-313b

## Application
Hereford was a "special employee" whose information had always proved accurate and reliable, so Marsh would have been "derelict in his duties had he not pursued it." When Marsh personally observed a man with Draper's exact attributes, clothing, and bag step off the very train from the place Hereford named and walk fast toward the exit, he had verified every facet of the tip except the heroin itself. That corroboration of the innocent details gave Marsh reasonable grounds to credit the one unverified, incriminating detail — that Draper was carrying heroin — supplying probable cause for the arrest and the search incident to it.

## Conclusion
Probable cause existed; the warrantless arrest and the search incident to it were lawful and the heroin was admissible. The conviction was affirmed. A reliable, detailed tip corroborated by police observation can establish probable cause even when the corroborated conduct is innocent.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Draper*'s corroboration principle was preserved and absorbed into the totality-of-the-circumstances test of [[Illinois v. Gates]] (which abandoned the rigid [[Aguilar v. Texas]]/[[Spinelli v. United States]] two-pronged formulation while reaffirming *Draper*-style corroboration as strong evidence of probable cause).

## Appears on
- [[Probable Cause]] — *Progeny*

## Sources
- *Draper v. United States*, 358 U.S. 307 (1959) — https://www.courtlistener.com/opinion/105820/draper-v-united-states/ — pinpoint: 313.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e7e1263df18f1814", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "358 U.S. 307 (1959)", "court": "U.S. Supreme Court", "neutral_cite": "1959 U.S. LEXIS 1607", "official_citation_present": true, "parallel_cite": "79 S. Ct. 329; 3 L. Ed. 2d 327", "title": "Draper v. United States", "year": "1959"}}
{"assertion_id": "5f64cb0a0bbb6dde", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Progeny", "title": "Draper v. United States"}}
{"assertion_id": "9f3ea234a77cd7d9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A reliable informant's detailed tip, the innocent details of which police personally corroborate, establishes probable cause to arrest even though the corroborated facts are themselves innocent.", "title": "Draper v. United States"}}
{"assertion_id": "20b79b90cd1b4a51", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Draper v. United States"}}
{"assertion_id": "713809a853d6b60e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1959-01-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Draper v. United States", "field_i_validity": "good_law", "scope_note": "Good law. A reliable informant's detailed tip whose innocent details police personally corroborate furnishes probable cause to arrest, even though the corroborated facts are themselves innocent. Folded into the totality-of-circumstances test of Illinois v. Gates.", "title": "Draper v. United States", "varies_by_point": "false"}}
```

### lake record — Draper v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Draper v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Draper v. United States",
    "case_name_short": "Draper",
    "case_name_full": "Draper v. United States",
    "input_case_name": "Draper v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1959-01-26",
    "year": 1959,
    "docket": null,
    "cluster_id": 105820,
    "lead_opinion_id": 105820,
    "sibling_ids": [
      105820,
      9421741,
      9421742
    ],
    "absolute_url": "/opinion/105820/draper-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "358 U.S. 307",
      "volume": "358",
      "reporter": "U.S.",
      "page": "307",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "79 S. Ct. 329",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "329",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 327",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "327",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1959 U.S. LEXIS 1607",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "1607",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "358 U.S. 307",
        "volume": "358",
        "reporter": "U.S.",
        "page": "307",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 S. Ct. 329",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "329",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 327",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "327",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1959 U.S. LEXIS 1607",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "1607",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "358 U.S. 307",
    "official_selection": {
      "court_class": "scotus",
      "selected": "358 U.S. 307",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-313",
      "page": null,
      "quote": "--- # Draper v. United States *358 U.S. 307 (1959)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A reliable paid informant, Hereford, told federal narcotics agent Marsh that James Draper had gone to Chicago and would return by train on one of two specified mornings carrying three ounces of heroin. Hereford described Draper's exact physical appearance, the precise clothing he would wear, the tan zipper bag he would carry, and his habit of walking fast. On the second morning Marsh watched a man matching every detail alight from the Chicago train and walk quickly toward the exit. Marsh arrested him without a warrant; a search incident to the arrest produced heroin and a syringe. Draper moved to suppress, arguing the agents lacked probable cause. ## Issue Whether a reliable informant's detailed tip \u2014 the innocent details of which police personally corroborate before acting \u2014 furnishes probable cause for a warrantless arrest, even though the corroborated facts are innocent and the informant's information was hearsay to the arresting officer. ## Rule Yes. Where police corroborate the verifiable details of a reliable informant's tip, they may reasonably infer that the remaining, incriminating detail is also true.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-313b",
      "page": null,
      "quote": "In dealing with probable cause, . . . as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act.",
      "star_marker": "313",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11420,
      "fragment": "#:~:text=In%20dealing%20with%20probable%20cause%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1959-01-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Draper v. United States",
    "varies_by_point": false,
    "scope_note": "Good law. A reliable informant's detailed tip whose innocent details police personally corroborate furnishes probable cause to arrest, even though the corroborated facts are themselves innocent. Folded into the totality-of-circumstances test of Illinois v. Gates.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Muldrow",
          "cluster_id": 4448772,
          "cite": [
            "2017 Ohio 8839",
            "100 N.E.3d 1093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Charley",
          "cluster_id": 4378006,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mark C. Hunter",
          "cluster_id": 2672711,
          "cite": [
            "156 Idaho 568",
            "328 P.3d 548",
            "2014 WL 1777986",
            "2014 Ida. App. LEXIS 51"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane1_negative"
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
        "journal_ref": "Draper v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Snell v. Com.",
          "cluster_id": 1058505,
          "cite": [
            "659 S.E.2d 510",
            "275 Va. 472",
            "2008 Va. LEXIS 50"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Birmingham v. Sutherland",
          "cluster_id": 1732877,
          "cite": [
            "834 So. 2d 755",
            "2002 WL 475176"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 2188251,
          "cite": [
            "32 S.W.3d 294",
            "2000 WL 1389720"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Curry v. State",
          "cluster_id": 1722567,
          "cite": [
            "965 S.W.2d 32",
            "1998 Tex. App. LEXIS 1214",
            "1998 WL 80406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 3937770,
          "cite": [
            "689 N.E.2d 598",
            "116 Ohio App. 3d 842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguilar v. Texas",
          "cluster_id": 106865,
          "cite": [
            "12 L. Ed. 2d 723",
            "84 S. Ct. 1509",
            "378 U.S. 108",
            "1964 U.S. LEXIS 994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
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
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. United States",
          "cluster_id": 107831,
          "cite": [
            "21 L. Ed. 2d 637",
            "89 S. Ct. 584",
            "393 U.S. 410",
            "1969 U.S. LEXIS 2701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. United States",
          "cluster_id": 106022,
          "cite": [
            "4 L. Ed. 2d 697",
            "80 S. Ct. 725",
            "362 U.S. 257",
            "1960 U.S. LEXIS 1413",
            "78 A.L.R. 2d 233"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
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
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
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
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. United States",
          "cluster_id": 105963,
          "cite": [
            "4 L. Ed. 2d 134",
            "80 S. Ct. 168",
            "361 U.S. 98",
            "1959 U.S. LEXIS 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiteley v. Warden, Wyoming State Penitentiary",
          "cluster_id": 108297,
          "cite": [
            "28 L. Ed. 2d 306",
            "91 S. Ct. 1031",
            "401 U.S. 560",
            "1971 U.S. LEXIS 65",
            "58 Ohio Op. 2d 434"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harris",
          "cluster_id": 108379,
          "cite": [
            "29 L. Ed. 2d 723",
            "91 S. Ct. 2075",
            "403 U.S. 573",
            "1971 U.S. LEXIS 18"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
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
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCray v. Illinois",
          "cluster_id": 107394,
          "cite": [
            "18 L. Ed. 2d 62",
            "87 S. Ct. 1056",
            "386 U.S. 300",
            "1967 U.S. LEXIS 1983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Janis",
          "cluster_id": 109539,
          "cite": [
            "49 L. Ed. 2d 1046",
            "96 S. Ct. 3021",
            "428 U.S. 433",
            "1976 U.S. LEXIS 162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Draper v. United States:lane2_top_cited"
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
        "journal_ref": "Draper v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105820 OR 9421741 OR 9421742) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NTEwNDAwMDAwMDAmcz0zOTM3NzcwJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105820+OR+9421741+OR+9421742%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(105820 OR 9421741 OR 9421742)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDgmcz00NDU0NjAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28105820+OR+9421741+OR+9421742%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105820 OR 9421741 OR 9421742)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 0,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(105820 OR 9421741 OR 9421742)",
    "indexed_citing_opinions": 2159,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105820,
        "count": 2001,
        "count_source": "search"
      },
      {
        "opinion_id": 9421741,
        "count": 211,
        "count_source": "search"
      },
      {
        "opinion_id": 9421742,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3191,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/draper-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcyNTA5MjQmcz00ODgyNjI3JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28105820+OR+9421741+OR+9421742%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105820,
        "cited_id": 87693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 89833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 100265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 100685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 227325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 231565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 240261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 242778,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 243147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1428463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1475726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1479874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1496911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1501475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1507600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1509096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1511010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1565168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1568274,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1570757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1735465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 1876453,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105820,
        "cited_id": 3880639,
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
    "date_created": "2026-07-05T02:53:55Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:54:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:54:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:54:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Draper v. United States

```
<div>
<center><b><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U.S. 307</a></span> (1959)</b></center>
<center><h1>DRAPER<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 136.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 11, 1958.</center>
<center>Decided January 26, 1959.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE TENTH CIRCUIT.
<p><i>Osmond K. Fraenkel</i> argued the cause and filed a brief for petitioner.</p>
<p><span class="star-pagination">*308</span> <i>Leonard B. Sand</i> argued the cause for the United States. On the brief were <i>Solicitor General Rankin, Assistant Attorney General Anderson, Beatrice Rosenberg</i> and <i>Jerome M. Feit.</i></p>
<p>MR. JUSTICE WHITTAKER delivered the opinion of the Court.</p>
<p>Petitioner was convicted of knowingly concealing and transporting narcotic drugs in Denver, Colorado, in violation of <span class="citation no-link">35 Stat. 614</span>, as amended, <span class="citation no-link">21 U. S. C. § 174</span>. His conviction was based in part on the use in evidence against him of two "envelopes containing [865 grains of] heroin" and a hypodermic syringe that had been taken from his person, following his arrest, by the arresting officer. Before the trial, he moved to suppress that evidence as having been secured through an unlawful search and seizure. After hearing, the District Court found that the arresting officer had probable cause to arrest petitioner without a warrant and that the subsequent search and seizure were therefore incident to a lawful arrest, and overruled the motion to suppress. <span class="citation" data-id="8723682"><a href="/opinion/8740441/united-states-v-draper/" aria-description="Citation for case: United States v. Draper">146 F. Supp. 689</a></span>. At the subsequent trial, that evidence was offered and, over petitioner's renewed objection, was received in evidence, and the trial resulted, as we have said, in petitioner's conviction. The Court of Appeals affirmed the conviction, <span class="citation" data-id="9445840"><a href="/opinion/243147/james-alonzo-draper-v-united-states/" aria-description="Citation for case: James Alonzo Draper v. United States">248 F. 2d 295</a></span>, and certiorari was sought on the sole ground that the search and seizure violated the Fourth Amendment<sup>[1]</sup> and therefore the use of the heroin in evidence vitiated the conviction. We granted the writ to determine that question. <span class="citation multiple-matches"><a href="/c/U.%20S./357/935/">357 U. S. 935</a></span>.</p>
<p><span class="star-pagination">*309</span> The evidence offered at the hearing on the motion to suppress was not substantially disputed. It established that one Marsh, a federal narcotic agent with 29 years' experience, was stationed at Denver; that one Hereford had been engaged as a "special employee" of the Bureau of Narcotics at Denver for about six months, and from time to time gave information to Marsh regarding violations of the narcotic laws, for which Hereford was paid small sums of money, and that Marsh had always found the information given by Hereford to be accurate and reliable. On September 3, 1956, Hereford told Marsh that James Draper (petitioner) recently had taken up abode at a stated address in Denver and "was peddling narcotics to several addicts" in that city. Four days later, on September 7, Hereford told Marsh "that Draper had gone to Chicago the day before [September 6] by train [and] that he was going to bring back three ounces of heroin [and] that he would return to Denver either on the morning of the 8th of September or the morning of the 9th of September also by train." Hereford also gave Marsh a detailed physical description of Draper and of the clothing he was wearing,<sup>[2]</sup> and said that he would be carrying "a tan zipper bag," and that he habitually "walked real fast."</p>
<p>On the morning of September 8, Marsh and a Denver police officer went to the Denver Union Station and kept watch over all incoming trains from Chicago, but they did not see anyone fitting the description that Hereford had given. Repeating the process on the morning of September 9, they saw a person, having the exact physical attributes and wearing the precise clothing described by Hereford, alight from an incoming Chicago train and <span class="star-pagination">*310</span> start walking "fast" toward the exit. He was carrying a tan zipper bag in his right hand and the left was thrust in his raincoat pocket. Marsh, accompanied by the police officer, overtook, stopped and arrested him. They then searched him and found the two "envelopes containing heroin" clutched in his left hand in his raincoat pocket, and found the syringe in the tan zipper bag. Marsh then took him (petitioner) into custody. Hereford died four days after the arrest and therefore did not testify at the hearing on the motion.</p>
<p>26 U. S. C. (Supp. V) § 7607, added by § 104 (a) of the Narcotic Control Act of 1956, <span class="citation no-link">70 Stat. 570</span>, provides, in pertinent part:</p>
<blockquote>"The Commissioner . . . and agents, of the Bureau of Narcotics . . . may</blockquote>
<blockquote>.....</blockquote>
<blockquote>"(2) make arrests without warrant for violations of any law of the United States relating to narcotic drugs . . . where the violation is committed in the presence of the person making the arrest or where such person has reasonable grounds to believe that the person to be arrested has committed or is committing such violation."</blockquote>
<p>The crucial question for us then is whether knowledge of the related facts and circumstances gave Marsh "probable cause" within the meaning of the Fourth Amendment, and "reasonable grounds" within the meaning of § 104 (a), <i>supra,</i><sup>[3]</sup> to believe that petitioner had committed or was committing a violation of the narcotic laws. If it did, the arrest, though without a warrant, was lawful <span class="star-pagination">*311</span> and the subsequent search of petitioner's person and the seizure of the found heroin were validly made incident to a lawful arrest, and therefore the motion to suppress was properly overruled and the heroin was competently received in evidence at the trial. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 158</a></span>; <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>; <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#483" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 483</a></span>.</p>
<p>Petitioner does not dispute this analysis of the question for decision. Rather, he contends (1) that the information given by Hereford to Marsh was "hearsay" and, because hearsay is not legally competent evidence in a criminal trial, could not legally have been considered, but should have been put out of mind, by Marsh in assessing whether he had "probable cause" and "reasonable grounds" to arrest petitioner without a warrant, and (2) that, even if hearsay could lawfully have been considered, Marsh's information should be held insufficient to show "probable cause" and "reasonable grounds" to believe that petitioner had violated or was violating the narcotic laws and to justify his arrest without a warrant.</p>
<p>Considering the first contention, we find petitioner entirely in error. <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#172" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 172-173</a></span>, has settled the question the other way. There, in a similar situation, the convict contended "that the factors relating to inadmissibility of the evidence [for] <i>purposes of proving guilt at the trial,</i> deprive[d] the evidence as a whole of sufficiency to show probable cause for the search . . . ." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#172" aria-description="Citation for case: Brinegar v. United States"><i>Id.,</i> at 172</a></span>. (Emphasis added.) But this Court, rejecting that contention, said: "[T]he so-called distinction places a wholly unwarranted emphasis upon the criterion of admissibility in evidence, to prove the accused's guilt, of the facts relied upon to show probable cause. That emphasis, we think, goes much too far in confusing and disregarding the difference between what is required to prove guilt in a criminal case and what is <span class="star-pagination">*312</span> required to show probable cause for arrest or search. It approaches requiring (if it does not in practical effect require) proof sufficient to establish guilt in order to substantiate the existence of probable cause. There is a large difference between the two things to be proved [guilt and probable cause], as well as between the tribunals which determine them, and therefore a like difference in the <i>quanta</i> and modes of proof required to establish them."<sup>[4]</sup> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#172" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 172-173</a></span>.</p>
<p>Nor can we agree with petitioner's second contention that Marsh's information was insufficient to show probable cause and reasonable grounds to believe that petitioner had violated or was violating the narcotic laws and to justify his arrest without a warrant. The information given to narcotic agent Marsh by "special employee" <span class="star-pagination">*313</span> Hereford may have been hearsay to Marsh, but coming from one employed for that purpose and whose information had always been found accurate and reliable, it is clear that Marsh would have been derelict in his duties had he not pursued it. And when, in pursuing that information, he saw a man, having the exact physical attributes and wearing the precise clothing and carrying the tan zipper bag that Hereford had described, alight from one of the very trains from the very place stated by Hereford and start to walk at a "fast" pace toward the station exit, Marsh had personally verified every facet of the information given him by Hereford except whether petitioner had accomplished his mission and had the three ounces of heroin on his person or in his bag. And surely, with every other bit of Hereford's information being thus personally verified, Marsh had "reasonable grounds" to believe that the remaining unverified bit of Hereford's informationthat Draper would have the heroin with himwas likewise true.</p>
<p>"In dealing with probable cause, . . . as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act." <i>Brinegar</i> v. <i>United States, supra,</i> at 175. Probable cause exists where "the facts and circumstances within [the arresting officers'] knowledge and of which they had reasonably trustworthy information [are] sufficient in themselves to warrant a man of reasonable caution in the belief that" an offense has been or is being committed. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span>.<sup>[5]</sup></p>
<p><span class="star-pagination">*314</span> We believe that, under the facts and circumstances here, Marsh had probable cause and reasonable grounds to believe that petitioner was committing a violation of the laws of the United States relating to narcotic drugs at the time he arrested him. The arrest was therefore lawful, and the subsequent search and seizure, having been made incident to that lawful arrest, were likewise valid.<sup>[6]</sup> It follows that petitioner's motion to suppress was properly denied and that the seized heroin was competent evidence lawfully received at the trial.</p>
<p><i>Affirmed.</i></p>
<p>THE CHIEF JUSTICE and MR. JUSTICE FRANKFURTER took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE DOUGLAS, dissenting.</p>
<p>Decisions under the Fourth Amendment,<sup>[1]</sup> taken in the long view, have not given the protection to the citizen which the letter and spirit of the Amendment would seem to require. One reason, I think, is that wherever a culprit is caught red-handed, as in leading Fourth Amendment cases, it is difficult to adopt and enforce a rule that would turn him loose. A rule protective of law-abiding citizens is not apt to flourish where its advocates are usually criminals. Yet the rule we fashion is for the innocent and guilty alike. If the word of the informer <span class="star-pagination">*315</span> on which the present arrest was made is sufficient to make the arrest legal, his word would also protect the police who, acting on it, hauled the innocent citizen off to jail.</p>
<p>Of course, the education we receive from mystery stories and television shows teaches that what happened in this case is efficient police work. The police are tipped off that a man carrying narcotics will step off the morning train. A man meeting the precise description does alight from the train. No warrant for his arrest has beenor, as I see it, could then beobtained. Yet he is arrested; and narcotics are found in his pocket and a syringe in the bag he carried. This is the familiar pattern of crime detection which has been dinned into public consciousness as the correct and efficient one. It is, however, a distorted reflection of the constitutional system under which we are supposed to live.</p>
<p>With all due deference, the arrest made here on the mere word of an informer violated the spirit of the Fourth Amendment and the requirement of the law, 26 U. S. C. (Supp. V) § 7607, governing arrests in narcotics cases. If an arrest is made without a warrant, the offense must be committed in the presence of the officer or the officer must have "reasonable grounds to believe that the person to be arrested has committed or is committing" a violation of the narcotics law. The arresting officers did not have a bit of evidence, known to them and as to which they could take an oath had they gone to a magistrate for a warrant, that petitioner had committed any crime. The arresting officers did not know the grounds on which the informer based his conclusion; nor did they seek to find out what they were. They acted solely on the informer's word. In my view that was not enough.</p>
<p>The rule which permits arrest for felonies, as distinguished from misdemeanors, if there are reasonable grounds for believing a crime has been or is being committed (<i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#157" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 157</a></span>), <span class="star-pagination">*316</span> grew out of the need to protect the public safety by making prompt arrests. <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Id.</a></span></i> Yet, apart from those cases where the crime is committed in the presence of the officer, arrests without warrants, like searches without warrants, are the exception, not the rule in our society. Lord Chief Justice Pratt in <i>Wilkes</i> v. <i>Wood,</i> 19 How. St. Tr. 1153, condemned not only the odious general warrant,<sup>[2]</sup> in which the name of the citizen to be arrested was left blank, but the whole scheme of seizures and searches<sup>[3]</sup> under "a discretionary power" of law officers to act "wherever their suspicions may chance to fall"a practice which he denounced as "totally subversive of the liberty of the subject." <i>Id.,</i> at 1167. See III May, Constitutional History of England, c. XI. Wilkes had written in 1762, "To take any man into custody, and deprive him of his liberty, without having some seeming foundation at least, on which to justify such a step, is inconsistent with wisdom and sound policy." The Life and Political Writings of John Wilkes, p. 372.</p>
<p>George III in 1777 pressed for a bill which would allow arrests on suspicion of treason committed in America. The words were "suspected of" treason and it was to these words that Wilkes addressed himself in Parliament. "There is not a syllable in the Bill of the degree of probability attending the <i>suspicion.</i> . . . Is it possible, Sir, to give more despotic powers to a bashaw of the Turkish <span class="star-pagination">*317</span> empire? What security is left for the devoted objects of this Bill against the malice of a prejudiced individual, a wicked magistrate . . . ?" The Speeches of Mr. Wilkes, p. 102.</p>
<p>These words and the complaints against which they were directed were will known on this side of the water. Hamilton wrote about "the practice of arbitrary imprisonments" which he denounced as "the favorite and most formidable instruments of tyranny." The Federalist No. 84. The writs of assistance, against which James Otis proclaimed,<sup>[4]</sup> were vicious in the same way as the general warrants, since they required no showing of "probable cause" before a magistrate, and since they allowed the police to search on suspicion and without "reasonable grounds" for believing that a crime had been or was being committed. Otis' protest was eloquent; but he lost the case. His speech, however, rallied public opinion. "Then and there," wrote John Adams, "the child Independence was born." 10 Life and Works of John Adams (1856), p. 248.</p>
<p>The attitude of Americans to arrests and searches on suspicion was also greatly influenced by the <i>lettres de cachet</i> extensively used in France.<sup>[5]</sup> This was an order emanating from the King and countersigned by a minister directing the seizure of a person for purposes of immediate imprisonment or exile. The ministers issued the <i>lettres</i> in an arbitrary manner, often at the request of the head of a noble family to punish a deviant son or relative. See Mirabeau, A Victim of the Lettres de Cachet, 3 Am. Hist. Rev. 19. One who was so arrested <span class="star-pagination">*318</span> might remain incarcerated indefinitely, as no legal process was available by which he could seek release. "Since the action of the government was secret, his friends might not know whither he had vanished, and he might even be ignorant of the cause of his arrest." 8 The Camb. Mod. Hist. 50. In the Eighteenth Century the practice arose of issuing the <i>lettres</i> in blank, the name to be filled in by the local mandatory. Thus the King could be told in 1770 "that no citizen of your realm is guaranteed against having his liberty sacrificed to revenge. For no one is great enough to be beyond the hate of some minister, nor small enough to be beyond the hate of some clerk." III Encyc. Soc. Sci. 138. As Blackstone wrote, ". . . if once it were left in the power of any, the highest, magistrate to imprison arbitrarily whomever he or his officers thought proper, (as in France it is daily practiced by the crown,) there would soon be an end of all other rights and immunities." I Commentaries (4th ed. Cooley) *135.</p>
<p>The Virginia Declaration of Rights, adopted June 12, 1776, included the forerunner of the Fourth Amendment:<sup>[6]</sup></p>
<blockquote>"That general warrants, whereby an officer or messenger may be commanded to search suspected places without evidence of a fact committed, or to seize any person or persons not named, or whose offence is not particularly described and <i>supported by evidence,</i> are grievous and oppressive, and ought not to be granted." (Italics added.)</blockquote>
<p>The requirement that a warrant of arrest be "supported by evidence" was by then deeply rooted in history. And it is inconceivable that in those days, when the right of <span class="star-pagination">*319</span> privacy was so greatly cherished, the mere word of an informersuch as we have in the present casewould be enough. For whispered charges and accusations, used in lieu of evidence of unlawful acts, were the main complaint of the age. <i>Frisbie</i> v. <i>Butler,</i> Kirby's Rep. (Conn.) 1785-1788, p. 213, decided in 1787, illustrates, I think, the mood of the day in the matter of arrests on suspicion. A warrant of arrest and search was issued by a justice of the peace on the oath of a citizen who had lost some pork from a cellar, the warrant stating, "said Butler suspects one Benjamin Frisbie, of Harwinton, to be the person that hath taken said pork." The court on appeal reversed the judgment of conviction, holding <i>inter alia</i> that the complaint "contained no direct charge of the theft, but only an averment that the defendant was suspected to be guilty." <i>Id.,</i> at 215. Nothing but suspicion is shown in the instant casesuspicion of an informer, not that of the arresting officers. Nor did they seek to obtain from the informer any information on which he based his belief. The arresting officers did not have a bit of <i>evidence</i> that the petitioner had committed or was committing a crime before the arrest. The only <i>evidence</i> of guilt was provided by the arrest itself.</p>
<p>When the Constitution was up for adoption, objections were made that it contained no Bill of Rights. And Patrick Henry was one who complained in particular that it contained no provision against arbitrary searches and seizures:</p>
<blockquote>". . . general warrants, by which an officer may search suspected places, without evidence of the commission of a fact, or seize any person without evidence of his crime, ought to be prohibited. As these are admitted, any man may be seized, any property may be taken, in the most arbitrary manner, without any evidence or reason. Every thing the most sacred <span class="star-pagination">*320</span> may be searched and ransacked by the strong hand of power. We have infinitely more reason to dread general warrants here than they have in England, because there, if a person be confined, liberty may be quickly obtained by the writ of <i>habeas corpus.</i> But here a man living many hundred miles from the judges may get in prison before he can get that writ." I Elliot's Debates 588.</blockquote>
<p>The determination that arrests and searches on mere suspicion would find no place in American law enforcement did not abate following the adoption of a Bill of Rights applicable to the Federal Government. In <i>Conner</i> v. <i>Commonwealth,</i> 3 Binn. (Pa.) 38, an arrest warrant issued by a magistrate stating his "strong reason to suspect" that the accused had committed a crime because of "common rumor and report" was held illegal under a constitutional provision identical in relevant part to the Fourth Amendment. "It is true, that by insisting on an oath, felons may sometimes escape. This must have been very well known to the framers of our constitution; but they thought it better that the guilty should sometimes escape, than that every individual should be subject to vexation and oppression." <i>Id.,</i> at 43-44. In <i>Grumon</i> v. <i>Raymond,</i> <span class="citation" data-id="6572959"><a href="/opinion/6693083/grumon-v-raymond/" aria-description="Citation for case: Grumon v. Raymond">1 Conn. 40</a></span>, the warrant stated that "several persons are suspected" of stealing some flour which is concealed in Hyatt's house or somewhere else, and ordered the constable to search Hyatt's house or other places and arrest the suspected persons if found with the flour. The court held the warrant void, stating it knew of "no such process as one to arrest all suspected persons, and bring them before a court for trial. It is an idea not to be endured for a moment." <span class="citation" data-id="6572959"><a href="/opinion/6693083/grumon-v-raymond/#44" aria-description="Citation for case: Grumon v. Raymond"><i>Id.,</i> at 44</a></span>. See also <i>Fisher</i> v. <i>McGirr,</i> <span class="citation no-link">1 Gray (Mass.) 1</span>; <i>Lippman</i> v. <i>People,</i> 175 III. 101, <span class="citation" data-id="6968164"><a href="/opinion/7064060/lippman-v-people/" aria-description="Citation for case: Lippman v. People">51 N. E. 872</a></span>; <i>Somerville</i> v. <i>Richards,</i> <span class="citation" data-id="7928685"><a href="/opinion/7976148/somerville-v-richards/" aria-description="Citation for case: Somerville v. Richards">37 Mich. 299</a></span>; <i>Commonwealth</i> v. <i>Dana,</i> 2 Metc. (Mass.) 329, 335-336.</p>
<p><span class="star-pagination">*321</span> It was against this long background that Professors Hogan and Snee of Georgetown University recently wrote:</p>
<blockquote>". . . it must be borne in mind that any arrest based on suspicion alone is illegal. This indisputable rule of law has grave implications for a number of traditional police investigative practices. The round-up or dragnet arrest, the arrest on suspicion, for questioning, for investigation or on an open charge all are prohibited by the law. It is undeniable that if those arrests were sanctioned by law, the police would be in a position to investigate a crime and to detect the real culprit much more easily, much more efficiently, much more economically, and with much more dispatch. It is equally true, however, that society cannot confer such power on the police without ripping away much of the fabric of a way of life which seeks to give the maximum of liberty to the individual citizen. The finger of suspicion is a long one. In an individual case it may point to all of a certain race, age group or locale. Commonly it extends to any who have committed similar crimes in the past. Arrest on mere suspicion collides violently with the basic human right of liberty. It can be tolerated only in a society which is willing to concede to its government powers which history and experience teach are the inevitable accoutrements of tyranny." 47 Geo. L. J. 1, 22.</blockquote>
<p>Down to this day our decisions have closely heeded that warning. So far as I can ascertain the mere word of an informer, not bolstered by some evidence<sup>[7]</sup> that a <span class="star-pagination">*322</span> crime had been or was being committed, has never been approved by this Court as "reasonable grounds" for making an arrest without a warrant. Whether the act complained of be seizure of goods, search of premises, or the arrest of the citizen, the judicial inquiry has been directed toward the reasonableness of inferences to be drawn from suspicious circumstances attending the action thought to be unlawful. Evidence required to prove guilt is not necessary. But the attendant circumstances must be sufficient to give rise in the mind of the arresting officer at least to inferences of guilt. <i>Locke</i> v. <i>United States,</i> <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">7 Cranch 339</a></span>; <i>The Thompson,</i> <span class="citation" data-id="87693"><a href="/opinion/87693/the-thompson/" aria-description="Citation for case: The Thompson">3 Wall. 155</a></span>; <i>Stacey</i> v. <i>Emery,</i> <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642</a></span>; <i>Director General</i> v. <i>Kastenbaum,</i> <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">263 U. S. 25</a></span>; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#159" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 159-162</a></span>; <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#591" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 591-592</a></span>; <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#165" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 165-171</a></span>.</p>
<p>The requirement that the arresting officer know some facts suggestive of guilt has been variously stated:</p>
<blockquote>"If the facts and circumstances before the officer are such as to warrant a man of prudence and caution in believing that the offense has been committed, it is sufficient." <i>Stacey</i> v. <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery"><i>Emery, supra,</i> at 645</a></span>.</blockquote>
<blockquote>". . . good faith is not enough to constitute probable cause. That faith must be grounded on facts within knowledge of the . . . agent, which in the judgment of the court would make his faith reasonable." <i>Director General</i> v. <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/#28" aria-description="Citation for case: Director General of Railroads v. Kastenbaum"><i>Kastenbaum, supra,</i> at 28</a></span>.</blockquote>
<p><span class="star-pagination">*323</span> Even when officers had information far more suggestive of guilt than the word of the informer used here, we have not sustained arrests without a warrant. In <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#16" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 16</a></span>, the arresting officer not only had an informer's tip but he actually smelled opium coming out of a room; and on breaking in found the accused. That arrest was held unlawful. Yet the smell of opium is far more tangible direct evidence than an unverified report that someone is going to commit a crime. And in <i>United States</i> v. <i>Di Re, supra</i><i>,</i> an arrest without a warrant of a man sitting in a car, where counterfeit coupons had been found passing between two men, was not justified in absence of any shred of evidence implicating the defendant, a third person. And see <i>Giacona</i> v. <i>State,</i> <span class="citation" data-id="9654188"><a href="/opinion/1570757/giacona-v-state/" aria-description="Citation for case: Giacona v. State">164 Tex. Cr. R. 325</a></span>, <span class="citation" data-id="9654188"><a href="/opinion/1570757/giacona-v-state/" aria-description="Citation for case: Giacona v. State">298 S. W. 2d 587</a></span>. Yet the evidence before those officers was more potent than the mere word of the informer involved in the present case.</p>
<p>The Court is quite correct in saying that proof of "reasonable grounds" for believing a crime was being committed need not be proof admissible at the trial. It could be inferences from suspicious acts, <i>e. g.,</i> consort with known peddlers, the surreptitious passing of a package, an intercepted message suggesting criminal activities, or any number of such events coming to the knowledge of the officer. See <i>People</i> v. <i>Rios,</i> <span class="citation" data-id="9627779"><a href="/opinion/1428463/people-v-rios/" aria-description="Citation for case: People v. Rios">46 Cal. 2d 297</a></span>, <span class="citation" data-id="9627779"><a href="/opinion/1428463/people-v-rios/" aria-description="Citation for case: People v. Rios">294 P. 2d 39</a></span>. But, if he takes the law into his own hands and does not seek the protection of a warrant, he must act on some evidence known to him.<sup>[8]</sup> The law goes for to protect <span class="star-pagination">*324</span> the citizen. Even suspicious acts observed by the officers may be as consistent with innocence as with guilt. That is not enough, for even the guilty may not be implicated on suspicion alone. <i>Baumboy</i> v. <i>United States,</i> <span class="citation" data-id="1496911"><a href="/opinion/1496911/baumboy-v-united-states/" aria-description="Citation for case: Baumboy v. United States">24 F. 2d 512</a></span>. The reason is, as I have said, that the standard set by the Constitution and by the statute is one that will protect both the officer and the citizen. For if the officer acts with "probable cause" or on "reasonable grounds," he is protected even though the citizen is innocent.<sup>[9]</sup> This important requirement should be strictly enforced, lest the whole process of arrest revert once more to whispered accusations by people. When we lower the guards as we do today, we risk making the role of the informerodious in our historyonce more supreme. I think the correct rule was stated in <i>Poldo</i> v. <i>United States,</i> <span class="citation" data-id="1565168"><a href="/opinion/1565168/poldo-v-united-states/#869" aria-description="Citation for case: Poldo v. United States">55 F. 2d 866, 869</a></span>. "Mere suspicion is not enough; there must be circumstances represented to the officers through the testimony of their senses sufficient to justify them in a good-faith belief that the defendant had violated the law."</p>
<p>Here the officers had no evidenceapart from the mere word of an informerthat petitioner was committing a crime. The fact that petitioner walked fast and carried a tan zipper bag was not evidence of any crime. The officers knew nothing except what they had been told by the informer. If they went to a magistrate to get a warrant of arrest and relied solely on the report of the informer, it is not conceivable to me that one would be granted. See <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span>. For they could not present to the magistrate any of the facts which the informer may have had. They could swear only to the fact that the informer had made the accusation. They could swear to no evidence that lay in their own knowledge. They could <span class="star-pagination">*325</span> present, on information and belief, no facts which the informer disclosed. No magistrate could issue a warrant on the mere word of an officer, without more.<sup>[10]</sup> See <i>Giordenello</i> v. <i>United States, supra</i><i>.</i> We are not justified in lowering the standard when an arrest is made without a warrant and allowing the officers more leeway than we grant the magistrate.</p>
<p>With all deference I think we break with tradition when we sustain this arrest. We said in <i>United States</i> v. <i>Di Re, supra,</i> at 595, ". . . a search is not to be made legal by what it turns up. In law it is good or bad when it starts and does not change character from its success." In this case it was only after the arrest and search were made that there was a shred of evidence known to the officers that a crime was in the process of being committed.<sup>[11]</sup></p>
<h2>NOTES</h2>
<p>[1]  The Fourth Amendment of the Constitution of the United States provides: "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>[2]  Hereford told Marsh that Draper was a Negro of light brown complexion, 27 years of age, 5 feet 8 inches tall, weighed about 160 pounds, and that he was wearing a light colored raincoat, brown slacks and black shoes.</p>
<p>[3]  The terms "probable cause" as used in the Fourth Amendment and "reasonable grounds" as used in § 104 (a) of the Narcotic Control Act, <span class="citation no-link">70 Stat. 570</span>, are substantial equivalents of the same meaning. <i>United States</i> v. <i>Walker,</i> <span class="citation" data-id="242778"><a href="/opinion/242778/the-united-states-of-america-v-farris-walker/#526" aria-description="Citation for case: The United States of America v. Farris Walker">246 F. 2d 519, 526</a></span> (C. A. 7th Cir.); cf. <i>United States</i> v. <i>Bianco,</i> <span class="citation" data-id="9442880"><a href="/opinion/227325/united-states-v-bianco/#720" aria-description="Citation for case: United States v. Bianco">189 F. 2d 716, 720</a></span> (C. A. 3d Cir.).</p>
<p>[4]  In <i>United States</i> v. <i>Heitner,</i> <span class="citation" data-id="1507600"><a href="/opinion/1507600/united-states-v-heitner/#106" aria-description="Citation for case: United States v. Heitner">149 F. 2d 105, 106</a></span> (C. A. 2d Cir.), Judge Learned Hand said "It is well settled that an arrest may be made upon hearsay evidence; and indeed, the `reasonable cause' necessary to support an arrest cannot demand the same strictness of proof as the accused's guilt upon a trial, unless the powers of peace officers are to be so cut down that they cannot possibly perform their duties."
</p>
<p><i>Grau</i> v. <i>United States,</i> <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/#128" aria-description="Citation for case: Grau v. United States">287 U. S. 124, 128</a></span>, contains a <i>dictum</i> that "A search warrant may issue only upon evidence which would be competent in the trial of the offense before a jury (<i>Giles</i> v. <i>United States,</i> <span class="citation" data-id="8827755"><a href="/opinion/8842552/giles-v-united-states/" aria-description="Citation for case: Giles v. United States">284 Fed. 208</a></span>; <i>Wagner</i> v. <i>United States,</i> 8 F. (2d) 581) . . . ." But the principles underlying that proposition were thoroughly discredited and rejected in <i>Brinegar</i> v. <i>United States, supra,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#172" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 172-174</a></span>, and notes 12 and 13. There are several cases in the federal courts that followed the now discredited <i>dictum</i> in the <i><span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">Grau</a></span></i> case, <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="1479874"><a href="/opinion/1479874/simmons-v-united-states/#88" aria-description="Citation for case: Simmons v. United States">18 F. 2d 85, 88</a></span>; <i>Worthington</i> v. <i>United States,</i> <span class="citation" data-id="1475726"><a href="/opinion/1475726/worthington-v-united-states/#564" aria-description="Citation for case: Worthington v. United States">166 F. 2d 557, 564-565</a></span>; cf. <i>Reeve</i> v. <i>Howe,</i> <span class="citation" data-id="1735465"><a href="/opinion/1735465/reeve-v-howe/#622" aria-description="Citation for case: Reeve v. Howe">33 F. Supp. 619, 622</a></span>; <i>United States</i> v. <i>Novero,</i> <span class="citation" data-id="1876453"><a href="/opinion/1876453/united-states-v-novero/#279" aria-description="Citation for case: United States v. Novero">58 F. Supp. 275, 279</a></span>, but the great weight of authority is the other way. See, <i>e. g., </i><i>Wrightson</i> v. <i>United States,</i> <span class="citation" data-id="240261"><a href="/opinion/240261/samuel-d-wrightson-jr-v-united-states/" aria-description="Citation for case: Samuel D. Wrightson, Jr. v. United States">236 F. 2d 672</a></span> (C. A. D. C. Cir.); <i>United States</i> v. <i><span class="citation" data-id="1507600"><a href="/opinion/1507600/united-states-v-heitner/" aria-description="Citation for case: United States v. Heitner">Heitner, supra</a></span></i> (C. A. 2d Cir.); <i>United States</i> v. <i>Bianco,</i> <span class="citation" data-id="9442880"><a href="/opinion/227325/united-states-v-bianco/" aria-description="Citation for case: United States v. Bianco">189 F. 2d 716</a></span> (C. A. 3d Cir.); <i>Wisniewski</i> v. <i>United States,</i> <span class="citation" data-id="1501475"><a href="/opinion/1501475/wisniewski-v-united-states/" aria-description="Citation for case: Wisniewski v. United States">47 F. 2d 825</a></span> (C. A. 6th Cir.); <i>United States</i> v. <i>Walker,</i> <span class="citation" data-id="242778"><a href="/opinion/242778/the-united-states-of-america-v-farris-walker/" aria-description="Citation for case: The United States of America v. Farris Walker">246 F. 2d 519</a></span> (C. A. 7th Cir.); <i>Mueller</i> v. <i>Powell,</i> <span class="citation" data-id="231565"><a href="/opinion/231565/mueller-v-powell/" aria-description="Citation for case: Mueller v. Powell">203 F. 2d 797</a></span> (C. A. 8th Cir.). And see Note, <span class="citation no-link">46 Harv. L. Rev. 1307</span>, 1310-1311, criticizing the <i>Grau dictum.</i></p>
<p>[5]  To the same effect are: <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/#700" aria-description="Citation for case: Husty v. United States">282 U. S. 694, 700-701</a></span>; <i>Dumbra</i> v. <i>United States,</i> <span class="citation" data-id="100685"><a href="/opinion/100685/dumbra-v-united-states/#441" aria-description="Citation for case: Dumbra v. United States">268 U. S. 435, 441</a></span>; <i>Steele</i> v. <i>United States No. 1,</i> <span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/#504" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498, 504-505</a></span>; <i>Stacey</i> v. <i>Emery,</i> <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span>; <i>Brinegar</i> v. <i>United States, supra,</i> at 175, 176.</p>
<p>[6]  <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 158</a></span>; <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>; <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#483" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 483</a></span>.</p>
<p>[1]  The Fourth Amendment provides:
</p>
<p>"The right of the people <i>to be secure in their persons,</i> houses, papers, and effects, <i>against unreasonable</i> searches and <i>seizures,</i> shall not be violated, and no Warrants shall issue, but <i>upon probable cause,</i> supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." (Italics added.)</p>
<p>[2]  The general warrant was declared illegal by the House of Commons in 1766. See 16 Hansard, Parl. Hist. Eng., 207.</p>
<p>[3]  The nameless general warrant was not the only vehicle for intruding on the privacy of the subjects without a valid basis for believing them guilty of offenses. In declaring illegal a warrant to search a plaintiff's house for evidence of libel, issued by the Secretary of State without any proof that the named accused was the author of the alleged libels, Lord Camden said, "we can safely say there is no law in this country to justify the defendants in what they have done; if there was, it would destroy all the comforts of society." <i>Entick</i> v. <i>Carrington,</i> 2 Wils. K. B. 275, 291.</p>
<p>[4]  See Quincy's Mass. Rep., 1761-1772, Appendix I, p. 469.</p>
<p>[5]  "Experience . . . has taught us that the power [to make arrests, searches and seizures] is one open to abuse. The most notable historical instance of it is that of lettres de cachet. Our Constitution was framed during the seethings of the French Revolution. The thought was to make lettres de cachet impossible with us." <i>United States</i> v. <i>Innelli,</i> <span class="citation" data-id="8828967"><a href="/opinion/8843746/united-states-v-innelli/" aria-description="Citation for case: United States v. Innelli">286 F. 731</a></span>.</p>
<p>[6]  See also Maryland Declaration of Rights (1776), Art. XXIII; Massachusetts Constitution (1780), Part First, Art. XIV; New Hampshire Constitution (1784), Part I, Art. XIX; North Carolina Declaration of Rights (1776), Art. XI; Pennsylvania Constitution (1776), Art. X.</p>
<p>[7]  Hale, who traced the evolution of arrests without warrants in The History of the Pleas of the Crown (1st Am. ed. 1847), states that while officers need at times to act on information from others, they must make that information, so far as they can, their own. He puts a case where A, suspecting B "on reasonable grounds" of being a felon, asks an officer to arrest B. The duty of the officer was stated as follows:
</p>
<p>"He ought to inquire and examine the circumstances and causes of the suspicion of <i>A.</i> which tho he cannot do it upon oath, yet such an information may carry over the suspicion even to the constable, whereby it may become his suspicion as well as the suspicion of <i>A.</i>" <i>Id.,</i> at 91.</p>
<p>[8]  <i>United States</i> v. <i>Heitner,</i> <span class="citation" data-id="1507600"><a href="/opinion/1507600/united-states-v-heitner/#106" aria-description="Citation for case: United States v. Heitner">149 F. 2d 105, 106</a></span>, that says an arrest may be made "upon hearsay evidence" was a case where the arrest was made after the defendant on seeing the officers tried to get away. Our cases cited by that court in support of the use of hearsay were <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>; <i>Dumbra</i> v. <i>United States,</i> <span class="citation" data-id="100685"><a href="/opinion/100685/dumbra-v-united-states/" aria-description="Citation for case: Dumbra v. United States">268 U. S. 435</a></span>; and <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span>. But each of them was a case where the information on which the arrest was made, though perhaps not competent at the trial, was known to the arresting officer.</p>
<p>[9]  <i>Maghan</i> v. <i>Jerome,</i> 67 App. D. C. 9, <span class="citation" data-id="1511010"><a href="/opinion/1511010/maghan-v-jerome/" aria-description="Citation for case: Maghan v. Jerome">88 F. 2d 1001</a></span>; <i>Pritchett</i> v. <i>Sullivan,</i> <span class="citation" data-id="8776690"><a href="/opinion/8792689/pritchett-v-sullivan/" aria-description="Citation for case: Pritchett v. Sullivan">182 F. 480</a></span>. See <i>Ravenscroft</i> v. <i>Casey,</i> <span class="citation" data-id="1568274"><a href="/opinion/1568274/ravenscroft-v-casey/" aria-description="Citation for case: Ravenscroft v. Casey">139 F. 2d 776</a></span>.</p>
<p>[10]  See <i>State</i> v. <i>Gleason,</i> <span class="citation" data-id="7886313"><a href="/opinion/7935867/state-v-gleason/" aria-description="Citation for case: State v. Gleason">32 Kan. 245</a></span>, <span class="citation no-link">4 P. 363</span>; <i>State</i> v. <i>Smith,</i> <span class="citation no-link">262 S. W. 65</span> (Mo. App.), arising under state constitutions having provisions comparable to our Fourth Amendment.</p>
<p>[11]  The Supreme Court of South Carolina has said:
</p>
<p>"Some things are to be more deplored than the unlawful transportation of whiskey; one is the loss of liberty. Common as the event may be, it is a serious thing to arrest a citizen, and it is a more serious thing to search his person; and he who accomplishes it, must do so in conformity to the laws of the land. There are two reasons for this: one to avoid bloodshed, and the other to preserve the liberty of the citizen. Obedience to law is the bond of society, and the officers set to enforce the law are not exempt from its mandates.</p>
<p>"In the instant case the possession of the liquor was the body of the offense; that fact was proven by a forcible and unlawful search of the defendant's person to secure the veritable key to the offense. It is fundamental that a citizen may not be arrested and have his person searched by force and without process in order to secure testimony against him. . . . It is better that the guilty shall escape, rather than another offense shall be committed in the proof of guilt." <i>Town of Blacksburg</i> v. <i>Beam,</i> 104 S. C. 146, 148, <span class="citation" data-id="3880639"><a href="/opinion/4119711/town-of-blacksburg-v-beam/" aria-description="Citation for case: Town of Blacksburg v. Beam">88 S. E. 441</a></span>.</p>

</div>
```

---
