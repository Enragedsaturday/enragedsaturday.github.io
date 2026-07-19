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

## GROUP: content/cases/Michigan v. Thomas.md  (`case`, 5 assertions)

### content_page

```
---
title: "Michigan v. Thomas"
type: case
citation: "458 U.S. 259 (1982)"
parallel_cite: "102 S. Ct. 3079; 73 L. Ed. 2d 750; 50 U.S.L.W. 3998"
neutral_cite: 1982 U.S. LEXIS 145
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1982
date_decided: 1982-06-28
docket: 81-593
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1982-06-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Thomas
  varies_by_point: false
  scope_note: "Per curiam. Reaffirmed by the Court's later auto-exception cases (e.g., Maryland v. Dyson)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110776/michigan-v-thomas/"
  cluster_id: 110776
  opinion_id: 110776
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Chambers v. Maroney]]", "[[United States v. Ross]]", "[[South Dakota v. Opperman]]", "[[Maryland v. Dyson]]", "[[California v. Carney]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "impound", "station-house", "no-exigency", "probable-cause"]
holding: "The automobile exception permits a warrantless search of an impounded car at the station on probable cause; the justification does not vanish once the car is immobilized and no separate showing of exigency is required."
lake:
  record_id: Michigan v. Thomas
  status: verified
  projected_at: 2026-07-06
---

# Michigan v. Thomas

*458 U.S. 259 (1982)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers stopped a car for a turn-signal violation, arrested the front-seat passenger (the respondent and owner) for possessing open intoxicants, and called a truck to tow the car. Conducting an inventory before towing, an officer found marijuana in the unlocked glove compartment; a more thorough search then turned up a loaded revolver hidden behind the dashboard air vents. The Michigan Court of Appeals held the warrantless search unreasonable because, with the car and occupants already in custody, there were no "exigent circumstances."

## Issue
Whether, once an officer has probable cause to believe a lawfully stopped and impounded car contains contraband, a warrantless search of the car is barred by the absence of separate "exigent circumstances."

## Rule
No. Restating *[[Chambers v. Maroney]]*: "when police officers have probable cause to believe there is contraband inside an automobile that has been stopped on the road, the officers may conduct a warrantless search of the vehicle, even after it has been impounded and is in police custody." — 458 U.S. at 261. ^pin-261

And no separate [[Exigent Circumstances and Hot Pursuit|exigency]] need be shown: "It is thus clear that the justification to conduct such a warrantless search does not vanish once the car has been immobilized; nor does it depend upon a reviewing court's assessment of the likelihood in each particular case that the car would have been driven away, or that its contents would have been tampered with, during the period required for the police to obtain a warrant." — *Id.* ^pin-261a

## Application
The inventory of the glove compartment lawfully turned up marijuana, which the State contended gave probable cause to believe contraband was hidden elsewhere in the car. The Court of Appeals did not refute that probable cause; it held only that, absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], a warrant was required. That holding was "plainly inconsistent" with *[[Chambers v. Maroney|Chambers]]* and *Texas v. White*: with probable cause established, the officers could search the immobilized car without a warrant and without proving any further [[Exigent Circumstances and Hot Pursuit|exigency]].

## Conclusion
Reversed. Probable cause supports a warrantless search of an impounded car under the automobile exception; the lack of separate [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] does not defeat it.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Thomas* is part of the line — [[Chambers v. Maroney]] forward — that the Court later distilled into the flat rule that the automobile exception "has no separate exigency requirement" in [[Maryland v. Dyson]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Michigan v. Thomas*, 458 U.S. 259 (1982) — https://www.courtlistener.com/opinion/110776/michigan-v-thomas/ — pinpoint: 261.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2775415e76c7c30e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "458 U.S. 259 (1982)", "court": "U.S. Supreme Court", "neutral_cite": "1982 U.S. LEXIS 145", "official_citation_present": true, "parallel_cite": "102 S. Ct. 3079; 73 L. Ed. 2d 750; 50 U.S.L.W. 3998", "title": "Michigan v. Thomas", "year": "1982"}}
{"assertion_id": "50335c748e6073dd", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "Michigan v. Thomas"}}
{"assertion_id": "81225e6cbb6623d6", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The automobile exception permits a warrantless search of an impounded car at the station on probable cause; the justification does not vanish once the car is immobilized and no separate showing of exigency is required.", "title": "Michigan v. Thomas"}}
{"assertion_id": "c81002b189bb715c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Thomas"}}
{"assertion_id": "e261dea63eb08cdd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1982-06-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Thomas", "field_i_validity": "good_law", "scope_note": "Per curiam. Reaffirmed by the Court's later auto-exception cases (e.g., Maryland v. Dyson).", "title": "Michigan v. Thomas", "varies_by_point": "false"}}
```

### lake record — Michigan v. Thomas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Thomas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Thomas",
    "case_name_short": "Thomas",
    "case_name_full": "Michigan v. Thomas",
    "input_case_name": "Michigan v. Thomas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1982-06-28",
    "year": 1982,
    "docket": "81-593",
    "cluster_id": 110776,
    "lead_opinion_id": 110776,
    "sibling_ids": [
      110776
    ],
    "absolute_url": "/opinion/110776/michigan-v-thomas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "458 U.S. 259",
      "volume": "458",
      "reporter": "U.S.",
      "page": "259",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "102 S. Ct. 3079",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "3079",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 750",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "750",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 U.S.L.W. 3998",
        "volume": "50",
        "reporter": "U.S.L.W.",
        "page": "3998",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1982 U.S. LEXIS 145",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "145",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "458 U.S. 259",
        "volume": "458",
        "reporter": "U.S.",
        "page": "259",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 S. Ct. 3079",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "3079",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 750",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "750",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1982 U.S. LEXIS 145",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "145",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 U.S.L.W. 3998",
        "volume": "50",
        "reporter": "U.S.L.W.",
        "page": "3998",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "458 U.S. 259",
    "official_selection": {
      "court_class": "scotus",
      "selected": "458 U.S. 259",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-261",
      "page": null,
      "quote": "## Rule No. Restating *Chambers v. Maroney*:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-261a",
      "page": null,
      "quote": "It is thus clear that the justification to conduct such a warrantless search does not vanish once the car has been immobilized; nor does it depend upon a reviewing court's assessment of the likelihood in each particular case that the car would have been driven away, or that its contents would have been tampered with, during the period required for the police to obtain a warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1982-06-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Thomas",
    "varies_by_point": false,
    "scope_note": "Per curiam. Reaffirmed by the Court's later auto-exception cases (e.g., Maryland v. Dyson).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Allen Robert Allensworth",
          "cluster_id": 4472786,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Blevins v. State",
          "cluster_id": 1384203,
          "cite": [
            "74 S.W.3d 125",
            "2002 WL 535490"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Trudeau",
          "cluster_id": 1907869,
          "cite": [
            "683 A.2d 725",
            "165 Vt. 355",
            "1996 Vt. LEXIS 82"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Keith Rudolph Ludwig, National Association of Criminal Defense Lawyers, Amicus Curiae",
          "cluster_id": 658364,
          "cite": [
            "10 F.3d 1523"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kye Soo Lee, Min Ho Chay, and Min Sik Lee",
          "cluster_id": 582583,
          "cite": [
            "962 F.2d 430"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Manuel Parrado and Elfobaldo Rodriguez",
          "cluster_id": 546976,
          "cite": [
            "911 F.2d 1567",
            "1990 U.S. App. LEXIS 16500",
            "1990 WL 126641"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 2412816,
          "cite": [
            "780 S.W.2d 497",
            "1989 WL 137646"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williams",
          "cluster_id": 3990817,
          "cite": [
            "561 N.E.2d 1038",
            "54 Ohio App. 3d 117",
            "1988 Ohio App. LEXIS 4386"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kelley v. State",
          "cluster_id": 2468256,
          "cite": [
            "677 S.W.2d 34",
            "1984 Tex. Crim. App. LEXIS 737"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williams",
          "cluster_id": 1513883,
          "cite": [
            "654 S.W.2d 238",
            "1983 Mo. App. LEXIS 4002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Panah",
          "cluster_id": 2509294,
          "cite": [
            "107 P.3d 790",
            "25 Cal. Rptr. 3d 672",
            "35 Cal. 4th 395",
            "2005 Cal. Daily Op. Serv. 2194",
            "2005 Daily Journal DAR 3023",
            "2005 Cal. LEXIS 2712"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johns",
          "cluster_id": 111305,
          "cite": [
            "83 L. Ed. 2d 890",
            "105 S. Ct. 881",
            "469 U.S. 478",
            "1985 U.S. LEXIS 45",
            "53 U.S.L.W. 4126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rocha",
          "cluster_id": 4345763,
          "cite": [
            "295 Neb. 716",
            "890 N.W.2d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Denny Ray Hunnicutt",
          "cluster_id": 751593,
          "cite": [
            "135 F.3d 1345",
            "1998 Colo. J. C.A.R. 962",
            "1998 U.S. App. LEXIS 1763",
            "1998 WL 48805"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guzman",
          "cluster_id": 1785574,
          "cite": [
            "959 S.W.2d 631",
            "1998 Tex. Crim. App. LEXIS 12",
            "1998 WL 28103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Willie Kincaide (96-1771), Christian R. Key (96-1915), Keith Elbert Riley (96-1772)",
          "cluster_id": 754758,
          "cite": [
            "145 F.3d 771"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Albert Thomas (92-4344) and Angelique Dupree (93-3026)",
          "cluster_id": 658579,
          "cite": [
            "11 F.3d 620",
            "1993 U.S. App. LEXIS 32262",
            "1993 WL 513330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Pace, Anthony Besase, Christ Savides, Donald Smith, John Cialoni, and Robert Wilson",
          "cluster_id": 538544,
          "cite": [
            "898 F.2d 1218",
            "1990 U.S. App. LEXIS 3831"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Amador Rodriguez Chaidez, A/K/A Rodriguez Amador Chaidez and Amador Rodriguez",
          "cluster_id": 543654,
          "cite": [
            "906 F.2d 377",
            "1990 U.S. App. LEXIS 11006",
            "1990 WL 88172"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Glen Shaw",
          "cluster_id": 415225,
          "cite": [
            "701 F.2d 367",
            "1983 U.S. App. LEXIS 29636",
            "12 Fed. R. Serv. 1566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony E. Anderson",
          "cluster_id": 741175,
          "cite": [
            "114 F.3d 1059",
            "1997 U.S. App. LEXIS 12598",
            "1997 WL 287031"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Meyers",
          "cluster_id": 111157,
          "cite": [
            "80 L. Ed. 2d 381",
            "104 S. Ct. 1852",
            "466 U.S. 380",
            "1984 U.S. LEXIS 66",
            "52 U.S.L.W. 3774"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Burgess",
          "cluster_id": 172511,
          "cite": [
            "576 F.3d 1078",
            "80 Fed. R. Serv. 344",
            "2009 U.S. App. LEXIS 17823",
            "2009 WL 2436674"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Solomon Philip Panitz, United States of America v. Andrew Stewart Baumwald",
          "cluster_id": 544607,
          "cite": [
            "907 F.2d 1267",
            "1990 U.S. App. LEXIS 11808"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lacey Lee Koenig and Lee Graf",
          "cluster_id": 511637,
          "cite": [
            "856 F.2d 843",
            "1988 U.S. App. LEXIS 12655",
            "1988 WL 93655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Darren Eugene Henderson",
          "cluster_id": 772238,
          "cite": [
            "241 F.3d 638"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimmy Lee Nixon, Richard Nixon, Michael Parks, Emmitt Lamar Manns, Henry L. Manns, Michael Keeley, Gerald Wells",
          "cluster_id": 551365,
          "cite": [
            "918 F.2d 895",
            "31 Fed. R. Serv. 920",
            "1990 U.S. App. LEXIS 20987"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard Lee Hatfield",
          "cluster_id": 486411,
          "cite": [
            "815 F.2d 1068",
            "1987 U.S. App. LEXIS 4273"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Badgett",
          "cluster_id": 7892532,
          "cite": [
            "200 Conn. 412",
            "512 A.2d 160",
            "1986 Conn. LEXIS 878"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Billy Ray Rowland",
          "cluster_id": 783350,
          "cite": [
            "341 F.3d 774",
            "2003 WL 22047799"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kelly",
          "cluster_id": 1031354,
          "cite": [
            "592 F.3d 586",
            "2010 U.S. App. LEXIS 1925",
            "2010 WL 322200"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Horace Chavis, (Two Cases) United States of America v. Clement Chavis",
          "cluster_id": 526753,
          "cite": [
            "880 F.2d 788",
            "1989 U.S. App. LEXIS 10676"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Walter George Strickland, Jr.",
          "cluster_id": 540933,
          "cite": [
            "902 F.2d 937",
            "1990 U.S. App. LEXIS 8825",
            "1990 WL 64575"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Thomas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110776) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 179,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 10,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 179,
        "triage_read": 12,
        "triage_snippet_classified": 167
      },
      "lane2_top_cited": {
        "query": "cites:(110776)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NSZzPTE2MTM5OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110776%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110776)",
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
    "complete_query": "cites:(110776)",
    "indexed_citing_opinions": 246,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110776,
        "count": 246,
        "count_source": "search"
      }
    ],
    "citation_count": 390,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-thomas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU2OTc2ODImcz02MjM5MzIyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110776%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110776,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110776,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110776,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110776,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110776,
        "cited_id": 1853732,
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
    "date_created": "2026-07-05T13:41:40Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:41:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:41:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:45:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:41:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Thomas

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b297-10">
  Per Curiam.
 </author>
<p id="b297-11">
  While respondent was the front-seat passenger in an automobile, the car was stopped for failing to signal a left turn. As two police officers approached the vehicle, they saw respondent bend forward so that his head was at or below the level of the dashboard. The officers then observed an open bottle of malt liquor standing upright on the floorboard between respondent’s feet, and placed respondent under arrest for possession of open intoxicants in a motor vehicle. The 14-year-old driver was issued a citation for not having a driver’s license. Respondent claimed ownership of the car.
 </p>
<p id="b298-4">
<span citation-index="1" class="star-pagination" label="260"> 
   *260
   </span>
  Respondent and the driver were taken to the patrol car, and a truck was called to tow respondent’s automobile. One of the officers searched the vehicle, pursuant to a departmental policy that impounded vehicles be searched prior to being towed. The officer found two bags of marihuana in the unlocked glove compartment.. The second officer then searched the car more thoroughly, checking under the front seat, under the dashboard, and inside the locked trunk. Opening the air vents under the dashboard, the officer discovered a loaded, .38-caliber revolver inside.
 </p>
<p id="b298-5">
  Respondent was convicted of possession of a concealed weapon. He moved for a new trial, contending that the revolver was taken from his car pursuant to an illegal search and seizure; the trial court denied the motion.
 </p>
<p id="b298-6">
  The Michigan Court of Appeals reversed, holding that the warrantless search of respondent’s automobile violated the Fourth Amendment. <span class="citation" data-id="9689038"><a href="/opinion/1853732/people-v-thomas/" aria-description="Citation for case: People v. Thomas">106 Mich. App. 601</a></span>, <span class="citation" data-id="9689038"><a href="/opinion/1853732/people-v-thomas/" aria-description="Citation for case: People v. Thomas">308 N. W. 2d 170</a></span> (1981). The court acknowledged that in
  <em>
   South Dakota
  </em>
  v. Opperman, <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976), this Court upheld the validity of warrantless inventory searches of impounded motor vehicles. Moreover, the court found that, since respondent had been placed under arrest and the other occupant of the car was too young to legally drive, it was proper for the officers to impound the vehicle and to conduct an inventory search prior to its being towed. However, in the view of the Court of Appeals, the search conducted in this case was “unreasonable in scope,” because it extended to the air vents which, unlike the glove compartment or the trunk, were not a likely place for the storage of valuables or personal possessions. <span class="citation" data-id="9689038"><a href="/opinion/1853732/people-v-thomas/#606" aria-description="Citation for case: People v. Thomas">106 Mich. App., at 606</a></span>, <span class="citation" data-id="9689038"><a href="/opinion/1853732/people-v-thomas/#172" aria-description="Citation for case: People v. Thomas">308 N. W. 2d, at 172</a></span>.
 </p>
<p id="b298-7">
  The Court of Appeals also rejected the State’s contention that the scope of the inventory search was properly expanded when the officers discovered contraband in the glove compartment. The court concluded that, because both the car and its occupants were already in police custody, there were
  <span citation-index="1" class="star-pagination" label="261"> 
   *261
   </span>
  no “exigent circumstances” justifying a warrantless search for contraband.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b299-5">
  We reverse. In
  <em>
   Chambers
  </em>
  v.
  <em>
   Maroney,
  </em>
  <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), we held that when police officers have probable cause to believe there is contraband inside an automobile that has been stopped on the road, the officers may conduct a warrantless search of the vehicle, even after it has been impounded and is in police custody. We firmly reiterated this holding in
  <em>
   Texas
  </em>
  v.
  <em>
   White,
  </em>
  <span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">423 U. S. 67</a></span> (1975). See also
  <em>
   United States
  </em>
  v.
  <em>
   Ross,
  </em>
  <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#807" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 807, n. 9</a></span> (1982). It is thus clear that the justification to conduct such a warrantless search does not vanish once the car has been immobilized; nor does it depend upon a reviewing court’s assessment of the likelihood in each particular case that the car would have been driven away, or that its contents would have been tampered with, during the period required for the police to obtain a warrant.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
<em>
   See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">ibid.</a></span>
  </em>
</p>
<p id="b299-6">
  Here, the Court of Appeals recognized that the officers were justified in conducting an inventory search of the car’s
  <span citation-index="1" class="star-pagination" label="262"> 
   *262
   </span>
  glove compartment, which led to the discovery of contraband. Without attempting to refute the State’s contention that this discovery gave the officers probable cause to believe there was contraband elsewhere in the vehicle, the Court of Appeals held that the absence of “exigent circumstances” precluded a warrantless search. This holding is plainly inconsistent with our decisions in
  <em>
   <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>
  </em>
  and
  <em>
   Texas
  </em>
  v.
  <em>
   <span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">White</a></span>.
  </em>
</p>
<p id="b300-5">
  The petition for certiorari and the motion of respondent to proceed
  <em>
   informa pauperis
  </em>
  are granted, the judgment of the Michigan Court of Appeals is reversed, and the case is remanded to that court for further proceedings not inconsistent with this opinion.
 </p>
<p id="b300-6">
<em>
   It is so ordered.
  </em>
</p>
<judges id="b300-7">
  Justice Brennan and Justice Marshall would grant the petition for a writ of certiorari and set the case for oral argument.
 </judges>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b299-7">
   The Court of Appeals did not directly address the State’s contention that the discovery of marihuana in the glove compartment provided probable cause to believe there was contraband hidden elsewhere in the vehicle. However, the court apparently assumed that the officers possessed information sufficient to support issuance of a warrant to search the automobile; the court’s holding was that the officers were required to obtain such a warrant, and could not search on the basis of probable cause alone. See <span class="citation" data-id="9689038"><a href="/opinion/1853732/people-v-thomas/#606" aria-description="Citation for case: People v. Thomas">106 Mich. App., at 606-608</a></span>, <span class="citation" data-id="9689038"><a href="/opinion/1853732/people-v-thomas/#172" aria-description="Citation for case: People v. Thomas">308 N. W. 2d, at 172-173</a></span>.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b299-8">
   Even were some demonstrable “exigency” a necessary predicate to such a search, we would find somewhat curious the Court of Appeals’ conclusion that no “exigent circumstances” were present in this case. Unlike the searches involved in
   <em>
    Chambers
   </em>
   v.
   <em>
    Maroney,
   </em>
   <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), and
   <em>
    Texas
   </em>
   v.
   <em>
    White,
   </em>
   <span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">423 U. S. 67</a></span> (1975) — which were conducted at the station house — the search at issue here was conducted on the roadside, before the car had been towed. As pointed out by Judge Deneweth, in dissent, “there was a clear possibility that the occupants of the vehicle could have had unknown confederates who would return to remove the secreted contraband.” <span class="citation" data-id="9689038"><a href="/opinion/1853732/people-v-thomas/#609" aria-description="Citation for case: People v. Thomas">106 Mich. App., at 609</a></span>, <span class="citation" data-id="9689038"><a href="/opinion/1853732/people-v-thomas/#174" aria-description="Citation for case: People v. Thomas">308 N. W. 2d, at 174</a></span>.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Michigan v. Tucker.md  (`case`, 5 assertions)

### content_page

```
---
title: "Michigan v. Tucker"
type: case
citation: "417 U.S. 433 (1974)"
parallel_cite: "94 S. Ct. 2357; 41 L. Ed. 2d 182"
neutral_cite: 1974 U.S. LEXIS 71
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-06-10
docket: 73-482
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Tucker
  varies_by_point: false
  scope_note: "Dickerson v. United States (2000) reaffirmed Miranda's constitutional status, but the Tucker fruits principle survives and was applied in United States v. Patane (2004)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109063/michigan-v-tucker/"
  cluster_id: 109063
  opinion_id: 9425753
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[United States v. Patane]]", "[[Oregon v. Elstad]]", "[[Dickerson v. United States]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "fruits", "prophylactic-rule"]
holding: "The 'fruits' of a mere prophylactic Miranda violation — here, a witness whose identity was learned from a statement taken with incomplete warnings — need not be suppressed where the statement was voluntary and not actually compelled; a Miranda procedural lapse is not itself a Fifth Amendment violation."
lake:
  record_id: Michigan v. Tucker
  status: verified
  projected_at: 2026-07-06
---

# Michigan v. Tucker

*417 U.S. 433 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Before *[[Miranda v. Arizona|Miranda]]* was decided, but tried afterward, Tucker was questioned about a rape. Police advised him of some rights but did not tell him a lawyer would be appointed if he could not afford one. Tucker gave an alibi naming a friend, Henderson; when contacted, Henderson's account instead incriminated Tucker. Tucker's own statements were suppressed under *[[Miranda v. Arizona|Miranda]]*, but the prosecution called Henderson as a witness, whose identity had been learned only through Tucker's incompletely warned statement.

## Issue
Whether the testimony of a witness whose identity was discovered through a statement taken in violation of *[[Miranda v. Arizona|Miranda]]*'s warning requirements — but given without actual compulsion — must be excluded as a "fruit" of the *[[Miranda v. Arizona|Miranda]]* violation.

## Rule
No. A failure to give the full *[[Miranda v. Arizona|Miranda]]* warnings, without more, is not itself a violation of the Fifth Amendment; it is a departure from prophylactic safeguards. "[T]he police conduct at issue here did not abridge respondent's constitutional privilege against compulsory self-incrimination, but departed only from the prophylactic standards later laid down by this Court in *Miranda* to safeguard that privilege." — 417 U.S. at 446. ^pin-446

Because there was no compulsion in the constitutional sense, there was no fixed rule (as in *[[Wong Sun v. United States|Wong Sun]]* for Fourth Amendment violations) requiring suppression of derivative evidence. Weighing deterrence against the cost of losing reliable third-party testimony, the Court held the witness's testimony was properly admitted.

## Application
Tucker's statement naming Henderson was voluntary; the only defect was the incomplete warning about appointed counsel. Since the privilege itself was not violated, the witness Henderson — though found via that statement — was not a poisoned fruit that had to be excluded. Suppressing his live testimony would do little to deter and would cost the truth-seeking process reliable evidence, so it was admissible.

## Conclusion
The witness's testimony was admissible; the Sixth Circuit's contrary judgment was reversed. *[[Miranda v. Arizona|Miranda]]*'s warning rules are prophylactic, so the strict fruit-of-the-poisonous-tree doctrine does not automatically reach evidence derived from a voluntary but unwarned statement.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- [[Dickerson v. United States]] later held *[[Miranda v. Arizona|Miranda]]* is constitutionally based and cannot be overruled by statute, but the *Tucker* fruits principle endures: a voluntary statement's physical or testimonial fruits are not suppressed for a bare *[[Miranda v. Arizona|Miranda]]* lapse — applied in [[United States v. Patane]] and consistent with [[Oregon v. Elstad]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Michigan v. Tucker*, 417 U.S. 433 (1974) — https://www.courtlistener.com/opinion/109063/michigan-v-tucker/ — pinpoint: 446.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dfeaff068f6fa8de", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "417 U.S. 433 (1974)", "court": "U.S. Supreme Court", "neutral_cite": "1974 U.S. LEXIS 71", "official_citation_present": true, "parallel_cite": "94 S. Ct. 2357; 41 L. Ed. 2d 182", "title": "Michigan v. Tucker", "year": "1974"}}
{"assertion_id": "953d3862e0742288", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny", "title": "Michigan v. Tucker"}}
{"assertion_id": "c0c44c9efbccd2cc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The 'fruits' of a mere prophylactic Miranda violation — here, a witness whose identity was learned from a statement taken with incomplete warnings — need not be suppressed where the statement was voluntary and not actually compelled; a Miranda procedural lapse is not itself a Fifth Amendment violation.", "title": "Michigan v. Tucker"}}
{"assertion_id": "6a36474b574bbfdc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Tucker"}}
{"assertion_id": "f9509c44fb8ab1de", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1974-06-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Tucker", "field_i_validity": "good_law", "scope_note": "Dickerson v. United States (2000) reaffirmed Miranda's constitutional status, but the Tucker fruits principle survives and was applied in United States v. Patane (2004).", "title": "Michigan v. Tucker", "varies_by_point": "false"}}
```

### lake record — Michigan v. Tucker

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Tucker",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Tucker",
    "case_name_short": "Tucker",
    "case_name_full": "Michigan v. Tucker",
    "input_case_name": "Michigan v. Tucker",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-06-10",
    "year": 1974,
    "docket": "73-482",
    "cluster_id": 109063,
    "lead_opinion_id": 9425753,
    "sibling_ids": [
      109063,
      9425753,
      9425754,
      9425755
    ],
    "absolute_url": "/opinion/109063/michigan-v-tucker/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8997318,
        "score": 20,
        "case_name": "Michigan v. Tucker"
      },
      {
        "cluster_id": 8997041,
        "score": 20,
        "case_name": "Michigan v. Tucker"
      },
      {
        "cluster_id": 8996752,
        "score": 20,
        "case_name": "Michigan v. Tucker"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "417 U.S. 433",
      "volume": "417",
      "reporter": "U.S.",
      "page": "433",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 2357",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "2357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "41 L. Ed. 2d 182",
        "volume": "41",
        "reporter": "L. Ed. 2d",
        "page": "182",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 71",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "71",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "417 U.S. 433",
        "volume": "417",
        "reporter": "U.S.",
        "page": "433",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 2357",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "2357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "41 L. Ed. 2d 182",
        "volume": "41",
        "reporter": "L. Ed. 2d",
        "page": "182",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 71",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "71",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "417 U.S. 433",
    "official_selection": {
      "court_class": "scotus",
      "selected": "417 U.S. 433",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-446",
      "page": null,
      "quote": "of the *Miranda* violation. ## Rule No. A failure to give the full *Miranda* warnings, without more, is not itself a violation of the Fifth Amendment; it is a departure from prophylactic safeguards.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Tucker",
    "varies_by_point": false,
    "scope_note": "Dickerson v. United States (2000) reaffirmed Miranda's constitutional status, but the Tucker fruits principle survives and was applied in United States v. Patane (2004).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cruz, Adelfo Ramirez",
          "cluster_id": 2950538,
          "cite": [
            "461 S.W.3d 531",
            "2015 Tex. Crim. App. LEXIS 561",
            "2015 WL 2236982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fernandez-Torres \u2013 (",
          "cluster_id": 2745409,
          "cite": [
            "50 Kan. App. 2d 1069",
            "337 P.3d 691"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Simon",
          "cluster_id": 2483876,
          "cite": [
            "456 Mass. 280",
            "923 N.E.2d 58",
            "2010 Mass. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Damon Kimbrough",
          "cluster_id": 796843,
          "cite": [
            "477 F.3d 144",
            "2007 U.S. App. LEXIS 3488",
            "2007 WL 495026"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James David Nichols, United States of America v. James David Nichols",
          "cluster_id": 793364,
          "cite": [
            "438 F.3d 437",
            "2006 WL 464130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane1_negative"
      },
      {
        "citing_case": {
          "name": "in the Matter of H v.",
          "cluster_id": 2847659,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane1_negative"
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
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doyle v. Ohio",
          "cluster_id": 109491,
          "cite": [
            "49 L. Ed. 2d 91",
            "96 S. Ct. 2240",
            "426 U.S. 610",
            "1976 U.S. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Elstad",
          "cluster_id": 111364,
          "cite": [
            "84 L. Ed. 2d 222",
            "105 S. Ct. 1285",
            "470 U.S. 298",
            "1985 U.S. LEXIS 60",
            "53 U.S.L.W. 4244"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fare v. Michael C.",
          "cluster_id": 110117,
          "cite": [
            "61 L. Ed. 2d 197",
            "99 S. Ct. 2560",
            "442 U.S. 707",
            "1979 U.S. LEXIS 133"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andresen v. Maryland",
          "cluster_id": 109522,
          "cite": [
            "49 L. Ed. 2d 627",
            "96 S. Ct. 2737",
            "427 U.S. 463",
            "1976 U.S. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leday v. State",
          "cluster_id": 1678149,
          "cite": [
            "983 S.W.2d 713",
            "1998 Tex. Crim. App. LEXIS 172",
            "1998 WL 870371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Michigan",
          "cluster_id": 145646,
          "cite": [
            "165 L. Ed. 2d 56",
            "126 S. Ct. 2159",
            "547 U.S. 586",
            "2006 U.S. LEXIS 4677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Waidla",
          "cluster_id": 1316339,
          "cite": [
            "996 P.2d 46",
            "94 Cal. Rptr. 2d 396",
            "22 Cal. 4th 690",
            "22 Cal. 690",
            "2000 Daily Journal DAR 3605",
            "2000 Cal. Daily Op. Serv. 2687",
            "2000 Cal. LEXIS 2229"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 110754,
          "cite": [
            "73 L. Ed. 2d 202",
            "102 S. Ct. 2579",
            "457 U.S. 537",
            "1982 U.S. LEXIS 134",
            "50 U.S.L.W. 4742"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tucker:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109063 OR 9425753 OR 9425754 OR 9425755) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDM5NDc4NDAwMDAwJnM9MTg5MDkzNSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109063+OR+9425753+OR+9425754+OR+9425755%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(109063 OR 9425753 OR 9425754 OR 9425755)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MjQmcz0yMjc4NzM5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109063+OR+9425753+OR+9425754+OR+9425755%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109063 OR 9425753 OR 9425754 OR 9425755)",
        "reviewed": 20,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 20,
        "triage_read": 0,
        "triage_snippet_classified": 20
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109063 OR 9425753 OR 9425754 OR 9425755)",
    "indexed_citing_opinions": 898,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109063,
        "count": 825,
        "count_source": "search"
      },
      {
        "opinion_id": 9425753,
        "count": 104,
        "count_source": "search"
      },
      {
        "opinion_id": 9425754,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425755,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1437,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-tucker.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc2OTAyMDcmcz02NDU2ODgzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109063+OR+9425753+OR+9425754+OR+9425755%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109063,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 105305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 105508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 105532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 106421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107741,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 107949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 108301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 108794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 108860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 239500,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 300429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 1661457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 2004533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
        "cited_id": 2181751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109063,
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
    "date_created": "2026-07-05T13:45:38Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:46:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:46:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:48:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:46:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Tucker

```
<opinion type="majority">
<author id="b499-5"><page-number citation-index="1" label="435">*435</page-number>Mr. Justice Rehnquist</author>
<p id="Aua">delivered the opinion of the Court.</p>
<p id="b499-6">This case presents the question whether the testimony of a witness in respondent’s state court trial for rape must be excluded simply because police had learned the identity of the witness by questioning respondent at a time when he was in custody as a suspect, but had not been advised that counsel would be appointed for him if he was indigent. The questioning took place before this Court’s decision in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), but respondent’s trial, at which he was convicted, took place afterwards. Under the holding of <em>Johnson </em>v. <em>New Jersey, </em><span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span> (1966), therefore, <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is applicable to this case. The United States District Court for the Eastern District of Michigan reviewed respondent’s claim on a petition for habeas corpus and held that the testimony must be excluded.<footnotemark>1</footnotemark> The Court of Appeals affirmed.<footnotemark>2</footnotemark></p>
<p id="b499-7">I</p>
<p id="b499-8">On the morning of April 19, 1966, a 43-year-old woman in Pontiac, Michigan, was found in her home by a friend and coworker, Luther White, in serious condition. At the time she was found the woman was tied, gagged, and partially disrobed, and had been both raped and severely beaten. She was unable to tell White anything about her assault at that time and still remains unable to recollect what happened.</p>
<p id="b499-9">While White was attempting to get medical help for the victim and to call for the police, he observed a dog inside the house. This apparently attracted White’s attention for he knew that the woman did not own 'a dog <page-number citation-index="1" label="436">*436</page-number>herself. Later, when talking with police officers, White observed the dog a second time, and police followed the dog to respondent’s house. Neighbors further connected the dog with respondent.</p>
<p id="b500-5">The police then arrested respondent and brought him to the police station for questioning. Prior to the actual interrogation the police asked respondent whether he knew for what crime he had been arrested, whether he wanted an attorney, and whether he understood his constitutional rights.<footnotemark>3</footnotemark> Respondent replied that he did understand the crime for which he was arrested, that he did not want an attorney, and that he understood his rights.<footnotemark>4</footnotemark> The police further advised him that any statements he might make could be used against him at a later date in court.<footnotemark>5</footnotemark> The police, however, did not advise respondent that he would be furnished counsel free of charge if he could not pay for such services himself.</p>
<p id="b500-6">The police then questioned respondent about his activities on the night of the rape and assault. Respondent replied that during the general time period at issue he had first been with one Robert Henderson and then later at home, alone, asleep. The police sought to confirm this story by contacting Henderson, but Henderson’s story served to discredit rather than to bolster respondent’s account. Henderson acknowledged that respondent had been with him on the night of the crime but said that he had left at a relatively early time. Furthermore, Henderson told police that he saw respondent the following day and asked him at that time about scratches on his face — “asked him if he got hold of a wild one or something.”<footnotemark>6</footnotemark> Respondent answered: “[S]omething like <page-number citation-index="1" label="437">*437</page-number>that.”<footnotemark>7</footnotemark> Then, Henderson said, he asked respondent “who it was,” <footnotemark>8</footnotemark> and respondent said: “[S]ome woman lived the next block over,” <footnotemark>9</footnotemark> adding: “She is a widow woman” or words to that effect.<footnotemark>10</footnotemark></p>
<p id="b501-5">These events all occurred prior to the date on which this Court handed down its decision in <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra,</a></span> </em>but respondent’s trial occurred after-wards. Prior to trial respondent’s appointed counsel made a motion to exclude Henderson’s expected testimony because respondent had revealed Henderson’s identity without having received full <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. Although respondent’s own statements taken during interrogation were excluded, the trial judge denied the motion to exclude Henderson’s testimony. Henderson therefore testified at trial, and respondent was convicted of rape and sentenced to 20 to 40 years’ imprisonment. His conviction was affirmed by both the Michigan Court of Appeals<footnotemark>11</footnotemark> and the Michigan Supreme Court.<footnotemark>12</footnotemark></p>
<p id="b501-6">Respondent then sought habeas corpus relief in Federal District Court. That court, noting that respondent had not received the full <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and that the police had stipulated Henderson’s identity was learned only through respondent’s answers, “reluctantly” concluded that Henderson’s testimony could not be admitted.<footnotemark>13</footnotemark> Application of such an exclusionary rule was necessary, the court reasoned, to protect respondent’s Fifth Amendment right against compulsory self-incrimination. The court therefore granted respondent’s petition for a writ of habeas corpus unless petitioner <page-number citation-index="1" label="438">*438</page-number>retried respondent within 90 days. The Court of Appeals for the Sixth Circuit affirmed. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1062/">414 U. S. 1062</a></span> (1973), and now reverse.</p>
<p id="b502-5">II</p>
<p id="b502-6">Although respondent’s sole complaint is that the police failed to advise him that he would be given free counsel if unable to afford counsel himself, he did not, and does not now, base his arguments for relief on a right to counsel under the Sixth and Fourteenth Amendments. Nor was the right to counsel, as such, considered to be persuasive by either federal court below. We do not have a situation such as that presented in <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), where the policemen interrogating the suspect had refused his repeated requests to see his lawyer who was then present at the police station. As we have noted previously, <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>is not to be broadly extended beyond the facts of that particular case. See <em>Johnson </em>v. <em>New Jersey, </em><span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#733" aria-description="Citation for case: Johnson v. New Jersey">384 U. S., at 733-734</a></span>; <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 689</a></span> (1972); <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969). This case also falls outside the rationale of <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#224" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 224</a></span> (1967), where the Court held that counsel was needed at a post-indictment lineup in order to protect the “right to a fair trial at which the witnesses against [the defendant] might be meaningfully cross-examined.” Henderson was fully available for searching cross-examination at respondent’s trial.</p>
<p id="b502-7">Respondent’s argument, and the opinions of the District Court and Court of Appeals, instead rely upon the Fifth Amendment right against compulsory self-incrimination and the safeguards designed in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to secure that right. In brief, the position urged upon this Court is that proper regard for the privilege against compulsory self-incrimination requires, with limited exceptions not <page-number citation-index="1" label="439">*439</page-number>applicable here, that all evidence derived solely from statements made without full <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings be excluded at a subsequent criminal trial. For purposes of analysis in this case we believe that the question thus presented is best examined in two separate parts. We will therefore first consider whether the police conduct complained of directly infringed upon respondent’s right against compulsory self-incrimination or whether it instead violated only the prophylactic rules developed to protect that right. We will then consider whether the evidence derived from this interrogation must be excluded.</p>
<p id="b503-5">Ill</p>
<p id="b503-6">The history of the Fifth Amendment right against compulsory self-incrimination, and the evils against which it was directed, have received considerable attention in the opinions of this Court. See, <em>e. g., Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441</a></span> (1972); <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra;</a></span> Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52</a></span> (1964); <em>Ullmann </em>v. <em>United States, </em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#426" aria-description="Citation for case: Ullmann v. United States">350 U. S. 422, 426</a></span> (1956); <em>Counselman </em>v. <em>Hitchcock, </em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547</a></span> (1892). At this point in our history virtually every schoolboy is familiar with the concept, if not the language, of the provision that reads: “No person . . . shall be compelled in any criminal case to be a witness against himself . ...” This Court’s decisions have referred to the right as “the mainstay of our adversary system of criminal justice,” <em>Johnson </em>v. <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#729" aria-description="Citation for case: Johnson v. New Jersey"><em>New Jersey, supra, </em>at 729</a></span>, and as “ ‘one of the great landmarks in man’s struggle to make himself civilized.’ ” <span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#426" aria-description="Citation for case: Ullmann v. United States"><em>Ullmann, supra, </em>at 426</a></span>. It is not surprising that the constitution of virtually every State has a comparable provision. 8 J. Wigmore, Evidence § 2252 (McNaughton rev. 1961) (hereinafter Wigmore).</p>
<p id="b503-7">The importance of a right does not, by itself, determine its scope, and therefore we must continue to hark back <page-number citation-index="1" label="440">*440</page-number>to the historical origins of the privilege, particularly the evils at which it was to strike. The privilege against compulsory self-incrimination was developed by painful opposition to a course of ecclesiastical inquisitions and Star Chamber proceedings occurring several centuries ago. See L. Levy, Origins of the Fifth Amendment (1968); Morgan, The Privilege Against Self-Incrimination, <span class="citation no-link">34 Minn. L. Rev. 1</span> (1949); 8 Wigmore §2250. Certainly anyone who reads accounts of those investigations, which placed a premium on compelling subjects of the investigation to admit guilt from their own lips, cannot help but be sensitive to the Framers’ desire to protect citizens against such compulsion. As this Court has noted, the privilege against self-incrimination “was aimed at a . . . far-reaching evil — a recurrence of the Inquisition and the Star Chamber, even if not in their stark brutality.” <span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#428" aria-description="Citation for case: Ullmann v. United States"><em>Ullmann, supra, </em>at 428</a></span>.</p>
<p id="b504-5">Where there has been genuine compulsion of testimony, the right has been given broad scope. Although the constitutional language in which the privilege is cast might be construed to apply only to situations in which the prosecution seeks to call a defendant to testify against himself at his criminal trial, its application has not been so limited. The right has been held applicable to proceedings before a grand jury, <em>Counselman </em>v. <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Hitchcock, supra;</a></span> </em>to civil proceedings, <em>McCarthy </em>v. <em>Arndstein, </em><span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34</a></span> (1924); to congressional investigations, <em>Watkins </em>v. <em>United States, </em><span class="citation" data-id="9421469"><a href="/opinion/105532/watkins-v-united-states/" aria-description="Citation for case: Watkins v. United States">354 U. S. 178</a></span> (1957); to juvenile proceedings, <em>In re Gault, </em><span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">387 U. S. 1</a></span> (1967); and to other statutory inquiries, <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964). The privilege has also been applied against the States by virtue of the Fourteenth Amendment. <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Ibid.</a></span></em></p>
<p id="b504-6">The natural concern which underlies many of these decisions is that an inability to protect the right at <page-number citation-index="1" label="441">*441</page-number>one stage of a proceeding may make its invocation useless at a later stage. For example, a defendant’s right not to be compelled to testify against himself at his own trial might be practically nullified if the prosecution could previously have required him to give evidence against himself before a grand jury. Testimony obtained in civil suits, or before administrative or legislative committees, could also prove so incriminating that a person compelled to give such testimony might readily be convicted on the basis of those disclosures in a subsequent criminal proceeding.<footnotemark>14</footnotemark></p>
<p id="b505-4">In more recent years this concern — that compelled disclosures might be used against a person at a later criminal trial — -has been extended to cases involving police interrogation. Before <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>the principal issue in these cases was not whether a defendant had waived his privilege against compulsory self-incrimination but simply whether his statement was “voluntary.” In state cases the Court applied the Due Process Clause of the Fourteenth Amendment, examining the circumstances of interrogation to determine whether the processes were so unfair or unreasonable as to render a subsequent confession involuntary. See, <em>e. g., Brown </em>v. <em>Mississippi, </em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936); <em>Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span> (1940); <em>White </em>v. <em>Texas, </em><span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U. S. 530</a></span> (1940); <em>Payne </em>v. <em>Arkansas, </em><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (1958); <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span> (1963). See also 3 J. Wigmore, Evidence §815 <em>et seq. </em>(Chadbourne rev. 1970). Where the State’s actions offended the standards of fundamental fairness under the Due Process Clause, the State was then deprived of the right to use the resulting confessions in court.</p>
<p id="b506-4"><page-number citation-index="1" label="442">*442</page-number>Although federal cases concerning voluntary confessions often contained references to the privilege against compulsory self-incrimination,<footnotemark>15</footnotemark> references which were strongly criticized by some commentators, see 8 Wig-more § 2266,<footnotemark>16</footnotemark> it was not until this Court’s decision in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that the privilege against compulsory self-incrimination was seen as the principal protection for a person facing police interrogation. This privilege had been made applicable to the States in <em>Malloy </em>v. <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Hogan, supra,</a></span> </em>and was thought to offer a more comprehensive and <page-number citation-index="1" label="443">*443</page-number>less subjective protection than the doctrine of previous cases. In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>the Court examined the facts of four separate- cases and stated:</p>
<blockquote id="b507-5">“In these cases, we might not find the defendants’ statements to have been involuntary in traditional terms. Our concern for adequate safeguards to protect precious Fifth Amendment rights is, of course, not lessened in the slightest. ... To be sure, the records do not evince overt physical coercion or patent psychological ploys. The fact remains that in none of these cases did the officers undertake to afford appropriate safeguards at the outset of the interrogation to insure that the statements were truly the product of free choice.” 384 U. S., at 457.</blockquote>
<p id="b507-6">Thus the Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>for the first time, expressly declared that the Self-Incrimination Clause was applicable to state interrogations at a police station, and that a defendant’s statements might be excluded at trial despite their voluntary character under traditional principles.</p>
<p id="b507-7">To supplement this new doctrine, and to help police officers conduct interrogations without facing a continued risk that valuable evidence would be lost, the Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>established a set of specific protective guidelines, now commonly known as the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rules. The Court declared that “the prosecution may not use statements, whether exculpatory or inculpatory, stemming from custodial interrogation of the defendant unless it demonstrates the use of procedural safeguards effective to secure the privilege against self-incrimination.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>. A series of recommended “procedural safeguards” then followed. The Court in particular stated:</p>
<blockquote id="Adz">“Prior to any questioning, the person must be warned that he has a right to remain silent, that any statement he does make may be used as evidence <page-number citation-index="1" label="444">*444</page-number>against him, and that he has a right to the presence of an attorney, either retained or appointed.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></blockquote>
<p id="b508-5">The Court said that the defendant, of course, could waive these rights, but that any waiver must have been made “voluntarily, knowingly and intelligently.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></p>
<p id="b508-6">The Court recognized that these procedural safeguards were not themselves rights protected by the Constitution but were instead measures to insure that the right against compulsory self-incrimination was protected. As the Court remarked:</p>
<blockquote id="b508-7">“[W]e cannot say that the Constitution necessarily requires adherence to any particular solution for the inherent compulsions of the interrogation process as it is presently conducted.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 467</a></span>.</blockquote>
<p id="b508-8">The suggested safeguards were not intended to “create a constitutional straitjacket,” <em>ibid., </em>but rather to provide practical reinforcement for the right against compulsory self-incrimination.</p>
<p id="b508-9">A comparison of the facts in this case with the historical circumstances underlying the privilege against compulsory self-incrimination strongly indicates that the police conduct here did not deprive respondent of his privilege against compulsory self-incrimination as such, but rather failed to make available to him the full measure of procedural safeguards associated with that right since <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>Certainly no one could contend that the interrogation faced by respondent bore any resemblance to the historical practices at which the right against compulsory self-incrimination was aimed. The District Court in this case noted that the police had “warned [respondent] that he had the right to remain silent,” <span class="citation" data-id="2004533"><a href="/opinion/2004533/tucker-v-johnson/#267" aria-description="Citation for case: Tucker v. Johnson">352 F. Supp. 266, 267</a></span> (1972), and the record in this case clearly shows that respondent was informed that any evidence taken could be used against him.<footnotemark>17</footnotemark> The record is also clear that <page-number citation-index="1" label="445">*445</page-number>respondent was asked whether he wanted an attorney and that he replied that he did not.<footnotemark>18</footnotemark> Thus, his statements could hardly be termed involuntary as that term has been defined in the decisions of this Court. Additionally, there were no legal sanctions, such as the threat of contempt, which could have been applied to respondent had he chosen to remain silent. He was simply not exposed to “the cruel trilemma of self-accusation, perjury or contempt.” <em>Murphy </em>v. <em>Waterfront Comm’n, </em>378 U. S., at 55.</p>
<p id="b509-5">Our determination that the interrogation in this case involved no compulsion sufficient to breach the right against compulsory self-incrimination does not mean there was not a disregard, albeit an inadvertent disregard, of the procedural rules later established in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The question for decision is how sweeping the judicially imposed consequences of this disregard shall be. This Court said in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that statements taken in violation of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>principles must not be used to prove the prosecution’s case at trial. That requirement was fully complied with by the state court here: respondent’s statements, claiming that he was with Henderson and then asleep during the time period of the crime were not admitted against him at trial. This Court has also said, in <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), that the “fruits” of police conduct which actually infringed a defendant’s Fourth Amendment rights must be suppressed.<footnotemark>19</footnotemark> But we have already concluded that the <page-number citation-index="1" label="446">*446</page-number>police conduct at issue here did not abridge respondent’s constitutional privilege against compulsory self-incrimination, but departed only from the prophylactic standards later laid down by this Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to safeguard that privilege. Thus, in deciding whether Henderson’s testimony must be excluded, there is no controlling precedent of this Court to guide us. We must therefore examine the matter as a question of principle.</p>
<p id="b510-5">IV</p>
<p id="b510-6">Just as the law does not require that a defendant receive a perfect trial, only a fair one, it cannot realistically require that policemen investigating serious crimes make no errors whatsoever. The pressures of law enforcement and the vagaries of human nature would make such an expectation unrealistic. Before we penalize police error, therefore, we must consider whether the sanction serves a valid and useful purpose.</p>
<p id="b510-7">We have recently said, in a search-and-seizure context, that the exclusionary rule’s “prime purpose is to deter future unlawful police conduct and thereby effectuate the guarantee of the Fourth Amendment against unreasonable searches and seizures.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347</a></span> (1974). We then continued:</p>
<blockquote id="b510-8"><em>“ </em>'The rule is calculated to prevent, not to repair. Its purpose is to deter — to compel respect for the constitutional guaranty in the only effectively available way — by removing the incentive to disregard it.’ <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960).”<footnotemark>20</footnotemark> <em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Ibid.</a></span></em></blockquote>
<p id="b511-4"><page-number citation-index="1" label="447">*447</page-number>In a proper case this rationale would seem applicable to the Fifth Amendment context as well.</p>
<p id="b511-5">The deterrent purpose of the exclusionary rule necessarily assumes that the police have engaged in willful, or at the very least negligent, conduct which has deprived the defendant of some right. By refusing to admit evidence gained as a result of such conduct, the courts hope to instill in those particular investigating officers, or in their future counterparts, a greater degree of care toward the rights of an accused. Where the official action was pursued in complete good faith, however, the deterrence rationale loses much of its force.</p>
<p id="b511-6">We consider it significant to our decision in this case that the officers’ failure to advise respondent of his right to appointed counsel occurred prior to the decision in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>Although we have been urged to resolve the broad question of whether evidence derived from statements taken in violation of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rules must be excluded regardless of when the interrogation took place/<footnotemark>21</footnotemark> we instead place our holding on a narrower ground. For at the time respondent was questioned these police officers were guided, quite rightly, by the principles established in <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), particularly focusing on the suspect’s opportunity to have retained counsel with him during the interrogation if he chose to do so.<footnotemark>22</footnotemark> Thus, the police asked respondent if he wanted counsel, and he answered that he did not. The <page-number citation-index="1" label="448">*448</page-number>statements actually made by respondent to the police, as we have observed, were excluded at trial in accordance with <em>Johnson </em>v. <em>New Jersey, </em><span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span> (1966). Whatever deterrent effect on future police conduct the exclusion of those statements may have had, we do not believe it would be significantly augmented by excluding the testimony of the witness Henderson as well.</p>
<p id="b512-5">When involuntary statements or the right against compulsory self-incrimination are involved, a second justification for the exclusionary rule also has been asserted: protection of the courts from reliance on untrustworthy evidence.<footnotemark>23</footnotemark> Cases which involve the Self-Incrimination Clause must, by definition, involve an element of coercion, since the Clause provides only that a person shall not be <em>compelled </em>to give evidence against himself. And cases involving statements often depict severe pressures which may override a particular suspect's insistence on innocence. Fact situations ranging from classical third-degree torture, <em>Brown </em>v. <em>Mississippi, </em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), to prolonged isolation from family or friends in a hostile setting, <em>Gallegos </em>v. <em>Colorado, </em><span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">370 U. S. 49</a></span> (1962), or to a simple desire on the part of a physically or mentally ex<page-number citation-index="1" label="449">*449</page-number>hausted suspect to have a seemingly endless interrogation end, <em>Watts </em>v. <em>Indiana, </em><span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49</a></span> (1949), all might be sufficient to cause a defendant to accuse himself falsely.</p>
<p id="b513-5">But those situations are a far cry from that presented here. The pressures on respondent to accuse himself were hardly comparable even with the least prejudicial of those pressures which have been dealt with in our cases. More important, the respondent did <em>not </em>accuse himself. The evidence which the prosecution successfully sought to introduce was not a confession of guilt by respondent, or indeed even an exculpatory statement by respondent, but rather the testimony of a third party who was subjected to no custodial pressures. There is plainly no reason to believe that Henderson’s testimony is untrustworthy simply because <em>respondent </em>was not advised of <em>his </em>right to appointed counsel. Henderson was both available at trial and subject to cross-examination by respondent’s counsel, and counsel fully used this opportunity, suggesting in the course of his cross-examination that Henderson’s character was less than exemplary and that he had been offered incentives by the police to testify against respondent.<footnotemark>24</footnotemark> Thus the reliability of his testimony was subject to the normal testing process of an adversary trial.</p>
<p id="b513-6">Respondent contends that an additional reason for excluding Henderson’s testimony is the notion that the adversary system requires “the government in its contest with the individual to shoulder the entire load.” 8 Wig-more § 2251, p. 317; <em>Murphy </em>v. <em>Waterfront Comm’n, </em>378 U. S., at 55; <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#460" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 460</a></span>. To the extent that this suggested basis for the exclusionary rule in Fifth Amendment cases may exist independently of the deterrence and trustworthiness rationales, we think it of no avail to respondent here. Sub<page-number citation-index="1" label="450">*450</page-number>ject to applicable constitutional limitations, the Government is not forbidden all resort to the defendant to make out its case. It may require the defendant to give physical evidence against himself, see <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966); <em>United States </em>v. <em>Dionisio, </em><span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1</a></span> (1973), and it may use statements which are voluntarily given by the defendant after he receives full disclosure of the rights offered by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>Here we deal, not with the offer of respondent’s own statements in evidence, but only with the testimony of a witness whom the police discovered as a result of respondent’s statements. This recourse to respondent’s voluntary statements does no violence to such elements of the adversary system as may be embodied in the Fifth, Sixth, and Fourteenth Amendments.</p>
<p id="b514-5">In summary, we do not think that any single reason supporting exclusion of this witness’ testimony, or all of them together, are very persuasive.<footnotemark>25</footnotemark> By contrast, we find the arguments in favor of admitting the testimony quite strong. For, when balancing the interests involved, we must weigh the strong interest under any system of justice of making available to the trier of fact all con-cededly relevant and trustworthy evidence which either party seeks to adduce. In this particular case we also “must consider society’s interest in the effective prosecution of criminals in light of the protection our pre-Miranda standards afford criminal defendants.” <em>Jenkins </em><page-number citation-index="1" label="451">*451</page-number>v. <em>Delaware, </em><span class="citation" data-id="9424052"><a href="/opinion/107949/jenkins-v-delaware/#221" aria-description="Citation for case: Jenkins v. Delaware">395 U. S. 213, 221</a></span> (1969). These interests may be outweighed by the need to provide an effective sanction to a constitutional right, <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), but they must in any event be valued. Here respondent’s own statement, which might have helped the prosecution show respondent’s guilty conscience at trial, had already been excised from the prosecution’s case pursuant to this Court’s <em><span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">Johnson</a></span> </em>decision. To extend the excision further under the circumstances of this case and exclude relevant testimony of a third-party witness would require far more persuasive arguments than those advanced by respondent.</p>
<p id="b515-5">This Court has already recognized that a failure to give interrogated suspects full <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings does not entitle the suspect to insist that statements made by him be excluded in every conceivable context. In <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), the Court was faced with the question of whether the statements of the defendant himself, taken without informing him of his right of access to appointed counsel, could be used to impeach defendant’s direct testimony at trial. The Court concluded that they could, saying:</p>
<blockquote id="b515-6">“Some comments in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion can indeed be read as indicating a bar to use of an uncounseled statement for any purpose, but discussion of that issue was not at all necessary to the Court’s holding and cannot be regarded as controlling. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>barred the prosecution from making its case with statements of an accused made while in custody prior to having or effectively waiving counsel. It does not follow from <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that evidence inadmissible against an accused in the prosecution’s case in chief is barred for all purposes, provided of course that the trustworthiness of the evidence satisfies legal standards.” <em>Id., </em>at 224.</blockquote>
<p id="b516-4"><page-number citation-index="1" label="452">*452</page-number>We believe that this reasoning is equally applicable here. Although <em><span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">Johnson</a></span> </em>enabled respondent to block admission of his own statements, we do not believe that it requires the prosecution to refrain from all use of those statements, and we disagree with the courts below that Henderson’s testimony should have been excluded in this case.<footnotemark>26</footnotemark></p>
<p id="b516-5">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b499-10"> <span class="citation" data-id="2004533"><a href="/opinion/2004533/tucker-v-johnson/" aria-description="Citation for case: Tucker v. Johnson">352 F. Supp. 266</a></span> (1972).</p>
</footnote>
<footnote label="2">
<p id="b499-11"> <span class="citation multiple-matches"><a href="/c/F.%202d/480/927/">480 F. 2d 927</a></span> (1973).</p>
</footnote>
<footnote label="3">
<p id="b500-7"> Tr. of Prelim. Hearing 99.</p>
</footnote>
<footnote label="4">
<p id="b500-8"> <em>Ibid.</em></p>
</footnote>
<footnote label="5">
<p id="b500-9"><em> Id,., </em>at 99-100.</p>
</footnote>
<footnote label="6">
<p id="b500-10"> Tr. of Trial 223.</p>
</footnote>
<footnote label="7">
<p id="b501-7">
<em> Ibid.</em>
</p>
</footnote>
<footnote label="8">
<p id="b501-8"> <em>Id., </em>at 224.</p>
</footnote>
<footnote label="9">
<p id="b501-9"> <em><span class="citation" data-id="2004533"><a href="/opinion/2004533/tucker-v-johnson/" aria-description="Citation for case: Tucker v. Johnson">Ibid.</a></span></em></p>
</footnote>
<footnote label="10">
<p id="b501-10"> <em><span class="citation" data-id="2004533"><a href="/opinion/2004533/tucker-v-johnson/" aria-description="Citation for case: Tucker v. Johnson">Ibid.</a></span></em></p>
</footnote>
<footnote label="11">
<p id="b501-11"> <span class="citation" data-id="2181751"><a href="/opinion/2181751/people-v-tucker/" aria-description="Citation for case: People v. Tucker">19 Mich. App. 320</a></span>, <span class="citation" data-id="2181751"><a href="/opinion/2181751/people-v-tucker/" aria-description="Citation for case: People v. Tucker">172 N. W. 2d 712</a></span> (1969).</p>
</footnote>
<footnote label="12">
<p id="b501-12"> <span class="citation" data-id="1661457"><a href="/opinion/1661457/people-v-tucker/" aria-description="Citation for case: People v. Tucker">385 Mich. 594</a></span>, <span class="citation" data-id="1661457"><a href="/opinion/1661457/people-v-tucker/" aria-description="Citation for case: People v. Tucker">189 N. W. 2d 290</a></span> (1971).</p>
</footnote>
<footnote label="13">
<p id="b501-13"> <span class="citation" data-id="2004533"><a href="/opinion/2004533/tucker-v-johnson/#268" aria-description="Citation for case: Tucker v. Johnson">352 F. Supp., at 268</a></span>.</p>
</footnote>
<footnote label="14">
<p id="b505-5"> The Court has also held that comment on a defendant’s silence or refusal to take the witness stand may be an impermissible penalty on exercise of the privilege. See <em>Griffin </em>v. <em>California, </em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965).</p>
</footnote>
<footnote label="15">
<p id="b506-5"> For example in <em>Bram </em>v. <em>United States, </em><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542</a></span> (1897), the Court stated:</p>
<blockquote id="b506-6">“In criminal trials, in the courts of the United States, wherever a question arises whether a confession is incompetent because not voluntary, the issue is controlled by that portion of the Fifth Amendment to the Constitution of the United States, commanding that no person ‘shall be compelled in any criminal case to be a witness against himself.’ ”</blockquote>
<p id="b506-7">As noted in the text, the privilege against compulsory self-incrimination was not held applicable against the States until <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964).</p>
</footnote>
<footnote label="16">
<p id="b506-8"> Wigmore states his objection in the following terms:</p>
<blockquote id="b506-9">“Today in the United States confessions, and probably even lesser self-incriminating admissions, are excluded despite their trustworthiness if coerced. The policies leading to this recent extension of the confession rule are quite similar to those underlying the privilege against self-incrimination. It is thus not surprising that the privilege, with its unclear boundaries and apparently unending capacity for transmogrification and assimilation, is now sometimes invoked to effect exclusion even though the disclosure was not compelled from a person under legal compulsion. Distortion of the privilege to cover such situations is not necessary. If trustworthy confessions are to be excluded because coerced, it should be done frankly as an exception to the principle . . . that the illegality of source of evidence is immaterial. It should be done, as it usually is, on the ground that the combination of coercion and use of the evidence in the particular case violates the relevant constitutional due process clause.” <em>Id., </em>at 402. (Citations omitted.)</blockquote>
</footnote>
<footnote label="17">
<p id="b508-10"> See n. 5, <em>supra.</em></p>
</footnote>
<footnote label="18">
<p id="b509-6"> See nn. 3 and 4, <em>supra.</em></p>
</footnote>
<footnote label="19">
<p id="b509-7"> In <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>the police discovered evidence through statements made by the accused after he had been placed under arrest. This Court, finding that the arrest had occurred without probable cause, held that the derivative evidence could not be introduced against the accused at trial. For the reasons stated in the text we do not believe that <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>controls the case before us.</p>
</footnote>
<footnote label="20">
<p id="b510-9"> The opinion also relied upon <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 656</a></span> (1961); <em>Tehan </em>v. <em>United States ex rel. Shott, </em><span class="citation" data-id="6751647"><a href="/opinion/6862154/tehan-v-united-states-ex-rel-shott/#416" aria-description="Citation for case: Tehan v. United States ex rel. Shott">382 U. S. 406, 416</a></span> (1966); and <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 29</a></span> (1968). See <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348</a></span>.</p>
</footnote>
<footnote label="21">
<p id="b511-7"> Brief for United States as <em>Amicus Curiae </em>31 <em>et seq.; </em>Brief for Respondent 9 <em>et seq.</em></p>
</footnote>
<footnote label="22">
<p id="b511-8"><em> </em>As previously noted, the defendant in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>had repeatedly asked to see his lawyer who was available at the police station. Those requests were denied, and the defendant ultimately confessed. Thus, in direct contrast to the situation here, the defendant in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>was told he did <em>not </em>have a right to see his lawyer, although he had expressly stated his desire to do so.</p>
</footnote>
<footnote label="23">
<p id="b512-6"> The Court has made clear that the truth or falsity of a statement is not the determining factor in the decision whether or not to exclude it. <em>Jackson </em>v. <em>Denno, </em><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span> (1964). Thus a State which has obtained a coerced or involuntary statement cannot argue for its admissibility on the ground that other evidence demonstrates its truthfulness. <em><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Ibid.</a></span> </em>But it also seems clear that coerced statements have been regarded with some mistrust. The Court in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>for example, stated that “a system of criminal law enforcement which comes to depend on the 'confession’ will, in the long run, be less reliable and more subject to abuses” than a system relying on independent investigation, 378 U. S., at 488-489. The Court then cited several authorities concerned with false confessions. <em>Id., </em>at 489 n. 11. Although completely voluntary confessions may, in many cases, advance the cause of justice and rehabilitation, coerced confessions, by their nature, cannot serve the same ends.</p>
</footnote>
<footnote label="24">
<p id="b513-7"> Tr. of Trial 226-234.</p>
</footnote>
<footnote label="25">
<p id="b514-6"> It has been suggested that courts should exclude evidence derived from “lawless invasions of the constitutional rights of citizens,” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#13" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 13</a></span>, in recognition of “the imperative of judicial integrity.” <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960). This rationale, however, is really an assimilation of the more specific rationales discussed in the text of this opinion, and does not in their absence provide an independent basis for excluding challenged evidence.</p>
</footnote>
<footnote label="26">
<p id="b516-6"> Our Brother BreNNAN in his opinion concurring in the judgment treats the principal question here simply as a lineal descendant of the one decided in <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span> (1965), to be analyzed only in terms of the retroactivity framework established in that and subsequent decisions. While his approach has a beguiling simplicity, we believe it marks a significant and unsettling departure from the past practice of the Court in this area. Our retroactivity cases, from <em>Linkletter </em>v. <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Walker, supra,</a></span> </em>to <em>Gosa </em>v. <em>Mayden, </em><span class="citation" data-id="9425433"><a href="/opinion/108860/gosa-v-mayden/" aria-description="Citation for case: Gosa v. Mayden">413 U. S. 665</a></span> (1973), all have in common a particular factual predicate: a previous constitutional decision of this Court governs the facts of an earlier decided case unless the constitutional decision is not to have retroactive effect. The doctrine of retroactivity does not modify the substantive scope of the constitutional decision but rather determines the point in time when it is held to apply.</p>
<p id="b516-7">That common factual predicate is absent here. No defendant in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>sought to block evidence of the type challenged in this case, and the holding of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>even if made fully retroactive, would not therefore resolve the question of whether Henderson’s testimony must also be excluded at trial. Contrary, therefore, to the suggestion in our Brother’s opinion that the question here is whether to “limit the effect of <em>Johnson </em>v. <em>New Jersey,” post, </em>at 454 n. 1, <em><span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">Johnson</a></span> </em>has never been thought controlling on the question of fruits, for the simple reason that the parent <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case did not reach that issue.</p>
<p id="b516-8">Our Brother BreNNAN’s method of disposition is to determine in the present case the retroactivity of a holding which the Court has yet to make. He would say, in effect, that if the Court should later determine that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires exclusion of fruits such as the testimony of Henderson, nonetheless that determination shall not be applied retroactively. But this approach wholly subverts the heretofore established relationship between the parent case and the subsidiary case determining whether or not to apply the parent case <page-number citation-index="1" label="453">*453</page-number>retroactively. Under the framework of the analysis established in <em>Linklebter, supra, </em>and in subsequent cases, it would seem indispensable to understand the basis for a constitutional holding of the Court in order to later determine whether that holding should be retroactive. Yet <em>ex hypothesi </em>our Brother has no such analysis available, since the case has yet to be decided. Cases which <em>subsequently </em>determine the retroactivity of a constitutional holding have given the Court enough occasion for concern without substantially increasing the difficulty of that type of decision by making it before, rather than after, the constitutional holding.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Michigan v. Tyler.md  (`case`, 6 assertions)

### content_page

```
---
title: "Michigan v. Tyler"
type: case
citation: "436 U.S. 499 (1978)"
parallel_cite: "98 S. Ct. 1942; 56 L. Ed. 2d 486"
neutral_cite: 1978 U.S. LEXIS 97
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-05-31
docket: 76-1608
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-05-31
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Tyler
  varies_by_point: false
  scope_note: "Good law; refined by Michigan v. Clifford (after the fire is out and the scene secured, further investigative entry needs an administrative or criminal warrant)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109874/michigan-v-tyler/"
  cluster_id: 109874
  opinion_id: 109874
  identity_checked: true
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Related (cross-doctrine)"
related: ["[[Michigan v. Clifford]]", "[[Camara v. Municipal Court]]", "[[Mincey v. Arizona]]", "[[Coolidge v. New Hampshire]]"]
aliases: []
tags: ["case", "fourth-amendment", "exigent-circumstances", "fire", "administrative-warrant", "plain-view"]
holding: "A burning building is an exigency justifying warrantless entry; firefighters may stay a reasonable time to fight the fire and investigate its cause and may seize arson evidence in plain view, but later investigative entries, once the exigency has ended, require a warrant (administrative or, on probable cause of arson, criminal)."
lake:
  record_id: Michigan v. Tyler
  status: verified
  projected_at: 2026-07-09
---

# Michigan v. Tyler

*436 U.S. 499 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A furniture store caught fire near midnight. As firefighters fought the blaze, the fire chief arrived, found plastic containers of flammable liquid, and (with a police detective) took some evidence; visibility was poor from smoke and steam, so officials left around 4 a.m. and returned shortly after daylight to continue. Over the following weeks, fire and police officials made several further entries, without warrants or consent, gathering more arson evidence. The Michigan Supreme Court ordered a new trial, holding much of the evidence the product of unlawful warrantless searches.

## Issue
Whether, and for how long, officials may make warrantless entries into fire-damaged premises to fight the fire and investigate its cause, and when later investigative entries require a warrant.

## Rule
A burning building is an [[Exigent Circumstances and Hot Pursuit|exigency]]: "A burning building clearly presents an exigency of sufficient proportions to render a warrantless entry 'reasonable.' . . . And once in a building for this purpose, firefighters may seize evidence of arson that is in plain view." — 436 U.S. at 509. ^pin-509

They may also stay to investigate cause: "officials need no warrant to remain in a building for a reasonable time to investigate the cause of a blaze after it has been extinguished." — [*Id.* at 510](https://www.courtlistener.com/opinion/109874/michigan-v-tyler/#:~:text=officials%20need%20no%20warrant%20to). ^pin-510

But later entries need a warrant: "we hold that an entry to fight a fire requires no warrant, and that once in the building, officials may remain there for a reasonable time to investigate the cause of the blaze. Thereafter, additional entries to investigate the cause of the fire must be made pursuant to the warrant procedures governing administrative searches." — [*Id.* at 511](https://www.courtlistener.com/opinion/109874/michigan-v-tyler/#:~:text=we%20hold%20that%20an%20entry). ^pin-511

## Application
The midnight entry to fight the fire, and the early-morning re-entries the same day (hindered only by darkness and smoke), were treated as a continuation of the initial [[Exigent Circumstances and Hot Pursuit|exigency]] and needed no warrant; evidence from them was admissible. The later entries — days and weeks afterward — were "clearly detached from the initial exigency," made without warrants or consent, and so were invalid; evidence from them had to be excluded. If investigators find probable cause of arson and need further access to gather evidence for prosecution, they must obtain a criminal warrant on a traditional probable-cause showing.

## Conclusion
Affirmed. The fire-fighting entry and same-morning continuation were lawful; the later warrantless entries were not, and their fruits are inadmissible.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Refined by** [[Michigan v. Clifford]] — once the blaze is out and the scene secured, a later investigative search requires an administrative warrant (or, on probable cause of arson, a criminal warrant). *Tyler* draws the administrative-warrant standard from [[Camara v. Municipal Court]] and runs parallel to the homicide-scene rule of [[Mincey v. Arizona]].

## Appears on
- [[Emergency Aid]] — *Key — Progeny / Refinement*
- [[Special Needs and Administrative Searches]] — *Related (cross-doctrine)*

## Sources
- *Michigan v. Tyler*, 436 U.S. 499 (1978) — https://www.courtlistener.com/opinion/109874/michigan-v-tyler/ — pinpoints: 509, 510, 511.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "300d6b9cda3c6cf7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "436 U.S. 499 (1978)", "court": "U.S. Supreme Court", "neutral_cite": "1978 U.S. LEXIS 97", "official_citation_present": true, "parallel_cite": "98 S. Ct. 1942; 56 L. Ed. 2d 486", "title": "Michigan v. Tyler", "year": "1978"}}
{"assertion_id": "32c9c44f94d61b5e", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Related (cross-doctrine)", "title": "Michigan v. Tyler"}}
{"assertion_id": "67e3ee142daae188", "dimension": "support", "kind": "home_role", "locator": {"home": "Emergency Aid"}, "payload": {"home": "Emergency Aid", "role": "Key — Progeny / Refinement", "title": "Michigan v. Tyler"}}
{"assertion_id": "a754751db103dc47", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A burning building is an exigency justifying warrantless entry; firefighters may stay a reasonable time to fight the fire and investigate its cause and may seize arson evidence in plain view, but later investigative entries, once the exigency has ended, require a warrant (administrative or, on probable cause of arson, criminal).", "title": "Michigan v. Tyler"}}
{"assertion_id": "a89277ca58095cf1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Tyler"}}
{"assertion_id": "fc84055b6d08796b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1978-05-31", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Tyler", "field_i_validity": "good_law", "scope_note": "Good law; refined by Michigan v. Clifford (after the fire is out and the scene secured, further investigative entry needs an administrative or criminal warrant).", "title": "Michigan v. Tyler", "varies_by_point": "false"}}
```

### lake record — Michigan v. Tyler

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Tyler",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Tyler",
    "case_name_short": "Tyler",
    "case_name_full": "MICHIGAN v. TYLER Et Al.",
    "input_case_name": "Michigan v. Tyler",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-05-31",
    "year": 1978,
    "docket": "76-1608",
    "cluster_id": 109874,
    "lead_opinion_id": 109874,
    "sibling_ids": [
      109874,
      9427218,
      9427219,
      9427220,
      9427221
    ],
    "absolute_url": "/opinion/109874/michigan-v-tyler/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "436 U.S. 499",
      "volume": "436",
      "reporter": "U.S.",
      "page": "499",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 1942",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1942",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 486",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 97",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "97",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "436 U.S. 499",
        "volume": "436",
        "reporter": "U.S.",
        "page": "499",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 1942",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1942",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 486",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 97",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "97",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "436 U.S. 499",
    "official_selection": {
      "court_class": "scotus",
      "selected": "436 U.S. 499",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-509",
      "page": null,
      "quote": "--- # Michigan v. Tyler *436 U.S. 499 (1978)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A furniture store caught fire near midnight. As firefighters fought the blaze, the fire chief arrived, found plastic containers of flammable liquid, and (with a police detective) took some evidence; visibility was poor from smoke and steam, so officials left around 4 a.m. and returned shortly after daylight to continue. Over the following weeks, fire and police officials made several further entries, without warrants or consent, gathering more arson evidence. The Michigan Supreme Court ordered a new trial, holding much of the evidence the product of unlawful warrantless searches. ## Issue Whether, and for how long, officials may make warrantless entries into fire-damaged premises to fight the fire and investigate its cause, and when later investigative entries require a warrant. ## Rule A burning building is an exigency:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-510",
      "page": null,
      "quote": "officials need no warrant to remain in a building for a reasonable time to investigate the cause of a blaze after it has been extinguished.",
      "star_marker": "510",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 23984,
      "fragment": "#:~:text=officials%20need%20no%20warrant%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-511",
      "page": null,
      "quote": "we hold that an entry to fight a fire requires no warrant, and that once in the building, officials may remain there for a reasonable time to investigate the cause of the blaze. Thereafter, additional entries to investigate the cause of the fire must be made pursuant to the warrant procedures governing administrative searches.",
      "star_marker": "511",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26093,
      "fragment": "#:~:text=we%20hold%20that%20an%20entry",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-05-31",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Tyler",
    "varies_by_point": false,
    "scope_note": "Good law; refined by Michigan v. Clifford (after the fire is out and the scene secured, further investigative entry needs an administrative or criminal warrant).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789820,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 4600764,
          "cite": [
            "119 N.E.3d 257",
            "481 Mass. 604"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sarah Beth Keller",
          "cluster_id": 4247956,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cole v. State",
          "cluster_id": 5446855,
          "cite": [
            "490 S.W.3d 918",
            "2016 Tex. Crim. App. LEXIS 84",
            "2016 WL 3018203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane1_negative"
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
        "journal_ref": "Michigan v. Tyler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bodie Witzlib",
          "cluster_id": 2825238,
          "cite": [
            "796 F.3d 799",
            "2015 U.S. App. LEXIS 13811",
            "2015 WL 4664340"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City and County of San Francisco v. Sheehan",
          "cluster_id": 2801435,
          "cite": [
            "575 U.S. 600",
            "135 S. Ct. 1765",
            "191 L. Ed. 2d 856",
            "2015 U.S. LEXIS 3200",
            "83 U.S.L.W. 4303",
            "25 Fla. L. Weekly Fed. S 254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fadul",
          "cluster_id": 7306139,
          "cite": [
            "16 F. Supp. 3d 270",
            "2014 WL 1584044"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Pamela A. Inghram",
          "cluster_id": 1053363,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Conley, 88495 (6-14-2007)",
          "cluster_id": 3971919,
          "cite": [
            "2007 Ohio 2920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane1_negative"
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
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Long",
          "cluster_id": 111020,
          "cite": [
            "77 L. Ed. 2d 1201",
            "103 S. Ct. 3469",
            "463 U.S. 1032",
            "1983 U.S. LEXIS 7",
            "51 U.S.L.W. 5231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Rodriguez",
          "cluster_id": 112475,
          "cite": [
            "111 L. Ed. 2d 148",
            "110 S. Ct. 2793",
            "497 U.S. 177",
            "1990 U.S. LEXIS 3295",
            "58 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welsh v. Wisconsin",
          "cluster_id": 111173,
          "cite": [
            "80 L. Ed. 2d 732",
            "104 S. Ct. 2091",
            "466 U.S. 740",
            "1984 U.S. LEXIS 82",
            "52 U.S.L.W. 4581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan Department of State Police v. Sitz",
          "cluster_id": 112459,
          "cite": [
            "110 L. Ed. 2d 412",
            "110 S. Ct. 2481",
            "496 U.S. 444",
            "1990 U.S. LEXIS 3144",
            "58 U.S.L.W. 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Michigan",
          "cluster_id": 145646,
          "cite": [
            "165 L. Ed. 2d 56",
            "126 S. Ct. 2159",
            "547 U.S. 586",
            "2006 U.S. LEXIS 4677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Indianapolis v. Edmond",
          "cluster_id": 118391,
          "cite": [
            "148 L. Ed. 2d 333",
            "121 S. Ct. 447",
            "531 U.S. 32",
            "2000 U.S. LEXIS 8084",
            "69 U.S.L.W. 4009",
            "14 Fla. L. Weekly Fed. S 9",
            "2000 Colo. J. C.A.R. 6401",
            "2000 Cal. Daily Op. Serv. 9549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Georgia v. Randolph",
          "cluster_id": 145669,
          "cite": [
            "164 L. Ed. 2d 208",
            "126 S. Ct. 1515",
            "547 U.S. 103",
            "2006 U.S. LEXIS 2498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
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
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Albrecht",
          "cluster_id": 2259115,
          "cite": [
            "720 A.2d 693",
            "554 Pa. 31",
            "1998 Pa. LEXIS 2619"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Andreas",
          "cluster_id": 111013,
          "cite": [
            "77 L. Ed. 2d 1003",
            "103 S. Ct. 3319",
            "463 U.S. 765",
            "1983 U.S. LEXIS 106",
            "51 U.S.L.W. 5157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iqbal v. Hasty",
          "cluster_id": 2716,
          "cite": [
            "490 F.3d 143"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. Kemna",
          "cluster_id": 118478,
          "cite": [
            "151 L. Ed. 2d 820",
            "122 S. Ct. 877",
            "534 U.S. 362",
            "2002 U.S. LEXIS 494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Tyler:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109874 OR 9427218 OR 9427219 OR 9427220 OR 9427221) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTc3NDU5MjAwMDAwJnM9ODkwNzU1JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109874+OR+9427218+OR+9427219+OR+9427220+OR+9427221%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109874 OR 9427218 OR 9427219 OR 9427220 OR 9427221)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMjkmcz0xMTIzNTQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109874+OR+9427218+OR+9427219+OR+9427220+OR+9427221%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109874 OR 9427218 OR 9427219 OR 9427220 OR 9427221)",
        "reviewed": 17,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 17,
        "triage_read": 0,
        "triage_snippet_classified": 17
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109874 OR 9427218 OR 9427219 OR 9427220 OR 9427221)",
    "indexed_citing_opinions": 909,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109874,
        "count": 821,
        "count_source": "search"
      },
      {
        "opinion_id": 9427218,
        "count": 112,
        "count_source": "search"
      },
      {
        "opinion_id": 9427219,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427220,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427221,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1386,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-tyler.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxMzc4NzImcz05Mzc1MDIwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109874+OR+9427218+OR+9427219+OR+9427220+OR+9427221%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109874,
        "cited_id": 95698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 96230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 96902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 105919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 106962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 107889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109874,
        "cited_id": 1273756,
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
    "date_created": "2026-07-05T13:48:49Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:48:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:48:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:51:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:48:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Tyler

```
<div>
<center><b><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">436 U.S. 499</a></span> (1978)</b></center>
<center><h1>MICHIGAN<br>
v.<br>
TYLER ET AL.</h1></center>
<center>No. 76-1608.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued January 10, 1978.</center>
<center>Decided May 31, 1978.</center>
CERTIORARI TO THE SUPREME COURT OF MICHIGAN.
<p><span class="star-pagination">*501</span> <i>Jeffrey Butler</i> argued the cause <i>pro hac vice</i> for petitioner. With him on the brief was <i>L. Brooks Patterson.</i></p>
<p><i>Jesse R. Bacalis</i> argued the cause and filed a brief for respondents.</p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The respondents, Loren Tyler and Robert Tompkins, were convicted in a Michigan trial court of conspiracy to burn real property in violation of <span class="citation no-link">Mich. Comp. Laws § 750</span>.157a (1970).<sup>[1]</sup> Various pieces of physical evidence and testimony based on personal observation, all obtained through unconsented and warrantless entries by police and fire officials onto the burned premises, were admitted into evidence at the respondents' trial. On appeal, the Michigan Supreme Court reversed the convictions, holding that "the warrantless searches were unconstitutional and that the evidence obtained was therefore inadmissible." <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#584" aria-description="Citation for case: People v. Tyler">399 Mich. 564, 584</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#477" aria-description="Citation for case: People v. Tyler">250 N. W. 2d 467, 477</a></span> (1977). We granted certiorari to consider the applicability of the Fourth and Fourteenth Amendments to official entries onto fire-damaged premises. <span class="citation multiple-matches"><a href="/c/U.%20S./434/814/">434 U. S. 814</a></span>.</p>
<p></p>
<h2>I</h2>
<p>Shortly before midnight on January 21, 1970, a fire broke out at Tyler's Auction, a furniture store in Oakland County, Mich. The building was leased to respondent Loren Tyler, who conducted the business in association with respondent Robert Tompkins. According to the trial testimony of various witnesses, the fire department responded to the fire and was "just watering down smoldering embers" when Fire Chief See arrived on the scene around 2 a. m. It was Chief See's responsibility "to determine the cause and make out all reports." Chief See was met by Lt. Lawson, who informed him that two <span class="star-pagination">*502</span> plastic containers of flammable liquid had been found in the building. Using portable lights, they entered the gutted store, which was filled with smoke and steam, to examine the containers. Concluding that the fire "could possibly have been an arson," Chief See called Police Detective Webb, who arrived around 3:30 a. m. Detective Webb took several pictures of the containers and of the interior of the store, but finally abandoned his efforts because of the smoke and steam. Chief See briefly "[l]ooked throughout the rest of the building to see if there was any further evidence, to determine what the cause of the fire was." By 4 a. m. the fire had been extinguished and the firefighters departed. See and Webb took the two containers to the fire station, where they were turned over to Webb for safekeeping. There was neither consent nor a warrant for any of these entries into the building, nor for the removal of the containers. The respondents challenged the introduction of these containers at trial, but abandoned their objection in the State Supreme Court. <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#570" aria-description="Citation for case: People v. Tyler">399 Mich., at 570</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#470" aria-description="Citation for case: People v. Tyler">250 N. W. 2d, at 470</a></span>.</p>
<p>Four hours after he had left Tyler's Auction, Chief See returned with Assistant Chief Somerville, whose job was to determine the "origin of all fires that occur within the Township." The fire had been extinguished and the building was empty. After a cursory examination they left, and Somerville returned with Detective Webb around 9 a. m. In Webb's words, they discovered suspicious "burn marks in the carpet, which [Webb] could not see earlier that morning, because of the heat, steam, and the darkness." They also found "pieces of tape, with burn marks, on the stairway." After leaving the building to obtain tools, they returned and removed pieces of the carpet and sections of the stairs to preserve these bits of evidence suggestive of a fuse trail. Somerville also searched through the rubble "looking for any other signs or evidence that showed how this fire was caused." Again, there was neither consent nor a warrant for these entries and seizures. <span class="star-pagination">*503</span> Both at trial and on appeal, the respondents objected to the introduction of evidence thereby obtained.</p>
<p>On February 16 Sergeant Hoffman of the Michigan State Police Arson Section returned to Tyler's Auction to take photographs.<sup>[2]</sup> During this visit or during another at about the same time, he checked the circuit breakers, had someone inspect the furnace, and had a television repairman examine the remains of several television sets found in the ashes. He also found a piece of fuse. Over the course of his several visits, Hoffman secured physical evidence and formed opinions that played a substantial role at trial in establishing arson as the cause of the fire and in refuting the respondents' testimony about what furniture had been lost. His entries into the building were without warrants or Tyler's consent, and were for the sole purpose "of making an investigation and seizing evidence." At the trial, respondents' attorney objected to the admission of physical evidence obtained during these visits, and also moved to strike all of Hoffman's testimony "because it was got in an illegal manner."<sup>[3]</sup></p>
<p>The Michigan Supreme Court held that with only a few exceptions, any entry onto fire-damaged private property by fire or police officials is subject to the warrant requirements of the Fourth and Fourteenth Amendments. "[Once] the blaze [has been] extinguished and the firefighters have left the premises, a warrant is required to reenter and search the premises, unless there is consent or the premises have been abandoned." <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#583" aria-description="Citation for case: People v. Tyler">399 Mich., at 583</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#477" aria-description="Citation for case: People v. Tyler">250 N. W. 2d, at 477</a></span>. Applying <span class="star-pagination">*504</span> this principle, the court ruled that the series of warrantless entries that began after the blaze had been extinguished at 4 a. m. on January 22 violated the Fourth and Fourteenth Amendments.<sup>[4]</sup> It found that the "record does not factually support a conclusion that Tyler had abandoned the fire-damaged premises" and accepted the lower court's finding that "`[c]onsent for the numerous searches was never obtained from defendant Tyler.'" <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#583" aria-description="Citation for case: People v. Tyler"><i>Id.,</i> at 583, 570-571</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#476" aria-description="Citation for case: People v. Tyler">250 N. W. 2d, at 476, 470</a></span>. Accordingly, the court reversed the respondents' convictions and ordered a new trial.</p>
<p></p>
<h2>II</h2>
<p>The decisions of this Court firmly establish that the Fourth Amendment extends beyond the paradigmatic entry into a private dwelling by a law enforcement officer in search of the fruits or instrumentalities of crime. As this Court stated in <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span>, the "basic purpose of this Amendment . . . is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials." The officials may be health, fire, or building inspectors. Their purpose may be to locate and abate a suspected public nuisance, or simply to perform a routine periodic inspection. The privacy that is invaded may be <span class="star-pagination">*505</span> sheltered by the walls of a warehouse or other commercial establishment not open to the public. <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span>; <i>Marshall</i> v. <i>Barlow's, Inc., ante,</i> at 311-313. These deviations from the typical police search are thus clearly within the protection of the Fourth Amendment.</p>
<p>The petitioner argues, however, that an entry to investigate the cause of a recent fire is outside that protection because no individual privacy interests are threatened. If the occupant of the premises set the blaze, then, in the words of the petitioner's brief, his "actions show that he has no expectation of privacy" because "he has abandoned those premises within the meaning of the Fourth Amendment." And if the fire had other causes, "the occupants of the premises are treated as victims by police and fire officials." In the petitioner's view, "[t]he likelihood that they will be aggrieved by a possible intrusion into what little remains of their privacy in badly burned premises is negligible."</p>
<p>This argument is not persuasive. For even if the petitioner's contention that arson establishes abandonment be accepted, its second propositionthat innocent fire victims inevitably have no protectible expectations of privacy in whatever remains of their propertyis contrary to common experience. People may go on living in their homes or working in their offices after a fire. Even when that is impossible, private effects often remain on the fire-damaged premises. The petitioner may be correct in the view that most innocent fire victims are treated courteously and welcome inspections of their property to ascertain the origin of the blaze, but "even if true, [this contention] is irrelevant to the question whether the . . . inspection is reasonable within the meaning of the Fourth Amendment." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Camara, supra,</i> at 536</a></span>. Once it is recognized that innocent fire victims retain the protection of the Fourth Amendment, the rest of the petitioner's argument unravels. For it is, of course, impossible to justify a warrantless search on the ground of abandonment by arson <span class="star-pagination">*506</span> when that arson has not yet been proved, and a conviction cannot be used <i>ex post facto</i> to validate the introduction of evidence used to secure that same conviction.</p>
<p>Thus, there is no diminution in a person's reasonable expectation of privacy nor in the protection of the Fourth Amendment simply because the official conducting the search wears the uniform of a firefighter rather than a policeman, or because his purpose is to ascertain the cause of a fire rather than to look for evidence of a crime, or because the fire might have been started deliberately. Searches for administrative purposes, like searches for evidence of crime, are encompassed by the Fourth Amendment. And under that Amendment, "one governing principle, justified by history and by current experience, has consistently been followed: except in certain carefully defined classes of cases, a search of private property without proper consent is `unreasonable' unless it has been authorized by a valid search warrant." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Camara, supra,</i> at 528-529</a></span>. The showing of probable cause necessary to secure a warrant may vary with the object and intrusiveness of the search,<sup>[5]</sup> but the necessity for the warrant persists.</p>
<p>The petitioner argues that no purpose would be served by requiring warrants to investigate the cause of a fire. This argument is grounded on the premise that the only fact that need be shown to justify an investigatory search is that a fire of undetermined origin has occurred on those premises. The <span class="star-pagination">*507</span> petitioner contends that this consideration distinguishes this case from <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>,</i> which concerned the necessity for warrants to conduct routine building inspections. Whereas the occupant of premises subjected to an unexpected building inspection may have no way of knowing the purpose or lawfulness of the entry, it is argued that the occupant of burned premises can hardly question the factual basis for fire officials' wanting access to his property. And whereas a magistrate performs the significant function of assuring that an agency's decision to conduct a routine inspection of a particular dwelling conforms with reasonable legislative or administrative standards, he can do little more than rubberstamp an application to search fire-damaged premises for the cause of the blaze. In short, where the justification for the search is as simple and as obvious to everyone as the fact of a recent fire, a magistrate's review would be a time-consuming formality of negligible protection to the occupant.</p>
<p>The petitioner's argument fails primarily because it is built on a faulty premise. To secure a warrant to investigate the cause of a fire, an official must show more than the bare fact that a fire has occurred. The magistrate's duty is to assure that the proposed search will be reasonable, a determination that requires inquiry into the need for the intrusion on the one hand, and the threat of disruption to the occupant on the other. For routine building inspections, a reasonable balance between these competing concerns is usually achieved by broad legislative or administrative guidelines specifying the purpose, frequency, scope, and manner of conducting the inspections. In the context of investigatory fire searches, which are not programmatic but are responsive to individual events, a more particularized inquiry may be necessary. The number of prior entries, the scope of the search, the time of day when it is proposed to be made, the lapse of time since the fire, the continued use of the building, and the owner's efforts to secure it against intruders might all be relevant factors. Even though a fire victim's privacy must normally yield to the vital <span class="star-pagination">*508</span> social objective of ascertaining the cause of the fire, the magistrate can perform the important function of preventing harassment by keeping that invasion to a minimum. See <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#544" aria-description="Citation for case: See v. City of Seattle">387 U. S., at 544-545</a></span>; <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span>; <i>Marshall</i> v. <i>Barlow's, Inc., ante,</i> at 323.</p>
<p>In addition, even if fire victims can be deemed aware of the factual justification for investigatory searches, it does not follow that they will also recognize the legal authority for such searches. As the Court stated in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>,</i> "when the inspector demands entry [without a warrant], the occupant has no way of knowing whether enforcement of the municipal code involved requires inspection of his premises, no way of knowing the lawful limits of the inspector's power to search, and no way of knowing whether the inspector himself is acting under proper authorization." 387 U. S., at 532. Thus, a major function of the warrant is to provide the property owner with sufficient information to reassure him of the entry's legality. See <i>United States</i> v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick"><i>Chadwick, supra,</i> at 9</a></span>.</p>
<p>In short, the warrant requirement provides significant protection for fire victims in this context, just as it does for property owners faced with routine building inspections. As a general matter, then, official entries to investigate the cause of a fire must adhere to the warrant procedures of the Fourth Amendment. In the words of the Michigan Supreme Court: "Where the cause [of the fire] is undetermined, and the purpose of the investigation is to determine the cause and to prevent such fires from occurring or recurring, a . . . search may be conducted pursuant to a warrant issued in accordance with reasonable legislative or administrative standards or, absent their promulgation, judicially prescribed standards; if evidence of wrongdoing is discovered, it may, of course, be used to establish probable cause for the issuance of a criminal investigative search warrant or in prosecution." But "[i]f the authorities are seeking evidence to be used in a criminal prosecution, the usual standard [of probable cause] will apply." <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#584" aria-description="Citation for case: People v. Tyler">399 Mich., at 584</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#477" aria-description="Citation for case: People v. Tyler">250 N. W. 2d, at 477</a></span>. Since all <span class="star-pagination">*509</span> the entries in this case were "without proper consent" and were not "authorized by a valid search warrant," each one is illegal unless it falls within one of the "certain carefully defined classes of cases" for which warrants are not mandatory. <i>Camara,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528-529</a></span>.</p>
<p></p>
<h2>III</h2>
<p>Our decisions have recognized that a warrantless entry by criminal law enforcement officials may be legal when there is compelling need for official action and no time to secure a warrant. <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (warrantless entry of house by police in hot pursuit of armed robber); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (warrantless and unannounced entry of dwelling by police to prevent imminent destruction of evidence). Similarly, in the regulatory field, our cases have recognized the importance of "prompt inspections, even without a warrant, ... in emergency situations." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#539" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Camara, supra,</i> at 539</a></span>, citing <i>North American Cold Storage Co.</i> v. <i>Chicago,</i> <span class="citation" data-id="96902"><a href="/opinion/96902/north-american-cold-storage-co-v-city-of-chicago/" aria-description="Citation for case: North American Cold Storage Co. v. City of Chicago">211 U. S. 306</a></span> (seizure of unwholesome food); <i>Jacobson</i> v. <i>Massachusetts,</i> <span class="citation" data-id="96230"><a href="/opinion/96230/jacobson-v-massachusetts/" aria-description="Citation for case: Jacobson v. Massachusetts">197 U. S. 11</a></span> (compulsory smallpox vaccination); <i>Compagnie Francaise</i> v. <i>Board of Health,</i> <span class="citation" data-id="9417887"><a href="/opinion/95698/compagnie-francaise-de-navigation-a-vapeur-v-louisiana-state-board-of/" aria-description="Citation for case: Compagnie Francaise De Navigation a Vapeur v. Louisiana...">186 U. S. 380</a></span> (health quarantine).</p>
<p>A burning building clearly presents an exigency of sufficient proportions to render a warrantless entry "reasonable." Indeed, it would defy reason to suppose that firemen must secure a warrant or consent before entering a burning structure to put out the blaze. And once in a building for this purpose, firefighters may seize evidence of arson that is in plain view. <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 465-466</a></span>. Thus, the Fourth and Fourteenth Amendments were not violated by the entry of the firemen to extinguish the fire at Tyler's Auction, nor by Chief See's removal of the two plastic containers of flammable liquid found on the floor of one of the showrooms.</p>
<p>Although the Michigan Supreme Court appears to have accepted this principle, its opinion may be read as holding that <span class="star-pagination">*510</span> the exigency justifying a warrantless entry to fight a fire ends, and the need to get a warrant begins, with the dousing of the last flame. <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#579" aria-description="Citation for case: People v. Tyler">399 Mich., at 579</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#475" aria-description="Citation for case: People v. Tyler">250 N. W. 2d, at 475</a></span>. We think this view of the firefighting function is unrealistically narrow, however. Fire officials are charged not only with extinguishing fires, but with finding their causes. Prompt determination of the fire's origin may be necessary to prevent its recurrence, as through the detection of continuing dangers such as faulty wiring or a defective furnace. Immediate investigation may also be necessary to preserve evidence from intentional or accidental destruction. And, of course, the sooner the officials complete their duties, the less will be their subsequent interference with the privacy and the recovery efforts of the victims. For these reasons, officials need no warrant to remain in a building for a reasonable time to investigate the cause of a blaze after it has been extinguished.<sup>[6]</sup> And if the warrantless entry to put out the fire and determine its cause is constitutional, the warrantless seizure of evidence while inspecting the premises for these purposes also is constitutional.</p>
<p></p>
<h2>IV</h2>
<p></p>
<h2>A</h2>
<p>The respondents argue, however, that the Michigan Supreme Court was correct in holding that the departure by the fire <span class="star-pagination">*511</span> officials from Tyler's Auction at 4 a. m. ended any license they might have had to conduct a warrantless search. Hence, they say that even if the firemen might have been entitled to remain in the building without a warrant to investigate the cause of the fire, their re-entry four hours after their departure required a warrant.</p>
<p>On the facts of this case, we do not believe that a warrant was necessary for the early morning re-entries on January 22. As the fire was being extinguished, Chief See and his assistants began their investigation, but visibility was severely hindered by darkness, steam, and smoke. Thus they departed at 4 a. m. and returned shortly after daylight to continue their investigation. Little purpose would have been served by their remaining in the building, except to remove any doubt about the legality of the warrantless search and seizure later that same morning. Under these circumstances, we find that the morning entries were no more than an actual continuation of the first, and the lack of a warrant thus did not invalidate the resulting seizure of evidence.</p>
<p></p>
<h2>B</h2>
<p>The entries occurring after January 22, however, were clearly detached from the initial exigency and warrantless entry. Since all of these searches were conducted without valid warrants and without consent, they were invalid under the Fourth and Fourteenth Amendments, and any evidence obtained as a result of those entries must, therefore, be excluded at the respondents' retrial.</p>
<p></p>
<h2>V</h2>
<p>In summation, we hold that an entry to fight a fire requires no warrant, and that once in the building, officials may remain there for a reasonable time to investigate the cause of the blaze. Thereafter, additional entries to investigate the cause of the fire must be made pursuant to the warrant procedures governing administrative searches. See <i>Camara,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 534-539</a></span>; <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#544" aria-description="Citation for case: See v. City of Seattle">387 U. S., at 544-545</a></span>; <i>Marshall</i> v. <span class="star-pagination">*512</span> <i>Barlow's, Inc., ante,</i> at 320-321. Evidence of arson discovered in the course of such investigations is admissible at trial, but if the investigating officials find probable cause to believe that arson has occurred and require further access to gather evidence for a possible prosecution, they may obtain a warrant only upon a traditional showing of probable cause applicable to searches for evidence of crime. <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span>.</p>
<p>These principles require that we affirm the judgment of the Michigan Supreme Court ordering a new trial.<sup>[7]</sup></p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BLACKMUN joins the judgment of the Court and Parts I, III, and IV-A of its opinion.</p>
<p>MR. JUSTICE BRENNAN took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE STEVENS, concurring in part and concurring in the judgment.</p>
<p>Because Part II of the Court's opinion in this case, like the opinion in <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span>, seems to <span class="star-pagination">*513</span> assume that an official search must either be conducted pursuant to a warrant or not take place at all, I cannot join its reasoning.</p>
<p>In particular, I cannot agree with the Court's suggestion that, if no showing of probable cause could be made, "the warrant procedures governing administrative searches," <i>ante,</i> at 511, would have complied with the Fourth Amendment. In my opinion, an "administrative search warrant" does not satisfy the requirements of the Warrant Clause.<sup>[1]</sup> See <i>Marshall</i> v. <i>Barlow's, Inc., ante,</i> p. 325 (STEVENS, J., dissenting). Nor does such a warrant make an otherwise unreasonable search reasonable.</p>
<p>A warrant provides authority for an unannounced, immediate entry and search. No notice is given when an application for a warrant is made and no notice precedes its execution; when issued, it authorizes entry by force.<sup>[2]</sup> In my view, when there is no probable cause to believe a crime has been committed and when there is no special enforcement need to justify an unannounced entry,<sup>[3]</sup> the Fourth Amendment neither requires nor sanctions an abrupt and peremptory confrontation <span class="star-pagination">*514</span> between sovereign and citizen.<sup>[4]</sup> In such a case, to comply with the constitutional requirement of reasonableness, I believe the sovereign must provide fair notice of an inspection.<sup>[5]</sup></p>
<p>The Fourth Amendment interests involved in this case could have been protected in either of two waysby a warrant, if probable cause existed; or by fair notice, if neither probable cause nor a special law enforcement need existed. Since the entry on February 16 was not authorized by a warrant and not preceded by advance notice, I concur in the Court's judgment and in Parts I, III, and IV of its opinion.</p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE MARSHALL joins, concurring in part and dissenting in part.</p>
<p>I join in all but Part IV-A of the opinion, from which I dissent. I agree with the Court that:</p>
<blockquote>"[A]n entry to fight a fire requires no warrant, and that once in the building, officials may remain there for a reasonable time to investigate the cause of the blaze. Thereafter, additional entries to investigate the cause of <span class="star-pagination">*515</span> the fire must be made pursuant to the warrant procedures governing administrative searches." <i>Ante,</i> at 511.</blockquote>
<p>The Michigan Supreme Court found that the warrantless searches, at 8 and 9 a. m. were not, in fact, continuations of the earlier entry under exigent circumstances<sup>[*]</sup> and therefore ruled inadmissible all evidence derived from those searches. The Court offers no sound basis for overturning this conclusion of the state court that the subsequent re-entries were distinct from the original entry. Even if, under the Court's "reasonable time" criterion, the firemen might have stayed in the building for an additional four hoursa proposition which is by no means clearthe fact remains that the firemen did not choose to remain and continue their search, but instead locked the door and departed from the premises entirely. The fact that the firemen were willing to leave demonstrates that the exigent circumstances justifying their original warrantless entry were no longer present. The situation is thus analogous to that in <i>G. M. Leasing Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#358" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 358-359</a></span> (1977):</p>
<blockquote>"The agents' own action . . . in their delay for two days following their first entry, and for more than one day following the observation of materials being moved from the office, before they made the entry during which they seized the records, is sufficient to support the District Court's implicit finding that there were no exigent circumstances. . . ."</blockquote>
<p>To hold that some subsequent re-entries are "continuations" <span class="star-pagination">*516</span> of earlier ones will not aid firemen, but confuse them, for it will be difficult to predict in advance how a court might view a re-entry. In the end, valuable evidence may be excluded for failure to seek a warrant that might have easily been obtained.</p>
<p>Those investigating fires and their causes deserve a clear demarcation of the constitutional limits of their authority. Today's opinion recognizes the need for speed and focuses attention on fighting an ongoing blaze. The firetruck need not stop at the courthouse in rushing to the flames. But once the fire has been extinguished and the firemen have left the premises, the emergency is over. Further intrusion on private property can and should be accompanied by a warrant indicating the authority under which the firemen presume to enter and search.</p>
<p>There is another reason for holding that re-entry after the initial departure required a proper warrant. The state courts found that at the time of the first re-entry a criminal investigation was under way and that the purpose of the officers in re-entering was to gather evidence of crime. Unless we are to ignore these findings, a warrant was necessary. <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), and <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967), did not differ with <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span> (1959), that searches for criminal evidence are of special significance under the Fourth Amendment.</p>
<p>MR. JUSTICE REHNQUIST, dissenting.</p>
<p>I agree with my Brother STEVENS, for the reasons expressed in his dissenting opinion in <i>Marshall</i> v. <i>Barlow's, Inc., ante,</i> at 328, that the "Warrant Clause has no application to routine, regulatory inspections of commercial premises." Since in my opinion the searches involved in this case fall within that category, I think the only appropriate inquiry is whether they were reasonable. The Court does not dispute that the entries which occurred at the time of the fire and the next morning were entirely justified, and I see nothing to indicate that the <span class="star-pagination">*517</span> subsequent searches were not also eminently reasonable in light of all the circumstances.</p>
<p>In evaluating the reasonableness of the later searches, their most obvious feature is that they occurred after a fire which had done substantial damage to the premises, including the destruction of most of the interior. Thereafter the premises were not being used and very likely could not have been used for business purposes, at least until substantial repairs had taken place. Indeed, there is no indication in the record that after the fire Tyler ever made any attempt to secure the premises. As a result, the fire department was forced to lock up the building to prevent curious bystanders from entering and suffering injury. And as far as the record reveals, Tyler never objected to this procedure or attempted to reclaim the premises for himself.</p>
<p>Thus, regardless of whether the premises were technically "abandoned" within the meaning of the Fourth Amendment, cf. <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#241" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 241</a></span> (1960); <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924), it is clear to me that no purpose would have been served by giving Tyler notice of the intended search or by requiring that the search take place during the hours which in other situations might be considered the only "reasonable" hours to conduct a regulatory search. In fact, as I read the record, it appears that Tyler not only had notice that the investigators were occasionally entering the premises for the purpose of determining the cause of the fire, but he never voiced the slightest objection to these searches and actually accompanied the investigators on at least one occasion. App. 54-57. In fact, while accompanying the investigators during one of these searches, Tyler himself suggested that the fire very well may have been caused by arson. <i>Id.,</i> at 56. This observation, coupled with all the other circumstances, including Tyler's knowledge of, and apparent acquiescence in, the searches, would have been taken by any sensible person as an indication that Tyler thought the <span class="star-pagination">*518</span> searches ought to continue until the culprit was discovered; at the very least they indicated that he had no objection to these searches. Thus, regardless of what sources may serve to inform one's sense of what is reasonable, in the circumstances of this case I see nothing to indicate that these searches were in any way unreasonable for purposes of the Fourth Amendment.</p>
<p>Since the later searches were just as reasonable as the search the morning immediately after the fire in light of all these circumstances, the admission of evidence derived therefrom did not, in my opinion, violate respondents' Fourth and Fourteenth Amendment rights. I would accordingly reverse the judgment of the Supreme Court of Michigan which held to the contrary.</p>
<h2>NOTES</h2>
<p>[1]  In addition, Tyler was convicted of the substantive offenses of burning real property, <span class="citation no-link">Mich. Comp. Laws § 750.73</span> (1970), and burning insured property with intent to defraud, <span class="citation no-link">Mich. Comp. Laws § 750.75</span> (1970).</p>
<p>[2]  Sergeant Hoffman had entered the premises with other officials at least twice before, on January 26 and 29. No physical evidence was obtained as a result of these warrantless entries.</p>
<p>[3]  The State's case was substantially buttressed by the testimony of Oscar Frisch, a former employee of the respondents. He described helping Tyler and Tompkins move valuable items from the store and old furniture into the store a few days before the fire. He also related that the respondents had told him there would be a fire on January 21, and had instructed him to place mattresses on top of other objects so that they would burn better.</p>
<p>[4]  Having concluded that warrants should have been secured for the postfire searches, the court explained that different standards of probable cause governed searches to determine the cause of a fire and searches to gather evidence of crime. It then described what standard of probable cause should govern all the searches in this case:
</p>
<p>"While it may be no easy task under some circumstances to distinguish as a factual matter between an administrative inspection and a criminal investigation, in the instant case the Court is not faced with that task. Having lawfully discovered the plastic containers of flammable liquid and other evidence of arson before the fire was extinguished, Fire Chief See focused his attention on assembling proof of arson and began a criminal investigation. At that point there was probable cause for issuance of a criminal investigative search warrant." <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#577" aria-description="Citation for case: People v. Tyler">399 Mich., at 577</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#474" aria-description="Citation for case: People v. Tyler">250 N. W. 2d, at 474</a></span> (citations omitted).</p>
<p>[5]  For administrative searches conducted to enforce local building, health, or fire codes, "`probable cause' to issue a warrant to inspect . . . exist[s] if reasonable legislative or administrative standards for conducting an area inspection are satisfied with respect to a particular dwelling. Such standards, which will vary with the municipal program being enforced, may be based upon the passage of time, the nature of the building (<i>e. g.,</i> a multi-family apartment house), or the condition of the entire area, but they will not necessarily depend upon specific knowledge of the condition of the particular dwelling." <i>Camara,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 538</a></span>; <i>Marshall</i> v. <i>Barlow's, Inc., ante,</i> at 320-321. See LaFave, Administrative Searches and the Fourth Amendment: The Camara and See Cases, <span class="citation no-link">1967 Sup. Ct. Rev. 1</span>, 18-20.</p>
<p>[6]  The circumstances of particular fires and the role of firemen and investigating officials will vary widely. A fire in a single-family dwelling that clearly is extinguished at some identifiable time presents fewer complexities than those likely to attend a fire that spreads through a large apartment complex or that engulfs numerous buildings. In the latter situations, it may be necessary for officialspursuing their duty both to extinguish the fire and to ascertain its originto remain on the scene for an extended period of time repeatedly entering or re-entering the building or buildings, or portions thereof. In determining what constitutes a "reasonable time to investigate," appropriate recognition must be given to the exigencies that confront officials serving under these conditions, as well as to individuals' reasonable expectations of privacy.</p>
<p>[7]  The petitioner alleges that respondent Tompkins lacks standing to object to the unconstitutional searches and seizures. The Michigan Supreme Court refused to consider the State's argument, however, because the prosecutor failed to raise the issue in the trial court or in the Michigan Court of Appeals. <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#571" aria-description="Citation for case: People v. Tyler">399 Mich., at 571</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#470" aria-description="Citation for case: People v. Tyler">250 N. W. 2d, at 470-471</a></span>. We read the state court's opinion to mean that in the absence of a timely objection by the State, a defendant will be presumed to have standing. Failure to present a federal question in conformance with state procedure constitutes an adequate and independent ground of decision barring review in this Court, so long as the State has a legitimate interest in enforcing its procedural rule. <i>Henry</i> v. <i>Mississippi,</i> <span class="citation" data-id="9422929"><a href="/opinion/106962/henry-v-mississippi/#447" aria-description="Citation for case: Henry v. Mississippi">379 U. S. 443, 447</a></span>. See <i>Safeway Stores</i> v. <i>Oklahoma Grocers,</i> <span class="citation" data-id="105919"><a href="/opinion/105919/safeway-stores-inc-v-oklahoma-retail-grocers-assn-inc/" aria-description="Citation for case: Safeway Stores, Inc. v. Oklahoma Retail Grocers Assn., Inc.">360 U. S. 334</a></span>, 342 n. 7; <i>Cardinale</i> v. <i>Louisiana,</i> <span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/#438" aria-description="Citation for case: Cardinale v. Louisiana">394 U. S. 437, 438</a></span>. The petitioner does not claim that Michigan's procedural rule serves no legitimate purpose. Accordingly, we do not entertain the petitioner's standing claim which the state court refused to consider because of procedural default.</p>
<p>[1]  The Warrant Clause of the Fourth Amendment provides that "no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>[2]  See <i>Wyman</i> v. <i>James,</i> <span class="citation" data-id="9424375"><a href="/opinion/108223/wyman-v-james/#323" aria-description="Citation for case: Wyman v. James">400 U. S. 309, 323-324</a></span>. As the Court observed in <i><span class="citation" data-id="9424375"><a href="/opinion/108223/wyman-v-james/" aria-description="Citation for case: Wyman v. James">Wyman</a></span>,</i> a warrant is not simply a device providing procedural protections for the citizen; it also grants the government increased authority to invade the citizen's privacy. See <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#307" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 307-308</a></span>.</p>
<p>[3]  In this case, there obviously was a special enforcement need justifying the initial entry to extinguish the fire, and I agree that the search on the morning after the fire was a continuation of that entirely legal entry. A special enforcement need can, of course, be established on more than a case-by-case basis, especially if there is a relevant legislative determination of need. See <i>Marshall</i> v. <i>Barlow's, Inc., ante,</i> p. 325 (STEVENS, J., dissenting).</p>
<p>[4]  The Fourth Amendment ensures "[t]he right of the people to be <i>secure</i> in their persons, houses, papers, and effects, against unreasonable searches and seizures." (Emphasis added.) Surely this broad protection encompasses the expectation that the government cannot demand immediate entry when it has neither probable cause to suspect illegality nor any other pressing enforcement concern. Yet under the rationale in Part II of the Court's opinion, the less reason an officer has to suspect illegality, the less justification he need give the magistrate in order to conduct an unannounced search. Under this rationale, the police will have no incentiveindeed they have a disincentiveto establish probable cause before obtaining authority to conduct an unannounced search.</p>
<p>[5]  See LaFave, Administrative Searches and the Fourth Amendment: The Camara and See Cases, <span class="citation no-link">1967 Sup. Ct. Rev. 1</span>. The requirement of giving notice before conducting a routine administrative search is hardly unprecedented. It closely parallels existing procedures for administrative subpoenas, see, <i>e. g.,</i> <span class="citation no-link">15 U. S. C. § 1312</span> (1976 ed.), and is, as Professor LaFave points out, embodied in English law and practice. See LaFave, <i>supra,</i> at 31-32.</p>
<p>[*]  The Michigan Supreme Court recognized that "[i]f there are exigent circumstances, such as reason to believe that the destruction of evidence is imminent or that a further entry of the premises is necessary to prevent the recurrence of the fire, no warrant is required and evidence discovered is admissible." <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#578" aria-description="Citation for case: People v. Tyler">399 Mich. 564, 578</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#474" aria-description="Citation for case: People v. Tyler">250 N. W. 2d 467, 474</a></span> (1977). It found, however, that "[i]n the instant case there were no exigent circumstances justifying the searches made hours, days or weeks after the fire was extinguished." <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#579" aria-description="Citation for case: People v. Tyler"><i>Id.,</i> at 579</a></span>, <span class="citation" data-id="1273756"><a href="/opinion/1273756/people-v-tyler/#475" aria-description="Citation for case: People v. Tyler">250 N. W. 2d, at 475</a></span>.</p>

</div>
```

---

## GROUP: content/cases/Milam v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: Milam v. United States
type: case
citation: "296 F. 629 (1924)"
parallel_cite: ""
neutral_cite: 1924 U.S. App. LEXIS 3380
court: 4th Cir.
court_level: coa
circuit: ca4
year: 1924
date_decided: ""
docket: ""
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
  opinion_url: "https://www.courtlistener.com/opinion/8849836/milam-v-united-states/"
  cluster_id: 8849836
  opinion_id: null
  identity_checked: true
lake:
  record_id: Milam v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Fourth Amendment Recalibration]]"
    role: Key
related:
  - "[[Fourth Amendment Recalibration]]"
  - "[[Carroll v. United States]]"
tags:
  - case
  - fourth-amendment
  - automobile-search
  - prohibition
  - reasonableness
  - living-constitution
holding: "The meaning of 'unreasonable searches' is not fixed but changes with social, economic, and legal conditions; on that reasoning the warrantless stop and search of a truck (which turned up smuggled persons rather than the expected liquor) was not unreasonable and the evidence was competent."
---

# Milam v. United States

*296 F. 629 (4th Cir. 1924)* · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 8849836 → opinion 8835196 (296 F. 629, decided 1924-02-08 per CourtListener; the lake stub's date_decided is empty — noted for recovery). Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Federal prohibition officers, tipped that an automobile loaded with whisky was en route from Florida, watched a bridge in Dinwiddie County, Virginia, for several days. Near midnight they stopped a motor truck; when Milam said it held "nothing," an officer opened the door and instead found eighteen Chinese immigrants being unlawfully transported. Milam and codefendants were convicted, and challenged the admission of evidence obtained by the warrantless search.

## Issue
Whether the warrantless stop and search of a motor vehicle, conducted on information of criminal activity, yields inadmissible evidence, and how the reasonableness of such a search should be judged.

## Rule
Writing a year before the Supreme Court's *[[Carroll v. United States|Carroll]]* decision, the Fourth Circuit declined to extend the exclusionary rule beyond then-existing Supreme Court precedent and framed reasonableness as an evolving standard: "The constitutional expression, 'unreasonable searches,' is not fixed and absolute in meaning. The meaning in some degree must change with changing social, economic and legal conditions." — 296 F. at 631. Applying that view to a vehicle stopped on definite information, the court held: "Assuming that this was a search of the truck, under these circumstances we hold that the search was not unreasonable, and that the evidence obtained was competent." — *Id.* at 632.

## Application
The court distinguished the warrantless search of a dwelling (generally unlawful) from the search of a mobile vehicle for evidence of crime, which the Supreme Court had not condemned. Given the officers' definite information and the mobility of the truck, the intrusion was reasonable; that the officers expected liquor but found smuggled persons did not render the otherwise-valid search unlawful.

## Conclusion
The convictions were largely **affirmed** (with a modification reducing the number of conspiracies proved); the warrantless vehicle search was reasonable and its fruits admissible.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Milam* is an early marker in the Fourth Amendment's long recalibration: its statement that "unreasonable" is not a fixed quantity but shifts with conditions anticipated the mobility-based automobile reasoning the Supreme Court would adopt in *[[Carroll v. United States]]* (1925), and it illustrates how courts have repeatedly reset the reasonableness balance as technology and enforcement needs change.

## Appears on
- [[Fourth Amendment Recalibration]] — *Key*

## Sources
- [*Milam v. United States*, 296 F. 629 (4th Cir. 1924)](https://www.courtlistener.com/opinion/8849836/milam-v-united-states/) — pinpoints: 631 (the "not fixed and absolute" recalibration passage), 632 (the reasonableness holding); Rule quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fa2171f0d1f26d15", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "296 F. 629 (1924)", "court": "4th Cir.", "neutral_cite": "1924 U.S. App. LEXIS 3380", "official_citation_present": true, "parallel_cite": "", "title": "Milam v. United States", "year": "1924"}}
{"assertion_id": "b3686f886d42d893", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The meaning of 'unreasonable searches' is not fixed but changes with social, economic, and legal conditions; on that reasoning the warrantless stop and search of a truck (which turned up smuggled persons rather than the expected liquor) was not unreasonable and the evidence was competent.", "title": "Milam v. United States"}}
{"assertion_id": "d06b5162e65d8112", "dimension": "support", "kind": "home_role", "locator": {"home": "Fourth Amendment Recalibration"}, "payload": {"home": "Fourth Amendment Recalibration", "role": "Key", "title": "Milam v. United States"}}
{"assertion_id": "0524c8909b108579", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "Milam v. United States"}}
{"assertion_id": "713790f983b79624", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Milam v. United States", "varies_by_point": "false"}}
```

### lake record — Milam v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Milam v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Milam v. United States",
    "case_name_short": "Milam",
    "case_name_full": "MILAM v. UNITED STATES",
    "input_case_name": "Milam v. United States",
    "court": "4th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": null,
    "year": 1924,
    "docket": null,
    "cluster_id": 8849836,
    "lead_opinion_id": 8835196,
    "sibling_ids": [],
    "absolute_url": "/opinion/8849836/milam-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "296 F. 629",
      "volume": "296",
      "reporter": "F.",
      "page": "629",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1924 U.S. App. LEXIS 3380",
        "volume": "1924",
        "reporter": "U.S. App. LEXIS",
        "page": "3380",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "296 F. 629",
        "volume": "296",
        "reporter": "F.",
        "page": "629",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1924 U.S. App. LEXIS 3380",
        "volume": "1924",
        "reporter": "U.S. App. LEXIS",
        "page": "3380",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "296 F. 629",
    "official_selection": {
      "court_class": "coa",
      "selected": "296 F. 629",
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
    "date_created": "2026-07-07T01:37:44Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:37:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:37:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "milam-v-united-states--8849836",
      "to_record_id": "Milam v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Milam v. United States

```
<opinion type="majority">
<author id="b651-22">WOODS, Circuit Judge.</author>
<p id="AlT1">There was a general verdict of guilty on an indictment containing four counts, each charging a separate conspiracy to conceal, harbor, transport, and convey persons of Chinese descent not.duly admitted into the United Statés by an immigration inspector, nor entitled to reside in the United States. The chinaman <page-number citation-index="1" label="630">*630</page-number>mentioned in the first count was'Moy Gong Chue, alias Lee Chu; in the second, Tong Yuen, alias Poy Jong; in the third, Gee Yuen, alias Toi Lock. In the fourth count 18 Chinamen were mentioned by name, including those mentioned in the first, second, and third counts. The sentence was that the defendants—</p>
<blockquote id="b652-4">“each be imprisoned in the penitentiary at- Atlanta, Ga., for the period of two years under, each of the three counts of the indictment, said terms of imprisonment to commence in.each instance at the expiration of the term of two years on each of the three counts.”</blockquote>
<p id="b652-5">It does not clearly appear which three of the four counts was referred to in the sentence, but, as the fourth embraced the other three, it seems fair to refer the sentence to the first three counts. The court refused a motion to direct a verdict of acquittal, made on the grounds: First, that the Immigration Act of February 5, 1917 (Comp. St. 1918, Comp. St. Ann. Supp. 1919, § 4289J4a et seq.), mentioned in the indictment, does not apply to Chinese; and, second, that the court admitted evidence obtained by illegal search, without which there would have been no basis for conviction.</p>
<p id="b652-6">The first position is disposed of by the adverse decision of the Supreme Court on the precise question. United States v. Butt, <span class="citation" data-id="99635"><a href="/opinion/99635/united-states-v-butt/" aria-description="Citation for case: United States v. Butt">254 U. S. 38</a></span>, 41 Sup. Ct. 37, <span class="citation" data-id="99635"><a href="/opinion/99635/united-states-v-butt/" aria-description="Citation for case: United States v. Butt">65 L. Ed. 119</a></span>. The evidence referred to in the second ground was obtained in this way: Federal prohibition officers, having information that an automobile loaded with whisky was on its way from Florida, via Savannah, had been on the watch for several days to intercept it at a bridge in Dinwiddie county, Va. About 10 o’clock on the night of August 16, 1922, the officers, without a search warrant, stopped at the bridge a motor truck in charge of two of the defendants. In answer to the question what was in the truck, Milam, one of them, answered, “Nothing.” One of the officers then opened the door of the truck, and discovered 18 Chinamen referred to by name in the indictment.</p>
<p id="b652-7">The decisions of the Supreme Court as to the incompetency of evidence obtained by unreasonable search and seizure are too familiar for restatement or citation. As they do not control in the( enforcement of state laws, many state courts of last resort have refused to follow them. Review of the decisions, federal and state, will be found in the notes in 3 A. L. R. 1514, 13 A. L. R. 1316, and 24 A. L. R. 1408; documents 3713 and 3781, printed for use of the Judiciary Committee of the Senate; annotation of H. R. 7294; American Bar Association Journal, August, 1922, and December, 1923; 34 Harvard Law Review, 361.</p>
<p id="b652-8">Full effect must be given here to the decisions of the Supreme Court holding that evidence obtained by an unreasonable, and therefore unlawful, search is not competent. Search of a dwelling house, possibly any house, without the authority of a search warrant, the court has declared as a general rule unlawful. But it has not declared unlawful all searches without warrant. It has not declared unlawful search without warrant of motor vehicles for intoxicating liquor or other evidence of crime. Nor has the co'urt ever explicitly decided that, if officers making an unlawful search for the discovery of evidence of one <page-number citation-index="1" label="631">*631</page-number>crime find evidence of another, the evidence so unexpectedly discovered may not be used.</p>
<p id="b653-4">We are not inclined to extend the rule of exclusion of evidence obtained by unlawful search beyond the decisions of the Supreme Court. The constitutional expression, “unreasonable searches,” is not fixed and absolute in meaning. The meaning in some degree must change with changing social, economic and legal conditions. The obligation to enforce the Eighteenth Amendment is no less solemn than that to give effect to the Fourth and Fifth Amendments. The courts are therefore under the duty of deciding what is an unreasonable search of motor cars, in the light of the mandate of the Constitution that intoxicating liquors shall not be manufactured, sold, or transported for beverage purposes. Every constitutional or statutory provision must be construed, with the purpose of giving effect, if possible, to every other constitutional and statutory provision, and in view of new conditions and circumstances in the progress of the nation and the state. Downes v. Bidwell, <span class="citation" data-id="9417865"><a href="/opinion/95504/downes-v-bidwell/" aria-description="Citation for case: Downes v. Bidwell">182 U. S. 244</a></span>, 21 Sup. Ct. 770, <span class="citation" data-id="9417865"><a href="/opinion/95504/downes-v-bidwell/" aria-description="Citation for case: Downes v. Bidwell">45 L. Ed. 1088</a></span>; South Carolina v. United States, <span class="citation" data-id="9418012"><a href="/opinion/96357/south-carolina-v-united-states/" aria-description="Citation for case: South Carolina v. United States">199 U. S. 437</a></span>, 26 Sup. Ct. 110, <span class="citation" data-id="9418012"><a href="/opinion/96357/south-carolina-v-united-states/" aria-description="Citation for case: South Carolina v. United States">50 L. Ed. 261</a></span>, 4 Ann. Cas. 737; Elrod v. Moss (C. C. A. 4th Circuit) <span class="citation" data-id="8823999"><a href="/opinion/8838892/elrod-v-moss/#129" aria-description="Citation for case: Elrod v. Moss">278 Fed. 123, 129</a></span>; Agnello v. United States (C. C. A. 2d Circuit) <span class="citation" data-id="8831130"><a href="/opinion/8845856/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">290 Fed. 671</a></span>.</p>
<p id="b653-5">In view of the difficulties of enforcing the mandate of the Eighteenth Amendment and the statutes passed in pursuance of it, we cannot shut our eyes to the fact known to everybody that the traffic in intoxicating liquors is carried on chiefly by professional criminals in motor cars. Robberies and other crimes are committed, and criminals escape by their use. To hold that such motor cars must never be stopped or searched without a search warrant would be a long step by the courts in aid of the traffic outlawed by the Constitution. The argument in favor of stopping and searching without warrant motor, cars in the effort to detect robbery and other crimes and to discover stolen goods is also very strong, but with that we are not now concerned. Objections to such searches made by officers with due courtesy and judgment generally come, not from citizens interested in the observance of the law, but from criminals who invoke the Constitution as a means of concealment of crime.</p>
<p id="b653-6">Property forfeited by reason of the crime with which it is connected is not entitled to legal protection. A person in possession of forfeited property has no right to the protection of his possession, and such forfeited property is always rightfully subject to seizure on behalf of the government. United States v. Stowell, <span class="citation" data-id="92645"><a href="/opinion/92645/united-states-v-stowell/" aria-description="Citation for case: United States v. Stowell">133 U. S. 19</a></span>, 10 Sup. Ct. 244, <span class="citation" data-id="92645"><a href="/opinion/92645/united-states-v-stowell/" aria-description="Citation for case: United States v. Stowell">33 L. Ed. 555</a></span>; Taylor v. United States, <span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/#205" aria-description="Citation for case: Taylor v. United States">3 How. 197, 205</a></span>, <span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">11 L. Ed. 559</a></span>; Boyd v. United States (4th Circuit) <span class="citation" data-id="8829028"><a href="/opinion/8843807/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">286 Fed. 930</a></span>; United States v. Welsh (D. C.) <span class="citation" data-id="8806081"><a href="/opinion/8821422/united-states-v-welsh/" aria-description="Citation for case: United States v. Welsh">247 Fed. 239</a></span>. Search and seizure of automobiles without search warrant in enforcement of the National Prohibition Act (Comp. St. Ann. Supp. 1923, §■ 10138% et seq.) has been justified on this ground. United States v. Fenton (D. C.) <span class="citation" data-id="8817907"><a href="/opinion/8832920/united-states-v-fenton/" aria-description="Citation for case: United States v. Fenton">268 Fed. 221</a></span>; United States v. Bateman (D. C.) <span class="citation" data-id="8824033"><a href="/opinion/8838926/united-states-v-bateman/" aria-description="Citation for case: United States v. Bateman">278 Fed. 231</a></span>; United States v. Rembert (D. C.) <span class="citation" data-id="8827993"><a href="/opinion/8842783/united-states-v-rembert/" aria-description="Citation for case: United States v. Rembert">284 Fed. 996</a></span>. We leave in abeyance the general question of the right of an officer to search an automobile whenever and where-<page-number citation-index="1" label="632">*632</page-number>ever he sees fit, to the end that he may obtain evidence and ascertain whether the car and liquor contained in it had been forfeited.</p>
<p id="b654-4">The case before us is this: Federal prohibition officers, having definite information that professional criminals were conveying in a motor car a quantity of whisky along a certain road about a certain time, were on the watch to intercept it. They stopped the defendants’ truck, opened it, and found, instead of whisky; Chinamen in the course of unlawful transportation. Assuming that this was a search of the truck, under these circumstances we hold that the search was not unreasonable, and that the evidence obtained was competent.</p>
<p id="b654-5">We are of opinion that only two conspiracies were proved. One was to transport and conceal the 2 Chinamen, Poy Jong and Fi Fong, alias Fi Fing, brought from Cuba. There was no proof of a separate conspiracy, except as to the other 16 Chinamen. On the contrary, precisely the same proof of conspiracy was adduced as to all the other 16 in the course of transportation. Gavieres v. United States, <span class="citation" data-id="97395"><a href="/opinion/97395/gavieres-v-united-states/" aria-description="Citation for case: Gavieres v. United States">220 U. S. 338</a></span>, 31 Sup. Ct. 421, <span class="citation" data-id="97395"><a href="/opinion/97395/gavieres-v-united-states/" aria-description="Citation for case: Gavieres v. United States">55 L. Ed. 489</a></span>. It follows that the sentence should have been imposed for conviction on two counts, instead of three counts, of the indictment. The sentence, must therefore be reduced to two terms of two years each under each of two counts of the indictment.</p>
<p id="b654-6">Sentence modified.</p>
<p id="b654-7">ROSE, Circuit Judge, concurs in result.</p>
</opinion>
```

---
