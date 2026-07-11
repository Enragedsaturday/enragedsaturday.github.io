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

## GROUP: _overhaul2/lake/cases/New York v. Class.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "New York v. Class"
type: case
citation: "475 U.S. 106 (1986)"
parallel_cite: "106 S. Ct. 960; 89 L. Ed. 2d 81; 54 U.S.L.W. 4178"
neutral_cite: 1986 U.S. LEXIS 5
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-02-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-02-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New York v. Class
  varies_by_point: false
  scope_note: "Good law; no reasonable expectation of privacy in a VIN required by law to be visible, and a minimal intrusion to read it during a lawful traffic stop is reasonable."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111600/new-york-v-class/"
  cluster_id: 111600
  opinion_id: 9430353
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
  - page: "[[Plain View Doctrine]]"
    role: "Related (cross-doctrine)"
related: ["[[Pennsylvania v. Mimms]]", "[[Delaware v. Prouse]]", "[[South Dakota v. Opperman]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "vehicle", "vin", "traffic-stop", "reasonable-expectation-of-privacy"]
holding: "There is no reasonable expectation of privacy in a VIN required by law to be visible; reaching into the car to move papers obscuring the VIN was a minimal but reasonable search."
lake:
  record_id: New York v. Class
  status: verified
  projected_at: 2026-07-09
---

# New York v. Class

*475 U.S. 106 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers stopped Class for two traffic violations. When Class exited the car, an officer reached into the passenger compartment to move papers on the dashboard that obscured the Vehicle Identification Number (VIN). In doing so he saw the handle of a gun protruding from under the seat. Class moved to suppress the gun, arguing the reach-in was an unconstitutional search.

## Issue
Whether an officer's entry into the passenger compartment of a lawfully stopped car to move papers obscuring the VIN — a number required by law to be visible — violates the Fourth Amendment.

## Rule
There is no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the VIN itself: "because of the important role played by the VIN in the pervasive governmental regulation of the automobile and the efforts by the Federal Government to ensure that the VIN is placed in plain view, we hold that there was no reasonable expectation of privacy in the VIN." — 475 U.S. at 114. ^pin-114

The minimal intrusion to read it was reasonable: "We hold that this search was sufficiently unintrusive to be constitutionally permissible in light of the lack of a reasonable expectation of privacy in the VIN and the fact that the officers observed respondent commit two traffic violations." — [*Id.* at 119](https://www.courtlistener.com/opinion/111600/new-york-v-class/#:~:text=We%20hold%20that%20this%20search). ^pin-119

## Application
The VIN is required by federal regulation to be visible from outside the car, so Class had no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in it, and placing papers over it did not create one. Although reaching into the passenger compartment was itself a minimal "search" of a space that retains some Fourth Amendment protection, it was reasonable here: the officers had observed two traffic violations, and had Class stayed in the car they could simply have asked him to move the papers. Because the intrusion was limited to the area where the VIN sits and was justified by the traffic violations, it was permissible — and the gun seen in the course of that lawful, minimal entry was admissible.

## Conclusion
Reading the obscured VIN by a brief reach into the car was a reasonable, minimal search; the gun was admissible. There is no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a legally mandated, publicly visible VIN.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Builds on the diminished vehicle-privacy line ([[South Dakota v. Opperman]]) and the traffic-stop officer-safety/authority cases ([[Pennsylvania v. Mimms]], [[Delaware v. Prouse]]).

## Appears on
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*
- [[Traffic Stops]] — *Related (cross-doctrine)*
- [[Plain View Doctrine]] — *Related (cross-doctrine)*

## Sources
- *New York v. Class*, 475 U.S. 106 (1986) — https://www.courtlistener.com/opinion/111600/new-york-v-class/ — pinpoints: 114, 119.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5f9b872173d5b1f7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "New York v. Class"}, "payload": {"all": [{"cite": "475 U.S. 106", "page": "106", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "475"}, {"cite": "106 S. Ct. 960", "page": "960", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "106"}, {"cite": "89 L. Ed. 2d 81", "page": "81", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "1986 U.S. LEXIS 5", "page": "5", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1986"}, {"cite": "54 U.S.L.W. 4178", "page": "4178", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "54"}], "display": "475 U.S. 106", "official": {"cite": "475 U.S. 106", "page": "106", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "475"}, "official_selection_present": true, "record_id": "New York v. Class"}}
{"assertion_id": "1c85cb4ffc5aa7e9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-114", "record_id": "New York v. Class"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-114", "pinpoint_status": "slip-only", "quote": "--- # New York v. Class *475 U.S. 106 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers stopped Class for two traffic violations. When Class exited the car, an officer reached into the passenger compartment to move papers on the dashboard that obscured the Vehicle Identification Number (VIN). In doing so he saw the handle of a gun protruding from under the seat. Class moved to suppress the gun, arguing the reach-in was an unconstitutional search. ## Issue Whether an officer's entry into the passenger compartment of a lawfully stopped car to move papers obscuring the VIN — a number required by law to be visible — violates the Fourth Amendment. ## Rule There is no reasonable expectation of privacy in the VIN itself:", "quote_fidelity": "mismatch", "record_id": "New York v. Class", "star_marker": null}}
{"assertion_id": "a3d380ca14ea7f66", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-119", "record_id": "New York v. Class"}, "payload": {"fragment": "#:~:text=We%20hold%20that%20this%20search", "page": null, "pin_id": "pin-119", "pinpoint_status": "star-verified", "quote": "We hold that this search was sufficiently unintrusive to be constitutionally permissible in light of the lack of a reasonable expectation of privacy in the VIN and the fact that the officers observed respondent commit two traffic violations.", "quote_fidelity": "matched", "record_id": "New York v. Class", "star_marker": "119"}}
{"assertion_id": "67a66bd17d89c4db", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "New York v. Class"}, "payload": {"as_of_content": "1986-02-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "New York v. Class", "scope_note": "Good law; no reasonable expectation of privacy in a VIN required by law to be visible, and a minimal intrusion to read it during a lawful traffic stop is reasonable.", "varies_by_point": false}}
```

### lake record — New York v. Class

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Class",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Class",
    "case_name_short": "Class",
    "case_name_full": "New York v. Class",
    "input_case_name": "New York v. Class",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-02-25",
    "year": 1986,
    "docket": null,
    "cluster_id": 111600,
    "lead_opinion_id": 9430353,
    "sibling_ids": [
      111600,
      9430353,
      9430354,
      9430355,
      9430356
    ],
    "absolute_url": "/opinion/111600/new-york-v-class/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "475 U.S. 106",
      "volume": "475",
      "reporter": "U.S.",
      "page": "106",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 960",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "960",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 81",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "81",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4178",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4178",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 5",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "5",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "475 U.S. 106",
        "volume": "475",
        "reporter": "U.S.",
        "page": "106",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 960",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "960",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 81",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "81",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 5",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "5",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4178",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4178",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "475 U.S. 106",
    "official_selection": {
      "court_class": "scotus",
      "selected": "475 U.S. 106",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-114",
      "page": null,
      "quote": "--- # New York v. Class *475 U.S. 106 (1986)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers stopped Class for two traffic violations. When Class exited the car, an officer reached into the passenger compartment to move papers on the dashboard that obscured the Vehicle Identification Number (VIN). In doing so he saw the handle of a gun protruding from under the seat. Class moved to suppress the gun, arguing the reach-in was an unconstitutional search. ## Issue Whether an officer's entry into the passenger compartment of a lawfully stopped car to move papers obscuring the VIN \u2014 a number required by law to be visible \u2014 violates the Fourth Amendment. ## Rule There is no reasonable expectation of privacy in the VIN itself:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-119",
      "page": null,
      "quote": "We hold that this search was sufficiently unintrusive to be constitutionally permissible in light of the lack of a reasonable expectation of privacy in the VIN and the fact that the officers observed respondent commit two traffic violations.",
      "star_marker": "119",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 33755,
      "fragment": "#:~:text=We%20hold%20that%20this%20search",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-02-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New York v. Class",
    "varies_by_point": false,
    "scope_note": "Good law; no reasonable expectation of privacy in a VIN required by law to be visible, and a minimal intrusion to read it during a lawful traffic stop is reasonable.",
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
        "journal_ref": "New York v. Class:lane1_negative"
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
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Thomas",
          "cluster_id": 1036878,
          "cite": [
            "726 F.3d 1086",
            "2013 U.S. App. LEXIS 16413",
            "2013 WL 4017239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Werra",
          "cluster_id": 212993,
          "cite": [
            "638 F.3d 326",
            "2011 U.S. App. LEXIS 5741",
            "2011 WL 982384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Friedman v. Boucher",
          "cluster_id": 3064806,
          "cite": [
            "580 F.3d 847",
            "2009 WL 2857199"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Friedman v. Boucher",
          "cluster_id": 1459727,
          "cite": [
            "568 F.3d 1119",
            "2009 U.S. App. LEXIS 13440",
            "2009 WL 1758366"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed, 23221 (6-27-2007)",
          "cluster_id": 4002592,
          "cite": [
            "2007 Ohio 3243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Anderson",
          "cluster_id": 5828324,
          "cite": [
            "17 A.D.3d 166",
            "793 N.Y.S.2d 353",
            "2005 N.Y. App. Div. LEXIS 3731"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Alvarez",
          "cluster_id": 6231565,
          "cite": [
            "308 A.D.2d 184",
            "764 N.Y.S.2d 42",
            "2003 N.Y. App. Div. LEXIS 9160"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Condon v. Reno",
          "cluster_id": 2967145,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. DeLaCruz",
          "cluster_id": 6151173,
          "cite": [
            "242 A.D.2d 410",
            "662 N.Y.S.2d 300",
            "1997 N.Y. App. Div. LEXIS 8505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES of America, Plaintiff-Appellee, v. Jeffrey Howard VAN POYCK, Defendant-Appellant",
          "cluster_id": 713090,
          "cite": [
            "77 F.3d 285",
            "96 Cal. Daily Op. Serv. 1091",
            "96 Daily Journal DAR 1850",
            "1996 U.S. App. LEXIS 2518",
            "1996 WL 69841"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morgan v. State",
          "cluster_id": 1713874,
          "cite": [
            "906 S.W.2d 620",
            "1995 WL 515837"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harris v. Reed",
          "cluster_id": 112205,
          "cite": [
            "103 L. Ed. 2d 308",
            "109 S. Ct. 1038",
            "489 U.S. 255",
            "1989 U.S. LEXIS 1044",
            "57 U.S.L.W. 4224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walter v. State",
          "cluster_id": 1755500,
          "cite": [
            "28 S.W.3d 538",
            "2000 Tex. Crim. App. LEXIS 84",
            "2000 WL 1348504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lidster",
          "cluster_id": 131154,
          "cite": [
            "157 L. Ed. 2d 843",
            "124 S. Ct. 885",
            "540 U.S. 419",
            "2004 U.S. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bailey v. United States",
          "cluster_id": 820749,
          "cite": [
            "185 L. Ed. 2d 19",
            "133 S. Ct. 1031",
            "568 U.S. 186",
            "2013 U.S. LEXIS 1075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Venham",
          "cluster_id": 3973805,
          "cite": [
            "645 N.E.2d 831",
            "96 Ohio App. 3d 649",
            "1994 Ohio App. LEXIS 4118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis Dayton Holt",
          "cluster_id": 774866,
          "cite": [
            "264 F.3d 1215",
            "2001 Colo. J. C.A.R. 4452",
            "2001 U.S. App. LEXIS 19759",
            "2001 WL 1013251"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terry King and Valerie Jean Burdex",
          "cluster_id": 604813,
          "cite": [
            "990 F.2d 1552",
            "1993 U.S. App. LEXIS 6056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jacoby, T., Aplt.",
          "cluster_id": 4429713,
          "cite": [
            "170 A.3d 1065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Spencer Ray Tilmon",
          "cluster_id": 666028,
          "cite": [
            "19 F.3d 1221",
            "1994 U.S. App. LEXIS 5598",
            "1994 WL 93939"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Torres",
          "cluster_id": 5689682,
          "cite": [
            "74 N.Y.2d 224",
            "544 N.Y.S.2d 796",
            "543 N.E.2d 61",
            "1989 N.Y. LEXIS 886"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. MacOn",
          "cluster_id": 1681383,
          "cite": [
            "957 So. 2d 1280",
            "2007 WL 1575004"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 5689813,
          "cite": [
            "74 N.Y.2d 773",
            "545 N.Y.S.2d 90",
            "543 N.E.2d 733",
            "1989 N.Y. LEXIS 882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 1175765,
          "cite": [
            "721 P.2d 1357",
            "301 Or. 268",
            "1986 Ore. LEXIS 1453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Stroud",
          "cluster_id": 1390081,
          "cite": [
            "720 P.2d 436",
            "106 Wash. 2d 144",
            "1986 Wash. LEXIS 1204"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111600 OR 9430353 OR 9430354 OR 9430355 OR 9430356) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03OTIzNzQ0MDAwMDAmcz02ODcyMjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111600+OR+9430353+OR+9430354+OR+9430355+OR+9430356%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(111600 OR 9430353 OR 9430354 OR 9430355 OR 9430356)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjAmcz0yOTY4Nzg4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111600+OR+9430353+OR+9430354+OR+9430355+OR+9430356%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111600 OR 9430353 OR 9430354 OR 9430355 OR 9430356)",
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
    "complete_query": "cites:(111600 OR 9430353 OR 9430354 OR 9430355 OR 9430356)",
    "indexed_citing_opinions": 433,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111600,
        "count": 374,
        "count_source": "search"
      },
      {
        "opinion_id": 9430353,
        "count": 71,
        "count_source": "search"
      },
      {
        "opinion_id": 9430354,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430355,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430356,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 729,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-class.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcyNTc2NSZzPTQ4ODQwNDgmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111600+OR+9430353+OR+9430354+OR+9430355+OR+9430356%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111600,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 2566781,
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
    "date_created": "2026-07-05T15:38:49Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:43:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Class

```
<opinion type="majority">
<author id="b189-10">Justice O’Connor</author>
<p id="A09">delivered the opinion of the Court.</p>
<p id="b189-11">In this case, we must decide whether, in order to observe a Vehicle Identification Number (VIN) generally visible from outside an automobile, a police officer may reach into the passenger compartment of a vehicle to move papers obscuring the VIN after its driver has been stopped for a traffic violation and has exited the car. We hold that, in these circumstances, the police officer’s action does not violate the Fourth Amendment.</p>
<p id="b189-12">I</p>
<p id="b189-13">On the afternoon of May 11, 1981, New York City police officers Lawrence Meyer and William McNamee observed re<page-number citation-index="1" label="108">*108</page-number>spondent Benigno Class driving above the speed limit in a car with a cracked windshield. Both driving with a cracked windshield and speeding are traffic violations under New York law. See N. Y. Veh. &amp; Traf. Law §§375(22), 1180(d) (McKinney 1970). Respondent followed the officers’ ensuing directive to pull over. Respondent then emerged from his car and approached Officer Meyer. Officer McNamee went directly to respondent’s vehicle. Respondent provided Officer Meyer with a registration certificate and proof of insurance, but stated that he had no driver’s license.</p>
<p id="b190-5">Meanwhile, Officer McNamee opened the door of respondent’s car to look for the VIN, which is located on the left doorjamb in automobiles manufactured before 1969. When the officer did not find the VIN on the doorjamb, he reached into the interior of respondent’s car to move some papers obscuring the area of the dashboard where the VIN is located in later model automobiles. In doing so, Officer McNamee saw the handle of a gun protruding about one inch from underneath the driver’s seat. The officer seized the gun, and respondent was promptly arrested. Respondent was also issued summonses for his traffic violations.</p>
<p id="b190-6">It is undisputed that the police officers had no reason to suspect that respondent’s car was stolen, that it contained contraband, or that respondent had committed an offense other than the traffic violations. Nor is it disputed that respondent committed the traffic violations with which he was charged, and that, as of the day of the arrest, he had not been issued a valid driver’s license.</p>
<p id="b190-7">After the state trial court denied a motion to suppress the gun as evidence, respondent was convicted of criminal possession of a weapon in the third degree. See N. Y. Penal Law § 265.02(4) (McKinney 1980). The Appellate Division of the New York Supreme Court upheld the conviction without opinion. 97 App. Div. 2d 741, 468 N. Y. S. 2d 892 (1983). The New York Court of Appeals reversed. It reasoned that the police officer’s “intrusion . . . was undertaken to obtain <page-number citation-index="1" label="109">*109</page-number>information and it exposed . . . hidden areas” of the car, and “therefore constituted a search.” 63 N. Y. 2d 491, 495, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1011" aria-description="Citation for case: People v. Class">472 N. E. 2d 1009, 1011</a></span> (1984). Although it recognized that a search for a VIN generally involves a minimal intrusion because of its limited potential locations, and agreed that there is a compelling law enforcement interest in positively identifying vehicles involved in accidents or automobile thefts, the court thought it decisive that the facts of this case “reveal no reason for the officer to suspect other criminal activity [besides the traffic infractions] or to act to protect his own safety.” <em>Id., </em>at 495-496, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1012" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1012</a></span>. The state statutory provision that authorizes officers to demand that drivers reveal their VIN “provided no justification for the officer’s entry of [respondent’s] car.” <em>Id., </em>at 497, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1013" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1013</a></span>. If the officer had taken advantage of that statute and asked to see the VIN, respondent could have moved the papers away himself and no intrusion would have occurred. In the absence of any justification for the search besides the traffic infractions, the New York Court of Appeals ruled that the gun must be excluded from evidence.</p>
<p id="b191-5">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./471/1003/">471 U. S. 1003</a></span> (1985), and now reverse.</p>
<p id="b191-6">II</p>
<p id="b191-7">Respondent asserts that this Court is without jurisdiction to hear this case because the decision of the New York Court of Appeals rests on an adequate and independent state ground. We disagree.</p>
<p id="b191-8">The opinion of the New York Court of Appeals mentions the New York Constitution but once, and then only in direct conjunction with the United States Constitution. 63 N. Y. 2d, at 493, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1010" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1010</a></span>. Cf. <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1043" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1043</a></span> (1983). The opinion below makes use of both federal and New York cases in its analysis, generally citing both for the same proposition. See, <em>e. g., </em>63 N. Y. 2d, at 494, 495, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1011" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1011</a></span>. The opinion lacks the requisite “plain statement” that it rests on state grounds. <page-number citation-index="1" label="110">*110</page-number><em>Michigan </em>v. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1042" aria-description="Citation for case: Michigan v. Long"><em>Long, supra, </em>at 1042, 1044</a></span>. Accordingly, our holding in <em>Michigan </em>v. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span> </em>is directly applicable here:</p>
<blockquote id="b192-5">“[WJhen ... a state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion, we will accept as the most reasonable explanation that the state court decided the case the way it did because it believed that federal law required it to do so.” <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1040-1041</a></span>.</blockquote>
<p id="b192-6">See also <em>California </em>v. <em>Carney, </em><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#389" aria-description="Citation for case: California v. Carney">471 U. S. 386, 389, n. 1</a></span> (1985).</p>
<p id="b192-7">Respondent’s claim that the opinion below rested on independent and adequate state <em>statutory </em>grounds is also without merit. The New York Court of Appeals did not hold that §401 of New York’s Vehicle and Traffic Law prohibited the search at issue here, but, in rejecting an assertion of petitioner, merely held that § 401 “provided no justification” for a search. 63 N. Y. 2d, at 497, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1013" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1013</a></span> (emphasis added). In determining that the police officer’s action was prohibited, the court below looked to the Federal Constitution, not the State’s statute. Moreover, New York adheres to the general rule that, when statutory construction can resolve a case, courts should not decide constitutional issues. See <em>Ashwander </em>v. <em>TV A, </em><span class="citation" data-id="9418878"><a href="/opinion/102605/ashwander-v-tennessee-valley-authority/#346" aria-description="Citation for case: Ashwander v. Tennessee Valley Authority">297 U. S. 288, 346-347</a></span> (1936) (Brandéis, J., concurring); <em>In re Peters </em>v. <em>New York City Housing Authority, </em><span class="citation" data-id="2566781"><a href="/opinion/2566781/matter-of-peters-v-new-york-city-hous-auth/#527" aria-description="Citation for case: MATTER OF PETERS v. New York City Hous. Auth.">307 N. Y. 519, 527</a></span>, <span class="citation" data-id="2566781"><a href="/opinion/2566781/matter-of-peters-v-new-york-city-hous-auth/#531" aria-description="Citation for case: MATTER OF PETERS v. New York City Hous. Auth.">121 N. E. 2d 529, 531</a></span> (1954). Since the New York Court of Appeals discussed both statutory and constitutional grounds, we may infer that the court believed the statutory issue insufficient to resolve the case. The discussion of the statute therefore could not have constituted an independent and adequate state ground.</p>
<p id="b193-10"><page-number citation-index="1" label="111">*111</page-number>i — I <em>h-i</em></p>
<p id="b193-3">A</p>
<p id="b193-4">The officer here, after observing respondent commit two traffic violations and exit the car, attempted to determine the VIN of respondent’s automobile. In reaching to remove papers obscuring the VIN, the officer intruded into the passenger compartment of the vehicle.</p>
<p id="b193-5">The VIN consists of more than a dozen digits, unique to each vehicle and required on all cars and trucks. See <span class="citation no-link">49 CFR §571.115</span> (1984). The VIN is roughly analogous to a serial number, but it can be deciphered to reveal not only the place of the automobile in the manufacturer’s production run, but also the make, model, engine type, and place of manufacture of the vehicle. See § 565.4.</p>
<p id="b193-6">The VIN is a significant thread in the web of regulation of the automobile. See generally <span class="citation no-link">43 Fed. Reg. 2189</span> (1978). The ease with which the VIN allows identification of a particular vehicle assists the various levels of government in many ways. For the Federal Government, the VIN improves the efficacy of recall campaigns, and assists researchers in determining the risks of driving various makes and models of automobiles. In combination with state insurance laws, the VIN reduces the number of those injured in accidents who go uncompensated for lack of insurance. In conjunction with the State’s registration requirements and safety inspections, the VIN helps to ensure that automobile operators are driving safe vehicles. By making automobile theft more difficult, the VIN safeguards not only property but also life and limb. See <span class="citation no-link">33 Fed. Reg. 10207</span> (1968) (noting that stolen vehicles are disproportionately likely to be involved in automobile accidents).</p>
<p id="b193-7">To facilitate the VIN’s usefulness for these laudable governmental purposes, federal law requires that the VIN be placed in the plain view of someone <em>outside </em>the automobile:</p>
<blockquote id="b194-4"><page-number citation-index="1" label="112">*112</page-number>“The VIN for passenger cars [manufactured after 1969] shall be located inside the passenger compartment. It shall be readable, without moving any part of the vehicle, through the vehicle glazing under daylight lighting conditions by an observer having 20/20 vision (Snellen) whose eye point is located <em>outside the vehicle </em>adjacent to the left windshield pillar. Each character in the VIN subject to this paragraph shall have a minimum height of 4 mm.” <span class="citation no-link">49 CFR §571.115</span> (S4.6) (1984) (emphasis added).</blockquote>
<p id="b194-5">In <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#658" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 658</a></span> (1979), we recognized the “vital interest” in highway safety and the various programs that contribute to that interest. In light of the important interests served by the VIN, the Federal and State Governments are amply justified in making it a part of the web of pervasive regulation that surrounds the automobile, and in requiring its placement in an area ordinarily in plain view from outside the passenger compartment.</p>
<p id="b194-6">B</p>
<p id="b194-7">A citizen does not surrender all the protections of the Fourth Amendment by entering an automobile. See <em>Delaware </em>v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 663</a></span>; <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#269" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 269</a></span> (1973). Nonetheless, the State’s intrusion into a particular area, whether in an automobile or elsewhere, cannot result in a Fourth Amendment violation unless the area is one in which there is a “constitutionally protected reasonable expectation of privacy.” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 360</a></span> (1967) (Harlan, J., concurring). See <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#177" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 177-180</a></span> (1984); <em>Maryland </em>v. <em>Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#469" aria-description="Citation for case: Maryland v. MacOn">472 U. S. 463, 469</a></span> (1985).</p>
<p id="b194-8">The Court has recognized that the physical characteristics of an automobile and its use result in a lessened expectation of privacy therein:</p>
<blockquote id="b194-9">“One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom <page-number citation-index="1" label="113">*113</page-number>serves as one’s residence or as the repository of personal effects. A car has little capacity for escaping public scrutiny. It travels public thoroughfares where both its occupants and its contents are in plain view.” <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion).</blockquote>
<p id="b195-4">Moreover, automobiles are justifiably the subject of pervasive regulation by the State. Every operator of a motor vehicle must expect that the State, in enforcing its regulations, will intrude to some extent upon that operator’s privacy:</p>
<blockquote id="b195-5">“Automobiles, unlike homes, are subject to pervasive and continuing governmental regulation and controls, including periodic inspection and licensing requirements. As an everyday occurrence, police stop and examine vehicles when license plates or inspection stickers have expired, or if other violations, such as exhaust fumes or excessive noise, are noted, or if headlights or other safety equipment are not in proper working order.” <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1976).</blockquote>
<p id="b195-6">See also <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441-442</a></span> (1973); <em>California </em>v. <em>Carney, </em><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#392" aria-description="Citation for case: California v. Carney">471 U. S., at 392</a></span>.</p>
<p id="b195-7">The factors that generally diminish the reasonable expectation of privacy in automobiles are applicable <em>a fortiori </em>to the VIN. As we have discussed above, the VIN plays an important part in the pervasive regulation by the government of the automobile. A motorist must surely expect that such regulation will on occasion require the State to determine the VIN of his or her vehicle, and the individual’s reasonable expectation of privacy in the VIN is thereby diminished. This is especially true in the case of a driver who has committed a traffic violation. See <em>Delaware </em>v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 659</a></span> (“The foremost method of enforcing traffic and vehicle safety regulations ... is acting upon observed violations. <em>Vehicle stops for traffic violations occur countless times each day; and on these occasions, licenses and registration papers are subject to inspection and drivers without them will be as</em><page-number citation-index="1" label="114">*114</page-number><em>certained”) </em>(emphasis added). In addition, it is unreasonable to have an expectation of privacy in an object required by law to be located in a place ordinarily in plain view from the exterior of the automobile. The VIN’s mandated visibility makes it more similar to the exterior of the car than to the trunk or glove compartment. The exterior of a car, of course, is thrust into the public eye, and thus to examine it does not constitute a “search.” See <em>Cardwell </em>v. <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#588" aria-description="Citation for case: Cardwell v. Lewis"><em>Lewis, supra, </em>at 588-589</a></span>. In sum, because of the important role played by the VIN in the pervasive governmental regulation of the automobile and the efforts by the Federal Government to ensure that the VIN is placed in plain view, we hold that there was no reasonable expectation of privacy in the VIN.</p>
<p id="b196-5">We think it makes no difference that the papers in respondent’s car obscured the VIN from the plain view of the officer. We have recently emphasized that efforts to restrict access to an area do not generate a reasonable expectation of privacy where none would otherwise exist. See <em>Oliver </em>v. <em>United States, supra, </em>at 182-184 (placement of “No Trespassing” signs on secluded property does not create “legitimate privacy interest” in marihuana fields). Here, where the object at issue is an identification number behind the transparent windshield of an automobile driven upon the public roads, we believe that the placement of the obscuring papers was insufficient to create a privacy interest in the VIN. The mere viewing of the formerly obscured VIN was not, therefore, a violation of the Fourth Amendment.</p>
<p id="b196-6">C</p>
<p id="b196-7">The evidence that respondent sought to have suppressed was not the VIN, however, but a gun, the handle of which the officer saw from the interior of the car while reaching for the papers that covered the VIN. While the interior of an automobile is not subject to the same expectations of privacy that exist with respect to one’s home, a car’s interior as a whole is nonetheless subject to Fourth Amendment protec<page-number citation-index="1" label="115">*115</page-number>tion from unreasonable intrusions by the police. We agree with the New York Court of Appeals that the intrusion into that space constituted a “search.” 63 N. Y. 2d, at 495, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1011" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1011</a></span>. Cf. <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 653</a></span> (“[Shopping an automobile and detaining its occupants constitute a ‘seizure’. . . even though the purpose of the stop is limited and the resulting detention quite brief”). We must decide, therefore, whether this search was constitutionally permissible.</p>
<p id="b197-5">If respondent had remained in the car, the police would have been justified in asking him to move the papers obscuring the VIN. New York law authorizes a demand by officers to see the VIN, see 63 N. Y. 2d, at 496-497, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1012" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1012-1013</a></span>, and even if the state law were not explicit on this point we have no difficulty in concluding that a demand to inspect the VIN, like a demand to see license and registration papers, is within the scope of police authority pursuant to a traffic violation stop. See <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 659</a></span>. If respondent had stayed in his vehicle and acceded to such a request from the officer, the officer would not have needed to intrude into the passenger compartment. Respondent chose, however, to exit the vehicle without removing the papers that covered the VIN; the officer chose to conduct his search without asking respondent to return to the car. We must therefore decide whether the officer acted within the bounds of the Fourth Amendment in conducting the search. We hold that he did.</p>
<p id="b197-6">Keeping the driver of a vehicle in the car during a routine traffic stop is probably the typical police practice. See D. Schultz &amp; D. Hunt, Traffic Investigation and Enforcement 17 (1983). Nonetheless, out of a concern for the safety of the police, the Court has held that officers may, consistent with the Fourth Amendment, exercise their discretion to require a driver who commits a traffic violation to exit the vehicle even though they lack any particularized reason for believing the driver possesses a weapon. <em>Pennsylvania </em>v. <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#108" aria-description="Citation for case: Pennsylvania v. Mimms">434 <page-number citation-index="1" label="116">*116</page-number>U. S. 106, 108-111</a></span> (1977) <em>(per curiam). </em>While we impute to respondent no propensity for violence, and while we are conscious of the fact that respondent here voluntarily left the vehicle, the facts of this case may be used to illustrate one of the principal justifications for the discretion given police officers by <em>Pennsylvania </em>v. <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>: </em>while in the driver’s seat, respondent had a loaded pistol at hand. <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>allows an officer to guard against that possibility by requiring the driver to exit the car briefly. Clearly, <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>also allowed the officers here to detain respondent briefly outside the car that he voluntarily exited while they completed their investigation.</p>
<p id="b198-5">The question remains, however, as to whether the officers could not only effect the seizure of respondent necessary to detain him briefly outside the vehicle, but also effect a search for the VIN that may have been necessary only because of that detention. The pistol beneath the seat did not, of course, disappear when respondent closed the car door behind him. To have returned respondent immediately to the automobile would have placed the officers in the same situation that the holding in <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>allows officers to avoid — permitting an individual being detained to have possible access to a dangerous weapon and the benefit of the partial concealment provided by the car’s exterior. See <em>Pennsylvania </em>v. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms"><em>Mimms, supra, </em>at 110</a></span>. In light of the danger to the officers’ safety that would have been presented by returning respondent immediately to his car, we think the search to obtain the VIN was not prohibited by the Fourth Amendment.</p>
<p id="b198-6">The Fourth Amendment by its terms prohibits “unreasonable” searches and seizures. We have noted:</p>
<blockquote id="b198-7">“[T]here is ‘no ready test for determining reasonableness other than by balancing the need to search [or seize] against the invasion which the search [or seizure] entails.’ <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535, 536-537</a></span> (1967). And in justifying the particular intrusion the police officer must be able to point to specific and articulable facts which, taken together with <page-number citation-index="1" label="117">*117</page-number>rational inferences from those facts, justifiably warrant that intrusion.” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21</a></span> (1968) (footnote omitted) (brackets as in <em>Terry).</em></blockquote>
<p id="b199-5">This test generally means that searches must be conducted pursuant to a warrant backed by probable cause. See <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#105" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 105-109</a></span> (1965); <em>United States </em>v. <em>Karo, </em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#714" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 714-715</a></span> (1984). When a search or seizure has as its immediate object a search for a weapon, however, we have struck the balance to allow the weighty interest in the safety of police officers to justify war-rantless searches based only on a reasonable suspicion of criminal activity. See <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra;</a></span> Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972). Such searches are permissible despite their substantial intrusiveness. See <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 24-25</a></span> (search was “a severe, though brief, intrusion upon cherished personal security, and . . . must surely [have] b[een] an annoying, frightening, and perhaps humiliating experience”).</p>
<p id="b199-6">When the officer’s safety is less directly served by the detention, something more than objectively justifiable suspicion is necessary to justify the intrusion if the balance is to tip in favor of the legality of the governmental intrusion. In <em>Pennsylvania </em>v. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#107" aria-description="Citation for case: Pennsylvania v. Mimms"><em>Mimms, supra, </em>at 107</a></span>, the officers had personally observed the seized individual in the commission of a traffic offense before requesting that he exit his vehicle. In <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#693" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 693</a></span> (1981), the officers had obtained a warrant to search the house that the person seized was leaving when they came upon him. While the facts in <em>Pennsylvania </em>v. <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>and <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>differ in some respects from the facts of this case, the similarities are strong enough that the balancing of governmental interests against governmental intrusion undertaken in those cases is also appropriate here. All three of the factors involved in <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>and <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>are present in this case: the safety of the officers was served by the governmental intrusion; the intrusion was minimal; and the search stemmed <page-number citation-index="1" label="118">*118</page-number>from some probable cause focusing suspicion on the individual affected by the search. Indeed, here the officers’ probable cause stemmed from directly observing respondent commit a violation of the law.</p>
<p id="b200-5">When we undertake the necessary balancing of “the nature and quality of the intrusion on the individual’s Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion,” <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983), the conclusion that the search here was permissible follows. As we recognized in <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#658" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 658</a></span>, the governmental interest in highway safety served by obtaining the VIN is of the first order, and the particular method of obtaining the VIN here was justified by a concern for the officers’ safety. The “critical” issue of the intrusiveness of the government’s action, <em>United States </em>v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#722" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 722</a></span> (Blackmun, J., concurring in judgment), also here weighs in favor of allowing the search. The search was focused in its objective and no more intrusive than necessary to fulfill that objective. The search was far less intrusive than a formal arrest, which would have been permissible for a traffic offense under New York law, see N. Y. Veh. &amp; Traf. Law § 155 (McKinney Supp. 1986); N. Y. Crim. Proc. Law §140.10(1) (McKinney 1981), and little more intrusive than a demand that respondent — under the eyes of the officers — move the papers himself. The VIN, which was the clear initial objective of the officer, is by law present in one of two locations — either inside the doorjamb, or atop the dashboard and thus ordinarily in plain view of someone outside the automobile. Neither of those locations is subject to a reasonable expectation of privacy. The officer here checked both those locations, and only those two locations. The officer did not root about the interior of respondent’s automobile before proceeding to examine the VIN. He did not reach into any compartments or open any containers. He did not even intrude into the interior at all until after he had checked the doorjamb for <page-number citation-index="1" label="119">*119</page-number>the VIN. When he did intrude, the officer simply reached directly for the unprotected space where the VIN was located to move the offending papers. We hold that this search was sufficiently unintrusive to be constitutionally permissible in light of the lack of a reasonable expectation of privacy in the VIN and the fact that the officers observed respondent commit two traffic violations. Any other conclusion would expose police officers to potentially grave risks without significantly reducing the intrusiveness of the ultimate conduct — viewing the VIN — which, as we have said, the officers were entitled, to do as part of an undoubtedly justified traffic stop.</p>
<p id="b201-5">We note that our holding today does not authorize police officers to enter a vehicle to obtain a dashboard-mounted VIN when the VIN is visible from outside the automobile. If the VIN is in the plain view of someone outside the vehicle, there is no justification for governmental intrusion into the passenger compartment to see it.<footnotemark>*</footnotemark></p>
<p id="b201-6">The judgment of the New York Court of Appeals is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b201-7">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b201-8">Petitioner invites us to hold that respondent’s status as an unlicensed driver deprived him of any reasonable expectations of privacy in the vehicle, because the officers would have been within their discretion to have prohibited respondent from driving the ear away, to have impounded the ear, and to have later conducted an inventory search thereof. Cf. <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976) (police may conduct inventory search of car impounded for multiple parking violations); <em>Nix </em>v. <em>Williams, </em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U. S. 431</a></span> (1984) (discussing the “inevitable discovery” exception to the exclusionary rule). Petitioner also argues that there can be no Fourth Amendment violation here because the police could have arrested respondent, see N. Y. Veh. &amp; Traf. Law §155 (McKinney Supp. 1986); N. Y. Crim. Proc. Law §140.10(1) (McKinney 1981), and could then have searched the passenger compartment at the time of arrest, cf. <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), or arrested respondent and searched the car after impounding it pursuant to the arrest, see <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973). We do not, however, reach those questions here.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/New York v. Harris.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "New York v. Harris"
type: case
citation: "495 U.S. 14 (1990)"
parallel_cite: "110 S. Ct. 1640; 109 L. Ed. 2d 13; 58 U.S.L.W. 4457"
neutral_cite: 1990 U.S. LEXIS 2037
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-04-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-04-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New York v. Harris
  varies_by_point: false
  scope_note: "Good law. Where police have probable cause to arrest, a Payton violation (warrantless in-home arrest) does not require suppression of a statement the suspect later makes outside the home; the exclusionary remedy reaches only what is gathered inside the home. Distinct from the reversed-party case Harris v. New York, 401 U.S. 222 (1971) (Miranda impeachment)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112413/new-york-v-harris/"
  cluster_id: 112413
  opinion_id: 9431975
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Limiting"
  - page: "[[Entry to Arrest]]"
    role: "Limiting"
  - page: "[[Fruits & Attenuation]]"
    role: "Related (cross-doctrine)"
related: ["[[Payton v. New York]]", "[[Brown v. Illinois]]", "[[Wong Sun v. United States]]", "[[Kirk v. Louisiana]]"]
aliases: ["New York v. Harris (1990)"]
tags: ["case", "fourth-amendment", "arrest-in-the-home", "exclusionary-rule", "payton-violation", "fruit-of-the-poisonous-tree"]
holding: "Where police have probable cause to arrest, a Payton violation does not require suppression of a statement the suspect makes outside his home; such a statement is not the fruit of the in-home location of the arrest."
lake:
  record_id: New York v. Harris
  status: verified
  projected_at: 2026-07-06
---

# New York v. Harris

*495 U.S. 14 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police had probable cause to believe Bernard Harris had murdered Thelma Staton. Without an arrest warrant and without consent or [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], three officers entered Harris's home, read him his *[[Miranda v. Arizona|Miranda]]* rights, and obtained an admission inside the home (a *[[Payton v. New York|Payton]]* violation; that in-home statement was suppressed, which the State conceded). They then took Harris to the station house, again administered *[[Miranda v. Arizona|Miranda]]* warnings, and Harris signed a written inculpatory statement. New York's courts suppressed the station-house statement as the fruit of the unlawful in-home arrest.

## Issue
Whether the exclusionary rule requires suppression of a statement a defendant makes at the police station, after a warrantless in-home arrest that violated *[[Payton v. New York|Payton]]*, when the police had probable cause to arrest him.

## Rule
No. "We hold that, where the police have probable cause to arrest a suspect, the exclusionary rule does not bar the State's use of a statement made by the defendant outside of his home, even though the statement is taken after an arrest made in the home in violation of *Payton*." — 495 U.S. at 21. ^pin-21

*[[Payton v. New York|Payton]]*'s remedy is tied to its purpose — protecting the home: "*Payton* was designed to protect the physical integrity of the home; it was not intended to grant criminal suspects, like Harris, protection for statements made outside their premises where the police have probable cause to arrest the suspect for committing a crime." — *Id.* at 17. ^pin-17

The station-house statement therefore was not suppressible: "Harris' statement taken at the police station was not the product of being in unlawful custody. Neither was it the fruit of having been arrested in the home rather than someplace else." — *Id.* at 19. ^pin-19

## Application
Because the officers had probable cause, Harris was in *lawful* custody once removed from the house, properly Mirandized, and allowed to talk; the warrantless entry's only unlawful product — what the police gained by arresting him *inside* the home (the in-home statement) — was already suppressed, vindicating *[[Payton v. New York|Payton]]*'s purpose. The station-house statement was neither the product of unlawful custody nor the fruit of the in-home location of the arrest. This distinguishes *[[Brown v. Illinois]]*, *[[Dunaway v. New York|Dunaway]]*, and *[[Taylor v. Alabama|Taylor]]*, where confessions were suppressed because the police lacked probable cause and the detention itself was illegal.

## Conclusion
With probable cause to arrest, a *[[Payton v. New York|Payton]]* violation does not require suppression of a statement made outside the home; the New York suppression of the station-house statement was reversed. The exclusionary remedy for a *[[Payton v. New York|Payton]]* violation reaches only the evidence obtained from the in-home arrest itself.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *New York v. Harris* limits the exclusionary consequences of [[Payton v. New York]] (reaffirmed in [[Kirk v. Louisiana]]) and turns on the presence of probable cause — contrast [[Brown v. Illinois]] (confession suppressed where the arrest lacked probable cause) and the [[Fruits and Attenuation|attenuation]] framework of [[Wong Sun v. United States]].
- *Disambiguation:* distinct from the reversed-party case *[[Harris v. New York]]*, 401 U.S. 222 (1971) (statements taken in violation of *[[Miranda v. Arizona|Miranda]]* may impeach a testifying defendant).

## Appears on
- [[Arrest in the Home]] — *Limiting*
- [[Entry to Arrest]] — *Limiting*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *New York v. Harris*, 495 U.S. 14 (1990) — https://www.courtlistener.com/opinion/112413/new-york-v-harris/ — pinpoints: 17, 19, 21.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2c976326f7875f09", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "New York v. Harris"}, "payload": {"all": [{"cite": "495 U.S. 14", "page": "14", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "495"}, {"cite": "110 S. Ct. 1640", "page": "1640", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "109 L. Ed. 2d 13", "page": "13", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "1990 U.S. LEXIS 2037", "page": "2037", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}, {"cite": "58 U.S.L.W. 4457", "page": "4457", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "58"}], "display": "495 U.S. 14", "official": {"cite": "495 U.S. 14", "page": "14", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "495"}, "official_selection_present": true, "record_id": "New York v. Harris"}}
{"assertion_id": "0b1f5c70f9046708", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-17", "record_id": "New York v. Harris"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-17", "pinpoint_status": "slip-only", "quote": "*Payton* was designed to protect the physical integrity of the home; it was not intended to grant criminal suspects, like Harris, protection for statements made outside their premises where the police have probable cause to arrest the suspect for committing a crime.", "quote_fidelity": "mismatch", "record_id": "New York v. Harris", "star_marker": null}}
{"assertion_id": "b89e54dce3381f57", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-19", "record_id": "New York v. Harris"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-19", "pinpoint_status": "slip-only", "quote": "Harris' statement taken at the police station was not the product of being in unlawful custody. Neither was it the fruit of having been arrested in the home rather than someplace else.", "quote_fidelity": "mismatch", "record_id": "New York v. Harris", "star_marker": null}}
{"assertion_id": "becbc6c0d08f9602", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-21", "record_id": "New York v. Harris"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-21", "pinpoint_status": "slip-only", "quote": "--- # New York v. Harris *495 U.S. 14 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police had probable cause to believe Bernard Harris had murdered Thelma Staton. Without an arrest warrant and without consent or exigent circumstances, three officers entered Harris's home, read him his *Miranda* rights, and obtained an admission inside the home (a *Payton* violation; that in-home statement was suppressed, which the State conceded). They then took Harris to the station house, again administered *Miranda* warnings, and Harris signed a written inculpatory statement. New York's courts suppressed the station-house statement as the fruit of the unlawful in-home arrest. ## Issue Whether the exclusionary rule requires suppression of a statement a defendant makes at the police station, after a warrantless in-home arrest that violated *Payton*, when the police had probable cause to arrest him. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "New York v. Harris", "star_marker": null}}
{"assertion_id": "7159bfe924d1b409", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "New York v. Harris"}, "payload": {"as_of_content": "1990-04-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "New York v. Harris", "scope_note": "Good law. Where police have probable cause to arrest, a Payton violation (warrantless in-home arrest) does not require suppression of a statement the suspect later makes outside the home; the exclusionary remedy reaches only what is gathered inside the home. Distinct from the reversed-party case Harris v. New York, 401 U.S. 222 (1971) (Miranda impeachment).", "varies_by_point": false}}
```

### lake record — New York v. Harris

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Harris",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Harris",
    "case_name_short": "Harris",
    "case_name_full": "New York v. Harris",
    "input_case_name": "New York v. Harris",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-04-18",
    "year": 1990,
    "docket": null,
    "cluster_id": 112413,
    "lead_opinion_id": 9431975,
    "sibling_ids": [
      112413,
      9431975,
      9431976
    ],
    "absolute_url": "/opinion/112413/new-york-v-harris/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "495 U.S. 14",
      "volume": "495",
      "reporter": "U.S.",
      "page": "14",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 1640",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1640",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 L. Ed. 2d 13",
        "volume": "109",
        "reporter": "L. Ed. 2d",
        "page": "13",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4457",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4457",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 2037",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2037",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "495 U.S. 14",
        "volume": "495",
        "reporter": "U.S.",
        "page": "14",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 1640",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1640",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 L. Ed. 2d 13",
        "volume": "109",
        "reporter": "L. Ed. 2d",
        "page": "13",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 2037",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2037",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4457",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4457",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "495 U.S. 14",
    "official_selection": {
      "court_class": "scotus",
      "selected": "495 U.S. 14",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-21",
      "page": null,
      "quote": "--- # New York v. Harris *495 U.S. 14 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police had probable cause to believe Bernard Harris had murdered Thelma Staton. Without an arrest warrant and without consent or exigent circumstances, three officers entered Harris's home, read him his *Miranda* rights, and obtained an admission inside the home (a *Payton* violation; that in-home statement was suppressed, which the State conceded). They then took Harris to the station house, again administered *Miranda* warnings, and Harris signed a written inculpatory statement. New York's courts suppressed the station-house statement as the fruit of the unlawful in-home arrest. ## Issue Whether the exclusionary rule requires suppression of a statement a defendant makes at the police station, after a warrantless in-home arrest that violated *Payton*, when the police had probable cause to arrest him. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-17",
      "page": null,
      "quote": "*Payton* was designed to protect the physical integrity of the home; it was not intended to grant criminal suspects, like Harris, protection for statements made outside their premises where the police have probable cause to arrest the suspect for committing a crime.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-19",
      "page": null,
      "quote": "Harris' statement taken at the police station was not the product of being in unlawful custody. Neither was it the fruit of having been arrested in the home rather than someplace else.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-04-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New York v. Harris",
    "varies_by_point": false,
    "scope_note": "Good law. Where police have probable cause to arrest, a Payton violation (warrantless in-home arrest) does not require suppression of a statement the suspect later makes outside the home; the exclusionary remedy reaches only what is gathered inside the home. Distinct from the reversed-party case Harris v. New York, 401 U.S. 222 (1971) (Miranda impeachment).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Serrano-Acevedo",
          "cluster_id": 4506969,
          "cite": [
            "892 F.3d 454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "NYIA GORE v. UNITED STATES",
          "cluster_id": 4248978,
          "cite": [
            "145 A.3d 540",
            "2016 D.C. App. LEXIS 313",
            "2016 WL 4411321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jenkins",
          "cluster_id": 2444991,
          "cite": [
            "3 A.3d 806",
            "298 Conn. 209",
            "2010 Conn. LEXIS 304"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Molina",
          "cluster_id": 6578709,
          "cite": [
            "439 Mass. 206",
            "786 N.E.2d 1191",
            "2003 Mass. LEXIS 271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Nieto",
          "cluster_id": 6346309,
          "cite": [
            "192 Misc. 2d 537",
            "746 N.Y.S.2d 371",
            "2002 N.Y. Misc. LEXIS 979"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Patrick Flores Oaxaca",
          "cluster_id": 771307,
          "cite": [
            "233 F.3d 1154",
            "2000 Cal. Daily Op. Serv. 9159",
            "2000 Daily Journal DAR 12172",
            "2000 U.S. App. LEXIS 28971",
            "2000 WL 1701453"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane1_negative"
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
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 2347917,
          "cite": [
            "256 S.W.3d 264",
            "2008 Tex. Crim. App. LEXIS 754",
            "2008 WL 2437667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ballard",
          "cluster_id": 1533349,
          "cite": [
            "987 S.W.2d 889",
            "1999 Tex. Crim. App. LEXIS 14",
            "1999 WL 89535"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Geisler",
          "cluster_id": 7894925,
          "cite": [
            "222 Conn. 672",
            "610 A.2d 1225",
            "61 U.S.L.W. 2093",
            "1992 Conn. LEXIS 214"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
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
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Riley",
          "cluster_id": 1367783,
          "cite": [
            "846 P.2d 1365",
            "121 Wash. 2d 22",
            "1993 Wash. LEXIS 66"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Henderson",
          "cluster_id": 1057155,
          "cite": [
            "2013 IL 114040"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Snider",
          "cluster_id": 1746280,
          "cite": [
            "608 N.W.2d 502",
            "239 Mich. App. 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Huddleston",
          "cluster_id": 2435833,
          "cite": [
            "924 S.W.2d 666",
            "1996 Tenn. LEXIS 387",
            "1996 WL 328642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ernest Martin v. Betty Mitchell, Warden",
          "cluster_id": 776544,
          "cite": [
            "280 F.3d 594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thurman",
          "cluster_id": 1367765,
          "cite": [
            "846 P.2d 1256",
            "203 Utah Adv. Rep. 18",
            "1993 Utah LEXIS 40",
            "1993 WL 4794"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas McClish v. Richard B. Nugent",
          "cluster_id": 77659,
          "cite": [
            "483 F.3d 1231",
            "2007 U.S. App. LEXIS 8294",
            "2007 WL 1063337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
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
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Osvaldo Rodriguez-Morales",
          "cluster_id": 558566,
          "cite": [
            "929 F.2d 780",
            "1991 U.S. App. LEXIS 4854",
            "1991 WL 40569"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 2012814,
          "cite": [
            "927 N.E.2d 1179",
            "237 Ill. 2d 81",
            "340 Ill. Dec. 168",
            "2010 Ill. LEXIS 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powell v. Nevada",
          "cluster_id": 117833,
          "cite": [
            "128 L. Ed. 2d 1",
            "114 S. Ct. 1280",
            "511 U.S. 79",
            "1994 U.S. LEXIS 2655"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McCauley",
          "cluster_id": 2127673,
          "cite": [
            "645 N.E.2d 923",
            "163 Ill. 2d 414",
            "206 Ill. Dec. 671",
            "63 U.S.L.W. 2476",
            "1994 Ill. LEXIS 175"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lovejoy",
          "cluster_id": 2162437,
          "cite": [
            "919 N.E.2d 843",
            "235 Ill. 2d 97",
            "335 Ill. Dec. 818",
            "2009 Ill. LEXIS 1302"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Busby v. State",
          "cluster_id": 2390040,
          "cite": [
            "990 S.W.2d 263",
            "1999 Tex. Crim. App. LEXIS 26",
            "1999 WL 172911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Othoudt",
          "cluster_id": 2185300,
          "cite": [
            "482 N.W.2d 218",
            "1992 Minn. LEXIS 73",
            "1992 WL 45841"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Perry",
          "cluster_id": 2390579,
          "cite": [
            "590 A.2d 624",
            "124 N.J. 128",
            "1991 N.J. LEXIS 45"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Canez",
          "cluster_id": 867610,
          "cite": [
            "42 P.3d 564",
            "202 Ariz. 133"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. State",
          "cluster_id": 2385168,
          "cite": [
            "932 S.W.2d 502",
            "1996 Tex. Crim. App. LEXIS 193",
            "1996 WL 512397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Harris",
          "cluster_id": 5690319,
          "cite": [
            "77 N.Y.2d 434",
            "568 N.Y.S.2d 702",
            "570 N.E.2d 1051",
            "1991 N.Y. LEXIS 210"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Harris:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112413 OR 9431975 OR 9431976) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NTA3NDU2MDAwMDAmcz0yMDQwMDc4JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112413+OR+9431975+OR+9431976%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112413 OR 9431975 OR 9431976)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OSZzPTE5ODcyNyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112413+OR+9431975+OR+9431976%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112413 OR 9431975 OR 9431976)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112413 OR 9431975 OR 9431976)",
    "indexed_citing_opinions": 428,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112413,
        "count": 372,
        "count_source": "search"
      },
      {
        "opinion_id": 9431975,
        "count": 67,
        "count_source": "search"
      },
      {
        "opinion_id": 9431976,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 659,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-harris.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY0MTM5OTQmcz02MjQwNzAzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112413+OR+9431975+OR+9431976%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112413,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 110760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112413,
        "cited_id": 112136,
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
    "date_created": "2026-07-05T15:43:14Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:48:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:43:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Harris

```
<opinion type="majority">
<author id="b71-10">Justice White</author>
<p id="AuY">delivered the opinion of the Court.</p>
<p id="b71-11">On January 11, 1984, New York City police found the body of Ms. Thelma Staton murdered in her apartment. Various facts gave the officers probable cause to believe that the respondent in this case, Bernard Harris, had killed Ms. Staton. As a result, on January 16, 1984, three police officers went to Harris’ apartment to take him into custody. They did not first obtain an arrest warrant.</p>
<p id="b71-12">When the police arrived, they knocked on the door, displaying their guns and badges. Harris let them enter. <page-number citation-index="1" label="16">*16</page-number>Once inside, the officers read Harris his rights under <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Harris acknowledged that he understood the warnings, and agreed to answer the officers’ questions. At that point, he reportedly admitted that he had killed Ms. Staton.</p>
<p id="b72-5">Harris was arrested, taken to the station house, and again informed of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. He then signed a written inculpatory statement. The police subsequently read Harris the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings a third time and videotaped an incriminating interview between Harris and a district attorney, even though Harris had indicated that he wanted to end the interrogation.</p>
<p id="b72-6">The trial court suppressed Harris’ first and third statements; the State does not challenge those rulings. The sole issue in this case is whether Harris’ second statement — the written statement made at the station house — should have been suppressed because the police, by entering Harris’ home without a warrant and without his consent, violated <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), which held that the Fourth Amendment prohibits the police from effecting a warrantless and nonconsensual entry into a suspect’s home in order to make a routine felony arrest. The New York trial court concluded that the statement was admissible. Following a bench trial, Harris was convicted of second-degree murder. The Appellate Division affirmed, 124 App. Div. 2d 472, 507 N. Y. S. 2d 823 (1986).</p>
<p id="b72-7">A divided New York Court of Appeals reversed, 72 N. Y. 2d 614, <span class="citation" data-id="5538549"><a href="/opinion/5689309/people-v-harris/" aria-description="Citation for case: People v. Harris">532 N. E. 2d 1229</a></span> (1988). That court first accepted the trial court’s finding that Harris did not consent to the police officers’ entry into his home and that the warrantless arrest therefore violated <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>even though there was probable cause. Applying <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), and its progeny, the court then determined that the station house statement must be deemed to be the inadmissible fruit of the illegal arrest because the connection between the statement and the arrest was not sufficiently attenuated. <page-number citation-index="1" label="17">*17</page-number>The court noted that some courts had reasoned that the “wrong in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>cases . . . lies not in the arrest, ‘but in the unlawful <em>entry </em>into a dwelling without proper judicial authorization’ ” and had therefore declined to suppress confessions that were made following <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violations. 72 N. Y. 2d, at 623, <span class="citation" data-id="5538549"><a href="/opinion/5689309/people-v-harris/#1234" aria-description="Citation for case: People v. Harris">532 N. E. 2d, at 1234</a></span>. The New York court disagreed with this analysis, finding it contrary to <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and its own decisions interpreting <em>Payton’s, </em>scope. We granted certiorari to resolve the admissibility of the station house statement. <span class="citation multiple-matches"><a href="/c/U.%20S./490/1018/">490 U. S. 1018</a></span> (1989).</p>
<p id="b73-5">For present purposes, we accept the finding below that Harris did not consent to the police officers’ entry into his home and the conclusion that the police had probable cause to arrest him. It is also evident, in light of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>that arresting Harris in his home without an arrest warrant violated the Fourth Amendment. But, as emphasized in earlier cases, “we have declined to adopt a <em>‘per se </em>or “but for” rule’ that would make inadmissible any. evidence, whether tangible or five-witness testimony, which somehow came to fight through a chain of causation that began with an illegal arrest.” <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#276" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 276</a></span> (1978). Rather, in this context, we have stated that “[t]he penalties visited upon the Government, and in turn upon the public, because its officers have violated the law must bear some relation to the purposes which the law is to serve. ” <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#279" aria-description="Citation for case: United States v. Ceccolini">Id., at 279</a></span>. In fight of these principles, we decline to apply the exclusionary rule in this context because the rule in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>was designed to protect the physical integrity of the home; it was not intended to grant criminal suspects, like Harris, protection for statements made outside their premises where the police have probable cause to arrest the suspect for committing a crime.</p>
<p id="b73-6"><em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>itself emphasized that our holding in that case stemmed from the “overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#601" aria-description="Citation for case: Payton v. New York">445 U. S., at 601</a></span>. Although it had <page-number citation-index="1" label="18">*18</page-number>long been settled that a warrantless arrest in a public place was permissible as long as the arresting officer had probable cause, see <em>United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976), <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>nevertheless drew a line at the entrance to the home. This special solicitude was necessary because ‘“physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed.’” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U. S., at 585</a></span> (citation omitted). The arrest warrant was required to “interpose the magistrate’s determination of probable cause” to arrest before the officers could enter a house to effect an arrest. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 602-603</a></span>.</p>
<p id="b74-5">Nothing in the reasoning of that case suggests that an arrest in a home without a warrant but with probable cause somehow renders unlawful continued custody of the suspect once he is removed from the house. There could be no valid claim here that Harris was immune from prosecution because his person was the fruit of an illegal arrest. <em>United States </em>v. <em>Crews, </em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/#474" aria-description="Citation for case: United States v. Crews">445 U. S. 463, 474</a></span> (1980). Nor is there any claim that the warrantless arrest required the police to release Harris or that Harris could not be immediately rearrested if momentarily released. Because the officers had probable cause to arrest Harris for a crime, Harris was not unlawfully in custody when he was removed to the station house, given <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, and allowed to talk. For Fourth Amendment purposes, the legal issue is the same as it would be had the police arrested Harris on his doorstep, illegally entered his home to search for evidence, and later interrogated Harris at the station house. Similarly, if the police had made a warrantless entry into Harris’ home, not found him there, but arrested him on the street when he returned, a later statement made by him after proper warnings would no doubt be admissible.</p>
<p id="b74-6">This case is therefore different from <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), and <em>Taylor </em>v. <em>Alabama, </em><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">457 U. S. 687</a></span> (1982). In each of those cases, evidence obtained from a criminal de<page-number citation-index="1" label="19">*19</page-number>fendant following arrest was suppressed because the police lacked probable cause. The three cases stand for the familiar proposition that the indirect fruits of an illegal search or arrest should be suppressed when they bear a sufficiently close relationship to the underlying illegality. See also <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). We have emphasized, however, that attenuation analysis is only appropriate where, as a threshold matter, courts determine that “the challenged evidence is in some sense the product of illegal governmental activity.” <em>United States </em>v. <span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/#471" aria-description="Citation for case: United States v. Crews"><em>Crews, supra, </em>at 471</a></span>. As Judge Titone, concurring in the judgment on the basis of New York state precedent, cogently argued below, “[i]n cases such as <em>Brown </em>v. <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois (supra)</a></span> </em>and its progeny, an affirmative answer to that preliminary question may be assumed, since the ‘illegality’ is the absence of probable cause and the wrong consists of the police’s having control of the defendant’s person at the time he made the challenged statement. In these cases, the ‘challenged <em>evidence’ </em>— i. <em>e., </em>the post arrest confession — is unquestionably ‘the product,of [the] illegal governmental <em>activity’ </em>— i. <em>e., </em>the wrongful detention.” 72 N. Y. 2d, at 625, <span class="citation" data-id="5538549"><a href="/opinion/5689309/people-v-harris/#1235" aria-description="Citation for case: People v. Harris">532 N. E. 2d, at 1235</a></span>.</p>
<p id="b75-5">Harris’ statement taken at the police station was not the product of being in unlawful custody. Neither was it the fruit of having been arrested in the home rather than someplace else. The case is analogous to <em>United States </em>v. <em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/" aria-description="Citation for case: United States v. Crews">Crews, supra.</a></span> </em>In that case, we refused to suppress a victim’s in-court identification despite the defendant’s illegal arrest. The Court found that the evidence was not “‘come at by exploitation’ of . . . the defendant’s Fourth Amendment rights,” and that it was not necessary to inquire whether the “taint” of the Fourth Amendment violation was sufficiently attenuated to permit the introduction of the evidence. 445 U. S., at 471. Here, likewise, the police had a justification to question Harris prior to his arrest; therefore, his subsequent statement was not an exploitation of the illegal entry into Harris’ home.</p>
<p id="b76-4"><page-number citation-index="1" label="20">*20</page-number>We do not hold, as the dissent suggests, that a statement taken by the police while a suspect is in custody is always admissible as long as the suspect is in legal custody. Statements taken during legal custody would of course be inadmissible, for example, if they were the product of coercion, if <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were not given, or if there was a violation of the rule of <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). We do hold that the station house statement in this case was admissible because Harris was in legal custody, as the dissent concedes, and because the statement, while the product of an arrest and being in custody, was not the fruit of the fact that the arrest was made in the house rather than someplace else.</p>
<p id="b76-5">To put the matter another way, suppressing the statement taken outside the house would not serve the purpose of the rule that made Harris’ in-house arrest illegal. The warrant requirement for an arrest in the home is imposed to protect the home, and anything incriminating the police gathered from arresting Harris in his home, rather than elsewhere, has been excluded, as it should have been; the purpose of the rule has thereby been vindicated. We are not required by the Constitution to go further and suppress statements later made by Harris in order to deter police from violating <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>“As cases considering the use of unlawfully obtained evidence in criminal trials themselves make clear, it does not follow from the emphasis on the exclusionary rule’s deterrent value that ‘anything which deters illegal searches is thereby commanded by the Fourth Amendment.’” <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#910" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 910</a></span> (1984) (citation omitted). Even though we decline to suppress statements made outside the home following a <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation, the principal incentive to obey <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>still obtains: the police know that a warrant-less entry will lead to the suppression of any evidence found, or statements taken, inside the home. If we did suppress statements like Harris’, moreover, the incremental deterrent value would be minimal. Given that the police have probable cause to arrest a suspect in Harris’ position, they need <page-number citation-index="1" label="21">*21</page-number>not violate <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>in order to interrogate the suspect. It is doubtful therefore that the desire to secure a statement from a criminal suspect would motivate the police to violate <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>As a result, suppressing a station house statement obtained after a <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation will have little effect on the officers’ actions, one way or another.</p>
<p id="b77-5">We hold that, where the police have probable cause to arrest a suspect, the exclusionary rule does not bar the State’s use of a statement made by the defendant outside of his home, even though the statement is taken after an arrest made in the home in violation of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>The judgment of the court below is accordingly</p>
<p id="b77-6">
<em>Reversed.</em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/New York v. Quarles.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "New York v. Quarles"
type: case
citation: "467 U.S. 649 (1984)"
parallel_cite: "104 S. Ct. 2626; 81 L. Ed. 2d 550; 52 U.S.L.W. 4790"
neutral_cite: 1984 U.S. LEXIS 111
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-06-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New York v. Quarles
  varies_by_point: false
  scope_note: "Establishes the public-safety exception to Miranda; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111214/new-york-v-quarles/"
  cluster_id: 111214
  opinion_id: 9429664
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Berkemer v. McCarty]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "public-safety-exception", "interrogation"]
holding: "There is a \"public safety\" exception to Miranda — when officers ask questions reasonably prompted by an immediate threat to public…"
lake:
  record_id: New York v. Quarles
  status: verified
  projected_at: 2026-07-06
---

# New York v. Quarles

*467 U.S. 649 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A woman told officers she had just been raped by an armed man who had entered a supermarket. An officer chased and apprehended Quarles inside the store, found he was wearing an empty shoulder holster, handcuffed him, and — before giving *[[Miranda v. Arizona|Miranda]]* warnings — asked where the gun was. Quarles nodded toward some cartons and said "the gun is over there"; the officer retrieved a loaded revolver.

## Issue
Whether there is an exception to *[[Miranda v. Arizona|Miranda]]* for questions reasonably prompted by a concern for public safety.

## Rule
Yes. "We hold that on these facts there is a 'public safety' exception to the requirement that *Miranda* warnings be given before a suspect's answers may be admitted into evidence, . . . and that the availability of that exception does not depend upon the motivation of the individual officers involved." — 467 U.S. at 655–56. ^pin-655

"We conclude that the need for answers to questions in a situation posing a threat to the public safety outweighs the need for the prophylactic rule protecting the Fifth Amendment's privilege against self-incrimination." — *Id.* at 657. ^pin-657

## Application
The unholstered, hidden gun in a public supermarket posed an immediate danger to the public and police, so the officer's question about its location fell within the public-safety exception. Both the statement "the gun is over there" and the gun itself were admissible despite the absence of *[[Miranda v. Arizona|Miranda]]* warnings, and the officer's actual motivation for asking was irrelevant.

## Conclusion
The statement and the gun were admissible under the public-safety exception; the New York Court of Appeals' suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Quarles* carves a public-safety exception out of [[Miranda v. Arizona]], turning on the objective existence of a public-safety concern rather than the officer's subjective motive.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *New York v. Quarles*, 467 U.S. 649 (1984) — https://www.courtlistener.com/opinion/111214/new-york-v-quarles/ — pinpoints: 655–56, 657.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "43645f230c98b9c5", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "New York v. Quarles"}, "payload": {"all": [{"cite": "467 U.S. 649", "page": "649", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "467"}, {"cite": "104 S. Ct. 2626", "page": "2626", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "81 L. Ed. 2d 550", "page": "550", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "81"}, {"cite": "1984 U.S. LEXIS 111", "page": "111", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 4790", "page": "4790", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "467 U.S. 649", "official": {"cite": "467 U.S. 649", "page": "649", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "467"}, "official_selection_present": true, "record_id": "New York v. Quarles"}}
{"assertion_id": "86ca9851af855be7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-657", "record_id": "New York v. Quarles"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-657", "pinpoint_status": "slip-only", "quote": "We conclude that the need for answers to questions in a situation posing a threat to the public safety outweighs the need for the prophylactic rule protecting the Fifth Amendment's privilege against self-incrimination.", "quote_fidelity": "mismatch", "record_id": "New York v. Quarles", "star_marker": null}}
{"assertion_id": "b6bb7210ed873e69", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-655", "record_id": "New York v. Quarles"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-655", "pinpoint_status": "slip-only", "quote": "; the officer retrieved a loaded revolver. ## Issue Whether there is an exception to *Miranda* for questions reasonably prompted by a concern for public safety. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "New York v. Quarles", "star_marker": null}}
{"assertion_id": "74048efd95ca1a99", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "New York v. Quarles"}, "payload": {"as_of_content": "1984-06-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "New York v. Quarles", "scope_note": "Establishes the public-safety exception to Miranda; good law.", "varies_by_point": false}}
```

### lake record — New York v. Quarles

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Quarles",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Quarles",
    "case_name_short": "Quarles",
    "case_name_full": "New York v. Quarles",
    "input_case_name": "New York v. Quarles",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-06-12",
    "year": 1984,
    "docket": null,
    "cluster_id": 111214,
    "lead_opinion_id": 9429664,
    "sibling_ids": [
      111214,
      9429664,
      9429665,
      9429666
    ],
    "absolute_url": "/opinion/111214/new-york-v-quarles/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "467 U.S. 649",
      "volume": "467",
      "reporter": "U.S.",
      "page": "649",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2626",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2626",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 550",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "550",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4790",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4790",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 111",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "111",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "467 U.S. 649",
        "volume": "467",
        "reporter": "U.S.",
        "page": "649",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2626",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2626",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 550",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "550",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 111",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "111",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4790",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4790",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "467 U.S. 649",
    "official_selection": {
      "court_class": "scotus",
      "selected": "467 U.S. 649",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-655",
      "page": null,
      "quote": "; the officer retrieved a loaded revolver. ## Issue Whether there is an exception to *Miranda* for questions reasonably prompted by a concern for public safety. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-657",
      "page": null,
      "quote": "We conclude that the need for answers to questions in a situation posing a threat to the public safety outweighs the need for the prophylactic rule protecting the Fifth Amendment's privilege against self-incrimination.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-06-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New York v. Quarles",
    "varies_by_point": false,
    "scope_note": "Establishes the public-safety exception to Miranda; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Earl",
          "cluster_id": 9404588,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chhay Lim",
          "cluster_id": 4522500,
          "cite": [
            "897 F.3d 673"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Castano",
          "cluster_id": 4432551,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane1_negative"
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
        "journal_ref": "New York v. Quarles:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jovan'z Smith v. Ken Clark",
          "cluster_id": 3134205,
          "cite": [
            "804 F.3d 983",
            "2015 U.S. App. LEXIS 18335",
            "2015 WL 6387862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Broom a/k/a Patrick Brown v. United States",
          "cluster_id": 2809687,
          "cite": [
            "118 A.3d 207",
            "2015 D.C. App. LEXIS 265",
            "2015 WL 3768885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gonzalez",
          "cluster_id": 2319916,
          "cite": [
            "25 A.3d 648",
            "302 Conn. 287",
            "2011 Conn. LEXIS 355",
            "2011 WL 3802478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berkemer v. McCarty",
          "cluster_id": 111249,
          "cite": [
            "82 L. Ed. 2d 317",
            "104 S. Ct. 3138",
            "468 U.S. 420",
            "1984 U.S. LEXIS 140",
            "52 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. Washington",
          "cluster_id": 145641,
          "cite": [
            "165 L. Ed. 2d 224",
            "126 S. Ct. 2266",
            "547 U.S. 813",
            "2006 U.S. LEXIS 4886"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Heller",
          "cluster_id": 145777,
          "cite": [
            "171 L. Ed. 2d 637",
            "128 S. Ct. 2783",
            "554 U.S. 570",
            "2008 U.S. LEXIS 5268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Ritchie",
          "cluster_id": 111822,
          "cite": [
            "94 L. Ed. 2d 40",
            "107 S. Ct. 989",
            "480 U.S. 39",
            "1987 U.S. LEXIS 558",
            "55 U.S.L.W. 4180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDonald v. City of Chicago",
          "cluster_id": 149702,
          "cite": [
            "177 L. Ed. 2d 894",
            "130 S. Ct. 3020",
            "561 U.S. 742",
            "2010 U.S. LEXIS 5523",
            "22 Fla. L. Weekly Fed. S 619",
            "78 U.S.L.W. 4844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Bryant",
          "cluster_id": 2959736,
          "cite": [
            "179 L. Ed. 2d 93",
            "131 S. Ct. 1143",
            "562 U.S. 344",
            "2011 U.S. LEXIS 1713"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Perkins",
          "cluster_id": 112452,
          "cite": [
            "110 L. Ed. 2d 243",
            "110 S. Ct. 2394",
            "496 U.S. 292",
            "1990 U.S. LEXIS 2885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chavez v. Martinez",
          "cluster_id": 127927,
          "cite": [
            "155 L. Ed. 2d 984",
            "123 S. Ct. 1994",
            "538 U.S. 760",
            "2003 U.S. LEXIS 4274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": [
            "182 L. Ed. 2d 17",
            "132 S. Ct. 1181",
            "565 U.S. 499",
            "2012 U.S. LEXIS 1077",
            "2012 WL 538280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Withrow v. Williams",
          "cluster_id": 112847,
          "cite": [
            "123 L. Ed. 2d 407",
            "113 S. Ct. 1745",
            "507 U.S. 680",
            "1993 U.S. LEXIS 2980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patane",
          "cluster_id": 137003,
          "cite": [
            "159 L. Ed. 2d 667",
            "124 S. Ct. 2620",
            "542 U.S. 630",
            "2004 U.S. LEXIS 4577"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
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
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Connecticut v. Barrett",
          "cluster_id": 111796,
          "cite": [
            "93 L. Ed. 2d 920",
            "107 S. Ct. 828",
            "479 U.S. 523",
            "1987 U.S. LEXIS 419",
            "55 U.S.L.W. 4151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Quarles:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111214 OR 9429664 OR 9429665 OR 9429666) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzA3NjY0MDAwMDAwJnM9NTk2ODYyOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111214+OR+9429664+OR+9429665+OR+9429666%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111214 OR 9429664 OR 9429665 OR 9429666)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjEmcz0xMjQ0NzUyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111214+OR+9429664+OR+9429665+OR+9429666%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111214 OR 9429664 OR 9429665 OR 9429666)",
        "reviewed": 53,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 53,
        "triage_read": 0,
        "triage_snippet_classified": 53
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111214 OR 9429664 OR 9429665 OR 9429666)",
    "indexed_citing_opinions": 925,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111214,
        "count": 782,
        "count_source": "search"
      },
      {
        "opinion_id": 9429664,
        "count": 160,
        "count_source": "search"
      },
      {
        "opinion_id": 9429665,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429666,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1468,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-quarles.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3MzIwNTEmcz05NDkzMDI5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111214+OR+9429664+OR+9429665+OR+9429666%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111214,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 103320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 109997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 336178,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 375540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
        "cited_id": 1173989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111214,
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
    "date_created": "2026-07-05T15:48:41Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:48:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:48:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:52:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:48:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Quarles

```
<opinion type="majority">
<author id="b709-4"><page-number citation-index="1" label="651">*651</page-number>Justice Rehnquist</author>
<p id="Ani">delivered the opinion of the Court.</p>
<p id="b709-5">Respondent Benjamin Quarles was charged in the New York trial court with criminal possession of a weapon. The trial court suppressed the gun in question, and a statement made by respondent, because the statement was obtained by police before they read respondent his <em>“Miranda </em>rights.” That ruling was affirmed on appeal through the New York Court of Appeals. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./461/942/">461 U. S. 942</a></span> (1983), and we now reverse.<footnotemark>1</footnotemark> We conclude that under the circumstances involved in this case, overriding considerations of public safety justify the officer’s failure to provide <em>Miranda </em>warnings before he asked questions devoted to locating the abandoned weapon.</p>
<p id="b709-6">On September 11, 1980, at approximately 12:30 a. m., Officer Frank Kraft and Officer Sal Scarring were on road patrol in Queens, N. Y., when a young woman approached their car. She told them that she had just been raped by a black male, approximately six feet tall, who was wearing a black jacket with the name “Big Ben” printed in yellow letters on the back. She told the officers that the man had just entered <page-number citation-index="1" label="652">*652</page-number>an A &amp; P supermarket located nearby and that the man was carrying a gun.</p>
<p id="b710-5">The officers drove the woman to the supermarket, and Officer Kraft entered the store while Officer Scarring radioed for assistance. Officer Kraft quickly spotted respondent, who matched the description given by the woman, approaching a checkout counter. Apparently upon seeing the officer, respondent turned and ran toward the rear of the store, and Officer Kraft pursued him with a drawn gun. When respondent turned the corner at the end of an aisle, Officer Kraft lost sight of him for several seconds, and upon regaining sight of respondent, ordered him to stop and put his hands over his head.</p>
<p id="b710-6">Although more than three other officers had arrived on the scene by that time, Officer Kraft was the first to reach respondent. He frisked him and discovered that he was wearing a shoulder holster which was then empty. After handcuffing him, Officer Kraft asked him where the gun was. Respondent nodded in the direction of some empty cartons and responded, “the gun is over there.” Officer Kraft thereafter retrieved a loaded .38-caliber revolver from one of the cartons, formally placed respondent under arrest, and read him his <em>Miranda </em>rights from a printed card. Respondent indicated that he would be willing to answer questions without an attorney present. Officer Kraft then asked respondent if he owned the gun and where he had purchased it. Respondent answered that he did own it and that he had purchased it in Miami, Fla.</p>
<p id="b710-7">In the subsequent prosecution of respondent for criminal possession of a weapon,<footnotemark>2</footnotemark> the judge excluded the statement, “the gun is over there,” and the gun because the officer had not given respondent the warnings required by our decision in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), before asking <page-number citation-index="1" label="653">*653</page-number>him where the gun was located. The judge excluded the other statements about respondent’s ownership of the gun and the place of purchase, as evidence tainted by the prior <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation. The Appellate Division of the Supreme Court of New York affirmed without opinion. 85 App. Div. 2d 936, 447 N. Y. S. 2d 84 (1981).</p>
<p id="A6W">The Court of Appeals granted leave to appeal and affirmed by a 4-3 vote. 58 N. Y. 2d 664, <span class="citation" data-id="5535302"><a href="/opinion/5686260/people-v-quarles/" aria-description="Citation for case: People v. Quarles">444 N. E. 2d 984</a></span> (1982). It concluded that respondent was in “custody” within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>during all questioning and rejected the State’s argument that the exigencies of the situation justified Officer Kraft’s failure to read respondent his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights until after he had located the gun. The court declined to recognize an exigency exception to the usual requirements of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>because it found no indication from Officer Kraft’s testimony at the suppression hearing that his subjective motivation in asking the question was to protect his own safety or the safety of the public. 58 N. Y. 2d, at 666, <span class="citation" data-id="5535302"><a href="/opinion/5686260/people-v-quarles/#985" aria-description="Citation for case: People v. Quarles">444 N. E. 2d, at 985</a></span>. For the reasons which follow, we believe that this case presents a situation where concern for public safety must be paramount to adherence to the literal language of the prophylactic rules enunciated in Miranda.<footnotemark>3</footnotemark></p>
<p id="b712-4"><page-number citation-index="1" label="654">*654</page-number>The Fifth Amendment guarantees that “[n]o person . . . shall be compelled in any criminal case to be a witness against himself.” In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>this Court for the first time extended the Fifth Amendment privilege against compulsory self-incrimination to individuals subjected to custodial interrogation by the police. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#460" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 460-461, 467</a></span>. The Fifth Amendment itself does not prohibit all incriminating admissions; “[ajbsent some officially <em>coerced </em>self-accusation, the Fifth Amendment privilege is not violated by even the most damning admissions.” <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977) (emphasis added). The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court, however, presumed that interrogation in certain custodial circumstances<footnotemark>4</footnotemark> is inherently coercive and held that statements made under those circumstances are inadmissible unless the suspect is specifically informed of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights and freely decides to forgo those rights. The prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings therefore are “not themselves rights protected by the Constitution but [are] instead measures to insure that the right against compulsory self-incrimination [is] protected.” <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974); see <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#492" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 492</a></span> (1981) (Powell, J., concurring). Requiring <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings before custodial interrogation provides “practical reinforcement” for the Fifth Amendment right. <em>Michigan </em>v. <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker"><em>Tucker, supra, </em>at 444</a></span>.</p>
<p id="b712-6">In this case we have before us no claim that respondent’s statements were actually compelled by police conduct which overcame his will to resist. See <em>Beckwith </em>v. <em>United States, </em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#347" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 347-348</a></span> (1976); <em>Davis </em>v. <em>North Carolina, </em><span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span> (1966). Thus the only issue before us is whether <page-number citation-index="1" label="655">*655</page-number>Officer Kraft was justified in failing to make available to respondent the procedural safeguards associated with the privilege against compulsory self-incrimination since Miranda.<footnotemark>5</footnotemark></p>
<p id="b713-5">The New York Court of Appeals was undoubtedly correct in deciding that the facts of this case come within the ambit of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision as we have subsequently interpreted it. We agree that respondent was in police custody because we have noted that “the ultimate inquiry is simply whether there is a ‘formal arrest or restraint on freedom of movement’ of the degree associated with a formal arrest,” <em>California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span> (1983) <em>(per curiam), </em>quoting <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495</a></span> (1977) <em>(per curiam). </em>Here Quarles was surrounded by at least four police officers and was handcuffed when the questioning at issue took place. As the New York Court of Appeals observed, there was nothing to suggest that any of the officers were any longer concerned for their own physical safety. 58 N. Y. 2d, at 666, <span class="citation" data-id="5535302"><a href="/opinion/5686260/people-v-quarles/#985" aria-description="Citation for case: People v. Quarles">444 N. E. 2d, at 985</a></span>. The New York Court of Appeals’ majority declined to express an opinion as to whether there might be an exception to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule if the police had been acting to protect the public, because the lower courts in New York had made no factual determination that the police had acted with that motive. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></p>
<p id="b713-6">We hold that on these facts there is a “public safety” exception to the requirement that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings be given before a suspect’s answers may be admitted into evidence, <page-number citation-index="1" label="656">*656</page-number>and that the availability of that exception does not depend upon the motivation of the individual officers involved. In a kaleidoscopic situation such as the one confronting these officers, where spontaneity rather than adherence to a police manual is necessarily the order of the day, the application of the exception which we recognize today should not be made to depend on <em>post hoc </em>findings at a suppression hearing concerning the subjective motivation of the arresting officer.<footnotemark>6</footnotemark> Undoubtedly most police officers, if placed in Officer Kraft’s position, would act out of a host of different, instinctive, and largely unverifiable motives — their own safety, the safety of others, and perhaps as well the desire to obtain incriminating evidence from the suspect.</p>
<p id="b714-5">Whatever the motivation of individual officers in such a situation, we do not believe that the doctrinal underpinnings of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>require that it be applied in all its rigor to a situation in which police officers ask questions reasonably prompted by a concern for the public safety. The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision was based in large part on this Court’s view that the warnings which it required police to give to suspects in custody would reduce the likelihood that the suspects would fall victim to constitutionally impermissible practices of police interrogation in the presumptively coercive environment of the station house. 384 U. S., at 455-458. The dissenters warned that the requirement of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings would have the effect of decreasing the number of suspects who respond to police questioning. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#504" aria-description="Citation for case: Miranda v. Arizona">Id., at 504, 516-517</a></span> (Harlan, J., joined by Stewart and White, JJ., dissenting). The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>majority, however, apparently felt that whatever the <page-number citation-index="1" label="657">*657</page-number>cost to society in terms of fewer convictions of guilty suspects, that cost would simply have to be borne in the interest of enlarged protection for the Fifth Amendment privilege.</p>
<p id="b715-5">The police in this case, in the very act of apprehending a suspect, were confronted with the immediate necessity of ascertaining the whereabouts of a gun which they had every reason to believe the suspect had just removed from his empty holster and discarded in the supermarket. So long as the gun was concealed somewhere in the supermarket, with its actual whereabouts unknown, it obviously posed more than one danger to the public safety: an accomplice might make use of it, a customer or employee might later come upon it.</p>
<p id="b715-6">In such a situation, if the police are required to recite the familiar <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings before asking the whereabouts of the gun, suspects in Quarles’ position might well be deterred from responding. Procedural safeguards which deter a suspect from responding were deemed acceptable in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>in order to protect the Fifth Amendment privilege; when the primary social cost of those added protections is the possibility of fewer convictions, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>majority was willing to bear that cost. Here, had <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings deterred Quarles from responding to Officer Kraft’s question about the whereabouts of the gun, the cost would have been something more than merely the failure to obtain evidence useful in convicting Quarles. Officer Kraft needed an answer to his question not simply to make his case against Quarles but to insure that further danger to the public did not result from the concealment of the gun in a public area.</p>
<p id="b715-7">We conclude that the need for answers to questions in a situation posing a threat to the public safety outweighs the need for the prophylactic rule protecting the Fifth Amendment’s privilege against self-incrimination. We decline to place officers such as Officer Kraft in the untenable position of having to consider, often in a matter of seconds, whether it best serves society for them to ask the necessary questions without the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and render whatever proba<page-number citation-index="1" label="658">*658</page-number>tive evidence they uncover inadmissible, or for them to give the warnings in order to preserve the admissibilty of evidence they might uncover but possibly damage or destroy their ability to obtain that evidence and neutralize the volatile situation confronting them.<footnotemark>7</footnotemark> ■</p>
<p id="b716-5">In recognizing a narrow exception to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule in this case, we acknowledge that to some degree we lessen the desirable clarity of that rule. At least in part in order to preserve its clarity, we have over the years refused to sanction attempts to expand our <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>holding. See, <em>e. g., Minnesota </em>v. <em>Murphy, </em><span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420</a></span> (1984) (refusal to extend <em>Miranda </em>requirements to interviews with probation officers); <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707</a></span> (1979) (refusal to equate request to see a probation officer with request to see a lawyer for <em>Miranda </em>purposes); <em>Beckwith </em>v. <em>United States, </em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341</a></span> (1976) (refusal to extend <em>Miranda </em>requirements to questioning in noncustodial circumstances). As we have in other contexts, we recognize here the importance of a workable rule “to guide police officers, who have only limited time and expertise to reflect on and balance the social and individual interests involved in the specific circumstances they confront.” <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213-214</a></span> (1979). But as we have pointed out, we believe that the exception which we recognize today lessens the necessity of that on-the-scene balancing process. The exception will not be difficult for police officers to apply because in each case it will be circumscribed by the exigency which justifies it. We think police officers can and will distinguish almost in<page-number citation-index="1" label="659">*659</page-number>stinctively between questions necessary to secure their own safety or the safety of the public and questions designed solely to elicit testimonial evidence from a suspect.</p>
<p id="b717-5">The facts of this case clearly demonstrate that distinction and an officer’s ability to recognize it. Officer Kraft asked only the question necessary to locate the missing gun before advising respondent of his rights. It was only after securing the loaded revolver and giving the warnings that he continued with investigatory questions about the ownership and place of purchase of the gun. The exception which we recognize today, far from complicating the thought processes and the on-the-scene judgments of police officers, will simply free them to follow their legitimate instincts when confronting situations presenting a danger to the public safety.<footnotemark>8</footnotemark></p>
<p id="b717-6">We hold that the Court of Appeals in this case erred in excluding the statement, “the gun is over there,” and the gun because of the officer’s failure to read respondent his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights before attempting to locate the weapon. Ac<page-number citation-index="1" label="660">*660</page-number>cordingly we hold that it also erred in excluding the subsequent statements as illegal fruits of a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation.<footnotemark>9</footnotemark> We therefore reverse and remand for further proceedings not inconsistent with this opinion.</p>
<p id="b718-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b709-7"> Although respondent has yet to be tried in state court, the suppression ruling challenged herein is a “final judgment” within the meaning of <span class="citation no-link">28 U. S. C. § 1257</span>(3), and we have jurisdiction over this case. In <em>Cox Broadcasting Corp. </em>v. <em>Cohn, </em><span class="citation" data-id="9426016"><a href="/opinion/109207/cox-broadcasting-corp-v-cohn/#477" aria-description="Citation for case: Cox Broadcasting Corp. v. Cohn">420 U. S. 469, 477</a></span> (1975), we identified four categories of cases where the Court will treat a decision of the highest state court as final for § 1257 purposes even though further proceedings are anticipated in the lower state courts. This ease, which comes to this Court in the same posture as <em>Michigan </em>v. <em>Clifford, </em><span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287</a></span> (1984), decided earlier this Term, falls within the category which includes “those situations where the federal claim has been finally decided . . . but in which later review of the federal issue cannot be had, whatever the ultimate outcome of the case.” <span class="citation" data-id="9426016"><a href="/opinion/109207/cox-broadcasting-corp-v-cohn/#481" aria-description="Citation for case: Cox Broadcasting Corp. v. Cohn">420 U. S., at 481</a></span>. In this case should the State convict respondent at trial, its claim that certain evidence was wrongfully suppressed will be moot. Should respondent be acquitted at trial, the State will be precluded from pressing its federal claim again on appeal. See <em>California </em>v. <em>Stewart, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#498" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 498, n. 71</a></span> (1966) (decided with <em>Miranda </em>v. <em>Arizona).</em></p>
</footnote>
<footnote label="2">
<p id="b710-8"> The State originally charged respondent with rape, but the record provides no information as to why the State failed to pursue that charge.</p>
</footnote>
<footnote label="3">
<p id="Aq9"> We have long recognized an exigent-circumstances exception to the warrant requirement in the Fourth Amendment context. See, <em>e. g., Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#509" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 509</a></span> (1978); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-300</a></span> (1967); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14-15</a></span> (1948). We have found the warrant requirement of the Fourth Amendment inapplicable in cases where the “ ‘exigencies of the situation’ make the needs of law enforcement so compelling that the warrantless search is objectively reasonable under the Fourth Amendment.” <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 394</a></span> (1978), quoting <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span> (1948). Although “the Fifth Amendment’s strictures, unlike the Fourth’s, are not removed by showing reasonableness,” <em>Fisher </em>v. <em>United States, </em><span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#400" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 400</a></span> (1976), we conclude today that there are limited circumstances where the judicially imposed strictures of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>are inapplicable.</p>
</footnote>
<footnote label="4">
<p id="b712-7"> <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>on its facts applies to station house questioning, but we have not so limited it in our subsequent cases, often over strong dissent. See, <em>e. g., Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980) (police car); <em>Orozco </em>v. <em>Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324</a></span> (1969) (defendant’s bedroom); <em>Mathis </em>v. <em>United States, </em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968) (prison cell during defendant’s sentence for an unrelated offense); but see <em>Orozco </em>v. <span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/#328" aria-description="Citation for case: Orozco v. Texas"><em>Texas, supra, </em>at 328-331</a></span> (White, J., dissenting).</p>
</footnote>
<footnote label="5">
<p id="b713-7"> The dissent curiously takes us to task for “endors[ing] the introduction of coerced self-incriminating statements in criminal prosecutions,” <em>post, </em>at 674, and for “sanction[ing] <em>sub silentio </em>criminal prosecutions based on compelled self-incriminating statements.” <em>Post, </em>at 686. Of course our decision today does nothing of the kind. As the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court itself recognized, the failure to provide <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings in and of itself does not render a confession involuntary, <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 457</a></span>, and respondent is certainly free on remand to argue that his statement was coerced under traditional due process standards. Today we merely reject the only argument that respondent has raised to support the exclusion of his statement, that the statement must be <em>presumed </em>compelled because of Officer Kraft’s failure to read him his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings.</p>
</footnote>
<footnote label="6">
<p id="b714-6"> Similar approaches have been rejected in other contexts. See <em>Rhode Island </em>v. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><em>Innis, supra, </em>at 301</a></span> (officer’s subjective intent to incriminate not determinative of whether “interrogation” occurred); <em>United States </em>v. <em>Men-denhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554</a></span>, and n. 6 (1980) (opinion of Stewart, J.) (officer’s subjective intent to detain not determinative of whether a “seizure” occurred within the meaning of the Fourth Amendment); <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#236" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 236</a></span>, and n. 7 (1973) (officer’s subjective fear not determinative of necessity for “search incident to arrest” exception to the Fourth Amendment warrant requirement).</p>
</footnote>
<footnote label="7">
<p id="b716-6"> The dissent argues that a public safety exception to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is unnecessary because in every case an officer can simply ask the necessary questions to protect himself or the public, and then the prosecution can decline to introduce any incriminating responses at a subsequent trial. <em>Post, </em>at 686. But absent actual coercion by the officer, there is no constitutional imperative requiring the exclusion of the evidence that results from police inquiry of this kind; and we do not believe that the doctrinal underpinnings of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>require us to exclude the evidence, thus penalizing officers for asking the very questions which are the most crucial to their efforts to protect themselves and the public.</p>
</footnote>
<footnote label="8">
<p id="b717-7"> Although it involves police questions in part relating to the whereabouts of a gun, <em>Orozco </em>v. <em>Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324</a></span> (1969), is in no sense inconsistent with our disposition of this ease. In <em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">Orozco</a></span> </em>four hours after a murder had been committed at a restaurant, four police officers entered the defendant’s boardinghouse and awakened the defendant, who was sleeping in his bedroom. Without giving him <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, they began vigorously to interrogate him about whether he had been present at the scene of the shooting and whether he owned a gun. The defendant eventually admitted that he had been present at the scene and directed the officers to a washing machine in the backroom of the boardinghouse where he had hidden the gun. We held that all the statements should have been suppressed. In <em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">Orozco</a></span>, </em>however, the questions about the gun were clearly investigatory; they did not in any way relate to an objectively reasonable need to protect the police or the public from any immediate danger associated with the weapon. In short there was no exigency requiring immediate action by the officers beyond the normal need expeditiously to solve a serious crime.</p>
<p id="b717-8"><em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980), also involved the whereabouts of a missing weapon, but our holding in that case depended entirely on our conclusion that no police interrogation took place so as to require consideration of the applicability of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>prophylactic.</p>
</footnote>
<footnote label="9">
<p id="b718-8"> Because we hold that there is no violation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>in this case, we have no occasion to reach arguments made by the State and the United States as <em>amicus curiae </em>that the gun is admissible either because it is nontestimonial or because the police would inevitably have discovered it absent their questioning.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Newman v. Underhill.json  (`lake-record`, 5 assertions)

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
{"assertion_id": "8326daa1b52769fb", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Newman v. Underhill"}, "payload": {"all": [{"cite": "134 F.4th 1025", "page": "1025", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "134"}], "display": "134 F.4th 1025", "official": {"cite": "134 F.4th 1025", "page": "1025", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "134"}, "official_selection_present": true, "record_id": "Newman v. Underhill"}}
{"assertion_id": "2751cf88d8ed727b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op13", "record_id": "Newman v. Underhill"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op13", "pinpoint_status": "slip-only", "quote": "[T]he nine-minute 'pause' identified by Plaintiff is far shorter than the 30-minute period", "quote_fidelity": "mismatch", "record_id": "Newman v. Underhill", "star_marker": null}}
{"assertion_id": "9ae1fe4d3b9bdc90", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op12", "record_id": "Newman v. Underhill"}, "payload": {"fragment": "#:~:text=delay%5Bs%5D%2C%20but%20%5Bdoes%5D%20not%20br%5Beak%5D%2C", "page": null, "pin_id": "pin-op12", "pinpoint_status": "slip-only", "quote": "delay[s], but [does] not br[eak],", "quote_fidelity": "matched", "record_id": "Newman v. Underhill", "star_marker": null}}
{"assertion_id": "b64acd9869f8868c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op10", "record_id": "Newman v. Underhill"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op10", "pinpoint_status": "slip-only", "quote": "--- # Newman v. Underhill *134 F.4th 1025 (9th Cir. 2025)* · U.S. Court of Appeals, 9th Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Deputy Underhill of the San Bernardino County Sheriff's Department tried to stop a black Chevy Silverado with an expired registration and an unilluminated license plate. The driver — later identified as Richard Delacruz — failed to yield and fled, and Underhill immediately pursued. Delacruz abandoned his truck on a dead-end street and ran on foot; Underhill followed, then lost sight of him near Michael Newman's home and decided to wait for backup before entering. Roughly nine minutes after losing sight of Delacruz, and after searching the backyard, announcing the deputies' presence, and coordinating with other officers (including a helicopter), Underhill entered Newman's home without a warrant and found Delacruz, who was Newman's roommate. Newman sued the deputies under 42 U.S.C. § 1983, alleging the warrantless entry violated the Fourth Amendment; the district court granted summary judgment to the deputies on the hot-pursuit exception. ## Issue Whether the warrantless entry into Newman's home was justified by the hot-pursuit exception, where about nine minutes elapsed between the deputy's losing sight of the fleeing suspect and his entry into the home. ## Rule To invoke the hot-pursuit exception, officers must show (A) probable cause to search the home and (B) exigent circumstances — the pursuit of a fleeing suspect — justifying the warrantless intrusion. The underlying principle is that", "quote_fidelity": "mismatch", "record_id": "Newman v. Underhill", "star_marker": null}}
{"assertion_id": "7b64f7e977612f54", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Newman v. Underhill"}, "payload": {"as_of_content": "2025-04-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Newman v. Underhill", "scope_note": "Good law; recent (decided 2025-04-23). Illustrates the continuity-of-pursuit requirement — a nine-minute gap delayed but did not break a hot pursuit.", "varies_by_point": false}}
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
