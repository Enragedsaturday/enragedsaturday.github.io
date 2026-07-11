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

## GROUP: _overhaul2/lake/cases/Pennsylvania v. Mimms.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Pennsylvania v. Mimms"
type: case
citation: "434 U.S. 106 (1977)"
parallel_cite: "98 S. Ct. 330; 54 L. Ed. 2d 331"
neutral_cite: 1977 U.S. LEXIS 157
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-12-05
docket: 76-1830
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-12-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pennsylvania v. Mimms
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109751/pennsylvania-v-mimms/"
  cluster_id: 109751
  opinion_id: 9427002
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Anchor"
related: ["[[Maryland v. Wilson]]", "[[Terry v. Ohio]]", "[[Rodriguez v. United States]]", "[[Delaware v. Prouse]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stops", "officer-safety", "order-out-of-vehicle", "per-curiam"]
holding: "Once a vehicle is lawfully stopped for a traffic violation, an officer may order the driver out of the vehicle as a matter of course;…"
lake:
  record_id: Pennsylvania v. Mimms
  status: verified
  projected_at: 2026-07-06
---

# Pennsylvania v. Mimms

*434 U.S. 106 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Philadelphia officer stopped Mimms's car for an expired license plate to issue a summons. The officer asked Mimms to step out of the car; as Mimms got out, the officer noticed a large bulge under his jacket, frisked him, and found a loaded revolver. Mimms was convicted of carrying a concealed firearm.

## Issue
Whether, consistent with the Fourth Amendment, an officer may order a driver lawfully stopped for a traffic violation to get out of the vehicle as a matter of course.

## Rule
Yes. Ordering the driver out is at most a "*de minimis*" additional intrusion: "We think this additional intrusion can only be described as *de minimis*. . . . What is at most a mere inconvenience cannot prevail when balanced against legitimate concerns for the officer's safety." — 434 U.S. at 111. ^pin-111

"[O]nce a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out of the vehicle without violating the Fourth Amendment's proscription of unreasonable searches and seizures." — 434 U.S. at 111 n.6. ^pin-111a

## Application
Mimms was lawfully stopped for an expired plate, so the officer could order him out of the car as a matter of course. Once Mimms stepped out, the visible bulge under his jacket gave the officer reasonable suspicion that he was armed and dangerous, justifying the protective frisk that produced the revolver. Both the order to exit and the frisk were reasonable.

## Conclusion
An officer may routinely order a lawfully stopped driver out of the vehicle; the search and seizure were reasonable and the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Mimms*'s order-out rule was extended to passengers in [[Maryland v. Wilson]].

## Appears on
- [[Traffic Stops]] — *Key — Anchor*

## Sources
- *Pennsylvania v. Mimms*, 434 U.S. 106 (1977) (per curiam) — https://www.courtlistener.com/opinion/109751/pennsylvania-v-mimms/ — pinpoints: 111, 111 n.6.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8a4477e8238d66ab", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Pennsylvania v. Mimms"}, "payload": {"all": [{"cite": "434 U.S. 106", "page": "106", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "434"}, {"cite": "98 S. Ct. 330", "page": "330", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "54 L. Ed. 2d 331", "page": "331", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "54"}, {"cite": "1977 U.S. LEXIS 157", "page": "157", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "434 U.S. 106", "official": {"cite": "434 U.S. 106", "page": "106", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "434"}, "official_selection_present": true, "record_id": "Pennsylvania v. Mimms"}}
{"assertion_id": "202a861ad138e00a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-111", "record_id": "Pennsylvania v. Mimms"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-111", "pinpoint_status": "slip-only", "quote": "--- # Pennsylvania v. Mimms *434 U.S. 106 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Philadelphia officer stopped Mimms's car for an expired license plate to issue a summons. The officer asked Mimms to step out of the car; as Mimms got out, the officer noticed a large bulge under his jacket, frisked him, and found a loaded revolver. Mimms was convicted of carrying a concealed firearm. ## Issue Whether, consistent with the Fourth Amendment, an officer may order a driver lawfully stopped for a traffic violation to get out of the vehicle as a matter of course. ## Rule Yes. Ordering the driver out is at most a", "quote_fidelity": "mismatch", "record_id": "Pennsylvania v. Mimms", "star_marker": null}}
{"assertion_id": "845b707e94925509", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-111a", "record_id": "Pennsylvania v. Mimms"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-111a", "pinpoint_status": "slip-only", "quote": "[O]nce a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out of the vehicle without violating the Fourth Amendment's proscription of unreasonable searches and seizures.", "quote_fidelity": "mismatch", "record_id": "Pennsylvania v. Mimms", "star_marker": null}}
{"assertion_id": "d5a700aeaa9fd557", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Pennsylvania v. Mimms"}, "payload": {"as_of_content": "1977-12-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Pennsylvania v. Mimms", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Pennsylvania v. Mimms

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pennsylvania v. Mimms",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pennsylvania v. Mimms",
    "case_name_short": "Mimms",
    "case_name_full": "Pennsylvania v. Mimms",
    "input_case_name": "Pennsylvania v. Mimms",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-12-05",
    "year": 1977,
    "docket": "76-1830",
    "cluster_id": 109751,
    "lead_opinion_id": 9427002,
    "sibling_ids": [
      109751,
      9427002,
      9427003,
      9427004
    ],
    "absolute_url": "/opinion/109751/pennsylvania-v-mimms/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "434 U.S. 106",
      "volume": "434",
      "reporter": "U.S.",
      "page": "106",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 330",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "330",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 331",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "331",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 157",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "157",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "434 U.S. 106",
        "volume": "434",
        "reporter": "U.S.",
        "page": "106",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 330",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "330",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 331",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "331",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 157",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "157",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "434 U.S. 106",
    "official_selection": {
      "court_class": "scotus",
      "selected": "434 U.S. 106",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-111",
      "page": null,
      "quote": "--- # Pennsylvania v. Mimms *434 U.S. 106 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Philadelphia officer stopped Mimms's car for an expired license plate to issue a summons. The officer asked Mimms to step out of the car; as Mimms got out, the officer noticed a large bulge under his jacket, frisked him, and found a loaded revolver. Mimms was convicted of carrying a concealed firearm. ## Issue Whether, consistent with the Fourth Amendment, an officer may order a driver lawfully stopped for a traffic violation to get out of the vehicle as a matter of course. ## Rule Yes. Ordering the driver out is at most a",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-111a",
      "page": null,
      "quote": "[O]nce a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out of the vehicle without violating the Fourth Amendment's proscription of unreasonable searches and seizures.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-12-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pennsylvania v. Mimms",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4786330,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane1_negative"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rakas v. Illinois",
          "cluster_id": 109953,
          "cite": [
            "58 L. Ed. 2d 387",
            "99 S. Ct. 421",
            "439 U.S. 128",
            "1978 U.S. LEXIS 2452"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spencer v. Kemna",
          "cluster_id": 118176,
          "cite": [
            "140 L. Ed. 2d 43",
            "118 S. Ct. 978",
            "523 U.S. 1",
            "1998 U.S. LEXIS 1597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Texas",
          "cluster_id": 110128,
          "cite": [
            "61 L. Ed. 2d 357",
            "99 S. Ct. 2637",
            "443 U.S. 47",
            "1979 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. United States",
          "cluster_id": 2795278,
          "cite": [
            "575 U.S. 348",
            "135 S. Ct. 1609",
            "191 L. Ed. 2d 492",
            "2015 U.S. LEXIS 2807",
            "83 U.S.L.W. 4241",
            "25 Fla. L. Weekly Fed. S 191"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Summers",
          "cluster_id": 110534,
          "cite": [
            "69 L. Ed. 2d 340",
            "101 S. Ct. 2587",
            "452 U.S. 692",
            "1981 U.S. LEXIS 118",
            "49 U.S.L.W. 4776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio v. Robinette",
          "cluster_id": 118066,
          "cite": [
            "136 L. Ed. 2d 347",
            "117 S. Ct. 417",
            "519 U.S. 33",
            "1996 U.S. LEXIS 6971"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Hunt",
          "cluster_id": 110660,
          "cite": [
            "71 L. Ed. 2d 353",
            "102 S. Ct. 1181",
            "455 U.S. 478",
            "1982 U.S. LEXIS 77"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Wilson",
          "cluster_id": 118086,
          "cite": [
            "137 L. Ed. 2d 41",
            "117 S. Ct. 882",
            "519 U.S. 408",
            "1997 U.S. LEXIS 1271"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Mimms:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109751 OR 9427002 OR 9427003 OR 9427004) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQ5NDExMjAwMDAwJnM9NDU4Nzk5MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109751+OR+9427002+OR+9427003+OR+9427004%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(109751 OR 9427002 OR 9427003 OR 9427004)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MTUmcz0xMTkxOTQ3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109751+OR+9427002+OR+9427003+OR+9427004%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109751 OR 9427002 OR 9427003 OR 9427004)",
        "reviewed": 94,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 94,
        "triage_read": 0,
        "triage_snippet_classified": 94
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109751 OR 9427002 OR 9427003 OR 9427004)",
    "indexed_citing_opinions": 1974,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109751,
        "count": 1693,
        "count_source": "search"
      },
      {
        "opinion_id": 9427002,
        "count": 309,
        "count_source": "search"
      },
      {
        "opinion_id": 9427003,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427004,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3270,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pennsylvania-v-mimms.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyODU0OTMmcz0xMDU5NzQ0MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109751+OR+9427002+OR+9427003+OR+9427004%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109751,
        "cited_id": 103823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 107900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 1311789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 2131784,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109751,
        "cited_id": 2267362,
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
    "date_created": "2026-07-05T16:58:02Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:58:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:58:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:00:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:58:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pennsylvania v. Mimms

```
<opinion type="majority">
<author id="Aqq">Per Curiam.</author>
<p id="b278-11">Petitioner Commonwealth seeks review of a judgment of the Supreme Court of Pennsylvania reversing respondent’s conviction for carrying a concealed deadly weapon and a firearm without a license. That court reversed the conviction because it held that respondent’s “revolver was seized in a <page-number citation-index="1" label="107">*107</page-number>manner which violated the Fourth Amendment to the Constitution of the United States.” <span class="citation" data-id="9747563"><a href="/opinion/2267362/commonwealth-v-mimms/#548" aria-description="Citation for case: Commonwealth v. Mimms">471 Pa. 546, 548</a></span>, <span class="citation" data-id="9747563"><a href="/opinion/2267362/commonwealth-v-mimms/#1158" aria-description="Citation for case: Commonwealth v. Mimms">370 A. 2d 1157, 1158</a></span> (1977). Because we disagree with this conclusion, we grant the Commonwealth’s petition for certiorari and reverse the judgment of the Supreme Court of Pennsylvania.</p>
<p id="b279-5">The facts are not in dispute. While on routine patrol, two Philadelphia police officers observed respondent Harry Mimms driving an automobile with an expired license plate. The officers stopped the vehicle for the purpose of issuing a traffic summons. One of the officers approached and asked respondent to step out of the car and produce his owner’s card and operator’s license. Respondent alighted, whereupon the officer noticed a large bulge under respondent’s sports jacket. Fearing that the bulge might be a weapon, the officer frisked respondent and discovered in his waistband a .38-caliber revolver loaded with five rounds of ammunition. The other occupant of the car was carrying a .32-caliber revolver. Respondent was immediately arrested and subsequently indicted for carrying a concealed deadly weapon and for unlawfully carrying a firearm without a license. His motion to suppress the revolver was denied; and, after a trial at which the revolver was introduced into evidence, respondent was convicted on both counts.</p>
<p id="b279-6">As previously indicated, the Supreme Court of Pennsylvania reversed respondent’s conviction, however, holding that the revolver should have been suppressed because it was seized contrary to the guarantees contained in the Fourth and Fourteenth Amendments to the United States Constitution.<footnotemark>1</footnotemark> The Pennsylvania court did not doubt that the officers acted reasonably in stopping the car. It was also willing to assume, <em>arguendo, </em>that the limited search for weapons was proper once the officer observed the bulge under respondent’s coat. But the court nonetheless thought the search constitutionally in<page-number citation-index="1" label="108">*108</page-number>firm because the officer's order to respondent to get out of the car was an impermissible “seizure.” This was so because the officer could not point to “objective observable facts to support a suspicion that criminal activity was afoot or that the occupants of the vehicle posed a threat to police safety.” <footnotemark>2</footnotemark> Since this unconstitutional intrusion led directly to observance of the bulge and to the subsequent “pat down,” the revolver was the fruit of an unconstitutional search, and, in the view of the Supreme Court of Pennsylvania, should have been suppressed.</p>
<p id="b280-5">We do not agree with this conclusion.<footnotemark>3</footnotemark> The touchstone of <page-number citation-index="1" label="109">*109</page-number>our analysis under the Fourth Amendment is always “the reasonableness in all the circumstances of the particular governmental invasion of a citizen’s personal security.” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span> (1968). Reasonableness, of course, depends “on a balance between the public interest and the individual’s right to personal security free from arbitrary interference by law officers.” <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975).</p>
<p id="b281-5">In this case, unlike <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>there is no question about the propriety of the initial restrictions on respondent’s freedom of movement. Respondent was driving an automobile with expired license tags in violation of the Pennsylvania Motor Vehicle Code.<footnotemark>4</footnotemark> Deferring for a moment the legality of the “frisk” once the bulge had been observed, we need presently deal only with the narrow question of whether the order to get out of the car, issued after the driver was lawfully detained, was reasonable and thus permissible under the Fourth Amendment. This inquiry must therefore focus not on the intrusion resulting from the request to stop the vehicle or from the later “pat down,” but on the incremental intrusion resulting from the request to get out of the car once the vehicle was lawfully stopped.</p>
<p id="b281-6">Placing the question in this narrowed frame, we look first to that side of the balance which bears the officer’s interest in taking the action that he did. The State freely concedes the officer had no reason to suspect foul play from the particular driver at the time of the stop, there having been nothing unusual or suspicious about his behavior. It was apparently <page-number citation-index="1" label="110">*110</page-number>his practice to order all drivers out of their vehicles as a matter of course whenever they had been stopped for a traffic violation. The State argues that this practice was adopted as a precautionary measure to afford a degree of protection to the officer and that it may be justified on that ground. Establishing a face-to-face confrontation diminishes the possibility, otherwise substantial, that the driver can make unobserved movements; this, in turn, reduces the likelihood that the officer will be the victim of an assault.<footnotemark>5</footnotemark></p>
<p id="b282-5">We think it too plain for argument that the State’s proffered justification — the safety of the officer — is both legitimate and weighty. “Certainly it would be unreasonable to require that police officers take unnecessary risks in the performance of their duties.” <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#23" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 23</a></span>. And we have specifically recognized the inordinate risk confronting an officer as he approaches a person seated in an automobile. “According to one study, approximately 30% of police shootings occurred when a police officer approached a suspect seated in an automobile. Bristow, Police Officer Shootings — A Tactical Evaluation, 54 J. Crim. L. C. &amp; P. S. 93 (1963).” <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span>, 148 n. 3 (1972). We are aware that not all these assaults occur when issuing traffic summons, but we have before expressly declined to accept the argument that traffic violations necessarily involve less danger to officers than other types of confrontations. <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 234</a></span> (1973). Indeed, it appears “that a significant percentage of murders of police officers occurs when the officers are making traffic stops.” <em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Id.,</a></span> </em>at 234 n. 5.</p>
<p id="b283-4"><page-number citation-index="1" label="111">*111</page-number>The hazard of accidental injury from passing traffic to an officer standing on the driver’s side of the vehicle may also be appreciable in some situations. Rather than conversing while standing exposed to moving traffic, the officer prudently may prefer to ask the driver of the vehicle to step out of the car and off onto the shoulder of the road where the inquiry may be pursued with greater safety to both.</p>
<p id="b283-5">Against this important interest we are asked to weigh the intrusion into the driver’s personal liberty occasioned not by the initial stop of the vehicle, which was admittedly justified, but by the order to get out of the car. We think this additional intrusion can only be described as <em>de minimis. </em>The driver is being asked to expose to view very little more of his person than is already exposed. The police have already lawfully decided that the driver shall be briefly detained; the only question is whether he shall spend that period sitting in the driver’s seat of his car or standing alongside it. Not only is the insistence of the police on the latter choice not a “serious intrusion upon the sanctity of the person,” but it hardly rises to the level of a “ ‘petty indignity.’ ” <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#17" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 17</a></span>. What is at most a mere inconvenience cannot prevail when balanced against legitimate concerns for the officer’s safety.<footnotemark>6</footnotemark></p>
<p id="b283-6">There remains the second question of the propriety of the search once the bulge in the jacket was observed. We have as little doubt on this point as on the first; the answer is controlled by <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra.</a></span> </em>In that case we thought the officer justified in conducting a limited search for weapons <page-number citation-index="1" label="112">*112</page-number>once he had reasonably concluded that the person whom he had legitimately stopped might be armed and presently dangerous. Under the standard enunciated in that case— whether “the facts available to the officer at the moment of the seizure or the search ‘warrant a man of reasonable caution in the belief’ that the action taken was appropriate” <footnotemark>7</footnotemark> — there is little question the officer was justified. The bulge in the jacket permitted the officer to conclude that Mimms was armed and thus posed a serious and present danger to the safety of the officer. In these circumstances, any man of “reasonable caution” would likely have conducted the “pat down.”</p>
<p id="b284-5">Respondent’s motion to proceed <em>in forma pauperis </em>is granted. The petition for writ of certiorari is granted, the judgment of the Supreme Court of Pennsylvania is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b284-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b279-7"> Three judges dissented on the federal constitutional issue.</p>
</footnote>
<footnote label="2">
<p id="b280-6"> <span class="citation" data-id="9747563"><a href="/opinion/2267362/commonwealth-v-mimms/#552" aria-description="Citation for case: Commonwealth v. Mimms">471 Pa., at 552</a></span>, <span class="citation" data-id="9747563"><a href="/opinion/2267362/commonwealth-v-mimms/#1160" aria-description="Citation for case: Commonwealth v. Mimms">370 A. 2d, at 1160</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b280-7"> We note that in his brief in opposition to a grant of certiorari respondent contends that this case is moot because he has already completed the 3-year maximum of the 1%- to 3-year sentence imposed. The case has, he argues, terminated against him for all purposes and for all time regardless of this Court’s disposition of the matter. See <em>St. Pierre </em>v. <em>United States, </em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">319 U. S. 41</a></span> (1943).</p>
<p id="b280-8">But cases such as <em>Sibron </em>v. <em>New </em>York, <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#53" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 53-57</a></span> (1968); <em>Street </em>v. <em>New York, </em><span class="citation" data-id="9423995"><a href="/opinion/107900/street-v-new-york/" aria-description="Citation for case: Street v. New York">394 U. S. 576</a></span> (1969); <em>Carafas </em>v. <em>LaVallee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968); and <em>Ginsberg </em>v. <em>New York, </em><span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629</a></span> (1968), bear witness to the fact that this Court has long since departed from the rule announced in <em>St. <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">Pierre, supra.</a></span> </em>These more recent cases have held that the possibility of a criminal defendant’s suffering “collateral legal consequences” from a sentence already served permits him to have his claims reviewed here on the merits. If the prospect of the State’s visiting such collateral consequences on a criminal defendant who has served his sentence is a sufficient burden as to enable him to seek reversal of a decision affirming his conviction, the prospect of the State’s inability to impose such a burden following a reversal of the conviction of a criminal defendant in its own courts must likewise be sufficient to enable the State to obtain review of its claims on the merits here. In any future state criminal proceedings against respondent, this conviction may be relevant to setting bail and length of sentence, and to the availability of probation. 18 Pa. Cons. Stat. Ann. §§ 1321, 1322, 1331, 1332 (Purdon Supp. 1977); Pa. Rule Crim. Proc. 4004. In view of the fact that respondent, having fully served his state sentence, is presently incarcerated in the federal penitentiary at Lewisburg, Pa., we cannot say that such considerations are unduly specula<page-number citation-index="1" label="109">*109</page-number>tive even if a determination of mootness depended on a case-by-case analysis.</p>
</footnote>
<footnote label="4">
<p id="b281-9"> Operating an improperly licensed motor vehicle was at the time of the incident covered by 1959 Pa. Laws, No. 32, which was found in Pa. Stat. Ann., Tit. 75, §511 (a) (Purdon 1971), and has been repealed by 1976 Pa. Laws, No. 81, § 7, effective July 1, 1977. This offense now appears to be covered by 75 Pa. Cons. Stat. Ann. §§ 1301, 1302 (Purdon 1977).</p>
</footnote>
<footnote label="5">
<p id="b282-6"> The State does not, and need not, go so far as to suggest that an officer may frisk the occupants of any car stopped for a traffic violation. Rather, it only argues that it is permissible to order the driver out of the car. In this particular case, argues the State, once the driver alighted, the officer had independent reason to suspect criminal activity and present danger and it was upon this basis, and not the mere fact that respondent had committed a traffic violation, that he conducted the search.</p>
</footnote>
<footnote label="6">
<p id="b283-7"> Contrary to the suggestion in the dissent of our Brother Stevens, <em>post, </em>at 122, we do not hold today that “whenever an officer has an occasion to speak with the driver of a vehicle, he may also order the driver out of the car.” We hold only that once a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out of the vehicle without violating the Fourth Amendment’s proscription of unreasonable searches and seizures.</p>
</footnote>
<footnote label="7">
<p id="b284-10"> 392 U. S., at 21-22.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Pennsylvania v. Muniz.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Pennsylvania v. Muniz"
type: case
citation: "496 U.S. 582 (1990)"
parallel_cite: "110 S. Ct. 2638; 110 L. Ed. 2d 528"
neutral_cite: 1990 U.S. LEXIS 3211
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-06-18
docket: 89-213
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-06-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pennsylvania v. Muniz
  varies_by_point: false
  scope_note: "Good law (fractured opinion). The slurred manner of speech is non-testimonial; the 'sixth birthday' answer was testimonial and required suppression (custodial, unwarned); the routine biographical booking questions fall within a 'routine booking question' exception to Miranda."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112464/pennsylvania-v-muniz/"
  cluster_id: 112464
  opinion_id: 112464
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Rhode Island v. Innis]]", "[[Schmerber v. California]]", "[[Illinois v. Perkins]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "testimonial", "booking-exception", "dui", "self-incrimination"]
holding: "The slurred manner of a DUI suspect's speech is non-testimonial physical evidence admissible without Miranda; but a question whose answer's content reveals the suspect's impaired mental state (the 'sixth birthday' question) elicits a testimonial response that must be suppressed if unwarned; routine biographical booking questions fall within a 'routine booking question' exception to Miranda interrogation."
lake:
  record_id: Pennsylvania v. Muniz
  status: verified
  projected_at: 2026-07-09
---

# Pennsylvania v. Muniz

*496 U.S. 582 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Muniz was arrested for driving under the influence and taken to a booking center, where the proceedings were videotaped. Without [[Miranda and Custodial Interrogation|Miranda warnings]], an officer asked him seven biographical questions — name, address, height, weight, eye color, date of birth, and current age — during which he stumbled over his address and age. The officer then asked, "Do you know what the date was of your sixth birthday?" and Muniz answered that he did not. His slurred speech and confused answers were used as evidence of intoxication. The Pennsylvania Superior Court held that the sixth-birthday answer (and other statements) should have been suppressed for lack of [[Miranda and Custodial Interrogation|Miranda warnings]].

## Issue
Whether, for a custodial DUI suspect questioned without [[Miranda and Custodial Interrogation|Miranda warnings]], (1) the slurred manner of his speech, (2) his answer to the "sixth birthday" question, and (3) his answers to routine biographical booking questions were testimonial and required suppression.

## Rule
**Slurring is non-testimonial.** "[A]ny slurring of speech and other evidence of lack of muscular coordination revealed by Muniz's responses . . . constitute nontestimonial components of those responses. Requiring a suspect to reveal the physical manner in which he articulates words . . . does not, without more, compel him to provide a 'testimonial' response for purposes of the privilege." — 496 U.S. at 590–591. ^pin-591

**The "sixth birthday" answer is testimonial.** Its content forced the trilemma of truth, falsity, or silence: "the incriminating inference of impaired mental faculties stemmed, not just from the fact that Muniz slurred his response, but also from a testimonial aspect of that response." — [*Id.* at 599](https://www.courtlistener.com/opinion/112464/pennsylvania-v-muniz/#:~:text=your-,sixth%20birthday). "[B]ecause we conclude that Muniz's response to the sixth birthday question was testimonial, the response should have been suppressed." — *Id.* at 600. ^pin-599

**Routine booking questions are exempt.** Muniz's "answers to th[e] first seven questions are . . . admissible because the questions fall within a 'routine booking question' exception which exempts from *Miranda*'s coverage questions to secure the 'biographical data necessary to complete booking or pretrial services.'" — *Id.* at 601. ^pin-601

## Application
The Commonwealth could use the slurred, uncoordinated manner of Muniz's speech as physical evidence of intoxication without [[Miranda and Custodial Interrogation|Miranda warnings]]. But the answer to the sixth-birthday question was different: its very content (that he could not supply the date) let the factfinder infer a confused mental state, so it was a testimonial communication that, taken in custody without warnings, had to be suppressed. The seven preceding biographical questions, though they produced incriminating fumbling, were asked to record routine booking data and so fell within the booking-question exception and were admissible.

## Conclusion
The slurring evidence and the biographical booking answers were admissible; the testimonial sixth-birthday answer should have been suppressed. The judgment of the Pennsylvania Superior Court was affirmed in part and reversed in part, and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (fractured opinion; the controlling holdings are stated above).
- No negative treatment. *Muniz* applies the testimonial/physical-evidence distinction of [[Schmerber v. California]] to custodial DUI questioning, defines interrogation through [[Rhode Island v. Innis]], and recognizes the routine-booking-question exception within the [[Miranda v. Arizona]] framework (decided the same Term as the [[Illinois v. Perkins]] undercover-questioning exception).

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Pennsylvania v. Muniz*, 496 U.S. 582 (1990) — https://www.courtlistener.com/opinion/112464/pennsylvania-v-muniz/ — pinpoints: 590–591, 599, 600, 601.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b65a4f05bb808232", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Pennsylvania v. Muniz"}, "payload": {"all": [{"cite": "496 U.S. 582", "page": "582", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "496"}, {"cite": "110 S. Ct. 2638", "page": "2638", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "110 L. Ed. 2d 528", "page": "528", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "1990 U.S. LEXIS 3211", "page": "3211", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}], "display": "496 U.S. 582", "official": {"cite": "496 U.S. 582", "page": "582", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "496"}, "official_selection_present": true, "record_id": "Pennsylvania v. Muniz"}}
{"assertion_id": "0cac75cfaa7a1d5f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-591", "record_id": "Pennsylvania v. Muniz"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-591", "pinpoint_status": "slip-only", "quote": "question, and (3) his answers to routine biographical booking questions were testimonial and required suppression. ## Rule **Slurring is non-testimonial.**", "quote_fidelity": "mismatch", "record_id": "Pennsylvania v. Muniz", "star_marker": null}}
{"assertion_id": "3c836ef05672b0d4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-599", "record_id": "Pennsylvania v. Muniz"}, "payload": {"fragment": "#:~:text=your-,sixth%20birthday", "page": null, "pin_id": "pin-599", "pinpoint_status": "star-verified", "quote": "sixth birthday", "quote_fidelity": "matched", "record_id": "Pennsylvania v. Muniz", "star_marker": "586"}}
{"assertion_id": "71cce4ebdeddd3ea", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-601", "record_id": "Pennsylvania v. Muniz"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-601", "pinpoint_status": "slip-only", "quote": "answers to th[e] first seven questions are . . . admissible because the questions fall within a 'routine booking question' exception which exempts from *Miranda*'s coverage questions to secure the 'biographical data necessary to complete booking or pretrial services.'", "quote_fidelity": "mismatch", "record_id": "Pennsylvania v. Muniz", "star_marker": null}}
{"assertion_id": "a6de14652b24b58f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Pennsylvania v. Muniz"}, "payload": {"as_of_content": "1990-06-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Pennsylvania v. Muniz", "scope_note": "Good law (fractured opinion). The slurred manner of speech is non-testimonial; the 'sixth birthday' answer was testimonial and required suppression (custodial, unwarned); the routine biographical booking questions fall within a 'routine booking question' exception to Miranda.", "varies_by_point": false}}
```

### lake record — Pennsylvania v. Muniz

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pennsylvania v. Muniz",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pennsylvania v. Muniz",
    "case_name_short": "Muniz",
    "case_name_full": "Pennsylvania v. Muniz",
    "input_case_name": "Pennsylvania v. Muniz",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-06-18",
    "year": 1990,
    "docket": "89-213",
    "cluster_id": 112464,
    "lead_opinion_id": 112464,
    "sibling_ids": [
      112464,
      9432075,
      9432076,
      9432077
    ],
    "absolute_url": "/opinion/112464/pennsylvania-v-muniz/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9093487,
        "score": 20,
        "case_name": "Pennsylvania v. Muniz"
      },
      {
        "cluster_id": 9093486,
        "score": 20,
        "case_name": "Pennsylvania v. Muniz"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "496 U.S. 582",
      "volume": "496",
      "reporter": "U.S.",
      "page": "582",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 2638",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2638",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 528",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "528",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 3211",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3211",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "496 U.S. 582",
        "volume": "496",
        "reporter": "U.S.",
        "page": "582",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 2638",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2638",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 528",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "528",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 3211",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3211",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "496 U.S. 582",
    "official_selection": {
      "court_class": "scotus",
      "selected": "496 U.S. 582",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-591",
      "page": null,
      "quote": "question, and (3) his answers to routine biographical booking questions were testimonial and required suppression. ## Rule **Slurring is non-testimonial.**",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-599",
      "page": null,
      "quote": "sixth birthday",
      "star_marker": "586",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 3073,
      "fragment": "#:~:text=your-,sixth%20birthday",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-601",
      "page": null,
      "quote": "answers to th[e] first seven questions are . . . admissible because the questions fall within a 'routine booking question' exception which exempts from *Miranda*'s coverage questions to secure the 'biographical data necessary to complete booking or pretrial services.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-06-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pennsylvania v. Muniz",
    "varies_by_point": false,
    "scope_note": "Good law (fractured opinion). The slurred manner of speech is non-testimonial; the 'sixth birthday' answer was testimonial and required suppression (custodial, unwarned); the routine biographical booking questions fall within a 'routine booking question' exception to Miranda.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Janvier",
          "cluster_id": 9494606,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Toler v. United States",
          "cluster_id": 4575476,
          "cite": [
            "198 A.3d 767"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kirby. v. State",
          "cluster_id": 10366681,
          "cite": [
            "304 Ga. 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Brigido Zapien",
          "cluster_id": 4405817,
          "cite": [
            "861 F.3d 971",
            "2017 WL 2836162",
            "2017 U.S. App. LEXIS 11809"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alfonzo Williams",
          "cluster_id": 4327223,
          "cite": [
            "842 F.3d 1143",
            "2016 U.S. App. LEXIS 21621",
            "2016 WL 7046754"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Boyd",
          "cluster_id": 4259208,
          "cite": [
            "360 Or. 302",
            "380 P.3d 941",
            "2016 Ore. LEXIS 612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tisa Farrow",
          "cluster_id": 3184707,
          "cite": [
            "2016 VT 30",
            "201 Vt. 437",
            "144 A.3d 1036",
            "2016 Vt. LEXIS 33",
            "2016 WL 932894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
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
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
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
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Zaitar",
          "cluster_id": 2662455,
          "cite": [
            "858 F. Supp. 2d 103",
            "2012 WL 1570865",
            "2012 U.S. Dist. LEXIS 63313"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "McNeil v. Wisconsin",
          "cluster_id": 112622,
          "cite": [
            "115 L. Ed. 2d 158",
            "111 S. Ct. 2204",
            "501 U.S. 171",
            "1991 U.S. LEXIS 3483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 2355344,
          "cite": [
            "41 S.W.3d 75",
            "2001 Tenn. LEXIS 222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Labron",
          "cluster_id": 118063,
          "cite": [
            "135 L. Ed. 2d 1031",
            "116 S. Ct. 2485",
            "518 U.S. 938",
            "1996 U.S. LEXIS 4268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Briggs",
          "cluster_id": 2550075,
          "cite": [
            "12 A.3d 291",
            "608 Pa. 430",
            "2011 Pa. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evans v. State",
          "cluster_id": 1707183,
          "cite": [
            "725 So. 2d 613",
            "1997 WL 562044"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 6897940,
          "cite": [
            "119 Ohio St. 3d 118",
            "892 N.E.2d 864"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1407706,
          "cite": [
            "14 Cal. 4th 1005",
            "929 P.2d 544",
            "97 Daily Journal DAR 899",
            "97 Cal. Daily Op. Serv. 520",
            "60 Cal. Rptr. 2d 225",
            "1997 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Morales",
          "cluster_id": 2629809,
          "cite": [
            "18 P.3d 11",
            "104 Cal. Rptr. 2d 582",
            "25 Cal. 4th 34",
            "2001 Daily Journal DAR 2253",
            "2001 Cal. Daily Op. Serv. 1805",
            "2001 Cal. LEXIS 1163"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hubbell",
          "cluster_id": 1087666,
          "cite": [
            "147 L. Ed. 2d 24",
            "120 S. Ct. 2037",
            "530 U.S. 27",
            "2000 U.S. LEXIS 3768"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pirtle v. Morgan",
          "cluster_id": 7109731,
          "cite": [
            "313 F.3d 1160",
            "2002 WL 31840626"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Golphin",
          "cluster_id": 1274200,
          "cite": [
            "533 S.E.2d 168",
            "352 N.C. 364",
            "2000 N.C. LEXIS 618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Augustine D'anjou, A/K/A Dennis Dennison",
          "cluster_id": 663096,
          "cite": [
            "16 F.3d 604",
            "40 Fed. R. Serv. 515",
            "1994 U.S. App. LEXIS 2622",
            "1994 WL 46727"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas v. Texas",
          "cluster_id": 903977,
          "cite": [
            "186 L. Ed. 2d 376",
            "133 S. Ct. 2174",
            "2013 U.S. LEXIS 4697",
            "570 U.S. 178",
            "81 U.S.L.W. 4467",
            "24 Fla. L. Weekly Fed. S 294",
            "2013 WL 2922119"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Powell",
          "cluster_id": 1736,
          "cite": [
            "175 L. Ed. 2d 1009",
            "130 S. Ct. 1195",
            "559 U.S. 50",
            "2010 U.S. LEXIS 1898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Rivera, Elena Vila",
          "cluster_id": 568540,
          "cite": [
            "944 F.2d 1563",
            "1991 U.S. App. LEXIS 24889",
            "1991 WL 197347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas v. Goord",
          "cluster_id": 8439101,
          "cite": [
            "430 F.3d 652",
            "2005 WL 3150611"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Pagan",
          "cluster_id": 2334891,
          "cite": [
            "950 A.2d 270",
            "597 Pa. 69",
            "2008 Pa. LEXIS 918"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Beshore",
          "cluster_id": 1979564,
          "cite": [
            "916 A.2d 1128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Balsys",
          "cluster_id": 118242,
          "cite": [
            "141 L. Ed. 2d 575",
            "118 S. Ct. 2218",
            "524 U.S. 666",
            "1998 U.S. LEXIS 4210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. JAVIER M.",
          "cluster_id": 2516018,
          "cite": [
            "33 P.3d 1",
            "131 N.M. 1",
            "2001 NMSC 030"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bormann",
          "cluster_id": 2234021,
          "cite": [
            "777 N.W.2d 829",
            "279 Neb. 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffith v. State",
          "cluster_id": 2335950,
          "cite": [
            "55 S.W.3d 598",
            "2001 Tex. Crim. App. LEXIS 70",
            "2001 WL 1090773"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramon Velarde-Gomez",
          "cluster_id": 775389,
          "cite": [
            "269 F.3d 1023",
            "2001 Daily Journal DAR 11297",
            "2001 Cal. Daily Op. Serv. 9050",
            "2001 U.S. App. LEXIS 22714",
            "2001 WL 1262610"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112464 OR 9432075 OR 9432076 OR 9432077) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjUyOTcyODAwMDAwJnM9MjQzMjc3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112464+OR+9432075+OR+9432076+OR+9432077%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(112464 OR 9432075 OR 9432076 OR 9432077)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTImcz03ODAyMTYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112464+OR+9432075+OR+9432076+OR+9432077%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112464 OR 9432075 OR 9432076 OR 9432077)",
        "reviewed": 30,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 30,
        "triage_read": 2,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112464 OR 9432075 OR 9432076 OR 9432077)",
    "indexed_citing_opinions": 634,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112464,
        "count": 520,
        "count_source": "search"
      },
      {
        "opinion_id": 9432075,
        "count": 123,
        "count_source": "search"
      },
      {
        "opinion_id": 9432076,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432077,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 976,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pennsylvania-v-muniz.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4MzU2NiZzPTk1MTYyMDAmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28112464+OR+9432075+OR+9432076+OR+9432077%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112464,
        "cited_id": 97290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 105528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 108710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 109292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 111878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 112120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 112123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 112152,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 375540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 403655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 424921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 424960,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 521998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1533585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1702883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1782123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1931990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1996025,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 2102837,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 2259488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 2592211,
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
    "date_created": "2026-07-05T17:00:21Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:00:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:00:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:05:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:00:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pennsylvania v. Muniz

```
<div>
<center><b><span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/" aria-description="Citation for case: Pennsylvania v. Muniz">496 U.S. 582</a></span> (1990)</b></center>
<center><h1>PENNSYLVANIA<br>
v.<br>
MUNIZ</h1></center>
<center>No. 89-213.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 27, 1990</center>
<center>Decided June 18, 1990</center>
CERTIORARI TO THE SUPERIOR COURT OF PENNSYLVANIA
<p><span class="star-pagination">*584</span> <i>J. Michael Eakin</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Richard F. Maffett, Jr.,</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p>JUSTICE BRENNAN delivered the opinion of the Court, except as to Part III-C.</p>
<p>We must decide in this case whether various incriminating utterances of a drunken-driving suspect, made while performing a series of sobriety tests, constitute testimonial responses to custodial interrogation for purposes of the Self-Incrimination Clause of the Fifth Amendment.</p>
<p></p>
<h2>
<span class="star-pagination">*585</span> I</h2>
<p>During the early morning hours of November 30, 1986, a patrol officer spotted respondent Inocencio Muniz and a passenger parked in a car on the shoulder of a highway. When the officer inquired whether Muniz needed assistance, Muniz replied that he had stopped the car so he could urinate. The officer smelled alcohol on Muniz's breath and observed that Muniz's eyes were glazed and bloodshot and his face was flushed. The officer then directed Muniz to remain parked until his condition improved, and Muniz gave assurances that he would do so. But as the officer returned to his vehicle, Muniz drove off. After the officer pursued Muniz down the highway and pulled him over, the officer asked Muniz to perform three standard field sobriety tests: a "horizontal gaze nystagmus" test, a "walk and turn" test, and a "one leg stand" test.<sup>[1]</sup> Muniz performed these tests poorly, and he informed the officer that he had failed the tests because he had been drinking.</p>
<p>The patrol officer arrested Muniz and transported him to the West Shore facility of the Cumberland Country Central Booking Center. Following its routine practice for receiving persons suspected of driving while intoxicated, the booking center videotaped the ensuing proceedings. Muniz was informed that his actions and voice were being recorded, but he <span class="star-pagination">*586</span> was not at this time (nor had he been previously) advised of his rights under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Officer Hosterman first asked Muniz his name, address, height, weight, eye color, date of birth, and current age. He responded to each of these questions, stumbling over his address and age. The officer then asked Muniz, "Do you know what the date was of your sixth birthday?" After Muniz offered an inaudible reply, the officer repeated, "When you turned six years old, do you remember what the date was?" Muniz responded, "No, I don't."</p>
<p>Officer Hosterman next requested Muniz to perform each of the three sobriety tests that Muniz had been asked to perform earlier during the initial roadside stop. The videotape reveals that his eyes jerked noticeably during the gaze test, that he did not walk a very straight line, and that he could not balance himself on one leg for more than several seconds. During the latter two tests, he did not complete the requested verbal counts from 1 to 9 and from 1 to 30. Moreover, while performing these tests, Muniz "attempted to explain his difficulties in performing the various tasks, and often requested further clarification of the tasks he was to perform." <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#390" aria-description="Citation for case: Commonwealth v. Muniz">377 Pa. Super. 382, 390</a></span>, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d 419, 423</a></span> (1988).</p>
<p>Finally, Officer Deyo asked Muniz to submit to a breathalyzer test designed to measure the alcohol content of his expelled breath. Officer Deyo read to Muniz the Common-wealth's Implied Consent Law, <span class="citation no-link">75 Pa. Cons. Stat. § 1547</span> (1987), and explained that under the law his refusal to take the test would result in automatic suspension of his driver's license for one year. Muniz asked a number of questions about the law, commenting in the process about his state of inebriation. Muniz ultimately refused to take the breath test. At this point, Muniz was for the first time advised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Muniz then signed a statement waiving his rights and admitted in response to further questioning that he had been driving while intoxicated.</p>
<p><span class="star-pagination">*587</span> Both the video and audio portions of the videotape were admitted into evidence at Muniz's bench trial,<sup>[2]</sup> along with the arresting officer's testimony that Muniz failed the roadside sobriety tests and made incriminating remarks at that time. Muniz was convicted of driving under the influence of alcohol in violation of <span class="citation no-link">75 Pa. Cons. Stat. § 3731</span>(a)(1) (1987). Muniz filed a motion for a new trial, contending that the court should have excluded the testimony relating to the field sobriety tests and the videotape taken at the booking center "because they were incriminating and completed prior to [Muniz's] receiving his Miranda warnings." App. to Pet. for Cert. C-5  C-6. The trial court denied the motion, holding that " `requesting a driver, suspected of driving under the influence of alcohol, to perform physical tests or take a breath analysis does not violate [his] privilege against self-incrimination because [the] evidence procured is of a physical nature rather than testimonial, and therefore no Miranda warnings are required.' " <i><span class="citation no-link">Id.,</span></i> at C-6, quoting <i>Commonwealth</i> v. <i>Benson,</i> <span class="citation" data-id="2259488"><a href="/opinion/2259488/commonwealth-v-benson/#29" aria-description="Citation for case: Commonwealth v. Benson">280 Pa. Super. 20, 29</a></span>, <span class="citation" data-id="2259488"><a href="/opinion/2259488/commonwealth-v-benson/#387" aria-description="Citation for case: Commonwealth v. Benson">421 A. 2d 383, 387</a></span> (1980).</p>
<p>On appeal, the Superior Court of Pennsylvania reversed. The appellate court agreed that when Muniz was asked "to submit to a field sobriety test, and later perform these tests before the videotape camera, no <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were required" because such sobriety tests elicit physical, rather than testimonial, evidence within the meaning of the Fifth Amendment. 377 Pa. Super., at 387, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#422" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 422</a></span>. The court concluded, however, that "when the physical nature of the tests begins to yield testimonial and communicative statements . . . the protections afforded by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are invoked." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> The court explained that Muniz's answer to the question regarding his sixth birthday and the statements and inquiries he made while performing the physical <span class="star-pagination">*588</span> dexterity tests and discussing the breathalyzer test "are precisely the sort of testimonial evidence that we expressly protected in [previous cases]," <i>id.,</i> at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>, because they " `reveal[ed] his thought processes.' " <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#389" aria-description="Citation for case: Commonwealth v. Muniz"><i>Id.,</i> at 389</a></span>, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>. The court further explained: "[N]one of Muniz's utterances were spontaneous, voluntary verbalizations. Rather, they were clearly compelled by the questions and instructions presented to him during his detention at the Booking Center. Since the . . . responses and communications were elicited before Muniz received his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, they should have been excluded as evidence." <i>Id.,</i> at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>.<sup>[3]</sup> Concluding that the audio portion of the videotape should have been suppressed in its entirety, the court reversed Muniz's conviction and remanded the case for a new trial.<sup>[4]</sup> After the Pennsylvania Supreme Court denied the Commonwealth's application for review, <span class="citation no-link">522 Pa. 575</span>, <span class="citation no-link">559 A. 2d 36</span> (1989), we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./493/916/">493 U. S. 916</a></span> (1989).</p>
<p></p>
<h2>II</h2>
<p>The Self-Incrimination Clause of the Fifth Amendment<sup>[5]</sup> provides that no "person . . . shall be compelled in any criminal case to be a witness against himself." Although the text does not delineate the ways in which a person might be made <span class="star-pagination">*589</span> a "witness against himself," cf. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 761-762, n. 6</a></span> (1966), we have long held that the privilege does not protect a suspect from being compelled by the State to produce "real or physical evidence." <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California"><i>Id.,</i> at 764</a></span>. Rather, the privilege "protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature." <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California"><i>Id.,</i> at 761</a></span>. "[I]n order to be testimonial, an accused's communication must itself, explicitly or implicitly, relate a factual assertion or disclose information. Only then is a person compelled to be a `witness' against himself." <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States">487 U. S. 201, 210</a></span> (1988).</p>
<p>In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), we reaffirmed our previous understanding that the privilege against self-incrimination protects individuals not only from legal compulsion to testify in a criminal courtroom but also from "informal compulsion exerted by law-enforcement officers during in-custody questioning." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 461</a></span>. Of course, voluntary statements offered to police officers "remain a proper element in law enforcement." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 478</a></span>. But "without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 467</a></span>. Accordingly, we held that protection of the privilege against self-incrimination during pretrial questioning requires application of special "procedural safeguards." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 444</a></span>. "Prior to any questioning, the person must be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> Unless a suspect "voluntarily, knowingly and intelligently" waives these rights, <i>ibid.,</i> any incriminating responses to questioning may not be introduced into evidence in the prosecution's case in chief in a subsequent criminal proceeding.</p>
<p><span class="star-pagination">*590</span> This case implicates both the "testimonial" and "compulsion" components of the privilege against self-incrimination in the context of pretrial questioning. Because Muniz was not advised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights until after the videotaped proceedings at the booking center were completed, any verbal statements that were both testimonial in nature and elicited during custodial interrogation should have been suppressed. We focus first on Muniz's responses to the initial informational questions, then on his questions and utterances while performing the physical dexterity and balancing tests, and finally on his questions and utterances surrounding the breathalyzer test.</p>
<p></p>
<h2>III</h2>
<p>In the initial phase of the recorded proceedings, Officer Hosterman asked Muniz his name, address, height, weight, eye color, date of birth, current age, and the date of his sixth birthday. Both the delivery and content of Muniz's answers were incriminating. As the state court found, "Muniz's videotaped responses . . . certainly led the finder of fact to infer that his confusion and failure to speak clearly indicated a state of drunkenness that prohibited him from safely operating his vehicle." 377 Pa. Super., at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>. The Commonwealth argues, however, that admission of Muniz's answers to these questions does not contravene Fifth Amendment principles because Muniz's statement regarding his sixth birthday was not "testimonial" and his answers to the prior questions were not elicited by custodial interrogation. We consider these arguments in turn.</p>
<p></p>
<h2>A</h2>
<p>We agree with the Commonwealth's contention that Muniz's answers are not rendered inadmissible by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> merely because the slurred nature of his speech was incriminating. The physical inability to articulate words in a clear manner due to "the lack of muscular coordination of his tongue and mouth," Brief for Petitioner 16, is not itself a testimonial <span class="star-pagination">*591</span> component of Muniz's responses to Officer Hosterman's introductory questions. In <i>Schmerber</i> v. <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">California, supra</a></span></i><i>,</i> we drew a distinction between "testimonial" and "real or physical evidence" for purposes of the privilege against self-incrimination. We noted that in <i>Holt</i> v. <i>United States,</i> <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#252" aria-description="Citation for case: Holt v. United States">218 U. S. 245, 252-253</a></span> (1910), Justice Holmes had written for the Court that " `[t]he prohibition of compelling a man in a criminal court to be witness against himself is a prohibition of the use of physical or moral compulsion to extort communications from him, not an exclusion of his body as evidence when it may be material.' " 384 U. S., at 763. We also acknowledged that "both federal and state courts have usually held that it offers no protection against compulsion to submit to fingerprinting, photographing, or measurements, to write or speak for identification, to appear in court, to stand, to assume a stance, to walk, or to make a particular gesture." <i>Id.,</i> at 764. Embracing this view of the privilege's contours, we held that "the privilege is a bar against compelling `communications' or `testimony,' but that compulsion which makes a suspect or accused the source of `real or physical evidence' does not violate it." <i>Ibid.</i> Using this "helpful framework for analysis," <i>ibid.,</i> we held that a person suspected of driving while intoxicated could be forced to provide a blood sample, because that sample was "real or physical evidence" outside the scope of the privilege and the sample was obtained in a manner by which "[p]etitioner's testimonial capacities were in no way implicated." <i>Id.,</i> at 765.</p>
<p>We have since applied the distinction between "real or physical" and "testimonial" evidence in other contexts where the evidence could be produced only through some volitional act on the part of the suspect. In <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), we held that a suspect could be compelled to participate in a lineup and to repeat a phrase provided by the police so that witnesses could view him and listen to his voice. We explained that requiring his presence and speech at a lineup reflected "compulsion of the accused to <span class="star-pagination">*592</span> exhibit his physical characteristics, not compulsion to disclose any knowledge he might have." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 222</a></span>; see <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade"><i>id.,</i> at 222-223</a></span> (suspect was "required to use his voice as an identifying physical characteristic"). In <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), we held that a suspect could be compelled to provide a handwriting exemplar, explaining that such an exemplar, "in contrast to the content of what is written, like the voice or body itself, is an identifying physical characteristic outside [the privilege's] protection." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 266-267</a></span>. And in <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1</a></span> (1973), we held that suspects could be compelled to read a transcript in order to provide a voice exemplar, explaining that the "voice recordings were to be used solely to measure the physical properties of the witnesses' voices, not for the testimonial or communicative content of what was to be said." <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#7" aria-description="Citation for case: United States v. Dionisio"><i>Id.,</i> at 7</a></span>.</p>
<p>Under <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> and its progeny, we agree with the Commonwealth that any slurring of speech and other evidence of lack of muscular coordination revealed by Muniz's responses to Officer Hosterman's direct questions constitute nontestimonial components of those responses. Requiring a suspect to reveal the physical manner in which he articulates words, like requiring him to reveal the physical properties of the sound produced by his voice, see <i><span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">Dionisio, supra,</a></span></i> does not, without more, compel him to provide a "testimonial" response for purposes of the privilege.</p>
<p></p>
<h2>B</h2>
<p>This does not end our inquiry, for Muniz's answer to the sixth birthday question was incriminating, not just because of his delivery, but also because of his answer's <i>content;</i> the trier of fact could infer from Muniz's answer (that he did not <i>know</i> the proper date) that his mental state was confused.<sup>[6]</sup><span class="star-pagination">*593</span> The Commonwealth and the United States as <i>amicus curiae</i> argue that this incriminating inference does not trigger the protections of the Fifth Amendment privilege because the inference concerns "the physiological functioning of [Muniz's] brain," Brief for Petitioner 21, which is asserted to be every bit as "real or physical" as the physiological makeup of his blood and the timbre of his voice.</p>
<p>But this characterization addresses the wrong question; that the "fact" to be inferred might be said to concern the physical status of Muniz's brain merely describes the way in which the inference is incriminating. The correct question for present purposes is whether the incriminating inference of mental confusion is drawn from a testimonial act or from physical evidence. In <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>,</i> for example, we held that the police could compel a suspect to provide a blood sample in order to determine the physical makeup of his blood and thereby draw an inference about whether he was intoxicated. This compulsion was outside of the Fifth Amendment's protection, not simply because the evidence concerned the suspect's physical body, but rather because the evidence was <i>obtained</i> in a manner that did not entail any testimonial act on the part of the suspect: "Not even a shadow of testimonial compulsion upon or enforced communication by the accused was involved either in the extraction or in the chemical analysis." 384 U. S., at 765. In contrast, had the police instead asked the suspect directly whether his blood contained a high concentration of alcohol, his affirmative response would have been testimonial even though it would have been used to draw the same inference concerning his physiology. See <i>ibid.</i> ("[T]he blood test evidence . . . was neither [the suspect's] testimony nor evidence relating to some communicative act"). In this case, the question is not whether a suspect's "impaired mental faculties" can fairly be characterized as an aspect of his physiology, but rather whether Muniz's response <span class="star-pagination">*594</span> to the sixth birthday question that gave rise to the inference of such an impairment was testimonial in nature.<sup>[7]</sup></p>
<p>We recently explained in <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">487 U. S. 201</a></span> (1988), that "in order to be testimonial, an accused's communication must itself, explicitly or implicitly, relate a factual assertion or disclose information." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States"><i>Id.,</i> at 210</a></span>. We reached this conclusion after addressing our reasoning in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber, supra,</a></span></i> and its progeny:</p>
<blockquote>"The Court accordingly held that the privilege was not implicated in [the line of cases beginning with <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i>], because the suspect was not required `to disclose any knowledge he might have,' or `to speak his guilt.' <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade">388 U. S., at 222-223</a></span>. See <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#7" aria-description="Citation for case: United States v. Dionisio">410 U. S., at 7</a></span>; <i>Gilbert,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S., at 266-267</a></span>. It is the `extortion of information from the accused,' <i>Couch</i> v. <i>United States,</i> 409 U. S., at 328, the attempt to force him `to disclose the contents of his own mind,' <i>Curcio</i> v. <i>United States,</i> <span class="citation" data-id="105528"><a href="/opinion/105528/curcio-v-united-states/#128" aria-description="Citation for case: Curcio v. United States">354 U. S. 118, 128</a></span> (1957), that implicates the Self-Incrimination Clause. . . . `Unless some attempt is made to secure a communication  written, oral or otherwise  upon which reliance is to be placed as involving [the accused's] consciousness of the facts and the operations of his mind in expressing it, the demand made upon <span class="star-pagination">*595</span> him is not a testimonial one.' 8 Wigmore § 2265, p. 386." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States">487 U. S., at 210-211</a></span>.</blockquote>
<p>After canvassing the purposes of the privilege recognized in prior cases,<sup>[8]</sup> we concluded that "[t]hese policies are served when the privilege is asserted to spare the accused from having to reveal, directly or indirectly, his knowledge of facts relating him to the offense or from having to share his thoughts and beliefs with the Government."<sup>[9]</sup><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#213" aria-description="Citation for case: Doe v. United States"><i>Id.,</i> at 213</a></span>.</p>
<p>This definition of testimonial evidence reflects an awareness of the historical abuses against which the privilege against self-incrimination was aimed. "Historically, the privilege was intended to prevent the use of legal compulsion to extract from the accused a sworn communication of facts which would incriminate him. Such was the process of the <span class="star-pagination">*596</span> ecclesiastical courts and the Star Chamber  the inquisitorial method of putting the accused upon his oath and compelling him to answer questions designed to uncover uncharged offenses, without evidence from another source. The major thrust of the policies undergirding the privilege is to prevent such compulsion." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#212" aria-description="Citation for case: Doe v. United States"><i>Id.,</i> at 212</a></span> (citations omitted); see also <i>Andresen</i> v. <i>Maryland,</i> <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#470" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463, 470-471</a></span> (1976). At its core, the privilege reflects our fierce " `unwillingness to subject those suspected of crime to the cruel trilemma of self-accusation, perjury or contempt,' " <i>Doe,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#212" aria-description="Citation for case: Doe v. United States">487 U. S., at 212</a></span> (citation omitted), that defined the operation of the Star Chamber, wherein suspects were forced to choose between revealing incriminating private thoughts and forsaking their oath by committing perjury. See <i>United States</i> v. <i>Nobles,</i> <span class="citation" data-id="9426145"><a href="/opinion/109292/united-states-v-nobles/#233" aria-description="Citation for case: United States v. Nobles">422 U. S. 225, 233</a></span> (1975) ("The Fifth Amendment privilege against compulsory self-incrimination . . . protects `a private inner sanctum of individual feeling and thought and proscribes state intrusion to extract self-condemnation' ") (quoting <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#327" aria-description="Citation for case: Couch v. United States">409 U. S. 322, 327</a></span> (1973)).</p>
<p>We need not explore the outer boundaries of what is "testimonial" today, for our decision flows from the concept's core meaning. Because the privilege was designed primarily to prevent "a recurrence of the Inquisition and the Star Chamber, even if not in their stark brutality," <i>Ullmann</i> v. <i>United States,</i> <span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#428" aria-description="Citation for case: Ullmann v. United States">350 U. S. 422, 428</a></span> (1956), it is evident that a suspect is "compelled . . . to be a witness against himself" at least whenever he must face the modern-day analog of the historic trilemma  either during a criminal trial where a sworn witness faces the identical three choices, or during custodial interrogation where, as we explained in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the choices are analogous and hence raise similar concerns.<sup>[10]</sup> Whatever <span class="star-pagination">*597</span> else it may include, therefore, the definition of "testimonial" evidence articulated in <i><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">Doe</a></span></i> must encompass all responses to questions that, if asked of a sworn suspect during a criminal trial, could place the suspect in the "cruel trilemma." This conclusion is consistent with our recognition in <i><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">Doe</a></span></i> that "[t]he vast majority of verbal statements thus will be testimonial" because "[t]here are very few instances in which a verbal statement, either oral or written, will not convey information or assert facts." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#213" aria-description="Citation for case: Doe v. United States">487 U. S., at 213</a></span>. Whenever a suspect is asked for a response requiring him to communicate an express or implied assertion of fact or belief,<sup>[11]</sup> the suspect confronts the "trilemma" of truth, falsity, or silence, and hence the response (whether based on truth or falsity) contains a testimonial component.</p>
<p>This approach accords with each of our post-<span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California"><i>Schmerber</i></a></span> cases finding that a particular oral or written response to express or implied questioning was nontestimonial; the questions presented in these cases did not confront the suspects with this trilemma. As we noted in <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States"><i>Doe, supra,</i> at 210-211</a></span>, the cases upholding compelled writing and voice exemplars did not involve situations in which suspects were asked to communicate any personal beliefs or knowledge of facts, and therefore the suspects were not forced to choose between <span class="star-pagination">*598</span> truthfully or falsely revealing their thoughts. We carefully noted in <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), for example, that a "mere handwriting exemplar, <i>in contrast to the content of what is written,</i> like the voice or body itself, is an identifying physical characteristic outside [the privilege's] protection." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 266-267</a></span> (emphasis added). Had the suspect been asked to provide a writing sample of his own composition, the content of the writing would have reflected his assertion of facts or beliefs and hence would have been testimonial; but in <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> "[n]o claim [was] made that the content of the exemplars was testimonial or communicative matter." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#267" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 267</a></span>.<sup>[12]</sup> And in <i><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">Doe</a></span>,</i> the suspect was asked merely to sign a consent form waiving a privacy interest in foreign bank records. Because the consent form spoke in the hypothetical and did not identify any particular banks, accounts, or private records, the form neither "communicate[d] any factual assertions, implicit or explicit, [n]or convey[ed] any information to the Government." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#215" aria-description="Citation for case: Doe v. United States">487 U. S., at 215</a></span>. We concluded, therefore, that compelled execution of the consent directive did not "forc[e] [the suspect] to express the contents of his mind," <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States"><i>id.,</i> at 210, n. 9</a></span>, but rather forced the suspect only to make a "nonfactual statement." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#213" aria-description="Citation for case: Doe v. United States"><i>Id.,</i> at 213, n. 11</a></span>.</p>
<p>In contrast, the sixth birthday question in this case required a testimonial response. When Officer Hosterman <span class="star-pagination">*599</span> asked Muniz if he knew the date of his sixth birthday and Muniz, for whatever reason, could not remember or calculate that date, he was confronted with the trilemma. By hypothesis, the inherently coercive environment created by the custodial interrogation precluded the option of remaining silent, see n. 10, <i>supra.</i> Muniz was left with the choice of incriminating himself by admitting that he did not then know the date of his sixth birthday, or answering untruthfully by reporting a date that he did not then believe to be accurate (an incorrect guess would be incriminating as well as untruthful). The content of his truthful answer supported an inference that his mental faculties were impaired, because his assertion (he did not know the date of his sixth birthday) was different from the assertion (he knew the date was (correct date)) that the trier of fact might reasonably have expected a lucid person to provide. Hence, the incriminating inference of impaired mental faculties stemmed, not just from the fact that Muniz slurred his response, but also from a testimonial aspect of that response.<sup>[13]</sup></p>
<p><span class="star-pagination">*600</span> The state court held that the sixth birthday question constituted an unwarned interrogation for purposes of the privilege against self-incrimination, 377 Pa. Super., at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>, and that Muniz's answer was incriminating. <i><span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/" aria-description="Citation for case: Commonwealth v. Muniz">Ibid.</a></span></i> The Commonwealth does not question either conclusion. Therefore, because we conclude that Muniz's response to the sixth birthday question was testimonial, the response should have been suppressed.</p>
<p></p>
<h2>C</h2>
<p>The Commonwealth argues that the seven questions asked by Officer Hosterman just <i>prior</i> to the sixth birthday question  regarding Muniz's name, address, height, weight, eye color, date of birth, and current age  did not constitute custodial interrogation as we have defined the term in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and subsequent cases. In <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court referred to "interrogation" as actual "questioning initiated by law enforcement officers." 384 U. S., at 444. We have since clarified that definition, finding that the "goals of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> safeguards could be effectuated if those safeguards extended not only to express questioning, but also to "its functional equivalent.' " <i>Arizona</i> v. <i>Mauro,</i> <span class="citation" data-id="9430952"><a href="/opinion/111878/arizona-v-mauro/#526" aria-description="Citation for case: Arizona v. Mauro">481 U. S. 520, 526</a></span> (1987). In <i>Rhode Island</i> v. <i>Innis,</i> <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980), the Court defined the phrase "functional equivalent" of express questioning to include "any words or actions on the part of the police (other than those normally attendant to arrest and custody) <span class="star-pagination">*601</span> that the police should know are reasonably likely to elicit an incriminating response from the suspect. The latter portion of this definition focuses primarily upon the perceptions of the suspect, rather than the intent of the police." <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><i>Id.,</i> at 301</a></span> (footnotes omitted); see also <i>Illinois</i> v. <i>Perkins, ante,</i> at 296. However, "[a]ny knowledge the police may have had concerning the unusual susceptibility of a defendant to a particular form of persuasion might be an important factor in determining" what the police reasonably should have known. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#302" aria-description="Citation for case: Rhode Island v. Innis"><i>Innis, supra,</i> at 302, n. 8</a></span>. Thus, custodial interrogation for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> includes both express questioning and words or actions that, given the officer's knowledge of any special susceptibilities of the suspect, the officer knows or reasonably should know are likely to "have . . . the force of a question on the accused," <i>Harryman</i> v. <i>Estelle,</i> <span class="citation" data-id="9466546"><a href="/opinion/375540/burley-clifton-harryman-v-w-j-estelle-jr-director-texas-department/#874" aria-description="Citation for case: Burley Clifton Harryman v. W. J. Estelle, Jr., Director,...">616 F. 2d 870, 874</a></span> (CA5 1980), and therefore be reasonably likely to elicit an incriminating response.</p>
<p>We disagree with the Commonwealth's contention that Officer Hosterman's first seven questions regarding Muniz's name, address, height, weight, eye color, date of birth, and current age do not qualify as custodial interrogation as we defined the term in <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis, supra,</a></span></i> merely because the questions were not intended to elicit information for investigatory purposes. As explained above, the <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span></i> test focuses primarily upon "the perspective of the suspect." <i>Perkins, ante,</i> at 296. We agree with <i>amicus</i> United States, however, that Muniz's answers to these first seven questions are nonetheless admissible because the questions fall within a "routine booking question" exception which exempts from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s coverage questions to secure the " `biographical data necessary to complete booking or pretrial services.' " Brief for United States as <i>Amicus Curiae</i> 12, quoting <i>United States</i> v. <i>Horton,</i> <span class="citation" data-id="521998"><a href="/opinion/521998/united-states-v-derrick-deon-horton-aka-thomas-deon-hill-united-states/#181" aria-description="Citation for case: United States v. Derrick Deon Horton, A/K/A Thomas Deon...">873 F. 2d 180, 181, n. 2</a></span> (CA8 1989). The state court found that the first seven questions were "requested for record-keeping purposes only," App. B16, and therefore the questions appear reasonably related to the police's administrative <span class="star-pagination">*602</span> concerns.<sup>[14]</sup> In this context, therefore, the first seven questions asked at the booking center fall outside the protections of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and the answers thereto need not be suppressed.</p>
<p></p>
<h2>IV</h2>
<p>During the second phase of the videotaped proceedings, Officer Hosterman asked Muniz to perform the same three sobriety tests that he had earlier performed at roadside prior to his arrest: the "horizontal gaze nystagmus" test, the "walk and turn" test, and the "one leg stand" test. While Muniz was attempting to comprehend Officer Hosterman's instructions and then perform the requested sobriety tests, Muniz made several audible and incriminating statements.<sup>[15]</sup> Muniz argued to the state court that both the videotaped performance of the physical tests themselves and the audiorecorded verbal statements were introduced in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p>The court refused to suppress the videotaped evidence of Muniz's paltry performance on the physical sobriety tests, reasoning that " `[r]equiring a driver to perform physical [sobriety] tests . . . does not violate the privilege against self-incrimination because the evidence procured is of a physical nature rather than testimonial.' " 377 Pa. Super., at 387, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 422</a></span> (quoting <i>Commonwealth</i> v. <i><span class="citation" data-id="2259488"><a href="/opinion/2259488/commonwealth-v-benson/" aria-description="Citation for case: Commonwealth v. Benson">Benson</a></span>,</i> 280 Pa. <span class="star-pagination">*603</span> Super., at 29, <span class="citation" data-id="2259488"><a href="/opinion/2259488/commonwealth-v-benson/#387" aria-description="Citation for case: Commonwealth v. Benson">421 A. 2d, at 387</a></span>).<sup>[16]</sup> With respect to Muniz's verbal statements, however, the court concluded that "none of Muniz's utterances were spontaneous, voluntary verbalizations," 377 Pa. Super., at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>, and because they were "elicited before Muniz received his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, they should have been excluded as evidence." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i></p>
<p>We disagree. Officer Hosterman's dialogue with Muniz concerning the physical sobriety tests consisted primarily of carefully scripted instructions as to how the tests were to be performed. These instructions were not likely to be perceived as calling for any verbal response and therefore were not "words or actions" constituting custodial interrogation, with two narrow exceptions not relevant here.<sup>[17]</sup> The dialogue also contained limited and carefully worded inquiries as to whether Muniz understood those instructions, but these focused inquiries were necessarily "attendant to" the police <span class="star-pagination">*604</span> procedure held by the court to be legitimate. Hence, Muniz's incriminating utterances during this phase of the videotaped proceedings were "voluntary" in the sense that they were not elicited in response to custodial interrogation.<sup>[18]</sup> See <i>South Dakota</i> v. <i>Neville,</i> <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#564" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 564, n. 15</a></span> (1983) (drawing analogy to "police request to submit to fingerprinting or photography" and holding that police inquiry whether suspect would submit to blood-alcohol test was not "interrogation within the meaning of <i>Miranda</i>").</p>
<p>Similarly, we conclude that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> does not require suppression of the statements Muniz made when asked to submit to a breathalyzer examination. Officer Deyo read Muniz a prepared script explaining how the test worked, the nature of Pennsylvania's Implied Consent Law, and the legal consequences that would ensue should he refuse. Officer Deyo then asked Muniz whether he understood the nature of the test and the law and whether he would like to submit to the test. Muniz asked Officer Deyo several questions concerning the legal consequences of refusal, which Deyo answered directly, and Muniz then commented upon his state of inebriation. 377 Pa. Super., at 387, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#422" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 422</a></span>. After offering to take the test only after waiting a couple of hours or drinking some water, Muniz ultimately refused.<sup>[19]</sup></p>
<p><span class="star-pagination">*605</span> We believe that Muniz's statements were not prompted by an interrogation within the meaning of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> and therefore the absence of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings does not require suppression of these statements at trial.<sup>[20]</sup> As did Officer Hosterman when administering the three physical sobriety tests, see <i>supra,</i> at 603-604, Officer Deyo carefully limited her role to providing Muniz with relevant information about the breathalyzer test and the Implied Consent Law. She questioned Muniz only as to whether he understood her instructions and wished to submit to the test. These limited and focused inquiries were necessarily "attendant to" the legitimate police procedure, see <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#564" aria-description="Citation for case: South Dakota v. Neville"><i>Neville, supra,</i> at 564, n. 15</a></span>, and were not likely to be perceived as calling for any incriminating response.<sup>[21]</sup></p>
<p></p>
<h2>V</h2>
<p>We agree with the state court's conclusion that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires suppression of Muniz's response to the question regarding the date of his sixth birthday, but we do not agree that the entire audio portion of the videotape must be suppressed.<sup>[22]</sup> Accordingly, the court's judgment reversing <span class="star-pagination">*606A</span> Muniz's conviction is vacated, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p><span class="star-pagination">*606B</span> CHIEF JUSTICE REHNQUIST, with whom JUSTICE WHITE, JUSTICE BLACKMUN, and JUSTICE STEVENS join, concurring in part, concurring in the result in part, and dissenting in part.</p>
<p>I join Parts I, II, III-A, and IV of the Court's opinion. In addition, although I agree with the conclusion in Part III-C that the seven "booking" questions should not be suppressed, I do so for a reason different from that of JUSTICE BRENNAN. I dissent from the Court's conclusion that Muniz's response to the "sixth birthday question" should have been suppressed.</p>
<p>The Court holds that the sixth birthday question Muniz was asked required a testimonial response, and that its admission at trial therefore violated Muniz's privilege against compulsory self-incrimination. The Court says:</p>
<blockquote>"When Officer Hosterman asked Muniz if he knew the date of his sixth birthday and Muniz, for whatever reason, could not remember or calculate that date, he was confronted with the trilemma [<i>i.e.,</i> the `"trilemma" of truth, falsity, or silence,' see <i>ante,</i> at 597]. . . . Muniz was left with the choice of incriminating himself by admitting that he did not then know the date of his sixth birthday, or answering untruthfully by reporting a date that he did not then believe to be accurate (an incorrect guess would be incriminating as well as untruthful)." <i>Ante,</i> at 598-599.</blockquote>
<p>As an assumption about human behavior, this statement is wrong. Muniz would no more have felt compelled to fabricate a false date than one who cannot read the letters on an eye chart feels compelled to fabricate false letters; nor does a wrong guess call into question a speaker's veracity. The Court's statement is also a flawed predicate on which to base its conclusion that Muniz's answer to this question was "testimonial" for purposes of the Fifth Amendment.</p>
<p><span class="star-pagination">*607</span> The need for the use of the human voice does not automatically make an answer testimonial, <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 222-223</a></span> (1967), any more than does the fact that a question calls for the exhibition of one's handwriting in written characters. <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 266-267</a></span> (1967). In <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), we held that the extraction and chemical analysis of a blood sample involved no "shadow of testimonial compulsion upon or enforced communication by the accused." <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California"><i>Id.,</i> at 765</a></span>. All of these holdings were based on Justice Holmes' opinion in <i>Holt</i> v. <i>United States,</i> <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">218 U. S. 245</a></span> (1910), where he said for the Court that "the prohibition of compelling a man in a criminal court to be witness against himself is a prohibition of the use of physical or moral compulsion to extort communications from him, not an exclusion of his body as evidence when it may be material." <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#252" aria-description="Citation for case: Holt v. United States"><i>Id.,</i> at 252-253</a></span>.</p>
<p>The sixth birthday question here was an effort on the part of the police to check how well Muniz was able to do a simple mathematical exercise. Indeed, had the question related only to the date of his birth, it presumably would have come under the "booking exception" to <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), to which the Court refers elsewhere in its opinion. The Court holds in this very case that Muniz may be required to perform a "horizontal gaze nystagmus" test, the "walk and turn" test, and the "one leg stand" test, all of which are designed to test a suspect's physical coordination. If the police may require Muniz to use his body in order to demonstrate the level of his physical coordination, there is no reason why they should not be able to require him to speak or write in order to determine his mental coordination. That was all that was sought here. Since it was permissible for the police to extract and examine a sample of Schmerber's blood to determine how much that part of his system had been affected by alcohol, I see no reason why they may not examine the functioning of Muniz's mental processes for the same purpose.</p>
<p><span class="star-pagination">*608</span> Surely if it were relevant, a suspect might be asked to take an eye examination in the course of which he might have to admit that he could not read the letters on the third line of the chart. At worst, he might utter a mistaken guess. Muniz likewise might have attempted to guess the correct response to the sixth birthday question instead of attempting to calculate the date or answer "I don't know." But the potential for giving a bad guess does not subject the suspect to the truth-falsity-silence predicament that renders a response testimonial and, therefore, within the scope of the Fifth Amendment privilege.</p>
<p>For substantially the same reasons, Muniz's responses to the videotaped "booking" questions were not testimonial and do not warrant application of the privilege. Thus, it is unnecessary to determine whether the questions fall within the "routine booking question" exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> JUSTICE BRENNAN recognizes.</p>
<p>I would reverse in its entirety the judgment of the Superior Court of Pennsylvania. But given the fact that five members of the Court agree that Muniz's response to the sixth birthday question should have been suppressed, I agree that the judgment of the Superior Court should be vacated so that, on remand, the court may consider whether admission of the response at trial was harmless error.</p>
<p>JUSTICE MARSHALL, concurring in part and dissenting in part.</p>
<p>I concur in Part III-B of the Court's opinion that the "sixth birthday question" required a testimonial response from respondent Muniz. For the reasons discussed below, see n. 1, <i>infra,</i> that question constituted custodial interrogation. Because the police did not apprise Muniz of his rights under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), before asking the question, his response should have been suppressed.</p>
<p>I disagree, however, with JUSTICE BRENNAN's recognition in Part III-C of a "routine booking question" exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> Moreover, even were such an exception warranted, <span class="star-pagination">*609</span> it should not extend to booking questions that the police should know are reasonably likely to elicit incriminating responses. Because the police in this case should have known that the seven booking questions were reasonably likely to elicit incriminating responses and because those questions were not preceded by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, Muniz's testimonial responses should have been suppressed.</p>
<p>I dissent from the Court's holding in Part IV that Muniz's testimonial statements in connection with the three sobriety tests and the breathalyzer test were not the products of custodial interrogation. The police should have known that the circumstances in which they confronted Muniz, combined with the detailed instructions and questions concerning the tests and the Commonwealth's Implied Consent Law, were reasonably likely to elicit an incriminating response, and therefore constituted the "functional equivalent" of express questioning. <i>Rhode Island</i> v. <i>Innis,</i> <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 301</a></span> (1980). Muniz's statements to the police in connection with these tests thus should have been suppressed because he was not first given the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.</p>
<p>Finally, the officer's directions to Muniz to count aloud during two of the sobriety tests sought testimonial responses, and Muniz's responses were incriminating. Because Muniz was not informed of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights prior to the tests, those responses also should have been suppressed.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>JUSTICE BRENNAN would create yet another exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>:</i> the "routine booking question" exception. See also <i>Illinois</i> v. <i>Perkins, ante,</i> p. 292 (creating exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> for custodial interrogation by an undercover police officer posing as the suspect's fellow prison inmate). Such exceptions undermine <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s fundamental principle that the doctrine should be clear so that it can be easily applied by both police and courts. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#441" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 441-442</a></span>; <span class="star-pagination">*610</span> <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 718</a></span> (1979); <i>Perkins, ante,</i> at 308-309 (MARSHALL, J., dissenting). JUSTICE BRENNAN's position, were it adopted by a majority of the Court, would necessitate difficult, time-consuming litigation over whether particular questions asked during booking are "routine," whether they are necessary to secure biographical information, whether that information is itself necessary for recordkeeping purposes, and whether the questions are  despite their routine nature  designed to elicit incriminating testimony. The far better course would be to maintain the clarity of the doctrine by requiring police to preface all direct questioning of a suspect with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings if they want his responses to be admissible at trial.</p>
<p></p>
<h2>B</h2>
<p>JUSTICE BRENNAN nonetheless asserts that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> does not apply to express questioning designed to secure " ` "biographical data necessary to complete booking or pretrial services," ' " <i>ante,</i> at 601 (citation omitted), so long as the questioning is not " `designed to elicit incriminatory admissions,' " <i>ante,</i> at 602, n. 14 (quoting Brief for United States as <i>Amicus Curiae</i> 13; citing <i>United States</i> v. <i>Avery,</i> <span class="citation" data-id="424921"><a href="/opinion/424921/united-states-v-ozzie-lee-avery-jr/#1024" aria-description="Citation for case: United States v. Ozzie Lee Avery, Jr.">717 F. 2d 1020, 1024-1025</a></span> (CA6 1983) (acknowledging that "[e]ven a relatively innocuous series of questions may, in light of the factual circumstances and the susceptibility of a particular suspect, be reasonably likely to elicit an incriminating response"); <i>United States</i> v. <i>Mata-Abundiz,</i> <span class="citation" data-id="424960"><a href="/opinion/424960/united-states-v-jesus-mata-abundiz/#1280" aria-description="Citation for case: United States v. Jesus Mata-Abundiz">717 F. 2d 1277, 1280</a></span> (CA9 1983) (holding that routine booking question exception does not apply if "the questions are reasonably likely to elicit an incriminating response in a particular situation"); <i>United States</i> v. <i>Glen-Archila,</i> <span class="citation" data-id="403655"><a href="/opinion/403655/united-states-v-homero-glen-archila-dudley-astor-may-mitchell/#816" aria-description="Citation for case: United States v. Homero Glen-Archila, Dudley Astor...">677 F. 2d 809, 816, n. 18</a></span> (CA11 1982) ("Even questions that usually are routine must be proceeded <i>[sic]</i> by <i>Miranda</i> warnings if they are intended to produce answers that are incriminating")). Even if a routine booking question exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> were warranted, that exception should not extend to any booking question <span class="star-pagination">*611</span> that the police should know is reasonably likely to elicit an incriminating response, cf. <i>Innis,</i> <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301</a></span>, regardless of whether the question is "designed" to elicit an incriminating response. Although the police's intent to obtain an incriminating response is relevant to this inquiry, the key components of the analysis are the nature of the questioning, the attendant circumstances, and the perceptions of the suspect. Cf. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><i>id.,</i> at 301, n. 7</a></span>. Accordingly, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are required before the police may engage in any questioning reasonably likely to elicit an incriminating response.</p>
<p>Here, the police should have known that the seven booking questions  regarding Muniz's name, address, height, weight, eye color, date of birth, and age  were reasonably likely to elicit incriminating responses from a suspect whom the police believed to be intoxicated. Cf. <i>id.,</i> at 302, n. 8 ("Any knowledge the police may have had concerning the unusual susceptibility of a defendant to a particular form of persuasion might be an important factor in determining whether the police should have known that their words or actions were reasonably likely to elicit an incriminating response from the suspect"). Indeed, as the Court acknowledges, Muniz did in fact "stumbl[e] over his address and age," <i>ante,</i> at 586; more specifically, he was unable to give his address without looking at his license and initially told police the wrong age. Moreover, the very fact that, after a suspect has been arrested for driving under the influence, the Pennsylvania police regularly videotape the subsequent questioning strongly implies a purpose to the interrogation other than "recordkeeping." The seven questions in this case, then, do not fall within the routine booking question exception even under JUSTICE BRENNAN's standard.<sup>[1]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*612</span> C</h2>
<p>Although JUSTICE BRENNAN does not address this issue, the booking questions sought "testimonial" responses for the same reason the sixth birthday question did: because the content of the answers would indicate Muniz's state of mind. <i>Ante,</i> at 598-599, and n. 12. See also <i>Estelle</i> v. <i>Smith,</i> <span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#464" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454, 464-465</a></span> (1981). The booking questions, like the sixth birthday question, required Muniz to (1) answer correctly, indicating lucidity, (2) answer incorrectly, implying that his mental faculties were impaired, or (3) state that he did not know the answer, also indicating impairment. Muniz's initial incorrect response to the question about his age and his inability to give his address without looking at his license, like his inability to answer the sixth birthday question, in fact gave rise to the incriminating inference that his mental faculties were impaired. Accordingly, because the police did not inform Muniz of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights before asking the booking questions, his responses should have been suppressed.</p>
<p></p>
<h2>II</h2>
<p></p>
<h2>A</h2>
<p>The Court finds in Part IV of its opinion that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is inapplicable to Muniz's statements made in connection with the three sobriety tests and the breathalyzer examination because those statements (which were undoubtedly testimonial) were not the products of "custodial interrogation." In my view, however, the circumstances of this case  in particular, Muniz's apparent intoxication  rendered the officers' words and actions the "functional equivalent" of express questioning <span class="star-pagination">*613</span> because the police should have known that their conduct was "reasonably likely to evoke an incriminating response." <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><i>Innis, supra,</i> at 301</a></span>. As the Court recounts, <i>ante,</i> at 602-604, Officer Hosterman instructed Muniz how to perform the sobriety tests, inquired whether Muniz understood the instructions, and then directed Muniz to perform the tests. Officer Deyo later explained the breathalyzer examination and the nature of the Commonwealth's Implied Consent Law, and asked several times if Muniz understood the Law and wanted to take the examination. <i>Ante,</i> at 604. Although these words and actions might not prompt most sober persons to volunteer incriminating statements, Officers Hosterman and Deyo had good reason to believe  from the arresting officer's observations, App. 13-19 (testimony of Officer Spotts), from Muniz's failure of the three roadside sobriety tests, <i>id.,</i> at 19, and from their own observations  that Muniz was intoxicated. The officers thus should have known that Muniz was reasonably likely to have trouble understanding their instructions and their explanation of the Implied Consent Law, and that he was reasonably likely to indicate, in response to their questions, that he did not understand the tests or the Law. Moreover, because Muniz made several incriminating statements regarding his intoxication during and after the roadside tests, <i>id.,</i> at 20-21, the police should have known that the same tests at the booking center were reasonably likely to prompt similar incriminating statements.</p>
<p>The Court today, however, completely ignores Muniz's condition and focuses solely on the nature of the officers' words and actions. As the Court held in <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>,</i> however, the focus in the "functional equivalent" inquiry is on "the perceptions of the suspect," not on the officers' conduct viewed in isolation. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301</a></span>. Moreover, the <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span></i> Court emphasized that the officers' knowledge of any "unusual susceptibility" of a suspect to a particular means of eliciting information is relevant to the question whether they should have known that their conduct was reasonably likely to elicit <span class="star-pagination">*614</span> an incriminating response. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#302" aria-description="Citation for case: Rhode Island v. Innis"><i>Id.,</i> at 302, n. 8</a></span>; <i>supra,</i> at 610-611. See also <i>Arizona</i> v. <i>Mauro,</i> <span class="citation" data-id="9430952"><a href="/opinion/111878/arizona-v-mauro/#531" aria-description="Citation for case: Arizona v. Mauro">481 U. S. 520, 531</a></span> (1987) (STEVENS, J., dissenting) (police "interrogated" suspect by allowing him to converse with his wife "at a time when they knew [the conversation] was reasonably likely to produce an incriminating statement"). Muniz's apparent intoxication, then, and the police's knowledge of his statements during and after the roadside tests compel the conclusion that the police should have known that their words and actions were reasonably likely to elicit an incriminating response.<sup>[2]</sup> Muniz's statements were thus the product of custodial interrogation and should have been suppressed because Muniz was not first given the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.</p>
<p></p>
<h2>B</h2>
<p>The Court concedes that Officer Hosterman's directions that Muniz count aloud to 9 while performing the "walk and turn" test and to 30 while performing the "one leg stand" test constituted custodial interrogation. <i>Ante,</i> at 603, and n. 17. Also indisputable is the testimonial nature of the responses sought by those directions; the content of Muniz's counting, just like his answers to the sixth birthday and the booking questions, would provide the basis for an inference regarding his state of mind. Cf. <i>ante,</i> at 599; <i>supra,</i> at 612. The Court finds the admission at trial of Muniz's responses permissible, however, because they were not incriminating "except to the extent [they] exhibited a tendency to slur words, <span class="star-pagination">*615</span> which [the Court already found to be] nontestimonial [evidence]." <i>Ante,</i> at 603, n. 17. The Court's conclusion is wrong for two reasons. First, as a factual matter, Muniz's responses <i>were</i> incriminating for a reason other than his apparent slurring. Muniz did not count at all during the walk and turn test, supporting the inference that he was unable to do so.<sup>[3]</sup> And, contrary to the Court's assertion, <i>ibid.,</i> during the one leg stand test, Muniz incorrectly counted in Spanish from one to six, skipping the number two. Even if Muniz had not skipped "two," his failure to complete the count was incriminating in itself.</p>
<p>Second, and more importantly, Muniz's responses would have been "incriminating" for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> even if he had fully and accurately counted aloud during the two tests. As the Court stated in <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>,</i> "[b]y `incriminating response' we refer to any response  whether inculpatory or exculpatory  that the <i>prosecution</i> may seek to introduce at trial." <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301, n. 5</a></span>. See also <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476-477</a></span> ("The privilege against self-incrimination protects the individual from being compelled to incriminate himself in any manner; it does not distinguish degrees of incrimination. Similarly, for precisely the same reason, no distinction may be drawn between inculpatory statements and statements alleged to be merely `exculpatory' "). Thus, <i>any</i> response by <span class="star-pagination">*616</span> Muniz that the prosecution sought to use against him was incriminating under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> That the majority thinks Muniz's responses were incriminating only because of his slurring is therefore irrelevant. Because Muniz did not receive the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, then, his responses should have been suppressed.</p>
<p></p>
<h2>III</h2>
<p>All of Muniz's responses during the videotaped session were prompted by questions that sought testimonial answers during the course of custodial interrogation. Because the police did not read Muniz the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings before he gave those responses, the responses should have been suppressed. I would therefore affirm the judgment of the state court.<sup>[4]</sup></p>
<h2>NOTES</h2>
<p>[*]  <i>Solicitor General Starr, Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Christopher J. Wright</i> filed a brief for the United States as <i>amicus curiae</i> urging reversal.</p>
<p>[1]  The "horizontal gaze nystagmus" test measures the extent to which a person's eyes jerk as they follow an object moving from one side of the person's field of vision to the other. The test is premised on the understanding that, whereas everyone's eyes exhibit some jerking while turning to the side, when the subject is intoxicated "the onset of the jerking occurs after fewer degrees of turning, and the jerking at more extreme angles becomes more distinct." 1 R. Erwin et al., Defense of Drunk Driving Cases § 8A.99, pp. 8A-43, 8A-45 (1989). The "walk and turn" test requires the subject to walk heel to toe along a straight line for nine paces, pivot, and then walk back heel to toe along the line for another nine paces. The subject is requires to count each pace aloud from one to nine. The "one leg stand" test requires the subject to stand on one leg with the other leg extended in the air for 30 seconds, while counting aloud from 1 to 30.</p>
<p>[2]  There was a 14-minute delay between the completion of the physical sobriety tests and the beginning of the breathalyzer test. During this period, Muniz briefly engaged in conversation with Officer Hosterman. This 14-minute segment of the videotape was not shown at trial. App. 29.</p>
<p>[3]  The court did not suppress Muniz's verbal admissions to the arresting officer during the roadside tests, ruling that Muniz was not taken into custody for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> until he was arrested after the roadside tests were completed. See <i>Pennsylvania</i> v. <i>Bruder,</i> <span class="citation" data-id="9431478"><a href="/opinion/112152/pennsylvania-v-bruder/" aria-description="Citation for case: Pennsylvania v. Bruder">488 U. S. 9</a></span> (1988).</p>
<p>[4]  The Superior Court's opinion refers to Art. 1, § 9, of the Pennsylvania Constitution but explains that this provision " `offers a protection against self-incrimination identical to that provided by the Fifth Amendment.' " 377 Pa. Super., at 386, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 421</a></span> (quoting <i>Commonwealth</i> v. <i>Conway,</i> <span class="citation" data-id="9648993"><a href="/opinion/1533585/commonwealth-v-conway/#498" aria-description="Citation for case: Commonwealth v. Conway">368 Pa. Super. 488, 498</a></span>, <span class="citation" data-id="9648993"><a href="/opinion/1533585/commonwealth-v-conway/#546" aria-description="Citation for case: Commonwealth v. Conway">534 A. 2d 541, 546</a></span> (1987)). The decision therefore does not rest on an independent and adequate state ground. See <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983).</p>
<p>[5]  In <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), we held the privilege against self-incrimination applicable to the States through the Fourteenth Amendment.</p>
<p>[6]  Under Pennsylvania law, driving under the influence of alcohol consists of driving while intoxicated to a degree " `which substantially impairs [the suspect's] judgment, or clearness of intellect, or any of the normal faculties essential to the safe operation of an automobile.' " <i>Commonwealth</i> v. <i>Griscavage,</i> <span class="citation" data-id="9707237"><a href="/opinion/1996025/commonwealth-v-griscavage/#545" aria-description="Citation for case: Commonwealth v. Griscavage">512 Pa. 540, 545</a></span>, <span class="citation" data-id="9707237"><a href="/opinion/1996025/commonwealth-v-griscavage/#1258" aria-description="Citation for case: Commonwealth v. Griscavage">517 A. 2d 1256, 1258</a></span> (1986) (emphasis deleted).</p>
<p>[7]  See, <i>e. g., </i><i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#211" aria-description="Citation for case: Doe v. United States">487 U. S. 201, 211, n. 10</a></span> (1988) ("[T]he <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> line of cases does not draw a distinction between unprotected evidence sought for its physical characteristics and protected evidence sought for its [other] content. Rather, the Court distinguished between the suspect's being compelled himself to <i>serve as evidence</i> and the suspect's being compelled to <i>disclose or communicate information or facts</i> that might serve as or lead to incriminating evidence") (emphasis added); cf. <i>Baltimore Dept. of Social Services</i> v. <i>Bouknight,</i> <span class="citation" data-id="9431889"><a href="/opinion/112360/baltimore-city-department-of-social-services-v-bouknight/#555" aria-description="Citation for case: Baltimore City Department of Social Services v. Bouknight">493 U. S. 549, 555</a></span> (1990) (individual compelled to produce document or other tangible item to State "may not claim the [Fifth] Amendment's protections based upon the incrimination that may result from the contents or nature of the thing demanded" but may "clai[m] the benefits of the privilege because the act of production would amount to testimony").</p>
<p>[8]  See <i><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">Doe, supra,</a></span></i> at 212-213 (quoting <i>Murphy</i> v. <i>Waterfront Comm'n of New York Harbor,</i> <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964) (internal citations omitted)): "[T]he privilege is founded on `our unwillingness to subject those suspected of crime to the cruel trilemma of self-accusation, perjury or contempt; our preference for an accusatorial rather than an inquisitorial system of criminal justice; our fear that self-incriminating statements will be elicited by inhumane treatment and abuses; our sense of fair play which dictates "a fair state-individual balance by requiring the government . . . in its contest with the individual to shoulder the entire load," . . . ; our respect for the inviolability of the human personality and of the right of each individual "to a private enclave where he may lead a private life," . . . ; our distrust of self-deprecatory statements; and our realization that the privilege, while sometimes "a shelter to the guilty," is often "a protection to the innocent." ' "</p>
<p>[9]  This definition applies to both verbal and nonverbal conduct; nonverbal conduct contains a testimonial component whenever the conduct reflects the actor's communication of his thoughts to another. See <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#209" aria-description="Citation for case: Doe v. United States"><i>Doe, supra,</i> at 209-210</a></span>, and n. 8; <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 761, n. 5</a></span> (1966) ("A nod or head-shake is as much a `testimonial' or `communicative' act in this sense as are spoken words"); see also <i>Braswell</i> v. <i>United States,</i> <span class="citation" data-id="9431386"><a href="/opinion/112120/braswell-v-united-states/#122" aria-description="Citation for case: Braswell v. United States">487 U. S. 99, 122</a></span> (1988) (KENNEDY, J., dissenting) ("Those assertions [contained within the act of producing subpoenaed documents] can convey information about that individual's knowledge and state of mind as effectively as spoken statements, and the Fifth Amendment protects individuals from having such assertions compelled by their own acts").</p>
<p>[10]  During custodial interrogation, the pressure on the suspect to respond flows not from the threat of contempt sanctions, but rather from the "inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely." <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467</a></span> (1966). Moreover, false testimony does not give rise directly to sanctions (either religious sanctions for lying under oath or prosecutions for perjury), but only indirectly (false testimony might itself prove incriminating, either because it links (albeit falsely) the suspect to the crime or because the prosecution might later prove at trial that the suspect lied to the police, giving rise to an inference of guilty conscience). Despite these differences, however, "[w]e are satisfied that all the principles embodied in the privilege apply to informal compulsion exerted by law-enforcement officers during in-custody questioning." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 461</a></span>; see <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 458</a></span> (noting "intimate connection between the privilege against self-incrimination and police custodial questioning").</p>
<p>[11]  As we explain <i>infra,</i> at 600-601, for purposes of custodial interrogation such a question may be either express, as in this case, or else implied through words or actions reasonably likely to elicit a response.</p>
<p>[12]  See also <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 222-223</a></span> (1967) ("[T]o utter words purportedly uttered by the robber [and dictated to the suspect by the police] was not compulsion to utter statements of a `testimonial' nature; [the suspect] was required to use his voice as an identifying physical characteristic, not to speak his guilt" because the words did not reflect any facts or beliefs asserted by the suspect); <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#7" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 7</a></span> (1973) (where suspects were asked to create voice exemplars by reading already-prepared transcripts, the "voice recordings were to be used solely to measure the physical properties of the witnesses' voices, not for the testimonial or communicative content of what was to be said" because the content did not reflect any facts or beliefs asserted by the suspects).</p>
<p>[13]  The Commonwealth's protest that it had no investigatory interest in the actual date of Muniz's sixth birthday, see Tr. of Oral Arg. 18, is inapposite. The critical point is that the Commonwealth had an investigatory interest in Muniz's assertion of belief that was communicated by his answer to the question. Putting it another way, the Commonwealth may not have cared about the <i>correct</i> answer, but it cared about <i>Muniz's</i> answer. The incriminating inference stems from the then-existing contents of Muniz's mind as evidenced by his assertion of his knowledge at that time.
</p>
<p>This distinction is reflected in <i>Estelle</i> v. <i>Smith,</i> <span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454</a></span> (1981), where we held that a defendant's answers to questions during a psychiatric examination were testimonial in nature. The psychiatrist asked a series of questions, some focusing on the defendant's account of the crime. After analyzing both the "statements [the defendant] made, and remarks he omitted." <span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#464" aria-description="Citation for case: Estelle v. Smith"><i>id.,</i> at 464</a></span>, the psychiatrist made a prognosis as to the defendant's "future dangerousness" and testified to this effect at his capital sentencing hearing. The psychiatrist had no investigative interest in whether the defendant's account of the crime and other disclosures were either accurate or complete as a historical matter; rather, he relied on the remarks  both those made and omitted  to infer that the defendant would likely pose a threat to society in the future because of his state of mind. We nevertheless explained that the "Fifth Amendment privilege . . . is directly involved here because the State used as evidence against [the defendant] the <i>substance of his disclosures</i> during the pretrial psychiatric examination." <span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#464" aria-description="Citation for case: Estelle v. Smith"><i>Id.,</i> at 464-465</a></span> (emphasis added). The psychiatrist may have presumed the defendant's remarks to be truthful for purposes of drawing his inferences as to the defendant's state of mind, see <i>South Dakota</i> v. <i>Neville,</i> <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#561" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 561-562, n. 12</a></span> (1983), but that is true in Muniz's case as well: The incriminating inference of mental confusion is based on the premise that Muniz was responding truthfully to Officer Hosterman's question when he stated that he did not then know the date of his sixth birthday.</p>
<p>[14]  As <i>amicus</i> United States explains, "[r]ecognizing a `booking exception' to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> does not mean, of course, that any question asked during the booking process falls within that exception. Without obtaining a waiver of the suspect's <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, the police may not ask questions, even during booking, that are designed to elicit incriminatory admissions." Brief for United States as <i>Amicus Curiae</i> 13. See, <i>e. g., </i><i>United States</i> v. <i>Avery,</i> <span class="citation" data-id="424921"><a href="/opinion/424921/united-states-v-ozzie-lee-avery-jr/#1024" aria-description="Citation for case: United States v. Ozzie Lee Avery, Jr.">717 F. 2d 1020, 1024-1025</a></span> (CA6 1983); <i>United States</i> v. <i>Mata-Abundiz,</i> <span class="citation" data-id="424960"><a href="/opinion/424960/united-states-v-jesus-mata-abundiz/#1280" aria-description="Citation for case: United States v. Jesus Mata-Abundiz">717 F. 2d 1277, 1280</a></span> (CA9 1983); <i>United States</i> v. <i>Glen-Archila,</i> <span class="citation" data-id="403655"><a href="/opinion/403655/united-states-v-homero-glen-archila-dudley-astor-may-mitchell/#816" aria-description="Citation for case: United States v. Homero Glen-Archila, Dudley Astor...">677 F. 2d 809, 816, n. 18</a></span> (CA11 1982).</p>
<p>[15]  Most of Muniz's utterances were not clearly discernible, though several of them suggested excuses as to why he could not perform the physical tests under these circumstances.</p>
<p>[16]  This conclusion is in accord with that of many other state courts, which have reasoned that standard sobriety tests measuring reflexes, dexterity, and balance do not require the performance of testimonial acts. See, <i>e. g., </i><i>Weatherford</i> v. <i>State,</i> <span class="citation" data-id="9682429"><a href="/opinion/1782123/weatherford-v-state/" aria-description="Citation for case: Weatherford v. State">286 Ark. 376</a></span>, <span class="citation" data-id="9682429"><a href="/opinion/1782123/weatherford-v-state/" aria-description="Citation for case: Weatherford v. State">692 S. W. 2d 605</a></span> (1985); <i>People</i> v. <i>Boudreau,</i> 115 App. Div. 2d 652, 496 N. Y. S. 2d 489 (1985); <i>Commonwealth</i> v. <i>Brennan,</i> <span class="citation" data-id="2102837"><a href="/opinion/2102837/commonwealth-v-brennan/" aria-description="Citation for case: Commonwealth v. Brennan">386 Mass. 772</a></span>, <span class="citation" data-id="2102837"><a href="/opinion/2102837/commonwealth-v-brennan/" aria-description="Citation for case: Commonwealth v. Brennan">438 N. E. 2d 60</a></span> (1982); <i>State</i> v. <i>Badon,</i> <span class="citation" data-id="1702883"><a href="/opinion/1702883/state-v-badon/" aria-description="Citation for case: State v. Badon">401 So. 2d 1178</a></span> (La. 1981); <i>State</i> v. <i>Arsenault,</i> 115 N. H. 109, <span class="citation" data-id="2263639"><a href="/opinion/2263639/state-v-arsenault/" aria-description="Citation for case: State v. Arsenault">336 A. 2d 244</a></span> (1975). Muniz does not challenge the state court's conclusion on this point, and therefore we have no occasion to review it.</p>
<p>[17]  The two exceptions consist of Officer Hosterman's requests that Muniz count aloud from 1 to 9 while performing the "walk and turn" test and that he count aloud from 1 to 30 while balancing during the "one leg stand" test. Muniz's counting at the officer's request qualifies as a response to custodial interrogation. However, as Muniz counted accurately (in Spanish) for the duration of his performance on the "one leg stand" test (though he did not complete it), his verbal response to this instruction was not incriminating except to the extent that it exhibited a tendency to slur words, which we have already explained is a nontestimonial component of his response. See <i>supra,</i> at 590-592. Muniz did not count during the "walk and turn" test, and he does not argue that his failure to do so has any independent incriminating significance. We therefore need not decide today whether Muniz's counting (or not counting) itself was "testimonial" within the meaning of the privilege.</p>
<p>[18]  We cannot credit the state court's contrary determination that Muniz's utterances (both during this phase of the proceedings and during the next when he was asked to provide a breath sample) were compelled rather than voluntary. 377 Pa. Super., at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>. The court did not explain how it reached this conclusion, nor did it cite <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span></i> or any other case defining custodial interrogation.</p>
<p>[19]  Muniz does not and cannot challenge the introduction into evidence of his refusal to submit to the breathalyzer test. In <i>South Dakota</i> v. <i>Neville,</i> <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553</a></span> (1983), we held that since submission to a blood test could itself be compelled, see <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), a State's decision to permit a suspect to refuse to take the test but then to comment upon that refusal at trial did not "compel" the suspect to incriminate himself and hence did not violate the privilege. <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#562" aria-description="Citation for case: South Dakota v. Neville"><i>Neville, supra,</i> at 562-564</a></span>. We see no reason to distinguish between chemical blood tests and breathalyzer tests for these purposes. Cf. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California"><i>Schmerber, supra,</i> at 765-766, n. 9</a></span>.</p>
<p>[20]  We noted in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> that "there may be circumstances in which the pain, danger, or severity of an operation [or other test seeking physical evidence] would almost inevitably cause a person to prefer confession to undergoing the `search,' " 384 U. S., at 765, n. 9, and in such cases "[i]f it wishes to compel persons to submit to such attempts to discover evidence, the State may have to forgo the advantage of any <i>testimonial</i> products of administering the test." <i>Ibid.</i> See also <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#563" aria-description="Citation for case: South Dakota v. Neville"><i>Neville, supra,</i> at 563</a></span> ("Fifth Amendment may bar the use of testimony obtained when the proffered alternative was to submit to a test so painful, dangerous, or severe, or so violative of religious beliefs, that almost inevitably a person would prefer `confession' "). But Muniz claims no such extraordinary circumstance here.</p>
<p>[21]  See n. 18, <i>supra.</i></p>
<p>[22]  The parties have not asked us to decide whether any error in this case was harmless. The state court is free, of course, to consider this question upon remand.</p>
<p>[1]  The sixth birthday question also clearly constituted custodial interrogation because it was a form of "express questioning." <i>Rhode Island</i> v. <i>Innis,</i> <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#300" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 300-301</a></span> (1980). Furthermore, that question would not fall within JUSTICE BRENNAN's proposed routine booking question exception. The question serves no apparent recordkeeping need, as the police already possessed Muniz's date of birth. The absence of any administrative need for the question, moreover, suggests that the question was designed to obtain an incriminating response. Regardless of any administrative need for the question and regardless of the officer's intent, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were required because the police should have known that the question was reasonably likely to elicit an incriminating response. <i>Supra,</i> at 610-611.</p>
<p>[2]  An additional factor strongly suggests that the police expected Muniz to make incriminating statements. Pursuant to their routine in such cases, App. 28-29, the police allotted 20 minutes for the three sobriety tests and for "observation." Because Muniz finished the tests in approximately 6 minutes, the police required him to wait another 14 minutes before they asked him to submit to the breathalyzer examination. Given the absence of any apparent technical or administrative reason for the delay and the stated purpose of "observing" Muniz, the delay appears to have been designed in part to give Muniz the opportunity to make incriminating statements.</p>
<p>[3]  The Commonwealth could not use Muniz's failure to count against him regardless of whether his silence during the walk and turn test was itself testimonial in those circumstances. Cf. <i>ante,</i> at 603, n. 17. A defendant's silence in response to police questioning is not admissible at trial even if the silence is not, in the particular circumstances, a form of communicative conduct. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 468, n. 37</a></span> (1966) ("[I]t is impermissible to penalize an individual for exercising his Fifth Amendment privilege when he is under police custodial interrogation. The prosecution may not, therefore, use at trial the fact that he stood mute or claimed his privilege in the face of accusation"). Cf. <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/#615" aria-description="Citation for case: Griffin v. California">380 U. S. 609, 615</a></span> (1965) ("[T]he Fifth Amendment . . . forbids either comment by the prosecution on the accused's silence or instructions by the court that such silence is evidence of guilt").</p>
<p>[4]  I continue to have serious reservations about the Court's limitation of the Fifth Amendment privilege to "testimonial" evidence. See <i>United States</i> v. <i>Mara,</i> <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#32" aria-description="Citation for case: United States v. Mara">410 U. S. 19, 32-38</a></span> (1973) (MARSHALL, J., dissenting). I believe that privilege extends to <i>any</i> evidence that a person is compelled to furnish against himself. <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#33" aria-description="Citation for case: United States v. Mara"><i>Id.,</i> at 33-35</a></span>. At the very least, the privilege includes evidence that can be obtained only through the person's affirmative cooperation. <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#36" aria-description="Citation for case: United States v. Mara"><i>Id.,</i> at 36-37</a></span>. Of course, a person's refusal to incriminate himself also cannot be used against him. See n. 3, <i>supra.</i> Muniz's performance of the sobriety tests and his refusal to take the breathalyzer examination are thus protected by the Fifth Amendment under this interpretation. But cf. <i>ante,</i> at 604-605, n. 19. Because Muniz does not challenge the admission of the video portion of the videotape showing the sobriety tests or of his refusal to take the breathalyzer examination, however, those issues are not before this Court.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/People v. Frederick.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: People v. Frederick
type: case
citation: "500 Mich. 228 (2017)"
parallel_cite: ""
neutral_cite: ""
court: Mich.
court_level: state
circuit: ""
year: 2017
date_decided: 2017-06-01
docket: 153115
authority_weight: "Persuasive — state, illustrative"
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
  opinion_url: "https://www.courtlistener.com/opinion/4396951/people-of-michigan-v-michael-christopher-frederick/"
  cluster_id: 4396951
  opinion_id: null
  identity_checked: false
lake:
  record_id: People v. Frederick
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Knock and Talk]]"
    role: Key
related:
  - "[[Knock and Talk]]"
  - "[[Florida v. Jardines]]"
tags:
  - case
  - fourth-amendment
  - knock-and-talk
  - curtilage
  - implied-license
  - jardines
  - trespass
  - michigan-supreme-court
holding: "The implied license that lets an officer approach a home and knock is time-sensitive and generally does not extend to predawn approaches; when officers conducted 4:00 and 5:30 a.m. 'knock and talks' at the defendants' homes, they exceeded that license and trespassed on Fourth-Amendment-protected property, and because the trespass was joined to information-gathering it was a search — so the consents that followed had to be analyzed for taint from the illegal search."
aliases:
  - People v. Frederick
  - "People v. Frederick (Mich. 2017)"
  - Michigan v. Frederick
---

# People v. Frederick

*500 Mich. 228 (2017)* (Docket Nos. 153115, 153117) · Michigan Supreme Court · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4396951 → unanimous opinion 4174204 (McCormack, J.; 500 Mich. 228, decided June 1, 2017). Citation recovered dual-leg (vLex + Justia), source web-dual-leg — CL cluster carries no citations[]. Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (CL text carries the Michigan syllabus/opinion, not the 500 Mich. star pages) — S9 verifies the reporter pincite. -->

## Background
Seven officers of the Kent Area Narcotics Enforcement Team made unscheduled predawn visits to the homes of Michael Frederick and Todd Van Doorne on March 18, 2014, knocking on Frederick's door around 4:00 a.m. and Van Doorne's around 5:30 a.m. to question them about suspected marijuana butter. Each defendant, awakened with his family, consented to a search; marijuana products were recovered. The trial court denied suppression, reasoning that the predawn knocks were not a search and the consents were valid. A divided Court of Appeals affirmed.

## Issue
Whether a predawn "knock and talk" at a home exceeds the scope of the implied license to approach and knock, so that the officers' conduct is a Fourth Amendment search.

## Rule
The scope of a [[Knock and Talk|knock-and-talk]] is bounded by the implied license extended to any private citizen, which is time-sensitive; a private citizen would not be welcome to knock at 4:00 a.m., so officers who do so stray beyond the license and trespass on constitutionally protected [[Curtilage|curtilage]]. The court held: "The scope of the implied license to approach a house and knock is time-sensitive; it generally does not extend to predawn approaches. While approaching a home with the purpose of gathering information is not, standing alone, a Fourth Amendment search, when information-gathering is conjoined with a trespass, a Fourth Amendment search has occurred." — slip op. at 1. ^pin-slip1

## Application
Because the officers approached the homes during predawn hours — outside the hours at which a homeowner would expect an uninvited visitor — they exceeded the implied license and trespassed on Fourth-Amendment-protected property. Since the trespass was joined to their purpose of gathering information, each was a search under *[[Florida v. Jardines]]*. The court did not decide the ultimate suppression question; it [[Reading and Citing Cases#on-remand|remanded]] for the trial court to determine whether the defendants' consent was attenuated from the illegal searches.

## Conclusion
**Reversed and [[Reading and Citing Cases#on-remand|remanded]]** for the trial court to determine whether the consents were attenuated from the officers' illegal searches. Justice McCormack wrote for a unanimous court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Frederick* is a widely taught state-court application of *[[Florida v. Jardines|Jardines]]*: the implied license to knock has temporal limits, and a predawn approach converts a [[Knock and Talk|knock-and-talk]] into a trespassory search. It is persuasive, illustrative authority (Michigan Supreme Court) for the federal *[[Knock and Talk|knock-and-talk]]* doctrine, not binding federal precedent.

## Appears on
- [[Knock and Talk]] — *Key*

## Sources
- [*People v. Frederick*, 500 Mich. 228 (2017)](https://www.courtlistener.com/opinion/4396951/people-of-michigan-v-michael-christopher-frederick/) — pinpoint: slip op. at 1 (predawn approach exceeds the implied license; trespass-plus-information-gathering is a search). Rule quote string-matched to the CL opinion text 2026-07-07. Official cite 500 Mich. 228 (parallel 895 N.W.2d 541) recovered via two independent sources (vLex, Justia); the CL cluster carries no citations[].

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a6e4c2a4c6d92730", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "People v. Frederick"}, "payload": {"all": [{"cite": "500 Mich. 228", "page": "228", "reporter": "Mich.", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "500"}], "display": "500 Mich. 228", "official": {"cite": "500 Mich. 228", "page": "228", "reporter": "Mich.", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "500"}, "official_selection_present": true, "record_id": "People v. Frederick"}}
{"assertion_id": "d08e1ab72f13d3e0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "People v. Frederick"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "People v. Frederick", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — People v. Frederick

```json
{
  "schema_version": "s2.v1",
  "record_id": "People v. Frederick",
  "status": "under_review",
  "identity": {
    "case_name": "People of Michigan v. Michael Christopher Frederick",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "People v. Frederick",
    "court": "Mich.",
    "court_id": null,
    "court_level": "state",
    "circuit": null,
    "state": "Michigan",
    "date_decided": "2017-06-01",
    "year": 2017,
    "docket": "153115",
    "cluster_id": 4396951,
    "lead_opinion_id": 4174204,
    "sibling_ids": [],
    "absolute_url": "/opinion/4396951/people-of-michigan-v-michael-christopher-frederick/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4246807,
        "score": 90,
        "case_name": "People of Michigan v. Michael Christopher Frederick"
      },
      {
        "cluster_id": 4246793,
        "score": 90,
        "case_name": "People of Michigan v. Michael Christopher Frederick"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "500 Mich. 228",
      "volume": "500",
      "reporter": "Mich.",
      "page": "228",
      "type": 1,
      "selected_official": true,
      "source": "web-dual-leg"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "500 Mich. 228",
        "volume": "500",
        "reporter": "Mich.",
        "page": "228",
        "type": 1,
        "selected_official": true,
        "source": "web-dual-leg"
      }
    ],
    "display": "500 Mich. 228",
    "official_selection": {
      "court_class": "state",
      "selected": "500 Mich. 228",
      "reason": "web-dual-leg"
    },
    "web_legs": [
      {
        "source": "vLex",
        "url": "https://case-law.vlex.com/vid/people-v-frederick-no-885598045",
        "cite": "500 Mich. 228",
        "checked_date": "2026-07-07"
      },
      {
        "source": "Justia",
        "url": "https://law.justia.com/cases/michigan/supreme-court/2017/153115.html",
        "cite": "500 Mich. 228",
        "checked_date": "2026-07-07"
      }
    ]
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
    "date_created": "2026-07-07T18:21:34Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:23:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:23:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:23:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:23:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "people-v-frederick--4396951",
      "to_record_id": "People v. Frederick",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — People v. Frederick

```
                                                                                     Michigan Supreme Court
                                                                                           Lansing, Michigan




Syllabus
                                                                Chief Justice:       Justices:
                                                                Stephen J. Markman   Brian K. Zahra
                                                                                     Bridget M. McCormack
                                                                                     David F. Viviano
                                                                                     Richard H. Bernstein
                                                                                     Joan L. Larsen
                                                                                     Kurtis T. Wilder
This syllabus constitutes no part of the opinion of the Court but has been           Reporter of Decisions:
prepared by the Reporter of Decisions for the convenience of the reader.             Kathryn L. Loomis



                                            PEOPLE v FREDERICK
                                           PEOPLE v VAN DOORNE

             Docket Nos. 153115 and 153117. Argued on application for leave to appeal March 9,
       2017. Decided June 1, 2017.

               Michael Frederick and Todd Van Doorne were separately charged in the Kent Circuit
       Court with various drug offenses after seven officers from the Kent Area Narcotics Enforcement
       Team made unscheduled visits to the defendants’ respective homes during the predawn hours on
       March 18, 2014. Officers knocked on Frederick’s door around 4:00 a.m. and on Van Doorne’s
       door around 5:30 a.m. Officers woke defendants and their families for the purpose of
       questioning each defendant about marijuana butter that they suspected the defendants possessed.
       Both defendants subsequently consented to a search of their respective homes, and marijuana
       butter and other marijuana products were recovered from each home. Defendants moved to
       suppress the evidence, and the court, Dennis B. Leiber, J., denied both motions, concluding that
       the officers had not conducted a search by knocking on defendants’ doors during the predawn
       hours and that the subsequent consent searches were valid. Defendants sought interlocutory
       leave to appeal, which the Court of Appeals denied in separate unpublished orders, entered
       October 15, 2014 (Docket Nos. 323642 and 323643). Defendants sought leave to appeal in the
       Supreme Court. The Supreme Court, in lieu of granting leave to appeal, remanded the cases to
       the Court of Appeals for consideration as on leave granted and directed the Court of Appeals to
       address whether the “knock and talk” procedure conducted in these cases was consistent with the
       Fourth Amendment as articulated in Florida v Jardines, 569 US ___; 133 S Ct 1409 (2013).
       People v Frederick, 497 Mich 993 (2015); People v Van Doorne, 497 Mich 993 (2015). The
       Court of Appeals consolidated the two cases and issued a split opinion. 313 Mich App 457
       (2015). The majority concluded that the officers’ predawn “knock and talk” visits were within
       the scope of the public’s implied license because homeowners would be unsurprised to find a
       predawn visitor delivering a newspaper or seeking emergency assistance, but the dissenting
       judge concluded that the police conduct violated the Fourth Amendment because the searches,
       which occurred during hours at which a homeowner would not expect visitors, were outside the
       scope of a proper knock and talk procedure. Defendants sought leave to appeal, and the Supreme
       Court ordered and heard oral argument on whether to grant the application or take other action.
       499 Mich 952 (2016).

             In a unanimous opinion by Justice MCCORMACK, in lieu of granting leave to appeal, the
       Supreme Court held:
        The scope of the implied license to approach a house and knock is time-sensitive; it
generally does not extend to predawn approaches. While approaching a home with the purpose
of gathering information is not, standing alone, a Fourth Amendment search, when information-
gathering is conjoined with a trespass, a Fourth Amendment search has occurred. In these cases,
the police conduct exceeded the scope of the implied license to knock and talk because the
officers approached the defendants’ respective homes during the predawn hours; therefore, the
officers trespassed on Fourth-Amendment-protected property. And because the officers
trespassed while seeking information, they performed searches in violation of the Fourth
Amendment.

        1. The proper scope of a knock and talk is determined by the implied license that is
granted to the general public. Therefore, a police officer not armed with a warrant may approach
a home and knock precisely because that is no more than any private citizen might do. When
police officers stray beyond what any private citizen might do, they have strayed beyond the
bounds of a permissible knock and talk; in other words, the officers are trespassing. Just as there
is no implied license to bring a drug-sniffing dog to someone’s front porch, there is generally no
implied license to knock at someone’s door in the middle of the night. Background social norms
that invite a visitor to the front door typically do not extend to a visit in the middle of the night.
Accordingly, the scope of the implied license to approach a house and knock is time-sensitive; it
generally does not extend to predawn approaches. Additionally, while approaching a home with
the purpose of gathering information is not, standing alone, a Fourth Amendment search, when
information-gathering is conjoined with a trespass, a Fourth Amendment search has occurred. In
these cases, the police officers exceeded the scope of the implied license to knock and talk
because the officers approached defendants’ respective homes without warrants during the
predawn hours; therefore, the officers trespassed on Fourth-Amendment-protected property.
And because the officers trespassed while seeking information about defendants’ alleged
possession of marijuana butter, they performed searches in violation of the Fourth Amendment.

        2. Consent searches, when voluntary, are an exception to the warrant requirement. The
voluntariness question turns on whether a reasonable person would, under the totality of the
circumstances, feel able to choose whether to consent. Evidence obtained through an illegal
search or seizure is tainted by that initial illegality unless sufficiently attenuated from it. Thus,
even when consent is voluntary, if it is not attenuated from the unconstitutional search, the
evidence must be suppressed. Three factors are considered in determining whether consent is
sufficiently attenuated: (1) the temporal proximity of the illegal act and the alleged consent, (2)
the presence of intervening circumstances, and (3) the purpose and flagrancy of the official
misconduct. In these cases, because the trial court determined that there was no Fourth
Amendment violation, it did not consider whether the subsequent consent was attenuated from
the illegality. Therefore, the cases had to be remanded to the trial court for consideration of that
question in the first instance.

       Reversed and remanded to the Kent Circuit Court to determine whether defendants’
consent to search was attenuated from the officers’ illegal search.



                                     ©2017 State of Michigan
                                                                 Michigan Supreme Court
                                                                       Lansing, Michigan




OPINION
                                          Chief Justice:           Justices:
                                          Stephen J. Markman       Brian K. Zahra
                                                                   Bridget M. McCormack
                                                                   David F. Viviano
                                                                   Richard H. Bernstein
                                                                   Joan L. Larsen
                                                                   Kurtis T. Wilder

                                                           FILED June 1, 2017




                        STATE OF MICHIGAN

                               SUPREME COURT


PEOPLE OF THE STATE OF MICHIGAN,

         Plaintiff-Appellee,

v                                                   No. 153115

MICHAEL CHRISTOPHER FREDERICK,

         Defendant-Appellant.



PEOPLE OF THE STATE OF MICHIGAN,

         Plaintiff-Appellee,

v                                                   No. 153117

TODD RANDOLPH VAN DOORNE,

         Defendant-Appellant.


BEFORE THE ENTIRE BENCH
MCCORMACK, J.
       In these consolidated cases, we consider the constitutionality of two early morning

searches of the defendants’ homes. We conclude that the police conduct in both cases

was unconstitutional; these were not permissible “knock and talks,” but rather warrantless

searches. Because of these illegal searches, the defendants’ consent to search—even if

voluntary—is invalid unless it is sufficiently attenuated from the illegality. Accordingly,

we reverse the Court of Appeals’ contrary determination and remand these cases to the

Kent Circuit Court for further proceedings.

                      I. FACTS AND PROCEDURAL HISTORY

       During the predawn hours on March 18, 2014, seven officers from the Kent Area

Narcotics Enforcement Team (KANET) made unscheduled visits to the defendants’

homes. Both defendants were employees of the corrections division of the Kent County

Sheriff Department. Their names had come up in a criminal investigation, and KANET

decided to perform these early morning visits to the defendants’ homes rather than

waiting until daytime to speak with the defendants (or seeking search warrants). KANET

knocked on defendant Michael Frederick’s door around 4:00 a.m. and on defendant Todd

Van Doorne’s door around 5:30 a.m. Lieutenant Al Roetman, who was present at both

searches, testified that everyone appeared to be asleep at both houses.

       Both defendants and their families were surprised and alarmed by the intrusions.

Van Doorne considered arming himself, as did Frederick’s wife. Nonetheless, both

defendants answered the door after a few minutes of knocking—each thinking that there

must have been some sort of emergency.




                                              2
         Instead, each defendant found himself confronted with a group of police officers.

The officers asked each defendant about marijuana butter that they suspected the

defendants possessed.     After a conversation with each defendant, during which the

defendants were read their Miranda 1 rights, both defendants consented to a search of

their homes and signed a consent form to that effect.        Marijuana butter and other

marijuana products were recovered from each house.

         The defendants were charged with various drug offenses. Both moved to suppress

evidence of the marijuana products found in their homes. The trial court denied both

motions. The court concluded that KANET had not conducted a search by approaching

the home and knocking, and that the subsequent consent search was a valid, voluntary

search. The court distinguished Florida v Jardines, 569 US ___; 133 S Ct 1409; 185 L

Ed 2d 495 (2013), noting that the police here did not use a drug-sniffing dog or otherwise

try to search the home without knocking. Rather, because the police approached the

home and knocked, the trial court held that these were valid knock and talks.

         The defendants sought interlocutory leave to appeal, which the Court of Appeals

denied. The defendants then sought leave to appeal in this Court. In lieu of granting

leave to appeal, we remanded the cases to the Court of Appeals for consideration as on

leave granted. People v Frederick, 497 Mich 993 (2015); People v Van Doorne, 497

Mich 993 (2015). We directed the Court of Appeals to address “whether the ‘knock and

talk’ procedure conducted in [these cases] is consistent with US Const, Am IV, as



1
    Miranda v Arizona, 384 US 436; 86 S Ct 1602; 16 L Ed 2d 694 (1966).



                                             3
articulated in Florida v Jardines . . . .” Frederick, 497 Mich 993; Van Doorne, 497 Mich

993.

       On remand, the Court of Appeals issued a split opinion. The majority concluded

that the knock and talk procedures at issue were permitted by the Fourth Amendment.

People v Frederick, 313 Mich App 457, 461; 886 NW2d 1 (2015).              The majority

emphasized that the officers approached the home, knocked, and waited to be received,

and “Jardines plainly condones such conduct.” Id. at 469. Though the police visits here

occurred during the early morning hours, the majority concluded that they were

nonetheless within the scope of the implied license because homeowners would be

unsurprised to find a predawn visitor delivering a newspaper or seeking emergency

assistance. Id. at 481.

       Judge SERVITTO dissented. She concluded that the police conduct violated the

defendants’ Fourth Amendment rights. Id. at 496 (SERVITTO, J., dissenting). First, Judge

SERVITTO noted that the Jardines majority and dissent had seemed to agree, in dicta, that

nighttime visits would be outside the scope of the implied license. Id. at 487-488.

Further, Judge SERVITTO reasoned that the validity of a knock and talk is premised on

“the implied license a homeowner extends to the public-at-large.” Id. at 496. Because

the hours the police arrived at the defendants’ homes are not times at which most

homeowners expect visitors, she concluded that the visits were outside the scope of a

proper knock and talk. Id.




                                           4
                                     II. ANALYSIS

      In general, a search or seizure within a home or its curtilage without a warrant is

per se an unreasonable search under the Fourth Amendment. People v Champion, 452

Mich 92, 98; 549 NW2d 849 (1996); Katz v United States, 389 US 347, 357; 88 S Ct 507;

19 L Ed 2d 576 (1967). Two arguments have been presented as to why this police

conduct was lawful. First, the prosecution argues that the initial approach was a knock

and talk, not a search. Second, the prosecution argues that the search that followed that

initial approach was a consent search.

                                A. KNOCK AND TALK

      A “knock and talk,” when performed within its proper scope, is not a search at all.

Jardines, 569 US at ___; 133 S Ct at 1415. The proper scope of a knock and talk is

determined by the “implied license” that is granted to “solicitors, hawkers, and peddlers

of all kinds.” Id. at ___; 133 S Ct at 1415 (citation and quotation marks omitted). “Thus,

a police officer not armed with a warrant may approach a home and knock, precisely

because that is ‘no more than any private citizen might do.’ ” Id. at ___; 133 S Ct at

1416, quoting Kentucky v King, 563 US 452, 469; 131 S Ct 1849; 179 L Ed 2d 865

(2011).

      In Jardines, the police approached a house via the front walk with a drug dog.

Jardines, 569 US at ___; 133 S Ct at 1413. The dog alerted, indicating that it smelled

contraband, and eventually sat at the front door of the home, where the odor was

strongest. Id. Using this information, the police obtained a warrant, and their search of

the home revealed marijuana plants. Id.




                                            5
       Justice Scalia, writing for the Court, employed a property-rights framework 2 to

conclude that the prewarrant conduct of the police constituted a search. The Court

distinguished the case from King, in which the Court had held that a knock and talk was

not a search, because the police in Jardines, unlike the police in King, had trespassed;

although the public, and thus the police, generally have an implied license to “approach

the door by the front path, knock promptly, wait briefly to be received, and then (absent

invitation to linger longer) leave,” the police in Jardines had not complied with the scope

of that implied license. Id. at ___; 133 S Ct at 1415-1416. “[I]ntroducing a trained police

dog to explore the area around the home in hopes of discovering incriminating evidence


2
  In Katz v United States, 389 US 347, the Court broke with tradition by considering not
whether the government had trod on the defendant’s property interests, but rather whether
it had violated his privacy interests. Subsequently, the Court clarified that Katz had not
replaced the property-interests test; Katz merely added to it. Alderman v United States,
394 US 165, 180; 89 S Ct 961; 22 L Ed 2d 176 (1969) (“[W]e [do not] believe that Katz,
by holding that the Fourth Amendment protects persons and their private conversations,
was intended to withdraw any of the protection which the Amendment extends to the
home . . . .”).

         The Court reaffirmed the importance of the property-rights analysis in the Fourth
Amendment context in United States v Jones, 565 US 400; 132 S Ct 945; 181 L Ed 2d
911 (2012). In that case, the Court held that the warrantless installation of a GPS
tracking device on the exterior of a Jeep and subsequent tracking of the defendant’s
movements on public roads constituted a search, despite the Court’s earlier holdings that
tracking of a defendant’s movements on public roads was not a search. Id. at 404; cf.
United States v Knotts, 460 US 276; 103 S Ct 1081; 75 L Ed 2d 55 (1983) (holding that
no search occurred when law enforcement tracked on public roads the location of a
beeper that had been installed in a container before the defendant’s possession of the
container). The Jones Court distinguished Knotts on the ground that it did not involve a
trespass. Jones, 565 US at 409-410. The violation of Jones’s property rights, combined
with the subsequent information-gathering, constituted a search. Id. at 407-408. The
Court cautioned that “[t]respass alone does not qualify, but there must be conjoined with
that . . . an attempt to find something or to obtain information.” Id. at 408 n 5.



                                            6
is something else. There is no customary invitation to do that.” Id. at ___; 133 S Ct at

1416. Thus, the police had trespassed on Fourth-Amendment-protected property. 3 Id.

       Consistently with United States v Jones, 565 US 400; 132 S Ct 945; 181 L Ed 2d

911 (2012), the Jardines Court required not only a trespass, but also some attempted

information-gathering, to find that a search had occurred. Jardines, 569 US at ___; 133 S

Ct at 1414; Jones, 565 US at 408 n 5 (“[P]ost-Katz we have explained that an actual

trespass is neither necessary nor sufficient to establish a constitutional violation. . . .

Trespass alone does not qualify [as a search], but there must be conjoined with that . . . an

attempt to find something or to obtain information.”) (citations and quotation marks

omitted).   The Jardines Court concluded that the police conduct there included

information-gathering, such that the behavior constituted a warrantless search of the

curtilage. Jardines, 569 US at ___; 133 S Ct at 1417.

       It is also clear from Jones and Jardines that “information-gathering” is not

synonymous with a Fourth Amendment “search.” Both Jones and Jardines held that

conduct that would not amount to a search, standing alone, was nonetheless information-

gathering. The information-gathering in Jardines was the use of a drug-sniffing dog—

conduct that the Supreme Court of the United States has held is not a search when the

3
   The Jardines Court distinguished between trespasses that implicate the Fourth
Amendment and those that do not. For instance, police may trespass and search in open
fields without violating the Fourth Amendment because “an open field . . . is not one of
those protected areas enumerated in the Fourth Amendment.” Jones, 565 US at 411,
citing Oliver v United States, 466 US 170, 177; 104 S Ct 1735; 80 L Ed 2d 214 (1984).
But because the curtilage is part of the home, Oliver, 466 US at 180, and homes are
protected by the Fourth Amendment, trespassing on the curtilage implicates Fourth
Amendment protections.



                                             7
police have not trespassed. Id. at ___; 133 S Ct at 1414; Illinois v Caballes, 543 US 405,

410; 125 S Ct 834; 160 L Ed 2d 842 (2005) (holding that a dog sniff conducted during a

lawful traffic stop did not implicate legitimate privacy interests). Similarly, in Jones, the

information-gathering was the tracking of the defendant’s location on public streets—

conduct that the Supreme Court has also held is not a search when the police have not

trespassed. Jones, 565 US at 408 n 5; United States v Knotts, 460 US 276, 285; 103 S Ct

1081; 75 L Ed 2d 55 (1983) (holding that a person traveling in an automobile on public

roads has no reasonable expectation of privacy in his or her location). But information-

gathering that is not a search nevertheless becomes a search when it is combined with a

trespass on Fourth-Amendment-protected property. 4

       In Jardines, the majority and dissenting opinions address in dicta one issue that is

particularly relevant here.    In his dissent, Justice Alito noted that, “as a general

matter, . . . a visitor [may not] come to the front door in the middle of the night without

an express invitation.” Jardines, 569 US at ___; 133 S Ct at 1422 (Alito, J., dissenting).

In response, the majority opinion reasoned that the dissent “quite rightly” relied on the

fact that a nighttime knock would be alarming in concluding that nightime visits would

be outside the scope of the implied license. Id. at ___; 133 S Ct at 1416 n 3 (opinion of

the Court) (“We think a typical person would find it a cause for great alarm (the kind of



4
  For example, looking into the windows of a home from a sidewalk or other public area
is not a search. But it is information-gathering, such that, if the police trespass on the
home’s curtilage and peer through the windows from that vantage point, they have
conducted a search. The trespass converts conduct that would not otherwise constitute a
search into a search.



                                             8
reaction the dissent quite rightly relies upon to justify its no-night-visits rule) to find a

stranger snooping about his front porch with or without a dog.”) (citation, quotation

marks, and emphasis omitted). Thus, the Jardines Court apparently agreed, albeit in

dicta, that a nighttime visit would be outside the scope of the implied license (and thus a

trespass).

       We believe, as the Supreme Court suggested in Jardines, that the scope of the

implied license to approach a house and knock is time-sensitive. Id. at ___; 133 S Ct at

1416 n 3; id. at ___; 133 S Ct at 1422 (Alito, J., dissenting). Just as there is no implied

license to bring a drug-sniffing dog to someone’s front porch, there is generally no

implied license to knock at someone’s door in the middle of the night. See id. at ___; 133

S Ct at 1416 (opinion of the Court) (“There is no customary invitation to do that.”). This

custom was apparent to the investigating officers in this case. KANET officers testified

candidly that it would be inappropriate for Girl Scouts or other visitors to knock on the

door in the middle of the night, but evidently the officers believed that they were not

bound by these customs. 5     But a knock and talk is not considered a governmental

intrusion precisely because its contours are defined by what anyone may do. King, 563

US at 469 (“When law enforcement officers who are not armed with a warrant knock on

a door, they do no more than any private citizen might do.”). When the officers stray



5
  In fact, multiple KANET members testified that they performed knock and talks in the
middle of the night on a regular basis. Roetman testified that “[j]ust because it hits the
stroke of midnight doesn’t mean our case stops and we don’t keep going to people’s
homes, whether it’s a marijuana case or an armed robbery. . . . I don’t know what you’re
getting at.”



                                             9
beyond what any private citizen might do, they have strayed beyond the bounds of a

permissible knock and talk; in other words, the officers are trespassing. That is what

happened here. The reasoning that leads us to conclude that these visits were outside the

scope of the implied license is not nuanced or complicated. As the Jardines Court aptly

explained, Girl Scouts and trick-or-treaters regularly manage to abide by the terms of the

implied license. See Jardines, 569 US at ___; 133 S Ct at 1415 (“Complying with the

terms of that traditional invitation does not require fine-grained legal knowledge; it is

generally managed without incident by the Nation’s Girl Scouts and trick-or-treaters.”).

And, as any Girl Scout knows, the “background social norms that invite a visitor to the

front door,” id. at ___; 133 S Ct at 1416, typically do not extend to a visit in the middle of

the night. See United States v Lundin, 817 F3d 1151, 1159 (CA 9, 2016) (“[U]nexpected

visitors are customarily expected to knock on the front door of a home only during

normal waking hours.”). Thus, we hold that the police were trespassing when they

approached the defendants’ homes. 6

       The Court of Appeals majority reasoned that the implied license extended to

midnight visitors seeking emergency assistance or delivering the newspaper and therefore

it extended, too, to the police conduct here.         We find these examples unhelpful.

Newspaper delivery services have express permission to be on the property; therefore,



6
  We need not decide precisely what time the implied license to approach begins and
ends. In these cases, there were no circumstances that would lead a reasonable member
of the public to believe that the occupants of the respective homes welcomed visitors at
4:00 a.m. or 5:30 a.m. Accordingly, we believe it is clear that these approaches were
outside the scope of the implied license.



                                             10
their conduct is irrelevant when considering the implied license to approach a house. 7

And the fact that a visitor may approach a home in an emergency does not mean that a

visitor who is not in an emergency may approach. Emergencies justify conduct that

would otherwise be unacceptable; they are exceptions to the rule, not the rule. 8 Because

we conclude that the implied scope of the license does not extend to these predawn

approaches, we hold that the police were trespassing.

       Having concluded that the police conduct was a trespass on Fourth-Amendment-

protected property, we next turn to whether the police were seeking “to find something or

to obtain information,” such that the Fourth Amendment is implicated. Jones, 565 US at

408 n 5. A police officer walking through a neighborhood who takes a shortcut across

the corner of a homeowner’s lawn has trespassed. Yet that officer has not violated the

Fourth Amendment because, without some information-gathering, no search has

occurred. In these cases, however, the police were seeking information; therefore, their

conduct implicated the Fourth Amendment.         The KANET officers were not simply

cutting across the defendants’ lawns as a shortcut, stopping by to drop off a get-well-soon

basket, or visiting the homes to regretfully inform the defendants that a loved one had



7
  Moreover, most newspaper delivery services have permission to leave newspapers on
the property, not to approach the house and knock. Most homeowners would be
surprised—and likely indignant—if their newspaper delivery person rang the bell and
knocked for several minutes at 5:00 a.m. rather than simply leaving the paper.
8
  See Ploof v Putnam, 81 Vt 471; 71 A 188, 189 (1908) (“It is clear that an entry upon the
land of another may be justified by necessity . . . .”); Vincent v Lake Erie Transp Co, 109
Minn 456, 460; 124 NW 221 (1910) (holding that trespass onto the property of another
may be justified by necessity).



                                            11
been injured in an accident. The officers approached each house to obtain information

about the marijuana butter they suspected each defendant possessed.         This intent is

sufficient to satisfy the information-gathering prong of the Jones test.

       That the officers intended to get permission to search for the marijuana butter does

not alter our analysis. We agree with the prosecution that, as King established and

Jardines affirmed, “it is not a Fourth Amendment search to approach the home in order to

speak with the occupant, because all are invited to do that.         The mere purpose of

gathering information in the course of engaging in that permitted conduct does not cause

it to violate the Fourth Amendment.” Jardines, 569 US at ___; 133 S Ct at 1416 n 4

(citations, quotation marks, and emphasis omitted), citing King, 563 US at 469-470. True

enough; approaching a home with the purpose of gathering information is not, standing

alone, a Fourth Amendment search. King, 563 US at 469-470. But, as noted above,

when “conjoined” with a trespass, information-gathering—which need not qualify as a

search, standing alone—is all that is required to turn the trespass into a Fourth

Amendment search. Jones, 565 US at 408 n 5. The officers here plainly approached the

defendants’ homes for the purpose of gathering information. 9

       The fact that the officers sought to gather their information by speaking with the

homeowners rather than by peering through windows or rummaging through the bushes

is irrelevant. What matters is that they sought to gather information by way of a trespass

on Fourth-Amendment-protected property.           That they did.   The approaches of the


9
  Detective Todd Butler, one of the KANET members who participated in the knock and
talk, testified that “[t]he only reason we were there is because of the drugs.”



                                             12
defendants’ homes were not valid knock and talks, but rather searches under the Fourth

Amendment. And because the police did not have warrants or any other exception to the

warrant requirement, we conclude that the approaches violated the Fourth Amendment.

                                      B. CONSENT

       This is not the end of the analysis, however. During the invalid knock and talks,

each defendant consented to a search of his respective home. Consent searches, when

voluntary, are an exception to the warrant requirement. Schneckloth v Bustamonte, 412

US 218, 219; 93 S Ct 2041; 36 L Ed 2d 854 (1973). The voluntariness question turns on

whether a reasonable person would, under the totality of the circumstances, feel able to

choose whether to consent. Id. at 227.

       The defendants believe that their consent, even if voluntary, is irrelevant, given the

contemporaneous Fourth Amendment violation.           The prosecution views the Fourth

Amendment violation as irrelevant, given the subsequent consent. Neither is correct.

The defendants’ consent is not irrelevant—but neither is it evaluated separately from the

illegal searches.

       Rather, the defendants’ consent—even if voluntary—is invalid unless it is

sufficiently attenuated from the warrantless search. The Supreme Court has repeatedly

held that evidence obtained through an illegal search or seizure is tainted by that initial

illegality unless sufficiently attenuated from it. See Wong Sun v United States, 371 US

471, 486; 83 S Ct 407; 9 L Ed 2d 441 (1963) (holding that evidence acquired after an

illegal search must be suppressed unless the government shows that its acquisition of the

evidence resulted from “an intervening independent act of free will” sufficient “to purge




                                             13
the primary taint of the unlawful invasion”). That analysis has been applied to both

consensual statements and—particularly relevant here—consensual searches. Brown v

Illinois, 422 US 590, 602; 95 S Ct 2254; 45 L Ed 2d 416 (1975) (holding that when an

inculpatory statement follows an unlawful arrest, a finding of voluntariness does not

obviate the need to make a separate Fourth Amendment determination as to whether the

statement was “ ‘sufficiently an act of free will to purge the primary taint’ ”), quoting

Wong Sun, 371 US at 486; Florida v Royer, 460 US 491, 507-508; 103 S Ct 1319; 75 L

Ed 2d 229 (1983) (“Because we affirm the . . . conclusion that Royer was being illegally

detained when he consented to the search of his luggage, we agree that the consent was

tainted by the illegality and was ineffective to justify the search.”).

       Thus, even when consent is voluntary, if it is not attenuated from the

unconstitutional search, the evidence must be suppressed. Wong Sun, 371 US at 486;

Brown, 422 US at 602; Royer, 460 US at 507-508. The Supreme Court has identified

three factors to be considered in determining whether consent is sufficiently attenuated:

(1) the temporal proximity of the illegal act and the alleged consent, (2) the presence of

intervening circumstances, and (3) the purpose and flagrancy of the official misconduct.

Brown, 422 US at 603-604.

       In these cases, because the trial court determined that there was no Fourth

Amendment violation, it did not consider whether the subsequent consent was attenuated

from the illegality. Therefore, we remand to that court for consideration of that question

in the first instance.




                                              14
                                   III. CONCLUSION

       A proper application of Fourth Amendment jurisprudence requires us to reverse

the Court of Appeals. Because these knock and talks were outside the scope of the

implied license, the officers trespassed on Fourth-Amendment-protected property. And

because the officers trespassed while seeking information, they performed illegal

searches. Finally, because of these illegal searches, the defendants’ consent—even if

voluntary—is nonetheless invalid unless it was sufficiently attenuated from the illegality.

We therefore reverse the Court of Appeals and remand these cases to the Kent Circuit

Court to determine whether the defendants’ consent to search was attenuated from the

officers’ illegal search.


                                                       Bridget M. McCormack
                                                       Stephen J. Markman
                                                       Brian K. Zahra
                                                       David F. Viviano
                                                       Richard H. Bernstein
                                                       Joan L. Larsen
                                                       Kurtis T. Wilder




                                            15

```

---

## GROUP: _overhaul2/lake/cases/People v. Hughes.json  (`lake-record`, 3 assertions)

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
{"assertion_id": "4e1fb4aa53b9f704", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-35", "record_id": "People v. Hughes"}, "payload": {"fragment": "#:~:text=reasonably%20limit%20the%20scope%20of", "page": null, "pin_id": "pin-35", "pinpoint_status": "slip-only", "quote": "reasonably limit the scope of their searches to evidence related to the criminal activity alleged in the warrant and not employ that authorization as a basis for seizing and searching digital data in the manner of a general warrant in search of evidence of any and all criminal activity.", "quote_fidelity": "matched", "record_id": "People v. Hughes", "star_marker": null}}
{"assertion_id": "fe962bbfaa4f5583", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-36", "record_id": "People v. Hughes"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-36", "pinpoint_status": "slip-only", "quote": "--- # People v. Hughes *506 Mich. 512, 958 N.W.2d 98 (2020)* · Michigan Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Hughes's cell phone was seized and its data extracted pursuant to a warrant authorizing a search for evidence of **drug trafficking**. About a month later, the prosecutor in a separate **armed-robbery** case asked a detective to search the same data for the robbery victims' names and phone numbers; that search turned up calls and texts tying Hughes to the robbery. Convicted of armed robbery, Hughes argued the robbery evidence exceeded the drug-trafficking warrant. ## Issue Whether officers violated the Fourth Amendment by searching lawfully seized cell-phone data for evidence of a different crime (armed robbery) than the one for which the warrant issued (drug trafficking). ## Rule A warrant to search digital data authorizes review only to the extent reasonably consistent with the warrant's scope; there is no per se rule permitting review of the entire contents.", "quote_fidelity": "mismatch", "record_id": "People v. Hughes", "star_marker": null}}
{"assertion_id": "b6e373bc45c2ed4a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "People v. Hughes"}, "payload": {"as_of_content": "2020-12-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "People v. Hughes", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
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
