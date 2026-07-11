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

## GROUP: _overhaul2/lake/cases/United States v. Place.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Place"
type: case
citation: "462 U.S. 696 (1983)"
parallel_cite: "103 S. Ct. 2637; 77 L. Ed. 2d 110; 51 U.S.L.W. 4844"
neutral_cite: 1983 U.S. LEXIS 74
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-06-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Place
  varies_by_point: false
  scope_note: "Good law. The luggage dog-sniff-is-not-a-search holding was applied in Illinois v. Caballes (2005); Florida v. Jardines (2013) held a dog sniff at a home's curtilage IS a search (trespass), a boundary on context, not an overruling. The duration holding is developed by United States v. Sharpe (no rigid time limit) and Rodriguez v. United States (no prolongation)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110979/united-states-v-place/"
  cluster_id: 110979
  opinion_id: 9429264
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — boundary"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Limiting (duration)"
related: ["[[Illinois v. Caballes]]", "[[Florida v. Jardines]]", "[[Terry v. Ohio]]", "[[Rodriguez v. United States]]", "[[United States v. Sharpe]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "seizure", "dog-sniff", "luggage", "terry-stop", "duration"]
holding: "A canine sniff of luggage in a public place is sui generis and not a search; but a 90-minute investigative seizure of the luggage exceeded the permissible limits of a Terry stop."
lake:
  record_id: United States v. Place
  status: verified
  projected_at: 2026-07-06
---

# United States v. Place

*462 U.S. 696 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
DEA agents, suspicious of Place at LaGuardia, seized his luggage when he refused to consent to a search, told him they would take it to a judge, and transported it to another airport for a dog sniff. About 90 minutes after the seizure, a trained dog alerted to one bag. Agents held the bags over the weekend, got a warrant Monday, and found cocaine. Place moved to suppress.

## Issue
(1) Whether subjecting luggage in a public place to a trained narcotics dog's sniff is a Fourth Amendment "search." (2) Whether the 90-minute seizure of the luggage on reasonable suspicion was a permissible *[[Terry v. Ohio|Terry]]*-type investigative detention.

## Rule
**Dog sniff.** A canine sniff of luggage is unique and not a search: "the canine sniff is *sui generis*. We are aware of no other investigative procedure that is so limited both in the manner in which the information is obtained and in the content of the information revealed by the procedure. Therefore, we conclude that the particular course of investigation that the agents intended to pursue here — exposure of respondent's luggage, which was located in a public place, to a trained canine — did not constitute a 'search' within the meaning of the Fourth Amendment." — 462 U.S. at 707. ^pin-707

**Duration of the seizure.** *[[Terry v. Ohio|Terry]]* principles can justify a brief seizure of luggage on reasonable suspicion, but the detention here was too long: "Under this standard, it is clear that the police conduct here exceeded the permissible limits of a *Terry*-type investigative stop. The length of the detention of respondent's luggage alone precludes the conclusion that the seizure was reasonable in the absence of probable cause." — *Id.* at 709. ^pin-709

## Application
The dog sniff itself, performed on luggage in a public airport, disclosed only the presence or absence of contraband and so was not a search. But the seizure of the bags was unreasonable: agents knew of Place's arrival hours in advance and could have arranged for a dog, yet detained his luggage roughly 90 minutes without probable cause — a detention whose length alone took it beyond the bounds of a brief investigative stop. The cocaine, the fruit of that overlong seizure, was suppressed.

## Conclusion
The dog sniff was not a search, but the 90-minute seizure of the luggage exceeded *[[Terry v. Ohio|Terry]]* and was unreasonable absent probable cause. *Place* anchors the dog-sniff doctrine and limits the permissible duration of investigative property seizures.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Dog-sniff holding applied to vehicles in [[Illinois v. Caballes]]; bounded at the home's [[Curtilage|curtilage]] by [[Florida v. Jardines]]. Duration analysis developed by [[United States v. Sharpe]] (no rigid time limit; diligence test) and [[Rodriguez v. United States]] (a stop may not be prolonged even briefly for a sniff absent reasonable suspicion).

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key — boundary*
- [[Terry Stops and Reasonable Suspicion]] — *Limiting (duration)*

## Sources
- *United States v. Place*, 462 U.S. 696 (1983) — https://www.courtlistener.com/opinion/110979/united-states-v-place/ — pinpoints: 707, 709.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "54dbcb1329eb0f7c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Place"}, "payload": {"all": [{"cite": "462 U.S. 696", "page": "696", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "462"}, {"cite": "103 S. Ct. 2637", "page": "2637", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "77 L. Ed. 2d 110", "page": "110", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "77"}, {"cite": "1983 U.S. LEXIS 74", "page": "74", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 4844", "page": "4844", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "462 U.S. 696", "official": {"cite": "462 U.S. 696", "page": "696", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "462"}, "official_selection_present": true, "record_id": "United States v. Place"}}
{"assertion_id": "2673595d7860bc5f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-707", "record_id": "United States v. Place"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-707", "pinpoint_status": "slip-only", "quote": "(2) Whether the 90-minute seizure of the luggage on reasonable suspicion was a permissible *Terry*-type investigative detention. ## Rule **Dog sniff.** A canine sniff of luggage is unique and not a search:", "quote_fidelity": "mismatch", "record_id": "United States v. Place", "star_marker": null}}
{"assertion_id": "9fa151628f405b70", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-709", "record_id": "United States v. Place"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-709", "pinpoint_status": "slip-only", "quote": "Under this standard, it is clear that the police conduct here exceeded the permissible limits of a *Terry*-type investigative stop. The length of the detention of respondent's luggage alone precludes the conclusion that the seizure was reasonable in the absence of probable cause.", "quote_fidelity": "mismatch", "record_id": "United States v. Place", "star_marker": null}}
{"assertion_id": "428b0088e10121b0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Place"}, "payload": {"as_of_content": "1983-06-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Place", "scope_note": "Good law. The luggage dog-sniff-is-not-a-search holding was applied in Illinois v. Caballes (2005); Florida v. Jardines (2013) held a dog sniff at a home's curtilage IS a search (trespass), a boundary on context, not an overruling. The duration holding is developed by United States v. Sharpe (no rigid time limit) and Rodriguez v. United States (no prolongation).", "varies_by_point": false}}
```

### lake record — United States v. Place

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Place",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Place",
    "case_name_short": "Place",
    "case_name_full": "United States v. Place",
    "input_case_name": "United States v. Place",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-06-20",
    "year": 1983,
    "docket": null,
    "cluster_id": 110979,
    "lead_opinion_id": 9429264,
    "sibling_ids": [
      110979,
      9429264,
      9429265,
      9429266
    ],
    "absolute_url": "/opinion/110979/united-states-v-place/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "462 U.S. 696",
      "volume": "462",
      "reporter": "U.S.",
      "page": "696",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2637",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 110",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "110",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4844",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4844",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 74",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "74",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "462 U.S. 696",
        "volume": "462",
        "reporter": "U.S.",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2637",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 110",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "110",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 74",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "74",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4844",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4844",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "462 U.S. 696",
    "official_selection": {
      "court_class": "scotus",
      "selected": "462 U.S. 696",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-707",
      "page": null,
      "quote": "(2) Whether the 90-minute seizure of the luggage on reasonable suspicion was a permissible *Terry*-type investigative detention. ## Rule **Dog sniff.** A canine sniff of luggage is unique and not a search:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-709",
      "page": null,
      "quote": "Under this standard, it is clear that the police conduct here exceeded the permissible limits of a *Terry*-type investigative stop. The length of the detention of respondent's luggage alone precludes the conclusion that the seizure was reasonable in the absence of probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Place",
    "varies_by_point": false,
    "scope_note": "Good law. The luggage dog-sniff-is-not-a-search holding was applied in Illinois v. Caballes (2005); Florida v. Jardines (2013) held a dog sniff at a home's curtilage IS a search (trespass), a boundary on context, not an overruling. The duration holding is developed by United States v. Sharpe (no rigid time limit) and Rodriguez v. United States (no prolongation).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane1_negative"
      },
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
        "journal_ref": "United States v. Place:lane1_negative"
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
        "journal_ref": "United States v. Place:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Darrell Mark Babcock",
          "cluster_id": 4623035,
          "cite": [
            "924 F.3d 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. Connor",
          "cluster_id": 112257,
          "cite": [
            "104 L. Ed. 2d 443",
            "109 S. Ct. 1865",
            "490 U.S. 386",
            "1989 U.S. LEXIS 2467",
            "57 U.S.L.W. 4513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Harris",
          "cluster_id": 145738,
          "cite": [
            "167 L. Ed. 2d 686",
            "127 S. Ct. 1769",
            "550 U.S. 372",
            "2007 U.S. LEXIS 4748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Palmer",
          "cluster_id": 111252,
          "cite": [
            "82 L. Ed. 2d 393",
            "104 S. Ct. 3194",
            "468 U.S. 517",
            "1984 U.S. LEXIS 143",
            "52 U.S.L.W. 5052"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Garner",
          "cluster_id": 111397,
          "cite": [
            "85 L. Ed. 2d 1",
            "105 S. Ct. 1694",
            "471 U.S. 1",
            "1985 U.S. LEXIS 195",
            "53 U.S.L.W. 4410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullenix v. Luna",
          "cluster_id": 3153112,
          "cite": [
            "577 U.S. 7",
            "136 S. Ct. 305",
            "193 L. Ed. 2d 255",
            "2015 U.S. LEXIS 7160",
            "84 U.S.L.W. 4003",
            "25 Fla. L. Weekly Fed. S 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jacobsen",
          "cluster_id": 111143,
          "cite": [
            "80 L. Ed. 2d 85",
            "104 S. Ct. 1652",
            "466 U.S. 109",
            "1984 U.S. LEXIS 53",
            "52 U.S.L.W. 4414"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segura v. United States",
          "cluster_id": 111259,
          "cite": [
            "82 L. Ed. 2d 599",
            "104 S. Ct. 3380",
            "468 U.S. 796",
            "1984 U.S. LEXIS 150",
            "52 U.S.L.W. 5128"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Hicks",
          "cluster_id": 111834,
          "cite": [
            "94 L. Ed. 2d 347",
            "107 S. Ct. 1149",
            "480 U.S. 321",
            "1987 U.S. LEXIS 1056",
            "55 U.S.L.W. 4258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 2419717,
          "cite": [
            "947 S.W.2d 240",
            "1997 Tex. Crim. App. LEXIS 43",
            "1997 WL 292676"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110979 OR 9429264 OR 9429265 OR 9429266) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI2NTE1MjAwMDAwJnM9NDQ5OTAxOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110979+OR+9429264+OR+9429265+OR+9429266%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110979 OR 9429264 OR 9429265 OR 9429266)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NDUmcz0yMzE2NjU4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110979+OR+9429264+OR+9429265+OR+9429266%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110979 OR 9429264 OR 9429265 OR 9429266)",
        "reviewed": 74,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 74,
        "triage_read": 1,
        "triage_snippet_classified": 73
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110979 OR 9429264 OR 9429265 OR 9429266)",
    "indexed_citing_opinions": 2066,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110979,
        "count": 1822,
        "count_source": "search"
      },
      {
        "opinion_id": 9429264,
        "count": 275,
        "count_source": "search"
      },
      {
        "opinion_id": 9429265,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429266,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3379,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-place.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNDI4NjImcz0xMDM1MDM5NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110979+OR+9429264+OR+9429265+OR+9429266%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110979,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 394856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 1652001,
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
    "date_created": "2026-07-06T02:17:45Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:18:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:18:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:21:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:18:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Place

```
<opinion type="majority">
<author id="b741-11">Justice O’Connor</author>
<p id="Abc">delivered the opinion of the Court.</p>
<p id="b741-12">This case presents the issue whether the Fourth Amendment prohibits law enforcement authorities from temporarily <page-number citation-index="1" label="698">*698</page-number>detaining personal luggage for exposure to a trained narcotics detection dog on the basis of reasonable suspicion that the luggage contains narcotics. Given the enforcement problems associated with the detection of narcotics trafficking and the minimal intrusion that a properly limited detention would entail, we conclude that the Fourth Amendment does not prohibit such a detention. On the facts of this case, however, we hold that the police conduct exceeded the bounds of a permissible investigative detention of the luggage.</p>
<p id="AHiy">pH</p>
<p id="ATD">Respondent Raymond J. Place’s behavior aroused the suspicions of law enforcement officers as he waited in line at the Miami International Airport to purchase a ticket to New York’s La Guardia Airport. As Place proceeded to the gate for his flight, the agents approached him and requested his airline ticket and some identification. Place complied with the request and consented to a search of the two suitcases he had checked. Because his flight was about to depart, however, the agents decided not to search the luggage.</p>
<p id="Ano">Prompted by Place’s parting remark that he had recognized that they were police, the agents inspected the address tags on the checked luggage and noted discrepancies in the two street addresses. Further investigation revealed that neither address existed and that the telephone number Place had given the airline belonged to a third address on the same street. On the basis of their encounter with Place and this information, the Miami agents called Drug Enforcement Administration (DEA) authorities in New York to relay their information about Place.</p>
<p id="AJD">Two DEA agents waited for Place at the arrival gate at La Guardia Airport in New York. There again, his behavior aroused the suspicion of the agents. After he had claimed his two bags and called a limousine, the agents decided to approach him. They identified themselves as federal narcotics agents, to which Place responded that he knew they were “cops” and had spotted them as soon as he had deplaned. <page-number citation-index="1" label="699">*699</page-number>One of the agents informed Place that, based on their own observations and information obtained from the Miami authorities, they believed that he might be carrying narcotics. After identifying the bags as belonging to him, Place stated that a number of police at the Miami Airport had surrounded him and searched his baggage. The agents responded that their information was to the contrary. The agents requested and received identification from Place — a New Jersey driver’s license, on which the agents later ran a computer check that disclosed no offenses, and his airline ticket receipt. When Place refused to consent to a search of his luggage, one of the agents told him that they were going to take the luggage to a federal judge to try to obtain a search warrant and that Place was free to accompany them. Place declined, but obtained from one of the agents telephone numbers at which the agents could be reached.</p>
<p id="b743-5">The agents then took the bags to Kennedy Airport, where they subjected the bags to a “sniff test” by a trained narcotics detection dog. The dog reacted positively to the smaller of the two bags but ambiguously to the larger bag. Approximately 90 minutes had elapsed since the seizure of respondent’s luggage. Because it was late on a Friday afternoon, the agents retained the luggage until Monday morning, when they secured a search warrant from a Magistrate for the smaller bag. Upon opening that bag, the agents discovered 1,125 grams of cocaine.</p>
<p id="b743-6">Place was indicted for possession of cocaine with intent to distribute in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). In the District Court, Place moved to suppress the contents of the luggage seized from him at La Guardia Airport, claiming that the warrantless seizure of the luggage violated his Fourth Amendment rights.<footnotemark>1</footnotemark> The District Court denied the motion. <page-number citation-index="1" label="700">*700</page-number>Applying the standard of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), to the detention of personal property, it concluded that detention of the bags could be justified if based on reasonable suspicion to believe that the bags contained narcotics. Finding reasonable suspicion, the District Court held that Place’s Fourth Amendment rights were not violated by seizure of the bags by the DEA agents. <span class="citation" data-id="1652001"><a href="/opinion/1652001/united-states-v-place/#1228" aria-description="Citation for case: United States v. Place">498 F. Supp. 1217, 1228</a></span> (EDNY 1980). Place pleaded guilty to the possession charge, reserving the right to appeal the denial of his motion to suppress.</p>
<p id="b744-5">On appeal of the conviction, the United States Court of Appeals for the Second Circuit reversed. <span class="citation" data-id="9468411"><a href="/opinion/394856/united-states-v-raymond-j-place/" aria-description="Citation for case: United States v. Raymond J. Place">660 F. 2d 44</a></span> (1981). The majority assumed both that <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>principles could be applied to justify a warrantless seizure of baggage on less than probable cause and that reasonable suspicion existed to justify the investigatory stop of Place. The majority concluded, however, that the prolonged seizure of Place’s baggage exceeded the permissible limits of a Terry-type investigative stop and consequently amounted to a seizure without probable cause in violation of the Fourth Amendment.</p>
<p id="b744-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./457/1104/">457 U. S. 1104</a></span> (1982), and now affirm.</p>
<p id="b744-7">) — I h — I</p>
<p id="AgL">The Fourth Amendment protects the “right of the people to be secure in their persons, houses, papers, <em>and effects, </em>against unreasonable searches and seizures.” (Emphasis added.) Although in the context of personal property, and particularly containers, the Fourth Amendment challenge is <page-number citation-index="1" label="701">*701</page-number>typically to the subsequent search of the container rather than to its initial seizure by the authorities, our cases reveal some general principles regarding seizures. In the ordinary case, the Court has viewed a seizure of personal property as <em>per se </em>unreasonable within the meaning of the Fourth Amendment unless it is accomplished pursuant to a judicial warrant issued upon probable cause and particularly describing the items to be seized.<footnotemark>2</footnotemark> See, <em>e. g., Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span> (1927). Where law enforcement authorities have probable cause to believe that a container holds contraband or evidence of a crime, but have not secured a warrant, the Court has interpreted the Amendment to permit seizure of the property, pending issuance of a warrant to examine its contents, if the exigencies of the circumstances demand it or some other recognized exception to the warrant requirement is present. See, <em>e. g., Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#761" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 761</a></span> (1979); <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977); <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971).<footnotemark>3</footnotemark> For example, “objects such as weapons or contraband found in a public place may be seized by the police without a warrant,” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980), because, under these circumstances, the risk of the item’s disappearance or use for its intended purpose before a <page-number citation-index="1" label="702">*702</page-number>warrant may be obtained outweighs the interest in possession. See also <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#354" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 354</a></span> (1977).</p>
<p id="b746-5">In this case, the Government asks us to recognize the reasonableness under the Fourth Amendment of warrantless seizures of personal luggage from the custody of the owner on the basis of less than probable cause, for the purpose of pursuing a limited course of investigation, short of opening the luggage, that would quickly confirm or dispel the authorities’ suspicion. Specifically, we are asked to apply the principles of <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra,</a></span> </em>to permit such seizures on the basis of reasonable, articulable suspicion, premised on objective facts, that the luggage contains contraband or evidence of a crime. In our view, such application is appropriate.</p>
<p id="b746-6">In <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>the Court first recognized “the narrow authority of police officers who suspect criminal activity to make limited intrusions on an individual’s personal security based on less than probable cause.” <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#698" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 698</a></span> (1981). In approving the limited search for weapons, or “frisk,” of an individual the police reasonably believed to be armed and dangerous, the Court implicitly acknowledged the authority of the police to make a <em>forcible stop </em>of a person when the officer has reasonable, articulable suspicion that the person has been, is, or is about to be engaged in criminal activity. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>.<footnotemark>4</footnotemark> That implicit proposition was embraced openly in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972), where the Court relied on <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>to hold that the police officer lawfully made a forcible stop of the suspect to investigate an informant’s tip that the suspect was carry<page-number citation-index="1" label="703">*703</page-number>ing narcotics and a concealed weapon. See also <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers, supra</a></span> </em>(limited detention of occupants while authorities search premises pursuant to valid search warrant); <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U. S. 411</a></span> (1981) (stop near border of vehicle suspected of transporting illegal aliens); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975) (brief investigative stop near border for questioning about citizenship and immigration status).</p>
<p id="b747-4">The exception to the probable-cause requirement for limited seizures of the person recognized in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and its progeny rests on a balancing of the competing interests to determine the reasonableness of the type of seizure involved within the meaning of “the Fourth Amendment’s general proscription against unreasonable searches and seizures.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>. We must balance the nature and quality of the intrusion on the individual’s Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion. When the nature and extent of the detention are minimally intrusive of the individual’s Fourth Amendment interests, the opposing law enforcement interests can support a seizure based on less than probable cause.</p>
<p id="b747-5">We examine first the governmental interest offered as a justification for a brief seizure of luggage from the suspect’s custody for the purpose of pursuing a limited course of investigation. The Government contends that, where the authorities possess specific and articulable facts warranting a reasonable belief that a traveler’s luggage contains narcotics, the governmental interest in seizing the luggage briefly to pursue further investigation is substantial. We agree. As observed in <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#561" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 561</a></span> (1980) (opinion of Powell, J.), “[t]he public has a compelling interest in detecting those who would traffic in deadly drugs for personal profit.”</p>
<p id="b747-6">Respondent suggests that, absent some special law enforcement interest such as officer safety, a generalized interest in law enforcement cannot justify an intrusion on an individual’s Fourth Amendment interests in the absence of <page-number citation-index="1" label="704">*704</page-number>probable cause. Our prior cases, however, do not support this proposition. In <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>we described the governmental interests supporting the initial seizure of the person as “effective crime prevention and detection; it is this interest which underlies the recognition that a police officer may in appropriate circumstances and in an appropriate manner approach a person for purposes of investigating possibly criminal behavior even though there is no probable cause to make an arrest.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>. Similarly, in <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>we identified three law enforcement interests that justified limited detention of the occupants of the premises during execution of a valid search warrant: “preventing flight in the event that incriminating evidence is found,” “minimizing the risk of harm” both to the officers and the occupants, and “orderly completion of the search.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 702-703</a></span>. Cf. <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality opinion) (“The predicate permitting seizures on suspicion short of probable cause is that law enforcement interests warrant a limited intrusion on the personal security of the suspect”). The test is whether those interests are sufficiently “substantial,” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#699" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 699</a></span>, not whether they are independent of the interest in investigating crimes effectively and apprehending suspects. The context of a particular law enforcement practice, of course, may affect the determination whether a brief intrusion on Fourth Amendment interests on less than probable cause is essential to effective criminal investigation. Because of the inherently transient nature of drug courier activity at airports, allowing police to make brief investigative stops of persons at airports on reasonable suspicion of drug-trafficking substantially enhances the likelihood that police will be able to prevent the flow of narcotics into distribution channels.<footnotemark>5</footnotemark></p>
<p id="b749-4"><page-number citation-index="1" label="705">*705</page-number>Against this strong governmental interest, we must weigh the nature and extent of the intrusion upon the individual’s Fourth Amendment rights when the police briefly detain luggage for limited investigative purposes. On this point, respondent Place urges that the rationale for a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop of the person is wholly inapplicable to investigative detentions of personalty. Specifically, the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>exception to the probable-cause requirement is premised on the notion that a <em>Terry-type </em>stop of the person is substantially less intrusive of a person’s liberty interests than a formal arrest. In the property context, however, Place urges, there are no degrees of intrusion. Once the owner’s property is seized, the dispossession is absolute.</p>
<p id="b749-5">We disagree. The intrusion on possessory interests occasioned by a seizure of one’s personal effects can vary both in its nature and extent. The seizure may be made after the owner has relinquished control of the property to a third party or, as here, from the immediate custody and control of the owner.<footnotemark>6</footnotemark> Moreover, the police may confine their investi<page-number citation-index="1" label="706">*706</page-number>gation to an on-the-spot inquiry — for example, immediate exposure of the luggage to a trained narcotics detection dog<footnotemark>7</footnotemark>— or transport the property to another location. Given the fact that seizures of property can vary in intrusiveness, some brief detentions of personal effects may be so minimally intrusive of Fourth Amendment interests that strong countervailing governmental interests will justify a seizure based only on specific articulable facts that the property contains contraband or evidence of a crime.</p>
<p id="b750-5">In sum, we conclude that when an officer’s observations lead him reasonably to believe that a traveler is carrying luggage that contains narcotics, the principles of <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and its progeny would permit the officer to detain the luggage briefly to investigate the circumstances that aroused his suspicion, provided that the investigative detention is properly limited in scope.</p>
<p id="b750-6">The purpose for which respondent’s luggage was seized, of course, was to <em>arrange </em>its exposure to a narcotics detection dog. Obviously, if this investigative procedure is itself a search requiring probable cause, the initial seizure of respondent’s luggage for the purpose of subjecting it to the sniff test — no matter how brief — could not be justified on less than probable cause. See <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>; <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#421" aria-description="Citation for case: United States v. Cortez">449 U. S., at 421</a></span>; <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 881-882</a></span>; <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S., at 146</a></span>.</p>
<p id="b750-7">The Fourth Amendment “protects people from unreasonable government intrusions into their legitimate expectations <page-number citation-index="1" label="707">*707</page-number>of privacy.” <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 7</a></span>. We have affirmed that a person possesses a privacy interest in the contents of personal luggage that is protected by the Fourth Amendment. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick"><em>Id., </em>at 13</a></span>. A “canine sniff” by a well-trained narcotics detection dog, however, does not require opening the luggage. It does not expose noncontraband items that otherwise would remain hidden from public view, as does, for example, an officer’s rummaging through the contents of the luggage. Thus, the manner in which information is obtained through this investigative technique is much less intrusive than a typical search. Moreover, the sniff discloses only the presence or absence of narcotics, a contraband item. Thus, despite the fact that the sniff tells the authorities something about the contents of the luggage, the information obtained is limited. This limited disclosure also ensures that the owner of the property is not subjected to the embarrassment and inconvenience entailed in less discriminate and more intrusive investigative methods.</p>
<p id="Axx">In these respects, the canine sniff is <em>sui generis. </em>We are aware of no other investigative procedure that is so limited both in the manner in which the information is obtained and in the content of the information revealed by the procedure. Therefore, we conclude that the particular course of investigation that the agents intended to pursue here — exposure of respondent’s luggage, which was located in a public place, to a trained canine — did not constitute a “search” within the meaning of the Fourth Amendment.</p>
<p id="A6V"><em>S </em>HH H-Í</p>
<p id="AHj">There is no doubt that the agents made a “seizure of Place’s luggage for purposes of the Fourth Amendment when, following his refusal to consent to a search, the agent told Place that he was going to take the luggage to a federal judge to secure issuance of a warrant. As we observed in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>“[t]he manner in which the seizure . . . [was] con<page-number citation-index="1" label="708">*708</page-number>ducted is, of course, as vital a part of the inquiry as whether [it was] warranted at all.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 28</a></span>. We therefore examine whether the agents’ conduct in this case was such as to place the seizure within the general rule requiring probable cause for a seizure or within <em>Terry’s </em>exception to that rule.</p>
<p id="b752-5">At the outset, we must reject the Government’s suggestion that the point at which probable cause for seizure of luggage from the person’s presence becomes necessary is more distant than in the case of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop of the person himself. The premise of the Government’s argument is that seizures of property are generally less intrusive than seizures of the person. While true in some circumstances, that premise is faulty on the facts we address in this case. The precise type of detention we confront here is seizure of personal luggage from the immediate possession of the suspect for the purpose of arranging exposure to a narcotics detection dog. Particularly in the case of detention of luggage within the traveler’s immediate possession, the police conduct intrudes on both the suspect’s possessory interest in his luggage as well as his liberty interest in proceeding with his itinerary. The person whose luggage is detained is technically still free to continue his travels or carry out other personal activities pending release of the luggage. Moreover, he is not subjected to the coercive atmosphere of a custodial confinement or to the public indignity of being personally detained. Nevertheless, such a seizure can effectively restrain the person since he is subjected to the possible disruption of his travel plans in order to remain with his luggage or to arrange for its return.<footnotemark>8</footnotemark> Therefore, when the police seize luggage from the <page-number citation-index="1" label="709">*709</page-number>suspect’s custody, we think the limitations applicable to investigative detentions of the person should define the permissible scope of an investigative detention of the person’s luggage on less than probable cause. Under this standard, it is clear that the police conduct here exceeded the permissible limits of a Terry-type investigative stop.</p>
<p id="b753-5">The length of the detention of respondent’s luggage alone precludes the conclusion that the seizure was reasonable in the absence of probable cause. Although we have recognized the reasonableness of seizures longer than the momentary ones involved in <em>Terry, Adams, </em>and <em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>, </em>see <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692</a></span> (1981), the brevity of the invasion of the individual’s Fourth Amendment interests is an important factor in determining whether the seizure is so minimally intrusive as to be justifiable on reasonable suspicion. Moreover, in assessing the effect of the length of the detention, we take into account whether the police diligently pursue their investigation. We note that here the New York agents knew the time of Place’s scheduled arrival at La Guardia, had ample time to arrange for their additional investigation at that location, and thereby could have minimized the intrusion on respondent’s Fourth Amendment interests.<footnotemark>9</footnotemark> Thus, although we decline to adopt any outside time limitation for a permissible <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop,<footnotemark>10</footnotemark> we have never <page-number citation-index="1" label="710">*710</page-number>approved a seizure of the person for the prolonged 90-minute period involved here and cannot do so on the facts presented by this case. See <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979).</p>
<p id="b754-5">Although the 90-minute detention of respondent’s luggage is sufficient to render the seizure unreasonable, the violation was exacerbated by the failure of the agents to accurately inform respondent of the place to which they were transporting his luggage, of the length of time he might be dispossessed, and of what arrangements would be made for return of the luggage if the investigation dispelled the suspicion. In short, we hold that the detention of respondent’s luggage in this case went beyond the narrow authority possessed by police to detain briefly luggage reasonably suspected to contain narcotics.</p>
<p id="b754-6">
<em>&gt;</em>
</p>
<p id="AXDH">We conclude that, under all of the circumstances of this case, the seizure of respondent’s luggage was unreasonable under the Fourth Amendment. Consequently, the evidence obtained from the subsequent search of his luggage was inadmissible, and Place’s conviction must be reversed. The judgment of the Court of Appeals, accordingly, is affirmed.</p>
<p id="Ab0">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b743-7"> In support of his motion, respondent also contended that the detention of his person at both the Miami and La Guardia Airports was not based on reasonable suspicion and that the “sniff test” of his luggage was conducted in a manner that tainted the dog’s reaction. <span class="citation" data-id="1652001"><a href="/opinion/1652001/united-states-v-place/#1221" aria-description="Citation for case: United States v. Place">498 F. Supp. 1217, 1221, 1228</a></span> <page-number citation-index="1" label="700">*700</page-number>(EDNY 1980). The District Court rejected both contentions. As to the former, it concluded that the agents had reasonable suspicion to believe that Place was engaged in criminal activity when he was detained at the two airports and that the stops were therefore lawful. <span class="citation" data-id="1652001"><a href="/opinion/1652001/united-states-v-place/#1225" aria-description="Citation for case: United States v. Place"><em>Id., </em>at 1225, 1226</a></span>. On appeal, the Court of Appeals did not reach this issue, assuming the existence of reasonable suspicion. Respondent Place cross-petitioned in this Court on the issue of reasonable suspicion, and we denied certiorari. <em>Place </em>v. <em>United States, </em><span class="citation" data-id="9032763"><a href="/opinion/9039428/place-v-united-states/" aria-description="Citation for case: Place v. United States">457 U. S. 1106</a></span> (1982). We therefore have no occasion to address the issue here.</p>
</footnote>
<footnote label="2">
<p id="b745-5"> The Warrant Clause of the Fourth Amendment provides that “no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</p>
</footnote>
<footnote label="3">
<p id="b745-6"> In <em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>, </em>the Court explained:</p>
<blockquote id="b745-7">“The police acted properly — indeed commendably — in apprehending respondent and his luggage. They had ample probable cause to believe that respondent’s green suitcase contained marihuana. . . . Having probable cause to believe that contraband was being driven away in the taxi, the police were justified in stopping the vehicle . . . and seizing the suitcase they suspected contained contraband.” 442 U. S., at 761.</blockquote>
<p id="b745-8">The Court went on to hold that the police violated the Fourth Amendment in immediately searching the luggage rather than first obtaining a warrant authorizing the search. <em>Id., </em>at 766. That holding was not affected by our recent decision in <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 824</a></span> (1982).</p>
</footnote>
<footnote label="4">
<p id="b746-7"><em> </em>In his concurring opinion in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>Justice Harlan made this logical underpinning of the Court’s Fourth Amendment holding clear:</p>
<blockquote id="b746-8">“In the first place, if the frisk is justified in order to protect the officer during an encounter with a citizen, the officer must first have constitutional grounds to insist on an encounter, to make a <em>forcible </em>stop. ... I would make it perfectly clear that the right to frisk in this case depends upon the reasonableness of a forcible stop to investigate a suspected crime.” 892 U. S., at 32-33.</blockquote>
</footnote>
<footnote label="5">
<p id="b748-5"> Referring to the problem of intercepting drug couriers in the Nation’s airports, Justice Powell has observed:</p>
<blockquote id="b748-6">“Much of the drug traffic is highly organized and conducted by sophisticated criminal syndicates. The profits are enormous. And many drugs . . . may be easily concealed. As a result, the obstacles to detection of <page-number citation-index="1" label="705">*705</page-number>illegal conduct may be unmatched in any other area of law enforcement.” <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#561" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 561-562</a></span> (1980).</blockquote>
<p id="b749-8">See <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#519" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 519</a></span> (1983) (Blackmun, J., dissenting) (“The special need for flexibility in uncovering illicit drug couriers is hardly debatable”) (airport context).</p>
</footnote>
<footnote label="6">
<p id="b749-11"> One need only compare the facts of this case with those in <em>United States </em>v. <em>Van Leeuwen, </em><span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span> (1970). There the defendant had voluntarily relinquished two packages of coins to the postal authorities. Several facts aroused the suspicion of the postal officials, who detained the packages, without searching them, for about 29 hours while certain lines of inquiry were pursued. The information obtained during this time was sufficient to give the authorities probable cause to believe that the packages contained counterfeit coins. After obtaining a warrant, the authorities opened the packages, found counterfeit coins therein, resealed the packages, and sent them on their way. Expressly limiting its holding to the facts of the case, the Court concluded that the 29-hour detention of the packages on reasonable suspicion that they contained contraband did not violate the Fourth Amendment. <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#253" aria-description="Citation for case: United States v. Van Leeuwen"><em>Id., </em>at 253</a></span>.</p>
<p id="b749-12">As one commentator has noted, <em>“Van Leeuwen </em>was an easy case for the Court because the defendant was unable to show that the invasion intruded <page-number citation-index="1" label="706">*706</page-number>upon either a privacy interest in the contents of the packages or a posses-sory interest in the packages themselves.” 3 W. LaFave, Search and Seizure § 9.6, p. 71 (Supp. 1982).</p>
</footnote>
<footnote label="7">
<p id="b750-11"> Cf. <em>Florida </em>v. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer"><em>Royer, supra, </em>at 502</a></span> (plurality opinion) (“We agree with the State that [the officers had] adequate grounds for suspecting Royer of carrying drugs and for temporarily detaining him <em>and his luggage </em>while they attempted to verify or dispel their suspicions in a manner that did not exceed the limits of an investigative detention”) (emphasis added).</p>
</footnote>
<footnote label="8">
<p id="b752-6"> “At least when the authorities do not make it absolutely clear how they plan to reunite the suspect and his possessions at some future time and place, seizure of the object is tantamount to seizure of the person. This is because that person must either remain on the scene or else seemingly surrender his effects permanently to the police.” 3 W. LaFave, Search and Seizure § 9.6, p. 72 (Supp. 1982).</p>
</footnote>
<footnote label="9">
<p id="b753-6"> Cf. <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#506" aria-description="Citation for case: Florida v. Royer">460 U. S., at 506</a></span> (plurality opinion) (“If [trained narcotics detection dogs] had been used, Royer and his luggage could have been momentarily detained while this investigative procedure was carried out”). This course of conduct also would have avoided the further substantial intrusion on respondent’s possessory interests caused by the removal of his luggage to another location.</p>
</footnote>
<footnote label="10">
<p id="b753-7"> Cf. ALI, Model Code of Pre-Arraignment Procedure § 110.2(1) (1975) (recommending a maximum of 20 minutes for a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop). We understand the desirability of providing law enforcement authorities with a clear rule to guide their conduct. Nevertheless, we question the wisdom of a rigid time limitation. Such a limit would undermine the equally important need to allow authorities to graduate their responses to the demands of any particular situation.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Porter.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: United States v. Porter
type: case
citation: "No. 25-60163, slip op. (5th Cir. 2026)"
parallel_cite: ""
neutral_cite: ""
court: 5th Cir.
court_level: coa
circuit: ca5
year: 2026
date_decided: 2026-03-17
docket: 25-60163
authority_weight: "Binding in-circuit — 5th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/10810059/united-states-v-porter/"
  cluster_id: 10810059
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Porter
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Lower-court development (ALPR)"
related:
  - "[[Carpenter v. United States]]"
  - "[[United States v. Knotts]]"
  - "[[Terry Stops and Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - license-plate-reader
  - digital-surveillance
  - plain-view
  - reasonable-suspicion
  - fifth-circuit
holding: "A police officer's use of a fixed license plate reader (LPR) to detect that a vehicle passed a public intersection is not a Fourth Amendment search and requires no warrant; the ensuing traffic stop was supported by reasonable suspicion, the officer lawfully seized a firearm and machinegun conversion switch he saw in plain view, and circuit precedent foreclosed the Second Amendment challenge, so the machinegun conviction was affirmed."
aliases:
  - United States v. Porter
  - "United States v. Porter (5th Cir. 2026)"
  - United States v. Elijah Porter
---

# United States v. Porter

*No. 25-60163, slip op. (5th Cir. 2026)* · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10810059 → published opinion 11276804 (Smith, J.; No. 25-60163, decided Mar. 17, 2026). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (published 5th Cir. slip; no F.4th reporter cite assigned yet — S2 A3). S9 promotes. -->

## Background
While on patrol in Gautier, Mississippi, Officer Hoggard received an LPR alert that a plate associated with criminal activity had passed a particular intersection; dispatch tied the vehicle to Elijah Porter, who had an outstanding aggravated-assault warrant. A computer check corroborated the association, and Hoggard located and stopped the vehicle. After identifying Porter and patting him down, Hoggard saw a firearm protruding from under the driver's seat with "a little silver switch" he took to be a machinegun conversion device; he later retrieved the Glock and switch during an inventory search. Porter was charged under 18 U.S.C. § 922(o) and moved to suppress the LPR data and the firearm.

## Issue
Whether the officer's use of an LPR to detect Porter's vehicle was a Fourth Amendment search, and whether the stop and seizure of the firearm were lawful.

## Rule
The court disposed of the Fourth Amendment claims and the § 922(o) challenge together at the outset: "Because the use of an LPR did not constitute a search, no warrant was required; the stop was supported by reasonable suspicion, and the officer found the Glock and its machinegun conversion switch in plain view. Our circuit precedent forecloses Porter's Second Amendment challenge. We affirm." — slip op. at 1. ^pin-slip1

## Application
Detecting a plate as the vehicle passed a fixed public-road camera revealed only a vehicle's public movement and did not invade a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]], so it was no search and needed no warrant. The LPR alert plus the confirmed link to a person with an active warrant supplied reasonable suspicion (indeed probable cause) for the stop. Once Porter was stopped, the barrel and switch were visible under the seat, bringing the firearm within the [[Plain View Doctrine|plain-view doctrine]]; its incriminating character (an apparent automatic Glock) was immediately apparent.

## Conclusion
**Affirmed.** Judge Jerry E. Smith wrote for the panel (Smith, Wiener, Higginson, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Porter* sits alongside *[[Robinson v. Commonwealth]]* on the ALPR frontier: like Norfolk's Flock system, a fixed LPR that captures a plate on a public road is treated as no search under the public-movements logic of *[[United States v. Knotts|Knotts]]*, distinguished from the pervasive tracking that made *[[Carpenter v. United States|Carpenter]]* a search.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Lower-court development (ALPR)*

## Sources
- [*United States v. Porter*, No. 25-60163, slip op. (5th Cir. 2026)](https://www.courtlistener.com/opinion/10810059/united-states-v-porter/) — pinpoint: slip op. at 1 (LPR use is not a search; plain-view firearm seizure; reasonable-suspicion stop). Rule quote string-matched to the CL opinion text 2026-07-07. Published 5th Cir. slip; no F.4th cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7f9c428dfe348b84", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Porter"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Porter", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Porter

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Porter",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Porter",
    "case_name_short": "Porter",
    "case_name_full": "",
    "input_case_name": "United States v. Porter",
    "court": "5th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": "2026-03-17",
    "year": 2026,
    "docket": "25-60163",
    "cluster_id": 10810059,
    "lead_opinion_id": 11276804,
    "sibling_ids": [],
    "absolute_url": "/opinion/10810059/united-states-v-porter/",
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
      "note": "W9 slip disposition. United States v. Porter (Elijah Porter), 5th Cir. PUBLISHED slip No. 25-60163, decided 2026-03-17 (ALPR identification / plain-view firearm). CL cluster 10810059 Published, citations[] empty (live-verified 2026-07-07); no F.4th cite assigned yet.",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://www.ca5.uscourts.gov/opinions/pub/25/25-60163-CR0.pdf",
          "cite": "No. 25-60163 (5th Cir.) PUBLISHED, filed 2026-03-17"
        },
        {
          "source": "Justia",
          "url": "https://law.justia.com/cases/federal/appellate-courts/ca5/25-60163/25-60163-2026-03-17.html",
          "cite": "No. 25-60163 (5th Cir. 2026), no F.4th cite listed"
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
    "date_created": "2026-07-07T18:20:54Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-porter--10810059",
      "to_record_id": "United States v. Porter",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Porter

```
Case: 25-60163       Document: 89-1       Page: 1   Date Filed: 03/17/2026




        United States Court of Appeals
             for the Fifth Circuit
                             ____________                          United States Court of Appeals
                                                                            Fifth Circuit


                               No. 25-60163
                                                                          FILED
                                                                    March 17, 2026
                             ____________
                                                                     Lyle W. Cayce
United States of America,                                                 Clerk

                                                         Plaintiff—Appellee,

                                   versus

Elijah Porter,

                                        Defendant—Appellant.
               ______________________________

               Appeal from the United States District Court
                 for the Southern District of Mississippi
                         USDC No. 1:24-CR-11-1
               ______________________________

Before Smith, Wiener, and Higginson, Circuit Judges.
Jerry E. Smith, Circuit Judge:
       Elijah Porter was charged with possession of a machinegun in violation
of 18 U.S.C. § 922(o). He challenges (1) the denial of his motion to suppress
vehicle-location data obtained from a license plate reader (“LPR”) and a
firearm obtained in a vehicle search and (2) the district court’s ruling that
18 U.S.C. § 922(o) is not unconstitutional. Because the use of an LPR did
not constitute a search, no warrant was required; the stop was supported by
reasonable suspicion, and the officer found the Glock and its machinegun
conversion switch in plain view. Our circuit precedent forecloses Porter’s
Second Amendment challenge. We affirm.




                                      1
Case: 25-60163        Document: 89-1       Page: 2    Date Filed: 03/17/2026




                                  No. 25-60163


                            I. Factual Background
                           A. Evidentiary Hearing
       At the suppression hearing, the district court heard testimony from
Charles Hoggard, a former officer for the Gautier Police Department. Video
footage from Hoggard’s body camera was also presented.

                       1. Officer Hoggard’s Testimony
       While on patrol in January 2024, Hoggard received an alert on his
phone that an LPR located at a specific intersection captured the license
plate of a vehicle that was associated with criminal activity. He contacted
dispatch and was told that the vehicle was “associated with” Elijah Porter,
who had a warrant for aggravated assault. Hoggard conducted a computer
check for the license plate, which revealed the vehicle was associated with
“James Stewart” or “E.L. Porter.” He located the vehicle and conducted a
traffic stop.
       After identifying Porter as the driver, Hoggard detained him and pat-
ted him down. Hoggard observed a firearm protruding from under the
driver’s seat. He was able to see the slide and barrel of the firearm, and a
“little silver switch on the back of it,” which he “believed to be the switch of
an automatic [G]lock.” Hoggard asked Porter if there were any weapons in
the car “to see if he was going to be honest” and later retrieved the firearm
during an inventory search of the vehicle, at which point he had not yet con-
firmed that “the warrant was valid and true.” After Hoggard secured the
firearm in his patrol car, the warrant was confirmed, and he took Porter to
the police station.
       Hoggard stated that the LPR system allowed him to see when a vehi-
cle had passed an LPR camera at a particular location, and he estimated there
were no more than ten LPR cameras stationed across Gautier. He did not
know how long the location data was stored within the LPR system, but he




                                       2
Case: 25-60163        Document: 89-1       Page: 3    Date Filed: 03/17/2026




                                  No. 25-60163


“could look and see how many times [a vehicle] passed within the general . . .
time period.” Hoggard stated there had been other LPR “hits” on Porter’s
vehicle earlier that day and the day before, but he was not able to locate the
vehicle on those occasions because of heavy traffic. He acknowledged that
he did not have a physical description of Porter when he initiated the traffic
stop. Hoggard also noted that after seeing the firearm, he left it in Porter’s
unlocked car, which was in a residential area, and did not immediately tell his
colleague at the scene about the weapon.

                           2. Body Camera Footage
       The footage is consistent with Hoggard’s testimony. Hoggard patted
Porter down next to the open driver’s side door and asked if he had any weap-
ons, to which Porter said he did not. Hoggard then removed several personal
items from Porter’s pockets and placed them on the driver’s seat. Just as
Hoggard turned toward the driver’s seat, he asked Porter if there were any
weapons in the car—Porter answered no. As Hoggard put Porter into his
patrol unit, Hoggard removed an earbud from Porter’s ear and returned to
Porter’s car to place it on the driver’s seat with his other belongings.
       Hoggard then locked Porter’s car and told his colleague that he had to
confirm “the hit.” He returned to Porter’s vehicle, opened the center con-
sole, and looked underneath the driver’s seat. Immediately thereafter, he
tried to flag down his colleague. Hoggard then reached under the driver’s
seat, pulled out a firearm, and said, “Oh, s--t.” The firearm was not visible
on the video until this point. Hoggard motioned again for his colleague to
come over and told him there’s “a f--king switch on that [G]lock.” Hoggard
then said, “it was basically in plain view,” and “the barrel [was] sticking out
from under the seat, so I saw it in plain view.”

                            3. Porter’s Arguments
       Porter asserts that the use of LPR cameras to detect his vehicle’s




                                       3
Case: 25-60163         Document: 89-1         Page: 4     Date Filed: 03/17/2026




                                    No. 25-60163


location constituted a search under the Fourth Amendment and that the
vehicle-location data should be suppressed. He posits that he had a reasona-
ble expectation of privacy in his location and movements that were captured
by the LPR cameras and that a warrant was required for police to obtain such
data from the LPR system. Porter also urges that the traffic stop was invalid
because it was not supported by reasonable suspicion and that the firearm
should be suppressed. Porter theorizes that even if the stop were lawful, the
firearm was not in plain view and was not discovered during a lawful
inventory search. And Porter claims that § 922(o) violates the Second
Amendment, both facially and as applied to him. 1

                           B. District Court’s Rulings
       In a bench ruling, the district court determined that § 922(o) is not
unconstitutional and denied Porter’s motion to dismiss the indictment. The
court denied his motion to suppress the vehicle-location data, reasoning that
“an individual traveling in an automobile on public thoroughfares has no rea-
sonable expectation of privacy in their movements from one place to
another” and “motorists do not have a privacy interest in their license
plates,” since they are “constantly open to plain view of” passersby.
       The court requested supplemental briefing on the threshold issue of
whether the traffic stop was lawful. The court then stated that if the stop was
valid, it would deny the motion to suppress based on its finding that the plain-
view doctrine applied.       The court also determined that the inevitable-
discovery doctrine would apply because the firearm would have been found
during the inventory search.
       After the parties submitted the requested supplemental briefing, the
       _____________________
       1
         Although he did at the district court, Porter does not make a Commerce Clause
challenge on appeal.




                                          4
 Case: 25-60163           Document: 89-1           Page: 5       Date Filed: 03/17/2026




                                        No. 25-60163


court concluded that the traffic stop was lawful, denied Porter’s motion to
suppress, and explained that the stop was valid for three reasons:
        First, Officer Hoggard, had reasonable suspicion to initiate the
        traffic stop based solely on the automatic license plate reader,
        or the ALPR, hit that revealed an outstanding arrest warrant
        for Mr. Porter; Number 2, the [“be on the lookout”] BOLO
        [report], or ALPR, hit does not need to include a physical de-
        scription of the driver to provide an officer reasonable suspi-
        cion to initiate a traffic stop; and number 3, under the collective
        knowledge doctrine, the ALPR was reliable and provided Offi-
        cer Hoggard with reasonable suspicion to initiate the traffic
        stop.
Thereafter, Porter consented to a bench trial, 2 where he was found guilty.

                           II. Denial of Motion to Suppress
        When reviewing the denial of a suppression motion, we review factual
findings for clear error and legal conclusions—“including whether an expec-
tation of privacy is reasonable under the circumstances”—de novo. United
States v. Gomez, 276 F.3d 694, 697 (5th Cir. 2001) (internal quotation marks
and citation omitted). The evidence is “viewed in the light most favorable to
the Government, as the prevailing party below.” United States v. Garcia,
99 F.4th 253, 266 (5th Cir. 2024). We “uphold the district court’s ruling if
there is any reasonable view of the evidence to support it.” United States v.
Alvarez, 40 F.4th 339, 344 (5th Cir. 2022) (internal quotation marks and cita-

        _____________________
        2
          Porter’s jury-trial waiver, the one that he, his counsel, the prosecutor, and district
judge signed, notes that Porter was “fully informed of [his] right to a trial by jury,”
“waive[d] that right,” and “waive[d] [his] right to special findings.” Some of the stipula-
tions, that Porter “knowingly and voluntarily” agreed to, include that “Officer Hoggard
. . . received an alert for a 2017 White Ford Fusion . . . associated with an outstanding
arrest warrant for Elijah Porter” and “Elijah Porter was the driver, and sole occupant of
the Ford Fusion.”




                                               5
 Case: 25-60163         Document: 89-1            Page: 6      Date Filed: 03/17/2026




                                      No. 25-60163


tion omitted).
       And “[w]hen the denial of a motion to suppress is based on live testi-
mony, the clearly erroneous standard is particularly strong because the judge
had the opportunity to observe the demeanor of the witnesses.” United
States v. Jefferson, 89 F.4th 494, 502 (5th Cir. 2023) (internal quotation marks
and citation omitted). “Where testimony conflicts with video evidence, our
court must view the ‘facts in the light depicted by the videotape,’” 3 but
“[w]hen video evidence is ‘ambiguous,’” no such consideration applies. 4

                                           III.
                              A. Vehicle Location Data
       Contrary to Porter’s assertion, the use of an LPR system did not
invade any reasonable expectation of privacy and did not constitute a search,
so no warrant was required.
       Where an individual has a reasonable expectation of privacy, “official
intrusion into that private sphere generally qualifies as a search and requires
a warrant supported by probable cause.” United States v. Smith, 110 F.4th
817, 830 (5th Cir. 2024) (internal quotation marks and citation omitted), cert.
denied, 146 S. Ct. 356 (2025). “A person does not surrender all Fourth
Amendment protection by venturing into the public sphere,” Carpenter v.
United States, 585 U.S. 296, 310 (2018), but “[a] person travel[]ing in an
automobile on public thoroughfares has no reasonable expectation of privacy
in his movements from one place to another,” United States v. Knotts,
460 U.S. 276, 281 (1983).

       _____________________
       3
         See United States v. Anderson, No. 23-50110, 2024 WL 2829243, at *1 (5th Cir.
2024) (per curiam) (unpublished) (citing Scott v. Harris, 550 U.S. 372, 380-81 (2007)).
       4 See id. (citing Aguirre v. City of San Antonio, 995 F.3d 395, 410 (5th Cir. 2021)).




                                             6
 Case: 25-60163           Document: 89-1           Page: 7       Date Filed: 03/17/2026




                                        No. 25-60163


        The LPR system provides periodic information about a vehicle’s
location on “public streets and highways.” A scan occurs when a vehicle
passes one of the locations where a camera is stationed. 5 The LPR system is
not capable of tracking the “whole of [an individual’s] physical movements,”
much less “for a very long period,” to the extent that a cell phone can
because the LPR system does not “faithfully follow[]” individuals “beyond
public thoroughfares.” 6 Indeed, Hoggard’s previous inability to locate Por-
ter’s vehicle, notwithstanding the earlier “hits” and the LPR technology’s
around-the-clock capabilities, illustrates the significant limitations of this
technology relative to cell-site location information (“CSLI”), which can
“provide[] an intimate window into a person’s life, revealing not only his par-
ticular movements, but through them his familial, political, professional,
religious, and sexual associations.” Carpenter, 585 U.S. at 311 (internal quo-
tation marks and citation omitted).
        With a gloss from Olabisiomotosho v. City of Houston, 7 which made
clear that “[a] motorist has no privacy interest in their [sic] license plate
number,” the LPR system is more analogous to the beeper signals in Knotts 8

        _____________________
        5
          See Knotts, 460 U.S. at 281 (reasoning that law enforcement’s monitoring the
beeper signals after placing a hidden beeper in a barrel of drug-precursor chemicals (which
was later purchased by the suspect’s accomplice and placed in the suspect’s vehicle)
“amounted principally to the following of an automobile on public streets and highways”
and did not constitute a search).
        6
          Cf. Carpenter, 585 U.S. at 310–11 (“A cell phone faithfully follows its owner
beyond public thoroughfares and into private residences, doctor’s offices, political head-
quarters, and other potentially revealing locales.”).
        7
         See Olabisiomotosho, 185 F.3d 521, 529 (5th Cir. 1999) (holding that the police did not
need probable cause to use an onboard computer to check a stranded motorist’s license plate
number since “[a] motorist has no privacy interest in their license plate number”).
        8
          See Knotts, 460 U.S. at 277–79, 285 (noting that the beeper transmitted periodic
radio signals that enhanced the police’s ability to surveil the vehicle’s movements and
allowed police to track the vehicle to a drug lab); see also id. at 285 (reasoning that a “sci-




                                               7
 Case: 25-60163           Document: 89-1           Page: 8       Date Filed: 03/17/2026




                                        No. 25-60163


than to the CSLI at issue in Carpenter. True, the LPR system allows the
government to access an historical record for some time, and that type of
retrospective data can allow police to “travel back in time to retrace a per-
son’s whereabouts” without needing to “know in advance whether they
want to follow a particular individual, or when.” 9 But the LPR technology
in the instant case provides only periodic information about a vehicle’s loca-
tion when a vehicle passes one of its ten locations where an LPR camera is
stationed in Gautier and is much more limited than CSLI and geofence 10
data, which is capable of capturing a greater volume of comprehensive infor-
mation with a higher degree of quality and precision. 11




        _____________________
entific enhancement of this sort raises no constitutional issues which visual surveillance
would not also raise”).
        9
           See Carpenter, 585 U.S. at 312; see also Smith, 110 F.4th at 834 (expressing “par-
ticular concern” with “the fact that a geofence will retroactively track anyone with Loca-
tion History enabled, regardless of whether a particular individual is suspicious or moving
within an area that is typically granted Fourth Amendment protection”).
        10
           Though geofences are typically limited to a discrete time period, “a brief snap-
shot can expose highly sensitive information,” such as a person’s “visit to ‘the psychiatrist,
the plastic surgeon, the abortion clinic, the AIDS treatment center, the strip club, the crim-
inal defense attorney, the by-the-hour-motel, the union meeting, the mosque, synagogue or
church, [or] the gay bar,’ or a location other than home during a COVID-19 shelter-in-place
order.” See Smith, 110 F.4th at 833 (citation omitted; alteration in original).
        11
            Cf. Smith, 110 F.4th at 823 (“Once a person enables Location History, Google
begins to ‘log[] [the] device’s location [into the Sensorvault], on average, every two min-
utes’ by ‘track[ing] [the] user’s location across every app and every device associated with
the user’s account.”) (alteration and emphasis in original); see also id. (noting that the “data
is ‘considerably more precise than other kinds of location data, including cell-site location
information because [Location History] is determined based on multiple inputs, including
GPS signals, signals from nearby Wi-Fi networks, Bluetooth beacons, and cell towers’”)
(alteration in original).




                                               8
 Case: 25-60163          Document: 89-1          Page: 9       Date Filed: 03/17/2026




                                       No. 25-60163


                                   B. Vehicle Search
                                       1. The Stop
        The traffic stop was lawful because Hoggard had reasonable suspicion
to stop Porter’s vehicle. “The ‘touchstone of Fourth Amendment analysis
is reasonableness.’” United States v. Henry, 37 F.4th 173, 176 (5th Cir. 2022)
(per curiam) (quoting United States v. Brigham, 382 F.3d 500, 507 (5th Cir.
2004) (en banc)). “[I]if police have reasonable suspicion, grounded in spe-
cific and articulable facts, that a person they encounter was involved in or is
wanted in connection with a completed felony, then a Terry stop may be made
to investigate that suspicion.” 12
        There is no reason to disagree with the district court’s thorough
rationale:
        Officer Hoggard [ ] had reasonable suspicion to initiate the traf-
        fic stop based solely on the automatic license plate reader, or
        the ALPR, hit that revealed an outstanding arrest warrant for
        Mr. Porter; Number 2, the BOLO, or ALPR, hit does not
        need to include a physical description of the driver to provide
        an officer reasonable suspicion to initiate a traffic stop; and
        number 3, under the collective knowledge doctrine, the ALPR
        was reliable and provided Officer Hoggard with reasonable sus-
        picion to initiate the traffic stop.
After all, the BOLO report “provide[d] the reasonable suspicion necessary
to justify an investigatory stop” because the arrest warrant information from
        _____________________
        12
           United States v. Hensley, 469 U.S. 221, 229 (1985); see United States v. Ochoa,
667 F.3d 643, 649 (5th Cir. 2012) (“The officer making the arrest need not have direct
knowledge of all the facts establishing probable cause, as long as he has communicated with
the officer who does.”); see also United States v. Alvarez, 40 F.4th 339, 352 (5th Cir. 2022)
(“Officers may conduct an investigatory stop in reliance on information issued through
police channels, such as a wanted flyer or bulletin or radio dispatch, if the information is
based on ‘articulable facts supporting a reasonable suspicion that the wanted person has
committed an offense.’”) (citing Hensley, 469 U.S. at 232).




                                             9
Case: 25-60163           Document: 89-1           Page: 10      Date Filed: 03/17/2026




                                       No. 25-60163


the other Mississippi jurisdiction was “credibl[e] and reliabl[e]”—it “speci-
fi[ed] Porter’s vehicle information, allowed Hoggard to “verif[y]” the
match, and related to an active warrant, which turned out to be valid. 13 Even
though he didn’t need to do so because “[t]he reasonable suspicion inquiry
‘falls considerably short’ of 51% accuracy,” Hoggard carefully conducted a
computer check for the license plate, which revealed the vehicle was associ-
ated with “James Stewart” or “E.L. Porter.” 14 That the vehicle may have
belonged to someone other than Porter or that Hoggard lacked a physical
description of the driver does not change the calculus in Porter’s favor 15
because Hoggard had sufficiently specific information to stop the car—he
knew the make and model, its license plate number, its approximate location,
and that Porter was wanted for arrest for aggravated assault.

               2. Glock Pistol and Machinegun Conversion Switch
                                      a. Plain View
        Hoggard found the Glock pistol and machinegun conversion switch
and testified in open court “that the barrel was sticking out from under the
seat” in plain view. Not only was the “incriminating nature” of the auto-
matic conversion switch “immediately apparent,” 16 but the district judge,

        _____________________
        13
           United States v. Gonzalez, 190 F.3d 668 (5th Cir. 1999) (“Whether a particular
tip or BOLO report provides a sufficient basis for an investigatory stop may depend upon
the credibility and reliability of the informant, the specificity of the information contained
in the tip or report, the extent to which the information in the tip or report can be verified
by others in the field, and whether the tip or report concerns active or recent activity, or
has instead gone stale.”) (citing Alabama v. White, 496 U.S. 325, 328-32 (1990)).
        14
           See Kansas v. Glover, 589 U.S. 376, 381 (2020) (noting that “[t]he reasonable
suspicion inquiry ‘falls considerably short’ of 51% accuracy”).
        15
          See Heien v. North Carolina, 574 U.S. 54, 60 (2014) (“To be reasonable is not to
be perfect.”).
        16
          See United States v. Rodriguez, 601 F.3d 402, 407 (5th Cir. 2010) (noting that the
“plain view” exception “allows police to seize items where (1) the police lawfully entered




                                             10
Case: 25-60163            Document: 89-1          Page: 11     Date Filed: 03/17/2026




                                        No. 25-60163


who had an opportunity to observe Hoggard’s demeanor, said in no uncertain
terms, “I do find Officer Hoggard’s testimony to be credible.” 17 There is no
reason to depart from the district court’s sound determination.
        One may be inappropriately tempted to engage in a frame-by-frame,
instant replay-type analysis of Hoggard’s behavior, based on the body camera
footage, considering the proposition that “[w]here testimony conflicts with
video evidence, our court must view the ‘facts in the light depicted by the
videotape.’” 18 But because the video evidence is ambiguous at best for Por-
ter, no such consideration applies. 19
        Although we first notice the gun at about the six-minute mark when
Hoggard physically removes it from under the driver’s seat, his body camera
may not have fully captured everything that he saw at eye-level with a
dynamic field of vision because the camera was in a static position near his
torso. 20 There is nothing that “plainly contradicts the district court’s finding

        _____________________
the area where the item was located; (2) the item was in plain view; (3) the incriminating
nature of the item was ‘immediately apparent’; and (4) the police had a lawful right of
access to the item”) (citing Horton v. California, 496 U.S. 128, 136–37 (1990)).
        17
           See United States v. Gibbs, 421 F.3d 352, 357 (5th Cir. 2005) (“One of the most
important principles in our judicial system is the deference given to the finder of fact who
hears the live testimony of witnesses because of his opportunity to judge the credibility of
those witnesses.”) (internal quotation marks and citation omitted).
        18
             Anderson, 2024 WL 2829243, at *1 (citing Scott v. Harris, 550 U.S. 372, 380–81
(2007)).
        19 See id. (“When video evidence is ‘ambiguous[,]’ however, Scott v. Harris ‘has

no application.’”) (alteration in original) (citing Aguirre v. City of San Antonio, 995 F.3d
395, 410 (5th Cir. 2021)).
        20
           See, e.g., United States v. Stuckey, No.24-CR-2017-CJW-MAR, 2025 WL 34816,
at *2 (N.D. Iowa 2025) (noting that “the body camera is positioned—on [the officer’]s
torso, and thus does not capture what [he] could see from an eye-level angle”); United
States v. Gray, No.20-191 (CKK), 2021 WL 2209462, at *2 (D.D.C. 2021) (“Because the
body-worn cameras focus only straight ahead and are lower than the officers’ sight-line, the




                                             11
Case: 25-60163          Document: 89-1           Page: 12     Date Filed: 03/17/2026




                                      No. 25-60163


that the officer saw” the Glock and the switch “in plain view.” 21
        Another rejoinder is that the factual circumstances suggest that Hog-
gard did not see the Glock and its switch in plain view. True, Hoggard initi-
ally left the Glock in an unlocked car in a residential neighborhood and did
not immediately tell his colleague at the scene about the weapon. But there
was no traffic on the side street, where another patrol car was already present
and blocking incoming traffic from the cross street. And during the three-
and-a-half-minute stretch between Hoggard’s initial discovery of the Glock
and the subsequent physical possession of it, Hoggard had other priorities—
he escorted Porter to his patrol vehicle, put Porter’s personal items in his car,
and rolled its windows up to prevent rain from coming in. Hoggard did not
raise the immediate alarm bells because he wanted “to see if [Porter] was
going to be honest,” something he testified to in open court, which the dis-
trict court found credible.
        The footage is not clear-cut in Porter’s favor. In fact, it shows that
Hoggard seamlessly reached under the seat in a “quick darting motion,”
suggesting that he knew precisely where the Glock and the switch were
because he had previously seen them in plain view. Admittedly, the officer
did exclaim, “Oh s--t,” but that can be explained by the fact that physically
seizing a suspect’s gun that has an attached machinegun conversion device

        _____________________
camera does not capture everything that each officer sees.”); United States v. Rowson,
652 F. Supp. 3d 436, 444 (S.D.N.Y. 2023) (“[B]ody camera footage sometimes does not
pick up nuances visible to the naked eye, including based on the different distances and
angles involved, and that the camera may not have focused on the same, precise part of a
suspect’s anatomy as did the officers.”).
        21
           See United States v. Riggins, No. 22-10306, 2023 WL 2964408, at *1 (5th Cir.
2023) (per curiam) (unpublished) (“Even if the body camera recording does not clearly
show that the syringe was visible inside Riggins’s pocket, we see nothing that plainly con-
tradicts the district court’s finding that the officer saw the syringe in plain view.”).




                                            12
Case: 25-60163          Document: 89-1           Page: 13     Date Filed: 03/17/2026




                                      No. 25-60163


may not be an everyday occurrence even for experienced officers, who may
be rightfully shocked. Far from being clear-cut in Porter’s favor, the footage
confirms that Hoggard contemporaneously corroborated that “[the Glock]
was basically in plain view,” and “the barrel [was] sticking out from under
the seat, so [he] saw it in plain view.”
        Viewing the evidence in the light most favorable to the government as
the prevailing party, there is nothing that plainly contradicts the district
court’s reasoned assessment that Hoggard saw the Glock and its switch in
plain view.

                    IV. Constitutionality of a Criminal Statute
        This court reviews a preserved challenge to the constitutionality of a
statute de novo. United States v. Howard, 766 F.3d 414, 419 (5th Cir. 2014).
“When a litigant brings both facial and as-applied challenges, we generally
decide the as-applied challenge first because it is the narrower question.”
Ostrewich v. Tatum, 72 F.4th 94, 104 (5th Cir. 2023). “To sustain a facial
challenge, ‘the challenger must establish that no set of circumstances exists
under which the statute would be valid.’” 22 A facial challenge will necessar-
ily fail if a statute is constitutional as applied to a defendant’s individual case.
Id.

                                V. 18 U.S.C. § 922(o)
        This court’s jurisprudence forecloses Porter’s Second Amendment
challenge to 18 U.S.C. § 922(o) argument—machineguns “do not receive
Second Amendment protection.” 23 Indeed, very recently, we squarely

        _____________________
        22
           United States v. Diaz, 116 F.4th 458, 471 (5th Cir. 2024) (quoting United States
v. Salerno, 481 U.S. 739, 745 (1987)), cert. denied, 145 S. Ct. 2822 (2025).
        23
         See Hollis v. Lynch, 827 F.3d 436, 451 (5th Cir. 2016) (concluding that machine-
guns “do not receive Second Amendment protection” and noting that “[m]achineguns are




                                            13
Case: 25-60163           Document: 89-1            Page: 14      Date Filed: 03/17/2026




                                        No. 25-60163


answered this question, reasoning that Hollis continues to bind us” and that
the defendant’s “Second Amendment challenge to his § 922(o) conviction
must fail” “because Hollis controls.” United States v. Wilson, 164 F.4th 380,
385–87 (5th Cir. 2026). Wilson makes clear that “Bruen reinforces the por-
tion of Heller on which Hollis relied.” 24 Under our Rule of Orderliness, 25
“only an intervening change in the law . . . permits a subsequent panel to
decline to follow a prior Fifth Circuit precedent.” 26 Bruen does not unequiv-
ocally overrule Hollis because Bruen addressed a law limiting the ability of
law-abiding citizens to carry handguns outside the home. See New York State
Rifle & Pistol Ass’n, Inc. v. Bruen, 597 U.S. 1, 13–14 (2022).
        AFFIRMED.




        _____________________
dangerous and unusual and therefore not in common use”).
        24
          Wilson, 164 F.4th at 386 (“In Hollis, the court cited dicta from Heller for the
proposition that the Second Amendment does not protect dangerous and unusual weapons.
And in Bruen, the Supreme Court reiterated that portion of Heller, observing that it is ‘fairly
supported by the historical tradition of prohibiting the carrying of dangerous and unusual
weapons that the Second Amendment protects the possession and use of weapons that are
in common use at the time.’”).
        25
           See Thompson v. Dall. City Att’y’s Off., 913 F.3d 464, 468 n.17 (5th Cir. 2019)
(“[A] panel’s interpretation of a Supreme Court decision is binding on a subsequent panel
even if the later panel disagrees with the earlier panel’s interpretation.”) (citing United
States v. Traxler, 764 F.3d 486, 489 (5th Cir. 2014) (“Even if persuaded that [our prior
panel opinion] is inconsistent with [an earlier Supreme Court opinion], we may not ignore
the decision, for in this circuit one panel may not overrule the decision of a prior panel.”)
(alteration in original)).
        26
          United States v. Alcantar, 733 F.3d 143, 145 (5th Cir. 2013); id. at 146 (noting that
the intervening change in the law “must be unequivocal”).




                                              14

```

---

## GROUP: _overhaul2/lake/cases/United States v. Ramirez.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Ramirez"
type: case
citation: "523 U.S. 65 (1998)"
parallel_cite: "118 S. Ct. 992; 140 L. Ed. 2d 191"
neutral_cite: 1998 U.S. LEXIS 1600
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-03-04
docket: 96-1469
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1998-03-04
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Ramirez
  varies_by_point: false
  scope_note: "Controlling: a no-knock entry that damages property is judged by the same Richards reasonable-suspicion standard — no heightened showing is required because property is destroyed — though excessive or unnecessary destruction may independently violate the Fourth Amendment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118180/united-states-v-ramirez/"
  cluster_id: 118180
  opinion_id: 118180
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Progeny"
related: ["[[Richards v. Wisconsin]]", "[[Wilson v. Arkansas]]", "[[United States v. Banks]]", "[[Sabbath v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "knock-and-announce", "no-knock", "warrant-execution", "property-damage"]
holding: "The Fourth Amendment does not impose a higher standard on a no-knock entry merely because the entry causes property damage; the entry is judged by Richards' reasonable-suspicion test, although excessive or unnecessary destruction of property in a search may itself violate the Fourth Amendment."
lake:
  record_id: United States v. Ramirez
  status: verified
  projected_at: 2026-07-09
---

# United States v. Ramirez

*523 U.S. 65 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers had a warrant connected to the search for Alan Shelby, a violent prison escapee reported to be hiding in Hernan Ramirez's home and to have access to a supply of weapons. Executing the warrant early one morning, the police announced their presence and broke a single window in Ramirez's garage — pointing a weapon through it to discourage anyone from rushing to the guns. Believing a burglary was underway, Ramirez fired a shot, then surrendered. Shelby was not found, but officers recovered firearms, and Ramirez (a felon) was charged with being a felon in possession. The District Court and Ninth Circuit suppressed the evidence, finding insufficient [[Exigent Circumstances and Hot Pursuit|exigency]] to justify the property destruction.

## Issue
Does the Fourth Amendment (or 18 U.S.C. § 3109) hold officers to a higher standard for a no-knock entry when the entry results in the destruction of property?

## Rule
No. "[W]hether the Fourth Amendment holds officers to a higher standard . . . when a 'no-knock' entry results in the destruction of property[,] [w]e hold that it does not." — 523 U.S. at 68. ^pin-68

"Under *Richards*, a no-knock entry is justified if police have a 'reasonable suspicion' that knocking and announcing would be dangerous, futile, or destructive to the purposes of the investigation. Whether such a 'reasonable suspicion' exists depends in no way on whether police must destroy property in order to enter." — *Id.* at 71. ^pin-71

The manner of entry is still constrained by reasonableness: "Excessive or unnecessary destruction of property in the course of a search may violate the Fourth Amendment, even though the entry itself is lawful and the fruits of the search are not subject to suppression." — [*Id.*](https://www.courtlistener.com/opinion/118180/united-states-v-ramirez/#:~:text=Excessive%20or%20unnecessary%20destruction%20of) ^pin-71b

Section 3109 codifies the common-law exceptions and imposes no greater requirement.

## Application
The police had reasonable suspicion that knocking and announcing would be dangerous: Shelby was a violent escapee, reportedly armed, who had vowed not to do federal time. Breaking a single garage window to deter a rush to weapons was a reasonable, limited method of entry, not excessive or unnecessary destruction. Because the *[[Richards v. Wisconsin|Richards]]* standard was satisfied and the property damage was reasonable, neither the Fourth Amendment nor § 3109 was violated.

## Conclusion
No Fourth Amendment or § 3109 violation occurred; the judgment suppressing the evidence was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Ramirez* remains controlling: property damage does not raise the bar for a no-knock entry, which is governed by the reasonable-suspicion standard of [[Richards v. Wisconsin]] (building on [[Wilson v. Arkansas]]), while excessive destruction can independently offend the Fourth Amendment. It is taught with [[United States v. Banks]] (timing of forcible entry) and [[Sabbath v. United States]] (what counts as an entry). No negative treatment.

## Appears on
- [[Knock-and-Announce]] — *Progeny*

## Sources
- *United States v. Ramirez*, 523 U.S. 65 (1998) — https://www.courtlistener.com/opinion/118180/united-states-v-ramirez/ — pinpoints: 68, 71.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3792d21edf81aef0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Ramirez"}, "payload": {"all": [{"cite": "523 U.S. 65", "page": "65", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "523"}, {"cite": "118 S. Ct. 992", "page": "992", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "118"}, {"cite": "140 L. Ed. 2d 191", "page": "191", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "140"}, {"cite": "1998 U.S. LEXIS 1600", "page": "1600", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1998"}], "display": "523 U.S. 65", "official": {"cite": "523 U.S. 65", "page": "65", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "523"}, "official_selection_present": true, "record_id": "United States v. Ramirez"}}
{"assertion_id": "3f38399d27a0329f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-68", "record_id": "United States v. Ramirez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-68", "pinpoint_status": "slip-only", "quote": "--- # United States v. Ramirez *523 U.S. 65 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had a warrant connected to the search for Alan Shelby, a violent prison escapee reported to be hiding in Hernan Ramirez's home and to have access to a supply of weapons. Executing the warrant early one morning, the police announced their presence and broke a single window in Ramirez's garage — pointing a weapon through it to discourage anyone from rushing to the guns. Believing a burglary was underway, Ramirez fired a shot, then surrendered. Shelby was not found, but officers recovered firearms, and Ramirez (a felon) was charged with being a felon in possession. The District Court and Ninth Circuit suppressed the evidence, finding insufficient exigency to justify the property destruction. ## Issue Does the Fourth Amendment (or 18 U.S.C. § 3109) hold officers to a higher standard for a no-knock entry when the entry results in the destruction of property? ## Rule No.", "quote_fidelity": "mismatch", "record_id": "United States v. Ramirez", "star_marker": null}}
{"assertion_id": "4a537eb2727d5ee8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-71", "record_id": "United States v. Ramirez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-71", "pinpoint_status": "slip-only", "quote": "Under *Richards*, a no-knock entry is justified if police have a 'reasonable suspicion' that knocking and announcing would be dangerous, futile, or destructive to the purposes of the investigation. Whether such a 'reasonable suspicion' exists depends in no way on whether police must destroy property in order to enter.", "quote_fidelity": "mismatch", "record_id": "United States v. Ramirez", "star_marker": null}}
{"assertion_id": "75decc6b5087c68d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-71b", "record_id": "United States v. Ramirez"}, "payload": {"fragment": "#:~:text=Excessive%20or%20unnecessary%20destruction%20of", "page": null, "pin_id": "pin-71b", "pinpoint_status": "star-verified", "quote": "Excessive or unnecessary destruction of property in the course of a search may violate the Fourth Amendment, even though the entry itself is lawful and the fruits of the search are not subject to suppression.", "quote_fidelity": "matched", "record_id": "United States v. Ramirez", "star_marker": "71"}}
{"assertion_id": "a8b09fca86ea6143", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Ramirez"}, "payload": {"as_of_content": "1998-03-04", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Ramirez", "scope_note": "Controlling: a no-knock entry that damages property is judged by the same Richards reasonable-suspicion standard — no heightened showing is required because property is destroyed — though excessive or unnecessary destruction may independently violate the Fourth Amendment.", "varies_by_point": false}}
```

### lake record — United States v. Ramirez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ramirez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Ramirez",
    "case_name_short": "Ramirez",
    "case_name_full": "United States v. Ramirez",
    "input_case_name": "United States v. Ramirez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-03-04",
    "year": 1998,
    "docket": "96-1469",
    "cluster_id": 118180,
    "lead_opinion_id": 118180,
    "sibling_ids": [
      118180
    ],
    "absolute_url": "/opinion/118180/united-states-v-ramirez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "523 U.S. 65",
      "volume": "523",
      "reporter": "U.S.",
      "page": "65",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "118 S. Ct. 992",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "992",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "140 L. Ed. 2d 191",
        "volume": "140",
        "reporter": "L. Ed. 2d",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 1600",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "1600",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "523 U.S. 65",
        "volume": "523",
        "reporter": "U.S.",
        "page": "65",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 992",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "992",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "140 L. Ed. 2d 191",
        "volume": "140",
        "reporter": "L. Ed. 2d",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 1600",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "1600",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "523 U.S. 65",
    "official_selection": {
      "court_class": "scotus",
      "selected": "523 U.S. 65",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-68",
      "page": null,
      "quote": "--- # United States v. Ramirez *523 U.S. 65 (1998)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had a warrant connected to the search for Alan Shelby, a violent prison escapee reported to be hiding in Hernan Ramirez's home and to have access to a supply of weapons. Executing the warrant early one morning, the police announced their presence and broke a single window in Ramirez's garage \u2014 pointing a weapon through it to discourage anyone from rushing to the guns. Believing a burglary was underway, Ramirez fired a shot, then surrendered. Shelby was not found, but officers recovered firearms, and Ramirez (a felon) was charged with being a felon in possession. The District Court and Ninth Circuit suppressed the evidence, finding insufficient exigency to justify the property destruction. ## Issue Does the Fourth Amendment (or 18 U.S.C. \u00a7 3109) hold officers to a higher standard for a no-knock entry when the entry results in the destruction of property? ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-71",
      "page": null,
      "quote": "Under *Richards*, a no-knock entry is justified if police have a 'reasonable suspicion' that knocking and announcing would be dangerous, futile, or destructive to the purposes of the investigation. Whether such a 'reasonable suspicion' exists depends in no way on whether police must destroy property in order to enter.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-71b",
      "page": null,
      "quote": "Excessive or unnecessary destruction of property in the course of a search may violate the Fourth Amendment, even though the entry itself is lawful and the fruits of the search are not subject to suppression.",
      "star_marker": "71",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9732,
      "fragment": "#:~:text=Excessive%20or%20unnecessary%20destruction%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1998-03-04",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Ramirez",
    "varies_by_point": false,
    "scope_note": "Controlling: a no-knock entry that damages property is judged by the same Richards reasonable-suspicion standard \u2014 no heightened showing is required because property is destroyed \u2014 though excessive or unnecessary destruction may independently violate the Fourth Amendment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Southerland, Vince",
          "cluster_id": 186774,
          "cite": [
            "373 U.S. App. D.C. 305",
            "466 F.3d 1083",
            "2006 U.S. App. LEXIS 26978",
            "2006 WL 3069122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Julio Cortez-Rocha",
          "cluster_id": 788904,
          "cite": [
            "394 F.3d 1115",
            "2005 U.S. App. LEXIS 1014",
            "2005 WL 107088"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Julio Cortez-Rocha",
          "cluster_id": 787787,
          "cite": [
            "383 F.3d 1093",
            "2004 U.S. App. LEXIS 19583",
            "2004 WL 2093451"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Deandre J. Scroggins",
          "cluster_id": 785508,
          "cite": [
            "361 F.3d 1075",
            "2004 WL 574495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Junior Wardrick",
          "cluster_id": 784262,
          "cite": [
            "350 F.3d 446",
            "2003 U.S. App. LEXIS 23669",
            "2003 WL 22789492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
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
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
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
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carpenter v. United States",
          "cluster_id": 4510032,
          "cite": [
            "585 U.S. 296",
            "138 S. Ct. 2206",
            "201 L. Ed. 2d 507",
            "2018 U.S. LEXIS 3844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado v. Joshua M. AARNESS",
          "cluster_id": 10014025,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Louis Lalonde v. County of Riverside, Robert Moquin, and Jason Horton, Opinion",
          "cluster_id": 767803,
          "cite": [
            "204 F.3d 947",
            "2000 Daily Journal DAR 2031",
            "2000 Cal. Daily Op. Serv. 1433",
            "2000 U.S. App. LEXIS 2778",
            "2000 WL 217552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Banks",
          "cluster_id": 131146,
          "cite": [
            "157 L. Ed. 2d 343",
            "124 S. Ct. 521",
            "540 U.S. 31",
            "2003 U.S. LEXIS 8966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James H. Spikes (96-3899) Marilyn Smith (96-3660)",
          "cluster_id": 758684,
          "cite": [
            "158 F.3d 913",
            "49 Fed. R. Serv. 1564",
            "1998 U.S. App. LEXIS 21399",
            "1998 WL 551966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terebesi v. Torreso",
          "cluster_id": 8441937,
          "cite": [
            "764 F.3d 217",
            "2014 U.S. App. LEXIS 16133",
            "2014 WL 4099309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Handy",
          "cluster_id": 2559301,
          "cite": [
            "18 A.3d 179",
            "206 N.J. 39",
            "2011 N.J. LEXIS 566"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Aarness",
          "cluster_id": 2632419,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roger Trent v. Steven Wade",
          "cluster_id": 2774855,
          "cite": [
            "776 F.3d 368",
            "2015 WL 394096"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McDonough",
          "cluster_id": 2483242,
          "cite": [
            "940 N.E.2d 1100",
            "239 Ill. 2d 260",
            "346 Ill. Dec. 496",
            "2010 Ill. LEXIS 1557"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Larry J. Leaf, Individually and as Personal Representative of the Estate of John P. Leaf, Deceased, Martha A. Leaf, John P. Leaf v. Ronald Shelnutt",
          "cluster_id": 789551,
          "cite": [
            "400 F.3d 1070",
            "2005 U.S. App. LEXIS 4513",
            "2005 WL 628217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hardin",
          "cluster_id": 1427400,
          "cite": [
            "539 F.3d 404",
            "2008 U.S. App. LEXIS 18135",
            "2008 WL 3891265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 2181223,
          "cite": [
            "846 A.2d 569",
            "179 N.J. 377",
            "2004 N.J. LEXIS 437"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ward",
          "cluster_id": 1614689,
          "cite": [
            "2000 WI 3",
            "604 N.W.2d 517",
            "231 Wis. 2d 723",
            "2000 Wisc. LEXIS 3"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cybernet, LLC v. Jonathan David",
          "cluster_id": 4738712,
          "cite": [
            "954 F.3d 162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Basham",
          "cluster_id": 161661,
          "cite": [
            "268 F.3d 1199",
            "2001 U.S. App. LEXIS 22854",
            "2001 WL 1262098"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Stevens",
          "cluster_id": 1693561,
          "cite": [
            "597 N.W.2d 53",
            "460 Mich. 626"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Bynum",
          "cluster_id": 785581,
          "cite": [
            "362 F.3d 574",
            "2004 U.S. App. LEXIS 5703",
            "2004 WL 595136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKay",
          "cluster_id": 2600831,
          "cite": [
            "41 P.3d 59",
            "117 Cal. Rptr. 2d 236",
            "27 Cal. 4th 601",
            "2002 Cal. Daily Op. Serv. 2036",
            "2002 Daily Journal DAR 2485",
            "2002 Cal. LEXIS 624"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rudolph Keszthelyi",
          "cluster_id": 779578,
          "cite": [
            "308 F.3d 557",
            "2002 U.S. App. LEXIS 21631",
            "2002 F. App'x 0362P"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Steven Guest Denise B. Kelley Nelda Sturgill Deborah Cummings Randy Bowling Richard E. Kramer, on Behalf of Themselves and All Others Similarly Situated v. Simon L. Leis, Jr. Hamilton County Sheriff's Department Hamilton County Regional Electronic Computer Intelligence Task Force Dale Menkhaus James Nerlinger David L. Ausdenmoore, Michael O'Brien Noah O'Brien Anthony Blackmon Randall Dodds Darrell McAvoy Brian Kaeppner v. Simon L. Leis, Jr. Hamilton County Sheriff's Department Hamilton County Regional Electronic Computer Intelligence Task Force Dale Menkhaus James Nerlinger David L. Ausdenmoore",
          "cluster_id": 773807,
          "cite": [
            "255 F.3d 325",
            "2001 U.S. App. LEXIS 14597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Brown v. Battle Creek Police Dep't",
          "cluster_id": 4331219,
          "cite": [
            "844 F.3d 556",
            "2016 FED App. 0293P",
            "2016 U.S. App. LEXIS 22447",
            "2016 WL 7336612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118180) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 178,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 178,
        "triage_read": 6,
        "triage_snippet_classified": 172
      },
      "lane2_top_cited": {
        "query": "cites:(118180)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NCZzPTI2Nzg2NzUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118180%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118180)",
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
    "complete_query": "cites:(118180)",
    "indexed_citing_opinions": 242,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118180,
        "count": 242,
        "count_source": "search"
      }
    ],
    "citation_count": 410,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-ramirez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2NjAxMzEmcz00NzI4ODE4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118180%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118180,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 723873,
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
    "date_created": "2026-07-06T02:21:27Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:21:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:21:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:24:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:21:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Ramirez

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b191-7">
  Chief Justice Rehnquist
 </author>
<p id="AZ">
  delivered the opinion of the Court.
 </p>
<p id="b191-8">
  In
  <em>
   Richards
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#394" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 394</a></span> (1997), we held that so-called “no-knoek” entries are justified when police officers have a “reasonable suspicion” that knocking and announcing their presence before entering would “be dangerous or futile, or .. . inhibit the effective investigation of
  <span citation-index="1" class="star-pagination" label="68"> 
   *68
   </span>
  the crime.” In this ease, we must decide whether the Fourth Amendment holds officers to a higher standard than this when a “no-knoek” entry results in the destruction of property. We hold that it does not.
 </p>
<p id="b192-5">
  Alan Shelby was a prisoner serving concurrent state and federal sentences in the Oregon state prison system. On November 1,1994, the Tillamook County Sheriff’s Office took temporary custody of Shelby, expecting to transport him to the Tillamook County Courthouse, where he was scheduled to testify. On the way to the courthouse, Shelby slipped his handcuffs, knocked over a deputy sheriff, and escaped from custody.
 </p>
<p id="b192-6">
  It was not the first time Shelby had attempted escape. In 1991 he struck an officer, kicked out a jail door, assaulted a woman, stole her vehicle, and used it to ram a police vehicle. Another time he attempted escape by using a rope made from torn bedsheets. He was reported to have made threats to kill witnesses and police officers, to have tortured people with a hammer, and to have said that he would “ ‘not do federal time.’” App. to Pet. for Cert. 38a. It was also thought that Shelby had had access to large supplies of weapons.
 </p>
<p id="b192-7">
  Shortly after learning of Shelby’s escape, the authorities sent out a press release, seeking information that would lead to his recapture. On November 3, a reliable confidential informant told Bureau of Alcohol, Tobacco, and Firearms Agent George Kim that on the previous day he had seen a person he believed to be Shelby at respondent Hernán Ramirez’s home in Boring, Oregon. Kim and the informant then drove to an area near respondent’s home, from where Kim observed a man working outside who resembled Shelby.
 </p>
<p id="b192-8">
  Based on this information, a Deputy United States Marshal sought and received a “no-knock” warrant granting permission to enter and search Ramirez’s home. Around this time, the confidential informant also told authorities that respondent might have a stash of guns and drugs hidden in
  <span citation-index="1" class="star-pagination" label="69"> 
   *69
   </span>
  his garage. In the early morning of November 5, approximately 45 officers gathered to execute the warrant. The officers set up a portable loudspeaker system and began announcing that they had a search warrant. Simultaneously, they broke a single window in the garage and pointed a gun through the opening, hoping thereby to dissuade any of the occupants from rushing to the weapons the officers believed might be in the garage.
 </p>
<p id="b193-5">
  Respondent and his family were asleep inside the house at the time this activity began. Awakened by the noise, respondent believed that they were being burglarized. He ran to his utility closet, grabbed a pistol, and fired it into the ceiling of his garage. The officers fired back and shouted “police.” At that point respondent realized that it was law enforcement officers who were trying to enter his home. He ran to the living room, threw his pistol away, and threw himself onto the floor. Shortly thereafter, he, his wife, and their child left the house and were taken into police custody. Respondent waived his
  <em>
   Miranda
  </em>
  rights, and then admitted that he had fired the weapon, that he owned both that gun and another gun that was inside the house, and that he was a convicted felon. Officers soon obtained another search warrant, which they used to return to the house and retrieve the two guns. Shelby was not found.
 </p>
<p id="b193-6">
  Respondent was subsequently indicted for being a felon in possession of firearms. <span class="citation no-link">18 U. S. C. § 922</span>(g)(1). The District Court granted his motion to suppress evidence regarding his possession of the weapons, ruling that the police officers had violated both the Fourth Amendment and <span class="citation no-link">18 U. S. C. § 8109</span> because there were “insufficient exigent circumstances” to justify the police officers’ destruction of property in their execution of the warrant. App. to Pet. for Cert. 34a.
 </p>
<p id="b193-7">
  The Court of Appeals for the Ninth Circuit affirmed. <span class="citation" data-id="9843168"><a href="/opinion/723873/united-states-of-america-plaintiff-appellant-v-hernan-ramirez/" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellant, v. Hernan...">91 F. 3d 1297</a></span> (1996). Applying Circuit precedent, that court concluded that while a “mild exigency” is sufficient to justify a no-knoek entry that can be accomplished without the de
  <span citation-index="1" class="star-pagination" label="70"> 
   *70
   </span>
  struction of property, “ 'more specific inferences of exigency are necessary’ ” when property is destroyed.
  <span class="citation" data-id="9843168"><a href="/opinion/723873/united-states-of-america-plaintiff-appellant-v-hernan-ramirez/#1301" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellant, v. Hernan..."><em>
   Id.,
  </em>
  at 1301</a></span>. It held that this heightened standard had not been met on the facts of this case. We granted certiorari and now reverse. <span class="citation multiple-matches"><a href="/c/U.%20S./521/1103/">521 U. S. 1103</a></span> (1997).
 </p>
<p id="b194-5">
  In two recent eases we have considered whether and to what extent “no-knock” entries implicate the protections of the Fourth Amendment. In
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), we reviewed the Arkansas Supreme Court’s holding that the common-law requirement that police officers knock and announce their presence before entering played no role in Fourth Amendment analysis. We rejected that conclusion, and held instead that “in some circumstances an officer’s unannounced entry into a home might be unreasonable under the Fourth Amendment.”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#934" aria-description="Citation for case: Wilson v. Arkansas"><em>
   Id.,
  </em>
  at 934</a></span>. We were careful to note, however, that there was no rigid rule requiring announcement in all instances, and left “to the lower courts the task of determining the circumstances under which an unannounced entry is reasonable under the Fourth Amendment.”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#934" aria-description="Citation for case: Wilson v. Arkansas"><em>
   Id.,
  </em>
  at 934, 936</a></span>.
 </p>
<p id="b194-6">
  In
  <em>
   Richards
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385</a></span> (1997),
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  the Wisconsin Supreme Court held that police officers executing search warrants in felony drug investigations were never required to knock and announce their presence. We concluded that this blanket rule was overly broad and held instead that “[i]n order to justify a 'no-knock’ entry, the police must have a reasonable suspicion that knocking and announcing them presence, under the particular circumstances, would be dangerous or futile, or that it would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence.”
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#394" aria-description="Citation for case: Richards v. Wisconsin"><em>
   Id.,
  </em>
  at 394</a></span>.
 </p>
<p id="b194-7">
  Neither of these cases explicitly addressed the question whether the lawfulness of a no-knock entry depends on whether property is damaged in the course of the entry. It
  <span citation-index="1" class="star-pagination" label="71"> 
   *71
   </span>
  is obvious from their holdings, however, that it does not. Under
  <em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>,
  </em>
  a no-knoek entry is justified if police have a “reasonable suspicion” that knocking and announcing would be dangerous, futile, or destructive to the purposes of the investigation. Whether such a “reasonable suspicion” exists depends in no way on whether police must destroy property in order to enter.
 </p>
<p id="A2r">
  This is not to say that the Fourth Amendment speaks not at all to the manner of executing a search warrant. The general touchstone of reasonableness which governs Fourth Amendment analysis, see
  <em>
   Pennsylvania
  </em>
  v.
  <em>
   Mimms,
  </em>
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#108" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 108-109</a></span> (1977)
  <em>
   (per curiam),
  </em>
  governs the method of execution of the warrant. Excessive or unnecessary destruction of property in the course of a search may violate the Fourth Amendment, even though the entry itself is lawful and the fruits of the search are not subject to suppression.
 </p>
<p id="b195-6">
  Applying these principles to the facts at hand, we conclude that no Fourth Amendment violation occurred. A reliable confidential informant had notified the police that Alan Shelby might be inside respondent’s home, and an officer had confirmed this possibility. Shelby was a prison escapee with a violent past who reportedly had access to a large supply of weapons. He had vowed that he would “‘not do federal time.’” The police certainly had a “reasonable suspicion” that knocking and announcing their presence might be dangerous to themselves or to others.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b195-7">
  As for the manner in which the entry was accomplished, the police here broke a single window in respondent’s garage. They did so because they wished to discourage Shelby, or any other occupant of the house, from rushing to the weapons that the informant had told them respondent might have
  <span citation-index="1" class="star-pagination" label="72"> 
   *72
   </span>
  kept there. Their conduct was clearly reasonable and we conclude that there was no
  <em>
   Fourth
  </em>
  Amendment violation.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b196-5">
  Respondent also argues, however, that suppression is appropriate because the officers executing the warrant violated <span class="citation no-link">18 U. S. C. §3109</span>. This statutory argument fares no better. Section 3109 provides:
 </p>
<blockquote id="b196-6">
  "The officer may break open any outer or inner door or window of a house, or any part of a house, or anything therein, to execute a search warrant, if, after notice of his authority and purpose, he is refused admittance or when necessary to liberate himself or a person aiding him in the execution of the warrant.”
 </blockquote>
<p id="b196-7">
  Respondent contends that the statute specifies the only circumstances under which an officer may damage property in executing a search warrant, and that it therefore forbids all other property-damaging entries.
 </p>
<p id="b196-8">
  But by its terms § 3109 prohibits nothing. It merely authorizes officers to damage property in certain instances. Even accepting,
  <em>
   arguendo,
  </em>
  that the statute implicitly forbids some of what it does not expressly permit, it is of no help to respondent. In
  <em>
   Miller
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#313" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 313</a></span> (1958), we noted that §3109’s "requirement of prior notice . .. before forcing entry ... codif[ied] a tradition embedded in Anglo-American law.” We repeated this point in
  <em>
   Sabbath
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="107718"><a href="/opinion/107718/sabbath-v-united-states/#591" aria-description="Citation for case: Sabbath v. United States">391 U. S. 585, 591, n. 8</a></span> (1968) (referring to §3109 as “codification” of the common law). In neither of
  <span citation-index="1" class="star-pagination" label="73"> 
   *73
   </span>
  these cases, however, did we expressly hold that §3109 also codified the exceptions to the common-law requirement of notice before entry. In
  <em>
   <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span>
  </em>
  the Government made “no claim ... of the existence of circumstances excusing compliance” and the question was accordingly not before us. <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#309" aria-description="Citation for case: Miller v. United States">357 U. S., at 309</a></span>. In
  <em>
   <span class="citation" data-id="107718"><a href="/opinion/107718/sabbath-v-united-states/" aria-description="Citation for case: Sabbath v. United States">Sabbath</a></span>
  </em>
  the Government did make such a claim, but because the record did “not reveal any substantial basis for the failure of the agents ... to announce their authority” we did not decide the question. We did note, however, that “[e]xceptions to any possible constitutional rule relating to announcement and entry have been recognized . . . and there is little'reason why those limited exceptions might not also apply to § 3109, since they existed at common law, of which the statute is a codification.” <span class="citation" data-id="107718"><a href="/opinion/107718/sabbath-v-united-states/#591" aria-description="Citation for case: Sabbath v. United States">391 U. S., at 591, n. 8</a></span>.
 </p>
<p id="b197-5">
  In this case the question is squarely presented. We remove whatever doubt may remain on the subject and hold that §3109 codifies the exceptions to the common-law announcement requirement. If § 3109 codifies the common law in this area, and the common law in turn informs the Fourth Amendment, our decisions in
  <em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
  </em>
  and
  <em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>
  </em>
  serve as guideposts in construing the statute. In
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), we concluded that the common-law principle of announcement is “an element of the reasonableness inquiry under the Fourth Amendment,” but noted that the principle “was never stated as an inflexible rule requiring announcement under all circumstances.”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#934" aria-description="Citation for case: Wilson v. Arkansas"><em>
   Id.,
  </em>
  at 934</a></span>. In
  <em>
   Richards
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385</a></span> (1997), we articulated the test used to determine whether exigent circumstances justify a particular no-knock entry.
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#394" aria-description="Citation for case: Richards v. Wisconsin"><em>
   Id.,
  </em>
  at 394</a></span>. We therefore hold that § 3109 includes an exigent circumstances exception and that the exception’s applicability in a given instance is measured by the same standard we articulated in
  <em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>.
  </em>
  The police met that standard here and § 3109 was therefore not violated.
 </p>
<p id="b198-4">
<span citation-index="1" class="star-pagination" label="74"> 
   *74
   </span>
  We accordingly reverse the judgment of the Court of Appeals and remand this case for further proceedings consistent with this opinion.
 </p>
<p id="b198-5">
<em>
   It is so ordered.
  </em>
</p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b194-8">
   It should be noted that our opinion in
   <em>
    <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>
   </em>
   came down after the Court of Appeals issued its opinion in this case.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b195-8">
   It is of no consequence that Shelby was not found. “[I]n determining the lawfulness of entry and the existence of probable cause we may concern ourselves only with what the officers had reason to believe
   <em>
    at the time of their entry.” Ker
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#40" aria-description="Citation for case: Ker v. California">374 U. S. 23, 40-41, n. 12</a></span> (1963) (opinion of Clark, J.) (emphasis in original).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b196-9">
   After concluding that the Fourth Amendment had been violated in this case, the Ninth Circuit farther concluded that the guns should be excluded from evidence. Because we conclude that there was no Fourth Amendment violation, we need not decide whether, for example, there was sufficient causal relationship between the breaking of the window and the discovery of the guns to warrant suppression of the evidence. Cf.
   <em>
    Nix
   </em>
   v.
   <em>
    Williams,
   </em>
   <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U. S. 431</a></span> (1984);
   <em>
    Wong Sun
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963).
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Ramsey.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Ramsey"
type: case
citation: "431 U.S. 606 (1977)"
parallel_cite: "97 S. Ct. 1972; 52 L. Ed. 2d 617"
neutral_cite: 1977 U.S. LEXIS 101
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-06-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-06-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Ramsey
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109675/united-states-v-ramsey/"
  cluster_id: 109675
  opinion_id: 109675
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Anchor"
related: ["[[Carroll v. United States]]", "[[United States v. Flores-Montano]]", "[[United States v. Montoya de Hernandez]]"]
aliases: []
tags: ["case", "fourth-amendment", "border-searches", "international-mail", "customs", "reasonable-suspicion"]
holding: "Routine searches at the international border (including incoming international mail) require neither a warrant nor probable cause; the…"
lake:
  record_id: United States v. Ramsey
  status: verified
  projected_at: 2026-07-09
---

# United States v. Ramsey

*431 U.S. 606 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A customs inspector working incoming international mail opened envelopes mailed from Thailand to addresses in the United States. The envelopes were bulky, many times the weight of a normal airmail letter, and felt as though they contained something; inside, the inspector found heroin. Charged with importing heroin through the mails, the defendants moved to suppress, contending that opening the letters without a warrant violated the Fourth Amendment.

## Issue
Whether customs officials may open incoming international mail at the border without a warrant, consistent with the Fourth Amendment, when they have reasonable cause to suspect it contains contraband.

## Rule
Border searches are reasonable simply because they occur at the border. "That searches made at the border, pursuant to the longstanding right of the sovereign to protect itself by stopping and examining persons and property crossing into this country, are reasonable simply by virtue of the fact that they occur at the border, should, by now, require no extended demonstration." — 431 U.S. at 616. ^pin-616

The governing statute permits opening such mail on "reasonable cause to suspect" contraband — a standard less demanding than probable cause: "The 'reasonable cause to suspect' test adopted by the statute is, we think, a practical test which imposes a less stringent requirement than that of 'probable cause' imposed by the Fourth Amendment as a requirement for the issuance of warrants." — [431 U.S. at 612–613](https://www.courtlistener.com/opinion/109675/united-states-v-ramsey/#:~:text=with%20%22-,reasonable%20cause%20to%20suspect). ^pin-612

## Application
The inspector knew the letters were from Thailand, were bulky, were many times the weight of a normal airmail letter, and felt as though they held something — facts giving reasonable cause to suspect they contained merchandise or contraband. The search was authorized by statute, and because it was a border search it required neither a warrant nor probable cause; opening the envelopes therefore did not violate the Fourth Amendment.

## Conclusion
The warrantless opening of the international mail was a constitutional border search; the Supreme Court reversed the Court of Appeals and upheld the searches.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Ramsey* anchors the border-search exception and extends it to incoming international mail: routine border searches need neither a warrant nor probable cause, and the statutory "reasonable cause to suspect" standard for opening mail is less demanding than probable cause.

## Appears on
- [[Border Searches]] — *Key — Anchor*

## Sources
- *United States v. Ramsey*, 431 U.S. 606 (1977) — https://www.courtlistener.com/opinion/109675/united-states-v-ramsey/ — pinpoints: 612–613, 616 (parallel 97 S. Ct. 1972).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d99033e779462d87", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Ramsey"}, "payload": {"all": [{"cite": "431 U.S. 606", "page": "606", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "431"}, {"cite": "97 S. Ct. 1972", "page": "1972", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "52 L. Ed. 2d 617", "page": "617", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "52"}, {"cite": "1977 U.S. LEXIS 101", "page": "101", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "431 U.S. 606", "official": {"cite": "431 U.S. 606", "page": "606", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "431"}, "official_selection_present": true, "record_id": "United States v. Ramsey"}}
{"assertion_id": "2c37c74cf1b06e11", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-612", "record_id": "United States v. Ramsey"}, "payload": {"fragment": "#:~:text=with%20%22-,reasonable%20cause%20to%20suspect", "page": null, "pin_id": "pin-612", "pinpoint_status": "star-verified", "quote": "reasonable cause to suspect", "quote_fidelity": "matched", "record_id": "United States v. Ramsey", "star_marker": "607"}}
{"assertion_id": "f731d533aa67d9fe", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-616", "record_id": "United States v. Ramsey"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-616", "pinpoint_status": "slip-only", "quote": "--- # United States v. Ramsey *431 U.S. 606 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A customs inspector working incoming international mail opened envelopes mailed from Thailand to addresses in the United States. The envelopes were bulky, many times the weight of a normal airmail letter, and felt as though they contained something; inside, the inspector found heroin. Charged with importing heroin through the mails, the defendants moved to suppress, contending that opening the letters without a warrant violated the Fourth Amendment. ## Issue Whether customs officials may open incoming international mail at the border without a warrant, consistent with the Fourth Amendment, when they have reasonable cause to suspect it contains contraband. ## Rule Border searches are reasonable simply because they occur at the border.", "quote_fidelity": "mismatch", "record_id": "United States v. Ramsey", "star_marker": null}}
{"assertion_id": "56e54acd32231d67", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Ramsey"}, "payload": {"as_of_content": "1977-06-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Ramsey", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Ramsey

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ramsey",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Ramsey",
    "case_name_short": "Ramsey",
    "case_name_full": "UNITED STATES v. RAMSEY Et Al.",
    "input_case_name": "United States v. Ramsey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-06-06",
    "year": 1977,
    "docket": null,
    "cluster_id": 109675,
    "lead_opinion_id": 109675,
    "sibling_ids": [
      109675,
      9426823,
      9426824,
      9426825
    ],
    "absolute_url": "/opinion/109675/united-states-v-ramsey/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "431 U.S. 606",
      "volume": "431",
      "reporter": "U.S.",
      "page": "606",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 1972",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "1972",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 L. Ed. 2d 617",
        "volume": "52",
        "reporter": "L. Ed. 2d",
        "page": "617",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 101",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "101",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "431 U.S. 606",
        "volume": "431",
        "reporter": "U.S.",
        "page": "606",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 1972",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "1972",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 L. Ed. 2d 617",
        "volume": "52",
        "reporter": "L. Ed. 2d",
        "page": "617",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 101",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "101",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "431 U.S. 606",
    "official_selection": {
      "court_class": "scotus",
      "selected": "431 U.S. 606",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-616",
      "page": null,
      "quote": "--- # United States v. Ramsey *431 U.S. 606 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A customs inspector working incoming international mail opened envelopes mailed from Thailand to addresses in the United States. The envelopes were bulky, many times the weight of a normal airmail letter, and felt as though they contained something; inside, the inspector found heroin. Charged with importing heroin through the mails, the defendants moved to suppress, contending that opening the letters without a warrant violated the Fourth Amendment. ## Issue Whether customs officials may open incoming international mail at the border without a warrant, consistent with the Fourth Amendment, when they have reasonable cause to suspect it contains contraband. ## Rule Border searches are reasonable simply because they occur at the border.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-612",
      "page": null,
      "quote": "reasonable cause to suspect",
      "star_marker": "607",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 1178,
      "fragment": "#:~:text=with%20%22-,reasonable%20cause%20to%20suspect",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-06-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Ramsey",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Caballero",
          "cluster_id": 7319742,
          "cite": [
            "178 F. Supp. 3d 1008",
            "2016 U.S. Dist. LEXIS 51132",
            "2016 WL 1546731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cotterman",
          "cluster_id": 213651,
          "cite": [
            "637 F.3d 1068",
            "2011 U.S. App. LEXIS 6483",
            "2011 WL 1137302"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stefan Irving",
          "cluster_id": 794720,
          "cite": [
            "452 F.3d 110",
            "2006 U.S. App. LEXIS 16077",
            "2006 WL 1735582"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Oladiji v. United States",
          "cluster_id": 8744707,
          "cite": [
            "953 F. Supp. 43",
            "1996 U.S. Dist. LEXIS 20367",
            "1996 WL 785758"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. LePera",
          "cluster_id": 6100913,
          "cite": [
            "197 A.D.2d 43",
            "611 N.Y.S.2d 394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Antonio Sylvester Hill and Joseph Herbert Francois",
          "cluster_id": 565137,
          "cite": [
            "939 F.2d 934",
            "1991 U.S. App. LEXIS 19428",
            "1991 WL 148908"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Ezeiruaku",
          "cluster_id": 563242,
          "cite": [
            "936 F.2d 136",
            "1991 WL 105684"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Patrick, Linda Taylor and Christopher Patrick",
          "cluster_id": 538805,
          "cite": [
            "899 F.2d 169",
            "1990 U.S. App. LEXIS 4674"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Enrique Carreon",
          "cluster_id": 521938,
          "cite": [
            "872 F.2d 1436",
            "1989 U.S. App. LEXIS 5032",
            "1989 WL 36046"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Juan Manuel Caminos",
          "cluster_id": 457063,
          "cite": [
            "770 F.2d 361",
            "1985 U.S. App. LEXIS 22328"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Villamonte-Marquez",
          "cluster_id": 110973,
          "cite": [
            "77 L. Ed. 2d 22",
            "103 S. Ct. 2573",
            "462 U.S. 579",
            "1983 U.S. LEXIS 68",
            "51 U.S.L.W. 4812"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James N. Gramenos v. Jewel Companies, Inc.",
          "cluster_id": 474259,
          "cite": [
            "797 F.2d 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rita Ann Cardenas and Shamsideen Abiodun Lawal",
          "cluster_id": 657339,
          "cite": [
            "9 F.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Puerto Rico",
          "cluster_id": 2620876,
          "cite": [
            "61 L. Ed. 2d 1",
            "99 S. Ct. 2425",
            "442 U.S. 465",
            "1979 U.S. LEXIS 111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Flores-Montano",
          "cluster_id": 134729,
          "cite": [
            "158 L. Ed. 2d 311",
            "124 S. Ct. 1582",
            "541 U.S. 149",
            "2004 U.S. LEXIS 2548",
            "72 U.S.L.W. 4263",
            "17 Fla. L. Weekly Fed. S 207"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stuart Romm",
          "cluster_id": 795139,
          "cite": [
            "455 F.3d 990",
            "2006 U.S. App. LEXIS 18474",
            "2006 WL 2042827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
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
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pierce v. Smith",
          "cluster_id": 12443,
          "cite": [
            "117 F.3d 866",
            "13 I.E.R. Cas. (BNA) 8",
            "1997 U.S. App. LEXIS 17907",
            "1997 WL 395259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frank Gunnar Williams",
          "cluster_id": 375926,
          "cite": [
            "617 F.2d 1063",
            "1980 U.S. App. LEXIS 17636",
            "1980 A.M.C. 2550"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Serafin Alfonso, Humberto Rayo, Fabian Mora, Primo Antonio Serrano-Tellez",
          "cluster_id": 450644,
          "cite": [
            "759 F.2d 728",
            "18 Fed. R. Serv. 1398",
            "1985 U.S. App. LEXIS 30539"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alfaro-Moncada",
          "cluster_id": 147332,
          "cite": [
            "607 F.3d 720",
            "2010 A.M.C. 1680",
            "2010 U.S. App. LEXIS 10841",
            "2010 WL 2103442"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elias Attallah, Violeta Lajam De Attallah, and the Conjugal Partnership They Comprise v. United States",
          "cluster_id": 577110,
          "cite": [
            "955 F.2d 776",
            "1992 U.S. App. LEXIS 1454",
            "1992 WL 17486"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensel",
          "cluster_id": 8926652,
          "cite": [
            "699 F.2d 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Silveus",
          "cluster_id": 1439120,
          "cite": [
            "542 F.3d 993",
            "50 V.I. 1101",
            "2008 U.S. App. LEXIS 19224",
            "2008 WL 4138460"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reporters Committee for Freedom of the Press v. American Telephone & Telegraph Company",
          "cluster_id": 363949,
          "cite": [
            "593 F.2d 1030",
            "192 U.S. App. D.C. 376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramsey:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109675 OR 9426823 OR 9426824 OR 9426825) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NjYxMjgwMDAwMDAmcz00NDE3NDYmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109675+OR+9426823+OR+9426824+OR+9426825%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(109675 OR 9426823 OR 9426824 OR 9426825)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OCZzPTU3MzA2NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109675+OR+9426823+OR+9426824+OR+9426825%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109675 OR 9426823 OR 9426824 OR 9426825)",
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
    "complete_query": "cites:(109675 OR 9426823 OR 9426824 OR 9426825)",
    "indexed_citing_opinions": 459,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109675,
        "count": 393,
        "count_source": "search"
      },
      {
        "opinion_id": 9426823,
        "count": 86,
        "count_source": "search"
      },
      {
        "opinion_id": 9426824,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426825,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 663,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-ramsey.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY5ODE2NDgmcz00Nzk5ODI0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109675+OR+9426823+OR+9426824+OR+9426825%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109675,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 90759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 103143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 105930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 106078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109011,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 265141,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 307979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 321210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 326933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 327074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 328030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 337566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 337725,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109675,
        "cited_id": 339048,
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
    "date_created": "2026-07-06T02:24:42Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:24:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:24:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:28:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:24:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Ramsey

```
<div>
<center><b><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">431 U.S. 606</a></span> (1977)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
RAMSEY ET AL.</h1></center>
<center>No. 76-167.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 30, 1977.</center>
<center>Decided June 6, 1977.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><span class="star-pagination">*607</span> <i>Kenneth S. Geller</i> argued the cause for the United States. on the brief were <i>Solicitor General Bork, Assistant Attorney General Thornburgh,</i> and <i>Jerome M. Feit.</i></p>
<p><i>Allan M. Palmer</i> argued the cause and filed a brief for respondent Ramsey. <i>Irving R. M. Panzer,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./429/916/">429 U. S. 916</a></span>, argued the cause and filed a brief for respondent Kelly.<sup>[*]</sup></p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Customs officials, acting with "reasonable cause to suspect" a violation of customs laws, opened for inspection incoming international letter-class mail without first obtaining a search warrant. A divided Court of Appeals for the District of Columbia <span class="star-pagination">*608</span> Circuit held, contrary to every other Court of Appeals which has considered the matter,<sup>[1]</sup> that the Fourth Amendment forbade the opening of such mail without probable cause and a search warrant. 176 U. S. App. D. C. 67, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d 415</a></span>. We granted the Government's petition for certiorari to resolve this Circuit conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./429/815/">429 U. S. 815</a></span>. We now reverse.</p>
<p></p>
<h2>I</h2>
<p>Charles W. Ramsey and James W. Kelly jointly commenced a heroin-by-mail enterprise in the Washington, D. C., area. The process involved their procuring of heroin, which was mailed in letters from Bangkok, Thailand, and sent to various locations in the District of Columbia area for collection. Two of their suppliers, Sylvia Bailey and William Ward, who were located in West Germany, were engaged in international narcotics trafficking during the latter part of 1973 and the early part of 1974. West German agents, pursuant to court-authorized electronic surveillance, intercepted several trans-Atlantic conversations between Bailey and Ramsey during which their narcotics operation was discussed. By late January 1974, Bailey and Ward had gone to Thailand. Thai <span class="star-pagination">*609</span> officials, alerted to their presence by West German authorities, placed them under surveillance. Ward was observed mailing letter-sized envelopes in six different mail boxes; five of these envelopes were recovered; and one of the addresses in Washington, D. C., was later linked to respondents. Bailey and Ward were arrested by Thai officials on February 2, 1974; among the items seized were eleven heroin-filled envelopes addressed to the Washington, D. C., area, and later connected with respondents.</p>
<p>Two days after this arrest of Bailey and Ward, Inspector George Kallnischkies, a United States customs officer in New York City, without any knowledge of the foregoing events, inspecting a sack of incoming international mail from Thailand, spotted eight envelopes that were bulky and which he believed might contain merchandise.<sup>[2]</sup> The envelopes, all of which appeared to him to have been typed on the same typewriter, were addressed to four different locations in the Washington, D. C., area. Inspector Kallnischkies, based on the fact that the letters were from Thailand, a known source of narcotics, and were "rather bulky," suspected that the envelopes might contain merchandise or contraband rather than correspondence. He took the letters to an examining area in the post office, and felt one of the letters: It "felt like there was something in there, in the envelope. It was not just plain paper that the envelope is supposed to contain." He weighed one of the envelopes, and found it weighed 42 grams, some three to six times the normal weight of an airmail letter. Inspector Kallnischkies then opened that envelope:<sup>[3]</sup></p>
<blockquote>"In there I saw some cardboard and between the cardboard, if I recall, there was a plastic bag containing a <span class="star-pagination">*610</span> white powdered substance, which, based on experience, I knew from Thailand would be heroin.</blockquote>
<blockquote>"I went ahead and removed a sample. Gave it a field test, a Marquis Reagent field test, and I had a positive reaction for heroin." App. 32.</blockquote>
<p>He proceeded to open the other seven envelopes which "in a lot of ways were identical"; examination revealed that at least the contents were in fact identical: each contained heroin.</p>
<p>The envelopes were then sent to Washington in a locked pouch where agents of the Drug Enforcement Administration, after obtaining a search warrant, opened the envelopes again and removed most of the heroin.<sup>[4]</sup> The envelopes were then resealed, and six of them were delivered under surveillance. After Kelly collected the envelopes from the three different addressees, rendezvoused with Ramsey, and gave Ramsey a brown paper bag, federal agents arrested both of them. The bag contained the six envelopes with heroin, $1,100 in cash, and "cutting" material for the heroin. The next day, in executing a search upon warrant of Ramsey's residence, agents recovered, <i>inter alia,</i> two pistols.</p>
<p>Ramsey and Kelly were indicted, along with Bailey and Ward, in a 17-count indictment.<sup>[5]</sup> Respondents moved to <span class="star-pagination">*611</span> suppress the heroin and the two pistols.<sup>[6]</sup> The District Court denied the motions, and after a bench trial on the stipulated record, respondents were found guilty and sentenced to imprisonment for what is in effect a term of 10 to 30 years. The Court of Appeals for the District of Columbia Circuit, one judge dissenting, reversed the convictions, holding that the "border search exception to the warrant requirement" applicable to persons, baggage, and mailed packages did not apply to the routine opening of international letter mail, and held that the Constitution requires that "before international letter mail is opened, a showing of probable cause be made to and a warrant secured from a neutral magistrate." 176 U. S. App. D. C., at 73, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/#421" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d, at 421</a></span>.<sup>[7]</sup></p>
<p></p>
<h2>II</h2>
<p>Congress and the applicable postal regulations authorized the actions undertaken in this case. Title <span class="citation no-link">19 U. S. C. § 482</span>, a recodification of Rev. Stat. § 3061, and derived from § 3 of the Act of July 18, 1866, <span class="citation no-link">14 Stat. 178</span>, explicitly deals with the search of an "envelope":</p>
<blockquote>"Any of the officers or persons authorized to board or search vessels may . . . search any trunk or envelope, wherever found, in which he may have a reasonable cause to suspect there is merchandise which was imported contrary to law . . . ."</blockquote>
<p>This provision authorizes customs officials to inspect, under <span class="star-pagination">*612</span> the circumstances therein stated, incoming international mail.<sup>[8]</sup> The "reasonable cause to suspect" test adopted by the statute is, we think, a practical test which imposes a less stringent <span class="star-pagination">*613</span> requirement than that of "probable cause" imposed by the Fourth Amendment as a requirement for the issuance of warrants. See <i>United States</i> v. <i>King,</i> <span class="citation" data-id="328030"><a href="/opinion/328030/united-states-v-edward-king-and-mose-franklin-pearson/" aria-description="Citation for case: United States v. Edward King and Mose Franklin Pearson">517 F. 2d 350</a></span>, 352 <span class="star-pagination">*614</span> (CA5 1975); cf. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#8" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 8, 21-22, 27</a></span> (1968). Inspector Kallnischkies, at the time he opened the letters, knew that they were from Thailand, were bulky, were many times the weight of a normal airmail letter, and "felt like there was something in there." Under these circumstances, we have no doubt that he had reasonable "cause to suspect" that there was merchandise or contraband in the envelopes.<sup>[9]</sup><span class="star-pagination">*615</span> The search, therefore, was plainly authorized by the statute.<sup>[10]</sup></p>
<p>Since the search in this case was authorized by statute, we are left simply with the question of whether the search, nevertheless violated the Constitution. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#877" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 877</a></span> (1975). Specifically, we need not decide whether Congress conceived the statute as a necessary precondition to the validity of the search or whether it was viewed, instead, as a limitation on otherwise existing authority of the Executive.<sup>[11]</sup> Having acted pursuant to, and <span class="star-pagination">*616</span> within the scope of, a congressional Act, Inspector Kallnischkies' searches were permissible unless they violated the Constitution.</p>
<p></p>
<h2>III</h2>
<p></p>
<h2>A</h2>
<p>That searches made at the border, pursuant to the longstanding right of the sovereign to protect itself by stopping and examining persons and property crossing into this country, are reasonable simply by virtue of the fact that they occur at the border, should, by now, require no extended demonstration. The Congress which proposed the Bill of Rights, including the Fourth Amendment, to the state legislatures on September 25, 1789, <span class="citation no-link">1 Stat. 97</span>, had, some two months prior to that proposal, enacted the first customs statute, Act of July 31, 1789, c. 5, <span class="citation no-link">1 Stat. 29</span>. Section 24 of this statute granted customs officials "full power and authority" to enter and search "any ship or vessel, in which they shall have reason to suspect any goods, wares or merchandise subject to duty shall be concealed . . . ." This acknowledgment of plenary customs power was differentiated from the more limited power to enter and search "any particular dwelling-house, store, building, or other place . . ." where a warrant upon "cause to suspect" was required.<sup>[12]</sup> The historical importance of the <span class="star-pagination">*617</span> enactment of this customs statute by the same Congress which proposed the Fourth Amendment is, we think, manifest. This Court so concluded almost a century ago. In <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 623</a></span> (1886), this Court observed:</p>
<blockquote>"The seizure of stolen goods is authorized by the common law; and the seizure of goods forfeited for a breach of the revenue laws, or concealed to avoid the duties payable on them, has been authorized by English statutes for at least two centuries past; and the like seizures have been authorized by our own revenue acts from the commencement of the government. The first statute passed by Congress to regulate the collection of duties, the act of July 31, 1789, <span class="citation no-link">1 Stat. 29</span>, 43, contains provisions to this effect. <i>As this act was passed by the same Congress which proposed for adoption the original amendments to the Constitution, it is clear that the members of that body did not regard searches and seizures of this kind as `unreasonable,' and they are not embraced within the prohibition of the amendment.</i>" (Emphasis supplied.)</blockquote>
<p>This interpretation, that border searches were not subject to the warrant provisions of the Fourth Amendment and were "reasonable" within the meaning of that Amendment, has been faithfully adhered to by this Court. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), after noting that "[t]he Fourth Amendment <span class="star-pagination">*618</span> does not denounce all searches or seizures, but only such as are unreasonable," <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#147" aria-description="Citation for case: Carroll v. United States"><i>id.,</i> at 147</a></span>, recognized the distinction between searches within this country, requiring probable cause, and border searches, <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">id.,</a></span></i> at 153-154:</p>
<blockquote>"It would be intolerable and unreasonable if a prohibition agent were authorized to stop every automobile on the chance of finding liquor and thus subject all persons lawfully using the highways to the inconvenience and indignity of such a search. <i>Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in.</i> But those lawfully within the country . . . have a right to free passage without interruption or search unless there is known to a competent official authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise."<sup>[13]</sup> (Emphasis supplied.)</blockquote>
<p>More recently, we noted this longstanding history in <i>United States</i> v. <i>Thirty-seven Photographs,</i> <span class="citation" data-id="9424558"><a href="/opinion/108332/united-states-v-thirty-seven-37-photographs/#376" aria-description="Citation for case: United States v. Thirty-Seven (37) Photographs">402 U. S. 363, 376</a></span> (1971):</p>
<blockquote>"But a port of entry is not a traveler's home. His right to be let alone neither prevents the search of his luggage nor the seizure of unprotected, but illegal, materials when his possession of them is discovered during such a search. Customs officials characteristically inspect luggage and their power to do so is not questioned in this case; it is an old practice and is intimately associated with excluding illegal articles from the country."</blockquote>
<p><span class="star-pagination">*619</span> In <i>United States</i> v. <i>12 200-Ft. Reels of Film,</i> <span class="citation" data-id="9425385"><a href="/opinion/108841/united-states-v-12-200-ft-reels-of-super-8mm-film/#125" aria-description="Citation for case: United States v. 12 200-Ft. Reels of Super 8MM. Film">413 U. S. 123, 125</a></span> (1973), we observed: "Import restrictions and searches of persons or packages at the national borders rest on different considerations and different rules of constitutional law from domestic regulations. The Constitution gives Congress broad, comprehensive powers `[t]o regulate Commerce with foreign Nations.' Art. I, § 8, cl. 3. Historically such broad powers have been necessary to prevent smuggling and to prevent prohibited articles from entry." Finally, citing <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>,</i> this Court stated in <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#272" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 272</a></span> (1973), that it was "without doubt" that the power to exclude aliens "can be effectuated by routine inspections and searches of individuals or conveyances seeking to cross our borders." See also <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 288</a></span> (WHITE, J., dissenting).</p>
<p>Border searches, then, from before the adoption of the Fourth Amendment, have been considered to be "reasonable" by the single fact that the person or item in question had entered into our country from outside. There has never been any additional requirement that the reasonableness of a border search depended on the existence of probable cause. This longstanding recognition that searches at our borders without probable cause and without a warrant are nonetheless "reasonable" has a history as old as the Fourth Amendment itself.<sup>[14]</sup> We reaffirm it now.</p>
<p></p>
<h2>B</h2>
<p>Respondents urge upon us, however, the position that mailed letters are somehow different, and, whatever may be the normal rule with respect to border searches, different considerations, requiring the full panoply of Fourth Amendment <span class="star-pagination">*620</span> protections, apply to international mail. The Court of Appeals agreed, and felt that whatever the rule may be with respect to travelers, their baggage, and even mailed packages, it would not "extend" the border-search exception to include mailed letter-size envelopes. 176 U. S. App. D. C., at 73, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/#421" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d, at 421</a></span>. We do not agree that this inclusion of letters within the border-search exception represents any "extension" of that exception.</p>
<p>The border-search exception is grounded in the recognized right of the sovereign to control, subject to substantive limitations imposed by the Constitution, who and what may enter the country. It is clear that there is nothing in the rationale behind the border-search exception which suggests that the mode of entry will be critical. It was conceded at oral argument that customs officials could search, without probable cause and without a warrant, envelopes carried by an entering traveler, whether in his luggage or on his person. Tr. of Oral Arg. 43-44. Surely no different constitutional standard should apply simply because the envelopes were mailed, not carried. The critical fact is that the envelopes cross the border and enter this country, not that they are brought in by one mode of transportation rather than another. It is their entry into this country from without it that makes a resulting search "reasonable."</p>
<p>Almost a century ago this Court rejected such a distinction in construing a protocol to the Treaty of Berne, <span class="citation no-link">19 Stat. 604</span>, which prohibited the importation of letters which might contain dutiable items. <i>Cotzhausen</i> v. <i>Nazro,</i> <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215</a></span> (1883). Condemning the unsoundness of any distinction between entry by mail and entry by other means, Mr. Justice Miller, on behalf of a unanimous Court, wrote, <i><span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">id.,</a></span></i> at 218:</p>
<blockquote>"Of what avail would it be that every passenger, citizen and foreigner, without distinction of country or sex, is compelled to sign a declaration before landing, either <span class="star-pagination">*621</span> that his trunks and satchels in hand contain nothing liable to duty, or if they do, to state what it is, and even the person may be subjected to a rigid examination, if the mail is to be left unwatched, and all its sealed contents, even after delivery to the person to whom addressed, are to be exempt from seizure, though laces, jewels, and other dutiable matter of great value may thus be introduced from foreign countries."</blockquote>
<p>The historically recognized scope of the border-search doctrine, suggests no distinction in constitutional doctrine stemming from the mode of transportation across our borders. The contrary view of the Court of Appeals and respondents stems, we think, from an erroneous reading of <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>, under which the Court of Appeals reasoned that "the rationale of the border search exception . . . is based upon . . . the difficulty of obtaining a warrant when the subject of the search is mobile, as a car or person . . . ." 176 U. S. App. D. C., at 70, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/#418" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d, at 418</a></span>.<sup>[15]</sup></p>
<p>The fundamental difficulty with this position is that the "border search" exception is not based on the doctrine of "exigent circumstances" at all. It is a longstanding, historically recognized exception to the Fourth Amendent's general principle that a warrant be obtained, and in this respect is like the similar "search incident to lawful arrest" exception treated in <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#224" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 224</a></span> (1973). We think that the language in <i>Carroll</i> v. <i>United States, supra</i><i>,</i> makes this point abundantly clear. The <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> Court <span class="star-pagination">*622</span> quoted verbatim the above-quoted language from <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), including the reference to customs searches and seizures of the kind authorized by <span class="citation no-link">1 Stat. 29</span>, 43, as being neither "unreasonable" nor "embraced within the prohibition of the [Fourth] [A]mendment." Later in the opinion, the Court commented that having "established that contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for <i>without a warrant,</i> we come now to consider under what circumstances such search may be made." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span> (emphasis supplied). It then, in the passage quoted <i>supra,</i> at 618, distinguished, among these types of searches which required no warrant, those which required <i>probable cause</i> from those which did not: border searches did not; vehicular searches inside the country did. <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> thus recognized that there was no "probable cause" requirement at the border. This determination simply has nothing to do with "exigent circumstances."</p>
<p>The Court of Appeals also relied upon what it described as this Court's refusal in recent years twice "to take an expansive view of the border search exception or the authority of the Border Patrol. See <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> . . . (1975); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> . . . (1973)." 176 U. S. App. D. C., at 72, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/#420" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d, at 420</a></span>. But, as the language from each of these opinions suggests, <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#876" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 876, 884</a></span>; 413 U. S., at 272-273, plenary border-search authority was not implicated by our refusal to uphold searches and stops made at places in the interior of the country; the express premise for each holding was that the checkpoint or stop in question was not the border or its "functional equivalent."</p>
<p>In view of the wealth of authority establishing the border search as "reasonable" within the Fourth Amendment even though there be neither probable cause nor a warrant, we reject the distinctions made by the Court of Appeals in its opinion.</p>
<p><span class="star-pagination">*623</span> Nor do we agree that, under the circumstances presented by this case, First Amendment considerations dictate a full panoply of Fourth Amendment rights prior to the border search of mailed letters. There is, again, no reason to distinguish between letters mailed into the country, and letters carried on the traveler's person.<sup>[16]</sup> More fundamentally, however, the existing system of border searches has not been shown to invade protected First Amendment rights,<sup>[17]</sup> and hence there is no reason to think that the potential presence of correspondence makes the otherwise constitutionally reasonable search "unreasonable."</p>
<p>The statute in question requires that there be "reasonable cause to believe" the customs laws are being violated prior to the opening of envelopes. Applicable postal regulations flatly prohibit, under all circumstances, the reading of correspondence absent a search warrant, <span class="citation no-link">19 CFR § 145.3</span> (1976):</p>
<blockquote>"No customs officer or employee shall read or authorize or allow any other person to read any correspondence contained in sealed letter mail of foreign origin unless a search warrant has been obtained in advance from an appropriate judge or U. S. magistrate which authorizes such action."</blockquote>
<p>Cf. <span class="citation no-link">18 U. S. C. § 1702</span>.</p>
<p>We are unable to agree with the Court of Appeals that the opening of international mail in search of customs violations, <span class="star-pagination">*624</span> under the above guidelines, impermissibly chills the exercise of free speech. Accordingly, we find it unnecessary to consider the constitutional reach of the First Amendment in this area in the absence of the existing statutory and regulatory protection.<sup>[18]</sup> Here envelopes are opened at the border only when the customs officers have reason to believe they contain other than correspondence, while the reading of any correspondence inside the envelopes is forbidden. Any "chill" that might exist under these circumstances may fairly be considered not only "minimal," <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 560, 562</a></span> (1976); cf. <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 316-317</a></span> (1972), but also wholly subjective.<sup>[19]</sup></p>
<p>We therefore conclude that the Fourth Amendment does not interdict the actions taken by Inspector Kallnischkies in <span class="star-pagination">*625</span> opening and searching the eight envelopes. The judgment of the Court of Appeals is, therefore,</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>The statute at issue expressly authorizes customs officials to "search any . . . envelope" at the border where there is "reasonable cause to suspect" the importation of contraband. <span class="citation no-link">19 U. S. C. § 482</span>. In view of the necessarily enhanced power of the Federal Government to enforce customs laws at the border, I have no doubt that this statuterequiring as a precondition to the opening of mail "reasonable cause to suspect" a violation of lawadequately protects both First and Fourth Amendment rights.<sup>[*]</sup></p>
<p>I therefore join in the judgment of the Court. On the understanding that the precedential effect of today's decision does not go beyond the validity of mail searches at the border pursuant to the statute, I also join the opinion of the Court.</p>
<p>MR. JUSTICE STEVENS, with whom MR. JUSTICE BRENNAN and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>The decisive question in this case is whether Congress has granted customs officials the authority to open and inspect personal letters entering the United States from abroad without the knowledge or consent of the sender or the addressee, and without probable cause to believe the mail contains contraband or dutiable merchandise.</p>
<p>In 1971 the Department of the Treasury and the Post Office Department first asserted that Congress had granted such authority in an awkwardly drafted statute enacted in 1866. <span class="star-pagination">*626</span> Under the earlier practice, which had been consistently followed for 105 years, customs officials were not allowed to open foreign mail except in the presence, and with the consent, of the addressees,<sup>[1]</sup> unless of course a warrant supported by probable cause had been first obtained. There are five reasons why I am convinced that Congress did not authorize the kind of secret searches of private mail that the Executive here conducted.</p>
<p>First, throughout our history Congress has respected the individual's interest in private communication. The notion that private letters could be opened and inspected without notice to the sender or the addressee is abhorrent to the tradition of privacy and freedom to communicate protected by the Bill of Rights. I cannot believe that any member of the Congress would grant such authority without considering its constitutional implications.<sup>[2]</sup></p>
<p><span class="star-pagination">*627</span> Second, the legislative history of the 1866 statute unambiguously discloses that this very concern was voiced during debate by Senator Howe, and that he was assured by the sponsor of the legislation that the bill would not authorize the examination of the United States mails. This colloquy is too plain to be misunderstood:</p>
<blockquote>"Mr. HOWE. The second and third sections of this bill speak of the seizure, search, and examination of all trunks, packages, and envelopes. It seems to me that language is broad enough to cover the United States mails. I suppose it is not the purpose of the bill to authorize the examination of the United States mails.</blockquote>
<blockquote>"Mr. MORRILL [sponsor of the bill]. Of course not.</blockquote>
<blockquote>"Mr. HOWE. I propose to offer an amendment to prevent such a construction.</blockquote>
<blockquote>"Mr. EDMUNDS. There is no danger of such a construction being placed upon this language. It is the language usually employed in these bills.</blockquote>
<blockquote>"Mr. HOWE. If gentlemen are perfectly confident that it will bear no such construction, and will receive no such construction, I do not care to press it.</blockquote>
<blockquote>"The PRESIDING OFFICER. The Senator from Wisconsin withdraws his amendment."<sup>[3]</sup></blockquote>
<p><span class="star-pagination">*628</span> Third, the language of the statute itself, when read in its entirety, quite plainly has reference to packages of the kind normally used to import dutiable merchandise.<sup>[4]</sup> It is true <span class="star-pagination">*629</span> that buried deep in the first long sentence in § 3 of the Act to prevent smuggling there is an authorization to "search any trunk or envelope, wherever found." I do not believe, however, that the word "envelope" as there used was intended to refer to ordinary letters. Contemporary American dictionaries <span class="star-pagination">*630</span> emphasize the usage of the word as descriptive of a package or wrapper as well as an ordinary letter.<sup>[5]</sup> This emphasis is consistent with the text of the bill as originally introduced, which used the phrase "any trunk, or other envelope."<sup>[6]</sup> Moreover, in 1866 when the Act was passed, there was no concern expressed in Congress about the smuggling of merchandise that would fit in a letter-size envelope.<sup>[7]</sup> A legislative decision to authorize the secret search of private mail would surely be expressed in plainer language than is found in the long statutory provision quoted in the margin; at the very least it would be supported by some affirmative evidence in the legislative history rather than the total disclaimer in the colloquy quoted above.</p>
<p><span class="star-pagination">*631</span> Fourth, the consistent construction of the statutory authorization by a series of changing administrations over a span of 105 years must be accorded great respect.<sup>[8]</sup><i>NLRB</i> v. <i>Bell Aerospace Co.,</i> <span class="citation" data-id="9425683"><a href="/opinion/109011/national-labor-relations-board-v-bell-aerospace-co/#274" aria-description="Citation for case: National Labor Relations Board v. Bell Aerospace Co.">416 U. S. 267, 274-275</a></span>; <i>Helvering</i> v. <i>Reynolds Co.,</i> <span class="citation" data-id="103143"><a href="/opinion/103143/helvering-v-r-j-reynolds-tobacco-co/#114" aria-description="Citation for case: Helvering v. R. J. Reynolds Tobacco Co.">306 U. S. 110, 114-115</a></span>. If the Executive perceives that new conditions and problems justify enlargement of the authority that had been found adequate for over a century, then these matters should be brought to the attention of Congress. Cf. <i>H. K. Porter Co.</i> v. <i>NLRB,</i> <span class="citation" data-id="9424188"><a href="/opinion/108083/h-k-porter-co-v-national-labor-relations-board/#109" aria-description="Citation for case: H. K. Porter Co. v. National Labor Relations Board">397 U. S. 99, 109</a></span>.<sup>[9]</sup></p>
<p>Finally, the asserted justification for the broad power claimed is so weak that it is difficult to believe that Congress would accept it without the most searching analysis. The fear the new practice is intended to overcome is that the addressee of a suspicious item of mail would withhold consent to open foreign mail, thereby necessitating the return of the item to the sender. But the refusal to accept delivery without disclosing the contents of a suspicious letter would itself be a fact which could be consideredalong with whatever indicia caused the inspector to regard the item with suspicion in the first place in a probable-cause determination. There is no reason to believe that the alternatives of probable cause or consent would lead to the extensive return of contraband that <span class="star-pagination">*632</span> would otherwise be confiscated on the basis of "reasonable cause to suspect."</p>
<p>If the Government is allowed to exercise the power it claims, the door will be open to the wholesale, secret examination of all incoming international letter mail. No notice would be necessary either before or after the search. Until Congress has made an unambiguous policy decision that such an unprecedented intrusion upon a vital method of personal communication is in the Nation's interest, this Court should not address the serious constitutional question it decides today. For it is settled that</p>
<blockquote>"when action taken by an inferior governmental agency was accomplished by procedures which raise serious constitutional questions, an initial inquiry will be made to determine whether or not `the President or Congress, within their respective constitutional powers, specifically has decided that the imposed procedures are necessary and warranted and has authorized their use.' [<i>Greene</i> v. <i>McElroy,</i> <span class="citation" data-id="9421855"><a href="/opinion/105930/greene-v-mcelroy/" aria-description="Citation for case: Greene v. McElroy">360 U. S. 474</a></span>,] 507." <i>Hannah</i> v. <i>Larche,</i> <span class="citation" data-id="9422021"><a href="/opinion/106078/hannah-v-larche/#430" aria-description="Citation for case: Hannah v. Larche">363 U. S. 420, 430</a></span>.</blockquote>
<p>Cf. <i>Ashwander</i> v. <i>Tennessee Valley Authority,</i> <span class="citation" data-id="9418878"><a href="/opinion/102605/ashwander-v-tennessee-valley-authority/#347" aria-description="Citation for case: Ashwander v. Tennessee Valley Authority">297 U. S. 288, 347-348</a></span> (Brandeis, J., concurring). Accordingly, I would affirm the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[*]  <i>Melvin L. Wulf, Joel M. Gora,</i> and <i>Jack D. Novik</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging affirmance.</p>
<p>[1]  Several Courts of Appeals have held that international letter-class mail may be opened, pursuant to a border search, without probable cause and without a warrant. <i>United States</i> v. <i>Milroy,</i> <span class="citation" data-id="337725"><a href="/opinion/337725/united-states-v-robert-michael-milroy/" aria-description="Citation for case: United States v. Robert Michael Milroy">538 F. 2d 1033</a></span> (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./426/924/">426 U. S. 924</a></span> (1976); <i>United States</i> v. <i>King,</i> <span class="citation" data-id="328030"><a href="/opinion/328030/united-states-v-edward-king-and-mose-franklin-pearson/" aria-description="Citation for case: United States v. Edward King and Mose Franklin Pearson">517 F. 2d 350</a></span> (CA5 1975); <i>United States</i> v. <i>Barclift,</i> <span class="citation" data-id="8896380"><a href="/opinion/8908839/united-states-v-barclift/" aria-description="Citation for case: United States v. Barclift">514 F. 2d 1073</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./423/842/">423 U. S. 842</a></span> (1975); <i>United States</i> v. <i>Bolin,</i> <span class="citation" data-id="326933"><a href="/opinion/326933/united-states-v-robert-c-bolin-aka-bob-bolin/" aria-description="Citation for case: United States v. Robert C. Bolin, A/K/A Bob Bolin">514 F. 2d 554</a></span> (CA7 1975); <i>United States</i> v. <i>Odland,</i> <span class="citation" data-id="321210"><a href="/opinion/321210/united-states-v-david-john-odland/" aria-description="Citation for case: United States v. David John Odland">502 F. 2d 148</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/1088/">419 U. S. 1088</a></span> (1974). Several other Courts of Appeals, in approving the warrantless opening of mailed packages crossing the borders, have indicated that the opening of international letter-class mail should be governed by the same standards. <i>United States</i> v. <i>Doe,</i> <span class="citation" data-id="307979"><a href="/opinion/307979/united-states-v-john-doe-aka-francisco-rodriquez-aka-juan-velez-s/" aria-description="Citation for case: United States v. John Doe, A/K/A Francisco Rodriquez,...">472 F. 2d 982</a></span> (CA2), cert. denied, <i>sub nom. Rodriguez</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./411/969/">411 U. S. 969</a></span> (1973); <i>United States</i> v. <i>Beckley,</i> <span class="citation" data-id="265141"><a href="/opinion/265141/united-states-v-john-e-beckley-united-states-of-america-v-anderson/" aria-description="Citation for case: United States v. John E. Beckley, United States of...">335 F. 2d 86</a></span> (CA6 1964), cert. denied, <i>sub nom. </i><i>Stone</i> v. <i>United States,</i> <span class="citation" data-id="8951845"><a href="/opinion/8960691/stone-v-united-states/" aria-description="Citation for case: Stone v. United States">380 U. S. 922</a></span> (1965). The First Circuit has reserved the question of letters. <i>United States</i> v. <i>Emery,</i> <span class="citation" data-id="339048"><a href="/opinion/339048/united-states-v-john-edward-emery/#888" aria-description="Citation for case: United States v. John Edward Emery">541 F. 2d 887, 888-889</a></span> (1976).</p>
<p>[2]  The mail was inspected at the General Post Office in New York City, where incoming international air mail landing at Kennedy Airport is taken for routing and customs inspections. There is no dispute that this is the "border" for purposes of border searches, see n. 11, <i>infra.</i></p>
<p>[3]  Inspector Kallnischkies also testified that his "normal procedure," when examining envelopes from certain countries which were of a certain weight and bulkiness, was to "shake it a little," and "if it moves, I know there is something in there that is not correspondence. It is merchandise and I have to open it to check it out." App. 48-49. He was unable to specifically recall, however, whether or not he had followed the "normal procedure" in this case.</p>
<p>[4]  The Government does not seek to justify the original discovery of the heroin on the basis of this warrant: "[A] post-opening warrant obviously does not justify the original opening." Brief for United States 4 n. 2. We accordingly accord no significance to the obtaining of this subsequent warrant.</p>
<p>[5]  Bailey and Ward, although indicted, were not tried, as they have remained outside the United States.</p>
<p>[6]  The Government acknowledges that "[t]he weapons were found as a result of respondents' arrests and so are `fruit' of the discovery of the heroin. The convictions consequently must stand or fall with the heroin offenses." <i><span class="citation" data-id="339048"><a href="/opinion/339048/united-states-v-john-edward-emery/" aria-description="Citation for case: United States v. John Edward Emery">Id.,</a></span></i> at 5 n. 4.</p>
<p>[7]  Neither court below considered whether Ramsey or Kelly had standing to object to the opening of the envelopes in light of the fact that none of the envelopes were addressed to them. The Government, however, did not raise the issue below, and consequently we do not reach it. <i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U. S. 38</a></span>, 41 n. 2 (1976).</p>
<p>[8]  Postal regulations have implemented this authority. See <span class="citation no-link">19 CFR § 145.2</span> (1976); <span class="citation no-link">39 CFR § 61.1</span> (1975). The regulations were promulgated in 1971; prior to that time existing regulations did not implement the statutory authority. The fact that postal authorities did not open incoming international letter-class mail upon "reasonable cause to suspect" prior to 1971 does not change our analysis.
</p>
<p>Title <span class="citation no-link">39 U. S. C. § 3623</span> (d), which prohibits the opening of first-class mail of "domestic origin," "except under authority of a search warrant authorized by law . . . ," has, by its own terms, no application to international mail of any class. A proposed amendment, which would have imposed similar statutory requirements on the opening of international mail, was defeated on the floor of the House, 116 Cong. Rec. 20482-20483 (1970).</p>
<p>Our dissenting Brethren find no fewer than five separate reasons for refusing to follow the unambiguous language of the statutory section. The first is the longstanding respect Congress has shown for "the individual's interest in private communication." <i>Post,</i> at 626. But as we examine it, <i>infra,</i> at 616-619, no such support may be garnered from the history of the Fourth Amendment insofar as border searches are concerned. Insofar as they rely on the First Amendment, they ignore the limitations imposed on the search by the statute, <i>infra,</i> at 623-624, as well as by the regulations. Postulating a sensitive concern for First Amendment values as of 1866 is a difficult historical exercise on the basis of available materials from that time. Cf. <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727</a></span> (1878) (Fourth Amendment analysis only). Most puzzling of all, however, is the dissent's reliance on the defeated amendment, offered in 1970, when there is no dearth of available materials, which would have imposed a specific warrant requirement on the opening of international letter-class mail. Contrary to the tenor of the dissent, the amendment was defeated, not passed. The one bit of legislative history the dissent quotes, a statement of Congressman Derwinski, reflects only the concern that with the amendment " `the problem of stopping the flow of narcotics and pornography would be greatly compounded.' " <i>Post,</i> at 626 n. 2. We do not see how any solace whatever for the dissenting position may be derived from this sort of legislative history.</p>
<p>The dissent also relies on a brief colloquy on the floor of the Senate during the debate on the 1866 Act. The colloquy is notable both for its brevity and for its ambiguity. It does not distinguish between mailed packages and mailed letters; it refers generally to the " `examination of . . . the United States mails.' " <i>Post,</i> at 627. Yet, by that time, the "mail" encompassed both. See <span class="citation no-link">12 Stat. 704</span>. (To the extent the colloquy was meant to encompass <i>any</i> intrusion on the "mails," the statute has long since been interpreted otherwise. <i>Cotzhausen</i> v. <i>Nazro,</i> <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/#219" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215, 219</a></span> (1883).) Perhaps because of its brevity, the colloquy does not distinguish between domestic and international mail, nor does it distinguish between the searching of envelopes for contraband and the possible reading of enclosed communications. It explicitly manifests a concern with § 2 as well as with § 3 of the bill. But § 2 allowed customs inspectors "to go on board of any vessel . . . and to inspect, search, and examine the same, and any person, trunk, or envelope on board . . . ." Section 3, however, contains a "reasonable cause to suspect" requirement that is not found in § 2, and the colloquy may have simply referred to a concern about the wholesale opening, and reading, of letters. Cf. Cong. Globe 39th Cong., 1st Sess., 3440-3441 (1866). The colloquy by no means indicates to us that Congress was concerned only with detecting smuggling that would be carried in "trunk"-sized packages. It is at best insufficient to overcome the precise and clear statutory language Congress actually enacted.</p>
<p>The dissent additionally relies on the language of the statute in its entirety as demonstrating a concern only with "packages of the kind normally used to import dutiable merchandise." <i>Post,</i> at 628. But this assertionassuming we as judges know what size packages dutiable merchandise <i>usually</i> comes inis wholly contrary to the thrust of the purpose, and the language, of the Act. The purpose of the Act is "to Prevent Smuggling." Nowhere does this purpose, however and wherever articulated, reflect a concern with the physical size of the container employed in smuggling, nor do we possess any reliable indication that only large items were smuggled into this country in 1866. As for the word "envelope," it is difficult to see how our dissenting Brethren derive comfort from its use in the statute. The contemporary dictionary source they cite states that the most common use of the word "envelope" is in the sense of " `the cover or wrapper of a document, as of a letter.' " <i>Post,</i> at 630 n. 5. We are quite unable to see how this, the most common usage of the word, reinforces the view that Congress intended only a narrow definition when it used the word without restriction.</p>
<p>The dissent also relies on a "consistent construction" over 105 years by the Executive. <i>Post,</i> at 631. To the extent it relies on a construction that things entering by mail are not covered by the statute, this reliance founders on the opinion of a former Acting Attorney General. See 18 Op. Atty. Gen. 457 (1886). To the extent it is referring only to lettersized mail, the dissent nowhere demonstrates <i>any</i> actual interpretation by anyone that the congressional authority was perceived as an affirmative limitation on the power of the Executive to open letters at the border when there existed "reasonable cause" to suspect a violation of customs laws. The evidence marshaled by our dissenting Brethren on this point could be called "consistent" only by the most generous appraiser of such material.</p>
<p>The dissent's final reliance is on the assertion that asking the addressee for consent to open a letter had not been proved unworkable. Presumably the conclusion to be drawn from this is that the Executive's reason for a change in its policy is weak. But this is beside the point; it reflects not at all on Congress' words or intent in 1866 or at any other time. That the Executive Branch may have relied on a less-than-cogent reason in its 1971 regulatory change has nothing to do with the interpretation of an Act of Congress.</p>
<p>Underlying all of these reasons, apparently, is the fear that "[i]f the Government is allowed to exercise the power it claims, the door will be open to the wholesale, secret examination of all incoming international letter mail." <i>Post,</i> at 632. That specter is simply not presented by this case. As we observe, <i>infra,</i> at 623-624, the opening of mail is limited by a "reasonable cause" requirement, while the reading of letters is totally interdicted by regulation. It is this unwarranted speculation, and not the policy followed by the Executive, that poses the "serious constitutional question" to be avoided.</p>
<p>[9]  The Court of Appeals, it should be noted, evidently believed that Inspector Kallnischkies possessed sufficient information at the time the envelopes were opened to meet the stricter "probable cause" requirement; it believed "that the facts in this case are such that, had they been presented to a magistrate, issuance of a search warrant permitting opening of the envelopes would have been appropriate." 176 U. S. App. D. C. 67, 73 n. 8, <span class="citation" data-id="9462874"><a href="/opinion/337566/united-states-v-charles-w-ramsey-united-states-of-america-v-james-w/" aria-description="Citation for case: United States v. Charles W. Ramsey, United States of...">538 F. 2d 415</a></span>, 421 n. 8. Because of our disposition of this case, we do not reach that question.</p>
<p>[10]  In light of our conclusion that there existed "reasonable cause to suspect" a violation of the customs laws, we need not, and do not, decide whether the search would have nonetheless been authorized by other statutory grants of authority urged alternatively upon us by the Government. Title <span class="citation no-link">19 U. S. C. § 482</span> also authorizes customs officials to "stop, search, and examine . . . any vehicle, beast, or person, on which or whom . . . they shall suspect there is merchandise which is subject to duty, or shall have been introduced into the United States in any manner contrary to law, whether by the person in possession or charge, or by, in, or upon such vehicle or beast, or otherwise . . . ." Title <span class="citation no-link">19 U. S. C. § 1582</span> provides, in pertinent part, that "[t]he Secretary of the Treasury may prescribe regulations for the search of persons and baggage . . . ; and all persons coming into the United States from foreign countries shall be liable to detention and search by authorized officers or agents of the Government under such regulations."</p>
<p>[11]  Although the statutory authority authorizes searches of envelopes "wherever found," <span class="citation no-link">19 U. S. C. § 482</span>, the envelopes were searched at the New York City Post Office as the mail was entering the United States. We, therefore, do not have before us the question, recently addressed in other contexts, of the geographical limits to border searches. See <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973). Nor do we need to decide whether the broad statutory authority subjects such mail to customs inspection at a place other than the point of entry into this country. See <i>United States</i> v. <i>King,</i> <span class="citation" data-id="328030"><a href="/opinion/328030/united-states-v-edward-king-and-mose-franklin-pearson/#354" aria-description="Citation for case: United States v. Edward King and Mose Franklin Pearson">517 F. 2d, at 354</a></span> ("[T]he envelopes had passed an initial stage in the customs process when they were routed to Alabama, but they were still in the process of being delivered, and still subject to customs inspection").</p>
<p>[12]  Section 23 of this customs statute provided, in pertinent part:
</p>
<p>"[I]t shall be lawful for the collector, or other officer of the customs, after entry made of any goods, wares or merchandise, on suspicion of fraud, to open and examine, in the presence of two or more reputable merchants, any package or packages thereof . . . ."</p>
<p>Section 24 of this customs statute provided, in pertinent part:</p>
<p>"[E]very collector, naval officer and surveyor, or other person specially appointed by either of them for that purpose, shall have full power and authority, to enter any ship or vessel, in which they shall have reason to suspect any goods, wares or merchandise subject to duty shall be concealed; and therein to search for, seize, and secure any such goods, wares or merchandise; and if they shall have cause to suspect a concealment thereof, in any particular dwelling-house, store, building, or other place, they or either of them shall, upon application on oath or affirmation to any justice of the peace, be entitled to a warrant to enter such house, store, or other place (in the day time only) and there to search for such goods, and if any shall be found, to seize and secure the same for trial . . . ."</p>
<p>[13]  We do not decide whether, and under what circumstances, a border search might be deemed "unreasonable" because of the particularly offensive manner in which it is carried out. Cf. <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span> (1957); <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#356" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 356-358</a></span> (1931)</p>
<p>[14]  The opinion in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149</a></span> (1925), itself reminds us that "[t]he Fourth Amendment is to be construed in the light of what was deemed an unreasonable search and seizure when it was adopted, and in a manner which will conserve public interests as well as the interests and rights of individual citizens."</p>
<p>[15]  This explanation does not, and cannot, fully explain the border-search "exception" even if it were grounded in the "exigent circumstances" doctrine. For a letter may as easily be held by customs officials when it crosses with a traveler as it can when it crosses in the mail. Too, this explanation cannot explain the different treatment which the Court of Appeals apparently would have accorded mailed packages, which presumably may be detained as easily as letter-size envelopes.</p>
<p>[16]  There is no reason to infer that mailed letters somehow carry with them a greater expectation of privacy than do letters carried on one's person. Cf. <span class="citation no-link">39 U. S. C. § 3623</span> (d).</p>
<p>[17]  There are limited justifiable expectations of privacy for incoming material crossing United States borders. Not only is there the longstanding, constitutionally authorized right of customs officials to search incoming persons and goods, but there is no statutorily created expectation of privacy. See <span class="citation no-link">39 U. S. C. § 3623</span> (d). See also <i>United States</i> v. <i>King,</i> <span class="citation" data-id="328030"><a href="/opinion/328030/united-states-v-edward-king-and-mose-franklin-pearson/#354" aria-description="Citation for case: United States v. Edward King and Mose Franklin Pearson">517 F. 2d, at 354</a></span>; <i>United States</i> v. <i>Odland,</i> <span class="citation" data-id="321210"><a href="/opinion/321210/united-states-v-david-john-odland/" aria-description="Citation for case: United States v. David John Odland">502 F. 2d 148</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/1088/">419 U. S. 1088</a></span> (1974); <i>United States</i> v. <i>Doe,</i> <span class="citation" data-id="307979"><a href="/opinion/307979/united-states-v-john-doe-aka-francisco-rodriquez-aka-juan-velez-s/#985" aria-description="Citation for case: United States v. John Doe, A/K/A Francisco Rodriquez,...">472 F. 2d, at 985</a></span>.</p>
<p>[18]  We, accordingly, have no occasion to decide whether, in the absence of the regulatory restrictions, speech would be "chilled," or, if it were, whether the appropriate response would be to apply the full panoply of Fourth Amendment requirements. Cf. <i>Roaden</i> v. <i>Kentucky,</i> <span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#502" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496, 502-506</a></span> (1973); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span> (1968); <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485</a></span> (1965).</p>
<p>[19]  In <i>Wolff</i> v. <i>McDonnell,</i> <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539</a></span> (1974), this Court, in the context of the opening of mail from an attorney to a prisoner-client, noted that "freedom from censorship is not equivalent to freedom from inspection or perusal," <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#576" aria-description="Citation for case: Wolff v. McDonnell"><i>id.,</i> at 576</a></span>. This Court held:
</p>
<p>"As to the ability to open the mail in the presence of inmates, this could in no way constitute censorship, since the mail would not be read. Neither could it chill such communications, since the inmate's presence insures that prison officials will not read the mail. The possibility that contraband will be enclosed in letters, even those from apparent attorneys, surely warrants prison officials' opening the letters." <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#577" aria-description="Citation for case: Wolff v. McDonnell"><i>Id.,</i> at 577</a></span>.</p>
<p>We deal here, of course, with borders, not prisons. Yet the power of customs officials to take plenary action to stop the entry of contraband is no less in the border-search area than in prisons. The safeguards in the border-search area, we think, are comparable to those found constitutionally valid in <i><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">Wolff</a></span>.</i></p>
<p>[*]  As the Court notes, <i>ante,</i> at 623, postal regulations flatly prohibit the reading of "any correspondence contained in sealed letter mail of foreign origin unless a search warrant has been obtained . . . ." <span class="citation no-link">19 CFR § 145.3</span> (1976).</p>
<p>[1]  This was the procedure followed by the customs officials in <i>Cotzhausen</i> v. <i>Nazro,</i> <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215</a></span>, relied upon by the Government here. For 100 years, from 1871 to 1971, Post Office Regulations allowed incoming international letter mail to be opened only in the presence, and with the consent, of the addressee. Brief for United States 20-21, nn. 12a, 14 (citing regulations).</p>
<p>[2]  This conviction is bolstered by the history of the defeat of the amendment which would have imposed a specific warrant requirement on the opening of international mails, <i>ante,</i> at 612 n. 8. The amendment was offered during the course of House debate on the Postal Reorganization and Salary Adjustment Act of 1970, Title 39 U. S. C., which created the United States Postal Service. This amendment was but one of more than 35 amendments to the Act offered on the floor of the House that day. 116 Cong. Rec. 20481 (1970). Speaking immediately before the amendment was defeated, Congressman Derwinski said:
</p>
<p>"Going beyond the constitutional debate which we do not have the time for this afternoon, if this amendment were to be adopted, the problem of stopping the flow of narcotics and pornography would be greatly compounded.</p>
<p>"I do not believe we want to legislate on such a major issue with just 10 minutes of debate." <i>Id.,</i> at 20483.</p>
<p>Under such circumstances the defeat of this amendment cannot be considered an expression of the will of the House of Representatives on the issue, but it does emphasize the reluctance of Congress to legislate in the area without careful consideration of the constitutional questions. See, <i>e. g.,</i> <span class="citation no-link">18 U. S. C. § 2510</span> (Omnibus Crime Control and Safe Streets Act of 1968) (warrant required to electronically intercept wire or oral communications); S. Rep. No. 1097, 90th Cong., 2d Sess., 66-76, 88-108, 161-177, 182-183, 187, 214-218, 224-226, 234-239 (1968). I do not, of course, imply that this incident is, in itself, sufficient to demonstrate congressional sensitivity to the individual interest in private communication. See <i>ante,</i> at 612 n. 8. I cannot believe, however, that the Court seriously questions the validity of my assumption that Congress (in 1866 as well as today) was indeed concerned about such matters.</p>
<p>[3]  Cong. Globe, 39th Cong., 1st Sess., 2596 (1866). After consideration of one more amendment the bill passed the Senate the same day.</p>
<p>[4]  The first three sections of the Act, Further to Prevent Smuggling and for Other Purposes, enacted on July 18, 1866, read as follows:
</p>
<p>"<i>Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled,</i> That, for the purposes of this act, the term `vessel,' whenever hereinafter used, shall be held to include every description of water-craft, raft, vehicle, and contrivance used or capable of being used as a means or auxiliary of transportation on or by water; and the term `vehicle,' whenever hereinafter used, shall be held to include every description of carriage, wagon, engine, car, sleigh, sled, sledge, hurdle, cart, and other artificial contrivance, used or capable of being used as a means or auxiliary of transportation on land.</p>
<p>"SEC. 2. <i>And be it further enacted,</i> That it shall be lawful for any officer of the customs, including inspectors and occasional inspectors, or of a revenue cutter, or authorized agent of the Treasury Department, or other person specially appointed for the purpose in writing by a collector, naval officer, or surveyor of the customs, to go on board of any vessel, as well without as within his district, and to inspect, search, and examine the same, and any person, trunk, or envelope on board, and to this end, to hail and stop such vessel if under way, and to use all necessary force to compel compliance; and if it shall appear that any breach or violation of the laws of the United States has been committed, whereby or in consequence of which, such vessel, or the goods, wares, and merchandise, or any part thereof, on board of or imported by such vessel, is or are liable to forfeiture, to make seizure of the same, or either or any part thereof, and to arrest, or in case of escape, or any attempt to escape, to pursue and arrest any person engaged in such breach or violation: <i>Provided,</i> That the original appointment in writing of any person specially appointed as aforesaid shall be filed in the custom-house where such appointment is made.</p>
<p>"SEC. 3. <i>And be it further enacted,</i> That any of the officers or persons authorized by the second section of this act to board or search vessels may stop, search, and examine, as well without as within their respective districts, any vehicle, beast, or person on which or whom he or they shall suspect there are goods, wares, or merchandise which are subject to duty or shall have been introduced into the United States in any manner contrary to law, whether by the person in possession or charge, or by, in, or upon such vehicle or beast, or otherwise, and to search any trunk or envelope, wherever found, in which he may have a reasonable cause to suspect there are goods which were imported contrary to law; and if any such officer or other person so authorized as aforesaid shall find any goods, wares, or merchandise, on or about any such vehicle, beast, or person, or in any such trunk or envelope, which he shall have reasonable cause to believe are subject to duty, or to have been unlawfully introduced into the United States, whether by the person in possession or charge, or by, in, or upon such vehicle, beast, or otherwise, he shall seize and secure the same for trial; and every such vehicle and beast, or either, together with teams or other motive-power used in conveying, drawing, or propelling such vehicle, goods, wares, or merchandise, and all other appurtenances, including trunks, envelopes, covers, and all means of concealment, and all the equipage, trappings, and other appurtenances of such beast, team, or vehicle shall be subject to seizure and forfeiture; and if any person who may be driving or conducting, or in charge of any such carriage or vehicle or beast, or any person travelling, shall wilfully refuse to stop and allow search and examination to be made as herein provided, when required so to do by any authorized person, he or she shall, on conviction, be fined in any sum, in the discretion of the court convicting him or her, not exceeding one thousand dollars, nor less than fifty dollars; and the Secretary of the Treasury may from time to time prescribe regulations for the search of persons and baggage, and for the employment of female inspectors for the examination and search of persons of their own sex; and all persons coming into the United States from foreign countries shall be liable to detention and search by authorized officers or agents of the government, under such regulations as the Secretary of the Treasury shall from time to time prescribe: <i>Provided,</i> That no railway car or engine or other vehicle, or team used by any person or corporation, as common carriers in the transaction of their business as such common carriers shall be subject to forfeiture by force of the provisions of this act unless it shall appear that the owners, superintendent, or agent of the owner in charge thereof at the time of such unlawful importation or transportation thereon or thereby, was a consenting party, or privy to such illegal importation or transportation." <span class="citation no-link">14 Stat. 178</span>-179.</p>
<p>[5]  "A wrapper; an outward covering or case." J. Worcester, A Dictionary of the English Language (1860).
</p>
<p>"That which envelops, wraps up, encases, or surrounds; a wrapper; a cover; especially, the cover or wrapper of a document, as of a letter." N. Webster, An American Dictionary of the English Language (Goodrich &amp; Porter eds. 1869).</p>
<p>These are the primary definitions given for "envelope."</p>
<p>[6]  The word "other was deleted by amendment, Cong. Globe, 39th Cong., 1st Sess., 2564 (1866). I recognize that one may argue that the deletion of the word "other" is evidence of an intent to include every kind of envelope rather than just those comparable to a "trunk." It seems more reasonable to infer, however, that the draftsmen considered the direct comparison to a trunk too restrictive and merely had in mind all containers which performed the same kind of packaging function even though not as large as a trunk. It seems unrealistic to interpret this change as intended to broaden the statute to encompass personal mail.</p>
<p>[7]  The stated object of the 1866 Act was to prevent smuggling, especially from Canada along the North and Northwestern frontier:
</p>
<p>"It has been found very difficult on our frontier during the last two years to prevent the system of smuggling which has been going on and increasing day by day. The custom-houses are defrauded and the Government is cheated." Remarks of Congressman Eliot, Cong. Globe, 39th Cong., 1st Sess., 3419 (1866).</p>
<p>See also remarks of Senator Morrill, <span class="citation no-link"><i>id.,</i> at 2563</span>; of Senator Williams, <span class="citation no-link"><i>id.,</i> at 2567</span>.</p>
<p>[8]  An 1886 opinion of Acting Attorney General Jenks made reference to the practice followed in <i>Cotzhausen</i> v. <i>Nazro,</i> <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215</a></span>, a case which involved the opening of package mail with the consent, and in the presence, of the addressee. See 18 Op. Atty. Gen. 457, 458. No opinion of any subsequent Attorney General has construed the statute any more broadly.</p>
<p>[9]  In support of its argument in this Court that the 1971 regulations are reasonable within the meaning of the Fourth Amendment, the Government has assembled a plethora of statistical data obtained after the regulations were adopted. Such a <i>post hoc</i> justification cannot, of course, inform us about the actual motivation for the adoption of the regulations. I mention the point only because the Government's reliance on these data tends to confirm my judgment that if a new rule is to be fashioned, it should be drafted by the Congress.</p>

</div>
```

---
